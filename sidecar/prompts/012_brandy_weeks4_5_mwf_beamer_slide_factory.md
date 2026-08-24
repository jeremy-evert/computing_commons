# Prompt 012 — Brandy Weeks 4–5 M/W/F Beamer Slide Factory

## Mission

Act as Luna on **Brandy** and, only after Prompt 011 is fully accepted and ungated, build projector-ready Computing Commons slide packages for **Weeks 4 and 5** across the three shared-rhythm days:

- **Monday Moments** — AI Fluency
- **Wacky Wednesdays** — Professional Minds
- **Fun Fridays** — Professional Minds

This mission should create **six teaching decks total**, plus instructor-note companions, using the reusable Computing Commons Beamer visual system proven in Prompt 008.

Do not deploy these decks to Canvas in this mission. Build, compile, inspect, and make them ready for later delivery.

## Preconditions

Do not begin unless Prompt 011 has reached:

`PRETTY HOME + TEACHER'S TABLE ACCEPTED; CONTINUE TO PROMPT 012 IF UNGATED`

and there is no human-decision, source, Canvas-health, or provenance gate.

If Prompt 011 is not cleanly accepted, stop. Do not skip the landing-pad work to make slides.

## Writable project

Primary writable repository:

`/mnt/brandy_nvme/jevert/git/computing_commons`

Read-only canonical sources:

- `/mnt/brandy_nvme/jevert/git/ai_fluency`
- `/mnt/brandy_nvme/jevert/git/professional_minds`
- `/mnt/brandy_nvme/jevert/git/swosu_cs_curriculum`

Do not modify canonical source repositories.

## Visual system

Reuse the accepted Computing Commons Week 2 Beamer system from Prompt 008:

- `slides/week2_local_ai_workbench/commons-week2-theme.sty`
- accepted visual patterns from the Week 2 projector deck;
- accepted instructor-notes pattern.

The Success Foundations Canvas page remains the broad aesthetic quality bar: deep navy, pale action/evidence/recovery surfaces, generous whitespace, strong hierarchy, calm professional typography.

Do not create a brand-new unrelated theme unless the existing theme genuinely cannot support these decks. If a reusable generic theme path is needed, refactor carefully so Week 2 still compiles unchanged.

## Day identity

Use the friendly day identities as a light framing device, not as cartoon decoration:

- **Monday Moments** — AI Fluency / thinking and workflow practice;
- **Wacky Wednesdays** — Professional Minds / perspective, people, ideas, surprising thinking traps;
- **Fun Fridays** — Professional Minds / practice, application, reflection, demonstration.

A small day label/masthead marker is enough. Preserve professional credibility.

## Week 4 source truth

### Monday Moment — AI Fluency Level 1: Decompose the Task

Canonical package:

`ai_fluency/ai_i/monday_moments/week_04_decompose_the_task/`

Current package includes:

- `monday_moment.md`
- `student_activity.md`
- `instructor_guide.md`
- `assessment_rubric.md`
- `portfolio_artifact_decomposed_task_pipeline.md`

Build a deck that helps students see why a large/vague task should be broken into bounded stages or components with visible interfaces/checkpoints, while preserving human judgment and verification.

Follow the canonical lesson rather than this summary if there is any conflict.

### Wacky Wednesday — Professional Minds: Mapping Arguments for Better Decisions

Canonical reading:

`professional_minds/readings/week_04_wed_spelling_out_arguments.md`

Primary source named by the reading:

*Critical Thinking: Your Guide to Effective Argument, Successful Analysis and Independent Study* by Tom Chatfield, chapter **“Spelling Out Arguments and Assumptions.”**

Current lesson emphasizes reconstruction, premises/conclusions, implicit premises, linked vs independent premises, intermediate conclusions, and the principle of charity.

Use the canonical day-specific Professional Minds Beamer deck as source evidence where useful, but **rebuild the Commons projector treatment** rather than simply copying old styling.

### Fun Friday — Professional Minds: The Outside View

Canonical reading:

