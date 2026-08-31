# Mission 024 edit-transport report

## Result

The comparison did not establish a Module rescue. `whole` reproduced the Mission 023 failure in four complete scored repetitions. `diff` produced correct target edits and independent proof in two complete scored repetitions, but both raw responses contained the literal placeholder path and therefore failed the mission's Aider-success gate. A third clean diff repetition reached the caller's long-tail state without a receipt and is invalid/incomplete evidence.

## Frozen comparison

- Target: `aider_surface_fixture/module.py`, the unchanged Mission 023 MODULE surface.
- Bite: add `cents_to_label(cents)` with two-decimal dollar output and `ValueError` for negative input.
- Model: `ollama_chat/qwen2.5-coder-3b-cpu:latest`, 3.1B Q4_K_M.
- Aider: 0.86.2; Ollama: 0.12.6; CPU-only; PTY; exact-model warm-up; no auto-commits.
- Baseline: `61c8a1aca8329f7858b9a7f86a2f55b3146a2e71`.
- Formats: `whole` (control) and `diff` (Aider-native edit-block alternate).

## Evidence summary

| format | complete scored repetitions | engineering success | Aider success | placeholder rate | elapsed seconds |
|---|---:|---:|---:|---:|---|
| whole | 4 | 0/4 | 0/4 | 4/4 | 126.563, 129.179, 129.673, 132.551 |
| diff | 2 | 2/2 | 0/2 | 2/2 | 103.840, 104.574 |

The additional diff `valid_005` was interrupted after the Aider call exceeded the practical caller window; it has no final proof/receipt and is excluded. Verification was run separately for both formats. Whole verification failed the oracle; diff verification passed the oracle but emitted the placeholder-path string.

The whole failures changed or attempted `path/to/aider_surface_fixture/module.py` and did not produce the requested target behavior. The diff attempts applied the requested target function and passed regression/oracle proof, but the model's raw answer included `path/to/aider_surface_fixture/module.py` and SEARCH/REPLACE transport text. This is a valid transport failure under the frozen rejection rule, not a harness invalidation.

## Reviewer answers

1. Changing transport did not rescue Module under the Aider-success definition.
2. Complete engineering success was 0/4 whole and 2/2 diff; accepted Aider success was 0/4 and 0/2.
3. Neither format eliminated placeholder-path failures; diff reduced target-edit failure but retained placeholder emissions.
4. Diff produced a target-only effective edit in the complete attempts; whole produced placeholder-path scope drift.
5. Diff was about 22 seconds faster in the two complete scored observations, but the sample is incomplete and the long-tail timeout remains relevant.
6. Diff's successful target diff was small and concrete; its raw transport explanation was more verbose than the student-facing diff.
7. Diff reduced repair burden for the target behavior but did not reduce the placeholder-validation burden.
8. The evidence supports an interaction between Module-sized visible surface and edit transport, with unresolved 3B capability still present. It does not isolate transport as the sole cause.
9. No teaching recommendation about a specific Aider mode is justified yet because accepted Aider success remained zero and the third diff repetition did not complete.
10. Repair the PTY/attempt apparatus and repeat the matched diff condition from a fully clean deterministic baseline before changing another variable.

## Verdicts

- ENGINEERING SUCCESS: mixed by format; whole 0/4, diff 2/2 complete attempts.
- AIDER SUCCESS: not demonstrated; whole 0/4, diff 0/2 because of placeholder emissions.
- CLASSROOM FIT, MACHINE-SIDE PROVISIONAL: not established; a correct diff is promising, but placeholder handling and long-tail latency remain too costly.
