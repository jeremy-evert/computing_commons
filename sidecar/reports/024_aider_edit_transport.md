# Mission 024 — Aider edit transport

Prompt: `foreman_interface/jobs/tasks/anna_brandy_aider_edit_transport_024.md`
Run: `98e5904e45437f91dcd8aba1ad39b215`
Work-file SHA-256: `dd8051c98836fd47fe2321a9ac73093e252392d951a46c8fa146dbe95b691a90`
Branch: `anna/aider-edit-transport-024`
Worktree: `/mnt/brandy_nvme/jevert/git/worktrees/computing_commons-aider-edit-transport-024`

## Summary

Mission 023's Module condition was reconstructed from baseline `61c8a1a…`: the same seven-helper `module.py`, cents-label bite, 3B Q4_K_M worker, Aider 0.86.2, PTY caller, independent oracle, regression proof, and warm policy. Installed Aider truth listed both `whole` and `diff`; Mission 023 used `whole`, so `diff` was selected as the direct alternate.

Whole completed 4/4 scored attempts with engineering 0/4, Aider 0/4, and placeholder-path rate 4/4. Diff completed 2/3 scored attempts with engineering 2/2, Aider 0/2, and placeholder-path rate 2/2; the third attempt (`valid_005`) timed out/incompletely captured and is excluded. Diff verification passed target proof but also emitted the placeholder path. Whole verification failed the oracle. See [EDIT_TRANSPORT_REPORT.md](../experiments/aider_classroom_bite_research_024/EDIT_TRANSPORT_REPORT.md) and the per-attempt raw bundles.

The apparatus had two repair findings: a fixed path-expression bookkeeping bug, and a long-tail PTY/caller hang that prevented the final diff repetition from completing. Those failures are preserved in the incomplete attempt directories and must not be laundered into scored results.

## Required contract checks

- AGENTS.md: read; no update required.
- Tests: baseline fixture proof passed before attempts; complete diff attempts passed oracle and regression; whole attempts failed oracle as recorded.
- `git diff --check`: working-tree check passed for implementation state; full staged check reports whitespace in preserved raw patch payloads, which are immutable evidence.
- `make task-check`: unavailable — `make: *** No rule to make target 'task-check'. Stop.`
- `make check`: unavailable — `make: *** No rule to make target 'check'. Stop.`
- Commit/push: pending.
- Final status: pending.

## Decision

Transport did not yet rescue Module under the strict Aider-success definition. Keep “small job + small workspace” as the only supported machine-side teaching rule. Do not put a specific edit mode on the student card. One next variable: repaired replication of the same whole-versus-diff Module comparison.
