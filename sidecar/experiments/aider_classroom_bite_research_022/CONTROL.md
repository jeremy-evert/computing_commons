# Mission 022 model crossover control

Run: `74cdd3619f0468bbf85c2b0e5e5d0908`  
Work file: `foreman_interface/jobs/tasks/anna_brandy_aider_model_crossover_022.md`  
Work-file launch SHA-256 supplied by owner: `79ba929c6f8c703c442aa8f190eefdb9419470ff45ccc3453451105aa7c7d6eb`  
Prior durable evidence: Mission 021 `anna/aider-bite-021` at `46684957c2dc7dc0b0b91b0783647fb43c3a7e45` plus audit `anna/aider-bite-021-audit-8a4525e` at `80880ccb0c3670dff8aaa9fc80688535ba72bede`.

Host: Brandy; 96 logical CPUs; about 375 GiB RAM; NVIDIA driver unavailable; Ollama 0.12.6 on loopback.  
Host: Brandy; 96 logical CPUs; about 375 GiB RAM; no usable NVIDIA driver; Ollama 0.12.6 on loopback.  
Worker A: Aider 0.86.2, `ollama_chat/qwen2.5-coder-3b-cpu:latest`, Q4_K_M, CPU-only.  
Worker B: Aider 0.86.2, `ollama_chat/qwen2.5-coder-7b-cpu:latest`, Q4_K_M, CPU-only.  
Both use whole edit format, no auto-commits, `--no-gitignore`, file-backed prompt, and PTY-backed faithful invocation. A separate Worker C is admitted only if B leaves the teaching decision unresolved. No hardware-rescue condition is possible on this host.

## Frozen controls

- Every attempt resets to the green fixture baseline commit for this branch.
- `fixture/test_budget.py` is the regression suite and is not an Aider file.
- `proof/*_oracle.py` is controller-side independent proof; its SHA-256 is recorded before the attempt and it is never supplied to Aider.
- Aider is given only `fixture/budget.py` and a file-backed prompt.
- Ollama is pre-warmed with the exact worker model before timing each scored attempt. One cold-start sample is recorded separately only as planning evidence.
- Aider stdout, stderr, timing, diff, baseline regression, oracle proof, and after-action receipt are preserved per immutable attempt.

## Frozen comparison

The task semantics are identical to Mission 021 Shot 1: MICRO adds `cents_to_label`; SMALL adds `remaining_cents`. Each condition has three repetitions, starting from the same green fixture commit and using the same controller-side oracle hashes. Mission 021 results remain historical corroboration, not pooled repetitions. Engineering success is oracle pass plus regression pass; Aider success additionally requires acceptable scope. Classroom fit is explicitly machine-side provisional.

## Selection rationale

Live Ollama inventory confirmed the exact 3B baseline unchanged and showed an installed 7.6B Q4_K_M coding model. It is the nearest meaningfully stronger coding-capable model already installed, so it is Worker B. The installed 14B candidates are not measured unless Worker B cannot resolve whether intelligence moves the MICRO/SMALL boundary.

## Ladder dimensions

MICRO adds one obvious formatter in one function. SMALL adds one bounded remaining-budget behavior. MEDIUM adds two related reporting behaviors across one file. LARGE adds a complete budget report with aggregation, formatting, and status. Surface, ambiguity, coupling, and proof burden increase together by design and are recorded per rung; LOC is not the task definition.
