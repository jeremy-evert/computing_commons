# Mission 022 handoff report

Prompt: `foreman_interface/jobs/tasks/anna_brandy_aider_model_crossover_022.md`

Mission 022 tested the exact installed `ollama_chat/qwen2.5-coder-7b-cpu:latest` Worker B against the repaired Mission 021 MICRO/SMALL apparatus. Worker B completed MICRO 1/3 and SMALL 0/3 with all six regressions green and 142–170 second warm loops. The contemporary 3B control was not fully reproducible: one completed MICRO attempt failed its oracle in 76.710 seconds, while repeated attempts reproduced a malformed `path/to/...` transport failure and were preserved as invalid evidence. Historical Mission 021 remains 3B MICRO 1/3, SMALL 0/3.

Conclusion: no dependable capability crossover; CPU latency worsened. Worker C and hardware rescue were not admitted. The next experiment should repair staged/unstaged diff accounting and transport validation, then test a smaller visible task surface before model escalation.

Artifacts: `sidecar/experiments/aider_classroom_bite_research_022/CONTROL.md`, `MODEL_INVENTORY.md`, `RUN_PLAN.md`, `run_crossover.py`, `MODEL_CROSSOVER_REPORT.md`, `TEACHING_DECISION.md`, `shot_02_crossover/`, and `invalid_attempts/`.

## Required handoff record

- AGENTS.md: read; no update required.
- Tests: `python3 -m pytest -q sidecar/experiments/aider_classroom_bite_research_022/fixture` — 3 passed; baseline controller proof — passed; Worker B regression proofs — 6/6 passed; contemporary 3B control — incomplete and explicitly reported.
- `git diff --check`: passed.
- `make task-check`: unavailable — `make: *** No rule to make target 'task-check'. Stop.`
- `make check`: unavailable — `make: *** No rule to make target 'check'. Stop.`
- Commits: `5467fb5` control; `4290ad5` transport correction; `f4155d4` restored proven prompt; `02cfe58` removed malformed artifact; `355968e` contemporary control failures; `1e4f0f4` isolated Worker B; `8a27285` final evidence.
- Push: completed to `origin/anna/aider-bite-022`.
- Final managed worktree: clean; branch `anna/aider-bite-022`.
- Next recommended prompt: repair staged/unstaged diff capture and placeholder-path rejection, then run a clean contemporary 3B control against a narrower visible MICRO/SMALL surface before any 14B escalation.
