# Student Zero Verification — Maise — 2026-09-11

This note records the first clean end-to-end verification of the public Git Safety Belt Lab on Maise.

Practice repository:

`jeremy-evert/git-safety-belt-lab`

## Clone and Git preflight

Observed repository state after clone:

```text
/home/jevert/git/git-safety-belt-lab
/mnt/nora/git/git-safety-belt-lab
## main...origin/main
origin  git@github.com:jeremy-evert/git-safety-belt-lab.git (fetch)
origin  git@github.com:jeremy-evert/git-safety-belt-lab.git (push)
main
7d12da5
```

Initial history:

```text
7d12da5 Document the verification workflow
44f559b Add verification tests
44305f2 Add tiny trail mix calculator
4dda6ff Initialize Git Safety Belt Lab
```

## First useful failure

The first verification instructions used `python`, but Maise exposes Python 3 as `python3`.

Observed evidence:

```text
Command 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
```

Interpretation:

- Git had not failed.
- The repository had not failed.
- An environment assumption had been exposed.
- The correction should be preserved as a new commit rather than hidden by rewriting history.

The lab documentation was corrected in commit:

```text
c8e294b Use python3 for Linux verification
```

## Pull and verification

Maise then pulled the correction with a clean fast-forward:

```text
Updating 7d12da5..c8e294b
Fast-forward
VERIFY.md | 44 ++++++++++++++++++++++++++++++++++++++++++--
1 file changed, 42 insertions(+), 2 deletions(-)
```

Python environment:

```text
Python 3.14.4
```

Program verification:

```text
Trail mix pieces: 30
Complete servings of 5: 6
```

Test verification:

```text
test_serving_size_must_be_positive ... ok
test_servings_possible ... ok
test_total_items ... ok

Ran 3 tests in 0.000s

OK
```

Final Git state:

```text
## main...origin/main
c8e294b (HEAD -> main, origin/main, origin/HEAD) Use python3 for Linux verification
7d12da5 Document the verification workflow
44f559b Add verification tests
44305f2 Add tiny trail mix calculator
4dda6ff Initialize Git Safety Belt Lab
```

This verifies that the final working tree is clean and local `main`, `origin/main`, and `origin/HEAD` agree on the current commit.

## Path observation

The shell presents the repository through:

```text
/home/jevert/git/git-safety-belt-lab
```

while physical path resolution reports:

```text
/mnt/nora/git/git-safety-belt-lab
```

Confirmed with:

```text
pwd
/home/jevert/git/git-safety-belt-lab

pwd -P
/mnt/nora/git/git-safety-belt-lab

readlink -f .
/mnt/nora/git/git-safety-belt-lab
```

Interpretation: the friendly home-directory path resolves through the filesystem to `/mnt/nora/git`. This is not a Git failure. It is an instructor-only example of two valid descriptions of the same location.

Do not make this path-resolution detail part of the foundational student lesson unless it appears in a student environment and needs explanation.

## Curriculum findings

Student Zero validated several teaching decisions:

1. **Failure is data.** The first failed Python command exposed an assumption rather than invalidating the workflow.
2. **Preserve corrections in history.** The `python3` correction became a new commit instead of rewriting the earlier instructional history.
3. **Git and runtime evidence are different.** Git proved repository state; Python execution and unit tests provided behavioral evidence.
4. **A clean final status matters.** The workflow ends with a known repository state, not merely a successful command.
5. **Environment preflight belongs before behavioral verification.** Future student instructions should confirm the Python 3 launcher before invoking the test suite.

## Release status

The public starter pathway is now verified on Maise through:

```text
clone
→ inspect repository state
→ pull a fast-forward correction
→ confirm Python 3
→ run program
→ run 3 unit tests
→ confirm clean final Git state
```

This is sufficient evidence to continue building the 01 mental-model lesson and the 02 Git preflight activity around the real repository.
