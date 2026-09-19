import { useState } from 'react'
import { plan, type Item, type Accent } from '../lib/plan'

function Tick({ on, onClick, label }: { on: boolean; onClick: () => void; label: string }) {
  return (
    <button type="button" className={on ? 'tick on' : 'tick'} onClick={onClick} aria-pressed={on} aria-label={label}>
      <span>
        {on && (
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#121211" strokeWidth="3.4" strokeLinecap="round" strokeLinejoin="round">
            <path d="M20 6L9 17l-5-5" />
          </svg>
        )}
      </span>
    </button>
  )
}

export default function ExerciseRow({
  item,
  accent,
  emphasis,
  done,
  onToggle,
}: {
  item: Item
  accent: Accent
  emphasis: boolean
  done: boolean
  onToggle: () => void
}) {
  const [open, setOpen] = useState(false)
  const ex = item.exid ? plan.exercises[item.exid] : undefined

  // A "Note" row is a standing instruction for the day, not something you tick off.
  if (item.cat === 'Note') {
    return (
      <div className="notebox">
        <h3 style={{ margin: '0 0 6px 0', fontFamily: 'var(--display)', fontSize: 11, letterSpacing: 2, color: 'var(--orange)' }}>
          {item.name}
        </h3>
        <p>{item.note}</p>
      </div>
    )
  }

  const rx = [item.sets, item.reps].filter(Boolean).join(' × ')

  return (
    <div className={['row', emphasis ? 'is-key' : '', done ? 'is-done' : ''].filter(Boolean).join(' ')}>
      <div className="row-main">
        <Tick on={done} onClick={onToggle} label={`Mark ${item.name} done`} />
        <button type="button" className="row-open" onClick={() => setOpen(!open)} aria-expanded={open}>
          <span className="row-line">
            <span className="row-name">{item.name}</span>
            {rx && <span className={`row-rx accent-${accent}`}>{rx}</span>}
          </span>
          {item.note && <span className="row-note" style={{ display: 'block' }}>{item.note}</span>}
          <span className="row-sub">
            {item.load && <span className={`pill bg-${accent}`}>{item.load}</span>}
            {item.rest && <span>rest {item.rest}</span>}
            {item.exid && <span>{item.exid}</span>}
            {item.contacts > 0 && <span>{item.contacts} contacts</span>}
            {item.km > 0 && <span>{item.km} km</span>}
          </span>
        </button>
      </div>

      {open && ex && (
        <div className="detail">
          <h3>Targets</h3>
          <div className="chips">
            {ex.targets.split(',').map((t) => (
              <span className="chip" key={t}>{t.trim()}</span>
            ))}
          </div>
          <h3 style={{ marginTop: 16 }}>How to perform</h3>
          <p>{ex.how}</p>
          {ex.caution && (
            <div className="caution">
              <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#e07a4f" strokeWidth="1.9" strokeLinecap="round" style={{ flex: '0 0 auto', marginTop: 2 }}>
                <path d="M12 9v5M12 17.5v.01" />
                <path d="M10.3 3.9L2.4 17.2A2 2 0 004.1 20.2h15.8a2 2 0 001.7-3L13.7 3.9a2 2 0 00-3.4 0z" />
              </svg>
              <div>
                <h3>Caution</h3>
                <p>{ex.caution}</p>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  )
}
