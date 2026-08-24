# Computing Commons build roadmap

## Goal

Build the Commons into a complete, coherent **shared Recitation and clearinghouse** before deploying it wholesale to SWOSU Canvas course `24298`.

The Commons should reduce duplicated teaching, duplicated grading, and duplicated navigation while preserving strong canonical source repositories.

## Product vision

A student should experience one shared workshop beneath the computing curriculum:

- learn common craft once;
- keep earlier levels available;
- apply shared capabilities inside each discipline;
- return to Recitation for help;
- avoid relearning the same setup/process in multiple courses.

The Commons is a composition layer. It should not become a copy warehouse.

## Build map

### Phase 0 — Lock architecture

Establish and maintain:

- source registry;
- course/Commons ownership boundary;
- cumulative level rule;
- Fall 2026 0-point/bonus soft-launch posture;
- Canvas deployment boundary;
- completion/evidence philosophy.

Exit condition: a future builder can answer “where does this belong?” without guessing.

### Phase 1 — Build the front door

Create the student-facing Commons information architecture:

1. Start Here
2. Recitation / How to Get Help
3. Success Foundations / Semester Kickoff
4. Local AI Lab
5. AI Fluency
6. Professional Minds
7. Recitation Toolbox
8. Farkle + Machine Learning Finale
9. Recovery / Reference area

The front door should explain that the Commons is shared support for the student’s actual computing courses, not an additional academic discipline.

Exit condition: a new student can identify where to start, where required work lives, and where to get help without knowing the repository architecture.

### Phase 2 — Complete the shared runway

#### Success Foundations

Stitch the strongest existing cross-course kickoff material into one Commons journey. Keep course-specific introductions in home courses.

#### Local AI Lab

Compose the student experience from:

- `local_ai_lab_setup` for curriculum/product;
- `windows_classroom` for accepted Windows evidence/contract.

Do not create a third setup path.

Exit condition: the repository contains one explicit Commons delivery map for the accepted Local AI sequence, evidence requirements, recovery path, and home-course wrapper contract.

### Phase 3 — Complete progressive AI Fluency

Use `ai_fluency` as canonical curriculum.

Required progression:

- Level 1 target: CS1
- Level 2 target: CS2
- Level 3 target: DSCT
- Level 4 target: Software Engineering
- Level 5 target: Machine Learning

Computer Architecture is a cross-cutting technical bridge rather than a forced numbered rung.

**Progressive release:** when Level N is assigned, Levels 1 through N remain available.

Exit condition: the Commons has a clear student route, completion model, level visibility contract, and no competing Monday Moment authoring copies.

### Phase 4 — Complete Professional Minds

Use `professional_minds` as canonical source.

For the current semester:

- Monday = AI Fluency
- Wednesday and Friday remain Professional Minds/Recitation rhythm to be refined without duplicating material across courses.

The Commons should expose one shared Professional Minds route while course repos retain only disciplinary applications when useful.

Exit condition: Professional Minds has one stable Commons delivery seam and a documented progression strategy.

### Phase 5 — Build the Recitation Toolbox

Audit existing sources before authoring new material. Build one coherent toolbox for:

1. Containers / reproducible environments
2. LaTeX and documentation
3. Work First
4. Linux command line and profiling/inspection
5. Git / source-code management

These are not locked to fixed semester weeks after the initial runway. Courses call them when needed.

Each toolbox capability should include:

- What is this for?
- Minimum useful skill
- Safe bounded practice
- Evidence of success
- Common failure/recovery
- Where later courses deepen it

Exit condition: every toolbox capability has a canonical source/delivery contract and can be assigned independently from a home course.

### Phase 6 — Build the shared finale

Create the Commons composition for **Farkle + Machine Learning**.

The shared phenomenon should support multiple disciplinary lenses:

- CS1: simulation/code
- CS2: design and implementation quality
- DSCT: probability, uncertainty, evidence
- Computer Architecture: profiling, CPU/GPU, throughput, hardware behavior
- Software Engineering: systems/reproducibility/testing
- Machine Learning: models, evaluation, prediction, limitations

Computer Architecture should provide the strongest machine-facing bridge.

Exit condition: one common experience can be reused across courses without turning into six duplicate assignments.

### Phase 7 — Build Fall 2026 completion/grading posture

For the soft launch:

- give Commons activities due dates where useful;
- represent shared work as 0-point assignments where appropriate;
- use completion/evidence tracking;
- allow exceptional work to earn bonus credit in a home course;
- do not require cross-course automatic grade synchronization until tested.

Exit condition: the repo contains an explicit student/completion model that can be implemented in Canvas without silently changing home-course grading contracts.

### Phase 8 — Repository acceptance

Before Canvas deployment, perform an adversarial review of the complete Commons:

- one coherent student story;
- no dead or competing paths;
- no stale ZyBooks dependency;
- no duplicate Local AI instructions;
- cumulative levels behave as intended;
- course-specific material is not accidentally centralized;
- source registry matches reality;
- every required student route has recovery guidance;
- Fall 2026 grading posture is internally consistent;
- Canvas deployment manifest can be generated from repository truth.

Required verdict:

`READY FOR COMPUTING COMMONS CANVAS DEPLOYMENT`

Anything less stays in Git until repaired.

## Post-acceptance sequence

After repository acceptance:

1. deploy complete Commons to Canvas course `24298`;
2. read back and verify the complete student-facing structure;
3. establish/test enrollment and progressive-level visibility behavior;
4. owner dogfoods the course;
5. repair observed problems;
6. owner records videos from the accepted path;
7. freeze/mark the first established Commons baseline;
8. Flo uses the Commons as the reference while cleaning duplicated shared material from individual courses and checking later weeks.

## Non-goals during build

- Do not clean every home course before the Commons exists.
- Do not depend on production Canvas as authoring truth.
- Do not invent grade synchronization.
- Do not duplicate strong canonical repositories into Commons.
- Do not force every student through every toolbox item on the same week.

## Success test

The Commons is earning its existence when adding a shared capability lets something else become simpler:

- one fewer duplicate lesson;
- one fewer grading event;
- one fewer conflicting instruction;
- one clearer place for students to recover;
- one stronger reusable capability across multiple courses.
