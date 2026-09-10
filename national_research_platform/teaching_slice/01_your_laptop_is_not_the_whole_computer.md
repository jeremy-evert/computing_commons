# 01 — Your Laptop Is Not the Whole Computer

Most of the programming you have done so far probably follows a very simple model:

```text
code → my computer → result
```

You write the program. Your computer supplies the operating system, processor, memory, files, installed tools, and environment. Then your computer runs the program and gives you the result.

That is a perfectly good way to learn programming.

Today we are going to make the picture bigger.

## The big idea

Your computer does not always have to be the machine that performs the work.

It can become the place where you **describe, send, inspect, and control** the work while another machine performs the actual computation.

The larger picture looks more like this:

```text
code
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

That shift matters because it opens the door to remote computing, reproducible environments, larger resources, specialized hardware, automation, and experiments that would be awkward or impossible to run on one classroom computer.

Your laptop can become the steering wheel instead of always being the engine.

## Why would we want to run somewhere else?

A program that works on your own machine can quietly depend on many local details:

- your operating system;
- your version of Python, Java, C++, or another language;
- libraries you happened to install;
- files that happen to exist in the right place;
- environment variables;
- your PATH;
- your CPU and memory;
- software that somebody else may not have.

Eventually computer scientists have to ask a harder question:

> Can this work run somewhere other than the machine where I wrote it?

That is the beginning of a much larger family of ideas involving cloud computing, research computing, containers, continuous integration, data processing, machine learning systems, and distributed infrastructure.

We are going to learn those ideas by starting very small.

## What is the National Research Platform?

The **National Research Platform**, usually shortened to **NRP**, gives researchers, educators, and students access to a large shared computing environment.

The Kubernetes environment we will use is commonly called **Nautilus**.

You do not need to memorize the physical infrastructure behind it today.

For this first lesson, think of the NRP as a large pool of computing resources that we can ask to perform work for us.

Instead of saying:

```text
Run this program on this particular classroom computer.
```

we can begin saying:

```text
Here is the work.
Here are the resources it needs.
Run it inside our course workspace.
Tell me what happened.
```

That is the important transition.

## Five words worth knowing today

You will see a lot of Kubernetes vocabulary eventually. You only need a small handful of words to make the first experience understandable.

### Cluster

A **cluster** is a collection of computing systems that can work together as a larger computing environment.

For our purposes, Nautilus is the cluster environment we are talking to.

### Namespace

A **namespace** is a bounded workspace inside the cluster.

Different projects, groups, and courses can have different namespaces. The namespace helps determine where your work belongs and what your identity is allowed to do.

For Fall 2026 Computer Science II, our current namespace is:

```text
swosu-jevert-cs2-f26
```

You will see us name the namespace explicitly. That is intentional. We want to know where our work is going instead of trusting whatever default happens to be configured.

Other courses and future semesters may use different namespaces.

### Job

A Kubernetes **Job** describes some finite work that should run and finish.

That fits many computer science experiments nicely:

```text
start the program
      ↓
do the work
      ↓
produce the result
      ↓
finish
```

### Pod

A **Pod** is one of Kubernetes' basic units of execution. For our first mental model, it is enough to think of the Pod as the place where Kubernetes runs the container that performs our Job.

### Container

A **container** gives the program a more predictable execution environment.

Instead of hoping that a random remote machine happens to be configured just like your laptop, we can start from a known container image and run our command inside it.

For now, this relationship is enough:

```text
Job
  ↓
Pod
  ↓
container
  ↓
program
```

We will make those definitions more precise later. Today the relationship matters more than memorizing vocabulary.

## Why containers matter

Suppose your program works because your laptop happens to have exactly the right tools installed.

That proves something useful, but it leaves a question:

> Did the program work because we described the work correctly, or because we got lucky with one particular machine?

Containers help move us toward a stronger question:

> Can I describe the environment and workload clearly enough that another system can reproduce what I did?

That is **reproducibility**, and it is one of the habits we will keep strengthening throughout Computing Commons and your computer science courses.

## Why are we doing this in Computer Science II?

We are not turning Computer Science II into a Kubernetes administration course.

Kubernetes is the vehicle, not the destination.

The larger lessons include:

- separating a program from one particular computer;
- describing the resources a program needs;
- understanding identity and permission;
- making execution more reproducible;
- observing what actually happened;
- collecting evidence instead of guessing;
- learning from failure;
- cleaning up resources after an experiment;
- connecting code, Git, containers, remote systems, hosted services, and eventually specialized hardware.

Those ideas can matter whether you become a software developer, systems engineer, cybersecurity professional, data scientist, researcher, or somebody building AI systems.

## Our first workload will be deliberately tiny

We are not beginning with a GPU.

We are not training a model.

We are not launching a giant distributed application.

Our first workload will be a tiny CPU-only Job that prints a message and a little information about the environment where it ran.

That may sound unimpressive. Good.

A small first success lets us prove the pipe before we add complexity.

The lifecycle we want to learn is:

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

Notice that **running the program is only one part of the workflow**.

A stronger definition of success includes knowing what ran, seeing the output, confirming completion, removing what we created, and independently checking that cleanup happened.

## Before we can run anything, identity comes first

A shared computing system cannot simply accept commands from everybody on the Internet.

It needs to answer two different questions:

1. **Who are you?**
2. **What are you allowed to do?**

For our current SWOSU path, we authenticate to the NRP through **CILogon using GitHub**.

Then the NRP needs to know that your identity belongs in the appropriate course namespace.

Then your local Kubernetes tools need configuration that lets them communicate with the cluster as you.

These ideas are related, but they are not the same thing:

```text
GitHub identity
      ↓
NRP identity
      ↓
course namespace membership
      ↓
local Kubernetes authentication
      ↓
permission to perform a particular action
```

That distinction becomes our next lesson.

## If you remember five things

After this page and the accompanying class discussion, you should be able to explain these five ideas in your own words:

1. A program does not have to execute on the same computer where it was written.
2. The NRP gives us access to a larger shared computing environment.
3. A namespace is the bounded workspace where our course work belongs.
4. A Job can describe finite work, and Kubernetes can run that work through a Pod and container.
5. Our definition of success includes observation, evidence, cleanup, and verification.

You do **not** need to be able to say, "I know Kubernetes."

A much better first milestone is:

> I understand the shape of the system well enough to enter it carefully and run one small, verifiable experiment.

## Next

Next we will work through **identity, access, and the course namespace**.

That means getting from:

```text
I have a GitHub account
```

to:

```text
The National Research Platform recognizes me,
my course namespace recognizes me,
and my computer can safely ask that namespace questions.
```

Then we will earn our first remote Job.

For the larger public NRP pathway, see the [Computing Commons National Research Platform landing page](../README.md).
