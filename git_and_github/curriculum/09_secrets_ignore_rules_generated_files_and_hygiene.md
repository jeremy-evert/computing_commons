# 09 — Video: Secrets, Ignore Rules, Generated Files, and Repository Hygiene

## Core question

**What should never become project history in the first place?**

Everything so far in this station has been about inspecting and preserving change well. This lesson is about the other half of the job: knowing what should never be preserved at all.

---

## What should never be committed

- passwords, API keys, tokens, private keys, and credentials;
- `.env` and other local secret/config files;
- build products and generated artifacts;
- editor and operating-system noise (temp files, swap files, OS metadata);
- giant datasets and binaries, unless the project intentionally manages them;
- machine-specific paths and temporary files.

None of these belong in source history — not because they're unimportant, but because they're either sensitive, regenerable, or specific to one machine in a way that pollutes a shared project.

---

## `.gitignore` as an explicit project boundary

`.gitignore` tells Git which files to leave alone — to never show as untracked, never suggest staging, never accidentally sweep up with a careless `git add .` (which is itself another reason lesson 04's "stage the specific file, not everything" habit matters).

Think of `.gitignore` as a written, explicit boundary around the project, the same way lesson 06's bounded-task prompts named an explicit file boundary for an AI tool. Both are the same underlying idea: say clearly what is and isn't in scope, rather than leaving it to be discovered by accident.

You already saw this in the integrated lab (`02_ai_git_safety_belt_lab.md`): an AI coding tool may ask whether it should add its own cache/history files to `.gitignore`. That's a real, recurring pattern worth naming explicitly:

```text
Source code        -> track it
Tests              -> track it
Documentation       -> track it
Tool cache/history  -> usually ignore it
```

If `.gitignore` itself changes, inspect that change the same way you'd inspect any other diff — it is, after all, still a change to the repository.

---

## Why deleting a secret from the newest file doesn't mean it's gone

This is the single most important idea in this lesson, and the one most likely to surprise a student the first time they encounter it:

> **Deleting a secret from the current version of a file does not remove it from Git history.**

A commit is a preserved snapshot — you learned that in lesson 01. If a credential was committed once, it exists in every commit made since, in the repository's full history, even after a later commit removes it from the current file. Anyone who clones the repository, or looks at an old commit, can still find it.

The practical consequence: if a secret is ever accidentally committed, the fix is not "delete it and commit again." The credential has to be treated as compromised and rotated — a new key generated, the old one revoked — because the old value is permanently recoverable from history by anyone with read access to the repository.

This is exactly the kind of thing `.gitignore` exists to prevent in the first place: it's far cheaper to keep a secret out of Git than to remove one that already got in.

---

## AI-era warning

AI coding tools can accidentally create credential files, debug dumps, local caches, copied datasets, or other generated files while working on a task — sometimes as a side effect of the work you actually asked for, sometimes unprompted.

This connects directly back to lesson 05's stop conditions: an unexpected new file appearing is exactly the kind of thing `git status` catches immediately, and exactly the kind of thing that should make you pause before staging anything.

> **Always inspect `git status` before staging** — not just to see what changed, but to see what's newly present that you didn't expect.

---

## Completion signal

Student can identify, from a short example scenario or file listing:

- one file that belongs in source history;
- one file that should usually be ignored;
- one file that must never be committed under any circumstances.

And can explain, without looking back at this page, why removing a secret from the latest commit does not remove it from the repository.

Ready for:

**10 — Try It: Publish a Git Evidence Receipt**
