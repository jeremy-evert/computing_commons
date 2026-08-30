# Mission 021 repaired campaign control

Run: `bf4ed9f0b3937d9942871697173ceb77`  
Work file SHA-256: `b07dc1c8b7c7dbae995a8e307a269d5a622fdcddcbe72071e60efe4505b7f721`  
Prior durable evidence: `anna/aider-bite-020` at `8a5d9cfddca511b29c69a92e5062166304653dcd`.

Host: Brandy; 96 logical CPUs; about 375 GiB RAM; NVIDIA driver unavailable; Ollama 0.12.6 on loopback.  
Worker: Aider 0.86.2, `ollama_chat/qwen2.5-coder-3b-cpu:latest`, whole edit format, no auto-commits, `--no-gitignore`, PTY-backed launcher.  
Reviewer: `ollama_chat/qwen2.5:14b-instruct`, review-only; reviewer time is not worker time.

## Frozen controls

- Every attempt resets to the green fixture baseline commit for this branch.
- `fixture/test_budget.py` is the regression suite and is not an Aider file.
- `proof/*_oracle.py` is controller-side independent proof; its SHA-256 is recorded before the attempt and it is never supplied to Aider.
- Aider is given only `fixture/budget.py` and a file-backed prompt.
- Ollama is pre-warmed with the exact worker model before timing each scored attempt. One cold-start sample is recorded separately.
- Aider stdout, stderr, timing, diff, baseline regression, oracle proof, and after-action receipt are preserved per immutable attempt.

## Ladder dimensions

MICRO adds one obvious formatter in one function. SMALL adds one bounded remaining-budget behavior. MEDIUM adds two related reporting behaviors across one file. LARGE adds a complete budget report with aggregation, formatting, and status. Surface, ambiguity, coupling, and proof burden increase together by design and are recorded per rung; LOC is not the task definition.
