# Mission 021 Shot 1 report — repaired ladder stop

## Valid results

| rung | repetitions | oracle pass | regression pass | warm-loop seconds | interpretation |
|---|---:|---:|---:|---|---|
| MICRO | 3 | 1/3 | 3/3 | 80.525, 77.658, 137.641 | bounded but unreliable |
| SMALL | 3 | 0/3 | 3/3 | 135.264, 133.935, 134.953 | no new-behavior success |
| MEDIUM | 3 | 0/3 | 3/3 | 144.418, 143.957, 141.429 | no new-behavior success |
| LARGE | 0 | not scored | not scored | not scored | stopped after boundary evidence |

All valid attempts used baseline commit `988a7a7`, the same hashed controller oracle per rung, Aider 0.86.2, `ollama_chat/qwen2.5-coder-3b-cpu:latest`, whole edit format, `--no-gitignore`, and exact-model pre-warm. Mission 020 data is not pooled.

## Boundary interpretation

The repaired experiment establishes a machine-side provisional classroom boundary at or below MICRO for this worker/transport/fixture. Aider exited 0 and kept the green regression suite in all nine valid attempts, but it produced the requested new behavior only once at MICRO and never at SMALL or MEDIUM. Warm-loop latency was about 78–145 seconds, already long for a live student-controlled loop. The dominant evidenced causes are model capability/precision and latency; no proof contamination or baseline redness explains the failures.

## Three verdicts

- **ENGINEERING SUCCESS:** 1/3 MICRO; 0/3 SMALL; 0/3 MEDIUM.
- **AIDER SUCCESS:** provisional failure for reliable bounded implementation beyond an occasional MICRO success; all attempts preserved regression behavior.
- **CLASSROOM FIT, MACHINE-SIDE PROVISIONAL:** MICRO is not yet dependable enough for live introduction with this stack; SMALL and MEDIUM are not classroom-fit. This is not human-student evidence.

## Stop

LARGE and Shots 2–7 were not run. Further repetitions would primarily add benchmark numbers without changing the current teaching decision, and the mission stop condition permits preserving the clean failure boundary. The incomplete LARGE directory contains only its pre-call plan/baseline capture and is not scored.

## Next experiment recommendations

1. Highest teaching value: repeat MICRO with the 7B CPU worker or an authorized stronger implementation engine while holding the repaired apparatus fixed, to separate small-model capability from bite size.
2. Next: test a narrower one-function prompt/fixture with the 3B worker to isolate whether the remaining MICRO miss is semantic or transport-related.
3. Only after a dependable MICRO/SMALL boundary exists, design Big-vs-Small Bites; do not spend runs on Model Crossover at an unestablished boundary.
