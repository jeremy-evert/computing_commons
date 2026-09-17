# 03 — Video: Status and Diff Are the Truth

## Core question

**What actually changed?**

You now know where work lives: working tree, commits, branches, remotes. This lesson is about a narrower, more practical skill — reading Git's own report of what is different, right now, instead of trusting a description of what is different.

---

## Why this matters more with AI in the loop

A model can tell you:

> "I only changed the requested function."

That sentence is a claim.

Git can show you what changed.

That is evidence.

> **Privilege inspectable artifacts over conversational confidence.**

This is the single habit this lesson exists to build. Everything else in this station assumes you already reach for `git status` and `git diff` before you believe anyone — human or AI — about what happened to a repository.

---

## The working tree and the staging area, just enough to be useful

You do not need a deep theory of Git's internals to use it well. You need two ideas:

- the **working tree** is the files as they currently sit on disk;
- the **staging area** (sometimes called the index) is a holding area for exactly the changes you intend to commit next.

A file can be:

```text
unmodified   -> matches the last commit
modified     -> changed in the working tree, not yet staged
staged       -> marked to go into the next commit
committed    -> preserved in history
```

`git status` tells you which of those states each file is in. `git diff` tells you what the actual content difference is.

---

## Primary inspection commands

Using the Safety Belt Lab (`jeremy-evert/git-safety-belt-lab`) as the running example, suppose you have made an edit to `trail_mix.py` but have not staged or committed anything yet.

```bash
git status
```

This reports, by file, whether it is untracked, modified, staged, or clean, and which branch you are on.

```bash
git diff
```

This shows the line-by-line difference between the working tree and what is currently staged (or the last commit, if nothing is staged) — the change nobody has agreed to keep yet.

```bash
git diff --staged
```

This shows the difference between what is staged and the last commit — the change you are about to commit. This is a different question from `git diff` and students frequently confuse the two.

```bash
git diff --stat
```

This gives a compact summary — file names and how many lines changed — useful for a quick "did anything unexpected touch a file I didn't intend to change" scan before reading a full diff.

```bash
git diff --check
```

This flags obvious problems in the diff itself, such as trailing whitespace or unresolved conflict markers left in a file. It is a cheap sanity check, not a substitute for reading the diff.

---

## `git diff` is not the same question as a test suite

This distinction matters enough to say plainly:

```text
git diff        -> what source changed?
test / build / run -> what behavior can we currently verify?
```

Imagine `trail_mix.py`'s diff shows one new function added, cleanly, with no changes to existing code. That answers "what changed." It does not answer "does the program still work." Running the test suite is a separate, necessary step — one this station keeps returning to.

Neither substitutes for the other. A clean diff can still hide a bug. A passing test suite does not tell you whether the diff also did something you didn't ask for, outside what the tests happen to cover.

---

## A worked example

Suppose a student opens `trail_mix.py` and changes one line — say, a comment or a small formatting fix. Before doing anything else:

```bash
git status
```

```text
On branch main
Changes not staged for commit:
  modified:   trail_mix.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Then:

```bash
git diff
```

This shows exactly the lines that changed — and nothing else. If more than the intended lines show up as different, that is worth stopping and understanding before going further, not something to shrug past.

If the change is staged next:

```bash
git add trail_mix.py
git diff --staged
```

The second command now shows the same change, but framed as "this is what the next commit will contain" — a distinct question from "what does the working tree currently look like compared to the last commit."

---

## Completion signal

Student can explain the difference between reading a diff and running a verification step — in their own words, without looking back at this page.

A useful way to check yourself: can you explain why a program could have a perfectly clean, minimal `git diff` and still be broken? And why a program could pass every test and still have a `git diff` full of unrelated, unreviewed changes?

If you can answer both, you are ready for:

**04 — Try It: Make One Tiny Human Change and Preserve It**
