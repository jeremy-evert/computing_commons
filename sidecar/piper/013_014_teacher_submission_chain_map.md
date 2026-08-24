# Chain map — Home/Table polish → Teacher Submission feedback loop

## Goal

Turn the accepted Computing Commons front door into a daily-use teaching cockpit, then add a teacher-only, repo-backed feedback seam so Jeremy can leave durable page-specific observations without asking students to see them and without dirtying course-source `main`.

## Barrel 1 — Prompt 013

`sidecar/prompts/013_brandy_home_teacher_table_polish_and_visibility.md`

Required result:

- course title becomes `SWOSU Computing Commons`;
- student Home says `Semester Map` rather than internal `All routes` language;
- Teacher's Table becomes published for instructor use but remains absent from student Home/modules;
- every Week 2/3 Teacher's Table session gets an explicit `STUDY BEFORE CLASS` cue;
- Savnac course 18 readback stays healthy.

Gate:

`HOME + TEACHER'S TABLE POLISH ACCEPTED; CONTINUE TO PROMPT 014 IF UNGATED`

## Barrel 2 — Prompt 014

`sidecar/prompts/014_brandy_teacher_submission_feedback_loop.md`

Required result:

- dedicated Grace teacher-review entry point;
- teacher-only `Teacher Submission` button/form injected only into exact locked Savnac course-18 targets;
- receipt sink isolated from the normal `main` checkout;
- durable machine-readable + human-readable page feedback;
- feedback made remotely durable with minimal relay;
- existing capture workflow preserved;
- Course Foundry host/course/path locking doctrine followed;
- final real gate is Grace owner dogfood, not a claim from Brandy.

Gate:

`TEACHER SUBMISSION LOOP READY FOR GRACE DOGFOOD`

## Feedback lifecycle

`Jeremy reviews page -> Teacher Submission -> durable receipt -> Piper/Luna reads receipt -> ACCEPT | REPAIR | HUMAN_DECISION -> bounded repair -> Savnac deploy/readback -> Grace capture/review`

A teacher submission is an observation/preference receipt. It is not automatically authoritative curriculum source and must not bypass source/provenance rules.

## Privacy rule

The feedback control is local teacher-side tooling, never student-facing Canvas HTML. No credentials, cookies, grades, student submissions, or private student data belong in teacher-feedback receipts.

## Future live-Canvas promotion

Before live SWOSU Canvas use, reuse the Course Foundry Visual Review Pipeline target-lock contract with exact production origin + course id + path prefix. Never use a permissive first-tab fallback in live mode.
