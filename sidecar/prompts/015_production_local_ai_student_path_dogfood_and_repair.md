# Prompt 015 — Production Local AI student path dogfood and repair

Owner: Jeremy
Foreman: Flo
Priority: **URGENT / CLASSROOM DELIVERY**
Execution host: April, with other already-proven seats used only when needed for student-view/browser validation
Owning repository: `jeremy-evert/computing_commons`
Production target: `https://swosu.instructure.com/courses/24298`

## Outcome

Make **Setting Up Your AI Lab / Build and Verify Your Local AI Lab** actually work as one obvious student path in the live Computing Commons.

A student should be able to begin in course 24298 and succeed by following this grammar at every step:

```text
GO HERE
DO THIS
LOOK FOR THIS
IF NOT, DO THIS
```

This is a production dogfood-and-repair mission, not another speculative curriculum-writing pass.

## Owner acceptance target

Jeremy now has a human-facing quick-start guide titled:

`Setting Up Your AI Lab — Student Quick Start`

Its required student path is reproduced below so completion does not depend on Google Drive access.

The durable canonical technical source remains `jeremy-evert/local_ai_lab_setup`. The Commons should stitch that accepted source into one production student road, not fork a competing setup procedure.

## Required student road

### Step 0 — Find the actual starting point

From the live Computing Commons, a student must be able to find **Week 2 / Build and Verify Your Local AI Lab** and reach the supplied Local AI / Windows classroom practice package without guessing.

Success:
- the starting page is obvious;
- the package/download/access path is explicit;
- the student knows where to open PowerShell;
- no repository filenames, instructor-only routes, or developer plumbing leak into the student experience.

### Step 1 — Inventory

Canonical command:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\verify_local_ai.ps1 Inventory
```

Expected evidence: items labeled `FOUND`, `MISSING`, or `NOT CHECKED`.

### Step 2 — Verify Windows foundation

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\verify_local_ai.ps1 Foundation
```

Expected evidence:

```text
FOUNDATION: PASS
```

### Step 3 — Verify Ollama

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\verify_local_ai.ps1 Ollama
```

Expected evidence:

```text
OLLAMA: PASS
```

The accepted service remains loopback-only at `127.0.0.1:11434` unless the canonical source has been deliberately changed by the Owner.

### Step 4 — Verify approved model

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\verify_local_ai.ps1 Model
```

Expected evidence:

```text
MODEL: PASS
```

The approved model is `qwen3:8b` unless the canonical source has been deliberately changed by the Owner.

### Step 5 — Prove local inference

```powershell
python scripts\hello_ollama.py
```

Expected evidence:

```text
HELLO_OLLAMA: PASS
```

plus a short local-model response.

### Step 6 — Verify Aider

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\verify_local_ai.ps1 Aider
```

Expected evidence:

```text
AIDER: PASS
```

A cloud-provider/API-key detour is a failure of this student path.

### Step 7 — Prepare the tiny disposable Git project

Canonical supplied example: `examples\aider_hello`.

The student needs a clean local Git starting state. No GitHub remote is required for the exercise.

### Step 8 — Make one bounded Aider change

Launch through the canonical wrapper:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts\launch_aider.ps1
```

Bounded request:

```text
Change display_label so it returns title-cased text; do not edit tests.
```

Expected behavior: Aider uses the approved local model and changes only the intended example source.

### Step 9 — Inspect the diff

```powershell
git -C examples\aider_hello diff
```

Expected core change: `.upper()` becomes `.title()` in the intended source. Tests are not edited.

### Step 10 — Verify independently

```powershell
python -m unittest discover -s examples\aider_hello\tests -v
```

Expected evidence: tests pass.

## Final student proof

A successful student can show all four:

1. `HELLO_OLLAMA: PASS`;
2. `AIDER: PASS` plus a bounded Aider edit;
3. a small Git diff they understand;
4. an independent test that passes.

The habit taught is:

```text
Know the starting state
-> ask for one bounded change
-> inspect the evidence
-> test independently
-> accept, repair, or recover
```

## Mission chain

```text
PRODUCTION RECON
-> STUDENT-ENTRY WALKTHROUGH
-> PACKAGE/DOWNLOAD PROOF
-> COMMAND-BY-COMMAND DOGFOOD
-> BREAKPOINT LEDGER
-> REPAIR SOURCE/COMMONS/DEPLOYMENT SEAMS
-> REDEPLOY BOUNDED PRODUCTION SURFACE
-> STUDENT-VIEW READBACK
-> COMPLETE END-TO-END REPLAY
-> INSTRUCTOR QUICK ROUTE
-> FINAL RECEIPT
```

## Recon

Before mutation:

1. Read `AGENTS.md` and only the relevant current sidecar evidence.
2. Read `curriculum/local-ai-lab.md`.
3. Read Prompt 005 for the accepted instructional intent, but do not inherit its old Savnac-only production prohibition; this Prompt 015 explicitly authorizes the bounded production work below.
4. Read the canonical `jeremy-evert/local_ai_lab_setup` Week 2 package and current accepted Windows evidence in `jeremy-evert/windows_classroom`.
5. Inspect live course 24298 object structure and current student-facing links/pages/modules/files relevant to the Local AI Lab.
6. Protect pre-existing repository work and record current source SHA before edits.

Do not ask Jeremy to reconstruct state that can be read from Git, Canvas, local files, or the active environment.

## Dogfood rule

Do not merely inspect source and declare the path plausible. **Execute the student journey.**

At each step record:

```text
where the student starts
what the student is told to do
what exact artifact/command they receive
what success should look like
what actually happens
PASS | REPAIR | HUMAN_DECISION
```

Use the real student-facing production path wherever safe. Use an already-proven student-view/test-user/browser method for visual/access validation when available.

## Repair authority

Flo may repair the smallest necessary seams in:

- `jeremy-evert/computing_commons`;
- bounded production course 24298 pages/modules/files/links/0-point completion objects relevant to this Local AI Lab path;
- deployment scripts/configuration in `computing_commons` needed to make those exact artifacts durable and repeatable.

Flo may inspect `local_ai_lab_setup` and `windows_classroom` as canonical/reference truth. Do **not** silently fork or rewrite their accepted technical contract inside Commons.

If the canonical source itself is demonstrably broken or internally inconsistent, produce a precise source-boundary defect and either repair it only if its repository instructions and current mission authority clearly permit that change, or yield one narrow HUMAN DECISION. Do not paper over a canonical defect with a contradictory Commons-only workaround.

## Production mutation boundary

Authorized production mutation target is exact Canvas course `24298` only, and only the Local AI Lab student path required by this mission.

Do not:

- alter grades;
- enroll/remove users;
- change unrelated Commons curriculum;
- change other courses;
- expose instructor/development controls to students;
- add cloud AI keys/providers as a fallback;
- weaken local-only/network safety boundaries;
- make destructive cleanup unrelated to this path.

## Broken-path priority

Treat these as blocking defects, not documentation polish:

- no obvious starting link;
- inaccessible/missing student package;
- instructions point to files students do not receive;
- command/path mismatch;
- PowerShell opens in the wrong place with no recovery instruction;
- scripts missing from the package;
- Ollama/model/Aider config contradicts canonical source;
- Aider asks for a cloud provider/key;
- Git exercise starts dirty or targets the wrong directory;
- expected diff is not bounded;
- independent test command does not run;
- Next/Back navigation strands the student;
- recovery text tells students to improvise system repair rather than stop with evidence;
- teacher-only/developer material leaks into the student route.

## Instructor route

Leave behind one short instructor-facing path in `computing_commons`, preferably under `instructor/`, using the same grammar:

```text
GO HERE
DO THIS
LOOK FOR THIS
IF NOT
```

It should be short enough to teach from live. Do not replace the student experience with a giant instructor manual.

## Verification

Completion requires more than successful deployment API responses.

Prove:

- live object/readback state;
- all student-facing links resolve;
- required package/artifacts are reachable with student-appropriate access;
- exact commands match the supplied files;
- the local workflow succeeds end to end on an accepted/proven Windows path;
- bounded Aider change produces the intended diff;
- independent test passes;
- student-view navigation is coherent;
- no unrelated course state changed.

Repair and replay from Step 0 after any substantive production fix.

## Priority relative to other April work

This mission is **higher priority than video transcription mechanics, Zoom-pipe refinement, and course deduplication cleanup** because students need a working Week 2 path now.

Do not destroy or lose progress on those lower-priority jobs. Park them durably and resume after this mission reaches acceptance or a real human gate.

## Real human gates only

Yield only for:

- a genuinely consequential choice between incompatible canonical source truths;
- missing credential/permission that cannot be resolved from the existing authenticated environment;
- destructive production content not created/owned by this system whose replacement requires Owner approval;
- unresolved student access topology;
- a required physical action;
- scope expansion outside course 24298 / the Local AI path.

Routine recon, Canvas reads, bounded deployment, local dogfooding, source repair inside authorized scope, link checking, command execution, verification, and evidence publication belong to Flo.

## Durable evidence

Publish a concise report under `sidecar/reports/flo/` containing:

- source commit(s);
- live production object identifiers/paths touched;
- student-path breakpoint ledger;
- repairs performed;
- end-to-end replay result;
- remaining real gates, if any;
- confirmation grades/enrollments/unrelated courses were untouched.

## Acceptance

Do not claim completion until a student can reasonably follow the live production route from Commons entry to independent passing test using the explicit `GO HERE -> DO THIS -> LOOK FOR THIS -> IF NOT` pattern, without Jeremy acting as the missing documentation layer.

Final sentinel:

```text
COMPUTING COMMONS LOCAL AI STUDENT PATH WORKS.
```
