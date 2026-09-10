# Lesson 5 — Resources, Scheduling, and Scale

## Why this matters

A shared cluster cannot give every workload "all the CPU, all the RAM, and maybe a GPU just in case."

Resource requests are part of how your program communicates with the scheduler. They are also part of being a good citizen on shared infrastructure.

This lesson asks you to stop treating CPU and memory as invisible background machinery.

## Learning outcomes

By the end of this lesson, you should be able to:

- distinguish a resource request from a resource limit;
- explain why schedulers need resource information;
- inspect the resources requested by a workload;
- compare two small workloads with intentionally different resource shapes;
- recognize why over-requesting is harmful;
- explain when scale helps and when it merely adds complexity.

## Mental model

A scheduler has to decide where work can fit.

A useful first approximation is:

```text
Job says what it needs
      ↓
Scheduler compares needs with available capacity
      ↓
Pod is placed on a suitable node
      ↓
Container runs within the declared boundaries
```

### Request

A **request** tells Kubernetes what capacity the workload needs to be scheduled.

### Limit

A **limit** places an upper bound on what the container may consume for that resource.

Those are related but not identical concepts.

## Step 1 — Read the resource block

A tiny first Job might contain:

```yaml
resources:
  requests:
    cpu: "10m"
    memory: "16Mi"
  limits:
    cpu: "50m"
    memory: "32Mi"
```

For CPU, `1000m` is approximately one CPU core of requested capacity. `10m` is a tiny fraction of one core.

For memory, `Mi` is mebibytes.

The point is not to memorize units. The point is to ask:

> What does this workload reasonably need?

## Step 2 — Inspect a Job's declared resources

For a Job you own:

```bash
kubectl get job YOUR_JOB -n YOUR_COURSE_NAMESPACE -o yaml
```

Find the `resources:` section.

You may also inspect the Pod created by the Job:

```bash
kubectl get pods -n YOUR_COURSE_NAMESPACE -l job-name=YOUR_JOB -o yaml
```

Do not publish large raw YAML dumps merely to prove completion. Use them for investigation, then extract the evidence that matters.

## Step 3 — Compare two bounded resource shapes

Run the same tiny finite command twice with two reasonable CPU request values, for example:

```text
Run A: 10m CPU request
Run B: 50m CPU request
```

Keep the program, image, and input the same.

Do not intentionally request absurd values. We are learning resource reasoning, not testing how annoyed a shared scheduler can become.

Record:

```text
Was either run delayed?
Did both complete?
Did the result change?
What changed in the workload declaration?
```

The purpose is to see that resource declarations are part of orchestration even when a tiny program's output does not change.

## Step 4 — Learn what scale does not mean

More resources do not automatically make every program faster.

Examples:

- a single-threaded program may not benefit from many CPU cores;
- a tiny workload may spend more time starting than computing;
- a memory-light program gains nothing from requesting huge RAM;
- a GPU does not accelerate arbitrary code merely because one is present;
- distributed execution can add coordination and communication costs.

Scale is a design choice, not a synonym for quality.

## Step 5 — Connect this to Computer Architecture

Resource requests are a bridge from software to hardware questions.

Later you can ask:

- Is this program CPU-bound, memory-bound, I/O-bound, or waiting on something else?
- Does the workload actually use the resources it requests?
- Does architecture or accelerator type change performance?
- What does the scheduler know about hardware that the source code does not?

Those are architecture questions hiding inside an orchestration interface.

## NRP policy connection

NRP expects users to right-size workloads and avoid wasting reserved resources. Current cluster policy emphasizes using finite Jobs for batch work, setting appropriate requests, monitoring usage, and freeing resources when computation is done.

Read the current policy before larger experiments:

<https://nrp.ai/documentation/userdocs/start/policies/>

## Failure as data

A Pod that remains `Pending` may be giving you scheduling information rather than a program error.

Inspect:

```bash
kubectl get pods -n YOUR_COURSE_NAMESPACE
kubectl describe pod POD_NAME -n YOUR_COURSE_NAMESPACE
```

Look at Events.

Possible causes include insufficient resources, quota, affinity/placement constraints, or another scheduling rule.

Do not immediately increase every request. First understand why the scheduler said no.

## Evidence receipt

Record:

```text
Lesson: NRP 05 Resources, Scheduling, Scale
Course namespace:
Program/image held constant:
Run A resource requests:
Run B resource requests:
Observed difference:
One reason over-requesting harms a shared cluster:
One reason more resources might NOT make my program faster:
Cleanup proof:
```

## Reflection

1. Why does Kubernetes need a resource request before the program actually runs?
2. When would a larger CPU request be justified by evidence?
3. Why should GPU access be introduced only when the workload can use a GPU meaningfully?

## Next

Continue to:

[Lesson 6 — Git and Remote Workloads](06_git_remote_workloads.md)
