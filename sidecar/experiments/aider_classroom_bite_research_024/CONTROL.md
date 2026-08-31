# Mission 024 frozen control

Run: `98e5904e45437f91dcd8aba1ad39b215`
Work-file SHA-256: `dd8051c98836fd47fe2321a9ac73093e252392d951a46c8fa146dbe95b691a90`
Branch baseline: `anna/aider-visible-surface-023` / `61c8a1aca8329f7858b9a7f86a2f55b3146a2e71`

This is a matched edit-transport comparison on the exact Mission 023 MODULE surface. The target is `aider_surface_fixture/module.py`, whose seven existing budgeting helpers remain visible to Aider. The semantic bite is unchanged: add `cents_to_label(cents)`; format non-negative integer cents as a two-decimal dollar string; raise `ValueError` for negative cents.

Frozen across conditions: Aider 0.86.2; Ollama 0.12.6; `ollama_chat/qwen2.5-coder-3b-cpu:latest` (3.1B Q4_K_M); local endpoint; CPU-only worker; file-backed prompt; PTY caller; exact-model warm request before each timed attempt; fresh Aider process/context; `--no-auto-commits`; `--no-gitignore`; same target-only scope; same controller-side oracle and regression proof; deterministic target reset from the tracked baseline; same prompt wording; three scored repetitions per condition.

Independent variable:

- Control A: `--edit-format whole` (Mission 023 MODULE transport).
- Condition B: `--edit-format diff` (the directly comparable Aider-native alternate, called edit-block in Aider's implementation).

Verification attempts are recorded separately and excluded from scored rates. Scored attempts are randomized in execution order only by the runner's fixed order; no result is pooled with verification. Aider staging is recorded as evidence and is not itself a success/failure criterion.

Acceptance requires baseline proof, final oracle, regression proof, target-only effective diff, no placeholder path in filesystem state or raw output, and successful evidence accounting. Engineering success is separate from Aider success; classroom fit remains machine-side provisional.
