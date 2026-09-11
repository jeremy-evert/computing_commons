# 02 — AI + Git Safety Belt Lab

## Why we are doing this

AI coding tools can change a project very quickly.

That is useful.

It also means we need a reliable way to answer:

- Where am I?
- What state did I start from?
- What did the AI actually change?
- Did it stay inside the task I gave it?
- Does the project still work?
- Do I want to keep this change?

Our rule for this lab is simple:

> **Git is the safety belt.**
>
> AI may help drive the change. The human still owns the decision to keep it.

This lab uses the public practice repository:

`jeremy-evert/git-safety-belt-lab`

The code is intentionally tiny. The point is not trail mix. The point is learning how to remain in control when an AI tool edits code for you.

---

# Part 1 — Make sure Git is ready

Open PowerShell on Windows, or a terminal on Linux/macOS.

Run:

```text
git --version
```

If Git prints a version number, continue.

If Git is not installed on a personally controlled Windows computer, install **Git for Windows** from the official Git website, reopen PowerShell, and verify again with `git --version`.

If a university-managed computer asks for an administrator password or blocks installation, stop. Do not bypass the computer's security controls.

## Configure your Git identity

Before you make commits, Git needs to know what name and email to record.

Use **your own** information:

```text
git config --global user.name "Your Name"
git config --global user.email "your-email-address"
```

Verify:

```text
git config --global --get user.name
git config --global --get user.email
```

Use an email associated with your GitHub account if you want GitHub to attribute the commits to that account.

Do not copy another person's Git identity settings.

---

# Part 2 — Get the practice repository

Fork the course practice repository on GitHub if your instructor asks you to work in your own fork.

Then clone the repository you are supposed to use.

Example:

```text
git clone git@github.com:YOUR-GITHUB-USERNAME/git-safety-belt-lab.git
cd git-safety-belt-lab
```

If SSH authentication is not configured, use the HTTPS clone address shown by GitHub instead.

Installing Git and authenticating to GitHub are separate checkpoints.

---

# Part 3 — Establish a known starting state

Before asking AI to edit anything, prove where you are.

Run these commands one at a time:

```text
git rev-parse --show-toplevel
git branch --show-current
git rev-parse --short HEAD
git status
git log -1 --oneline --decorate
git remote -v
```

You should be able to fill in:

```text
Repository: _________________________________
Branch: _____________________________________
Starting HEAD: ______________________________
Working tree: clean / not clean
Remote: _____________________________________
```

## Why this matters

A commit hash is stronger evidence than saying:

> I started from the latest version.

"Latest" can change.

A commit identifier names one exact snapshot.

## Stop condition

If `git status` shows old changes you do not understand, stop.

Do not mix mystery edits with a new AI experiment.

---

# Part 4 — Verify the starter project before changing it

We need evidence that the project worked **before** AI touched it.

### Windows

Try:

```text
py -3 -B trail_mix.py
py -3 -B -m unittest discover -s tests -v
```

If `py -3` is not your Python launcher but `python` is Python 3, use `python` instead.

### Linux / macOS

Run:

```text
python3 -B trail_mix.py
python3 -B -m unittest discover -s tests -v
```

Expected program output includes:

```text
Trail mix pieces: 30
Complete servings of 5: 6
```

Expected test result:

```text
Ran 3 tests

OK
```

## What this proves

It supports the claim:

> The current starter code passed these three tests in this environment.

It does **not** prove the program is correct for every possible input.

---

# Part 5 — Create a branch for the experiment

Do not experiment directly on `main` for this exercise.

Create a branch:

```text
git switch -c lab/average-pieces
```

Then verify:

```text
git branch --show-current
git rev-parse --short HEAD
git status
```

The branch name should change.

The commit hash should initially stay the same.

That is an important idea:

> Creating a branch does not change the program. It creates another movable pointer to the same starting snapshot.

---

# Part 6 — Bound the AI task

We are going to ask an AI coding tool to make **one tiny change**.

The task is:

```text
Modify only trail_mix.py.

Add a new function:

    average_pieces_per_category(pretzels, raisins, chocolate)

The function should return the arithmetic mean of the three values as a float.

Examples:
- average_pieces_per_category(12, 8, 10) returns 10.0
- average_pieces_per_category(3, 3, 3) returns 3.0

Acceptance criteria:
1. Existing behavior must remain unchanged.
2. total_items() must still work.
3. servings_possible() must still work.
4. The program must still run from the command line.
5. Modify only trail_mix.py.
6. Do not add dependencies.
7. Do not push anything to GitHub.
```

Notice what this prompt contains:

```text
FILE BOUNDARY
trail_mix.py

BEHAVIOR
add one function

ACCEPTANCE CONDITIONS
specific examples + existing behavior remains intact

AUTHORITY BOUNDARY
AI edits; human inspects and decides what survives
```

That is a bounded task.

"Improve this project" is not.

---

# Part 7 — Run Aider

First check that Aider is installed:

```text
aider --version
```

For the Fall 2026 lab environment, one possible local model command is:

```text
aider --model ollama/qwen2.5-coder:3b trail_mix.py
```

Your instructor may provide a different approved model or AI tool.

If Aider reports that no model is configured, that is not a Git failure and not a repository failure. It is an AI-tool configuration problem.

Diagnose the layer that actually failed.

## Repository hygiene prompt

Aider may ask whether it should add `.aider*` to `.gitignore`.

This creates a useful distinction:

```text
Source code        -> track it
Tests              -> track it
Documentation      -> track it
Tool cache/history -> usually ignore it
```

If `.gitignore` changes, inspect that change just like any other repository change.

---

# Part 8 — Do not trust the summary. Inspect Git.

