# Prompt 010 — Brandy Week 3 shared rhythm: AI Fluency + Professional Minds

## Mission

Act as Luna on **Brandy** and build the next Computing Commons shared week behind the now-accepted Week 2 rhythm so Jeremy wakes up with **next Monday ready first**, plus a credible Wednesday/Friday preview.

This is intentionally a greedy overnight mission, but it is still bounded to **Week 3 only**. Do not migrate the whole semester.

Target rhythm:

- **Monday — AI Fluency, Level 1:** Plan the Work
- **Wednesday — Professional Minds:** Growth / *Limitless Mind* / growing through mistakes
- **Friday — Professional Minds:** Growth / resilience and risk competence

Priority order matters:

1. Monday AI Fluency must be complete and teachable first.
2. Wednesday should be complete enough that Jeremy can show students what is coming next.
3. Friday should be coherent and ready if source truth is clean.

If time or a real source gate prevents all three, finish Monday cleanly, then Wednesday, then Friday. Do not leave all three half-built.

## Writable project

Primary writable repository:

`/mnt/brandy_nvme/jevert/git/computing_commons`

Authorized mutable prototype surface:

- **Savnac Canvas course 18 only**

Read-only source repositories:

- `/mnt/brandy_nvme/jevert/git/ai_fluency`
- `/mnt/brandy_nvme/jevert/git/professional_minds`
- `/mnt/brandy_nvme/jevert/git/swosu_cs_curriculum`

Do not modify canonical source repositories.

## Required reading

Before mutation, read current Computing Commons truth:

- `AGENTS.md`
- `docs/source-registry.md`
- `docs/canvas-information-architecture.md`
- `curriculum/ai-fluency.md`
- `curriculum/professional-minds.md`
- Prompt 009 report/readback/provenance and the current Week 2 shared-rhythm deployment code
- `instructor/week2_shared_rhythm_teaching_guide.md`

Use Prompt 009 as the implementation pattern. Extend the system cleanly rather than starting a second delivery mechanism.

## Monday source authority — AI Fluency

Canonical source is `jeremy-evert/ai_fluency`.

For Week 3, use the current AI I / Level 1 source package:

`ai_i/monday_moments/week_03_plan_the_work/`

The current package includes at least:

- `monday_moment.md`
- `student_activity.md`
- `instructor_guide.md`
- `assessment_rubric.md`
- `portfolio_artifact_plan_first_workflow.md`

Preserve canonical intent and provenance. Do not invent a competing AI Fluency lesson.

The Monday route should make the lesson teachable and student-usable in Commons. It should help students move from a vague goal toward a bounded plan, identify what context/resources are needed, decide what work should happen first, and preserve a small plan-first receipt. Follow the actual canonical lesson rather than this summary if there is any conflict.

## Wednesday/Friday source authority — Professional Minds

Canonical source is `jeremy-evert/professional_minds`.

Do not trust stale week-number prose in `START_HERE.md`.

Reconcile current Week 3 against:

1. `books/session_book_ledger.md` — authoritative week/book/source mapping;
2. `indexes/session_coverage_matrix.md` — current direct-inspection coverage evidence;
3. actual day-specific reading/presentation/deck files.

Current repository evidence indicates the intended Week 3 pairing is:

- **Wednesday:** Growth — *Limitless Mind* — growing through mistakes;
- **Friday:** Growth — resilience and risk competence / *Resilience Education* source set.

The coverage matrix has historically retained filenames whose numeric prefix does not trivially match the corrected calendar week. **Never infer a source path from the week number.** Resolve the authoritative files from the ledger/matrix and inspect the actual artifact before delivery.

## Product goal

When Jeremy opens Savnac course 18 in the morning, he should be able to:

- teach/show the complete Week 3 Monday AI Fluency route without hunting in repositories;
- show students a clean preview of Wednesday's Professional Minds session;
- see Friday staged coherently behind it;
- move between Week 2 and Week 3 without breaking existing routes;
- retain obvious Recitation/Get Help and recovery seams.

The student should see one Computing Commons product, not source-repository plumbing.

## Clearinghouse rule — stitch, do not fork

Computing Commons owns the **student journey, wrapper pages, navigation, delivery composition, and Canvas presentation**.

Canonical repositories continue to own their source curriculum.

For source material:

- preserve provenance;
- prefer thin wrappers and direct delivery of canonical read-only assets;
- if a canonical compiled PDF/read-only artifact is useful in Canvas, upload that exact source asset rather than rebuilding it just to rename it;
- record source paths and source commit/blob where practical;
- do not copy editable source into a new competing Commons curriculum home.

## Student-facing design

Use the now-proven Computing Commons grammar:

- dark navy hero/masthead;
- pale blue action surfaces;
- pale green success/evidence surfaces;
- warm cream/gold caution/recovery surfaces;
- generous whitespace;
- clear Home / Back / Next;
- visible Recitation/Get Help;
- no repository filenames in visible links;
- no `/edit` links;
- mobile/narrow-friendly Canvas-safe HTML;
- more pages are acceptable when that reduces cognitive load.

Apply the learning-to-fish pattern when useful:

- DO THIS
- WHAT THIS MEANS
- FIND THIS YOURSELF
- PRIMARY SOURCE / DOCUMENTATION
- VERIFY / SHOW EVIDENCE
- KEEP THE RECEIPT
- IF THIS FAILS / RECITATION

