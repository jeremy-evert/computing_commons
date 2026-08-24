# Teacher feedback loop

This is a teacher-side course-development inbox, not a Canvas submission
surface. On Grace, run `pwsh -File .\scripts\grace\start-teacher-feedback-review.ps1`.
The strict CDP lock allows only `http://localhost:3002/courses/18...` in the
dedicated browser target. Receipts are written to the isolated
`teacher-feedback/grace` worktree and published with
`publish-teacher-feedback.ps1`, keeping course-source `main` clean.

Protocol: Jeremy reviews -> Teacher Submission -> durable JSON/Markdown receipt
-> Piper/Luna reads receipts -> classify `ACCEPT | REPAIR | HUMAN_DECISION` ->
Luna repairs bounded source -> Savnac redeploy/readback -> Grace recapture/review.
Raw observation is not an implementation order; source authority and human
decisions remain in force.
