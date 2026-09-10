# Fall 2026 NRP Course Namespace Plan

Status: **INSTRUCTOR PLAN**

The goal is to give each course a clean Kubernetes workspace while allowing Computing Commons to provide one shared curriculum for how students learn to use NRP.

NRP's current hierarchy maps a **Project** to a Kubernetes namespace. Separate course Projects therefore give us useful roster, troubleshooting, cleanup, and experiment boundaries.

## Recommended structure

```text
swosu
└── swosu-jevert
    ├── swosu-jevert-cs1-f26
    ├── swosu-jevert-cs2-f26        # existing
    ├── swosu-jevert-dsct-f26
    └── swosu-jevert-comp-arch-f26
```

Optional later shared workspace:

```text
swosu-jevert-commons-f26
```

Do **not** create the Commons namespace merely because the name is attractive. Add it when we have a real cross-course workload that benefits from shared membership rather than course isolation.

## Why separate course namespaces?

Separate namespaces make several things easier:

- membership follows the actual class roster;
- a cleanup mistake is less likely to affect another course;
- course-specific examples can use one explicit namespace;
- troubleshooting can ask "which course workspace?" and get a meaningful answer;
- resource usage can be understood in course context;
- end-of-semester membership cleanup is clearer;
- experimental curriculum can be released to one class before another.

Computing Commons should share **curriculum and habits**, not necessarily force every class into one giant Kubernetes namespace.

## Namespace 1 — Computer Science I

### Name

```text
swosu-jevert-cs1-f26
```

### Suggested description

```text
Fall 2026 Computer Science I instructional namespace at Southwestern Oklahoma State University. Used for introductory remote computing, containers, reproducible execution, evidence-oriented workflows, and selected Computing Commons activities. Managed by Jeremy Evert.
```

### Suggested features

```text
K8s Namespace: ON
LLM Access:     ON if the shared AI/hosted-model strand will be used; otherwise enable when needed
Milvus:         OFF
```

### Natural curriculum slice

Primarily NRP Lessons 1–3:

```text
identity -> namespace -> first Job -> logs -> cleanup -> evidence
```

The purpose is not to turn CS1 into infrastructure administration. It is to make a safe first remote-computing experience available when it supports the programming curriculum.

## Namespace 2 — Computer Science II

### Name

```text
swosu-jevert-cs2-f26
```

### Status

**Already created.**

Current intended features:

```text
K8s Namespace: ON
LLM Access:     ON
Milvus:         OFF
```

### Current description

```text
Fall 2026 Computer Science II instructional namespace at Southwestern Oklahoma State University. Used by students for hands-on computing, software development, Kubernetes experimentation, and responsible use of NRP-hosted LLM services as part of course activities. Managed by Jeremy Evert.
```

### Natural curriculum slice

Lessons 1–7, with particular emphasis on:

```text
repeatable workloads
containers
Git provenance
resource reasoning
failure diagnosis
hosted service boundaries
```

GPU work should remain optional/later and only be introduced for a workload that can use it meaningfully.

## Namespace 3 — Discrete Structures & Critical Thinking

### Name

```text
swosu-jevert-dsct-f26
```

### Suggested description

```text
Fall 2026 Discrete Structures and Critical Thinking instructional namespace at Southwestern Oklahoma State University. Used for computational reasoning, simulations, reproducible experiments, evidence collection, containers, and selected NRP-hosted AI activities. Managed by Jeremy Evert.
```

### Suggested features

```text
K8s Namespace: ON
LLM Access:     ON
Milvus:         OFF
```

### Natural curriculum slice

Students can reuse the earlier NRP foundation rather than repeat it. DSCT adds a stronger reasoning lens:

```text
claim
  -> assumptions
  -> experiment/simulation
  -> observation
  -> evidence
  -> interpretation
  -> limitations
```

This is a natural home for repeated simulations, probability experiments, comparison, uncertainty, and asking what a computational result actually proves.

## Namespace 4 — Computer Architecture

### Name

```text
swosu-jevert-comp-arch-f26
```

### Suggested description

```text
Fall 2026 Computer Architecture instructional namespace at Southwestern Oklahoma State University. Used for Linux and container inspection, CPU and memory experiments, performance measurements, reproducible workloads, hardware-aware computing, and selected accelerator experiments. Managed by Jeremy Evert.
```

### Suggested features

```text
K8s Namespace: ON
LLM Access:     ON if hosted-model/client experiments are part of the course; otherwise optional
Milvus:         OFF
```

### Natural curriculum slice

Architecture is the strongest hardware-facing bridge:

```text
container/runtime
  -> CPU
  -> memory
  -> process behavior
  -> resource requests/utilization
  -> timing/profiling
  -> accelerator suitability
```

NRP Lesson 8 (GPUs and Accelerators) fits here naturally after CPU baselines and inspection habits are established.

## Optional namespace — Computing Commons

### Possible name

```text
swosu-jevert-commons-f26
```

### Do not create yet unless we need it

A shared Commons namespace makes sense when students from multiple classes need to collaborate in the **same live Kubernetes workspace**.

It is not necessary merely because they share the same instructional material. Shared curriculum can point students to their own course namespace.

A Commons namespace would add another membership surface and another place where students might accidentally launch work. Keep the topology boring until a real shared workload earns the extra namespace.

## Metadata defaults

For instructional namespaces without a current grant directly funding the class:

### PI

```text
Jeremy Evert
```

### Institution

```text
Southwestern Oklahoma State University
```

### Grant

```text
No active grant - instructional use
```

Do not use historical grant roles as though they were current funding for the course.

### Software / Publications

Leave blank unless there is meaningful current information.

## Student identity policy

For the current SWOSU path:

```text
student GitHub account
  -> CILogon
  -> NRP account
  -> instructor adds student to course Project/namespace
  -> student's own Kubernetes/OIDC identity
```

Students should use their own identities. Do not issue shared classroom kubeconfigs or reuse instructor automation ServiceAccounts as student credentials.

If a course has LLM access, students should use their own personal NRP LLM tokens rather than a shared instructor token.

## Membership workflow

For each class:

1. Collect/confirm the student's expected GitHub-associated school email.
2. Have the student authenticate to NRP through CILogon/GitHub.
3. Add that user to the appropriate course namespace in the NRP Namespaces Manager.
4. Have the student verify the namespace appears.
5. Have the student run the read-only Commons preflight against that exact namespace.
6. Only after access is green, allow the tiny first Job.

If newly added membership is not visible in `kubectl`, NRP currently documents:

```bash
kubectl oidc-login clean
```

followed by a fresh authenticated command.

## Workspace naming rule

Use semester-scoped, descriptive names consistently:

```text
swosu-jevert-<course>-f26
```

Future semesters can follow the same pattern:

```text
swosu-jevert-cs2-s27
swosu-jevert-dsct-s27
```

This makes old and current workspaces distinguishable without inventing new naming conventions every term.

## Recommended creation order

Create only the namespaces needed soonest:

```text
1. cs2-f26        existing and Student-One testing now
2. comp-arch-f26  high-value NRP fit
3. dsct-f26       strong simulation/reasoning fit
4. cs1-f26        introduce when the Level-1 slice is ready
5. commons-f26    only if a shared live workspace earns its existence
```

The curriculum can exist before every namespace does. The live workspace should appear when we have a tested student path ready for it.

## Current official NRP references

- Namespace / access flow: <https://nrp.ai/documentation/userdocs/start/getting-started/>
- NRP hierarchy: <https://nrp.ai/documentation/userdocs/start/hierarchy/>
- Cluster policies: <https://nrp.ai/documentation/userdocs/start/policies/>
