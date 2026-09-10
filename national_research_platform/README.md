# National Research Platform

The **National Research Platform (NRP)** is the Computing Commons runway from "my program runs on my computer" to "my program is a portable workload that can run in a larger computing ecosystem."

This material is shared curriculum. Individual courses can point here instead of rebuilding the same authentication, Kubernetes, container, evidence, cleanup, and remote-computing lessons over and over.

## What students should become able to do

The goal is not to memorize Kubernetes vocabulary. The goal is to become increasingly comfortable with these ideas:

1. **Identity** — prove who you are to a remote computing system.
2. **Authorization** — understand that identity and permission are different things.
3. **Namespace** — work inside the correct course workspace rather than "somewhere on the cluster."
4. **Workload** — describe finite work and ask a scheduler to run it.
5. **Container** — package an execution environment instead of depending on one lucky laptop.
6. **Evidence** — recover logs, status, resource information, and other receipts that show what actually happened.
7. **Cleanup** — remove what you created and verify that it is gone.
8. **Reproducibility** — move from one-off success toward work another environment can repeat.
9. **Resources and scale** — reason about CPU, memory, storage, GPUs, and scheduling instead of treating compute as invisible magic.
10. **Remote services** — eventually use hosted models and other services without leaking credentials or confusing a service token with Kubernetes identity.

## Start here

If this is your first NRP experience, begin with:

- [Getting Started](getting_started.md)
- [Curriculum Map](curriculum/README.md)
- [Curriculum Quality Standard](curriculum/QUALITY_STANDARD.md)

The first three student lessons are designed to be completed in order:

- [Lesson 1 — Identity, Access, and the Course Namespace](curriculum/01_identity_access_namespace.md)
- [Lesson 2 — Your First Remote Job](curriculum/02_first_remote_job.md)
- [Lesson 3 — Evidence, Cleanup, and Failure as Data](curriculum/03_evidence_cleanup_failure.md)

Then continue into the deeper shared strand:

- [Lesson 4 — Containers and Reproducibility](curriculum/04_containers_reproducibility.md)
- [Lesson 5 — Resources, Scheduling, and Scale](curriculum/05_resources_scheduling_scale.md)
- [Lesson 6 — Git and Remote Workloads](curriculum/06_git_remote_workloads.md)
- [Lesson 7 — Hosted LLMs as a Remote Service](curriculum/07_hosted_llms.md)
- [Lesson 8 — GPUs and Accelerators](curriculum/08_gpu_accelerators.md)
- [Lesson 9 — Remote Experiment Capstone](curriculum/09_remote_experiment_capstone.md)

## Student tools

Reusable public-safe helpers live here:

- [`scripts/student_preflight.sh`](scripts/student_preflight.sh) — read-only checks for `kubectl`, `kubelogin`, context, namespace access, and Job permission.
- [`templates/first_job.template.yaml`](templates/first_job.template.yaml) — a tiny CPU-only first Job template.
- [`templates/evidence_receipt.md`](templates/evidence_receipt.md) — a simple evidence receipt students can use after experiments.

## Course namespaces

A course should use an explicit namespace. Do not assume the default namespace is the right one.

For Fall 2026, Computer Science II uses:

```text
swosu-jevert-cs2-f26
```

The instructor namespace plan for the other Fall 2026 courses is documented at:

- [Fall 2026 NRP Namespace Plan](instructor/fall_2026_namespace_plan.md)

## How this fits the Computing Commons progression

The Commons uses cumulative levels.

- **Level 1 / CS1:** identity, safe remote access, first workload, evidence, cleanup.
- **Level 2 / CS2:** reproducibility, repeatable workloads, resource reasoning, Git-backed remote execution, stronger verification.
- **Level 3 / DSCT:** experiment design, assumptions, uncertainty, comparison, evidence quality, and interpretation.
- **Computer Architecture:** deeper inspection of CPU, memory, containers, scheduling, performance, and accelerators.
- **Later software engineering / ML work:** collaboration, automation, deployment, model services, GPU workloads, and larger experiments.

A later course should not force a student to relearn the first login from scratch. Earlier levels stay available as a recovery path while later work asks for stronger evidence and deeper reasoning.

## Instructor / validation material

Public-safe instructor notes live under [`instructor/`](instructor/). They are safe for students to read, but they are written to help an instructor test the pathway before releasing it broadly.

Current validation target:

- [Morgan Student-Surrogate Validation Plan](instructor/morgan_validation_plan.md)

## Safety boundaries

Do not put passwords, API tokens, kubeconfigs, private keys, protected student information, grades, or other reusable credentials into this repository, Canvas submissions, screenshots, chat, or assignment artifacts.

When something fails, preserve the **error and context**, not the secret.

## Canonical public references

Use the NRP documentation for current cluster-specific truth:

- NRP Getting Access: <https://nrp.ai/documentation/userdocs/start/getting-started/>
- NRP Using Nautilus: <https://nrp.ai/documentation/userdocs/start/using-nautilus/>
- NRP Basic Kubernetes Tutorial: <https://nrp.ai/documentation/userdocs/tutorial/basic/>
- NRP Cluster Policies: <https://nrp.ai/documentation/userdocs/start/policies/>

The Commons owns the **student learning path**. NRP owns the live service and its current operational documentation.