`professional_minds/readings/week_04_fri_the_outside_view.md`

Primary source named by the reading:

*Thinking, Fast and Slow* by Daniel Kahneman, chapter **“The Outside View.”**

Current lesson emphasizes inside vs outside view, reference classes, planning fallacy, base rates, realistic baselines, case-specific adjustment, and decision points for revise/stop/continue.

## Week 5 source truth

### Monday Moment — AI Fluency Level 1: Select the Right Model

Canonical package:

`ai_fluency/ai_i/monday_moments/week_05_select_the_right_model/`

Current package includes:

- `monday_moment.md`
- `student_activity.md`
- `instructor_guide.md`
- `assessment_rubric.md`
- `portfolio_artifact_model_comparison_table.md`

Build around selecting a model/tool for the actual task and constraints rather than treating “best model” as a universal property. Preserve whatever dimensions/criteria the canonical lesson actually teaches.

### Wacky Wednesday — Professional Minds: Outcome Bias

Canonical reading:

`professional_minds/readings/week_05_wed_never_judge_a_decision_by_its_outcome.md`

Primary source named by the reading:

*The Art of Thinking Clearly* by Rolf Dobelli, chapter **“Never Judge a Decision by Its Outcome.”**

Current lesson emphasizes outcome bias/historian error, luck vs process, reconstructing what was known at decision time, small samples, and judging decision quality separately from result quality.

### Fun Friday — Professional Minds: Regression to the Mean

Canonical reading:

`professional_minds/readings/week_05_fri_regression_to_the_mean.md`

Primary source named by the reading:

*How Not to Be Wrong: The Power of Mathematical Thinking* by Jordan Ellenberg, chapter **“The Triumph of Mediocrity.”**

Current lesson emphasizes regression to the mean, stable factors + chance, selection on extremes, why real patterns can receive wrong causal stories, and the need for comparison/control when evaluating before/after claims.

Preserve the canonical reading's limitation note around historical material and do not introduce unnecessary biographical detours.

## Product requirements

Create one projector deck and one instructor-notes PDF for each of the six sessions.

Preferred layout:

`slides/shared_rhythm/week04/monday_moment/`
`slides/shared_rhythm/week04/wacky_wednesday/`
`slides/shared_rhythm/week04/fun_friday/`
`slides/shared_rhythm/week05/monday_moment/`
`slides/shared_rhythm/week05/wacky_wednesday/`
`slides/shared_rhythm/week05/fun_friday/`

Each session directory should contain at least:

- `.tex` projector source;
- compiled projector `.pdf`;
- instructor-notes `.tex` or generated source;
- compiled instructor-notes `.pdf`;
- short `README.md` with canonical source/provenance and compile command.

A shared source-data/helper layer is allowed if it reduces duplication.

## Projector-deck design

Target roughly **8–15 slides per session** unless source complexity clearly requires otherwise.

Do not cram. More slides with one clear idea are preferable to a dense wall.

Use slide families proven useful in Week 2:

- hero / essential question;
- explain / mental model;
- diagram / flow;
- worked example;
- ask / predict;
- do this / student move;
- evidence / what this proves and does not prove;
- recovery / misconception;
- receipt / exit move.

Avoid repetitive six-box templates. Choose the appropriate family for the teaching moment.

For Professional Minds, use the source examples responsibly and clearly distinguish source examples from instructor-created computing/professional examples.

Where a concept benefits from computing translation, add a bounded computing example while labeling it as instructor/application material, not the book's claim.

## Instructor notes

Every projector slide needs a matching instructor note entry with:

- **Purpose**
- **Say**
- **Ask**
- **Do**
- **Watch for**
- **Move on when**

Notes should be podium-usable, not a transcript.

For book-backed sessions, include a short **Study before class** block at the beginning naming:

- the exact book/chapter/source;
- the canonical Professional Minds reading;
- the most important 3–5 concepts Jeremy needs to be ready to explain.

For AI Fluency sessions, point to the canonical instructor guide, student activity, rubric, and portfolio artifact.

