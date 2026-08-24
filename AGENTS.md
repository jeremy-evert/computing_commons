# Computing Commons agent guidance

## Mission

Keep the Commons a **shared recitation, clearinghouse, and apprenticeship layer**, not a duplicate academic course and not a monorepo that unnecessarily absorbs every strong shared project.

The Commons composes the common student journey. Individual course repositories own disciplinary teaching, assessment, and application. Specialized shared repositories may remain authoritative for their domain.

## Clearinghouse rule

**Stitch, do not fork.**

When a strong canonical source already exists, consume, link, package, or orchestrate that source rather than silently copying it into a second drifting implementation.

Current high-value source relationships include:

- `jeremy-evert/local_ai_lab_setup` — canonical shared Local AI Lab instructional product;
- `jeremy-evert/windows_classroom` — reviewed/tested Windows classroom implementation evidence and contract;
- `jeremy-evert/ai_fluency` — AI I–V progression and Monday Moments;
- `jeremy-evert/professional_minds` — Professional Minds source and reusable professional-development artifacts;
- `jeremy-evert/swosu_cs_curriculum` — cross-course map and shared curriculum decisions.

`computing_commons` owns the composition/delivery map that turns these sources into one coherent Recitation experience.

## Source boundaries

Use this order when sources disagree:

1. explicit current owner decisions in this repository;
2. current `computing_commons` composition/progression docs;
3. the canonical specialized source for the shared capability being delivered;
4. cross-course decisions in `jeremy-evert/swosu_cs_curriculum`;
5. current owning course repositories for course-specific truth;
6. Canvas as deployment evidence;
7. historical syllabi, old Canvas copies, and archived material as provenance only.

Do not revive retired ZyBooks dependencies or other stale artifacts merely because they remain in historical sources. Fall 2026 computing material is open-source/course-owned unless a current source explicitly says otherwise.

## Course purity rule

Course repositories should increasingly contain only material that teaches, assesses, or applies that discipline.

For example, `computer_science_1` should be about Computer Science I. Shared AI Fluency lessons, Professional Minds source, Local AI Lab setup, generic Git/Linux/container/documentation instruction, and shared finale content should migrate to their canonical shared homes and/or the Commons delivery layer.

Do not delete or move course material blindly. First identify the canonical destination and any home-course wrapper that must remain so grading, navigation, and disciplinary application are preserved.

## Ownership test

Before adding material here, ask:

- Is this capability genuinely shared across multiple computing courses?
- Can a student learn it once and then apply it differently in each discipline?
- Is there already a canonical repository that should remain the source?
- Will centralizing the student delivery reduce duplicate content, duplicate grading, or navigation confusion?

If the learning outcome is specifically Python, software design, discrete mathematics, architecture, software engineering, or machine learning, keep the disciplinary teaching in the owning course repo.

Course-specific reminders, graded receipts, and applications may remain in home courses as **wrappers** around Commons capabilities.

## Progressive-release rule

Levels accumulate.

When a student is assigned Level N, the intended student experience exposes Levels 1 through N. Earlier levels remain available for review and recovery. Later levels remain unopened until assigned.

Example: assigning Level 4 should make Levels 1, 2, 3, and 4 available, not Level 4 alone.

Do not design a level system that hides foundational material after completion.

## Canvas boundary

Canvas is a delivery surface. Repository truth should be reconciled into Canvas, not reconstructed from stale Canvas objects.

Do not mutate production Canvas, enroll/drop students, change production grading, or assume cross-course grade synchronization without explicit authorization and an appropriate test boundary.

The current Computing Commons Canvas course is a test/prototype surface until explicitly promoted.

## Fall 2026 soft launch

Favor low-risk experimentation:

- due dates and completion tracking are useful;
- Commons activities may be 0-point assignments;
- exceptional evidence may earn bonus credit in a home course;
- avoid gradebook architecture that creates more work than the Commons removes.

## Evidence rule

A tool being installed is not proof it works. A model being listed is not proof it can infer. A command existing is not proof the student can complete the workflow.

Prefer short evidence receipts that show what was attempted, what happened, and what independently verified success.

## Simplicity test

Every Commons addition should answer:

> What duplication, grading, or confusion can now shrink elsewhere because this exists?

If the answer is “none,” reconsider whether the material belongs here.
