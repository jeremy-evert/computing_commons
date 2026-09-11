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

3. Teach the numbered student material in sequence.
   - [`../curriculum/00_start_here.md`](../curriculum/00_start_here.md)
   - [`../curriculum/01_git_github_repositories_commits_branches_remotes.md`](../curriculum/01_git_github_repositories_commits_branches_remotes.md)
   - [`../curriculum/02_ai_git_safety_belt_lab.md`](../curriculum/02_ai_git_safety_belt_lab.md)

   The 02 lab is currently an **integrated guided lab** distilled from the September 11 CS2 teaching run. It carries students from preflight through a bounded AI change, diff inspection, verification, repository hygiene, authority limits, recovery, and a receipt. Later Canvas authoring may split that integrated lab into the smaller 02–10 pages defined by the master map.

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
02 Lab — known state + baseline verification + branch + bounded task setup
```

Tuesday class should move students from observing a repository to establishing a known state, proving the starter project works, and understanding the boundary around a proposed change.

### Thursday — AI as a Fast, Fallible Contributor

Continue the integrated 02 lab:

```text
AI edits
  -> inspect status + diff
  -> identify scope creep / authority surprises
  -> verify independently
  -> stage intentionally
  -> inspect staged diff
  -> human commit
  -> publish when appropriate
  -> evidence receipt
```

Thursday should move students into bounded AI-assisted work, inspection, independent verification, repository hygiene, authority awareness, recovery, and evidence limits.

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

Fully written student-facing material:

```text
00 — Start Here
01 — Git / GitHub mental model
02 — Integrated AI + Git Safety Belt lab
```

The remaining smaller 02–11 slices are already specified in [`../curriculum/README.md`](../curriculum/README.md). The integrated lab gives us a tested student pathway now; Flo can later split/polish it for Canvas delivery without losing the real classroom evidence that produced it.

## Raw teaching provenance

The September 11 CS2 ChatGPT/Copilot transcript is preserved at:

[`../CS2_notes_2026_09_11.md`](../CS2_notes_2026_09_11.md)

Do **not** teach from that raw file. It is provenance and design evidence.

Teach from the numbered curriculum pages above.

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
numbered student lesson / integrated lab
    ↓
practice repo
    ↓
evidence receipt
    ↓
DSCT reasoning question
```
