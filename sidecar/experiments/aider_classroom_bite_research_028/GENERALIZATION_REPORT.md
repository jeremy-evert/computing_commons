# Mission 028 generalization report

## Outcome

The mission stopped before scoring could begin. Non-scored verification completed
for both formats with child reaping, reset, Git diff accounting, independent proof,
and terminal receipts. The first scored `whole` and `diff` attempts each timed out
at the frozen 360-second ceiling and were explicitly process-group terminated and
reaped. Therefore there are zero valid scored repetitions in both conditions.

| format | verification | scored valid | scored invalid | engineering | Aider |
|---|---:|---:|---:|---:|---:|
| whole | 1 valid-complete | 0 | 1 timeout | not estimable | not estimable |
| diff | 1 valid-complete | 0 | 1 timeout | not estimable | not estimable |

The verification `diff` attempt produced a target edit but deleted neighboring
helpers and added an unrequested in-module test; its independent regression proof
correctly rejected the result. The verification `whole` attempt emitted forbidden
placeholder paths and did not produce the requested implementation. These are
qualitative observations only, not scored generalization results.

## Frozen truth and limits

The stack was present and matched Mission 025: Aider 0.86.2, Ollama 0.12.6,
`ollama_chat/qwen2.5-coder-3b-cpu:latest`, CPU-only, PTY caller, 360-second
timeout, exact-model warm-up, and independent oracle/regression proof. The local
model route nevertheless failed to yield a valid scored completion in either
format during this run. No prompt tuning or model substitution was performed.

The new 27-line, six-helper string module is somewhat smaller than Mission 025's
37-line, seven-helper module, but remains a comparable SMALL single-module bite.
That surface comparison cannot overcome the missing valid matrix.

## Verdicts

- ENGINEERING SUCCESS: not estimable for the scored matrix.
- AIDER SUCCESS: not estimable for the scored matrix.
- CLASSROOM FIT, MACHINE-SIDE PROVISIONAL: not estimable; the observed scored
  waits alone are a classroom risk, but cannot be treated as a stable latency result.

The apparatus stop condition applies. The evidence does not establish whether
Mission 025's diff advantage generalizes.
