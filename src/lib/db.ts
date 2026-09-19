/**
 * Progress lives in IndexedDB rather than localStorage: Safari evicts both for
 * sites you have not opened in 7 days, but an installed PWA is exempt, and
 * IndexedDB survives a lot more than localStorage does when storage gets tight.
 * Export is the real backup - see exportProgress().
 */

const DB = 'hybrid-block'
const STORE = 'progress'
const KEY = 'v1'

export type Progress = {
  /** date -> the whole day is done */
  days: Record<string, boolean>
  /** date -> "sectionIdx:itemIdx" -> ticked */
  items: Record<string, Record<string, boolean>>
}

const empty: Progress = { days: {}, items: {} }

function open(): Promise<IDBDatabase> {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(DB, 1)
    req.onupgradeneeded = () => {
      if (!req.result.objectStoreNames.contains(STORE)) req.result.createObjectStore(STORE)
    }
    req.onsuccess = () => resolve(req.result)
    req.onerror = () => reject(req.error)
  })
}

export async function load(): Promise<Progress> {
  try {
    const db = await open()
    return await new Promise((resolve, reject) => {
      const req = db.transaction(STORE, 'readonly').objectStore(STORE).get(KEY)
      req.onsuccess = () => resolve((req.result as Progress) ?? empty)
      req.onerror = () => reject(req.error)
    })
  } catch {
    return empty
  }
}

export async function save(p: Progress): Promise<void> {
  try {
    const db = await open()
    await new Promise<void>((resolve, reject) => {
      const tx = db.transaction(STORE, 'readwrite')
      tx.objectStore(STORE).put(p, KEY)
      tx.oncomplete = () => resolve()
      tx.onerror = () => reject(tx.error)
    })
  } catch {
    /* storage refused; the session still works, it just will not persist */
  }
}

export function exportProgress(p: Progress) {
  const blob = new Blob([JSON.stringify(p, null, 2)], { type: 'application/json' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `hybrid-progress-${new Date().toISOString().slice(0, 10)}.json`
  a.click()
  URL.revokeObjectURL(url)
}

export { empty as emptyProgress }
