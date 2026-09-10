# Lesson 9 — Remote Experiment Capstone

## Why this matters

By this point, the interesting question is no longer whether you can make Kubernetes run something.

The stronger question is:

> **Can another person inspect what you did, understand why you did it, evaluate the evidence, and reproduce the important parts?**

That is the difference between a remote-computing trick and an actual computational experiment.

## Learning outcomes

By the end of this lesson, you should be able to:

- state a small computational question or claim;
- identify the variables you intend to change and hold constant;
- connect source, runtime, workload, and evidence through durable identifiers;
- perform multiple bounded remote runs when comparison requires them;
- distinguish observation from interpretation;
- state limitations and uncertainty;
- leave a clean namespace and a durable experiment report.

## Before you begin

Complete the earlier NRP lessons appropriate to your course.

Your instructor may supply the experiment question or allow you to choose one.

A good first capstone is narrow enough to finish and inspect.

Examples:

- compare two implementations of the same algorithm;
- compare the same program under two CPU resource requests;
- compare two input sizes;
- compare local versus remote runtime behavior;
- compare CPU versus GPU only when an accelerator is genuinely appropriate;
- run repeated simulations and summarize variation;
- compare two versions of a program connected to two Git commits.

## Mental model

A computational experiment should form a chain like this:

```text
QUESTION / CLAIM
      ↓
ASSUMPTIONS
      ↓
SOURCE + INPUT + ENVIRONMENT
      ↓
WORKLOAD DEFINITION
      ↓
REMOTE EXECUTION
      ↓
OBSERVATIONS
      ↓
EVIDENCE
      ↓
INTERPRETATION
      ↓
LIMITATIONS
      ↓
CLEANUP + DURABLE REPORT
```

Skipping the middle and jumping directly from "I ran code" to "therefore my claim is true" is not enough.

## Step 1 — Write the question first

Before launching anything, write one sentence:

```text
I want to determine whether ______________________________.
```

Then identify:

```text
What will I change?
What will I hold constant?
What will I measure or observe?
What result would count as evidence?
```

If you cannot answer those questions, the experiment is not ready to run.

## Step 2 — Establish provenance

Record the exact source state:

```bash
git status
git rev-parse HEAD
```

If the working tree contains uncommitted changes that matter to the experiment, either commit them intentionally or explain why the experiment cannot yet be tied to a durable source identity.

Also record:

```text
container image/tag
course namespace
input identity/version
important parameters
resource requests/limits
```

## Step 3 — Define bounded runs

Each run should have:

- a unique, meaningful Job name;
- explicit namespace;
- finite completion behavior;
- reasonable CPU/memory resources;
- accelerator request only when justified;
- logs or output that can be recovered;
- a narrow cleanup command.

If you need multiple runs, name them so another person can understand the comparison.

Example:

```text
jsmith-sort-n1000-a
jsmith-sort-n1000-b
jsmith-sort-n10000-a
jsmith-sort-n10000-b
```

## Step 4 — Run without moving the goalposts

Once the comparison starts, avoid changing unrelated variables between runs.

If you discover that a change is necessary, record it and restart the comparison cleanly rather than quietly mixing incompatible runs.

This is where Git and explicit workload definitions become useful safeguards.

## Step 5 — Collect observations

Depending on the experiment, collect only the evidence that matters.

Possible evidence:

```text
Job completion status
program output
runtime measurements
resource requests
Pod events
hardware/device information
repeated-run measurements
correctness checks
logs
Git commit
container image
```

Do not equate "more output" with "better evidence."

A focused table of relevant measurements is usually stronger than a 400-line terminal dump.

## Step 6 — Analyze honestly

Separate:

### Observation

```text
Run A completed in 1.82 seconds.
Run B completed in 1.21 seconds.
```

### Interpretation

```text
Under these conditions, Run B was faster in this measurement.
```

### Overclaim

```text
Run B is always the better algorithm everywhere.
```

The first two may be supported. The third likely requires much more evidence.

## Step 7 — State limitations

A strong experiment report contains a section titled:

```text
Limitations
```

Possible limitations include:

- few repetitions;
- startup overhead;
- uncontrolled cluster scheduling differences;
- mutable external service;
- different hardware;
- small input size;
- measurement precision;
- nondeterministic program behavior;
- incomplete utilization data.

A limitation does not destroy the experiment. It tells the reader how far the evidence can reasonably travel.

## Step 8 — Clean up

Delete only the Jobs/resources created for your experiment.

Then independently verify they are gone.

Your final report should include cleanup evidence.

The experiment is not finished while your abandoned resources are still running in a shared namespace.

## Durable capstone report

Use this structure:

```text
# Experiment title

## Question / claim
## Why this matters
## Assumptions
## Source provenance
## Runtime/container environment
## Namespace and workload shape
## Inputs and parameters
## Procedure
## Observations
## Evidence table
## Interpretation
## Limitations
## Cleanup proof
## Reproduction instructions
## What I would test next
```

Do not include credentials.

## Course-specific lenses

### Computer Science II

Focus on program design, data structures/algorithms, source versions, testing, repeatable execution, and the difference between code behavior and environment behavior.

### Discrete Structures & Critical Thinking

Focus on claims, assumptions, probability/simulation when relevant, repeated observations, uncertainty, logical interpretation, and what the evidence does not prove.

### Computer Architecture

Focus on runtime context, CPU/memory behavior, hardware differences, timing, profiling, accelerator suitability, utilization, and the relationship between software structure and machine structure.

### Software Engineering / ML later

Focus on automation, collaboration, CI, deployment, model/data provenance, evaluation, reproducibility, and operating boundaries.

## Failure as data

A failed run belongs in the experiment history when it taught you something relevant.

Record:

```text
what failed
how you classified the failure
what evidence supported that classification
what single change you made next
whether the next run resolved the problem
```

Do not rewrite the story so the experiment appears magically perfect from the beginning.

## Evidence receipt

For this capstone, the report itself is the primary receipt.

At minimum it must identify:

```text
source commit
namespace
workload(s)
container image(s)
important inputs/parameters
observed result(s)
interpretation
limitations
cleanup proof
```

## Reflection

1. What part of your conclusion is directly supported by evidence?
2. What part remains uncertain?
3. What would another person need to reproduce the experiment?
4. Which uncontrolled variable would you reduce first if you repeated the work?
5. What did remote execution teach you that a purely local run would have hidden?

## End state

A successful capstone leaves behind **knowledge and evidence**, not abandoned Pods.

That is the target habit for the whole NRP strand.
