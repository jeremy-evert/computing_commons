# NRP Canvas Teaching Slice — Design Space

Status: **DESIGN / STAGING — NOT YET DEPLOYED TO CANVAS**

Owner: Computing Commons
Canvas destination when promoted: **Computing Commons, course 24298**
Primary purpose: **teaching and learning, not grading**

## Why this artifact exists

The National Research Platform curriculum in `national_research_platform/curriculum/` is now broad enough to support a real learning sequence, but the next move should not be a full-course Canvas rewrite.

The right next move is a bounded teaching slice that lets students understand the NRP, authenticate, perform one small remote workload, observe what happened, clean up, and connect that experience to later Computer Science work.

This slice should be teachable across several short videos, supported by public files in this repository, and deployable to Canvas without creating a new grading pipeline.

The design principle is:

> **Teach one coherent journey. Let the public repository hold the durable files. Let Canvas provide the front door and sequence.**

## What this is not

This is not:

- a full rewrite of Computing Commons Canvas;
- a mirror of the GitHub directory tree;
- a Kubernetes certification unit;
- a new gradebook architecture;
- a scored assignment sequence;
- a requirement that every student master GPUs, hosted LLMs, or distributed systems immediately;
- a reason to duplicate canonical material already owned by another repository.

The first slice is intentionally small enough to teach, observe, revise, and redeploy cleanly.

## Student outcome for the first slice

By the end of this teaching artifact, a student should be able to explain and demonstrate the following chain:

```text
GitHub identity
      ↓
NRP account
      ↓
course namespace
      ↓
kubectl + kubeconfig
      ↓
small Kubernetes Job
      ↓
Pod / container execution
      ↓
logs and evidence
      ↓
cleanup
```

The student does not need to say, "I know Kubernetes."

A much better outcome is:

> "I understand how my identity gives me access to a shared computing workspace, how I can ask a remote system to run a finite workload, how I verify what happened, and why cleanup and evidence are part of the job."

## Recommended Canvas shape

Use **one bounded module** rather than immediately creating nine NRP modules.

Working module title:

> **National Research Platform — Your First Remote Workload**

The module should feel like a guided lab and mini-documentary rather than a list of files.

Recommended student-facing flow:

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

No graded assignment is required for this first deployment.

If Canvas completion requirements are useful for navigation, they may be used carefully, but the teaching artifact should remain valuable even with **zero points, no due date, and no submission box**.

## Video arc

The videos should be short enough that each has one memorable job.

### Video 1 — Your Laptop Is Not the Whole Computer

Target length: roughly 6–10 minutes.

Teaching goal:

Move the student's mental model from:

```text
code → my computer → result
```

into:

```text
code → remote computing request → scheduler → another machine → result
```

Topics:

- what the National Research Platform is;
- why a CS2 student is being introduced to it;
- cluster, namespace, Job, Pod, container at the minimum useful level;
- the idea that a personal computer can become a steering wheel rather than the engine;
- why reproducibility and remote execution matter beyond this one exercise.

Companion source:

- `national_research_platform/getting_started.md`
- `national_research_platform/curriculum/01_identity_access_namespace.md`

### Video 2 — Identity, Access, and the Course Namespace

Target length: roughly 7–12 minutes.

Teaching goal:

Help students understand that GitHub identity, NRP identity, namespace membership, Kubernetes authorization, and credentials are related but different things.

Topics:

- CILogon using GitHub for the current SWOSU path;
- why the student's GitHub account should be associated with their school email when possible;
- course namespace naming;
- installing `kubectl` and `kubelogin`;
- kubeconfig purpose and credential safety;
- selecting or explicitly naming the namespace;
- read-only verification before mutation;
- `kubectl auth can-i` as an authorization question rather than a hacking puzzle.

Primary live example for CS2 Fall 2026:

```text
swosu-jevert-cs2-f26
```

Important portability rule:

The public curriculum should not hard-code the CS2 namespace everywhere. Files and scripts should accept a namespace value so the same learning artifact can later serve CS1, DSCT, Computer Architecture, and future courses.

