# Lesson 8 — GPUs and Accelerators

## Why this matters

A GPU is not a magic "make code fast" button.

It is specialized hardware that can be extremely effective for the right kind of parallel work and nearly useless for the wrong kind.

This lesson comes **after** students can already run, observe, verify, and clean up ordinary CPU workloads. Specialized hardware should solve a real computational problem, not serve as decorative horsepower.

## Learning outcomes

By the end of this lesson, you should be able to:

- explain why a GPU differs from a general-purpose CPU;
- identify workloads that are plausible GPU candidates;
- inspect whether a remote environment can see an accelerator;
- distinguish requesting a GPU from actually using it effectively;
- explain why GPU utilization matters on a shared cluster;
- design a small CPU-vs-GPU comparison without overclaiming the result.

## Mental model

A simplified model is:

```text
CPU
  -> fewer powerful general-purpose cores
  -> excellent for control-heavy, serial, and mixed workloads

GPU
  -> many parallel execution units
  -> excellent for selected highly parallel workloads
```

Real hardware is more nuanced than that, but this distinction is a useful starting point.

The important question is not:

> Can I get a GPU?

The important question is:

> Does the structure of my workload give a GPU useful work to do?

## Before you begin

Do not request a GPU unless:

- the instructor has opened this lesson;
- your course namespace has appropriate accelerator access/quota;
- your workload and container image actually support the GPU stack you intend to use;
- you already have a CPU baseline for comparison when comparison is the learning goal.

Read the current NRP Cluster Policies before accelerator work:

<https://nrp.ai/documentation/userdocs/start/policies/>

NRP expects expensive resources to be used efficiently.

## Step 1 — Classify candidate workloads

For each example, decide whether you would expect a GPU to help and explain why:

```text
print("hello")
sorting 50 integers
matrix multiplication on very large matrices
training a neural network
rendering/parallel image operations
reading one configuration file
large vector operations
```

Do not worry about being perfect. The goal is to connect **algorithm structure** with **hardware structure**.

## Step 2 — Establish a CPU baseline first

Choose an instructor-approved program with enough work to measure meaningfully.

Record:

```text
source commit
container image
input size
CPU request
runtime measurement
result correctness check
```

Run it more than once when startup noise could dominate the measurement.

Do not compare one lucky CPU run against one unlucky GPU run and call that science.

## Step 3 — Request an accelerator only in the approved workload

GPU syntax and resource names are cluster-specific enough that this curriculum should not freeze a stale manifest forever.

Use the current instructor-provided/NRP-supported example for the accelerator type available to the course.

Before applying it, identify:

```text
namespace
GPU resource request
gpu-capable image
command
CPU/memory resources
finite deadline
cleanup path
```

Never add a GPU request to the Day-One hello Job.

## Step 4 — Verify visibility and actual use

Merely receiving a GPU-backed Pod does not prove the program used the accelerator effectively.

Depending on the workload/toolchain, useful evidence may include:

- framework reports that a CUDA/accelerator device is available;
- device name/model;
- framework-selected device;
- timing comparison;
- NRP monitoring/utilization evidence;
- logs showing work was actually sent to the accelerator.

The exact evidence depends on the software stack.

## Step 5 — Compare carefully

A useful comparison tries to hold important variables constant:

```text
same source commit
same input
same algorithm
known container/runtime differences
multiple runs when practical
correctness checked on both paths
```

Then ask:

```text
Did the GPU reduce compute time?
Was startup/transfer overhead important?
Was the problem large enough to benefit?
Did both paths produce equivalent results?
What limitations remain in the comparison?
```

## Computer Architecture connection

This lesson is a natural bridge into architecture because performance emerges from the interaction among:

- algorithm;
- instruction/data parallelism;
- memory hierarchy;
- transfer costs;
- runtime/framework;
- compiler/library choices;
- hardware architecture;
- problem size.

A performance result is not just a property of "the code."

It is a property of the code **running in a particular computational context**.

## Failure as data

Possible accelerator failures include:

- namespace has no GPU quota;
- Pod cannot be scheduled;
- image lacks required accelerator libraries;
- framework cannot see the device;
- CPU fallback happens silently;
- program uses the GPU but performance is worse because the workload is too small;
- requested accelerator type is unavailable;
- program consumes little of the reserved GPU.

Each tells you something different.

A Pending Pod is not the same failure as a framework that starts on CPU.

## Evidence receipt

Record:

```text
Lesson: NRP 08 GPUs and Accelerators
Course namespace:
Source commit:
Input size:
CPU baseline result/runtime:
Accelerator type requested:
Accelerator visibility evidence:
GPU/accelerator result/runtime:
Correctness comparison:
Observed utilization evidence if available:
One reason the comparison may be imperfect:
Cleanup proof:
```

## Reflection

1. Why can a GPU-backed run be slower than a CPU run for a small problem?
2. Why is "Pod scheduled on a GPU node" weaker than "program demonstrably used the GPU"?
3. Which characteristics of an algorithm make specialized parallel hardware attractive?
4. What evidence would justify requesting the accelerator again?

## Next

Continue to:

[Lesson 9 — Remote Experiment Capstone](09_remote_experiment_capstone.md)
