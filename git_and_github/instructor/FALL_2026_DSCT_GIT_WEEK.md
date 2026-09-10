# Fall 2026 DSCT Git Week

Home course: Discrete Structures & Critical Thinking

Shared source: [`../README.md`](../README.md)

Canvas delivery source: [`../curriculum/README.md`](../curriculum/README.md)

Dates: **Tuesday, September 15, 2026** and **Thursday, September 17, 2026**

## Home-course question

The Computing Commons teaches the Git craft.

DSCT adds the reasoning lens:

> **What does this Git history actually prove, and what does it not prove?**

Students should leave the week more willing to use Git, but also less willing to confuse a clean commit history with proof that a program, claim, or AI-generated change is correct.

## Week outcome

By the end of the week, a student should be able to make or delegate a bounded change, inspect the evidence Git provides, verify the resulting behavior independently, recover from a small failure, and state the limits of the evidence.

## Tuesday, September 15: History as Evidence

### Before class / Canvas runway

Students complete or review:

```text
00 — Start Here: Git Is the Safety Belt
01 — Video: Git, GitHub, Repositories, Commits, Branches, and Remotes
02 — Try It: Open a Repo and Run the Git Preflight
03 — Video: Status and Diff Are the Truth
```

### In-class question

**If I have a commit, what do I actually know?**

Build the distinction explicitly:

```text
Git can provide evidence that:
- a particular snapshot exists;
- particular files differ from another snapshot;
- a commit has particular metadata;
- a branch currently points somewhere;
- a remote received a commit.

Git alone does NOT prove that:
- the program is correct;
- the author understood the code;
- the AI's explanation is accurate;
- tests are sufficient;
- the experiment was well designed;
- the result means what the student claims it means.
```

### In-class lab

Use the shared practice repository.

Students:

1. run the Git preflight;
2. record the starting commit;
3. make one tiny human-authored change;
4. inspect `git diff`;
5. run the provided verification;
6. stage only the intended file(s);
7. inspect `git diff --staged`;
8. commit;
9. compare what Git proves with what the verification proves.

### Tuesday exit receipt

Three claims:

1. **What changed?** Support with Git evidence.
2. **What worked?** Support with independent verification.
3. **What do these artifacts still not prove?** State one meaningful limitation.

## Between Tuesday and Thursday

Students complete or review:

```text
04 — Try It: Make One Tiny Human Change and Preserve It
05 — Video: AI at the Keyboard, Human on the Commit
```

The point is not to reward AI use by volume. The goal is to establish a bounded, inspectable delegation loop.

## Thursday, September 17: AI as a Fast, Fallible Contributor

### Opening question

**If an AI tool can edit twenty files in thirty seconds, what must the human do differently?**

Desired answer: the human does not need to type faster. The human needs a stronger boundary, a cleaner starting state, better inspection, and independent verification.

### In-class lab

Students:

1. prove the working tree state;
2. create a descriptive branch;
3. record starting `HEAD`;
4. give an approved AI tool one bounded change;
5. inspect `git status`, `git diff --stat`, and the actual diff;
6. stop and investigate if scope expanded unexpectedly;
7. run the project verification;
8. stage only intended files;
9. inspect the staged diff;
10. commit only after they are willing to own the change.

### Controlled failure and recovery

Introduce one small failure after a known good state.

Students must:

- capture the failure;
- identify the relevant diff/state;
- recover using the assigned safe technique;
- rerun the verification;
- prove the intended state was restored.

### Thursday exit receipt

Use [`../templates/GIT_EVIDENCE_RECEIPT.md`](../templates/GIT_EVIDENCE_RECEIPT.md).

The most important DSCT field is:

> **What does this evidence NOT prove?**

A student who can answer that well is reasoning rather than merely operating tools.

## Recommended Canvas sequence for the week

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

For the soft launch, not every video has to exist before Tuesday. The minimum viable slice is 00 through 06 plus the receipt. Recovery and repository hygiene can be taught live and promoted to polished video/pages after the student pathway is proven.

## Shared versus DSCT ownership

### Computing Commons owns

- Git/GitHub mental model;
- command spine;
- repository preflight;
- status/diff/history inspection;
- branching basics;
- AI-assisted change protocol;
- safe recovery basics;
- repository hygiene;
- shared evidence receipt format.

### DSCT owns

- evidence versus claim;
- limitations;
- observation versus interpretation;
- whether verification is sufficient;
- what provenance can and cannot justify;
- course-specific reasoning prompts and grading.

Do not fork the generic Git lesson into DSCT. Link back to the Commons and let DSCT spend its time on reasoning.

## Instructor success test

Git Week succeeds if students stop saying only:

> "It works."

and begin naturally saying something closer to:

> "Here is the commit. Here is the diff. Here is the verification I ran. Here is what those artifacts support, and here is what they still do not prove."
