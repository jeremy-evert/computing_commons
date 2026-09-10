# Video 01 Script — Your Laptop Is Not the Whole Computer

Status: **RECORDING DRAFT — READY FOR FIRST PASS**

Target length: **6–10 minutes**

Teaching job: move the student from `code → my computer → result` to a larger model where code can become a remote computing request that runs somewhere else.

Companion student page:

- `national_research_platform/teaching_slice/00_start_here.md`

Companion curriculum:

- `national_research_platform/getting_started.md`
- `national_research_platform/curriculum/01_identity_access_namespace.md`

## Recording posture

Keep this conversational. The goal is not to define every Kubernetes noun correctly enough for a certification exam. The goal is to give students a mental map they can hang later details on.

Use the terminal, browser, or a simple diagram only when it helps the idea. Do not spend this video installing software. Installation and authentication belong in the next teaching step.

---

## Cold open

Most of the programming you have done so far probably looks something like this:

> I write code on my computer. I run the code on my computer. My computer gives me the answer.

That is a perfectly good model when you are learning to program.

But today I want to stretch that model.

Your laptop is not the whole computer anymore.

What if your machine could describe some work, send that request to a large shared computing system, and then let another machine somewhere else actually do the work?

That is what we are going to start exploring with the National Research Platform.

## Part 1 — The small model we already know

[Show or draw]

```text
code → my computer → result
```

When you run Python, Java, C++, or another language locally, your own machine supplies the operating system, processor, memory, installed tools, files, and environment.

A lot of beginning programming quietly depends on that fact.

Your machine already has the right version of something installed. Your files are already where you expect them. Your PATH already works. Your operating system happens to match the instructions.

That is convenient, but it can also hide assumptions.

Eventually computer scientists have to ask a harder question:

> Can this work run somewhere other than the machine where I wrote it?

## Part 2 — Make the picture bigger

[Replace the first diagram with]

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

Now my computer is still important, but its role changes.

It can become the steering wheel rather than the engine.

I can use my local machine to describe what I want done and send that request to a larger computing environment.

That larger environment decides where the work should run.

This is one of the ideas behind cloud computing, research computing, large-scale data processing, machine learning systems, CI pipelines, and modern software infrastructure.

We are going to learn it by doing something extremely small first.

## Part 3 — What is the National Research Platform?

The National Research Platform, or NRP, gives researchers, educators, and students access to a large shared computing environment.

The Kubernetes cluster we will use is commonly called Nautilus.

You do not need to memorize the infrastructure behind it today.

For this course, think of the NRP as a large pool of computing resources that we can ask to perform work for us.

Instead of saying:

> Run this on Jeremy's laptop.

or:

> Run this on the classroom PC.

we can eventually say:

> Here is the work. Here are the resources it needs. Please run it in our course workspace and tell me what happened.

That shift is the point.

## Part 4 — Four Kubernetes words, minimum useful version

I want to give you four words now so the interface does not look like it was written by space wizards.

### Cluster

The **cluster** is the larger collection of computing systems working together.

For us, Nautilus is the environment we are talking to.

### Namespace

A **namespace** is our bounded workspace inside that cluster.

Different classes, projects, and groups can have different namespaces.

For Fall 2026 Computer Science II, our current namespace is:

```text
swosu-jevert-cs2-f26
```

You will see that name repeatedly because I want us to be explicit about where our work belongs.

### Job

A **Job** is a request to perform some finite work.

That makes sense for us because many computer science experiments have a beginning and an end.

Run the program. Gather the result. Finish.

### Pod

A **Pod** is one of the places where Kubernetes actually runs the container that performs the work.

For our first mental model, this is enough:

```text
Job
  ↓
Pod
  ↓
container
  ↓
program
```

Later we can make those definitions more precise.

Today I care more that you understand the relationship.

## Part 5 — Why containers show up here

A container lets us describe more of the environment our program expects.

Instead of hoping that some random remote machine happens to be configured exactly like ours, we can start with a known container image and run our command inside it.

This helps with reproducibility.

The question becomes less:

> Does this happen to work on my laptop?

and more:

> Can I describe the environment and workload clearly enough that another system can reproduce it?

That is a very useful computer science habit.

## Part 6 — Why are we doing this in CS2?

I am not trying to turn Computer Science II into a Kubernetes administration class.

Kubernetes is the vehicle, not the destination.

The bigger lessons are things like:

- separating your program from one particular computer;
- learning to describe resources;
- understanding identity and permissions;
- making execution reproducible;
- observing what actually happened;
- collecting evidence instead of guessing;
- cleaning up resources when the experiment is over;
- eventually scaling from tiny workloads toward larger experiments, hosted models, or GPUs.

Those ideas will matter whether you become a software developer, systems engineer, data scientist, security professional, researcher, or somebody working with AI systems.

## Part 7 — What we are actually going to do first

Our first workload is intentionally unimpressive.

We are going to ask the NRP to run a tiny CPU-only Job that prints a message and a little information about the machine environment.

That is it.

We are not starting with a GPU.

We are not training a model.

We are not launching a giant distributed application.

We are going to prove the pipe.

The lifecycle will be:

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

If we can do that reliably, then we have something worth building on.

## Part 8 — A tiny preview of identity

Before we can send work to a shared computing environment, the system needs to know who we are and what we are allowed to do.

That means our next step is identity and access.

For our current SWOSU path, we authenticate to NRP through CILogon using GitHub.

Then the NRP needs to know that your identity belongs in the course namespace.

Then your local Kubernetes tools need credentials that let them act as you.

Those are related steps, but they are not all the same thing.

The next video and activity will slow that down and make it understandable.

## Closing

Here is the one idea I want you to keep from this video:

> Your computer does not always have to be the machine that performs the work.

It can be the place where you write, inspect, and control the work.

The actual computation can happen somewhere else.

That change opens the door to reproducibility, remote computing, larger resources, specialized hardware, and eventually much bigger experiments.

But we earn that future by making the first step small and verifiable.

Next, we are going to prove who you are, find your course namespace, and make sure your computer can actually talk to the National Research Platform.

---

## Suggested screen beats

These are optional. Do not let visuals interrupt a good explanation.

1. Start with a blank terminal/editor and the simple diagram `code → my computer → result`.
2. Expand it into `code → remote request → scheduler → another machine → result`.
3. Briefly show the public Computing Commons NRP folder.
4. Briefly show the NRP website without entering credentials or displaying private account material.
5. Put `swosu-jevert-cs2-f26` on screen when defining namespace.
6. Draw `Job → Pod → container → program`.
7. End on the lifecycle `CREATE → RUN → OBSERVE → VERIFY → CLEAN UP → VERIFY AGAIN`.

## Recording cautions

Do not display:

- kubeconfig contents;
- API tokens;
- private keys;
- browser credential details;
- student account information;
- private repository material.

If a live browser view contains personal account details, crop or avoid that view.

## Definition of a good take

The recording is good enough when a student can answer these questions afterward:

1. Why might a program run somewhere other than the student's own computer?
2. What is the NRP in the context of this course?
3. At a basic level, what are a cluster, namespace, Job, Pod, and container?
4. Why are we deliberately starting with a tiny workload?
5. What is the lifecycle we are trying to prove?
6. What are we doing next?
