# Lesson 3 — Evidence, Cleanup, and Failure as Data

## Why this matters

A professional computing habit is not simply:

> "I ran the command."

A stronger habit is:

> "Here is what I attempted, what happened, what proves it, what I changed, and what remains."

Remote computing makes that habit especially important because the work may run on another machine, in another container, under a scheduler you do not directly control.

## Learning outcomes

By the end of this lesson, you should be able to:

- distinguish a claim from evidence;
- collect useful Job/Pod evidence without exposing credentials;
- verify cleanup rather than merely issuing a delete command;
- classify common failure types;
- preserve enough context for another person to help you;
- explain why failure is useful data rather than a reason to start changing random things.

## Before you begin

Complete Lessons 1 and 2, including one successful finite Job.

## Mental model

Use this loop:

```text
INTENT
  ↓
ACTION
  ↓
OBSERVATION
  ↓
EVIDENCE
  ↓
INTERPRETATION
  ↓
NEXT ACTION
```

Do not collapse all six stages into "worked" or "didn't work."

### Claim

```text
My Job completed successfully.
```

### Evidence

```text
kubectl wait reported condition=complete.
kubectl logs returned the expected output.
The Job status showed one successful completion.
```

The evidence supports the claim.

## Step 1 — Build a small evidence package

For a Job you created, gather only what is useful:

```bash
kubectl get job YOUR_JOB -n YOUR_COURSE_NAMESPACE -o wide
kubectl logs job/YOUR_JOB -n YOUR_COURSE_NAMESPACE
kubectl describe job YOUR_JOB -n YOUR_COURSE_NAMESPACE
```

If you need the related Pod:

```bash
kubectl get pods -n YOUR_COURSE_NAMESPACE -l job-name=YOUR_JOB
```

Then inspect that exact Pod if necessary.

Do not dump your kubeconfig into an assignment to prove authentication. The fact that an authenticated command succeeded is usually enough evidence.

## Step 2 — Separate observation from interpretation

Suppose you observe:

```text
Job status: Complete
Logs: expected output
```

An appropriate interpretation is:

```text
The requested container command completed successfully at least once in the selected namespace.
```

A stronger unsupported claim would be:

```text
This program will always work on every Kubernetes cluster.
```

Your evidence does not prove that.

Learning to say what evidence **does not** prove is an important computer science skill.

## Step 3 — Treat cleanup as part of the experiment

Deleting a Job is an action:

```bash
kubectl delete job YOUR_JOB -n YOUR_COURSE_NAMESPACE
```

Cleanup proof is a separate observation:

```bash
kubectl get job YOUR_JOB -n YOUR_COURSE_NAMESPACE
```

and, when useful:

```bash
kubectl get pods -n YOUR_COURSE_NAMESPACE -l job-name=YOUR_JOB
```

The desired result is that your matching objects are gone.

Do not broadly delete classmates' resources in a shared namespace.

## Step 4 — Learn a failure taxonomy

When a workload fails, first ask **what kind of failure this is**.

### Authentication failure

Typical clues:

- login cannot complete;
- token/login plugin problems;
- Kubernetes does not accept your identity.

Useful evidence:

```bash
kubectl config get-contexts
```

Do not publish the kubeconfig itself.

### Authorization failure

Typical clue:

```text
Forbidden
```

or:

```bash
kubectl auth can-i create jobs -n YOUR_COURSE_NAMESPACE
```

returns:

```text
no
```

Do not try to defeat the permission system. Report the evidence.

### Namespace failure

Typical clues:

- resource appears to be missing;
- permission differs from expectation;
- command is pointed at the wrong namespace.

Check the namespace explicitly.

### Image failure

Typical clues:

```text
ImagePullBackOff
ErrImagePull
```

Investigate the image name, tag, availability, and access requirements.

### Program failure

Typical clues:

- Pod starts but exits nonzero;
- logs contain a stack trace or program error.

Now the orchestration system may be healthy while your program is not.

### Scheduling/resource failure

Typical clues:

- Pod remains Pending;
- events mention insufficient CPU, memory, GPU, affinity, quota, or scheduling constraints.

Do not "solve" this by requesting enormous resources. Inspect why the scheduler could not place the work.

### Timeout / finite-work failure

Typical clues:

- Job exceeds the intended deadline;
- program never reaches its natural end.

NRP policy is particularly important here: Jobs should be finite. Do not turn a batch Job into an endless sleeper.

## Step 5 — Write a useful help request

A good help request contains:

```text
Goal:
Exact command:
Namespace:
Expected result:
Actual result:
Exact error/status:
What I already checked:
```

A weak help request contains only:

```text
It doesn't work.
```

The first version gives another person something to reason about.

## Step 6 — Keep secrets out of evidence

Never include:

```text
passwords
tokens
API keys
private keys
full kubeconfigs
secret environment files
protected student information
```

If a screenshot includes a credential, do not submit the screenshot.

If you are unsure whether a value is secret, ask before publishing it.

## Evidence receipt

Use [`../templates/evidence_receipt.md`](../templates/evidence_receipt.md).

For this lesson, your receipt should include one successful observation and one cleanup observation. If you encountered a real failure, include the failure classification and what evidence led you there.

## Reflection

1. Why is "I ran delete" weaker than "I ran delete and then proved the object was gone"?
2. What is the difference between a permission failure and a program failure?
3. Why can a technically correct error message still be useful progress?
4. What is one claim you could make from your evidence, and one stronger claim your evidence does **not** justify?

## Next

Continue to:

[Lesson 4 — Containers and Reproducibility](04_containers_reproducibility.md)
