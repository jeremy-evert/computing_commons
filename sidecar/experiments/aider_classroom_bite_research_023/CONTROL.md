# Mission 023 visible-surface control

Run: `124291966df2aff1c2a3eb00659bfc27`  
Work file SHA-256: `06a06f839dd9d95d1c9629d027cd0ebb3eceb3d86fb371deaf06b2b5b202ca13`  
Branch: `anna/aider-visible-surface-023`

Worker and tool stack were frozen across all scored conditions: Aider 0.86.2; `ollama_chat/qwen2.5-coder-3b-cpu:latest`; Q4_K_M, 3.1B; Ollama 0.12.6; CPU-only; whole edit format; file-backed prompt; PTY-backed caller; exact-model warm request before each timed attempt; no Aider auto-commits; no gitignore mutation; independent controller-side oracle.

The semantic bite was identical everywhere: add `cents_to_label(cents)` with exact two-decimal dollar output and `ValueError` for negative cents. Only visible/editable source surface changed:

| condition | target | visible context | pre-registered prediction |
|---|---|---|---|
| ISOLATED | `aider_surface_fixture/isolated.py` | target responsibility alone | one target function, one file, no unrelated changes |
| NEIGHBORHOOD | `aider_surface_fixture/neighborhood.py` | target plus two helpers | same |
| MODULE | `aider_surface_fixture/module.py` | target plus seven helpers | same |

Regression tests and `proof/oracle.py` were never passed to Aider. The oracle hash for every attempt is `2ed82404fd278ca31091576d9028b38a83faba6b2e418c2ae2f1414e9917316a`.

Instrumentation captures porcelain status, unstaged target diff, cached target diff, `git diff HEAD -- target`, baseline/final oracle, regression proof, warm output, and separate Aider stdout/stderr. Placeholder paths (`path/to/...`, `...`, angle-bracket paths) and non-target paths are invalid for Aider success. Reset uses `git restore --source=<baseline> --staged --worktree -- <target>` and touches no unexplained path.

