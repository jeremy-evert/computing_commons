# 00 — Start Here: Git Is the Safety Belt

Welcome to the Git + GitHub station of the Computing Commons.

This is not a week about memorizing commands.

It is a week about learning how to **change things without being afraid of losing yesterday**.

That matters even more now because humans are no longer the only ones editing our files. AI coding tools can create, rewrite, rename, and delete code much faster than we can type it ourselves.

Speed is useful.

Speed without inspection is chaos with good marketing.

Git gives us a durable way to answer:

- Where am I?
- What changed?
- What did I mean to change?
- What did I actually change?
- What state worked?
- What evidence do I have?
- Can I get back there?

## The big idea

> **Git is the safety belt.**
>
> AI may help drive the change. The human still owns the commit.

The goal is not to distrust AI.

The goal is to build a workflow where trust is never the only evidence we have.

## Three rules for this station

### 1. In God we trust. Everything else we verify.

A person can say a change works.

An AI can say a change works.

A green-looking screen can make us feel like a change works.

We still verify.

Verification might be a test, a build, an example run, direct inspection, or another appropriate check.

### 2. Love AI more. Trust AI less.

Use AI boldly.

Ask it to explain, generate, repair, refactor, test, document, and explore.

But do not confuse confidence with evidence.

An AI summary of a change is a claim.

A Git diff is inspectable evidence about what changed.

A successful test is evidence about tested behavior.

Those are different things.

### 3. Git is the safety belt.

Before making a meaningful change, know your starting state.

After making a change, inspect what happened.

Before preserving a change, verify it.

If something goes wrong, use history and state to recover instead of randomly changing more things.

## The workflow we are learning

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

AI fits inside **MAKE ONE BOUNDED CHANGE**.

It does not replace the rest of the loop.

## What Git is not

Git is not GitHub.

Git is not cloud storage.

Git is not a magical backup system.

Git is not proof that your program is correct.

Git is not something you use only after the project is finished.

Git is the history and state machinery that lets us work deliberately while the project is alive.

## What GitHub adds

GitHub gives us a remote place to publish and collaborate around Git repositories.

That adds useful ideas such as:

- remote repositories;
- forks;
- pull requests;
- code review;
- issues;
- automated checks;
- shared project history.

But we are going to learn **Git before GitHub**.

If you understand the local repository, GitHub becomes much easier to reason about.

## Your job this week

You are not expected to become a Git wizard.

You are expected to become comfortable enough with Git that you can:

1. identify the repository and branch you are working in;
2. inspect whether the project is clean or already changed;
3. make one bounded change;
4. inspect the actual diff;
5. verify the resulting behavior;
6. preserve a useful commit;
7. publish your work when appropriate;
8. recover from an ordinary mistake;
9. explain what your evidence proves;
10. explain what your evidence does **not** prove.

That last one matters.

A clean Git history can tell a very useful story.

It can also tell a beautifully organized story about incorrect code.

## The DSCT connection

Discrete Structures & Critical Thinking asks a deeper question than simply:

> Did the command work?

This week we will repeatedly ask:

> **What does this evidence justify me claiming?**

For example:

```text
Observation:
The test suite reports 12 tests passed.

Possible claim:
The program passed these 12 tests in this environment.

Claim that goes too far:
The program is completely correct.
```

Git gives us evidence.

Reasoning determines what that evidence allows us to conclude.

## Before moving on

You should be able to explain these two statements in your own words:

> **AI can accelerate a change without proving the change is good.**

> **Git can preserve and expose a change without proving the change is correct.**

If those ideas make sense, you are ready for the next stop:

**01 — Git, GitHub, Repositories, Commits, Branches, and Remotes**

There we will build the mental model for where all of this work actually lives.

---

## Completion signal

This entry point is complete when you can answer the following in one or two sentences:

> **Why does Git become more important, not less important, when AI tools can edit code for us?**
