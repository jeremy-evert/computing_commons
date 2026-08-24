# Prompt 013 — Brandy Home + Teacher's Table polish and visibility

## Mission

Act as Luna on **Brandy** and make the already-accepted Computing Commons front door and instructor cockpit ready for daily use before building any new feedback plumbing.

This is a small polish/deployment mission against Savnac Canvas course **18 only**. Do not rewrite curriculum.

## Required changes

1. Rename the Savnac course from the prototype-facing name to exactly:

   **SWOSU Computing Commons**

2. On the student Home page, replace the student-facing label **All routes** with **Semester Map** (or the closest existing durable map route if the exact link target requires a different but equally plain label). Do not expose internal repository/process vocabulary.

3. Make **Teacher's Table** visible for normal instructor use:
   - publish the Canvas page;
   - keep it OUT of student modules and OFF the student Home page;
   - do not add it as a student-facing navigation item;
   - preserve the clear instructor-cockpit labeling.

   This is convenience/discoverability, not a claim of access secrecy. Do not put credentials/private student data on the page.

4. Add an explicit **STUDY BEFORE CLASS** line/card to every Week 2 and Week 3 Teacher's Table session.
   - AI Fluency sessions: point to the canonical instructor guide / Monday Moment first, then student activity/rubric as useful.
   - Professional Minds sessions: name the exact book/chapter or companion reading, the durable Professional Minds reading, and the projector deck/notes when present.
   - Keep this cue short enough to use as a morning prep queue.

5. Preserve the accepted Home visual grammar and current Week 2 / Week 3 routes.

## Starting truth

Use current `computing_commons/main` at/after merge commit:

`a1945c4c155b387f6a3d292057c54268d61c41ad`

Read:

- `sidecar/reports/luna/011_pretty_home_teachers_table_report.md`
- `previews/home.html`
- `previews/teacher-table.html`
- Week 2 and Week 3 instructor guides/provenance

The accepted Success Foundations page remains the visual quality bar.

## Writable project / Canvas target

Primary writable repository:

`/mnt/brandy_nvme/jevert/git/computing_commons`

Authorized Canvas mutation:

- Savnac Canvas course **18 only**

Read-only canonical sources as needed:

- `/mnt/brandy_nvme/jevert/git/ai_fluency`
- `/mnt/brandy_nvme/jevert/git/professional_minds`
- `/mnt/brandy_nvme/jevert/git/swosu_cs_curriculum`

## Chain-gun passes

### Pass 1 — RECONCILE

Read current Home/Table source, current Savnac readback, exact Week 2/3 canonical links, and current course title/default view.

### Pass 2 — POLISH SOURCE

Update durable Home/Table previews and deployment support. Keep changes surgical.

### Pass 3 — DEPLOY

Deploy only to course 18. Rename the course, preserve Home as front page/default wiki, publish Teacher's Table, keep Teacher's Table out of student modules/Home.

### Pass 4 — READ BACK

Verify:

- course title = `SWOSU Computing Commons`;
- Home remains published/front page/default wiki;
- student Home says `Semester Map` instead of `All routes`;
- Teacher's Table is published;
- Teacher's Table remains absent from student module items and Home links;
- every Week 2/3 session has a `STUDY BEFORE CLASS` cue;
- existing student routes still resolve;
- no `.md`, `.html`, repository-looking, or `/edit` href leakage in student-facing pages.

### Pass 5 — ACCEPT

Write:

`sidecar/reports/luna/013_home_teacher_table_polish_report.md`

and durable Savnac readback evidence.

Commit/push accepted project work according to branch-protection policy.

## Hard boundaries

Do not:

- touch SWOSU production Canvas or live home courses;
- change Week 2/3 curriculum content beyond these presentation/prep cues;
- modify canonical source repositories;
- add teacher-feedback controls to Canvas HTML in this prompt;
- run Quick Tune or synthetic students;
- delete course 17;
- expose credentials or private student data.

## Continuation gate

If and only if Prompt 013 is accepted and course 18 remains healthy, continue immediately to pinned Prompt 014 for the teacher-only feedback/submission loop.

Final sentinel:

`HOME + TEACHER'S TABLE POLISH ACCEPTED; CONTINUE TO PROMPT 014 IF UNGATED`
