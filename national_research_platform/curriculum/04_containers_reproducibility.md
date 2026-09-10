# Lesson 4 — Containers and Reproducibility

## Why this matters

A program that works only on one lucky laptop is fragile.

Containers help separate **your code** from the accidental details of **your machine**. They give you a way to describe an execution environment that another system can obtain and run.

This lesson moves from "Kubernetes ran a container" to "I can reason about what the container contributes to reproducibility."

## Learning outcomes

By the end of this lesson, you should be able to:

- explain the difference between a host machine and a container environment;
- identify the image used by a Kubernetes workload;
- explain why image tags/versions matter;
- compare local and remote runtime observations;
- make one small workload more reproducible by making its environment explicit;
- identify what a container does **not** automatically make reproducible.

## Before you begin

Complete Lessons 1–3.

You should already know how to run and clean up a finite Job in your course namespace.

## Mental model

A container image is not a tiny virtual machine in the simplest sense. It is a packaged filesystem and execution environment that runs using the host's operating-system kernel.

A useful first model is:

```text
Physical / virtual host
  └── host kernel
       └── container runtime
            └── container image/filesystem
                 └── your command/program
```

Kubernetes decides where the Pod runs. The container image helps describe what userspace environment should be there when it runs.

## Step 1 — Inspect the image from your first Job

Your first Job used:

```text
busybox:1.36
```

The `busybox` part names the image repository. The `1.36` part is a tag.

Compare that with a vague reference such as:

```text
busybox:latest
```

A changing tag makes it harder to know exactly what environment a future run will receive.

A first reproducibility rule is:

> Prefer intentional versions over accidental "whatever is latest" behavior.

## Step 2 — Observe the remote environment

Create a finite Job that prints runtime information such as:

```bash
uname -a
cat /etc/os-release || true
id
pwd
```

Do not leave the Job running. Use the same create → observe → verify → cleanup rhythm from earlier lessons.

Now run comparable read-only commands on your local machine:

```bash
uname -a
cat /etc/os-release 2>/dev/null || true
id
pwd
```

Record the differences.

## Step 3 — Ask what actually traveled

Your source code may travel through Git.

Your container environment is described by an image.

Your Kubernetes Job describes how that image should run.

The physical host does **not** travel with your project.

A useful chain is:

```text
Git commit
   + container image/version
   + workload definition
   + input data/version
   + command/parameters
   = much stronger reproducibility story
```

A container alone is not enough.

If the input data changes, the result may change.
If the image tag changes, the environment may change.
If external services change, behavior may change.
If randomness is uncontrolled, results may change.

## Step 4 — Strengthen one Job definition

Take a small program you already understand and make these pieces explicit:

- exact container image/tag;
- exact command;
- namespace;
- CPU request/limit;
- memory request/limit;
- finite deadline;
- input assumptions;
- expected output.

Then run it twice.

Ask:

```text
Did I get the same result?
If yes, what did I hold constant?
If no, what changed?
```

## Step 5 — Connect containers to CS2

Computer Science II often asks you to move beyond syntax into program structure and behavior.

Containers add another useful question:

> What does this program need from its environment?

That can expose assumptions about:

- files;
- libraries;
- runtime versions;
- environment variables;
- working directories;
- command-line arguments;
- external services.

Those are software-design concerns, not merely operations trivia.

## Failure as data

Common container-related failures include:

- wrong image name/tag;
- image cannot be pulled;
- expected executable does not exist inside the image;
- file path exists locally but not in the container;
- permissions differ;
- architecture/platform mismatch;
- runtime version differs from what your code expects.

When one occurs, capture the image name, command, Pod status, and logs/events. Do not respond by changing three unrelated things at once.

## Evidence receipt

Record:

```text
Lesson: NRP 04 Containers and Reproducibility
Course namespace:
Git commit (if code was used):
Container image/tag:
Remote runtime observations:
Local runtime observations:
One important difference:
What I held constant across runs:
What a container did NOT guarantee for me:
Cleanup proof:
```

## Reflection

1. Why is pinning an image version stronger than relying on `latest`?
2. Which parts of your experiment were described by the container, and which were outside it?
3. What additional information would another student need to reproduce your result a month from now?

## Next

Continue to:

[Lesson 5 — Resources, Scheduling, and Scale](05_resources_scheduling_scale.md)