## Recurring judgment questions

Use these recurring prompts where they genuinely fit:

- What does this prove?
- What does this **not** prove?
- Is this safe?
- Is this secure?
- How do I know?
- Where can I verify that?

Do not force security questions onto unrelated book concepts. Preserve the broader habit of evidence and bounded claims.

## Learning-to-fish progression

Where useful, continue the Week 2 grammar:

- DO THIS
- WHAT THIS MEANS
- FIND THIS YOURSELF
- DEMAND DOCUMENTATION / PRIMARY SOURCE
- VERIFY / SHOW EVIDENCE
- KEEP THE RECEIPT

By Weeks 4–5, begin fading the scaffold slightly. Students should increasingly be asked to propose the question/check before the deck reveals it.

## Grace review automation

Create or extend one Grace helper so Jeremy can review all six session packages without manually hunting paths.

Preferred behavior:

```powershell
pwsh -File .\scripts\grace\review-weeks4-5-shared-rhythm-slides.ps1
```

It should:

- fail on dirty checkout if appropriate;
- verify expected PDFs exist;
- print current commit and file receipt;
- open the six projector decks and instructor-note companions in a predictable review order, or open an index/launcher that makes review easy.

Do not require a new runtime or heavyweight dependency.

## Chain-gun passes

### Pass 1 — PLAN

Inventory all exact canonical source files, existing Professional Minds decks, Prompt 008 theme/notes system, and intended output paths.

### Pass 2 — BUILD WEEK 4 MONDAY

Compile and inspect.

### Pass 3 — BUILD WEEK 4 WEDNESDAY

Compile and inspect.

### Pass 4 — BUILD WEEK 4 FRIDAY

Compile and inspect.

### Pass 5 — WEEK 4 ADVERSARIAL REVIEW

Check source fidelity, density, examples, instructor notes, and visual consistency. Repair before Week 5.

### Pass 6 — BUILD WEEK 5 MONDAY

Compile and inspect.

### Pass 7 — BUILD WEEK 5 WEDNESDAY

Compile and inspect.

### Pass 8 — BUILD WEEK 5 FRIDAY

Compile and inspect.

### Pass 9 — WEEK 5 ADVERSARIAL REVIEW

Repair source, layout, and notes defects.

### Pass 10 — CROSS-DECK ACCEPTANCE

Verify all six projector PDFs and six note PDFs compile cleanly and feel like one product family.

## Visual inspection

For every deck:

- compile with `pdflatex -interaction=nonstopmode -halt-on-error` twice;
- inspect representative rendered pages, including the densest/most complex slide;
- reject overfull boxes, clipped text, tiny unreadable type, overlapping TikZ, or excessive text density;
- split slides when needed rather than shrinking them to survival size.

## Hard boundaries

Do not:

- deploy any Week 4/5 slide artifact to Canvas;
- touch SWOSU production Canvas or live home courses;
- modify canonical `ai_fluency` / `professional_minds` repositories;
- rewrite source claims to fit a preferred story;
- rebuild Weeks 1–3;
- create student assignments beyond what the canonical sources already support;
- expose private data/credentials;
- run Quick Tune or synthetic students.

## Deliverables

At minimum:

- six projector `.tex` sources;
- six compiled projector PDFs;
- six instructor-note PDFs plus source;
- shared/refined theme pieces if needed;
- Grace review helper;
- `sidecar/reports/luna/012_weeks4_5_shared_rhythm_slides_report.md`.

The report must list exact canonical sources and commits used for each session.

## Git / completion

Before stopping:

- all 12 PDFs exist and are non-empty;
- `git diff --check` passes;
- accepted work is committed and pushed according to branch-protection policy;
- remote readback verifies report and at least one deck source/README;
- canonical source repos remain unchanged;
- Canvas remains unchanged by Prompt 012.

Final sentinel:

`WEEKS 4–5 M/W/F SLIDE FACTORY READY FOR GRACE REVIEW`
