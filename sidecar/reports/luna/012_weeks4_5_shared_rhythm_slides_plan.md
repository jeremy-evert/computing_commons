# Prompt 012 plan — Weeks 4–5 shared-rhythm slide factory

## Exact source inventory

| Session | Canonical source | Pinned commit | Planned output |
|---|---|---|---|
| Week 4 Monday | `ai_fluency/ai_i/monday_moments/week_04_decompose_the_task/` | `022262cf207c28a9504425779a24247ddcf66884` | `slides/shared_rhythm/week04/monday_moment/` |
| Week 4 Wednesday | `professional_minds/readings/week_04_wed_spelling_out_arguments.md`; Tom Chatfield, “Spelling Out Arguments and Assumptions” | `af54438aeb4bddbbceed4524bc10379b0b9d5a3c` | `slides/shared_rhythm/week04/wacky_wednesday/` |
| Week 4 Friday | `professional_minds/readings/week_04_fri_the_outside_view.md`; Daniel Kahneman, “The Outside View” | `af54438aeb4bddbbceed4524bc10379b0b9d5a3c` | `slides/shared_rhythm/week04/fun_friday/` |
| Week 5 Monday | `ai_fluency/ai_i/monday_moments/week_05_select_the_right_model/` | `022262cf207c28a9504425779a24247ddcf66884` | `slides/shared_rhythm/week05/monday_moment/` |
| Week 5 Wednesday | `professional_minds/readings/week_05_wed_never_judge_a_decision_by_its_outcome.md`; Rolf Dobelli, “Never Judge a Decision by Its Outcome” | `af54438aeb4bddbbceed4524bc10379b0b9d5a3c` | `slides/shared_rhythm/week05/wacky_wednesday/` |
| Week 5 Friday | `professional_minds/readings/week_05_fri_regression_to_the_mean.md`; Jordan Ellenberg, “The Triumph of Mediocrity” | `af54438aeb4bddbbceed4524bc10379b0b9d5a3c` | `slides/shared_rhythm/week05/fun_friday/` |

## Build approach

The six wrappers use `slides/shared_rhythm/shared_rhythm_deck.tex` and `shared_rhythm_notes.tex`, while retaining the accepted `commons-week2-theme.sty`. Each session keeps a 10-slide projector arc: essential question, mental model, worked example, student move, evidence/limits, recovery, and receipt. Each notes PDF mirrors all ten slide numbers and adds podium prompts plus a session-specific study/source block.

Compilation is two `pdflatex -interaction=nonstopmode -halt-on-error` passes per source. Prompt 012 produces repository artifacts only; Canvas is not part of this deployment.
