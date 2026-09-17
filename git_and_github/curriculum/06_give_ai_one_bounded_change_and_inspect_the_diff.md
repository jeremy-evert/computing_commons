# 06 — Try It: Give AI One Bounded Change and Inspect the Diff

## Core question

**Can I delegate without surrendering control?**

This is lesson 05's practice, run for real. If you completed the integrated Fall 2026 lab (`02_ai_git_safety_belt_lab.md`), the shape of this exercise will feel familiar — this is the same discipline in a smaller, standalone slice.

---

## Assumption stated up front

This page uses the same practice repository as every other lesson, `jeremy-evert/git-safety-belt-lab`, and gives you a small bounded task of the same size and shape as the one in the integrated lab, but not the identical task — so that working through this page doesn't just repeat work you may have already done. If your instructor assigns the integrated lab's own task instead, follow their instruction; the loop below is the same either way.

---

## Start clean and create a branch

```bash
git status --short --branch
```

Confirm the working tree is clean before you begin. If it isn't, resolve that first — don't layer this exercise on top of an unrelated dirty state.

```bash
git switch -c ai/largest-category
```

---

## Give the approved AI tool one small task

A bounded task for this exercise:

```text
Modify only trail_mix.py.

Add a new function:

    largest_category(pretzels, raisins, chocolate)

The function should return the name of the category ("pretzels",
"raisins", or "chocolate") with the largest count. Assume no ties.

Acceptance criteria:
1. Existing behavior must remain unchanged.
2. The program must still run from the command line.
3. Modify only trail_mix.py.
4. Do not add dependencies.
5. Do not commit or push anything.
```

Notice the same four elements from lesson 05's task-bounding principle: a file boundary, a behavior, acceptance conditions, and an explicit authority boundary (the AI edits; you decide what survives).

---

## After the AI acts, inspect before you trust

```bash
git status --short
git diff --stat
git diff
git diff --check
```

Read the diff. Confirm only `trail_mix.py` changed. Confirm the new function matches what you asked for and nothing else was added, removed, or rewritten.

---

## Verify independently

Run the assigned test/build/example command for this project — do not ask the AI tool whether its own change works. For the Safety Belt Lab:

```bash
python3 -B trail_mix.py
python3 -B -m unittest discover -s tests -v
```

Then check the new function directly, since the existing test suite won't know about it yet:

```bash
python3 -B -c "from trail_mix import largest_category; assert largest_category(12,8,10) == 'pretzels'; assert largest_category(2,9,4) == 'raisins'; print('Direct acceptance checks: PASS')"
```

---

## Only after inspection and verification, commit

```bash
git add trail_mix.py
git diff --staged
git commit -m "Implement largest_category bounded change"
```

Confirm the result:

```bash
git log -1 --oneline --decorate
git status --short --branch
```

---

## Required reflection

Write two sentences:

1. What did the AI actually change, according to Git — not according to the AI's own summary?
2. What independent evidence makes you willing to preserve this change?

If you cannot answer the second question with something more specific than "it looked right," you are not done with the verification step yet — go back and run the direct check above.

---

## Completion signal

A bounded AI-assisted commit, plus a written verification receipt (the two-sentence reflection above, backed by real command output you can show).

Ready for:

**07 — Video: Branches, Pull Requests, Conflicts, and Recovery**
