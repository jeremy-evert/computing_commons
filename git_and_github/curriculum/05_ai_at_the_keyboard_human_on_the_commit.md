# 05 — Video: AI at the Keyboard, Human on the Commit

## Core question

**What changes when an AI tool can edit the repository for me?**

## The answer, stated plainly

The speed changes. The ownership model does not.

An AI coding tool can produce a working-tree change in seconds that would have taken a human minutes or hours to type. That is genuinely useful. It does not change who is responsible for deciding whether that change becomes part of the project's permanent history. That decision is still the student's, every time.

---

## Before delegating anything

Record where you're starting from — the same habit from lesson 04, now non-negotiable rather than optional:

```bash
git status --short --branch
git rev-parse --short HEAD
```

Prefer a clean working tree before handing anything to an AI tool. If the tree is already dirty, you will not be able to cleanly tell "what did I already have" apart from "what did the AI just do."

For work that should be isolated from `main` while it's being explored:

```bash
git switch -c <descriptive-branch-name>
```

A branch name that describes the task (`ai/add-average-function`, not `ai/test` or `ai/branch1`) does real work later — it's the label that will show up in `git branch --show-current`, in a pull request, and in your own memory of what this line of work was for.

---

## Bound the AI task before you hand it over

A strong task for an AI coding tool names one or more of:

- the exact file or small file set it may touch;
- the behavior to change;
- what must **not** change;
- the test or acceptance condition that will decide success;
- the stopping condition — when the tool should stop and hand control back.

"Improve this project" is not a bounded task. "Add a function to `trail_mix.py` that does X, matching these examples, without touching anything else" is. The difference is not politeness — it's what makes the resulting diff possible to inspect quickly and confidently.

---

## After the AI acts — do not stop at the summary

An AI tool will typically tell you what it believes it did. That sentence is a claim, not evidence, exactly as in lesson 03.

Do not ask the model whether it succeeded and stop there. Inspect:

```bash
git status --short
git diff --stat
git diff
git diff --check
```

Read the actual diff. Confirm the file set matches what you authorized. Then run the independent verification appropriate to the project — for the Safety Belt Lab, that means actually running `trail_mix.py` and its test suite, not asking the AI tool whether the tests would pass.

---

## Stop conditions

Pause the change — do not push forward, do not ask the AI to "just fix it" — when:

- unrelated files changed;
- generated or binary junk appeared that you did not expect;
- the change is much larger than the task you gave it;
- tests fail;
- the tool changed security, dependency, configuration, or data-handling behavior outside the scope you named;
- you cannot explain the diff well enough to own it yourself.

That last condition is worth sitting with. If you cannot explain what changed and why, in your own words, to someone else, you are not ready to commit it — no matter how confident the AI tool sounded.

---

## A real example of exactly this failure mode

The Safety Belt Lab's own classroom history has a concrete instance of the second stop condition above: an AI coding tool, asked to add one function, also added an unrequested print statement to the program's output. Reasonable on its own, but outside the narrow request — a small, clean example of scope creep that only showed up because someone actually read `git diff` instead of trusting the tool's summary.

The lesson from that moment was not "AI failed." It was:

> **AI made a choice. Git made that choice inspectable.**

That is the whole point of this station, said one more way.

---

## Completion signal

Student can state why "the AI said it worked" is not an acceptable verification receipt — and can name at least one concrete stop condition from the list above in their own words.

Ready for:

**06 — Try It: Give AI One Bounded Change and Inspect the Diff**
