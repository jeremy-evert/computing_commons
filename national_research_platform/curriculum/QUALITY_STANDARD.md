# NRP Curriculum Quality Standard

Status: **ACTIVE DESIGN CONTRACT**

This file defines the expected quality and shape of National Research Platform lessons in Computing Commons.

The purpose is consistency. Students should not encounter one lesson that reads like a friendly workshop and the next that reads like a vendor manual dropped from orbit.

## Core teaching promise

Every NRP lesson should help the student answer three questions:

1. **What is this?**
2. **What can I do with it?**
3. **Why does this matter in my computer science journey?**

Technical instructions without a mental model are incomplete. A mental model without a real task is also incomplete.

## Required lesson anatomy

Each full lesson should contain these sections unless there is a strong reason not to:

### 1. Why this matters

Give the student a short conceptual reason to care. Connect the lesson to software development, systems, reproducibility, evidence, or later coursework.

### 2. Learning outcomes

Use observable outcomes. Prefer "verify namespace access" over "understand namespaces."

### 3. Before you begin

State prerequisites, required tools, expected namespace, and any human/instructor gate.

### 4. Mental model

Explain the smallest useful model before introducing commands.

Good:

```text
GitHub identity -> NRP account -> course namespace -> Kubernetes permission
```

Less useful:

```text
Here are twelve kubectl commands. Good luck.
```

### 5. Do the smallest real thing

Prefer a small, bounded, inspectable task over a large demo.

The first success should normally be CPU-only and low-resource. GPU use belongs later when the learning outcome actually requires an accelerator.

### 6. Verify independently

A command returning without an obvious error is not enough. Students should retrieve another piece of evidence that confirms what happened.

Examples:

- inspect Job status;
- retrieve Pod logs;
- compare requested versus observed resources;
- verify a deleted object is gone;
- inspect a Git diff/commit;
- compare two experimental runs.

### 7. Clean up

If the lesson creates a remote object, it should normally teach cleanup and independent cleanup verification.

Cleanup should target only the object the student created. Avoid broad deletes.

### 8. Failure as data

Give the student at least one useful troubleshooting path. Teach them to preserve the exact command, expected result, actual result, and error/status without sharing secrets.

### 9. Evidence receipt

Every practical lesson should end with a compact student-owned receipt. The receipt should record what happened, not merely claim completion.

### 10. Reflection / transfer

End with one or two questions that move the student from syntax to computer science meaning.

Examples:

- What part of this execution depended on your laptop, and what part did not?
- What did the container make reproducible?
- What would change if ten students launched this at once?
- Which evidence would convince another person that your result is repeatable?

## Safety invariants

NRP lessons must not teach students to:

- publish passwords, tokens, kubeconfigs, private keys, or secret environment files;
- use instructor automation credentials;
- bypass RBAC because a permission check returned `no`;
- force-delete Pods as routine recovery;
- launch endless Jobs using `sleep` or equivalent commands;
- request GPUs for work that does not need GPUs;
- delete broad namespace resources as cleanup;
- put protected student information, grades, or sensitive records on NRP.

## Namespace invariant

Student commands that create, inspect, or delete Kubernetes resources should normally make the intended namespace visible in the command or the surrounding verified context.

For shared/public instructions, prefer explicit examples such as:

```bash
kubectl get pods -n YOUR_COURSE_NAMESPACE
```

Do not assume a student's current namespace is correct merely because a previous lesson set it once.

## Evidence ladder

Lessons should progressively strengthen evidence rather than repeating the same screenshot ritual.

### Level 1

Command + result + simple cleanup proof.

### Level 2

Command + result + logs/status + resource intent + cleanup proof + Git provenance when code is involved.

### Level 3

Comparative evidence, assumptions, uncertainty, interpretation, and explanation of what the evidence does **not** prove.

### Architecture bridge

Runtime inspection, CPU/memory/process/container evidence, performance measurements, and accelerator visibility.

### Later engineering / ML

Repeatability across runs, automated validation, collaboration evidence, model/data provenance, evaluation, and deployment boundaries.

## Consistent voice

Write directly to the student. Assume intelligence and curiosity, not prior infrastructure experience.

Prefer:

> "Ask Kubernetes whether your identity may create Jobs. If it says `no`, preserve that result and stop. Permission is part of the system design."

Avoid:

> "Simply configure RBAC appropriately."

The first version teaches. The second version assumes the student already knows the thing we are trying to teach.

## The boring-success rule

Early infrastructure lessons should optimize for **boringly reliable success**.

A tiny Job that prints one line and cleans itself up teaches more on Day One than a GPU workload with six dependencies and three mystery failures.

Complexity should be earned by the learning outcome.

## Canonical-source rule

Computing Commons owns the student learning path. The NRP owns current service-specific operational truth.

When live NRP details change, link to or reconcile against the official NRP documentation rather than freezing undocumented assumptions into the curriculum.

Primary references:

- <https://nrp.ai/documentation/userdocs/start/getting-started/>
- <https://nrp.ai/documentation/userdocs/start/using-nautilus/>
- <https://nrp.ai/documentation/userdocs/tutorial/basic/>
- <https://nrp.ai/documentation/userdocs/start/policies/>

## Acceptance test for a lesson

A lesson is not done because the Markdown looks polished.

A strong lesson should survive this question:

> **Could a student who has never used this system follow the path, know what success looks like, know what not to expose, and explain why the task mattered afterward?**

If not, keep working.
