import { useState } from 'react'
import type { Section as SectionType } from '../lib/plan'
import ExerciseRow from './ExerciseRow'

/** Warm-up and cool-down start folded away: at 6am you want the main work first. */
const FOLDED = new Set(['Warm-up', 'Cool-down', 'Mobility'])

export default function Section({
  section,
  sectionIdx,
  isDone,
  onToggle,
}: {
  section: SectionType
  sectionIdx: number
  isDone: (key: string) => boolean
  onToggle: (key: string) => void
}) {
  const [open, setOpen] = useState(!FOLDED.has(section.title))
  const doneCount = section.items.filter((_, i) => isDone(`${sectionIdx}:${i}`)).length
  const contacts = section.items.reduce((a, b) => a + b.contacts, 0)
  const km = section.items.reduce((a, b) => a + b.km, 0)

  const tail = contacts > 0 ? `${contacts} contacts` : km > 0 ? `${km.toFixed(1)} km` : `${section.items.length} items`

  return (
    <>
      <button type="button" className="sec-head" onClick={() => setOpen(!open)} aria-expanded={open}>
        <span className={`sec-title accent-${section.accent}`}>{section.title.toUpperCase()}</span>
        <span className="rule" />
        <span className="sec-count">
          {doneCount > 0 && `${doneCount}/${section.items.length} · `}
          {tail}
        </span>
        <svg
          width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#7a7770" strokeWidth="2.2" strokeLinecap="round"
          style={{ flex: '0 0 auto', transform: open ? 'rotate(90deg)' : 'none', transition: 'transform 160ms ease' }}
        >
          <path d="M9 6l6 6-6 6" />
        </svg>
      </button>

      {open && (
        <div className="sec-body">
          {section.items.map((item, i) => (
            <ExerciseRow
              key={`${sectionIdx}:${i}`}
              item={item}
              accent={section.accent}
              emphasis={section.title === 'Strength' && i === 0}
              done={isDone(`${sectionIdx}:${i}`)}
              onToggle={() => onToggle(`${sectionIdx}:${i}`)}
            />
          ))}
        </div>
      )}
    </>
  )
}
