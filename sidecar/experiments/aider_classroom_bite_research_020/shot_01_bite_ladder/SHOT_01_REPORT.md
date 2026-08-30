# Shot 1 report — preliminary bite ladder and validity stop

## Evidence

The frozen worker was Aider 0.86.2 with `ollama_chat/qwen2.5-coder-3b-cpu:latest`, whole edits, local Ollama 0.12.6, and clean independent baselines. Three repetitions were run for MICRO and SMALL.

| rung | repetitions | wall clock seconds | targeted proof | scope result |
|---|---:|---:|---|---|
| MICRO, one-function isolated fixture | 3 | 46.32, 50.22, 37.68 | 3/3 pass | 3/3 bounded |
| SMALL, one function in three-function file | 3 | 20.52, 12.61, 12.52 | 3/3 targeted pass | 3/3 bounded |

The first calibration against the multi-function file is preserved separately: both `diff` and `whole` trials caused deletion/scope drift when asked to touch only one function. The corrected MICRO fixture made the visible surface match the request and passed. This is important evidence about context/surface design, not a license to pool the failed calibration with scored results.

## Interpretation

For this bounded fixture and worker stack, the first plausible classroom concern is not engineering capability: MICRO and SMALL both completed with clean targeted proof. The important boundary signal is inspectability/context. A one-function request in a file containing other unfinished functions caused a destructive-looking rewrite in calibration; the same semantic request in an isolated file was safe. The 3B model therefore needs the student-visible task surface to be smaller than the full repository context suggests.

The apparent SMALL speed advantage is not a teaching conclusion: MICRO and SMALL used different visible surfaces and the sample is only three repetitions. No MEDIUM/LARGE result exists yet. No claim about freshman attention or comprehension is supported.

## Three verdicts

- ENGINEERING SUCCESS: MICRO 3/3 and SMALL 3/3 targeted behavior pass.
- AIDER SUCCESS: provisional pass for the corrected MICRO and SMALL conditions; calibration in the larger file failed scope control.
- CLASSROOM FIT, MACHINE-SIDE PROVISIONAL: MICRO plausible; SMALL plausible only with a targeted oracle and a diff small enough to inspect. Live classroom validation remains required.

## Decision

`REPEAT` for Shot 1 only after the fixture is versioned so every rung has an independent, targeted oracle and the remaining MEDIUM/LARGE prompts can be scored without neighboring TODO failures contaminating proof. The raw evidence is immutable under `micro_00{1,2,3}` and `small_00{1,2,3}`.
