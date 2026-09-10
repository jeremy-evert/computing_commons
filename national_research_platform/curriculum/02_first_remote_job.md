# Lesson 2 — Your First Remote Job

## Why this matters

Your first remote workload should be small enough that you can understand every moving part.

The goal is not to impress anyone with computational scale. The goal is to prove this chain:

```text
your terminal
  -> Kubernetes API
  -> course namespace
  -> Job
  -> Pod
  -> container
  -> command
  -> logs
```

Once that chain is real, later workloads can become more interesting without becoming more mysterious.

## Learning outcomes

By the end of this lesson, you should be able to:

- create a finite Kubernetes Job in the correct course namespace;
- explain the relationship among a Job, Pod, container, and command;
- wait for Job completion;
- retrieve logs from the Job;
- identify the container image and resource requests used;
- delete exactly the Job you created;
- independently verify cleanup.

## Before you begin

Complete Lesson 1 first.

Verify:

```bash
kubectl auth can-i create jobs -n swosu-jevert-cs2-f26
```

You want:

```text
yes
```

If your course uses a different namespace, substitute it everywhere in this lesson.

## Mental model

A **Job** describes finite work.

Kubernetes creates a **Pod** for that Job.

The Pod starts a **container** from an image.

Inside the container, Kubernetes runs the command you described.

```text
Job
 └── Pod
      └── Container image
           └── Command
                └── Output
```

The Job is not your source code. It is the orchestration object that describes how the work should run.

## Step 1 — Make your Job name unique

Use your GitHub username in the Job name so classmates do not collide with one another.

Example pattern:

```text
YOUR_GITHUB_USERNAME-hello
```

Kubernetes names must be DNS-safe. Lowercase letters, numbers, and dashes are the safest choice.

## Step 2 — Copy the starter template

The public template is here:

[`../templates/first_job.template.yaml`](../templates/first_job.template.yaml)

Copy it into your own working directory:

```bash
cp national_research_platform/templates/first_job.template.yaml first-nrp-job.yaml
```

Edit the copy.

Replace:

```text
REPLACE_WITH_GITHUB_USERNAME
REPLACE_WITH_COURSE_NAMESPACE
```

For Fall 2026 CS2, the namespace is:

```text
swosu-jevert-cs2-f26
```

Before you apply the file, read it.

You should be able to point to:

- the Job name;
- the namespace;
- the container image;
- the command;
- CPU request/limit;
- memory request/limit;
- the finite timeout/cleanup settings.

## Step 3 — Ask Kubernetes to create the Job

Run:

```bash
kubectl apply -f first-nrp-job.yaml
```

Now inspect only the course namespace:

```bash
kubectl get jobs -n swosu-jevert-cs2-f26
kubectl get pods -n swosu-jevert-cs2-f26
```

Find your Job and its Pod.

## Step 4 — Wait for completion

Replace the example with your actual Job name:

```bash
kubectl wait \
  --for=condition=complete \
  job/YOUR_GITHUB_USERNAME-hello \
  -n swosu-jevert-cs2-f26 \
  --timeout=120s
```

If the Job completes, do not stop there. A success message is one piece of evidence, not the whole story.

## Step 5 — Retrieve the output

Run:

```bash
kubectl logs \
  job/YOUR_GITHUB_USERNAME-hello \
  -n swosu-jevert-cs2-f26
```

The starter Job prints a small greeting plus basic information about the container environment.

Read the output.

The container hostname will likely not look anything like your own computer's hostname. That is useful evidence that your command ran elsewhere.

## Step 6 — Inspect what Kubernetes knows

Run:

```bash
kubectl get job YOUR_GITHUB_USERNAME-hello \
  -n swosu-jevert-cs2-f26 -o wide
```

Then:

```bash
kubectl describe job YOUR_GITHUB_USERNAME-hello \
  -n swosu-jevert-cs2-f26
```

Do not try to memorize the entire `describe` output.

Look for evidence about:

- creation;
- desired/completed work;
- Pod relationship;
- image;
- timing/events when present.

## Step 7 — Clean up exactly what you created

Run:

```bash
kubectl delete job YOUR_GITHUB_USERNAME-hello \
  -n swosu-jevert-cs2-f26
```

Do not use a broad delete such as "delete all Jobs" merely because it is shorter.

This is a shared namespace.

## Step 8 — Verify cleanup independently

Run:

```bash
kubectl get job YOUR_GITHUB_USERNAME-hello \
  -n swosu-jevert-cs2-f26
```

A `NotFound` result is useful cleanup evidence.

You may also check for any Pod left with the Job label:

```bash
kubectl get pods \
  -n swosu-jevert-cs2-f26 \
  -l job-name=YOUR_GITHUB_USERNAME-hello
```

The normal end state is no matching resource.

## What just happened?

Your local computer did **not** execute the workload itself.

It sent a request to the Kubernetes API.

Kubernetes accepted the request in the course namespace, scheduled a Pod, obtained the requested container image, ran the command, tracked completion, and exposed logs back to you.

That is a small example of orchestration.

## Failure as data

If the Job does not complete, do not immediately recreate it with random changes.

Capture:

```bash
kubectl get jobs -n swosu-jevert-cs2-f26
kubectl get pods -n swosu-jevert-cs2-f26
kubectl describe job YOUR_GITHUB_USERNAME-hello -n swosu-jevert-cs2-f26
```

If a Pod exists, inspect it:

```bash
kubectl describe pod POD_NAME -n swosu-jevert-cs2-f26
kubectl logs POD_NAME -n swosu-jevert-cs2-f26
```

Useful failure categories include:

- permission denied;
- image could not be pulled;
- command exited with an error;
- scheduling/resource problem;
- timeout;
- typo in namespace or resource name.

Each category suggests a different next move.

## Evidence receipt

Use the Commons receipt template or record:

```text
Lesson: NRP 02 First Remote Job
Course namespace:
Job name:
Container image:
CPU request / limit:
Memory request / limit:
Job completion result:
One meaningful log line:
Cleanup command:
Independent cleanup result:
What evidence convinces me this did not run directly on my laptop?
```

## Reflection

1. Why is a finite Job a better first experiment than leaving a Pod running indefinitely?
2. Which parts of the Job definition describe *what you want* and which parts describe *resources the system should reserve*?
3. What evidence would you show another student to prove the workload completed and was cleaned up?

## Next

Continue to:

[Lesson 3 — Evidence, Cleanup, and Failure as Data](03_evidence_cleanup_failure.md)
