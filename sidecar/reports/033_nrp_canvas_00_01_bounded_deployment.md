# NRP Canvas 00+01 bounded deployment — evidence report

Date: 2026-09-16
Mission: `foreman_interface/jobs/tasks/computing_commons_nrp_canvas_00_01_deploy_033.md`
Prompt: `sidecar/prompts/033_nrp_canvas_00_01_bounded_deployment.md`, pinned commit `dc7ad84732cd8a0c9e29abaec6cd7bd2f541753c` (verified present and an ancestor of `origin/main` before this run)
Anna — Assistant Foreman, April. Flo — Lead Foreman, Brandy, retains final live sign-off.

## Source commit

`computing_commons` fast-forwarded to `origin/main` (`a817e1a`) before writing. Source files read at that commit:

- `national_research_platform/teaching_slice/00_start_here.md`
- `national_research_platform/teaching_slice/01_your_laptop_is_not_the_whole_computer.md`

## Pre-deployment reconnaissance (read-only)

- Course `24298` independently verified: `name = "Computing Commons"`, `course_code = "CC101"`.
- Listed all 24 existing modules — no "National Research Platform" module existed.
- Listed all 90 existing course Pages — no page titled "00 — Start Here: What Are We About to Do?" or "01 — Your Laptop Is Not the Whole Computer" existed (only unrelated "Week 2 — Start Here" and "Aider Days — Start Here").
- Conclusion: clean additive path, no collision, no destructive reconciliation needed.

## Content fixes applied during markdown→Canvas conversion

Both fixes are in `computing_commons/scripts/deploy_nrp_canvas_00_01.py` (not hand-edited in Canvas after the fact — the script builds the corrected HTML before writing):

1. **01's dead relative link.** Source ends with `[Computing Commons National Research Platform landing page](../README.md)`, which 404s inside Canvas. Rewritten to the public GitHub blob URL `https://github.com/jeremy-evert/computing_commons/blob/main/national_research_platform/README.md`, verified live via `gh api repos/jeremy-evert/computing_commons/contents/national_research_platform/README.md`.
2. **00's stale cross-reference.** "Where to go next" called 01 "01 — Video: Your Laptop Is Not the Whole Computer"; corrected to the real page title "01 — Your Laptop Is Not the Whole Computer". The instructor video-script file was not exposed as student content anywhere in this deployment.

## Objects created

| Object | ID / slug | Title | Published |
|---|---|---|---|
| Module | `219432` | National Research Platform — Your First Remote Workload | true |
| Page | `00-start-here-what-are-we-about-to-do` | 00 — Start Here: What Are We About to Do? | true |
| Page | `01-your-laptop-is-not-the-whole-computer` | 01 — Your Laptop Is Not the Whole Computer | true |
| Module item | `1534998` (position 1) | 00 — Start Here… → Page `00-start-here-…` | true |
| Module item | `1534999` (position 2) | 01 — Your Laptop… → Page `01-your-laptop-…` | true |

Receipt: `sidecar/runs/nrp_canvas_00_01_deploy.json`.

One correction mid-run: `create_module` accepted `module[published]=true` in the POST body but Canvas returned the module `published: false` (module publish state isn't honored on create the way page/item publish is). Fixed with an explicit `update_module(..., {"module[published]": "true"})` call, then independently re-read to confirm `published: true`.

## Independent readback QC (Prompt 033's 14-point contract)

1. Course `24298` reads as Computing Commons — confirmed.
2. Exactly one NRP teaching module used — confirmed (`219432`, only match for "National Research Platform" across all modules).
3. Module title correct — confirmed, exact string match.
4. Item order is 00 then 01 — confirmed (positions 1, 2).
5. Both items resolve to the intended Canvas Pages — confirmed (`page_url` on each item matches the created page).
6. Page titles correct — confirmed, exact string match on both.
7. Rendered content corresponds to the public student source — confirmed by direct read-back diff against source, modulo the two documented fixes.
8. Code blocks/text diagrams remain readable — confirmed: 01's fenced code blocks rendered as `<pre><code>` in the read-back body.
9. Module and pages published/student-visible — confirmed on all three (module fixed mid-run, see above; both pages published on create).
10. Public links used resolve — confirmed (`github.com/.../national_research_platform/README.md` returns a live `html_url` via `gh api`).
11. No private-repository link exposed — confirmed; the only added link is the public `computing_commons` repo.
12. No credential-shaped material exposed — confirmed by string check on both page bodies (no `api_token=`, `password:`, PEM markers).
13. No graded object/submission/due date/enrollment/unrelated Canvas object changed — confirmed: course-wide assignment list re-read after the deploy, no new assignment matching this content; the client's course allowlist was scoped to `24298` only for every call in this run.
14. 01 is usable as Jeremy's live teaching/recording surface — page is published, headed by the "big idea" framing, five numbered vocabulary terms, and the CREATE→RUN→OBSERVE→VERIFY→CLEAN UP→VERIFY AGAIN lifecycle diagram, readable top to bottom without instructor-only stage directions (those live only in the separate, untouched `instructor/video_scripts/01_...md`).

## Implementation script

`computing_commons/scripts/deploy_nrp_canvas_00_01.py` — target-locked to course `24298` via the client's course allowlist, idempotent conversion logic (asserts both content fixes actually applied before writing), reusable if this slice ever needs to be rebuilt.

## Scope confirmation

No other Canvas course was touched. No assignment, points, submission type, due date, rubric, assignment group, or enrollment object was created or changed anywhere in this run.

## Flo sign-off

Pending — handing this readback to Flo (Brandy) for final live QC per the standing Flo→Anna operating model. Not marking the JTT item done.

## Remaining gates

None identified. Acceptance criteria met: Jeremy can open Computing Commons Canvas and see the module with both pages, published, in order, ready to teach 01 live.
