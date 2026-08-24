# Prompt 014 — Brandy teacher-only submission / feedback loop

## Mission

Act as Luna on **Brandy** and build the first usable **Teacher Submission** loop for Computing Commons.

Jeremy wants to be able to read any Savnac Computing Commons page in his dedicated Grace teacher/review browser, click one small **Teacher Submission** button, type what he likes/does not like/needs changed, and create a durable feedback receipt that is visible to Jeremy and authorized tools but not to students.

Do **not** implement this as student-facing Canvas HTML. The control must be teacher-side tooling only.

This mission builds the reusable mechanism and leaves it ready for one-command Grace dogfood.

## Core user experience

While Jeremy is browsing an allowed Savnac course-18 page in the dedicated Grace capture/review browser, a small fixed teacher-only control should appear, preferably lower-right:

**Teacher Submission**

Clicking it opens a compact form with:

- disposition: `KEEP | CHANGE | CONFUSING | BROKEN | IDEA`;
- free-text **What I want / do not want**;
- optional **What I expected instead**;
- current page title and URL captured automatically;
- timestamp captured automatically.

On submit, the system creates a durable receipt without editing the Canvas page.

The button/form must never be injected into a browser target unless the exact target lock passes.

## Privacy / visibility contract

Teacher submissions are not Canvas student submissions.

They are private course-development receipts stored in the private `computing_commons` repository workflow so Jeremy and authorized tools can consume them.

Do not:

- write feedback into student Canvas pages;
- create student-visible assignments/discussions/forms;
- store credentials, cookies, tokens, or browser-session secrets;
- capture student names, grades, submissions, or other private student data;
- claim that a published Canvas page is private merely because it is unlinked.

## Safety lock

Follow the Course Foundry Visual Review Pipeline safety doctrine in `jeremy-evert/course_foundry/planning/visual-review-pipeline.md`.

For this Savnac implementation, fail closed unless all of these are true:

- expected origin: `http://localhost:3002`;
- exact course id: `18`;
- allowed path prefix: `/courses/18`;
- dedicated Grace review/capture browser debug port/profile is the configured target;
- the rendered URL still satisfies the origin/course/path lock after navigation;
- no ambiguous first-tab or generic-tab fallback is used.

The implementation should be designed so live SWOSU Canvas can later replace the Savnac lock with an exact production host/course/path manifest. Do not hard-wire permissive behavior that would be unsafe live.

## Preserve the working capture path

The existing Grace capture prototype is proven and must keep working:

- `scripts/grace/start-savnac-capture-browser.ps1`
- `scripts/grace/capture-canvas-full-page.ps1`
- `scripts/grace/capture-computing-commons-set.ps1`

Do not break or replace it.

Prefer to reuse the existing dedicated browser profile and DevTools port, but add the feedback surface as a thin teacher-review layer.

Avoid browser extensions or heavyweight runtimes unless there is a concrete reason the existing PowerShell + Chrome DevTools Protocol path cannot support the feature.

A reasonable implementation is a small local Grace feedback service plus CDP-injected teacher-only overlay, but choose the smallest robust design after recon.

## Durable receipt contract

Each submission should create a machine-readable receipt and a human-readable record containing at least:

- schema/version;
- submission id;
- submitted timestamp (UTC and/or local offset-aware time);
- source `computing_commons` commit visible to the review browser/session;
- expected origin/course/path lock;
- rendered page title;
- rendered page URL;
- page/course identity;
- disposition;
- feedback text;
- optional expected outcome;
- lock-validation result.

Preferred repository location:

`sidecar/teacher-feedback/grace/<date-or-session>/`

Use a durable index such as JSONL or JSON plus readable Markdown receipts.

## Keep main clean

Do not dirty the normal Grace `main` checkout every time Jeremy leaves feedback.

Build a safe feedback-publish seam, preferably one of:

1. a dedicated feedback worktree/branch such as `teacher-feedback/grace`, or
2. another equally isolated repo-backed inbox that keeps course source `main` clean.

The feedback branch/worktree may be intentionally noisy. Course source `main` may not be.

