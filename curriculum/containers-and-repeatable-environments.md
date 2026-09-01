# Containers and Repeatable Environments — It Worked on My Machine

**Recitation Toolbox station.** Question: **Can another environment reproduce what I just did?**

## Commons role

This is the canonical, shared Week 3 lesson on repeatability, reproducibility,
containers, and evidence. Computer Architecture and Discrete Structures &
Critical Thinking (DSCT) both point their Week 3 students here for the shared
concept, then apply it through their own disciplinary lens. Neither course
authors its own copy of this material — see the source-audit rule in
[`recitation-toolbox.md`](recitation-toolbox.md).

The shared doctrine:

> **Same code is not the same experiment.**
>
> **Control what you can. Record what you cannot.**
>
> **Make only the claim your evidence can carry.**

The bounded container claim:

> **We use a container so that we can hold more of the software environment
> constant while deliberately observing what still depends on the host.**

---

## 1. If the code stays the same, what else can change?

Imagine you and a classmate have the same source file, the same input, and
the same instructions. You run it. It works. Your classmate runs it. It
fails — or both succeed, but one is faster, reports a different tool
version, sees a different amount of memory, or writes output somewhere
unexpected.

That is not a side quest. That is the Week 3 problem.

A computing experiment is more than its source code. Between your source and
the physical machine sit layers of context:

```text
source + input + command
        ↓
shell + paths + environment variables
        ↓
runtime + libraries + compiler/toolchain
        ↓
operating system + kernel + filesystem
        ↓
CPU + memory + storage + physical host
```

Variation can enter at every layer.

## 2. Repeatability, reproducibility, and the reproducibility contract

**Repeatable**: you can run it again on your own machine and get the same
shape of result.

**Reproducible**: someone else, on a different machine, following your
record, can get the same shape of result.

A **reproducibility contract** states, in advance, what you will hold fixed
and what you will record:

- **Control it** when you reasonably can — source revision, input data, tool
  versions, package versions, entry command, known filesystem layout.
- **Record it** when you cannot or should not hold it fixed — host
  architecture, kernel, load, timing, other execution-visible facts.

A **reproducibility receipt** is evidence that survives the terminal: what
ran, what environment ran it, and what came out. A receipt records what
happened. It does not, by itself, prove *why*.

## 3. What is a container?

An **image** is a frozen template for a software environment: tools,
libraries, packages, files, environment settings, and a default command.

A **container** is a running instance created from an image. The image can
outlive the container; a container can be disposable.

**Image = template. Container = running instance.**

A floating label such as `latest` may point to something different later. A
**pinned digest** identifies one specific, immutable environment — that is
what gives another person real evidence about what you actually ran.

A **bind mount** makes a folder from your computer visible inside the
container. The same file therefore has two path names: a **host path** on
your computer, and a **container path** inside the running container. Work
written into the mounted folder survives after the container exits; work
written only to the container's private filesystem may not.

### What a container helps control

- installed tools;
- package/library versions;
- userspace files;
- working directory;
- entry command;
- environment variables.

### What a container does not magically control

- physical CPU;
- host kernel;
- host load and scheduling;
- storage hardware;
- timing noise;
- other host-specific behavior.

Containers do not make two machines identical. They let you hold more of the
*software* environment constant while the host, kernel, and hardware remain
visibly outside that boundary — which is exactly why Week 3 records them
rather than pretending they are controlled away.

## 4. Watch the lecture

**Slides (PDF):** [`slides/week3_containers/week3_containers.pdf`](../slides/week3_containers/week3_containers.pdf)
(21 slides — prediction, the layer stack, control-vs-record, the
reproducibility contract, image vs. container, pinned identity, bind mounts,
what containers do and do not control, the known-good run, deliberate
perturbation, and the bounded claim.)

**Video / recorded lecture:** not yet published. This is a live classroom
recording, produced separately from this deck (see the Aug-31 lecture
video/distillation workflow) — not something authored in this repository.
Update this line once Jeremy records and publishes it.

**Accessible text / transcript:** pending the recording above.

## 5. Run a known-good container

You are not being graded on memorizing a container command. You are being
asked to understand the contract:

1. Which image ran, and is it pinned?
2. Which input went in?
3. Which host folder was made visible, and at what container path?
4. What output should be produced?
5. What evidence proves the output is real?

The currently published, independently verified Week 3 container is the
DSCT LaTeX environment. It doubles as the shared "known-good run"
demonstration for this lesson:

```
Image (pinned):  ghcr.io/jeremy-evert/dsct-week3-latex@sha256:e7987919298c909f1a7f52247b8a7b54395cbde2400e2d6f3e8c5078425e2fca
Package:         public — pull with no credentials
Wrapper:         discrete_structures_and_critical_thinking/week-03/container/run-latex.sh
```