Companion sources:

- `national_research_platform/curriculum/01_identity_access_namespace.md`
- `national_research_platform/scripts/student_preflight.sh`

### Video 3 — Your First Remote Job

Target length: roughly 8–15 minutes.

Teaching goal:

Create the first satisfying remote-compute moment.

The workload should be deliberately tiny and CPU-only.

The student should see this lifecycle:

```text
describe work
    ↓
submit Job
    ↓
watch Job / Pod
    ↓
read logs
    ↓
verify completion
```

Topics:

- why a finite Kubernetes Job fits the task;
- YAML as a description of desired work rather than magical punctuation;
- container image;
- commands;
- CPU and memory requests/limits;
- why we do not request a GPU for a hello-world workload;
- Job vs Pod;
- reading logs as evidence.

Companion sources:

- `national_research_platform/curriculum/02_first_remote_job.md`
- `national_research_platform/templates/first_job.template.yaml`

### Video 4 — Failure Is Data, and Cleanup Is Part of Success

Target length: roughly 7–12 minutes.

Teaching goal:

Make observability and cleanup part of the student's definition of "done."

Topics:

- capture exact commands and exact errors;
- distinguish authentication, authorization, scheduling, workload, and application failures;
- inspect before changing things randomly;
- why "No resources found" can be a success condition;
- why a completed experiment still leaves a cleanup responsibility;
- verifying deletion;
- what belongs in an evidence receipt;
- what absolutely does not belong in an evidence receipt, especially tokens, kubeconfigs, passwords, and private keys.

Companion sources:

- `national_research_platform/curriculum/03_evidence_cleanup_failure.md`
- `national_research_platform/templates/evidence_receipt.md`

### Video 5 — Where the Road Goes Next

Target length: roughly 5–10 minutes.

This can be recorded now or deferred until the first four videos survive Morgan and Student One.

Teaching goal:

Connect the tiny first workload to the larger Computing Commons curriculum without drowning the student in future vocabulary.

Preview:

- containers and reproducibility;
- resource requests and scheduling;
- Git and remote workloads;
- hosted LLMs as remote services;
- GPUs and accelerators;
- reproducible remote experiments.

Companion curriculum:

- `04_containers_reproducibility.md`
- `05_resources_scheduling_scale.md`
- `06_git_remote_workloads.md`
- `07_hosted_llms.md`
- `08_gpu_accelerators.md`
- `09_remote_experiment_capstone.md`

## Public-repository artifact strategy

Because `jeremy-evert/computing_commons` is public, the student should be able to obtain the durable files directly from the repository.

Canvas does not need to duplicate every file.

Prefer this relationship:

```text
Canvas page / video
        ↓
explains what to do and why
        ↓
public Computing Commons file
        ↓
student runs / edits / inspects it
        ↓
Canvas points to the next learning step
```

Candidate public artifacts already present:

- `getting_started.md`
- `scripts/student_preflight.sh`
- `templates/first_job.template.yaml`
- `templates/evidence_receipt.md`
- curriculum lessons 01–09

During Morgan validation, prefer testing these exact public files instead of creating private instructor-only substitutes.

## No-grade design

The absence of a grading pipeline is a feature for this first release.

This frees the Canvas experience to optimize for:

- understanding;
- confidence;
- experimentation;
- useful failure;
- troubleshooting;
- evidence habits;
- curiosity;
- connection to later CS work.

A student's evidence receipt can be used as a learning artifact without being submitted or scored.

If a home course later wants a graded application, that course should own the graded wrapper around the shared Commons capability.

Example:

```text
Commons teaches: run and verify a remote Job
CS2 applies: run a CS2 algorithm remotely and compare behavior
Architecture applies: inspect machine/runtime characteristics
DSCT applies: design and interpret an experiment
```

This preserves the Commons as the shared apprenticeship layer rather than turning it into another academic course.

## Morgan validation role

