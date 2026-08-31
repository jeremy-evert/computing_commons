# Teaching decision

## AIDER BITE CHECK

1. Is the job small?
2. Is the visible/editable workspace also small?
3. Can I predict the file and behavior that should change?
4. Do I know the proof before I run Aider?
5. Can I read the expected diff before my attention wanders?

If not: shrink the job, shrink the workspace, or use a different tool.

## Decision

Mission 023 supports, but does not yet human-validate, the stronger teaching phrase **SMALL JOB + SMALL WORKSPACE**. The same MICRO behavior was dependable in ISOLATED and NEIGHBORHOOD (6/6) and failed in MODULE (0/3), with module failures specifically showing malformed placeholder transport. Narrowing the workspace improved correctness and control, not latency: accepted loops still took about one minute on CPU.

Teach the student to bound both the requested bite and the visible/editable source surface, then predict the one-file diff and proof before invoking Aider. Do not claim that a neighborhood-sized file is universally safe; this is a machine-side provisional boundary for this worker, prompt, and fixture.

Exactly one next experimental variable: **edit transport**. Hold the semantic bite, 3B worker, and MODULE surface fixed and compare the current whole-edit route against one deterministic native edit transport, with the same path validation and independent proof. This isolates whether MODULE failure is transport-dominant rather than adding another model benchmark.

