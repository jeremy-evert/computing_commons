# Prompt 006 — Grace full-page visual capture depth repair

## Mission

Act as Luna on **Grace** and repair one specific defect in the current Computing Commons visual-review capture prototype without changing course content.

The current published visual-review session is:

- commit: `b36354c3557a096f4c2811652ad42f9be59621c8`
- evidence: `sidecar/visual-review/grace/2026-08-23_221446/`
- Savnac course: `18`

The batch successfully visited the intended 18 routes and the manifest shows requested URL = rendered URL for every target. That part is accepted.

However, every captured PNG is reported as exactly **1920 x 911**, including long Week 2 content pages. The current helper claims to capture the entire rendered page beyond the viewport, but this evidence does not prove that below-fold Canvas content is actually being captured. Treat this as a **REPAIR** finding in the visual-review pipeline.

## Scope

Writable repository:

`J:\git\computing_commons`

Target host:

**Grace / Windows / PowerShell 7**

Authorized live surface:

Read-only browser interaction with Savnac course 18 through the existing dedicated capture browser and tunnel.

Do not modify Canvas content, assignments, grades, enrollments, settings, credentials, or production SWOSU Canvas.

## Required reading

Read:

- `AGENTS.md`
- `scripts/grace/README.md`
- `scripts/grace/start-savnac-capture-browser.ps1`
- `scripts/grace/capture-canvas-full-page.ps1`
- `scripts/grace/capture-computing-commons-set.ps1`
- `sidecar/visual-review/grace/2026-08-23_221446/manifest.json`

Also read the current Course Foundry plan if the checkout is locally available:

`course_foundry/planning/visual-review-pipeline.md`

The eventual generalized implementation belongs in Course Foundry, but this mission is only to prove and minimally repair the working prototype on Grace so Foundry has reliable behavior to promote.

## Investigation

Determine why every capture reports the viewport-sized height.

At minimum measure and compare, after the normal 5-second settle:

- browser viewport width/height;
- `document.documentElement.scrollWidth` / `scrollHeight`;
- `document.body.scrollWidth` / `scrollHeight`;
- CDP `Page.getLayoutMetrics` content dimensions;
- the dimensions and overflow behavior of the Canvas element that actually scrolls, if Canvas uses an internal scroll container.

Do not assume the browser document itself is the scrolling surface.

## Repair requirement

Make the smallest robust change that produces a complete visual capture of the rendered Canvas content.

Acceptable approaches include:

- correctly capturing the actual full document when that is the true scroll surface;
- temporarily expanding an internal Canvas scroll container for capture and restoring it afterward;
- another bounded CDP/DOM technique that demonstrably captures the entire student-facing content.

Do not turn this into a large Selenium/Playwright framework.

Preserve:

- the dedicated browser profile;
- current authentication/session behavior;
- the 5-second settle default;
- existing course-specific batch flow;
- guarded `-Publish` behavior.

## Evidence contract improvement

The capture result and batch manifest should record enough information to prove capture completeness rather than merely claim it.

At minimum record fields equivalent to:

- viewport width/height;
- measured rendered-content width/height;
- actual PNG width/height;
- capture completeness verdict or check;
- if an internal scroll container is used, its selector/description and measured scroll height.

If the helper cannot prove that the PNG covers the measured rendered content, it must clearly fail or mark the capture incomplete rather than silently call it full-page.

## Acceptance test

Use at least:

1. a short page;
2. one known long Week 2 page, preferably `Week 2 — Three tiny Aider wins` or `Week 2 — Bridge to Work First`;
3. the Modules page.

Prove that long content produces evidence taller than the viewport when appropriate, or otherwise demonstrate with measured scroll-container evidence that the complete visual content was captured.

Then run the full configured 18-target batch and publish a fresh session only if the checkout was clean before the run.

Do not ask Jeremy to inspect all 18 pages manually.

## Report

Write a concise report under:

`sidecar/reports/luna/006_grace_full_page_capture_depth_repair.md`

Include:

- root cause;
- files changed;
- before/after dimensions for the selected long page;
- completeness checks added;
- fresh visual-review session path and commit SHA if published;
- confirmation no Canvas mutation occurred;
- any behavior that should be carried into Course Foundry Prompt 140.

Final sentinel:

`GRACE FULL-PAGE CAPTURE PROVEN — PIPER REVIEW READY`
