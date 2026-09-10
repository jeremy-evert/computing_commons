# 00 — Start Here: What Are We About to Do?

Welcome to the National Research Platform portion of Computing Commons.

This is not a Kubernetes certification unit, and you are not expected to arrive already knowing clusters, containers, schedulers, namespaces, or remote computing.

We are going to learn one small, useful path through a real shared computing environment.

By the end of this first teaching slice, you should be able to explain and demonstrate this chain:

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

The goal is not to say, "I know Kubernetes."

A better goal is:

> I understand how my identity gives me access to a shared computing workspace, how I can ask a remote system to run a finite workload, how I verify what happened, and why cleanup and evidence are part of the job.

## Why are we doing this?

Most beginning programming work follows a simple path:

```text
my code → my computer → my result
```

That is a perfectly good way to learn programming.

But professional and research computing often adds more layers:

```text
my code
   ↓
remote computing request
   ↓
scheduler
   ↓
another machine
   ↓
container
   ↓
result
```

The National Research Platform gives us a safe place to start exploring that larger world.

Your laptop or classroom computer can become the steering wheel instead of always being the engine.

## What you will do in this first slice

You will:

1. learn what the National Research Platform is;
2. authenticate using your own identity;
3. confirm that you can see the course namespace assigned by your instructor;
4. use `kubectl` to ask the cluster a few read-only questions;
5. launch one tiny CPU-only Job;
6. observe the Job and the Pod that runs it;
7. read the program output from the logs;
8. delete the Job when you are finished;
9. verify that cleanup actually happened;
10. explain what the system did.

That is enough for a very good first experience.

## The four ideas to carry with you

### 1. Identity

The system needs to know who you are.

For our current SWOSU path, CILogon uses GitHub as the identity provider. Your instructor adds that NRP identity to the appropriate course namespace.

Your GitHub identity, your NRP account, your Kubernetes permissions, and your local credentials are related, but they are not the same thing.

### 2. Namespace

A namespace is the bounded workspace where your course work lives.

Your instructor will tell you the exact namespace for your class.

For Fall 2026 Computer Science II, the current namespace is:

```text
swosu-jevert-cs2-f26
```

Do not assume that namespace belongs to every course or every semester.

### 3. Workload

You will submit one tiny Kubernetes Job.

The Job will ask the NRP to run a small containerized command somewhere on the cluster. It is intentionally boring. Boring first success is useful because it lets us verify the path before adding complexity.

### 4. Evidence

We do not stop at "it probably worked."

We will inspect what happened, read the logs, confirm completion, clean up the Job, and verify that it is gone.

A successful workflow is:

```text
CREATE
   ↓
RUN
   ↓
OBSERVE
   ↓
VERIFY
   ↓
CLEAN UP
   ↓
VERIFY AGAIN
```

## What you do not need yet

You do not need to understand all of these before starting:

- GPUs;
- distributed systems theory;
- Kubernetes administration;
- persistent storage;
- production networking;
- cluster-wide permissions;
- hosted AI models;
- advanced container construction.

Those are later roads.

For now, we are proving that you can enter the environment, ask it to do one small thing, see what happened, and leave the workspace clean.

## Your safety rules

Never paste or commit any of the following into GitHub, Canvas, chat, screenshots, assignment files, or AI prompts:

- passwords;
- API tokens;
- private keys;
- full kubeconfig files;
- secret environment files;
- reusable credentials.

If you are unsure whether something is a credential, treat it as private and ask.

## When something fails

A failure is not a reason to start changing random things.

A failure is data.

Capture:

```text
What were you trying to do?
What exact command did you run?
What did you expect?
What actually happened?
What exact error did the system return?
```

That information is often enough to classify whether the problem is identity, authorization, configuration, scheduling, workload execution, or application behavior.

## Where to go next

Start with:

**01 — Video: Your Laptop Is Not the Whole Computer**

Then continue through the authentication, first Job, evidence, and cleanup steps in this teaching slice.

If you are curious about the larger road, the public Computing Commons repository also contains deeper National Research Platform curriculum on containers, scheduling, Git, hosted LLMs, GPUs, and remote experiments.

For now, keep the first goal small:

> Get in. Run one thing. Prove what happened. Clean up after yourself.