Do not force every label onto every page.

## Monday — Plan the Work

Monday is the highest-priority deliverable.

Build a concise, progressive Commons route from the canonical AI Fluency package. If one page becomes dense, split it.

At minimum, a student should be able to:

- state the actual task/problem;
- identify the desired outcome;
- name useful context/resources and obvious unknowns;
- break work into a small first plan rather than asking AI to 'do everything';
- identify what should be checked before execution;
- keep a small plan-first receipt/artifact;
- understand that a plan is a hypothesis about the work, not proof that the work will succeed.

Use the canonical student activity and rubric when they already answer these needs.

Create/extend the instructor guide so Jeremy has a podium-skimmable Monday route: purpose, say, ask, student action, evidence, watch-for, move-on-when.

## Wednesday — Professional Minds preview + teaching route

Build a clean Wednesday route around the canonical *Limitless Mind* / growing-through-mistakes materials.

The wrapper should tell students:

- what they will read/view;
- why mistakes and struggle matter in computing learning;
- one concrete retrieval/discussion/application move;
- what small reflection/evidence to keep;
- how this connects to debugging, failed checks, recovery, and asking for help without turning mistakes into identity judgments.

Preserve the source nuance. Do not reduce the lesson to motivational slogans.

Jeremy should be able to open the Wednesday page on Monday and say, 'This is what we are doing Wednesday.'

## Friday — Professional Minds

Build the Friday route around the authoritative resilience/risk-competence materials.

The wrapper should make clear:

- what students read/view;
- what resilience means in the actual source rather than pop-psychology shorthand;
- how bounded recovery, risk competence, help-seeking, and evidence connect to technical work;
- one small reflection/application receipt.

Honor any wellbeing/accessibility caution in the canonical source.

## Canvas composition

Deploy Week 3 **in place** to Savnac course 18.

Do not create a replacement course.

Prefer one obvious Week 3 module/route with Monday, Wednesday, Friday sequence and minimal supporting items. It is acceptable to use multiple pages inside a day when hand-holding improves.

Preserve all existing Week 2 modules/pages/files/assignment and navigation.

Add the smallest useful transition from Week 2 to Week 3 and, if appropriate, a clear path back.

Published state in Savnac should support owner dogfood. Do not touch production Canvas.

## Instructor handoff

Create:

`instructor/week3_shared_rhythm_teaching_guide.md`

It should include:

- Monday Plan the Work teaching route;
- Wednesday Growth / mistakes teaching route;
- Friday resilience/risk competence route;
- source asset paths;
- recovery/help route;
- what not to improvise live;
- one short 'show this on Monday' note for previewing Wednesday.

Keep it skimmable.

## Chain-gun execution

### Pass 1 — PLAN
Inventory exact source files/commits/blobs and current course-18 state. Record intended Canvas objects before mutation.

### Pass 2 — BUILD MONDAY
Build Monday completely first.

### Pass 3 — REVIEW MONDAY
Adversarially inspect source fidelity, hand-holding, density, navigation, evidence, and recovery. Repair.

### Pass 4 — BUILD WEDNESDAY
Build Wednesday completely.

### Pass 5 — REVIEW WEDNESDAY
Check nuance, source fidelity, student clarity, and preview usefulness. Repair.

### Pass 6 — BUILD/REVIEW FRIDAY
Only after Monday and Wednesday are clean.

### Pass 7 — DEPLOY
Deploy only to Savnac course 18.

### Pass 8 — READ BACK
Verify all created/changed objects, titles/order, published state, files, slugs, hrefs, and cross-week navigation. Confirm no repository-looking hrefs, `.md`/`.html` leaks, or `/edit` targets.

### Pass 9 — ACCEPT
Commit/push only after source and Canvas readback agree.

## Grace / screenshots

Do not require Jeremy to remain awake for screenshot work. Do not block this mission on the separate full-page capture-depth repair.

Final visual owner dogfood can happen in the morning.

## Hard boundaries

Do not:

- touch SWOSU production Canvas or any live home course;
- modify `ai_fluency`, `professional_minds`, or `swosu_cs_curriculum`;
- rebuild the whole semester;
- infer Professional Minds file paths from stale week numbering;
- redesign all canonical Professional Minds decks tonight;
- delete Savnac course 17;
- run Quick Tune or synthetic students;
- expose credentials or private student data.

## Deliverables

At minimum:

- complete Week 3 Monday AI Fluency Commons route;
- Week 3 Wednesday Professional Minds route;
- Week 3 Friday Professional Minds route if source truth remains clean;
- provenance map for delivered source assets;
- `instructor/week3_shared_rhythm_teaching_guide.md`;
- Savnac deployment manifest/readback evidence;
- `sidecar/reports/luna/010_week3_shared_rhythm_report.md`.

If Friday is gated after Monday+Wednesday are fully accepted, report the gate rather than weakening Monday or Wednesday.

## Git / completion

Before stopping:

- `git diff --check` passes;
- commit/push accepted Commons source and reports to `origin/main`;
- remote/read-back verify report and a key Week 3 source;
- return exact project commit SHA;
- confirm canonical repos unchanged;
- confirm production Canvas untouched;
- confirm Quick Tune/synthetic students did not run.

Final sentinel:

`WEEK 3 MONDAY READY + WEDNESDAY PREVIEW READY FOR OWNER DOGFOOD`