A saved submission should become remotely durable with minimal human relay. If safe auto-push per submission is feasible with the existing Git SSH setup, use it. Otherwise provide one obvious **Publish feedback** action and make the unpublished/local state unmistakable.

Never force-push.

## Tool consumption contract

Create a short durable protocol/document describing the loop:

`Jeremy reviews -> Teacher Submission -> durable receipt -> Piper/Luna reads receipts -> classify ACCEPT | REPAIR | HUMAN_DECISION -> Luna repairs bounded source -> Savnac redeploy/readback -> Grace recapture/review`

The raw teacher submission is Jeremy's observation/preference, not automatically an implementation order. A downstream repair pass must preserve source authority and classify real human-decision issues rather than blindly editing.

## Grace entry point

Create one obvious Grace helper, preferably:

```powershell
pwsh -File .\scripts\grace\start-teacher-feedback-review.ps1
```

The helper should:

- resolve repository root safely;
- verify/prepare the isolated feedback sink;
- verify exact Savnac target lock configuration;
- start/reuse the dedicated capture/review browser without breaking capture;
- start the local feedback listener/service if required;
- ensure the teacher-only button appears on exact allowed course-18 pages;
- print a short receipt telling Jeremy what is running and where submissions will be stored.

Also provide a clean stop/helper if a background process is used.

## Feedback form behavior

Keep the form fast enough to use repeatedly while reading pages.

Required behavior:

- Escape/cancel closes without receipt;
- submit cannot silently succeed if persistence failed;
- successful submit visibly confirms the receipt id;
- current URL/title are read-only context, not manually typed;
- textarea preserves ordinary punctuation/newlines;
- no arbitrary HTML execution from feedback text;
- repeated submissions on the same page are allowed;
- receipt filenames/ids are collision-safe.

## Teacher's Table integration

After Prompt 013, Teacher's Table is the instructor cockpit. Add a small instructor-only explanatory section in durable source/documentation telling Jeremy:

- use Teacher's Table for prep;
- use the local **Teacher Submission** button while reading any course-18 page to leave course-development feedback;
- feedback does not go to students and does not change Canvas by itself.

Do not add a student-facing feedback button to the published Home or lesson pages.

## Chain-gun passes

### Pass 1 — RECON

Read:

- current Grace capture scripts;
- Course Foundry `planning/visual-review-pipeline.md`;
- current course-18 Home/Table reports/readback;
- existing Git/worktree/branch conventions.

Record the implementation plan before editing.

### Pass 2 — BUILD FEEDBACK SINK

Build isolated receipt persistence first. Prove it cannot dirty course source `main`.

### Pass 3 — BUILD TEACHER CONTROL

Build the local teacher-only button/form and exact host/course/path lock.

### Pass 4 — HARDEN

Adversarially test or statically verify:

- wrong origin refuses;
- wrong course refuses;
- escaped path refuses;
- no first-tab fallback;
- persistence failure is visible;
- malformed feedback text cannot become executable content;
- main checkout remains clean;
- existing capture scripts remain intact.

### Pass 5 — GRACE PACKAGE

Create README / start / stop / publish helpers and a one-command owner dogfood route.

### Pass 6 — ACCEPT SOURCE

Write:

`sidecar/reports/luna/014_teacher_submission_feedback_loop_report.md`

and any machine-readable test/receipt evidence available from Brandy/static testing.

Commit/push accepted project source according to branch-protection policy.

Do NOT claim live Grace acceptance from Brandy. The final gate is a real Grace owner test.

## Hard boundaries

Do not:

- modify SWOSU production Canvas or live home courses;
- write feedback into Canvas content;
- expose the control to students;
- modify canonical curriculum/source repositories;
- break the current capture scripts;
- install a heavyweight runtime/dependency without a real gate;
- create cloud credentials or copy browser cookies;
- run Quick Tune or synthetic students;
- auto-apply raw feedback to curriculum without a later repair/classification pass.

## Final sentinel

`TEACHER SUBMISSION LOOP READY FOR GRACE DOGFOOD`
