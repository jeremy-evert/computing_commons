# Initial Computing Commons curriculum map

This map is intentionally architectural. It identifies the shared-capability spine without pretending every module is already built.

## Shared runway

### Success Foundations / Semester Kickoff

Purpose:

- know where the student is;
- know where the student is trying to go;
- know how to get help;
- understand the shared computing ecosystem;
- begin degree/career/professional planning;
- establish evidence and participation habits.

Primary ownership: **COMMON**.

Home-course role: course-specific welcome, schedule, disciplinary framing, and lightweight completion/application wrapper if needed.

### Build and Verify Your Local AI Lab

Purpose:

- inventory the machine;
- distinguish “present” from “working”;
- establish the approved local foundation;
- run a local model;
- verify direct inference;
- use an approved local coding assistant workflow;
- create a small Git worktree;
- make, inspect, and independently verify a bounded change.

Primary ownership: **COMMON**.

Home-course role: apply the working lab to a small disciplinary task rather than reteaching setup.

### National Research Platform remote-computing runway

Core question: **Can my software leave my laptop and become a remote workload that another computing environment can understand, schedule, run, observe, and verify?**

Primary ownership: **COMMON** for the shared student pathway. NRP itself remains authoritative for live service-specific instructions and policy.

Start at [`../national_research_platform/README.md`](../national_research_platform/README.md).

Minimum shared outcomes:

- authenticate safely through the approved identity path;
- distinguish authentication from authorization;
- work in an explicit course namespace;
- run one finite CPU-only Job;
- recover logs and status as evidence;
- clean up exactly what the student created and verify cleanup;
- understand Job → Pod → container → program at a practical level;
- connect remote execution to containers and reproducibility;
- reason about CPU/memory requests before requesting specialized hardware;
- connect Git provenance to remote experiment evidence;
- understand hosted LLM APIs as a separate service/credential boundary;
- treat failures as data rather than random-change triggers.

Natural progression:

- **Level 1 / CS1:** identity, namespace, first Job, evidence, cleanup.
- **Level 2 / CS2:** containers, repeatable workloads, Git provenance, resource reasoning, stronger verification, hosted-service boundaries.
- **Level 3 / DSCT:** experiment design, assumptions, comparison, uncertainty, interpretation, limitations.
- **Computer Architecture:** CPU/memory/runtime inspection, performance, scheduling, architecture differences, accelerators.
- **Later SE/ML:** automation, collaboration, deployment, model/data provenance, GPU-backed experiments, evaluation.

Home-course role: apply the shared remote-computing capability to disciplinary questions rather than reteaching login, `kubectl`, cleanup, and receipt habits from zero.

## Recitation toolbox

### Containers and repeatable environments

Core question: **Can another environment reproduce what I just did?**

Minimum shared outcomes:

- understand host vs environment/container;
- run a bounded containerized task;
- understand files/mounts at a practical level;
- capture evidence about what environment actually ran the task;
- use containers for repeatability rather than as vocabulary trivia.

The NRP curriculum provides a natural remote application of this capability after the local/container foundation is ready.

### LaTeX and evidence-oriented documentation

Core question: **Can another human understand and inspect what I did?**

Minimum shared outcomes:

- write useful Markdown;
- create a useful README;
- use minimum-useful LaTeX when formal typesetting is appropriate;
- include commands, results, assumptions, captions, and evidence;
- treat documentation as part of the work rather than an afterthought.

### Work First

Core question: **Can I organize the work so tools help without taking control?**

Minimum shared outcomes:

- distinguish project/product from the workspace/process around it;
- keep plans, prompts, evidence, reports, and source in understandable homes;
- delegate bounded details while retaining direction and verification;
- narrow tasks enough that smaller/local models can succeed;
- preserve durable project truth outside transient chat.

### Linux command line and profiling

Core question: **Can I look under the dashboard when the machine behaves strangely?**

Minimum shared outcomes:

- navigate with `pwd`, `ls`, and `cd`;
- inspect text/files with simple command-line tools;
- locate files/processes;
- inspect CPU, memory, disk, and process behavior;
- use timing/profiling evidence rather than guessing;
- recognize GPU visibility when appropriate;
- begin with inspection, not broad administration.

Computer Architecture should provide the strongest deeper application of this strand.

### Source-code management with Git

Core question: **Can I change something without being afraid of losing yesterday?**

Minimum shared outcomes:

- understand repository/worktree/state;
- use status and diff before acting;
- make useful commits;
- inspect history;
- understand branches at a practical level;
- recover from bounded mistakes;
- learn Git before treating GitHub as the concept itself.

### AI accountability and verification

Core question: **What did the tool claim, and what independently proves it?**

Minimum shared outcomes:

- disclose meaningful AI assistance;
- distinguish suggestion from evidence;
- test/check outputs independently;
- identify uncertainty and hidden assumptions;
- remain responsible for submitted work.

## Continuing strands

### AI Fluency

Monday is the current natural recurring AI Fluency strand.

The strand should deepen by level rather than repeating introductory material.

### Professional Minds

Professional Minds remains a recurring common strand. The exact Wednesday/Friday distinction is still a design question.

A promising split is:

- **Wednesday: People / professional perspectives**
- **Friday: Practice / professional habits and decisions**

This is not yet locked as final terminology.

## Shared finale: Farkle + Machine Learning

The Commons should preserve a common late-semester experience built around Farkle, simulation, probability, models, evidence, and machine behavior.

The finale should be one shared phenomenon with course-specific lenses, not six duplicated assignments.

Computer Architecture has especially strong fit for the profiling/performance/CPU-GPU portion, while Machine Learning provides the deepest model lens and DSCT provides probability/reasoning foundations.

NRP can become one of the execution environments for this shared finale when a remote/reproducible or accelerator-backed run adds genuine learning value rather than complexity for its own sake.

## Ownership rule

A topic belongs in the Commons when students can learn the shared capability once and then apply it differently in multiple disciplines.

A topic stays in the home course when the learning outcome itself is disciplinary.
