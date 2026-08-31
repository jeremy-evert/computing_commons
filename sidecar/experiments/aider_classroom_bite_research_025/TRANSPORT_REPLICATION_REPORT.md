# Mission 025 transport replication report

## Result

The fixed MODULE comparison reached the required three valid-complete repetitions per condition. `whole` was 0/3 engineering success and 0/3 Aider success. `diff` was 3/3 engineering success and 3/3 Aider success after an evidence audit corrected an over-broad placeholder regex in the first classifier: Aider's expected `<<<<<<< SEARCH` / `>>>>>>> REPLACE` delimiters were mistakenly matched as angle-bracket placeholders. The raw transcripts contain no forbidden `path/to/...` target in the successful diff runs, and the only filesystem extra was the known `.aider.tags.cache.v4/` transient removed by cleanup.

## Matrix

| format | valid complete | invalid | engineering | Aider | latency seconds | placeholder/path finding |
|---|---:|---:|---:|---:|---|---|
| whole | 3/3 | 0 | 0/3 | 0/3 | 87.160, 153.951, 58.703 | 2/3 raw placeholder or wrong-path emission; transient cache in all three |
| diff | 3/3 | 2 | 3/3 | 3/3 (audited) | 100.996, 190.213, 240.276 | 0/3 forbidden placeholder paths; expected diff delimiters only; transient cache in all three |

Invalid diff evidence: repetition 2 timed out at 360.115 seconds and repetition 3 was interrupted before terminal accounting. Both are preserved and excluded. No valid-complete run remained with an unreaped Aider child; the timeout's outer shell attachment was separately preserved as caller evidence.

## Interpretation

Mission 024's apparent engineering advantage for `diff` replicated on the fixed surface and strengthened to 3/3 valid engineering success versus 0/3 for `whole`. Unlike Mission 024, the corrected raw audit establishes nonzero accepted Aider success for `diff` (3/3). `whole` reproduced the visible-surface failure. Effective diff runs touched only the target, produced small freshman-inspectable changes, and passed oracle/regression proof. Latency was long-tail for `diff` (median 190.213 s) and remains a classroom risk.

The result supports edit transport as a real control variable. It does not establish freshman comprehension or justify broadening task size. The next experiment should replicate `diff` on one second task family before publishing a student-facing mode rule.

## Correction lineage

**ANNA SELF-CORRECTION / APPARATUS AUDIT:** the initial classifier treated any `<...>` span as a placeholder, which conflated expected diff transport delimiters with forbidden path placeholders. The raw evidence and filesystem/path captures show the distinction. The runner now matches concrete placeholder path forms only and permits the known transient cache for scope classification while still recording it.
