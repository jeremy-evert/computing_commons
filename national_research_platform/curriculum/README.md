# National Research Platform Curriculum

This is the shared Computing Commons curriculum for moving students from first remote access to reproducible, evidence-rich computing on the National Research Platform.

The sequence is deliberately cumulative. Students should not repeatedly "start over" in every course. Earlier lessons remain available for review while later courses ask for stronger reasoning, stronger evidence, and more sophisticated workloads.

## Curriculum spine

| Lesson | Core question | Primary capability | Natural Commons fit |
|---|---|---|---|
| 1. Identity, Access, Namespace | **Who am I to this system, and where am I allowed to work?** | CILogon/GitHub identity, namespace membership, kubectl access | Level 1 / CS1 foundation |
| 2. First Remote Job | **Can I make one tiny piece of work run somewhere else?** | Job, Pod, logs, finite execution | Level 1 → Level 2 bridge |
| 3. Evidence, Cleanup, Failure | **What proves what happened, and what did I leave behind?** | receipts, verification, cleanup, troubleshooting | Level 1 / Level 2 |
| 4. Containers and Reproducibility | **Can another environment reproduce what I just did?** | images, containers, versions, portable execution | Level 2 / CS2 |
| 5. Resources, Scheduling, Scale | **What did my work ask for, use, and compete for?** | CPU, memory, requests/limits, scheduling | Level 2 + Architecture bridge |
| 6. Git and Remote Workloads | **Can source, environment, execution, and evidence tell one coherent story?** | Git provenance, remote execution, repeatability | Level 2 / CS2 |
| 7. Hosted LLMs | **How is calling a remote model service different from running my own Pod?** | service APIs, personal tokens, model discovery, verification | Level 2/3 AI bridge |
| 8. GPUs and Accelerators | **When does specialized hardware actually matter?** | GPU requests, suitability, utilization, architecture | Architecture + ML bridge |
| 9. Remote Experiment Capstone | **Can someone else inspect and reproduce my experiment?** | experiment design, comparative evidence, durable report | Level 3+ / cross-course |

## Progression by course

### Computer Science I target

Students should leave the first level able to:

- authenticate safely;
- identify the correct namespace;
- distinguish identity from permission;
- run a tiny finite workload;
- retrieve its output;
- clean it up;
- preserve a useful receipt;
- ask for help with evidence rather than "it doesn't work."

This is not intended to displace introductory programming. It gives programming a larger world to eventually live in.

### Computer Science II target

Students should move from "I ran a Job" to "I can build a repeatable remote workload."

Expected growth:

- reason about container images and versions;
- make the execution environment explicit;
- move source through Git rather than manual copy rituals;
- use resource requests intentionally;
- compare expected versus observed behavior;
- preserve stronger evidence;
- separate local development, remote execution, and remote services;
- recover from ordinary failures without randomly changing everything.

### Discrete Structures & Critical Thinking target

The NRP becomes an experiment and reasoning environment.

Expected growth:

- state claims and assumptions;
- design comparisons;
- distinguish observation from interpretation;
- discuss uncertainty and limitations;
- identify what a result does and does not prove;
- use repeated runs/simulations when appropriate;
- make evidence inspectable by another person.

The disciplinary mathematics/reasoning remains in DSCT. The Commons supplies the shared execution/evidence craft.

### Computer Architecture bridge

Architecture deepens the machine-facing side of the sequence:

- CPU and memory behavior;
- operating-system/container boundaries;
- process and runtime inspection;
- architecture/platform differences;
- performance measurements;
- resource utilization;
- accelerator visibility and GPU suitability;
- explaining why the same source can behave differently on different hardware.

### Software Engineering / Machine Learning later

The same foundation can grow into:

- team-owned deployment artifacts;
- CI/validation;
- services and APIs;
- reproducible pipelines;
- model/data provenance;
- GPU-backed experiments;
- evaluation and monitoring;
- responsible deployment boundaries.

## Standard student rhythm

A practical NRP lesson should usually feel like this:

```text
ORIENT
  ↓
PREFLIGHT
  ↓
DO ONE BOUNDED THING
  ↓
OBSERVE
  ↓
VERIFY
  ↓
CLEAN UP
  ↓
VERIFY AGAIN
  ↓
EXPLAIN WHAT IT MEANS
```

That rhythm is intentional. It prevents the curriculum from becoming a collection of disconnected shell incantations.

## Evidence progression

Early receipts should be tiny. Later receipts should become more analytical.

### Foundation receipt

```text
identity path
namespace
command
result
logs/status
cleanup proof
one-sentence explanation
```

### CS2 receipt

Add:

```text
Git commit
container image/version
resource requests/limits
reproduction instructions
failure/recovery evidence when applicable
```

### DSCT / Architecture receipt

Add the evidence appropriate to the discipline:

```text
claim
assumptions
comparison or measurement
observed data
interpretation
limitations
machine/runtime details
```

## Release posture for Fall 2026

Treat this as a **soft-launch curriculum**.

Students should encounter the smallest tested slice first. Do not release an entire infrastructure staircase merely because the files exist.

Recommended initial release:

1. Getting Started
2. Lesson 1
3. Lesson 2
4. Lesson 3

After the Student-One/Morgan pathway is proven, release deeper lessons as they become useful to the home courses.

## Curriculum development rule

New NRP content must follow [`QUALITY_STANDARD.md`](QUALITY_STANDARD.md).

A lesson should not be promoted merely because it is technically correct. It should also be teachable, bounded, safe, independently verifiable, and connected to a larger computer science idea.

## Current course namespace

Fall 2026 CS2:

```text
swosu-jevert-cs2-f26
```

See the instructor namespace plan for the other course workspaces:

[`../instructor/fall_2026_namespace_plan.md`](../instructor/fall_2026_namespace_plan.md)
