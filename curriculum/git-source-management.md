# Git / Source Management

Status: **BUILDING / Fall 2026 soft launch**

Core question:

> **Can I let humans and AI change a project quickly without losing control of what changed, why it changed, or how to recover?**

## Canonical source

The shared instructional source is:

[`../git_and_github/README.md`](../git_and_github/README.md)

Canvas-ready curriculum spine:

[`../git_and_github/curriculum/README.md`](../git_and_github/curriculum/README.md)

Reusable evidence receipt:

[`../git_and_github/templates/GIT_EVIDENCE_RECEIPT.md`](../git_and_github/templates/GIT_EVIDENCE_RECEIPT.md)

## Shared outcomes

Students should learn to:

- distinguish Git from GitHub;
- inspect repository identity, branch, history, and working-tree state before acting;
- use status and diff as routine evidence;
- make small intentional commits;
- use branches practically;
- place AI-assisted edits inside a bounded human-owned workflow;
- verify behavior independently before preserving a change;
- recover from ordinary mistakes;
- protect secrets and keep repository history clean;
- create an inspectable evidence receipt.

## Composition rule

Home courses should not fork a generic Git tutorial.

Instead:

```text
Git + GitHub shared station
        ↓
course-specific wrapper
        ↓
disciplinary application / assessment
```

For the first Fall 2026 application, DSCT adds the reasoning question:

> **What does this Git history actually prove, and what does it not prove?**

See:

[`../git_and_github/instructor/FALL_2026_DSCT_GIT_WEEK.md`](../git_and_github/instructor/FALL_2026_DSCT_GIT_WEEK.md)

## Source audit

Older Git-related repositories remain useful as historical/provenance sources, but they are not the canonical Fall 2026 student experience. The current Commons module should prioritize durable Git concepts and AI-era verification over old installer walkthroughs or third-party exercise sequencing.

## Canvas delivery status

Not yet promoted as a fully validated production station.

Soft-launch target: **September 15-17, 2026**, with DSCT as the first home-course wrapper.

Minimum viable release:

```text
00 — Start Here
01 — Mental model
02 — Preflight
03 — Status and diff
04 — Tiny human change
05 — AI at the keyboard
06 — Bounded AI change
10 — Evidence receipt
```

Recovery, pull-request collaboration, and repository hygiene can be taught live during the first run and promoted into polished standalone pages after the pathway is validated.
