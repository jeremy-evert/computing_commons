# Mission 023 — visible surface report

## Results

| surface | scored success | warm wall time | scope/transport | proof burden |
|---|---:|---:|---|---|
| ISOLATED | 3/3 engineering and Aider | 59.5–61.3 s, median 60.9 s | 0/3 unexpected or placeholder paths; one target file | independent oracle + regression passed 3/3 |
| NEIGHBORHOOD | 3/3 engineering and Aider | 66.0–70.9 s, median 70.3 s | 0/3 unexpected or placeholder paths; one target file | independent oracle + regression passed 3/3 |
| MODULE | 0/3 engineering or Aider | 69.7–145.5 s, median 143.6 s | 3/3 placeholder `path/to/aider_surface_fixture/module.py`; no accepted target diff | independent oracle failed 3/3; regression remained green |

The module condition's failures are cleanly separated from proof correctness: the baseline/regression suite stayed green, while Aider generated a malformed placeholder path and the controller rejected it. The module did not produce an accepted target diff. The isolated and neighborhood diffs were small single-file changes (14–17 patch lines including headers), and the exact target path was the only edited path.

## Required analysis

1. Narrowing the visible surface materially improved engineering success: 100% for isolated/neighborhood versus 0% for module.
2. It improved Aider success without changing the semantic goal: 3/3 versus 0/3.
3. It reduced destructive/irrelevant scope drift: none in accepted narrow conditions; module had 3/3 malformed-path transport failures.
4. It reduced observed malformed-path failure for narrow surfaces, but cannot prove whether the trigger is file width, path/context interaction, or both.
5. It reduced proof burden because accepted narrow attempts had one predictable target and independent green proof; module required rejection and cleanup.
6. It did not reduce latency monotonically: neighborhood was about 9 seconds slower than isolated, while module failures were much slower in two attempts. Correctness/control improved more clearly than speed.
7. The student-facing diff stopped being predictably inspectable at MODULE in this apparatus; NEIGHBORHOOD remained inspectable by machine-side inference.
8. The dominant boundary in this run is visible surface plus Aider orchestration/transport interaction, not model size. Model capability remains a possible contributor, but this run held it fixed.
9. The data support teaching “small job + small workspace” as a provisional machine-side rule, with classroom validation still required.

## Verdicts

- **ENGINEERING SUCCESS:** ISOLATED 3/3; NEIGHBORHOOD 3/3; MODULE 0/3. Regression stayed green on all scored attempts.
- **AIDER SUCCESS:** ISOLATED 3/3 and NEIGHBORHOOD 3/3 with target-only accepted diffs; MODULE 0/3 because all attempts generated rejected placeholder-path transport.
- **CLASSROOM FIT, MACHINE-SIDE PROVISIONAL:** ISOLATED and NEIGHBORHOOD are plausible supervised demonstrations; MODULE is not. A roughly one-minute CPU wait remains a live-class concern, and no freshman attention/comprehension claim is made.

