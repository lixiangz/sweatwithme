# CLAUDE.md

## Deploy

This repo is linked to a Vercel project. **Pushing to `main` deploys it** — there
is no separate deploy step and no CLI to run. To ship a change: commit, push to
`main`, wait for the Vercel build.

Note the repo root is `hybrid-app/`, not the parent `sweatwithme/` directory.

## Testing on iPhone

The app is used as a home-screen PWA, so anything layout-related has to be
checked there, not in Safari as a tab. Standalone mode differs in two ways that
matter:

- `apple-mobile-web-app-status-bar-style: black-translucent` + `viewport-fit=cover`
  put the web view under the status bar, so `env(safe-area-inset-*)` is non-zero
  (it is ~0 in a Safari tab). Safe-area padding belongs on `.topbar` and
  `.footer` only — they are the sticky/fixed elements against the edges.
  Applying it on `:root` as well double-counts the notch.
- The service worker (`vite-plugin-pwa`, `registerType: 'autoUpdate'`) serves the
  cached build. After a deploy, close and reopen the app so the new worker takes
  over; a visible-looking "no change" is usually a stale cache, not a broken fix.

Everything else — architecture, the plan data pipeline, what is not built yet —
is in `README.md`.
