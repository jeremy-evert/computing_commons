# Build and Verify Your Local AI Lab

## Commons role

The Commons is the student-facing clearinghouse for the Local AI Lab. It does **not** own a third independent implementation.

## Canonical sources

### Instructional product

`jeremy-evert/local_ai_lab_setup`

Current source responsibilities include:

- approachable shared Week 2 curriculum;
- PowerShell, Python, Git, Ollama, Aider, and local-model explanations;
- readiness/evidence distinctions;
- bounded exercises;
- instructor support and troubleshooting guidance.

Current approved local model in that source is `qwen3:8b`.

### Windows implementation evidence

`jeremy-evert/windows_classroom`

Current source responsibilities include:

- measured restricted-Windows capability;
- reviewed classroom/student Windows layer;
- student guide and instructor runbook;
- experimental evidence used to determine what the student path may safely promise.

## Commons composition

The intended student journey should present one path:

1. understand what the tools are;
2. inventory what is present;
3. distinguish installed/present from actually working;
4. verify the Windows foundation where applicable;
5. verify Ollama;
6. verify the approved model;
7. run direct local inference;
8. establish the approved Aider workflow;
9. create/use a tiny Git worktree;
10. make a bounded AI-assisted change;
11. independently verify what changed and whether it works.

For the Aider portion, use the dedicated student guide:
[`week2/aider-work-first.md`](week2/aider-work-first.md). It explains the
local-only boundary, the one-change request, the diff inspection, and the
independent test without creating a second Local AI setup procedure.

The exact student sequence should be reconciled to the accepted current `local_ai_lab_setup` package rather than rewritten from memory here.

## Evidence principle

Different checks prove different things:

- executable found ≠ usable tool;
- API reachable ≠ model inference works;
- model listed ≠ model can answer;
- Aider launched ≠ code change is correct;
- AI changed a file ≠ the student has verified the result.

## Course wrappers

Home courses should apply the capability rather than duplicate setup.

Examples:

- CS1: use the working lab for a tiny Python edit/test/explanation.
- CS2: use it in a more intentional coding workflow.
- DSCT: use it to investigate a reasoning claim and independently verify evidence.
- Architecture: use it as an investigation aid while inspecting machine evidence.
- Software Engineering: use it inside a bounded engineering/change workflow.
- Machine Learning: use it with deeper model/evaluation understanding.

## Fall 2026 delivery posture

Initial Commons delivery may use a 0-point completion/evidence assignment with a due date. Strong evidence may earn home-course bonus credit while the grading seam is still being tested.

## Current status

**SOURCE-BOUND / COMMONS DELIVERY TO BE BUILT AND TESTED.**

Do not claim final Windows or student-artifact readiness merely because these canonical repositories exist. Use their accepted evidence gates.
