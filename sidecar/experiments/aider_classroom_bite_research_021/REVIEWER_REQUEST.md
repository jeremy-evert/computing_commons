# Mission 021 pre-Scored Reviewer Request

You are the milestone reviewer, not the implementation worker. The following is the complete decision context.

Mission 020 pilot: Aider 0.86.2 with `ollama_chat/qwen2.5-coder-3b-cpu:latest` completed isolated MICRO 3/3 and SMALL 3/3, but an earlier calibration with unfinished neighboring functions deleted untouched functions under both diff and whole formats. MICRO timings were 37.68–50.22 seconds and SMALL timings 12.52–20.52 seconds, but those are invalid as a size curve because visible surface and warm/startup state differed. The prior fixture baseline was red.

Mission 021 repair: the new fixture baseline is green and committed before attempts; Aider receives only `fixture/budget.py`; `fixture/test_budget.py` and `proof/*_oracle.py` are controller-side and excluded from editable scope. Each oracle is hashed before use. The corrected `ollama_chat/` route, Aider 0.86.2, whole format, PTY-backed caller, `--no-gitignore`, and exact-model pre-warm before every scored attempt are frozen. One cold-start sample is kept separate. Three repetitions are planned for each MICRO, SMALL, MEDIUM, and LARGE rung.

Classify the Mission 020 visible-surface scope-drift event and identify the smallest apparatus changes needed before freezing Mission 021 Shot 1. Check that the green baseline, controller-side non-editable oracle, corrected provider/transport, and warm-state policy address the known defects. Do not edit implementation. Return the three verdicts, failure taxonomy, and PROCEED/REPEAT/RESTART/STOP recommendation.
