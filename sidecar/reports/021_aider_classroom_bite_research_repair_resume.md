# Mission 021 — Aider classroom bite research repair/resume

## Prompt and scope

Prompt: `foreman_interface/jobs/tasks/anna_brandy_aider_classroom_bite_research_repair_resume_021.md`
Primary repository: `computing_commons`
Branch: `anna/aider-bite-021`
Run: `bf4ed9f0b3937d9942871697173ceb77`
Work-file SHA-256: `b07dc1c8b7c7dbae995a8e307a269d5a622fdcddcbe72071e60efe4505b7f721`

## Outcome

Mission 020 was preserved as pilot evidence and not relabeled or pooled. Its visible-surface scope drift, red baseline, independent-proof weakness, and warm/cold timing confound were classified and repaired. The stronger reviewer approved proceeding. Mission 021 then completed valid MICRO, SMALL, and MEDIUM ladder repetitions under one repaired apparatus and stopped before LARGE because the teaching decision was already clear.

## Evidence

- Valid MICRO: 1/3 oracle pass; 3/3 regression pass; 77.658–137.641 seconds.
- Valid SMALL: 0/3 oracle pass; 3/3 regression pass; 133.935–135.264 seconds.
- Valid MEDIUM: 0/3 oracle pass; 3/3 regression pass; 141.429–144.418 seconds.
- Aider exited 0 for all nine valid attempts; the independent oracles, not Aider’s exit status, determined behavior success.
- The first caller version produced invalid absolute-path edits under `path/to/...`; those attempts are preserved as invalid evidence, the accidental tree was removed, and the caller was corrected and separately committed before valid scoring.
- Host truth: 96 logical CPUs, about 375 GiB RAM, Ollama 0.12.6, no usable NVIDIA driver. CPU-only execution was authorized for Shots 1–4.

## Verdicts

Engineering success was occasional only at MICRO and absent at SMALL/MEDIUM. Aider success was not reliable for the requested new behaviors with the 3B worker, despite clean regression preservation. Machine-side provisional classroom fit is not established for SMALL/MEDIUM and is not dependable for MICRO at this stack; no claim about freshman comprehension is made.

## Teaching artifacts and next work

This mission produced the repaired control, pilot classification, reviewer judgment, green fixture, hashed independent oracles, immutable attempt receipts, and Shot 1 report. It did not produce the required final Shot 7 student Bite Card/rubric/live-class packet because the campaign stopped at the evidenced boundary. The next recommended prompt is a controlled model-capability crossover at MICRO/SMALL using the same repaired apparatus; only after that should Big-vs-Small Bites be designed.

## Required validation record

- AGENTS.md: read; no update required.
- `make task-check`: unavailable — `make: *** No rule to make target 'task-check'. Stop.`
- `make check`: unavailable — `make: *** No rule to make target 'check'. Stop.`
- Tests: `python3 -m pytest -q sidecar/experiments/aider_classroom_bite_research_021/fixture` — 3 passed; every valid attempt’s regression proof — 9/9 passed.
- `git diff --check`: passed before commits; rerun at handoff.
- Commits: `988a7a7` repaired fixture/control; `3d78a59` caller correction and invalid-attempt record; `1d9feba` final evidence and report.
- Push status: pending final commit/push.
- Final status: clean after final commit/push, except any explicitly reported allocator-managed worktree metadata outside Git.

## Final result

`AIDER BITE CAMPAIGN REPAIRED — MORE VALID RUNS NEEDED`
