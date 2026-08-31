# Mission 022 — model crossover report

## Scope and validity

Mission 021's repaired apparatus was carried forward: the same green budget fixture, controller-side hashed MICRO/SMALL oracles, Aider 0.86.2, `ollama_chat/...`, whole edit format, file-backed prompts, CPU-only host, and exact-model warm before each timed loop. Mission 021 historical results are not pooled with this run.

The contemporary 3B control was partially completed. One MICRO attempt completed (oracle miss, regression pass, 76.710 s); a second and later retry reproduced the model-generated `path/to/...` transport failure and were preserved under `invalid_attempts`; the full contemporary 3B 3+3 matrix therefore remains incomplete. Worker B completed all six planned attempts.

## Results

| condition | rung | completed repetitions | engineering/oracle success | regression | warm wall seconds | scope drift |
|---|---|---:|---:|---:|---|---|
| contemporary Worker A, 3B | MICRO | 1 scored + invalid transport attempts preserved | 0/1 scored | 1/1 | 76.710 | 1 malformed-path completed attempt; subsequent retry interrupted |
| historical Mission 021 Worker A, 3B | MICRO | 3 | 1/3 | 3/3 | 77.658–137.641 | recorded in 021 |
| historical Mission 021 Worker A, 3B | SMALL | 3 | 0/3 | 3/3 | 133.935–135.264 | recorded in 021 |
| Worker B, 7B CPU | MICRO | 3 | 1/3 | 3/3 | 141.949–154.359 | no unexpected path in completed receipts; 2 oracle misses had no target diff |
| Worker B, 7B CPU | SMALL | 3 | 0/3 | 3/3 | 150.146–169.742 | no unexpected path in completed receipts; no oracle successes |

The Worker B success was the first MICRO attempt. Worker B therefore did not improve the observed MICRO rate over the historical 3B control and did not rescue SMALL. Its median warm loop was approximately 154 s for MICRO and 150 s for SMALL, versus approximately 80–135 s for the historical 3B ladder. Time to first useful visible feedback was not reliably separable from Aider/model startup in these non-timestamped logs; the complete Aider transcript is retained per attempt.

## Evidence/accounting limitation

Although the caller requested `--no-auto-commits`, Aider staged some target edits. The harness captured `git diff -- target` rather than `git diff HEAD -- target`, so several raw `git_diff.patch` files are empty even when `status.log` says `AM`. This is a reporting/instrumentation defect, not proof that no model edit occurred. Raw stdout, status, proofs, and the staged final state remain available. The baseline restore was performed after each attempt, and final cleanup will remove staged/worktree fixture edits. Future runs must capture both staged and unstaged diffs and must assert no forbidden staged path before acceptance.

## Three verdicts

### ENGINEERING SUCCESS

Worker B: MICRO 1/3; SMALL 0/3. Worker A contemporary control: 0/1 completed scored MICRO, with additional invalid transport attempts. All completed attempts preserved the independent regression suite. Historical 3B corroboration remains MICRO 1/3 and SMALL 0/3.

### AIDER SUCCESS

Worker B is not dependable for either matched bite. It occasionally completes MICRO but does not establish a reliable classroom implementation loop. The staged-edit behavior and malformed-path attempts add repair/inspection burden.

### CLASSROOM FIT, MACHINE-SIDE PROVISIONAL

Not classroom-fit for live introductory use at either measured worker. Worker B's CPU latency is too long for a student-owned loop and it does not move the SMALL boundary. A beginning student could inspect the one-function MICRO diff, but the 142–170 s wait and 1/3 success rate make that only a machine-side occasional success, not a live recommendation.

## Decision table

| question | answer |
|---|---|
| Does stronger intelligence rescue MICRO? | No dependable rescue: Worker B 1/3, matching historical 3B rate. |
| Does stronger intelligence rescue SMALL? | No: Worker B 0/3. |
| Does it reduce scope drift? | It reduced the observed placeholder-path frequency in completed Worker B receipts, but did not remove failure/repair burden; conclusion is provisional because diff capture was defective. |
| Does it increase proof/repair burden? | Yes: substantially slower CPU loops and staged-edit accounting/occasional malformed transport complicate proof. |
| Is CPU latency classroom-plausible? | No, machine-side inference only. |
| If not, does acceleration rescue latency? | Not tested; Brandy had no usable NVIDIA accelerator. |
| Where is the new machine-side boundary? | At or below MICRO for dependable Aider work; no SMALL rescue. |
| Best current live-intro worker/bite pairing? | 3B CPU with a narrower MICRO bite only as a carefully supervised demonstration; no dependable autonomous pairing. |
| Best current independent-lab pairing? | 7B CPU for occasional MICRO exploration when latency is acceptable, with independent proof and human review; not SMALL. |
| Next useful experiment? | Repair diff/staging capture and transport validation, then test a smaller visible task surface or native deterministic edit path before any larger model. |

## Interpretation

The measured result does not support “buy more intelligence” as the next teaching move. The 7B worker did not move the reliable boundary and made waiting longer. The next suspect is the Aider/task surface and transport, while preserving the rule that Aider remains part of the lesson. Worker C is not admitted: it would add another benchmark number without resolving the repaired-apparatus limitation or the observed teaching decision.
