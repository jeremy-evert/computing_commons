# Lesson 6 — Git and Remote Workloads

## Why this matters

Remote execution is much more useful when the code you ran has a durable identity.

"I ran `program.py`" is weak evidence if nobody knows which version of `program.py` you mean.

Git gives your source a history. Kubernetes gives your workload an execution environment. Together they can produce a much stronger story:

```text
this exact source
  + this exact environment
  + this exact command
  + this exact input
  -> this observed result
```

## Learning outcomes

By the end of this lesson, you should be able to:

- connect a remote experiment to a Git commit;
- distinguish source provenance from runtime evidence;
- avoid manual-copy workflows when a repository can carry the source;
- record the image, command, namespace, and commit used for a run;
- explain why a Git commit alone does not make an experiment reproducible.

## Before you begin

You should be comfortable with:

```bash
git status
git diff
git add <specific-file>
git commit
git log
```

If those are unfamiliar, use the Computing Commons Git material before continuing.

## Mental model

Git answers:

> Which source version are we talking about?

The container image answers:

> Which execution environment are we asking for?

The Kubernetes workload answers:

> How should that environment run on the cluster?

The evidence receipt answers:

> What actually happened?

No one layer replaces the others.

## Step 1 — Create a tiny versioned program

Use a small program you understand completely. It can be Java, Python, C/C++, or another course-appropriate language if you have a suitable container image.

Before remote execution:

```bash
git status
git diff
```

Commit the version you intend to run.

Then record:

```bash
git rev-parse HEAD
```

That commit SHA becomes part of your experiment identity.

## Step 2 — Make the runtime path explicit

Your workload should identify:

- course namespace;
- container image/tag;
- command that runs the program;
- input or arguments;
- CPU/memory requests;
- finite deadline;
- Job name unique to you/this run.

Do not assume that because the source is in GitHub the cluster automatically knows how to obtain and run it. The transport/build mechanism is part of the design and should be explicit.

## Step 3 — Run and collect evidence

For the remote run, capture at minimum:

```text
Git commit
namespace
Job name
container image/tag
command/arguments
result/logs
cleanup proof
```

If you modify the source after the run, the old receipt should still point to the commit that actually produced the result.

## Step 4 — Make one controlled change

Change one meaningful but small piece of the program.

Before committing:

```bash
git diff
```

Commit the change.

Now you have two source identities:

```text
Run A -> commit A
Run B -> commit B
```

Run the new version with the same environment/input when practical.

Compare the results.

This creates a tiny controlled software experiment.

## Step 5 — Ask what Git did not capture

A Git commit may preserve source code but not automatically preserve:

- an unversioned external dataset;
- a mutable container tag;
- a secret environment variable;
- a remote API's behavior;
- a model that changed behind an endpoint;
- nondeterministic randomness;
- cluster scheduling conditions;
- hardware differences.

That is why provenance is broader than version control.

## CS2 connection

Computer Science II is a natural place to make this habit routine.

When data structures, algorithms, classes, recursion, testing, or other program behavior becomes more complex, the question "which version actually produced this result?" becomes increasingly important.

Git lets you change software without losing yesterday.

Remote receipts let you prove which yesterday or today actually ran.

## Failure as data

If local code works but remote code fails, compare the layers instead of assuming Kubernetes is broken.

Check:

```text
same commit?
same runtime/language version?
same files present?
same working directory?
same command-line arguments?
same input data?
same environment variables?
same architecture assumptions?
```

A local/remote difference is often evidence that an implicit dependency finally became visible.

## Evidence receipt

Record:

```text
Lesson: NRP 06 Git and Remote Workloads
Repository:
Git commit:
Course namespace:
Job name:
Container image/tag:
Command/arguments:
Expected result:
Observed result:
Cleanup proof:
One dependency Git did not capture automatically:
```

## Reflection

1. Why is "the latest code" weaker evidence than a commit SHA?
2. Why is a commit SHA still not enough to reproduce a remote experiment by itself?
3. What implicit dependency became visible when you moved code from your own machine to a remote environment?

## Next

Continue to:

[Lesson 7 — Hosted LLMs as a Remote Service](07_hosted_llms.md)
