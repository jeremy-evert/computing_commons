# DRAFT — Flo: NRP Canvas Teaching Slice Deployment

Status: **HOLD — DESIGN INPUT ONLY — DO NOT DISPATCH YET**

This file is being staged so the eventual Flo handoff is clean. It is not current authorization to mutate Canvas.

## Owner intent

When Jeremy declares the NRP teaching slice ready, reconcile the approved public Computing Commons NRP material into one bounded, polished teaching module in the Computing Commons Canvas course.

The purpose is **teaching and learning, not grading**.

Canvas destination:

```text
Computing Commons
course_id = 24298
```

Repository source of truth:

```text
jeremy-evert/computing_commons
```

Primary design authority for this slice:

```text
national_research_platform/instructor/canvas_teaching_slice_design.md
```

Supporting student curriculum:

```text
national_research_platform/getting_started.md
national_research_platform/curriculum/01_identity_access_namespace.md
national_research_platform/curriculum/02_first_remote_job.md
national_research_platform/curriculum/03_evidence_cleanup_failure.md
national_research_platform/scripts/student_preflight.sh
national_research_platform/templates/first_job.template.yaml
national_research_platform/templates/evidence_receipt.md
```

## Expected deployment scope

Create or reconcile **one** bounded Canvas teaching module provisionally titled:

> National Research Platform — Your First Remote Workload

Expected learning sequence:

```text
00 — Start Here: What Are We About to Do?
01 — Video: Your Laptop Is Not the Whole Computer
02 — Video: Identity, Access, and the Course Namespace
03 — Try It: Authenticate and Run the Preflight
04 — Video: Send One Tiny Job Somewhere Else
05 — Try It: Launch, Observe, and Read the Logs
06 — Video: Failure Is Data + Clean Up What You Create
07 — Try It: Cleanup and Evidence Receipt
08 — Where This Goes Next in Computer Science
```

Do not mirror the repository tree into Canvas. Build a student journey.

## Boundaries

Authorized only when this draft is explicitly promoted by Jeremy or a controlling Foreman mission.

When promoted:

- course 24298 only;
- read-only reconnaissance first;
- preserve useful existing student-facing content;
- additive or narrowly scoped updates preferred;
- public Computing Commons files may be linked directly;
- no grades;
- no submissions required;
- no enrollment changes;
- no home-course mutation;
- no gradebook redesign;
- no destructive cleanup without HUMAN_GATE;
- no secret material in Canvas, GitHub, reports, or receipts.

If an existing Canvas module/page conflicts with the proposed teaching slice, report the conflict and show the proposed reconciliation before destructive replacement.

## QC contract

After any authorized deployment, Flo must read back and verify every object she creates or modifies.

QC should include:

- correct course lock (`24298`);
- module title/order;
- module item order;
- publication state;
- page title/body readback;
- public repository links;
- video links;
- code formatting;
- no accidental private GitHub links;
- no broken relative links;
- no accidental grading/submission settings;
- student-visible navigation from first item to last;
- no unrelated Canvas objects changed.

Preserve durable evidence under `sidecar/` in the owning repository.

## HUMAN_GATE conditions

Stop and ask Jeremy before:

- deleting or unpublishing existing student-visible content;
- materially renaming/reordering unrelated existing modules;
- creating assignments with points or submission requirements;
- changing due dates;
- changing enrollments;
- touching grades/submissions;
- mutating any Canvas course other than 24298;
- inventing a new interpretation where repository/design evidence is consequentially ambiguous.

## Promotion gate

Do not dispatch this draft until the companion design artifact says the slice is ready for Flo and Jeremy explicitly agrees to promotion.

The target state before dispatch is:

```text
curriculum stable enough to teach
        ↓
Morgan machine-path validation
        ↓
major friction repaired/documented
        ↓
video purposes and public companion files stable
        ↓
Jeremy says GO
        ↓
Flo reconciles + writes + QC's Canvas
```

The eventual job is a clean transition, not a full send.
