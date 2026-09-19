import { useEffect, useMemo, useState } from 'react'
import { plan, getDay, openingDate, shiftDate, weekDays, daysUntilRace, fmtLong, fmtShort, todayKey } from './lib/plan'
import { load, save, exportProgress, emptyProgress, type Progress } from './lib/db'
import Section from './components/Section'

export default function App() {
  const [date, setDate] = useState<string>(openingDate)
  const [progress, setProgress] = useState<Progress>(emptyProgress)
  const [ready, setReady] = useState(false)

  useEffect(() => {
    load().then((p) => {
      setProgress(p)
      setReady(true)
    })
  }, [])

  useEffect(() => {
    if (ready) save(progress)
  }, [progress, ready])

  const day = getDay(date)
  const strip = useMemo(() => (day ? weekDays(day.week) : []), [day])

  const total = useMemo(
    () => (day ? day.sections.reduce((a, s) => a + s.items.filter((i) => i.cat !== 'Note').length, 0) : 0),
    [day]
  )
  const ticks = progress.items[date] ?? {}
  const doneCount = Object.values(ticks).filter(Boolean).length
  const dayDone = !!progress.days[date]

  function toggleItem(key: string) {
    setProgress((p) => {
      const forDay = { ...(p.items[date] ?? {}) }
      if (forDay[key]) delete forDay[key]
      else forDay[key] = true
      return { ...p, items: { ...p.items, [date]: forDay } }
    })
  }

  function toggleDay() {
    setProgress((p) => {
      const days = { ...p.days }
      if (days[date]) delete days[date]
      else days[date] = true
      return { ...p, days }
    })
  }

  if (!day) {
    return (
      <div className="app">
        <p className="empty">
          {date} is outside the block ({plan.meta.start} to {plan.meta.end}).
        </p>
      </div>
    )
  }

  const { dow, dm } = fmtLong(date)
  const atStart = date === plan.meta.start
  const atEnd = date === plan.meta.end
  const isToday = date === todayKey()
  const todayInBlock = !!getDay(todayKey())
  const toRace = daysUntilRace(date)

  return (
    <div className="app">
      <header className="topbar">
        <div className="topbar-row">
          <button
            type="button" className="iconbtn" aria-label="Previous day" disabled={atStart}
            onClick={() => setDate(shiftDate(date, -1))}
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#a3a099" strokeWidth="2" strokeLinecap="round">
              <path d="M15 6l-6 6 6 6" />
            </svg>
          </button>

          <div>
            {!isToday && todayInBlock && (
              <button type="button" className="todaychip" onClick={() => setDate(todayKey())}>
                JUMP TO TODAY
              </button>
            )}
            <div className="blockline">
              WEEK {day.week} · BLOCK {day.block} · {day.blockName.toUpperCase()}
            </div>
            <div className="dateline">
              <span className="dow">{dow}</span>
              <span className="dm">{dm}</span>
            </div>
          </div>

          <button
            type="button" className="iconbtn" aria-label="Next day" disabled={atEnd}
            onClick={() => setDate(shiftDate(date, 1))}
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#a3a099" strokeWidth="2" strokeLinecap="round">
              <path d="M9 6l6 6-6 6" />
            </svg>
          </button>
        </div>

        <nav className="strip" aria-label="This week">
          {strip.map((d) => {
            const done = !!progress.days[d.date]
            return (
              <button
                key={d.date} type="button"
                className={['strip-day', d.date === date ? 'is-current' : '', done ? 'is-done' : ''].filter(Boolean).join(' ')}
                onClick={() => setDate(d.date)}
                aria-current={d.date === date ? 'date' : undefined}
                aria-label={`${d.dow} ${d.date}, ${d.label}`}
              >
                <span className="strip-dow">{fmtShort(d.date).dow}</span>
                <span className="strip-num">{fmtShort(d.date).d}</span>
                <span className={`strip-dot accent-${d.accent}${done ? ' is-filled' : ''}`} />
              </button>
            )
          })}
        </nav>
      </header>

      <section className="session">
        <div className="session-title">
          <span className={`dot bg-${day.accent}`} />
          <h1>{day.label.toUpperCase()}</h1>
        </div>
        <div className="session-meta">
          <span>{day.location}</span>
          {day.km > 0 && <span>{day.km} km</span>}
          {day.contacts > 0 && <span>{day.contacts} contacts</span>}
          {toRace > 0 && toRace <= 21 && <span className="accent-red">{toRace}d to race</span>}
        </div>
        {total > 0 && (
          <>
            <div className="bar">
              <i className={`bg-${day.accent}`} style={{ width: `${Math.round((doneCount / total) * 100)}%` }} />
            </div>
            <div className="bar-label">
              {doneCount} of {total} done
            </div>
          </>
        )}
      </section>

      {day.sections.map((s, i) => (
        <Section
          key={`${date}-${i}`}
          section={s}
          sectionIdx={i}
          isDone={(k) => !!ticks[k]}
          onToggle={toggleItem}
        />
      ))}

      <div style={{ margin: '28px 16px 0 16px', display: 'flex', justifyContent: 'center' }}>
        <button
          type="button"
          onClick={() => exportProgress(progress)}
          style={{ background: 'none', border: 'none', color: 'var(--dim)', fontSize: 12, padding: 12 }}
        >
          Export progress
        </button>
      </div>

      <footer className="footer">
        <div className="footer-inner">
          <button type="button" className={dayDone ? 'cta done' : 'cta'} onClick={toggleDay}>
            {dayDone ? 'DAY COMPLETE' : 'MARK DAY DONE'}
          </button>
        </div>
      </footer>
    </div>
  )
}