Morgan is the student-surrogate machine for the first technical pass.

Morgan should test the public journey from as close to zero as practical:

```text
public repo
   ↓
student instructions
   ↓
required tools
   ↓
authentication
   ↓
namespace
   ↓
preflight
   ↓
first Job
   ↓
logs
   ↓
cleanup
```

Record friction rather than silently fixing around it.

Particularly valuable observations:

- ambiguous installation steps;
- commands that assume the wrong shell or directory;
- Windows/WSL path confusion;
- missing dependencies;
- hidden assumptions about Git, Python, Linux, or Kubernetes;
- authentication prompts that differ from the written guide;
- namespace assumptions;
- error messages a student would not know how to classify;
- public links that are awkward to discover or download;
- steps that are technically correct but pedagogically exhausting.

Morgan validates the **machine path**.

Student One validates the **human path**.

Both matter before broad promotion.

## Canvas deployment posture for Flo

Flo should eventually receive a bounded deployment mission, not an invitation to redesign the Commons.

Her job should be:

1. inspect the live Computing Commons Canvas course read-only;
2. reconcile this teaching-slice design against the existing student experience;
3. build one clean NRP teaching module in course 24298;
4. render the learning sequence as Canvas pages/module items, not as a filesystem mirror;
5. link to the public repository artifacts where appropriate;
6. preserve useful existing course content;
7. avoid grades, enrollments, submissions, and home-course mutation;
8. read back and QC every created/modified Canvas object;
9. leave durable evidence in `sidecar/`;
10. stop at a human gate before destructive replacement or consequential reorganization.

Until Morgan validation and the student-facing materials are sufficiently clean, this remains a design artifact rather than a dispatch authorization.

## What "ready for Flo" means

The teaching slice is ready for Flo when:

- the first four videos have a stable instructional purpose and companion artifact;
- Morgan can follow the public path far enough to expose the major friction points;
- those friction points have either been repaired or deliberately documented;
- the student-facing public links are stable;
- the namespace parameterization is clear enough to avoid making CS2 the accidental permanent default for every class;
- no secret or private credential appears in the public material;
- the Canvas module order is settled;
- the expected Canvas scope is one bounded module in course 24298;
- the repository remains the source of truth;
- Jeremy is comfortable saying: "This is ready to teach, now make it clean in Canvas."

## Open design questions to resolve through testing

These are not blockers yet. They are questions Morgan and Student One can answer for us.

### How much installation belongs in the first video sequence?

Possibilities:

- fully teach installation inside Video 2;
- make installation a companion page/checklist and keep the video conceptual;
- create a small platform-specific appendix for Windows/WSL, macOS, and Linux.

Preference for testing: keep the main video coherent and move brittle version-specific installation details into the public written guide when possible.

### Should students clone the whole Commons repo or download only the NRP folder/files?

Morgan should test both ergonomics.

Cloning the repository strengthens Git habits and makes later updates easy, but a first-time student may reasonably want the smallest path to one template.

The final student experience can support both without teaching two competing workflows.

### Should the first Job be YAML-first or script-assisted?

The YAML-first path teaches what Kubernetes is actually being asked to do.

A later script-assisted path can reduce repetitive command work.

Preference for the first teaching slice: show the YAML once, then allow a helper script after the student understands the pieces.

### How visible should the deeper 04–09 curriculum be in Canvas?

Do not dump all future lessons into the first module.

A single "Where This Goes Next" page can preview the road while the public repository already contains the deeper curriculum for curious students.

## Current recommendation

Build and test the **first four-video teaching slice** first.

Treat Video 5 and curriculum 04–09 as the next horizon rather than current deployment scope.

That gives us a compact experimental unit:

```text
UNDERSTAND
    ↓
AUTHENTICATE
    ↓
RUN
    ↓
OBSERVE
    ↓
CLEAN UP
    ↓
EXPLAIN WHAT HAPPENED
```

If that journey becomes boring and reliable on Morgan and understandable to Student One, we have earned the right to expand it.
