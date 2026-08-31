# Mission 020 pilot classification

Mission 020 remains immutable pilot evidence; none of its MICRO/SMALL timings are pooled with Mission 021 scored results.

## Valid qualitative findings

- The corrected provider route is `ollama_chat/...`, not `ollama/...`.
- A faithful PTY-backed invocation matters; non-interactive local inference can look like worker failure.
- The 3B worker completed an isolated one-function MICRO request.
- The same semantic request shown beside unfinished neighboring functions caused destructive-looking scope drift.
- Aider 0.86.2, the 3B CPU worker, host resource inventory, and remote-clean handoff are durable historical facts.

## Invalid or confounded quantitative comparisons

- Mission 020 MICRO (37.68–50.22 seconds) and SMALL (12.52–20.52 seconds) are not a task-size curve: visible surfaces and warm/startup state differed.
- Mission 020 MICRO/SMALL targeted proof was useful, but the original shared fixture baseline was red, so whole-suite proof could not establish clean repository health.

## Required apparatus corrections

1. Start each attempt from the same green repository baseline.
2. Pre-register controller-side proofs and hash them before implementation; never give proofs/tests to Aider as editable files.
3. Use the corrected `ollama_chat/` route and PTY-backed invocation.
4. Pre-warm the exact worker before every scored attempt; record one separate cold-start measurement only as instructor-planning evidence.
5. Keep the fixture, plans, proofs, and receipts in durable versioned state with deterministic reset.
6. Record engineering success, Aider success, and classroom-fit machine-side provisional verdicts separately.
