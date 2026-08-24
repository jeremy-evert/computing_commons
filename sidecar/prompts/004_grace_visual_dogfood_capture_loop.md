# Prompt 004 — Grace visual dogfood capture loop

## Mission

Act as Luna on **Grace** and hold the visual-review process together while Jeremy dogfoods the Savnac Computing Commons prototype.

The goal is to make the human interaction cheap: Jeremy should mostly navigate, react, and make aesthetic/usability judgments while Luna handles capture, evidence organization, Git hygiene, and the next bounded inspection step.

This is a visual-review mission, not a Savnac authoring or production deployment mission.

## Required reading

Read:

1. `AGENTS.md`
2. `scripts/grace/README.md`
3. `docs/savnac-prototype-loop.md`
4. the latest `sidecar/reports/luna/002G_savnac_owner_visual_handoff.md` if present
5. the latest visual-repair reports under `sidecar/reports/luna/`

## Environment

Expected Grace repository family is under the local Git root already used on Grace. Resolve the actual checkout rather than assuming a drive letter if current machine truth differs.

Expected Savnac browser route for this campaign is the existing tunnel-backed local endpoint:

`http://localhost:3002/courses/18`

Do not create a new networking path merely for convenience.

## Operating loop

### 1. Reconcile

- fast-forward `computing_commons` if safe;
- verify the capture scripts exist under `scripts/grace/`;
- protect unrelated local work;
- verify the Savnac course-18 route is reachable before asking Jeremy to inspect anything.

### 2. Start the capture browser

Use:

`scripts/grace/start-savnac-capture-browser.ps1`

If the dedicated browser needs a login, ask Jeremy only to perform the login. Do not ask Jeremy to relay routine machine state that Luna can inspect locally.

### 3. Human visual pass

Guide Jeremy through a small number of high-value views rather than dumping the whole course at once.

Preferred initial route:

1. Modules / course map
2. Success Foundations / Semester Kickoff
3. Recitation / Get Help
4. Week 2 Local AI landing
5. Verify the Tools
6. Recovery with Evidence

For each page:

- let Jeremy navigate naturally;
- capture a full-page PNG with `scripts/grace/capture-canvas-full-page.ps1`;
- preserve the rendered URL/title and capture path;
- ask Jeremy for only the judgment machines cannot supply: what feels clear, ugly, crowded, confusing, reassuring, or wrong;
- record concise findings, not a transcript.

### 4. Batch evidence

When useful, use:

`scripts/grace/capture-computing-commons-set.ps1`

This creates a timestamped visual-review bundle under `sidecar/visual-review/grace/`.

Do not publish visual evidence automatically merely because it exists. Publish only when the checkout is clean, the evidence contains no credentials/student data, and Jeremy has authorized the visual-review record to go to GitHub.

When publication is authorized, `capture-computing-commons-set.ps1 -Publish` may commit/push the capture bundle directly to `main` if its built-in safety checks pass.

### 5. Produce the punch list

Keep one short ranked punch list with categories such as:

- navigation
- visual hierarchy
- wording
- link behavior
- recovery/help
- consistency
- mobile/narrow-window behavior
- Canvas-only defects versus repository-source defects

Do not inflate stylistic preferences into P0/P1 defects.

### 6. Stop before authoring repairs

This Grace mission is primarily the human-observation and evidence lane.

Do not mutate Savnac course content, enrollments, grades, assignments, or modules unless a later explicit prompt authorizes that repair. The default handoff is a clean visual punch list for the Savnac builder.

## Hard boundaries

Do not:

- touch SWOSU Canvas course 24298;
- access or preserve student submissions, grades, comments, or identities;
- rotate credentials;
- change Savnac VM/network/libvirt state;
- delete course 17;
- run Quick Tune or synthetic students unless separately authorized;
- clean home-course repositories;
- record final instructional videos.

## Human role

Jeremy is the visual/usability authority. Ask him to click, look, and judge. Do not turn him into the screenshot operator, Git relay, or machine-state reporter when Luna can do those tasks locally.

## Desired result

At the end of a pass, write a concise report under:

`sidecar/reports/luna/004_grace_visual_dogfood_report.md`

Include:

- pages inspected;
- capture bundle path/commit if published;
- ranked visual/usability punch list;
- repository-source defects versus Canvas-rendering defects;
- what should be repaired next in Savnac;
- what already feels accepted and should stop being churned;
- confirmation that production Canvas was untouched.

Preferred final status:

`GRACE VISUAL PASS COMPLETE — SAVNAC REPAIR LIST READY`
