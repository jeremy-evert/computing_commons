# 04 — Try It: Make One Tiny Human Change and Preserve It

## Core question

**Can I make one intentional change and turn it into useful history?**

This is the first hands-on commit of the station. No AI involved yet — the point is to build the human-driven version of the loop before adding a second actor to it.

---

## Before you start

Confirm you know your starting state (this should already be a reflex from 02):

```bash
git status --short --branch
git rev-parse --short HEAD
```

Start from a clean working tree. If `git status` already shows changes you don't recognize, stop and understand those first — don't layer a new intentional change on top of a mystery one.

---

## Student task

Working in the Safety Belt Lab (`jeremy-evert/git-safety-belt-lab`), make **one tiny visible change**. Keep it small on purpose — this lesson is about the discipline of the loop, not the size of the edit. A reasonable example: add one line to `README.md` describing what you're currently working on, or adjust one comment in `trail_mix.py`.

Then work through the loop one command at a time — do not skip ahead to `git commit` out of habit:

```bash
git status --short
```

Confirm only the file(s) you meant to touch show up as modified.

```bash
git diff
```

Read it. All of it. This is the step students most often skip once they get comfortable, and it's the step that matters most.

```bash
git diff --check
```

A cheap check for stray whitespace or formatting problems before you commit them into history.

```bash
git add <specific-file>
```

Stage the exact file you intend to commit — not `git add .`, not `git add -A`. Naming the file is part of the discipline: you should always be able to say what you're about to commit before you commit it.

```bash
git diff --staged
```

Confirm what's staged matches what you intended — this is your last look before it becomes permanent history.

```bash
git commit -m "Describe the useful change"
```

Write a commit message that describes *why* the change exists, not just "update file." Look back at the Safety Belt Lab's own commit history from lesson 01 — `Add verification tests`, `Document the verification workflow` — for the shape a useful message takes.

```bash
git log -1 --oneline
git status --short --branch
```

Confirm the commit landed and the working tree is clean again.

If your assigned repository allows it, publish the work:

```bash
git push
```

---

## Teaching emphasis — do not reward "commit everything" behavior

It is tempting, especially once a student is comfortable with the commands, to run `git add .` out of habit and commit whatever happens to be sitting in the working tree. Resist that.

The question this lesson is really testing is not "can you run `git commit`" — it's:

> Do you know what you staged, and can you say why the commit exists?

A student who can point to their own `git diff --staged` output and explain every line is doing the actual skill. A student who committed a pile of unrelated changes because it was easier than checking is not — even if the commit technically succeeded.

---

## What this is building toward

This exact loop — status, diff, stage, review staged diff, commit, confirm — is the same loop you will run again in lesson 06 once an AI tool is doing the editing instead of you. Learning it cleanly here, with a human-authored change you fully understand, makes the AI-assisted version in 06 a variation on a habit you already have rather than a brand-new skill under pressure.

---

## Completion signal

One useful commit whose diff the student inspected *before* committing — not after, and not skipped entirely. If you can show your own `git status`, `git diff`, and `git log -1 --oneline` output for the change you made, you've met the bar.

Ready for:

**05 — Video: AI at the Keyboard, Human on the Commit**
