# 01 — Git, GitHub, Repositories, Commits, Branches, and Remotes

This lesson builds the mental map for the rest of Git Week.

Do not memorize definitions in isolation. Use the real practice repository:

`jeremy-evert/git-safety-belt-lab`

The goal is to understand **where the work lives, what Git records, and what GitHub adds**.

## The picture first

Start with this model:

```text
GITHUB
jeremy-evert/git-safety-belt-lab
        │
        │  remote repository
        │
        ├── main
        │    │
        │    └── c8e294b  Use python3 for Linux verification
        │         │
        │         └── 7d12da5  Document the verification workflow
        │              │
        │              └── 44f559b  Add verification tests
        │                   │
        │                   └── 44305f2  Add tiny trail mix calculator
        │                        │
        │                        └── 4dda6ff  Initialize Git Safety Belt Lab
        │
        │ clone / fetch / pull / push
        ↓
LOCAL COMPUTER
...
/git-safety-belt-lab/
        │
        ├── working tree
        │    ├── README.md
        │    ├── VERIFY.md
        │    ├── trail_mix.py
        │    └── tests/
        │
        ├── local branch: main
        │
        ├── local Git history
        │
        └── remote name: origin
             └── points back to GitHub
```

Almost everything we do this week fits somewhere in that picture.

---

## Git is not GitHub

### Git

Git is the version-control system.

It can operate locally on your computer.

Git tracks project state and history inside a repository.

Useful Git questions include:

- What repository am I in?
- What branch am I on?
- What changed?
- What did the project look like before?
- What commits exist?
- Can I recover a known state?

### GitHub

GitHub is a service that hosts Git repositories and adds collaboration features.

GitHub gives us things such as:

- remote repositories;
- forks;
- pull requests;
- code review;
- issues;
- automated checks;
- shared project visibility.

A useful sentence to remember:

> **Git manages history. GitHub helps people share and collaborate around that history.**

---

## Repository

A repository is the project plus the Git information needed to understand its state and history.

In the Safety Belt Lab, the visible project currently contains:

```text
README.md
VERIFY.md
trail_mix.py
tests/
```

But the repository is more than those visible files.

Git also maintains history and metadata behind the scenes.

When you clone the repository, you do not merely download four current files. You also receive the Git history needed to inspect how the project reached the current state.

That is why, immediately after cloning, a student can run:

```bash
git log --oneline --decorate -6
```

and see multiple earlier states.

---

## Working tree

The **working tree** is the version of the project you can currently see and edit.

If you open `trail_mix.py` in an editor and change one line, you have changed the working tree.

You have **not automatically changed Git history**.

This distinction matters:

```text
edit file
   ≠
commit change
```

Saving changes the file.

Committing asks Git to preserve a new project state in history.

---

## Commit

A commit is a preserved project snapshot with metadata and a connection to earlier history.

The Safety Belt Lab was deliberately built with readable commits:

```text
4dda6ff  Initialize Git Safety Belt Lab
44305f2  Add tiny trail mix calculator
44f559b  Add verification tests
7d12da5  Document the verification workflow
c8e294b  Use python3 for Linux verification
```

Notice that the commit messages tell a story.

The fifth commit is especially useful.

The original verification instructions assumed the command `python` existed. A real test on Maise showed that the environment exposed Python 3 as `python3` instead.

We did not pretend the earlier assumption never happened.

We corrected the documentation and preserved the correction as another commit.

That is one of Git's strengths:

> **History can record learning, not just success.**

---

## Commit IDs

Every commit has an identifier.

For example:

```text
c8e294b
```

That short value is an abbreviated form of the full Git commit hash.

You do not need to memorize it.

You use it when you need to refer precisely to a particular state in history.

A sentence such as:

> "The tests passed at commit `c8e294b`."

is more precise than:

> "The tests worked earlier."

Git gives conversations anchors.

---

## Branch

A branch is a named line of development.

The starter repository currently uses:

```text
main
```

Think of `main` as a movable label pointing at the latest commit on that line of work.

Right now:

```text
main
 ↓
c8e294b
 ↓
7d12da5
 ↓
44f559b
 ↓
44305f2
 ↓
4dda6ff
```

When we later create another branch, we will create another line where work can happen without immediately changing `main`.

That is useful for:

