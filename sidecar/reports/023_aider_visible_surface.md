# Mission 023 handoff — Aider visible surface

Prompt: `foreman_interface/jobs/tasks/anna_brandy_aider_visible_surface_023.md`  
Run: `124291966df2aff1c2a3eb00659bfc27`  
Work file SHA-256: `06a06f839dd9d95d1c9629d027cd0ebb3eceb3d86fb371deaf06b2b5b202ca13`  
Branch: `anna/aider-visible-surface-023`

Mission 021/022 evidence was preserved from the durable branches. Mission 023 repaired staged/unstaged/HEAD diff accounting, added placeholder-path rejection, used a tracked green baseline, controller-side oracle hashing, deterministic target reset, and a PTY-backed Aider caller. The post-repair non-scored verification passed; its evidence and earlier failed calibrations remain preserved.

Frozen stack: Aider 0.86.2; `ollama_chat/qwen2.5-coder-3b-cpu:latest` (3.1B Q4_K_M); Ollama 0.12.6; CPU-only; whole edit; exact-model warm before timing; no auto-commits; no gitignore mutation.

Scored results: ISOLATED 3/3 at 59.5–61.3 s; NEIGHBORHOOD 3/3 at 66.0–70.9 s; MODULE 0/3 at 69.7–145.5 s, all three rejected for `path/to/aider_surface_fixture/module.py`. Regression proof remained green; accepted conditions had no unexpected paths and small target-only diffs.

Conclusion: **SMALL JOB + SMALL WORKSPACE** is supported as a machine-side provisional teaching rule. The result improves correctness, scope control, and proof inspectability more clearly than latency. It does not establish freshman comprehension. Exactly one next variable is recommended: edit transport on the fixed MODULE surface.

Required artifact: `sidecar/experiments/aider_classroom_bite_research_023/TEACHING_DECISION.md`.

## Handoff contract

- AGENTS.md: read; no update required.
- Tests: `python3 -m pytest -q sidecar/experiments/aider_classroom_bite_research_023/fixture` — 1 passed.
- `git diff --check` — passed.
- `make task-check` — unavailable: `make: *** No rule to make target 'task-check'. Stop.`
- `make check` — unavailable: `make: *** No rule to make target 'check'. Stop.`
- Commits: `8ca04d9` apparatus; `b9597b0` path/setup repair; `ddc49d4` malformed artifact cleanup; `42fd70b` PTY reap repair; `e523440` tracked baselines; `8cad494` verification mode; `4e80986` evidence-path repair; `b105b3b` scored evidence and synthesis.
- Push: completed to `origin/anna/aider-visible-surface-023`; final remote tip verified.
- Final `git status --short`: clean.
- Next recommended prompt: test exactly one variable—edit transport—on the fixed MODULE surface while holding the 3B worker, semantic bite, proof, and visible workspace constant.
