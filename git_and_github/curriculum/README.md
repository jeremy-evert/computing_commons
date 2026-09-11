# Git + GitHub Curriculum

This curriculum is the shared Computing Commons station for source management in the age of AI-assisted computing.

It is designed for Canvas delivery in short videos and bounded hands-on activities. The sequence is cumulative. Students should be able to revisit earlier pieces when they need recovery.

## Canvas arc

```text
00 — Start Here: Git Is the Safety Belt
01 — Video: Git, GitHub, Repositories, Commits, Branches, and Remotes
02 — Try It: Open a Repo and Run the Git Preflight
03 — Video: Status and Diff Are the Truth
04 — Try It: Make One Tiny Human Change and Preserve It
05 — Video: AI at the Keyboard, Human on the Commit
06 — Try It: Give AI One Bounded Change and Inspect the Diff
07 — Video: Branches, Pull Requests, Conflicts, and Recovery
08 — Try It: Break Something Small, Recover, and Verify
09 — Video: Secrets, Ignore Rules, Generated Files, and Repository Hygiene
10 — Try It: Publish a Git Evidence Receipt
11 — Where This Goes Next in Computer Science
```

### Integrated Fall 2026 student lab

The September 11 CS2 teaching run produced a tested guided pathway that spans several of the smaller Canvas slices above:

[`02_ai_git_safety_belt_lab.md`](02_ai_git_safety_belt_lab.md)

Use that integrated lab for the Fall 2026 soft launch while the smaller 02–10 Canvas pages are being split and polished. It preserves the real classroom evidence around Git identity, baseline verification, branches, bounded AI work, Aider authority, `.gitignore`, scope creep, diff inspection, tests, recovery, and receipts.

The week should feel like one repeating loop rather than eleven unrelated pages:

```text
KNOW WHERE YOU ARE
  ↓
KNOW WHAT CHANGED
  ↓
VERIFY WHAT HAPPENED
  ↓
PRESERVE THE GOOD STATE
  ↓
PUBLISH / REVIEW
  ↓
RECOVER WHEN NEEDED
```

## 00 — Start Here: Git Is the Safety Belt

### Core question

**Why does version control matter more when AI can change code quickly?**

### Student takeaway

Git is not primarily a command vocabulary exercise. It is the mechanism that lets a student work boldly without surrendering history, inspection, or recovery.

Introduce three class rules:

1. **In God we trust. Everything else we verify.**
2. **Love AI more. Trust AI less.**
3. **Git is the safety belt.**

### Completion signal

Student can explain, in their own words, why an AI-generated change should be inspected through Git before it is accepted.

---

## 01 — Video: Git, GitHub, Repositories, Commits, Branches, and Remotes

### Core question

**Where does my work actually live?**

### Concepts

- Git is the version-control system.
- GitHub is a remote collaboration and publishing service built around Git repositories.
- working tree: files currently visible and editable;
- repository: working files plus version history and Git metadata;
- commit: a named snapshot in project history;
- branch: a movable line of development;
- remote: another repository location, commonly on GitHub;
- `origin`: a conventional remote name, not magic;
- `HEAD`: the commit/branch position the student is currently working from.

### Misconceptions to kill early

- Saving a file is not committing it.
- Committing is not pushing.
- Pushing does not prove the program is correct.
- GitHub is not Git.
- A repository is not automatically synchronized merely because it has a remote.

### Completion signal

Student can look at a simple local-plus-GitHub diagram and identify where an edit, commit, and push occur.

---

## 02 — Try It: Open a Repo and Run the Git Preflight

### Core question

**Before I change anything, can I prove where I am and what state the project is in?**

### Minimum command set

```bash
pwd
git rev-parse --show-toplevel
git status --short --branch
git remote -v
git log --oneline --decorate -5
```

Optional orientation:

```bash
git branch --show-current
git rev-parse --short HEAD
```

### Student task

Open or clone the assigned practice repository. Do not edit anything yet.

Capture:

- repository root;
- current branch;
- current short commit ID;
- remote destination;
- whether the working tree is clean or dirty;
- the five most recent commits.