- experiments;
- human-authored features;
- AI-assisted changes;
- fixes;
- pull-request review.

For now, the important idea is simple:

> **A branch tells Git which line of work you are currently advancing.**

---

## HEAD

`HEAD` answers a practical question:

**Where am I currently positioned in Git history?**

After the verified Maise pull, the history showed:

```text
c8e294b (HEAD -> main, origin/main, origin/HEAD) Use python3 for Linux verification
```

Read that slowly:

```text
HEAD -> main
```

means the local working position is on the `main` branch.

```text
origin/main
```

means the local record of the remote `main` branch points at the same commit.

At that moment, local and remote agree.

---

## Remote

A remote is another Git repository location known to your local repository.

When the Safety Belt Lab is cloned from GitHub, Git creates a conventional remote name:

```text
origin
```

On Maise:

```text
origin  git@github.com:jeremy-evert/git-safety-belt-lab.git (fetch)
origin  git@github.com:jeremy-evert/git-safety-belt-lab.git (push)
```

`origin` is not a special server and not a required GitHub word.

It is simply the conventional name Git gives the repository you cloned from.

A useful mental translation is:

```text
origin
=
"the remote repository this local copy originally came from"
```

---

## Clone

`git clone` creates a local repository from an existing repository.

For the Safety Belt Lab:

```bash
git clone git@github.com:jeremy-evert/git-safety-belt-lab.git
```

Clone gives you:

- the current project files;
- the Git history;
- a local branch;
- a configured remote named `origin`.

That is much richer than downloading a ZIP archive.

A ZIP gives you files.

A clone gives you files **plus the repository's history and relationships**.

---

## Fetch, pull, and push

We will practice these later, but place them on the map now.

### Fetch

```text
GitHub → local Git knowledge
```

Fetch learns about remote changes without automatically changing your working tree.

### Pull

```text
GitHub → local repository → working state catches up
```

During Student Zero, Maise began at:

```text
7d12da5
```

GitHub had advanced to:

```text
c8e294b
```

A `git pull` produced a clean fast-forward and brought Maise to the new commit.

### Push

```text
local commits → GitHub
```

Push publishes commits from the local repository to a remote branch when you have permission.

A useful warning:

> **Commit is not push. Push is not proof.**

A commit preserves a local state.

A push publishes commits.

Neither operation proves the program is correct.

---

## Fork

A fork is a GitHub-hosted copy of another repository under a different GitHub account or organization.

For this lab, students will eventually fork:

```text
jeremy-evert/git-safety-belt-lab
```

into something like:

```text
student-name/git-safety-belt-lab
```

That gives each student a public practice space where they can:

- create branches;
- push commits;
- break things;
- recover;
- create pull requests;

without modifying the instructor's upstream repository.

We are **not forking yet** in this lesson.

First understand the map.

Then operate the machine.

---

## One important distinction

After cloning, there can be several related but different ideas in one line:

```text
c8e294b (HEAD -> main, origin/main, origin/HEAD)
```

They happened to agree during the successful Maise verification.

That does not mean they must always agree.

A local branch can move ahead after a local commit.

A remote branch can move ahead when another person pushes.

Git's job is partly to make those relationships inspectable rather than mysterious.

---

## The mental model checkpoint

Before moving to 02, a student should be able to explain this picture:

```text
EDIT
  ↓
WORKING TREE
  ↓
COMMIT
  ↓
LOCAL GIT HISTORY
  ↓
PUSH
  ↓
REMOTE GIT HISTORY ON GITHUB
```

and this return path:

```text
GITHUB CHANGES
  ↓
FETCH / PULL
  ↓
LOCAL GIT KNOWLEDGE / STATE
```

## Five statements worth remembering

1. **Git is not GitHub.**
2. **Saving a file is not committing it.**
3. **Committing is not pushing.**
4. **A clone includes history, not just current files.**
5. **A successful commit or push does not prove the program is correct.**

---

## Completion signal

Without looking back, explain the difference among these five things:

```text
working tree
commit
branch
remote
GitHub
```

Then answer:

> **Why can `HEAD`, `main`, and `origin/main` point to the same commit at one moment but differ later?**

If you can explain that idea conceptually, you are ready for:

**02 — Try It: Open a Repo and Run the Git Preflight**
