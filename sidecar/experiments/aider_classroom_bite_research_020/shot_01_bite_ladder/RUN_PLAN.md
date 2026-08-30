# Shot 1 — Bite Ladder frozen plan

Question: how does increasing visible bite size change latency, prediction mismatch, scope drift, repair burden, proof, and provisional classroom fit?

Frozen stack: Brandy; Aider 0.86.2; `ollama_chat/qwen2.5-coder-3b-cpu:latest`; whole edit format; local Ollama endpoint; independent process/context; warmed after calibration; clean baseline `a230e578`; pytest oracle in `fixture/test_budget.py`.

Rungs, ordered by surface/ambiguity/coupling/proof burden:

- MICRO: isolated `micro_fixture.py`, one formatting function, one assertion.
- SMALL: `budget.py`, implement `add_expense`, one validation rule.
- MEDIUM: `budget.py`, implement `add_expense` and `summarize`, two related behaviors and three assertions.
- LARGE: `budget.py`, implement all three public behaviors and satisfy the full oracle.

Each rung has three clean repetitions. Exact prompt and prediction are stored per attempt. Aider may edit only the named production file; tests are read-only evidence.
