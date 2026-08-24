# Course-boundary migration: keep course repos about their courses

## Goal

As the Commons matures, individual course repositories should become more disciplined about ownership.

**Computer Science I should be about Computer Science I.** The same principle applies to CS2, DSCT, Architecture, Software Engineering, and Machine Learning.

Shared student-development and common-tooling material should move toward a canonical shared repository plus the Commons delivery layer rather than living as six semi-independent copies.

## Migration pattern

For each candidate shared artifact:

1. identify what learning outcome it actually serves;
2. identify the best canonical shared source;
3. preserve/strengthen that source;
4. add the Commons composition/delivery pointer;
5. leave only the home-course wrapper needed for disciplinary application, navigation, or grading;
6. verify no course-specific objective was accidentally removed;
7. only then retire the duplicate copy from the course repo.

Do not perform blind file moves. A filename being generic does not prove the learning outcome is generic.

## High-confidence CS1 extraction candidates

### AI Fluency / Monday Moments

Current CS1 repository evidence already says its `monday_moments/` directory is **not** the canonical authoring home and that real entries belong in `jeremy-evert/ai_fluency/ai_i/`.

Desired end state:

- `ai_fluency` owns AI I source/content;
- Computing Commons owns the student-facing Level 1 route and progressive availability;
- CS1 keeps only references and CS1-specific application/assessment where needed;
- historical scaffolding can be retired after dependency/navigation checks.

### Local AI Lab

Desired end state:

- `local_ai_lab_setup` owns the shared instructional product;
- `windows_classroom` owns the accepted/tested Windows implementation evidence;
- Computing Commons stitches these into one student-facing Recitation experience;
- CS1 keeps a small programming application/receipt rather than a second setup curriculum.

### Success Foundations / Semester Kickoff

Desired end state:

- cross-course/shared source remains shared;
- Computing Commons delivers the common student experience;
- CS1 retains only CS1-specific welcome, schedule, expectations, and disciplinary framing.

### Professional Minds

Desired end state:

- `professional_minds` owns reusable source/content;
- Computing Commons owns the progressive student-facing route;
- CS1 retains only CS1-specific reflection/application if the outcome is genuinely programming-course specific.

### Common Git / Linux / container / documentation instruction

Desired end state:

- canonical shared source identified or promoted after an evidence audit;
- Commons exposes the shared recitation;
- CS1 assignments assume/apply the skill in introductory programming rather than maintaining independent generic tutorials.

### Shared Farkle + Machine Learning finale

Desired end state:

- Computing Commons owns the common experience/map;
- Architecture provides the strongest machine/profiling lens;
- DSCT supplies probability/reasoning depth;
- Machine Learning supplies model/evaluation depth;
- CS1 contributes an appropriately bounded programming/simulation lens if needed rather than owning the whole shared experience.

## Material that should remain CS1

Examples include:

- Python syntax and programming instruction;
- variables, expressions, types, branching, loops, functions, strings, collections, objects/classes, and other CS1 outcomes;
- CS1 Reasoning Odyssey programming applications;
- CS1-specific rubrics, grading model, and course schedule;
- programming tasks that use Commons tools to accomplish a CS1 learning objective;
- lightweight wrappers/receipts that connect Commons completion to CS1 application.

## Migration safety rule

The destination must exist and be accepted before a useful source disappears from a course repository.

The Commons should reduce duplication, not create a scavenger hunt across half-built repositories.

## First migration target

Use CS1 as the donor/reference because its repository currently represents intended course truth more strongly than its Canvas shell.

The first vertical slice should remain:

**Local AI canonical sources → Computing Commons test Canvas → student completion → lightweight CS1 programming application/receipt.**

Once that seam works, use the same migration pattern for AI Fluency, Professional Minds, Success Foundations, and the remaining common recitations.
