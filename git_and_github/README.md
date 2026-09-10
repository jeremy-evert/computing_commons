# Git + GitHub in the AI Era

This is the shared Computing Commons home for practical Git and GitHub skills across the computing curriculum.

The goal is not to memorize a bag of Git commands. The goal is to make students **dangerously comfortable changing things because they know how to inspect, verify, preserve, publish, and recover their work**.

In an AI-assisted workflow, code can change faster than a human can type or even read it. That makes version control more important, not less.

> **Git is the safety belt.**
>
> AI may help drive the change. The human still owns the commit.

## Core question

**Can I let humans and AI change a project quickly without losing control of what changed, why it changed, or how to recover?**

## Student promise

After this station, a student should be able to:

- explain the practical difference between Git, GitHub, a repository, a working tree, a commit, a branch, and a remote;
- identify which repository and branch they are actually changing before they act;
- use `git status`, `git diff`, and `git log` as inspection tools rather than decorations;
- clone or open a repository and establish a clean preflight state;
- make one bounded change, inspect it, verify it, commit it, and push it;
- create and use a branch for work that should not immediately land on the default branch;
- use an AI coding tool inside a bounded Git workflow;
- detect when an AI-assisted change has expanded beyond the requested scope;
- inspect the actual diff rather than trusting a chat summary of the diff;
- run an independent verification step before accepting a change;
- distinguish a successful commit from a correct program;
- recover from ordinary mistakes without panic;
- keep secrets, credentials, large generated artifacts, and machine-specific junk out of the repository;
- publish a compact evidence receipt another person can inspect.

## The canonical loop

```text
ORIENT
  ↓
PREFLIGHT
  ↓
START CLEAN
  ↓
MAKE ONE BOUNDED CHANGE
  ↓
INSPECT THE DIFF
  ↓
VERIFY THE BEHAVIOR
  ↓
COMMIT
  ↓
PUBLISH / REVIEW
  ↓
PRESERVE A RECEIPT
```

AI does not replace this loop.

AI enters inside **MAKE ONE BOUNDED CHANGE**.

## Human ownership rules for AI-assisted Git

1. **Start from a known state.** Know the repository, branch, and current `HEAD` before delegating.
2. **Prefer a clean working tree.** Do not mix old mystery edits with new AI edits.
3. **Bound the task.** Name the files, behavior, test, or acceptance condition when possible.
4. **Inspect what Git says changed.** The diff is the durable record. A model's summary is only a claim about that record.
5. **Verify independently.** Tests, builds, linters, example runs, or direct inspection should determine whether the change behaves as intended.
6. **Commit intentionally.** The student owns the decision to preserve the change in project history.
7. **Stop when scope expands unexpectedly.** A tiny request that changes fourteen unrelated files is evidence to investigate, not a reason to shrug.
8. **Never treat a commit as proof of correctness.** A commit proves that a snapshot entered history. It does not prove the snapshot is good.

## What we deliberately do not teach first

This station does not begin with:

- rebasing gymnastics;
- detached-HEAD trivia;
- Git object internals;
- clever aliases;
- destructive reset commands;
- GUI-versus-CLI arguments;
- giant branching taxonomies;
- memorizing every flag.

Those can come later. The first win is a student who can inspect state, make a bounded change, preserve it, publish it, and recover from an ordinary mistake.

## Curriculum

The Canvas-ready learning spine lives in:

[`curriculum/README.md`](curriculum/README.md)

## Fall 2026 DSCT handoff

The first home-course wrapper is:

[`instructor/FALL_2026_DSCT_GIT_WEEK.md`](instructor/FALL_2026_DSCT_GIT_WEEK.md)

The Commons teaches the shared craft. DSCT asks the reasoning question:

> **What does this Git history actually prove, and what does it not prove?**

## Course growth path

### Foundation

Students can inspect state, create useful commits, push safely, and recover from simple mistakes.

### CS2 / AI-assisted development

Students add branches, pull requests, bounded agent work, tests, code review, and stronger receipts.

### DSCT

Students treat commit history, diffs, tests, and receipts as evidence. They distinguish observation from interpretation and avoid claiming more than the artifacts justify.

### Computer Architecture

Students connect source history to build environment, machine/runtime details, and performance evidence.

### Software Engineering / Machine Learning

The same foundation grows into team workflows, CI, review gates, release provenance, experiment provenance, and automated agents operating inside explicit repository boundaries.

## Fall 2026 release posture

Treat this as a soft launch. Release the smallest tested slice first, preserve earlier material for review, and strengthen the evidence expectations as students progress.
