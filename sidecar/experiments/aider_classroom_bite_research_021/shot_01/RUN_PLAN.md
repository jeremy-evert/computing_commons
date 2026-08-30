# Mission 021 Shot 1 — repaired Bite Ladder

Three repetitions per rung, with a clean reset to the green baseline before every attempt.

| rung | requested behavior | surface | ambiguity | coupling | proof burden |
|---|---|---|---|---|---|
| MICRO | add `cents_to_label` | one function | obvious | none | two assertions |
| SMALL | add `remaining_cents` | one function | low | arithmetic boundary | two assertions |
| MEDIUM | add `remaining_cents` and `by_category` | two functions | low-medium | shared input convention | four assertions |
| LARGE | add `budget_report` using category aggregation and status | one public API plus helpers | medium | multiple related outputs | full structured oracle |

Scored timing begins after exact-model pre-warm and ends when Aider exits. Baseline regression is run before Aider; the independent oracle and regression suite run after Aider. No Mission 020 result is pooled here.
