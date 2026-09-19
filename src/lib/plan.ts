import raw from '../data/plan.json'

export type Item = {
  exid: string
  name: string
  cat: string
  sets: string
  reps: string
  rest: string
  load: string
  note: string
  km: number
  contacts: number
}

export type Section = {
  title: string
  accent: Accent
  items: Item[]
}

export type Accent = 'orange' | 'teal' | 'olive' | 'grey' | 'red' | 'text'

export type Day = {
  date: string
  dow: string
  week: number
  block: number
  blockName: string
  focus: string
  accent: Accent
  label: string
  location: string
  km: number
  contacts: number
  sections: Section[]
}

export type Exercise = {
  name: string
  cat: string
  targets: string
  how: string
  rx: string
  caution: string
}

export type Plan = {
  meta: {
    title: string
    start: string
    end: string
    weeks: number
    race: { name: string; date: string; goal: string; pace: string }
    travel: { from: string; to: string }
    generated: string
  }
  exercises: Record<string, Exercise>
  days: Day[]
}

export const plan = raw as unknown as Plan

const index = new Map(plan.days.map((d) => [d.date, d]))

/** Plan days are plain YYYY-MM-DD strings, never timestamps, so nothing shifts across time zones. */
export function todayKey(): string {
  const n = new Date()
  const p = (v: number) => String(v).padStart(2, '0')
  return `${n.getFullYear()}-${p(n.getMonth() + 1)}-${p(n.getDate())}`
}

export function getDay(date: string): Day | undefined {
  return index.get(date)
}

/** Clamps to the plan window, so the arrows never walk off the end. */
export function shiftDate(date: string, delta: number): string {
  const i = plan.days.findIndex((d) => d.date === date)
  if (i < 0) return date
  const next = Math.min(Math.max(i + delta, 0), plan.days.length - 1)
  return plan.days[next].date
}

/** The plan day to open on: today if it is in the block, otherwise the nearest end. */
export function openingDate(): string {
  const t = todayKey()
  if (index.has(t)) return t
  return t < plan.meta.start ? plan.meta.start : plan.meta.end
}

export function weekDays(week: number): Day[] {
  return plan.days.filter((d) => d.week === week)
}

export function daysUntilRace(from: string): number {
  const a = Date.parse(from + 'T00:00:00Z')
  const b = Date.parse(plan.meta.race.date + 'T00:00:00Z')
  return Math.round((b - a) / 86400000)
}

export function fmtLong(date: string): { dow: string; dm: string } {
  const [y, m, d] = date.split('-').map(Number)
  const dt = new Date(Date.UTC(y, m - 1, d))
  return {
    dow: dt.toLocaleDateString('en-GB', { weekday: 'long', timeZone: 'UTC' }).toUpperCase(),
    dm: dt.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', timeZone: 'UTC' }),
  }
}

export function fmtShort(date: string): { dow: string; d: string } {
  const [y, m, d] = date.split('-').map(Number)
  const dt = new Date(Date.UTC(y, m - 1, d))
  return {
    dow: dt.toLocaleDateString('en-GB', { weekday: 'short', timeZone: 'UTC' }).toUpperCase(),
    d: String(d),
  }
}
