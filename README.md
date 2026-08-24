# SWOSU Computing Commons

The **SWOSU Computing Commons** is the shared **recitation, clearinghouse, and apprenticeship layer** for SWOSU computing students.

Its purpose is simple:

> **Learn the common craft once. Practice it everywhere.**

The Commons does not need to absorb every shared project into one giant repository. Instead, it stitches together the best existing sources into one coherent student journey and one coherent Canvas delivery surface.

## Clearinghouse model

Specialized repositories may remain authoritative for the thing they do best:

- `jeremy-evert/local_ai_lab_setup` owns the shared **Build and Verify Your Local AI Lab** instructional product.
- `jeremy-evert/windows_classroom` owns tested/reviewed Windows classroom evidence and the accepted Windows implementation contract.
- `jeremy-evert/ai_fluency` owns the progressive AI I–V sequence and Monday Moments.
- `jeremy-evert/professional_minds` owns Professional Minds source material, lessons, professional DNA, and related artifacts.
- `jeremy-evert/swosu_cs_curriculum` owns the cross-course curriculum map and decisions about where shared material belongs.
- individual course repositories own their actual disciplines and course-specific applications.

`computing_commons` owns the **composition layer**: what students see, how shared capabilities are sequenced, which canonical source supplies each experience, how Canvas should present it, and what lightweight course wrappers remain behind.

The rule is **stitch, do not fork**. When a strong canonical source already exists, the Commons should point to, package, or consume it rather than silently creating another drifting copy.

## Course-repository boundary

A course repository should increasingly contain only material that belongs to that course.

For example, `computer_science_1` should own introductory programming, CS1 Reasoning Odyssey applications, CS1 grading, and CS1-specific wrappers. Shared material such as AI Fluency, Professional Minds, Local AI Lab setup, general Git instruction, common Linux/container/documentation training, and shared finale material should migrate toward their canonical shared sources and the Commons delivery layer.

The Commons is therefore both a student-facing workshop and a **de-duplication seam** for the course repositories.

## Student model

The Commons should feel like a shared computing recitation/workshop, not a seventh academic course.

Students take their normal academic courses. Those courses point into the Commons when they need a common capability. Recitation hours provide a shared place to get help with those capabilities regardless of which computing course sent the student there.

## Progressive levels

The long-term progression is course-targeted but cumulative:

1. **Level 1 — CS1 target:** become a capable computing student.
2. **Level 2 — CS2 target:** become a capable computing practitioner.
3. **Level 3 — DSCT target:** strengthen judgment, evidence, uncertainty, and critical reasoning.
4. **Level 4 — Software Engineering target:** teamwork, systems, review, change, and professional engineering workflow.
5. **Level 5 — Machine Learning target:** understand models, data, evaluation, limitations, and responsible AI at a deeper level.

Computer Architecture acts as a cross-cutting technical bridge, especially for Linux inspection, profiling, CPU/GPU behavior, local-model performance, containers, and the shared Farkle + Machine Learning finale.

### Progressive-release rule

Levels accumulate rather than replace one another.

If a student is assigned **Level 4**, the intended Commons experience exposes **Levels 1, 2, 3, and 4**. Level 5 can remain unopened until it is assigned. Earlier levels stay available for review, recovery, and students who entered the sequence through a nonstandard course path.

## Initial shared experiences

The Commons is expected to stitch together:

- Success Foundations / Semester Kickoff;
- AI Fluency;
- Professional Minds;
- Build and Verify Your Local AI Lab;
- containers and reproducible environments;
- LaTeX and evidence-oriented documentation;
- Work First;
- Linux command-line inspection and profiling;
- Git / source-code management;
- common AI accountability and verification habits;
- professional-pathway foundations;
- the shared Farkle + Machine Learning finale.

Course-specific applications remain in course repositories. The Commons may teach Git once, while CS1 uses Git to protect a Python project, Architecture uses it to preserve investigation evidence, and Software Engineering uses it as part of collaborative engineering work.

## Fall 2026 posture

Fall 2026 is a soft-launch semester for the Commons:

- shared activities can have real due dates and completion tracking;
- Commons activities can be represented as **0-point assignments** while the architecture is being proven;
- strong evidence, useful troubleshooting, excellent verification, or other exceptional work may earn bonus credit in a home course;
- avoid rebuilding every production gradebook merely to test the Commons seam.

## Design test

Every addition to the Commons should make the overall system simpler.

> **What duplication, grading, or student confusion can shrink because this shared experience now has one clear home?**

If the answer is “none,” reconsider whether it belongs here.

See:

- `docs/vision.md`
- `docs/source-registry.md`
- `docs/curriculum-map.md`
- `docs/progression.md`
- `docs/course-boundary-migration.md`
- `docs/fall-2026-soft-launch.md`
