# Git Safety Belt Lab — Practice Repository Build Plan

Proposed public repository:

```text
jeremy-evert/git-safety-belt-lab
```

The practice repository is deliberately separate from `computing_commons`.

- `computing_commons` owns the teaching.
- `git-safety-belt-lab` owns the tiny project students inspect, fork, change, break, verify, and recover.

## Why public?

This particular repository should contain no secrets, student data, grades, proprietary code, or answer keys.

Public visibility gives us:

- frictionless cloning;
- frictionless forking;
- a stable upstream everyone can inspect;
- preserved starter commit history in student forks;
- easy links from Canvas;
- a realistic GitHub collaboration surface.

Students should **not** receive write permission to the upstream repository for the normal exercise.

The default workflow is:

```text
public upstream
     ↓ fork
student-owned fork
     ↓ branch
student bounded change
     ↓ inspect + verify
student commit
     ↓
optional PR inside the student's fork
```

This keeps the canonical lab clean and avoids a pile of class-wide practice branches and pull requests in the upstream repository.

## Why fork instead of GitHub template?

For this lesson, preserving history is a feature.

A fork carries the upstream commit history with it. Students can inspect the exact same baseline history and then add their own work on top.

A template repository is useful for many assignments, but a newly generated repository does not give us the same inherited Git history story.

## Repository design principle

The code should be almost boring.

The Git behavior is the curriculum.

Students should not lose the source-management lesson because they are debugging complicated domain logic.

## Proposed tiny project

Use Python because it is readable, already familiar in the broader computing sequence, and easy to verify with no external dependencies.

```text
git-safety-belt-lab/
├── README.md
├── .gitignore
├── src/
│   └── trail_mix.py
├── tests/
│   └── test_trail_mix.py
└── receipts/
    └── README.md
```

The project can expose a tiny function such as:

```python
def total_items(pretzels: int, raisins: int, chocolate: int) -> int:
    return pretzels + raisins + chocolate
```

The point is not trail mix. The point is that everyone can understand the behavior almost instantly.

## Intentional starter history

Do not create the repository as one giant first commit.

Build this history deliberately.

### Commit 1

```text
Initialize Git Safety Belt Lab
```

Add:

- `README.md`
- `.gitignore`

Purpose: students can see the repository begin.

### Commit 2

```text
Add tiny trail mix calculator
```

Add:

- `src/trail_mix.py`

Purpose: students can inspect a source-adding commit.

### Commit 3

```text
Add verification tests
```

Add:

- `tests/test_trail_mix.py`

Use Python's standard-library `unittest` so the lab has no package-install dependency.

Verification command:

```bash
python -m unittest discover -s tests -v
```

Purpose: establish an independently verifiable green baseline.

### Commit 4

```text
Document the verification workflow
```

Update `README.md` and add `receipts/README.md`.

Purpose: students see documentation evolve separately from source behavior.

## Green baseline requirement

Before students ever see the repository:

```bash
python -m unittest discover -s tests -v
git status --short --branch
git log --oneline --decorate -5
```

must show:

- passing tests;
- a clean working tree;
- an understandable starter history.

## Planned use through Git Week

### 00 — Start Here

No repository interaction required.

Students learn why Git matters.

### 01 — Mental model

Use the public repository visually to distinguish:

- GitHub repository;
- local clone;
- working tree;
- commit history;
- branch;
- remote.

### 02 — Preflight

Students fork, clone their fork, and prove:

```text
repository root
branch
HEAD
remote(s)
working-tree state
recent history
```

### 04 — Tiny human change

Student makes an intentionally simple change, such as adding a fourth ingredient to a text summary or improving a message.

They inspect, verify, stage, inspect again, and commit.

### 06 — Bounded AI change

AI receives one narrowly scoped change with an acceptance condition.

Example:

> Add a `total_weight` function to `src/trail_mix.py`. Do not change existing behavior. Add tests for the new function. Use only the Python standard library. Stop after making the requested source and test changes.

Student owns inspection and verification.

### 08 — Failure and recovery

Student deliberately changes one known-good expression so a test fails, captures evidence, and restores the intended state.

The initial recovery can use an uncommitted change so `git restore <file>` is sufficient and safe.

Later material can introduce `git revert` for a committed/shared mistake.

## Repository rules

The upstream lab should remain:

- tiny;
- green on `main`;
- dependency-free;
- free of secrets;
- free of student work;
- free of hidden answer keys;
- easy to reset by recloning/reforking;
- understandable in under five minutes.

## Creation settings

When creating the repository on GitHub:

```text
Owner: jeremy-evert
Repository name: git-safety-belt-lab
Visibility: Public
Initialize with README: No
Add .gitignore: No
Choose a license: No during creation
```

Start it empty so we can create the intentional four-commit history ourselves rather than inherit a GitHub-generated bootstrap commit.

A license can be added intentionally in the first commit if desired.

## Definition of ready

The repository is ready for Student Zero when:

- all four baseline commits exist;
- tests pass with stock Python;
- clone/fork instructions are accurate;
- no authentication secret is required to run the project;
- the baseline diff/history is small enough to explain on screen;
- recovery has been tested from a fresh clone;
- the full 02 → 04 → 06 → 08 pathway has been performed once by the instructor.
