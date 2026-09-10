# Git Evidence Receipt

Name:

Course / section:

Date:

## 1. Repository identity

Repository:

Branch:

Starting commit:

```text
Paste the relevant output from:
git status --short --branch
git rev-parse --short HEAD
```

## 2. Bounded task

In one or two sentences, what were you trying to change?

What files or behavior were intended to be in scope?

What was explicitly out of scope, if anything?

## 3. What actually changed?

```text
Paste:
git diff --stat
```

Summarize the important source changes in your own words.

If AI assisted with the change, compare what the AI claimed it changed with what Git actually shows.

## 4. Verification

Verification command or procedure:

```text
Paste the command and the relevant result.
```

Did the verification pass?

What does this verification actually check?

## 5. Preserved state

Final commit:

```text
Paste:
git log -1 --oneline
git status --short --branch
```

GitHub commit or pull-request location, when available:

## 6. Claim supported by the evidence

Write one precise claim that the Git evidence plus the independent verification support.

## 7. Limitation

**What does this evidence NOT prove?**

Name at least one important limitation. Examples might include untested inputs, performance, security, correctness beyond the tested behavior, authorship/understanding, environmental differences, or assumptions not examined by this work.

## 8. Recovery evidence, when assigned

Starting good state:

Failure introduced or observed:

Failure evidence:

Recovery action:

Verification after recovery:

Final repository state:

## Compact receipt checklist

- [ ] I knew the repository and branch before changing anything.
- [ ] I recorded the starting commit.
- [ ] I inspected the actual diff.
- [ ] I checked for unintended files or scope expansion.
- [ ] I ran an independent verification step.
- [ ] I staged only what I intended to commit.
- [ ] I can explain the change in my own words.
- [ ] I recorded the final commit and repository state.
- [ ] I stated what my evidence supports.
- [ ] I stated at least one thing my evidence does not prove.