When the AI finishes, do **not** jump straight to `git add` or `git push`.

Run:

```text
git status --short
git diff --stat
git diff
```

Ask:

- Which files changed?
- Did only the authorized file change?
- Did the AI add behavior I did not request?
- Did it remove or rewrite unrelated behavior?
- Did a new file appear?
- Did the AI commit automatically?

## Important real-world lesson

During the original classroom run, Aider was asked to add one function.

It added the function **and** added a new print statement to the command-line program.

That extra output was reasonable, but it was outside the narrow request.

This is scope creep.

The lesson is not:

> AI failed.

The lesson is:

> AI made a choice. Git made that choice inspectable.

---

# Part 9 — AI tools may have more authority than you expected

During the original lab run, Aider also created a Git commit automatically.

That mattered because the intended lesson was:

> The AI may edit. The human inspects, verifies, stages, commits, and pushes.

Some AI coding tools can commit automatically unless configured otherwise.

For Aider, your instructor may use:

```text
--no-auto-commits
```

Example:

```text
aider --no-auto-commits --model ollama/qwen2.5-coder:3b trail_mix.py
```

The important principle is broader than Aider:

> Before using an AI coding tool, know what authority the tool has.

Can it only suggest text?

Can it edit files?

Can it create files?

Can it run commands?

Can it commit?

Can it push?

Those are different levels of authority.

---

# Part 10 — Verify independently

After inspecting the diff, run the program and tests yourself.

### Windows

```text
py -3 -B trail_mix.py
py -3 -B -m unittest discover -s tests -v
```

### Linux / macOS

```text
python3 -B trail_mix.py
python3 -B -m unittest discover -s tests -v
```

Then directly check the new function.

### Windows

```text
py -3 -B -c "from trail_mix import average_pieces_per_category; assert average_pieces_per_category(12,8,10) == 10.0; assert average_pieces_per_category(3,3,3) == 3.0; print('Direct acceptance checks: PASS')"
```

### Linux / macOS

```text
python3 -B -c "from trail_mix import average_pieces_per_category; assert average_pieces_per_category(12,8,10) == 10.0; assert average_pieces_per_category(3,3,3) == 3.0; print('Direct acceptance checks: PASS')"
```

## Why both Git and tests?

They answer different questions.

```text
git diff
    -> What source changed?

tests / example runs
    -> What behavior can we currently verify?
```

Neither substitutes for the other.

---

# Part 11 — Decide what deserves to survive

If the AI made an extra change you do not want, correct it before preserving the work.

Then inspect again:

```text
git status --short
git diff
git diff --check
```

When the working change is exactly what you intend, stage only the intended files:

```text
git add trail_mix.py
```

If `.gitignore` was intentionally added or updated, stage it separately after inspecting it:

```text
git add .gitignore
```

Inspect what is staged:

```text
git diff --staged
```

Only then commit:

```text
git commit -m "Add average pieces calculation"
```

Check the result:

```text
git log -1 --oneline --decorate
git status
```

Push only when your instructor tells you to publish the branch:

```text
git push -u origin lab/average-pieces
```

---

# Part 12 — What if something goes wrong?

The Git Safety Belt does not guarantee that AI will make a perfect change.

It gives you tools to inspect and recover.

For an unwanted **uncommitted** edit to a file:

```text
git restore trail_mix.py
```

For a bad commit that has already been shared, prefer a history-preserving reversal:

```text
git revert <commit>
```

Do not make destructive reset commands your first beginner reflex.

If you are unsure what state the repository is in, stop and inspect:

```text
git status
git log --oneline --decorate -5
git diff
git diff --staged
```

Failure is data.

Random commands are not diagnosis.

---

# Part 13 — One more safety lesson: copy commands from code blocks

During the original classroom experiment, commands copied through formatted text were corrupted with things such as:

```text
<br>
&gt;
***
```

PowerShell then tried to execute broken commands.

The repository itself was not damaged, but the terminal session became a confetti cannon of parser errors.

For command-line work:

- copy commands from plain code blocks;
- prefer short commands over giant clever scripts;
- run one logical step at a time;
- inspect the output before moving on.

A complicated safety script can become a new source of failure.

For this lab, simple inspection commands are usually better.

---

# The full workflow

```text
KNOWN STARTING STATE
        ↓
CLEAN WORKING TREE
        ↓
CREATE A BRANCH
        ↓
VERIFY STARTER BEHAVIOR
        ↓
BOUND THE AI TASK
        ↓
AI EDITS
        ↓
INSPECT GIT STATUS + DIFF
        ↓
VERIFY BEHAVIOR INDEPENDENTLY
        ↓
CORRECT SCOPE CREEP IF NEEDED
        ↓
STAGE INTENTIONALLY
        ↓
INSPECT STAGED DIFF
        ↓
HUMAN COMMITS
        ↓
PUBLISH WHEN APPROPRIATE
```

# What this lab is really teaching

You do not need to type faster than AI.

You need to become good at controlling the boundary around the work.

By the end of this lab, you should be able to say:

```text
Here is the repository I used.
Here is the branch I worked on.
Here is the exact commit I started from.
Here is the task I gave the AI.
Here is what Git says changed.
Here is how I verified the behavior.
Here is what I chose to preserve.
Here is what my evidence supports.
Here is what my evidence does not prove.
```

That is the beginning of professional AI-assisted development.

---

# Completion receipt

Submit a short Markdown receipt containing:

```text
Repository:
Branch:
Starting HEAD:
AI tool/model:
Bounded task:
Files changed:
Verification command(s):
Verification result:
Final commit:

What changed according to Git?

Why are you willing to keep the change?

What does this evidence NOT prove?
```
