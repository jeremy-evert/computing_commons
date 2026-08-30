# Mission 021 audit and handoff

## Assignment identity

- Work file: `foreman_interface/jobs/tasks/anna_brandy_aider_classroom_bite_research_repair_resume_021.md`
- Assigned run: `8a4525e15b25d7d7c2a2b535682ac1da`
- Work-file SHA-256: `b07dc1c8b7c7dbae995a8e307a269d5a622fdcddcbe72071e60efe4505b7f721`
- Audit worktree: `worktrees/computing-commons-aider-bite-021-audit`
- Source evidence branch: `anna/aider-bite-021` at `46684957c2dc7dc0b0b91b0783647fb43c3a7e45`

## Finding

Mission 021's repaired Shot 1 evidence already exists as a clean, pushed forward continuation of Mission 020. It preserves Mission 020 as pilot evidence, uses the corrected `ollama_chat/` route and PTY-backed Aider path, hashes controller-side oracles, starts from a green fixture baseline, pre-warms the exact 3B worker, and records nine valid attempts plus six invalid caller attempts.

The valid results support the existing stop decision: MICRO succeeded 1/3, SMALL 0/3, and MEDIUM 0/3, while regression proof passed 9/9. The evidence supports a provisional machine-side boundary at or below MICRO for this 3B CPU stack; it does not support claims about freshman comprehension. LARGE and later adaptive shots were correctly not run after the boundary became clear.

## Reconciled discrepancies

The prior report was authored under an earlier Foreman run (`bf4ed9f0b3937d9942871697173ceb77`) and retained that historical identity. This audit keeps that report immutable and records the present assigned run separately. The branch is currently clean and locally tracks `origin/anna/aider-bite-021`; the prior report's “push pending” note is stale, not an indication of current branch state.

The standalone `proof/baseline_regression.py` helper failed when invoked without `PYTHONPATH`, although the recorded fixture pytest regression proof passed. The caller now sets the fixture directory in the same environment for both baseline and final oracle calls, making the documented proof path reproducible without changing any scored evidence.

## Validation

- Fixture tests: `python3 -m pytest -q sidecar/experiments/aider_classroom_bite_research_021/fixture` — 3 passed.
- Baseline proof: `PYTHONPATH=sidecar/experiments/aider_classroom_bite_research_021/fixture python3 sidecar/experiments/aider_classroom_bite_research_021/proof/baseline_regression.py` — passed.
- Valid attempt regression proofs: 9/9 passed in preserved receipts.
- `make task-check`: unavailable — `make: *** No rule to make target 'task-check'. Stop.`
- `make check`: unavailable — `make: *** No rule to make target 'check'. Stop.`
- `git diff --check`: passed.
- Remote verification: local tracking metadata confirms `anna/aider-bite-021` tracks the pushed remote branch; a fresh `git ls-remote` was blocked by the host's bad-permissions SSH config (`/etc/ssh/ssh_config.d/30-libvirt-ssh-proxy.conf`), so no new network claim is made here.

## Commit and push record

- `bbaa300` — controller proof-import repair.
- `2d00f13` — this audit report.
- Push: `origin/anna/aider-bite-021-audit-8a4525e` created successfully.
- Final audit worktree status: clean.

## Changed files

- `sidecar/experiments/aider_classroom_bite_research_021/run_shot1.py` — reproducible fixture import environment for controller proofs.
- This audit report.

## AGENTS.md and next step

`AGENTS.md` was read; no update was required. The next recommended prompt remains a controlled model-capability crossover at MICRO/SMALL using the repaired apparatus, followed by Big-vs-Small design only if a dependable boundary is established. This audit does not execute that next prompt.
