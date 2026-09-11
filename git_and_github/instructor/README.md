# Instructor Start Here — Git Week

This is the **primary teaching entry point** for the Git + GitHub station.

If you are teaching DSCT Git Week, start here.

## What to follow

Use these materials in this order:

1. [`FALL_2026_DSCT_GIT_WEEK.md`](FALL_2026_DSCT_GIT_WEEK.md)
   - This is the week-level teaching plan.
   - It tells you what Tuesday and Thursday are trying to accomplish.
   - It defines the DSCT reasoning lens: **What does this Git history actually prove, and what does it not prove?**

2. [`../curriculum/README.md`](../curriculum/README.md)
   - This is the complete Git + GitHub curriculum map.
   - It defines the 00–11 sequence, outcomes, command spine, evidence expectations, recovery, AI-assisted workflow, and where the material goes next.

3. Teach the numbered student pages in sequence.
   - [`../curriculum/00_start_here.md`](../curriculum/00_start_here.md)
   - [`../curriculum/01_git_github_repositories_commits_branches_remotes.md`](../curriculum/01_git_github_repositories_commits_branches_remotes.md)
   - Additional numbered pages should be added here as they are promoted from the curriculum map into full lessons.

4. Use the public exercise repository for all hands-on work:
   - https://github.com/jeremy-evert/git-safety-belt-lab

5. Use the shared evidence receipt when students begin making changes:
   - [`../templates/GIT_EVIDENCE_RECEIPT.md`](../templates/GIT_EVIDENCE_RECEIPT.md)

## Current Fall 2026 teaching sequence

### Tuesday — History as Evidence

Teach / use:

```text
00 — Start Here: Git Is the Safety Belt
01 — Git, GitHub, Repositories, Commits, Branches, and Remotes
02 — Preflight / Know Where You Are   [next full lesson to build]
03 — Status and Diff Are the Truth    [curriculum map currently defines this]
04 — Tiny Human Change                [curriculum map currently defines this]
```

Tuesday class should move students from observing a repository to making one small human-authored change and explaining what Git evidence does and does not establish.

### Thursday — AI as a Fast, Fallible Contributor

Teach / use:

```text
05 — AI at the Keyboard, Human on the Commit
06 — Bounded AI Change + Inspect the Diff
07 — Branches, Pull Requests, Conflicts, and Recovery
08 — Break Something Small, Recover, and Verify
10 — Git Evidence Receipt
```

Thursday should move students into bounded AI-assisted work, inspection, independent verification, and recovery.

## The teaching loop

Keep returning to this instead of treating Git as command memorization:

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

AI only enters inside **MAKE ONE BOUNDED CHANGE**.

## Three class rules

1. **In God we trust. Everything else we verify.**
2. **Love AI more. Trust AI less.**
3. **Git is the safety belt.**

## Current build status

Fully written student-facing pages:

```text
00 — Start Here
01 — Git / GitHub mental model
```

The remaining 02–11 sequence is already specified in [`../curriculum/README.md`](../curriculum/README.md), but not every step has yet been promoted into its own polished standalone page.

That means the curriculum exists, but the next authoring priority is clear:

```text
02 — Try It: Open a Repo and Run the Git Preflight
```

## Verified Student Zero evidence

The first end-to-end starter check was completed on Maise on September 11, 2026.

See:

[`STUDENT_ZERO_MAISE_2026-09-11.md`](STUDENT_ZERO_MAISE_2026-09-11.md)

That run verified cloning, history inspection, fast-forward pull, Python 3 verification, passing tests, and a clean final repository state.

## Instructor rule

Do not teach from the practice repository README alone.

Do not teach from the master curriculum map alone.

Use this instructor entry point to navigate:

```text
Instructor plan
    ↓
numbered student lesson
    ↓
practice repo
    ↓
evidence receipt
    ↓
DSCT reasoning question
```
