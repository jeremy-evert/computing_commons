# Prompt 014 — Teacher Submission feedback loop

## Verdict

**TEACHER SUBMISSION LOOP READY FOR GRACE DOGFOOD**

The reusable teacher-side loop is source-complete and intentionally stops at
the real owner gate: Jeremy must run the one-command Grace dogfood in the
dedicated review browser.

Entry point: `scripts/grace/start-teacher-feedback-review.ps1`. Stop with
`stop-teacher-feedback-review.ps1`; publish isolated receipts with
`publish-teacher-feedback.ps1`. The existing capture scripts remain unchanged.

The overlay is injected only when exactly one DevTools page matches
`http://localhost:3002/courses/18` and the current path stays under
`/courses/18`; there is no first-tab or generic-tab fallback. The local service
revalidates the same lock, rejects wrong-course URLs, validates dispositions,
and visibly returns persistence errors. Feedback is inserted with text-safe
DOM APIs and escaped in Markdown receipts. Receipts contain schema, ID,
timestamp, source commit, page context, disposition, feedback, expected outcome,
and lock result in both JSON and Markdown.

The sink is `.teacher-feedback-worktree`, branch `teacher-feedback/grace`, so
normal course-source `main` remains clean. The protocol is documented in
`sidecar/teacher-feedback/README.md`. Static/live-local evidence is in
`sidecar/evidence/teacher-feedback/014_static_checks.json`.

No Canvas content/settings/submissions were changed by Prompt 014; no
credentials, cookies, grades, student names, or private student data are stored.