### Completion signal

A small preflight receipt showing the student knows exactly what repository and state they are about to change.

---

## 03 — Video: Status and Diff Are the Truth

### Core question

**What actually changed?**

### Concepts

Teach the working tree and staging area only as deeply as needed to make inspection useful.

Primary inspection commands:

```bash
git status
git diff
git diff --staged
git diff --stat
git diff --check
```

### AI-era principle

A model can say, "I only changed the requested function."

Git can show what changed.

The student should learn to privilege inspectable artifacts over conversational confidence.

### Useful distinction

`git diff` answers a different question from a test suite.

- diff: **what source changed?**
- test/build/run: **what behavior can we currently verify?**

Neither substitutes for the other.

### Completion signal

Student can explain the difference between reading a diff and running a verification step.

---

## 04 — Try It: Make One Tiny Human Change and Preserve It

### Core question

**Can I make one intentional change and turn it into useful history?**

### Student task

Make one tiny visible change in the practice repository.

Then:

```bash
git status --short
git diff
git diff --check
git add <specific-file>
git diff --staged
git commit -m "Describe the useful change"
git log -1 --oneline
git status --short --branch
```

Push when the assigned repository allows it:

```bash
git push
```

### Teaching emphasis

Do not reward "commit everything" behavior.

The student should know what they staged and why the commit exists.

### Completion signal

One useful commit whose diff the student inspected before committing.

---

## 05 — Video: AI at the Keyboard, Human on the Commit

### Core question

**What changes when an AI tool can edit the repository for me?**

### Answer

The speed changes. The ownership model does not.

### Before delegating

Record:

```bash
git status --short --branch
git rev-parse --short HEAD
```

Prefer a clean tree.

For work that should be isolated:

```bash
git switch -c <descriptive-branch-name>
```

### Bound the AI task

A strong task names one or more of:

- the exact file or small file set;
- the behavior to change;
- what must not change;
- the test or acceptance condition;
- the stopping condition.

### After the AI acts

Do not ask the model whether it succeeded and stop there.

Inspect:

```bash
git status --short
git diff --stat
git diff
git diff --check
```

Then run the independent verification appropriate to the project.

### Stop conditions

Pause the change when:

- unrelated files changed;
- generated/binary junk appeared unexpectedly;
- the change is much larger than the task;
- tests fail;
- the tool changed security, dependency, configuration, or data-handling behavior outside scope;
- the student cannot explain the diff well enough to own it.

### Completion signal

Student can state why "the AI said it worked" is not an acceptable verification receipt.

---

## 06 — Try It: Give AI One Bounded Change and Inspect the Diff

### Core question

**Can I delegate without surrendering control?**

### Student task

Start clean and create a branch:

```bash
git status --short --branch
git switch -c ai/<short-task-name>
```

Give the approved AI tool one small task.

Then capture:

```bash
git status --short
git diff --stat
git diff
git diff --check
```

Run the assigned test/build/example command.

Only after inspection and verification:

```bash
git add <intended-files>
git diff --staged
git commit -m "Implement <bounded change>"
```

### Required reflection

Two sentences:

1. What did the AI actually change according to Git?
2. What independent evidence makes the student willing to preserve the change?

### Completion signal

A bounded AI-assisted commit plus a verification receipt.

---

## 07 — Video: Branches, Pull Requests, Conflicts, and Recovery

### Core question

**How do we experiment and collaborate without making every change everybody else's problem immediately?**

### Branches

Teach branches as cheap lines of work, not as ceremony.

```bash
git branch --show-current
git switch -c feature/example
```

### Pull requests

A pull request is a reviewable proposal to integrate one line of work into another.

The student should be able to read:

- what commits are included;
- what files changed;
- the diff;
- checks/test status;
- review comments;
- whether the branch can merge cleanly.

### Conflicts

Teach conflict resolution conceptually before teaching tricks:

1. stop;
2. inspect the conflicting file;
3. understand both intended changes;
4. produce the desired final content;
5. verify behavior;
6. stage the resolved file;
7. continue the merge/rebase operation appropriate to the workflow.

