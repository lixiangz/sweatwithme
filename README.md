# Hybrid Block

A phone-first view of the 13-week hybrid training plan (21 Sep – 20 Dec 2026).
One screen: what to do today. Logging stays in Hevy.

## Run it

```bash
npm install
npm run dev      # http://localhost:5173
npm run build    # -> dist/
```

## Deploy (free)

**Cloudflare Pages** or **Vercel** — both detect Vite automatically.

```bash
npx vercel --prod          # or: npx wrangler pages deploy dist
```

Build command `npm run build`, output directory `dist`. No server, no database,
no environment variables.

**Then add it to your home screen.** iOS Safari evicts storage for sites you
have not opened in 7 days, and installed PWAs are exempt. Three weeks in Asia
without installing it and your progress is gone.

## How it is put together

- `src/data/plan.json` — the whole plan, generated from the spreadsheet by
  `tools/gen_plan_json.py`. Committed on purpose: it ships in the bundle, so the app works
  offline after the first load. Edit the plan by regenerating this file.
- `src/lib/plan.ts` — types and date helpers. Plan days are plain `YYYY-MM-DD`
  strings, never timestamps, so nothing shifts when you cross time zones.
- `src/lib/db.ts` — progress in IndexedDB. Two things are stored: which days are
  done, and which items are ticked. Nothing else.
- `src/App.tsx` — the day view, week strip, progress bar.
- `src/components/Section.tsx` — one block of the session. Warm-up, cool-down and
  mobility sections start folded.
- `src/components/ExerciseRow.tsx` — a row; tapping it opens how-to and cautions.

## Backup

"Export progress" at the bottom of the page downloads a JSON file. There is no
import yet — if you need one, it is about ten lines in `db.ts`.

## Not built yet

Week view, 13-week overview, and the "adjust today" swap flow are designed but
not implemented. The swap flow needs a decision first: whether plan days are
anchored to dates or to a sequence.
