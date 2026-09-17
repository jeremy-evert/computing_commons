# 10 — Try It: Publish a Git Evidence Receipt

## Core question

**Can another person inspect what I changed and why I trust it?**

This is the capstone exercise for the station. Every earlier lesson has been building toward the habit of producing evidence, not just claims — lesson 03's diffs, lesson 04's inspected commit, lesson 06's verification reflection, lesson 08's recovery evidence. This lesson turns that habit into one standing, submittable shape.

---

## Required receipt

Using either the change you made in lesson 04, the AI-assisted change from lesson 06, or a new bounded change of your own in the Safety Belt Lab, produce a compact Markdown receipt containing:

```text
repository
branch
starting commit
bounded task
files changed / diff stat
verification command
verification result
final commit
final git status
GitHub commit or pull-request location when available
student explanation: what changed
student explanation: why the evidence is sufficient for the claim being made
student limitation: what this receipt does NOT prove
```

Every field above should be something you can point to real command output for — not something you're recalling from memory or paraphrasing from an AI tool's summary.

---

## Recommended command capture

Run these against your final commit to gather the material for the receipt fields above:

```bash
git status --short --branch
git rev-parse --short HEAD
git show --stat --oneline HEAD
git diff --check HEAD^ HEAD
```

`git show --stat --oneline HEAD` gives you the commit message and the file-level summary of what that commit changed — useful directly for the "files changed / diff stat" field. `git diff --check HEAD^ HEAD` re-runs the same sanity check from lesson 03 against the committed change itself, one more time, before you publish it as evidence.

The project-specific test/build command belongs beside those Git receipts — for the Safety Belt Lab, that's the same `python3 -B trail_mix.py` and `python3 -B -m unittest discover -s tests -v` pair used throughout this station.

---

## The two explanation fields matter as much as the commands

It is easy to treat this receipt as a checklist of command output and skip the two written explanation fields. Don't. They're the actual point.

**"Why is this evidence sufficient for the claim being made?"** — Be specific. "The tests passed" is weaker than "the test suite exercises the exact function I changed, and no other files were touched, so the passing result speaks directly to this change."

**"What does this receipt NOT prove?"** — This is the field students most often want to skip, and the one lesson 00 named as mattering most:

> A clean Git history can tell a very useful story. It can also tell a beautifully organized story about incorrect code.

A passing test suite proves the tested behavior worked in this environment, on these inputs. It does not prove the program is correct for every input, that it will behave the same way on a different machine, or that nothing outside the test suite's coverage is broken. Naming that limitation honestly is not a weakness in the receipt — it's what makes the rest of the receipt trustworthy.

---

## An example of the shape, briefly

```text
Repository: jeremy-evert/git-safety-belt-lab
Branch: ai/largest-category
Starting commit: c8e294b
Bounded task: add largest_category(pretzels, raisins, chocolate) to trail_mix.py, no other changes
Files changed: trail_mix.py (+9, -0)
Verification command: python3 -B -m unittest discover -s tests -v
Verification result: Ran 3 tests, OK
Final commit: <short hash>
Final git status: clean, branch ai/largest-category, 1 commit ahead of main
GitHub location: <pull request URL, if published>

What changed: one new function added to trail_mix.py; no existing
function or test was modified.

Why this evidence is sufficient: the diff shows only the new function;
the full existing test suite still passes unchanged, and a direct check
of the new function's two example cases also passed.

What this does NOT prove: the function has not been tested against
inputs where two categories tie for the largest count, and this receipt
says nothing about performance or behavior outside this repository's
environment.
```

That's the level of specificity to aim for — not a longer receipt, a more honest one.

---

## Completion signal

A receipt another student could inspect without needing the original AI chat, or without needing to ask you what you meant — every claim in it backed by something they could independently re-run or verify themselves.

This is the last "Try It" page in the core sequence. From here:

**11 — Where This Goes Next in Computer Science**
