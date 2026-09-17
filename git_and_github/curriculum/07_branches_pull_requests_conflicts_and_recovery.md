# 07 — Video: Branches, Pull Requests, Conflicts, and Recovery

## Core question

**How do we experiment and collaborate without making every change everybody else's problem immediately?**

You've already used one branch, in lesson 06 (`ai/largest-category`). This lesson steps back to explain branches properly, adds pull requests and conflicts, and gives you a recovery ladder for when something goes wrong.

---

## Branches, taught as cheap, not as ceremony

A branch is a movable pointer to a commit — nothing more mysterious than that. You saw this in lesson 01: `main` is just a label that moves forward as new commits land on it. Creating a new branch costs almost nothing:

```bash
git branch --show-current
git switch -c feature/example
```

Creating the branch does not change any file. It creates another named line where commits can happen without immediately affecting `main` or anyone else working from it. That's the entire value proposition — cheap, disposable lines of work, not a formal ceremony you need permission to perform.

---

## Pull requests

A pull request is a reviewable proposal to integrate one line of work into another — typically a branch into `main`.

A pull request lets a reader inspect, before anything merges:

- what commits are included;
- what files changed;
- the diff itself;
- checks/test status, if automated checks are configured;
- review comments from other people;
- whether the branch can merge cleanly or has a conflict.

This is the same discipline from lesson 03 — status and diff are the truth — applied at the scale of a whole proposed change instead of a single local commit. A pull request is, in a real sense, a diff with a conversation attached.

---

## Conflicts

Teach conflict resolution as a concept before teaching the mechanical tricks:

1. **Stop.** A conflict is Git telling you it found two different intended changes to the same place and cannot guess which one you want.
2. **Inspect the conflicting file.** Git marks the competing versions directly in the file.
3. **Understand both intended changes.** Not just the text — the *purpose* behind each one.
4. **Produce the desired final content.** This might be one side, the other, or a combination — your judgment, not Git's.
5. **Verify behavior.** A resolved conflict that doesn't run is not actually resolved.
6. **Stage the resolved file.**
7. **Continue the merge/rebase operation** appropriate to the workflow you're in.

A conflict is not a failure state to panic about. It's Git correctly refusing to silently guess at something that requires a human decision.

---

## Recovery ladder — prefer tools that preserve evidence

Not every recovery situation is the same, and treating them the same is where students get into trouble.

For an uncommitted file change you truly intend to discard:

```bash
git restore <file>
```

This throws away uncommitted working-tree changes to that file. Use it only when you are certain you don't want to keep the edit — it does not create a record of what you discarded.

For a bad commit that has already been shared or published, prefer a new history-preserving reversal instead:

```bash
git revert <commit>
```

`git revert` creates a **new** commit that undoes the effect of an earlier one, while keeping both the original mistake and the correction visible in history. This matters once a commit has been pushed and possibly seen by other people or automation — silently rewriting shared history creates a different, harder problem than the one you started with.

> **Do not make destructive history rewriting the beginner's first reflex.**

If you are ever unsure which situation you're in, stop and inspect before acting:

```bash
git status
git log --oneline --decorate -5
git diff
git diff --staged
```

Diagnose first. A recovery command run without understanding the current state can turn one problem into two.

---

## Completion signal

Student can choose between "discard an uncommitted edit" (`git restore`) and "revert a published commit" (`git revert`) without treating them as the same problem — and can explain, in their own words, why the difference matters once other people or systems may already be depending on what was pushed.

Ready for:

**08 — Try It: Break Something Small, Recover, and Verify**
