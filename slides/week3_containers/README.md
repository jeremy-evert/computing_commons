# Week 3 Containers + Reproducibility deck

Student-facing Beamer deck for the shared Computing Commons Week 3 module,
"It Worked on My Machine — Repeatability, Reproducibility, Containers, and
Evidence." This is the canonical Week 3 containers lesson referenced by
Computer Architecture and Discrete Structures & Critical Thinking; neither
course authors its own copy.

## Build

```bash
pdflatex -interaction=nonstopmode -halt-on-error week3_containers.tex
pdflatex -interaction=nonstopmode -halt-on-error week3_containers.tex
```

Standard TeX Live packages only (`beamer`, `booktabs`, `array`, `tikz`). 16:9,
21-page PDF. The PDF is checked into this repository as a review/deployment
artifact.

## Teaching route

- **Act I — Same code is not the same experiment** (slides 2–6): prediction,
  the source-to-silicon layer stack, where variation sneaks in, control vs.
  record.
- **Act II — Evidence** (slides 7–8): the reproducibility contract, and why a
  receipt is evidence that survives the terminal.
- **Act III — Containers** (slides 9–14): image vs. running container, pinned
  digest identity vs. `latest`, host/container path crossing via bind mount,
  what a container helps control, and — just as important — what it does not
  (containers do not make machines identical).
- **Act IV — Claim** (slides 15–20): the known-good run, deliberate
  perturbation, native-vs-container as an experiment in itself, repeatability
  vs. reproducibility, the bounded claim your evidence can actually carry,
  and the split into the two course lenses (DSCT / Architecture).
- Slide 21 is the transition into student work.

Closing doctrine, repeated on the final content slide:

> **Same code is not the same experiment.**
> **Control what you can. Record what you cannot.**
> **Make only the claim your evidence can carry.**

## Source relationships

Authored directly in the Commons per the shared-substrate doctrine in
`foreman_interface/jobs/tasks/week03_shared_containers_ghcr_and_module.md`
("Commons teaches the common craft once; each course applies it through its
own lens") — this is not copied from DSCT or Architecture, and neither
course should fork its own version.

Technical claims (image vs. container, pinned digest, bind mount, what a
container does and does not control) are reconciled against the validated,
published Week 3 container release:

- `jeremy-evert/discrete_structures_and_critical_thinking`,
  `week-03/container/IMAGE_CONTRACT.md` — the actual build/publish/verify
  record for the pinned image this deck describes.
- Live pin as of 2026-09-01:
  `ghcr.io/jeremy-evert/dsct-week3-latex@sha256:e7987919298c909f1a7f52247b8a7b54395cbde2400e2d6f3e8c5078425e2fca`
  (tag `v1`), GHCR package **public**, anonymous pull independently verified.

The deck deliberately does not teach Docker/Podman syntax as the objective,
does not claim containers make hosts identical, and does not present
Unix-only cleanup commands as a universal cross-platform path.

## Pending

- **Recorded lecture / video / transcript**: not yet produced. This deck is
  built and reviewed; the actual classroom recording is a separate video
  pipeline (Jeremy / the Aug-31-class lecture-distillation workflow), not
  something authored here. See `curriculum/containers-and-repeatable-
  environments.md` for the current placeholder state of that link.
