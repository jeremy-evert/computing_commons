# 08 — Try It: Break Something Small, Recover, and Verify

## Core question

**Can I recover because I understand the state, not because I found a magic command online?**

## Assumption stated up front

The README spec for this lesson names the shape of the exercise (break something, capture the failure, recover, verify) without naming the exact break to introduce. This page builds one concrete, bounded scenario using `trail_mix.py` in the Safety Belt Lab, consistent with the functions introduced in lessons 02 and 06. If your instructor assigns a different intentional break, the loop below still applies — only the specific edit changes.

---

## Step 1 — Begin from a known clean commit

```bash
git status --short --branch
git rev-parse --short HEAD
git log -1 --oneline --decorate
```

Confirm the working tree is clean and you know exactly which commit you're starting from. Write it down. You will need it later to prove you got back to it.

---

## Step 2 — Verify the starting behavior

Before breaking anything, prove it currently works — the same habit from lesson 02:

```bash
python3 -B trail_mix.py
python3 -B -m unittest discover -s tests -v
```

Expected output includes `Trail mix pieces: 30`, `Complete servings of 5: 6`, and a test result of `Ran 3 tests` / `OK`. This is your "before" evidence.

---

## Step 3 — Make a deliberate bounded edit that causes the check to fail

Open `trail_mix.py` and intentionally change the servings calculation — for example, change the divisor used to compute `servings_possible()` from `5` to `4`. This is a small, single-line, easy-to-explain break, chosen on purpose: it will make the test suite's assertion about `servings_possible()` fail without touching anything else in the file.

---

## Step 4 — Capture the failure

Run the same verification as step 2:

```bash
python3 -B -m unittest discover -s tests -v
```

You should now see a test failure — the assertion that checked `servings_possible()`'s expected value no longer matches the actual result. Capture the actual failure output. This is your evidence that something broke, not just a feeling that something might be wrong.

---

## Step 5 — Inspect the diff

```bash
git status --short
git diff
```

Read the diff. Confirm it shows exactly the one-line change you intentionally made — nothing more. This is the diagnosis step: you should be able to point at the diff and say precisely why the test is now failing, not just that it is failing.

---

## Step 6 — Recover using the assigned safe recovery technique

Because this is an **uncommitted** change you want to discard entirely, the correct tool from lesson 07's recovery ladder is:

```bash
git restore trail_mix.py
```

This is not the tool you would reach for if the broken change had already been committed and pushed — that situation calls for `git revert`, per lesson 07. Knowing which situation you're in is part of the exercise.

---

## Step 7 — Rerun verification

```bash
python3 -B trail_mix.py
python3 -B -m unittest discover -s tests -v
```

Confirm the output matches step 2 exactly — the same pass count, the same program output.

---

## Step 8 — Prove the working tree is back in the intended state

```bash
git status --short --branch
git rev-parse --short HEAD
git diff
```

`git status` should report a clean tree. `git rev-parse --short HEAD` should match the commit you recorded in step 1. `git diff` should show nothing.

---

## Evidence to collect

Your submission for this exercise should show all seven pieces below, in order:

```text
starting commit
intentional failure
failing verification
relevant diff
recovery action
passing verification
final git status
```

This is not extra busywork — it's the same evidence pattern lesson 10 will formalize into a standing receipt shape.

---

## Completion signal

A recovery receipt that shows failure, diagnosis, recovery, and verification — in that order, with real command output backing each step, not a description of what you assume would have happened.

Ready for:

**09 — Video: Secrets, Ignore Rules, Generated Files, and Repository Hygiene**
