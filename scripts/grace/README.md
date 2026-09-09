# Grace visual review loop

Purpose: make Jeremy's visual inspection of the live production course fast
enough that the human spends time judging the course instead of manually
stitching screenshots.

This loop uses a **dedicated Chrome/Edge profile** on Grace with Chrome
DevTools enabled locally. It does not require Playwright, Selenium, Node, or
a browser extension.

(The earlier Savnac-staging-tunnel version of this loop — its dedicated
capture browser launcher and the course-18-hardwired capture set script —
moved to `course_foundry` along with the rest of that tuning/refining
history; this README now documents what's left, which targets the real
production course directly.)

## 1. Capture the current production Week 2 review set

```powershell
pwsh -File .\scripts\grace\capture-maise-production-week2.ps1
```

Targets `https://swosu.instructure.com/courses/24298` (the live Computing
Commons course) directly — not a staging tunnel. Writes PNGs under
`sidecar/visual-review/maise/<date>/` plus a manifest and README for the
session.

## 2. Capture whatever page is currently visible

With a dedicated capture browser open and Chrome DevTools debugging enabled
locally (port 9222), navigate normally, then run:

```powershell
pwsh -File .\scripts\grace\capture-canvas-full-page.ps1
```

The script attaches to the local browser debugging port, captures the
**entire rendered page** beyond the viewport, and writes a PNG under
`sidecar/visual-review/grace/<date>/`. It captures rendered Canvas content
only — no Windows taskbar or browser tabs/chrome.

You can also provide a specific URL and output path:

```powershell
pwsh -File .\scripts\grace\capture-canvas-full-page.ps1 `
  -Url 'https://swosu.instructure.com/courses/24298/pages/recitation-slash-get-help' `
  -OutputPath '.\sidecar\visual-review\grace\recitation.png'
```

## Human review workflow

The useful loop is now:

**Build/repair in `computing_commons` -> deploy to production Canvas ->
Jeremy navigates on Grace -> script captures -> judge -> repair -> repeat.**

The capture scripts are evidence plumbing. They do not modify Canvas
content, enrollments, or grades.

## Owner review helpers

From a clean `computing_commons` checkout on Grace, run:

```powershell
.\scripts\grace\review-week2-slides.ps1
```

The helper refuses a dirty checkout, confirms both PDFs exist, prints the
current commit and paths, and opens the projected deck and instructor
notes. Pull or sync the checkout before running it.