Full build/publish/pull/fixture/failure-recovery evidence is recorded in
`discrete_structures_and_critical_thinking/week-03/container/IMAGE_CONTRACT.md`.
Do not substitute a different Docker/Podman recipe from the internet — use
the validated wrapper for your course.

A successful run should make the important facts visible: image identity,
runtime, host source/work directory, container work directory, the
input/source, the expected output, and a `RESULT` line with a useful reason
on failure. Do not stop at a clean exit code — open the produced artifact
and check that it is actually what you intended to produce.

Keep a tiny receipt: the exact source/snapshot used, the exact command, the
image/runtime identity shown to you, the host and container work paths, the
artifact you verified, and one sentence describing what the run
demonstrates.

## 6. Inspect the container boundary

Using your known-good run, classify what you saw:

- **Probably supplied by the image:** installed tools, package/library
  versions, userspace files, working directory, entry command, environment
  variables.
- **Probably supplied or influenced by the host:** CPU architecture, host
  kernel, available resources, machine load, storage behavior, timing.

Find the folder that contains your input on the host. Find the path at which
that same folder appears inside the container. Complete the sentence: *My
file lives at \_\_\_\_ on the host. The container sees the mounted work at
\_\_\_\_. The output survives because \_\_\_\_.*

After the run, the container itself may be gone — that is fine and
intentional (disposable state). The useful questions are not "where is my
container now" but: did the intended work happen, did the artifact survive,
and did you preserve enough evidence to know what environment did the work?

## 7. Break it, diagnose it, recover, verify

A tool is not really yours until you can recover from a bounded failure. Use
this loop rather than changing five things at once:

1. **Read** the failure reason before changing anything.
2. **Classify** it: path/mount problem (the system can't find the file or
   folder you intended), container/runtime problem (the container can't
   start or the image/runtime is wrong), or content/tool problem (the
   container ran, but the tool rejected the input).
3. **Propose** one specific repair. An AI suggestion is a proposal, not a
   result.
4. **Execute** the repair yourself.
5. **Rerun** the same validated wrapper.
6. **Verify** the actual artifact/evidence — not just that the terminal
   looks happier.

Record: the observed failure, the category, the repair you proposed, what
you changed, the rerun result, and the evidence that convinced you the
repair actually worked.

## 8. Take the skill back to your course

### DSCT — Can your evidence carry your claim?

See `discrete_structures_and_critical_thinking/week-03/` (student path:
`student/container-latex-skill-ladder.md`). You use the same pinned
container to turn a small `.tex` claim/proof into a PDF, then reason about
what the evidence actually proves, what it does not, which differences are
relevant, and how verification changes your confidence:

**Run → Inspect → Explain → Perturb → Diagnose → Recover → Verify**

### Computer Architecture — Where does the machine end?

See `computer_architecture/weeks/week-03/`. You compare repeated
observations of the execution environment and investigate what a container
boundary actually controls versus what still comes from the host, kernel,
or hardware:

- What did the process see?
- What was fixed by source/wrapper/image?
- What came from the container environment?
- What still came from the host/kernel/hardware?
- What stayed stable across repeated runs, and what changed legitimately?
- What would another person need to decide whether a difference mattered?

## 9. The finish line

By the end of your course-specific investigation, you should be able to make
a bounded statement shaped like this:

> The same \_\_\_\_ and \_\_\_\_ produced \_\_\_\_ across repeated runs. The
> receipt describes \_\_\_\_, but it does not prove \_\_\_\_. Another person
> could reproduce the reasoning by preserving \_\_\_\_ and recording \_\_\_\_.

Not "my machine is the same as yours." Not "the container makes everything
portable." Not "the command exited successfully, therefore the result is
correct."

---

## Canonical sources

- `discrete_structures_and_critical_thinking/week-03/container/` — the
  actual pinned, published, independently-verified container release this
  lesson is built on (`IMAGE_CONTRACT.md`, `Containerfile`, `run-latex.sh`).
- `computer_architecture/lab/` — the provenance pattern the DSCT container
  reused (`debian:trixie-slim` + TeX Live toolchain shape).
- `slides/week3_containers/` — this module's deck (Commons-authored, not a
  copy of course material).

## Commons composition status

| Field | Status |
| --- | --- |
| Shared container image | **published & pinned** — see §5 above |
| Deck | authored, compiled (21 slides) |
| Recorded lecture / transcript | **pending** — separate video pipeline |
| DSCT course link-back | pending Phase 4 wiring |
| Architecture course link-back | pending Phase 5 wiring |
| Canvas delivery | not yet deployed — source-first per mission gate |
