# Mission 022 handoff report

Prompt: `foreman_interface/jobs/tasks/anna_brandy_aider_model_crossover_022.md`

Mission 022 tested the exact installed `ollama_chat/qwen2.5-coder-7b-cpu:latest` Worker B against the repaired Mission 021 MICRO/SMALL apparatus. Worker B completed MICRO 1/3 and SMALL 0/3 with all six regressions green and 142–170 second warm loops. The contemporary 3B control was not fully reproducible: one completed MICRO attempt failed its oracle in 76.710 seconds, while repeated attempts reproduced a malformed `path/to/...` transport failure and were preserved as invalid evidence. Historical Mission 021 remains 3B MICRO 1/3, SMALL 0/3.

Conclusion: no dependable capability crossover; CPU latency worsened. Worker C and hardware rescue were not admitted. The next experiment should repair staged/unstaged diff accounting and transport validation, then test a smaller visible task surface before model escalation.

Artifacts: `sidecar/experiments/aider_classroom_bite_research_022/CONTROL.md`, `MODEL_INVENTORY.md`, `RUN_PLAN.md`, `run_crossover.py`, `MODEL_CROSSOVER_REPORT.md`, `TEACHING_DECISION.md`, `shot_02_crossover/`, and `invalid_attempts/`.
