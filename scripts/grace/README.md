# Grace visual review loop

Purpose: make Jeremy's Savnac visual inspection fast enough that the human spends time judging the course instead of manually stitching screenshots.

This loop uses a **dedicated Chrome/Edge profile** on Grace with Chrome DevTools enabled locally. It does not require Playwright, Selenium, Node, or a browser extension.

## 1. Start the dedicated capture browser

From the `computing_commons` checkout on Grace:

```powershell
pwsh -File .\scripts\grace\start-savnac-capture-browser.ps1
```

The default target is Savnac course 18 through the existing local tunnel:

`http://localhost:3002/courses/18`

Log into Savnac once in this dedicated browser window. Its local profile is stored under `%LOCALAPPDATA%\ComputingCommonsCapture\ChromeProfile`, outside Git.

Keep this browser open while reviewing pages.

## 2. Capture whatever page is currently visible

Navigate normally in the dedicated browser, then run:

```powershell
pwsh -File .\scripts\grace\capture-canvas-full-page.ps1
```

The script attaches to the local browser debugging port, captures the **entire rendered page** beyond the viewport, and writes a PNG under:

`sidecar/visual-review/grace/<date>/`

It captures rendered Canvas content only. It does not include the Windows taskbar or browser tabs/chrome.

You can also provide a specific URL and output path:

```powershell
pwsh -File .\scripts\grace\capture-canvas-full-page.ps1 `
  -Url 'http://localhost:3002/courses/18/pages/recitation-slash-get-help' `
  -OutputPath '.\sidecar\visual-review\grace\recitation.png'
```

## 3. Capture the whole current Commons review set

Once the dedicated browser is logged in:

```powershell
pwsh -File .\scripts\grace\capture-computing-commons-set.ps1
```

This currently captures:

1. Modules
2. Success Foundations / Semester Kickoff
3. Recitation / Get Help
4. Week 2 Local AI Lab
5. Week 2 Verify the Tools
6. Week 2 Recovery with Evidence

The script writes PNGs plus a `manifest.json` and a small `README.md` for the session.

## 4. Publish the capture set to GitHub main

When the Grace checkout is clean and on `main`:

```powershell
pwsh -File .\scripts\grace\capture-computing-commons-set.ps1 -Publish
```

`-Publish` deliberately refuses to run when:

- the current branch is not `main`; or
- unrelated uncommitted changes already exist.

If clean, it stages only the new visual-review session, commits it, and pushes `origin main`.

## Human + Luna workflow

The useful loop is:

**Luna builds in Savnac -> Jeremy navigates on Grace -> script captures -> Jeremy/Piper judge -> Luna repairs -> capture again.**

The capture scripts are evidence plumbing. They do not modify Canvas content, enrollments, grades, or Savnac infrastructure.

## Troubleshooting

If the capture script says no browser is listening on port 9222, rerun `start-savnac-capture-browser.ps1`.

If Savnac shows a login page in the screenshot, sign in once in the dedicated browser profile and capture again.

If port 3002 is unavailable, restore the existing Grace-to-Savnac tunnel first. These scripts intentionally do not mutate networking or create alternate access paths.
# Owner review helpers

From a clean `computing_commons` checkout on Grace, run:

```powershell
.\scripts\grace\review-week2-slides.ps1
```

The helper refuses a dirty checkout, confirms both PDFs exist, prints the current commit and paths, and opens the projected deck and instructor notes. Pull or sync the checkout before running it.
