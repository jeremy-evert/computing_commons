# Mission 025 handoff — Aider edit transport replication

Prompt: `foreman_interface/jobs/tasks/anna_brandy_aider_edit_transport_replication_025.md`
Run: `dbab4f46ba90f0d386ea49c6725e2afa`
Worktree: `/mnt/brandy_nvme/jevert/git/worktrees/computing-commons-aider-edit-transport-replication-025`
Branch: `anna/aider-edit-transport-replication-025`

## Handoff

- Frozen stack reproduced: Aider 0.86.2; Ollama 0.12.6; `ollama_chat/qwen2.5-coder-3b-cpu:latest`, 3.1B Q4_K_M, digest `6a345c…`; CPU-only; local endpoint; PTY; no auto-commit; exact-model warm-up.
- Apparatus repairs: explicit process-group lifecycle and reap; 360-second timeout; terminal invalid receipts; deterministic target/path/cache reset; complete Git diff/path accounting; raw-vs-filesystem placeholder scan.
- Verification: both formats valid-complete through the repaired PTY/reset/proof path; expected transport failures were captured without orphan processes. Earlier caller/reset failures remain immutable evidence.
- Scored valid counts: whole 3, diff 3. Invalid diff counts: timeout 1, interrupted caller accounting 1.
- Scored results: whole engineering/Aider 0/3 and 0/3; diff engineering/Aider 3/3 and 3/3 after classifier audit correcting SEARCH/REPLACE false positives.
- Latencies: whole 87.160, 153.951, 58.703 s; diff 100.996, 190.213, 240.276 s. Diff target changes are small and proof-clean.
- Verdicts: ENGINEERING SUCCESS—diff reproducible; AIDER SUCCESS—diff reproducible after evidence audit; CLASSROOM FIT, MACHINE-SIDE PROVISIONAL—latency and single-task-family limits remain.
- Mission 024's apparent diff advantage replicated. The next and only variable is a second task-family replication using diff.

## Required contract checks

- AGENTS.md: read; no update required.
- Tests: `python3 -m pytest -q sidecar/experiments/aider_classroom_bite_research_023/fixture/test_surfaces.py` passed (baseline and per-attempt proofs recorded).
- `make task-check`: unavailable — `make: *** No rule to make target 'task-check'. Stop.`
- `make check`: unavailable — `make: *** No rule to make target 'check'. Stop.`
- `git diff --check`: raw evidence contains expected transcript whitespace; implementation/docs are checked separately before final commit.
- Prior Mission 023/024 artifacts preserved unchanged.

## Git durability

- Commits: `cf2a5e8` (apparatus and verification checkpoint), `8d95e66` (scored evidence and synthesis).
- Push: completed; `origin/anna/aider-edit-transport-replication-025` matches the local HEAD after the final forward commit.
- Final worktree status after cleanup: clean.

## Next recommended prompt

Run one second task-family replication with `diff`, holding the model, proof, CPU condition, and scope discipline constant. Do not broaden task size or add a student-facing edit-mode rule before that shot.

## Durable artifacts

- Control, run plan, apparatus repair, runner, verification bundles, and scored raw bundles: `sidecar/experiments/aider_classroom_bite_research_025/`.
- Synthesis: `sidecar/experiments/aider_classroom_bite_research_025/TRANSPORT_REPLICATION_REPORT.md`.
- Teaching decision: `sidecar/experiments/aider_classroom_bite_research_025/TEACHING_DECISION.md`.
