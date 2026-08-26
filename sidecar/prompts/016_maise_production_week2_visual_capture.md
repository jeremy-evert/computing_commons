# Prompt 016: Maise production Week 2 visual capture

## Context

Flo just published live changes to SWOSU Canvas, Computing Commons (course
`24298`), module `02 -- Week 2: Build and Verify Local AI` (module id
`218816`):

* a new landing page, `Week 2 -- Start Here`, at the top of the module;
* ten new file items (Day 1 slides PPTX/PDF, field guide, session notes,
  Jeremy's own field notes on what broke, the actual setup script, and both
  run receipts -- the CUDA failure and the fixed rerun).

This is real production content students are looking at today. It needs a
human-eyeball visual pass (tint/crop/contrast, broken embeds, awkward file
previews) the same way the existing Grace loop does for Savnac staging --
see `scripts/grace/README.md` and
`sidecar/prompts/004_grace_visual_dogfood_capture_loop.md` /
`sidecar/prompts/006_grace_full_page_capture_depth_repair.md` for the
established pattern. This prompt is the same trick, run from `maise`
(Jeremy's Linux box) instead of `Grace` (Windows), pointed at the live
production course instead of the Savnac tunnel.

A new script for this already exists:
`scripts/grace/capture-maise-production-week2.ps1`. It reuses the existing,
OS-portable `scripts/grace/capture-canvas-full-page.ps1` (pure .NET
ClientWebSocket + Chrome DevTools Protocol -- no Windows-only APIs) and
targets `https://swosu.instructure.com/courses/24298/...` directly. Read
both scripts before running anything.

## Owner's manual step (already handled outside this job)

Jeremy will start a Chromium/Chrome browser on `maise` by hand with:

```bash
google-chrome --remote-debugging-port=9222 --user-data-dir="$HOME/.cache/computing-commons-capture-profile" --no-first-run --no-default-browser-check https://swosu.instructure.com/courses/24298/modules
```

(or `chromium` / `chromium-browser`, whichever exists on this machine), and
will log into Canvas once by hand in that window. That window must stay
open and logged in for the duration of this job. Do not attempt to automate
or script around the SSO login yourself -- if the browser is not there or
not logged in, stop and report that gate rather than trying to log in
programmatically.

## Your job

1. Confirm `pwsh` (PowerShell 7) is available on this machine. If not,
   report that as a blocking gate -- do not attempt to port the scripts to
   Python/Node under time pressure; ask first.
2. Confirm a browser is listening on `127.0.0.1:9222`
   (`curl -s http://127.0.0.1:9222/json/version`) and that the open tab is
   actually on `swosu.instructure.com` and logged in (not a Canvas login
   page). If not, stop and report -- this is Jeremy's manual step to fix,
   not yours.
3. From a clean `computing_commons` checkout on `main`
   (`/mnt/nora/git/computing_commons` or wherever it lives on this
   machine), pull latest.
4. Run:

   ```powershell
   pwsh -File ./scripts/grace/capture-maise-production-week2.ps1
   ```

   without `-Publish` first. Confirm all 26 targets captured (module index,
   15 pages, 10 files) and that none of the screenshots show a Canvas login
   page, a 404, or an obviously broken render.
5. If everything looks like real rendered content, rerun with `-Publish` so
   it commits and pushes the capture set (under
   `sidecar/visual-review/maise/<timestamp>/`) to `origin main`. The script
   refuses to publish from a dirty checkout or a non-`main` branch -- do not
   work around that refusal.
6. This is read-only against Canvas. Do not click into edit mode, do not
   change any course content, grades, or enrollments from the capture
   browser.

## Report back

* the commit SHA that was pushed;
* the path to the manifest;
* anything that looked visually wrong (broken embed, ugly file-preview
  chrome, cut-off content) so Flo can decide what to repair;
* whether every one of the 26 targets rendered as real logged-in Canvas
  content (not a login page).

## Final sentinel

```text
MAISE PRODUCTION WEEK 2 VISUAL CAPTURE COMPLETE
```

If blocked (no pwsh, no browser on 9222, not logged in, dirty checkout that
isn't yours to touch), stop and report the exact gate instead of working
around it.
