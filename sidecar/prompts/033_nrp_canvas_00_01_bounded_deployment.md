# Prompt 033 — NRP Canvas 00+01 Bounded Deployment

Status: **AUTHORIZED FOR BOUNDED CANVAS DEPLOYMENT**

## Owner authorization

Jeremy explicitly authorizes this bounded Computing Commons Canvas deployment now.

The purpose is to put the first two National Research Platform teaching artifacts in front of students so Jeremy can teach **01 — Your Laptop Is Not the Whole Computer** directly from Canvas and record the video while working through the material with the class.

This is **not** authorization for the full NRP curriculum, a whole-course redesign, or a grade-bearing deployment.

## Operating route

Use the established production operating model:

```text
Flo — Lead Foreman on Brandy
        ↓ routes the bounded student-bound write
Anna — Assistant Foreman on April
        ↓ deploys with the established Canvas/Harbor boundary
Flo
        ↓ performs final live QC / sign-off
Computing Commons Canvas
```

Flo may choose to perform the Canvas write herself from Brandy if that is materially safer based on current live truth, but the preferred route for this clean content load is **Anna on April**, with Flo retaining final sign-off.

Do not send Canvas work to Ivy. Ivy never touches Canvas.

## Canvas target

The only authorized Canvas course is:

```text
Computing Commons
course_id = 24298
```

Before any mutation, read the live course metadata and independently verify that course `24298` is Computing Commons.

If the identity does not match, stop at `HUMAN_GATE` without writing anything.

## Repository source of truth

Public repository:

```text
jeremy-evert/computing_commons
```

Read and follow `AGENTS.md`.

Before work:

1. `git fetch origin`;
2. verify the checkout is at current `origin/main` or use a deliberately isolated worktree from current `origin/main`;
3. inspect current Canvas state read-only before deciding what needs to be created or reconciled.

Do not deploy from a stale checkout.

## Exact teaching artifacts authorized now

### 00 — Start Here

Student source:

```text
national_research_platform/teaching_slice/00_start_here.md
```

Canvas title:

> **00 — Start Here: What Are We About to Do?**

### 01 — Your Laptop Is Not the Whole Computer

Student source:

```text
national_research_platform/teaching_slice/01_your_laptop_is_not_the_whole_computer.md
```

Canvas title:

> **01 — Your Laptop Is Not the Whole Computer**

Instructor recording companion:

```text
national_research_platform/instructor/video_scripts/01_your_laptop_is_not_the_whole_computer.md
```

The instructor script is source context for Jeremy's teaching/recording flow. Do **not** expose raw recording directions such as screen cues, recording cautions, or instructor-only notes as the student-facing Canvas page. The student-facing 01 file above is the Canvas body authority.

## Canvas shape

Create or reconcile one bounded module titled:

> **National Research Platform — Your First Remote Workload**

For this deployment, the module needs only two student-visible items, in this exact order:

```text
00 — Start Here: What Are We About to Do?
01 — Your Laptop Is Not the Whole Computer
```

Do not create placeholder items for 02–08 yet.

The broader planned sequence remains in:

```text
national_research_platform/instructor/canvas_teaching_slice_design.md
```

but it is future scope.

## Teaching posture

This is a **teaching and learning artifact**, not a graded assignment pipeline.

Do not create:

- points;
- assignments merely to hold the content;
- submission requirements;
- gradebook entries;
- due dates;
- rubrics;
- assignment groups;
- enrollment changes;
- completion requirements that accidentally behave like graded work.

Normal Canvas Pages inside a Module are preferred.

Jeremy wants to open 01 in Canvas, teach from that page, and make the accompanying video while moving through what students need to see.

The page should therefore be readable on its own during class, with clean headings, diagrams/code blocks, and no instructor-only stage directions.

## Read-only reconnaissance first

Before writing:

1. inspect course `24298` live;
2. inspect existing module titles and relevant NRP/page titles;
3. determine whether an NRP module or either page already exists;
4. avoid blind duplication;
5. preserve useful existing student-facing material;
6. determine the safest additive/idempotent reconciliation.

If similarly named content exists and can be safely updated or reused without destructive changes, reconcile it narrowly.