### Recovery ladder

Prefer recovery tools that preserve evidence.

For an uncommitted file change you truly intend to discard:

```bash
git restore <file>
```

For a bad commit already shared/published, prefer a new history-preserving reversal:

```bash
git revert <commit>
```

Do not make destructive history rewriting the beginner's first reflex.

### Completion signal

Student can choose between "discard an uncommitted edit" and "revert a published commit" without treating them as the same problem.

---

## 08 — Try It: Break Something Small, Recover, and Verify

### Core question

**Can I recover because I understand the state, not because I found a magic command online?**

### Student task

In the practice repository:

1. begin from a known clean commit;
2. make a deliberate bounded edit that causes the provided check/test to fail;
3. capture the failure;
4. inspect the diff;
5. recover using the assigned safe recovery technique;
6. rerun the verification;
7. prove the working tree is back in the intended state.

### Evidence

```text
starting commit
intentional failure
failing verification
relevant diff
recovery action
passing verification
final git status
```

### Completion signal

A recovery receipt that shows failure, diagnosis, recovery, and verification.

---

## 09 — Video: Secrets, Ignore Rules, Generated Files, and Repository Hygiene

### Core question

**What should never become project history in the first place?**

### Topics

- passwords, API keys, tokens, private keys, and credentials;
- `.env` and other local secret/config files;
- `.gitignore` as an explicit project boundary;
- build products and generated artifacts;
- editor/OS noise;
- giant datasets and binaries unless the project intentionally manages them;
- machine-specific paths and temporary files;
- why deleting a secret from the newest file version does not mean it vanished from Git history.

### AI-era warning

AI tools can accidentally create credential files, debug dumps, local caches, copied datasets, or generated files. Always inspect `git status` before staging.

### Completion signal

Student can identify at least one file that belongs in source history, one that should usually be ignored, and one that must never be committed.

---

## 10 — Try It: Publish a Git Evidence Receipt

### Core question

**Can another person inspect what I changed and why I trust it?**

### Required receipt

A student submits a compact Markdown receipt containing:

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

Recommended command capture:

```bash
git status --short --branch
git rev-parse --short HEAD
git show --stat --oneline HEAD
git diff --check HEAD^ HEAD
```

The project-specific test/build command belongs beside those Git receipts.

### Completion signal

A receipt another student could inspect without needing the original AI chat.

---

## 11 — Where This Goes Next in Computer Science

Git is not a one-week topic that disappears after Friday.

### Computer Science I

- preserve working programs;
- make small intentional commits;
- recover from ordinary mistakes;
- learn to show evidence when asking for help.

### Computer Science II

- AI-assisted coding inside bounded branches;
- pull requests;
- tests and code review;
- multiple contributors and agents;
- repository as the durable project record.

### DSCT

- distinguish evidence from interpretation;
- use diffs and history to support claims;
- state what a receipt proves and what it cannot prove;
- reason about provenance and reproducibility.

### Computer Architecture

- connect source version to build/runtime/machine evidence;
- compare behavior across environments without losing provenance.

### Software Engineering / Machine Learning

- team workflows;
- CI and review gates;
- release history;
- experiment provenance;
- model/data/code version relationships;
- automated agents constrained by repository policy.

## Minimal command spine

Students do not need fifty Git commands in their heads. These are enough to build the first durable workflow:

```bash
git status --short --branch
git diff
git diff --staged
git diff --stat
git diff --check
git log --oneline --decorate -5
git branch --show-current
git switch -c <branch>
git add <specific-file>
git commit -m "message"
git push
git restore <file>
git revert <commit>
```

Add `git clone` and repository-specific authentication/setup at the entry point where needed.

## Instructor quality gate

Before a page is considered ready for production Canvas use, verify that:

- the example works on the intended student environment;
- the activity is bounded;
- the recovery path is known;
- the student can independently verify success;
- the receipt is small enough to inspect;
- the lesson teaches a durable idea rather than a brittle UI sequence;
- no step encourages students to paste credentials into chat or commit them to Git;
- AI use is framed as delegated work inside a human-owned verification loop.