If resolving a collision would require deleting, unpublishing, or materially repurposing unrelated student-visible content, stop at `HUMAN_GATE` and show the conflict.

## Publication state

Jeremy intends to teach from this immediately.

After successful write + readback QC, the module and both pages should be **published/student-visible**.

Do not leave the finished slice silently unpublished unless Canvas or current repository truth reveals a concrete safety reason. If so, report the reason as a gate.

## Public links

`jeremy-evert/computing_commons` is public.

It is acceptable to link students to public Computing Commons NRP material when useful. Prefer a small number of deliberate links over turning the Canvas page into a GitHub directory mirror.

Any public link used must be checked for accessibility.

Do not include private operator repositories, credential-bearing links, local absolute paths, or host-specific instructor paths.

## Safety boundaries

Do not expose or request:

- Canvas API tokens;
- kubeconfigs;
- NRP tokens;
- API keys;
- private keys;
- passwords;
- student private information;
- reusable credentials.

No mutation outside Canvas course `24298` is authorized.

Do not touch CS1, CS2, DSCT, Computer Architecture, or any other Canvas course during this mission.

Do not alter grades, submissions, enrollments, assignment weights, existing graded objects, or due dates.

Do not perform broad module cleanup or course reorganization.

Morgan validation continues separately and is **not a prerequisite for this intentionally small 00+01 deployment**. Future lessons may be refined from Morgan evidence before they are promoted.

## Implementation preference

Use the existing tested Canvas/Harbor deployment boundary already proven in Computing Commons work.

If a small target-locked, idempotent deployment script materially improves repeatability, create it in the owning repository and keep it narrow to this module/slice. Reuse existing `harbor` patterns rather than inventing a second Canvas client.

A script is not required if the established bounded deployment path already makes the write safely and reproducibly.

## QC contract

After writing, independently read back the live Canvas objects and verify at minimum:

1. course id `24298` reads as Computing Commons;
2. exactly one intended NRP teaching module is used for this slice;
3. module title is correct;
4. item order is 00 then 01;
5. both items resolve to the intended Canvas Pages;
6. page titles are correct;
7. the rendered/student-facing content corresponds to the public student source files;
8. code blocks and text diagrams remain readable;
9. module and pages are published/student-visible;
10. public links used by the pages resolve;
11. no private-repository link is exposed;
12. no credential-shaped material is exposed;
13. no graded object, submission requirement, due date, enrollment, grade, or unrelated Canvas object was changed;
14. 01 is usable by Jeremy as the live teaching surface for recording the first video.

Do not treat a successful POST/PUT as proof of success. Readback is required.

## Durable evidence

Leave a durable report in the owning repository at:

```text
sidecar/reports/033_nrp_canvas_00_01_bounded_deployment.md
```

The report should record, without secrets:

- repository commit used as source;
- Canvas course identity readback;
- pre-deployment reconnaissance;
- objects created or reconciled;
- module/page IDs or slugs;
- publication state;
- item order;
- link/QC results;
- confirmation that no graded/enrollment surfaces were touched;
- any implementation script created;
- Flo's final live QC result;
- any remaining HUMAN_GATE or follow-up.

A compact machine-readable receipt under `sidecar/runs/` is encouraged if it fits existing practice.

Commit and push normal durable repository artifacts according to repository policy.

## HUMAN_GATE conditions

Stop and ask Jeremy only if:

- course `24298` does not identify as Computing Commons;
- current Canvas credentials are unavailable and require a human login/token action;
- an existing page/module collision requires destructive replacement;
- the intended two-page sequence cannot be made student-visible without altering grades, submissions, enrollment, or unrelated content;
- a consequential ambiguity remains after inspecting current repository and Canvas truth.

## Acceptance

This bounded mission is complete when Jeremy can open Computing Commons Canvas and see:

```text
National Research Platform — Your First Remote Workload
    00 — Start Here: What Are We About to Do?
    01 — Your Laptop Is Not the Whole Computer
```

Both are clean, published student-facing pages, 00 leads naturally into 01, and 01 is strong enough for Jeremy to teach directly from Canvas while recording.

The target is not the whole NRP curriculum today.

The target is a **clean first two steps with evidence that the Canvas transition stayed clean**.
