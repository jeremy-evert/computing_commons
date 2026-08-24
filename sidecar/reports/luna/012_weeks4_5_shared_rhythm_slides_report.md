# Prompt 012 — Weeks 4–5 shared-rhythm slide factory report

## Verdict

**WEEKS 4–5 M/W/F SLIDE FACTORY READY FOR GRACE REVIEW**

Prompt 012 continued only after Prompt 011’s Home/Teacher’s Table acceptance and exact Savnac readback. It produced repository artifacts only; Canvas was not changed by this continuation.

## Six projector decks and six notes PDFs

| Session | Projector source / PDF | Notes source / PDF |
|---|---|---|
| Week 4 Monday — AI Fluency: Decompose the Task | `slides/shared_rhythm/week04/monday_moment/week04_monday_decompose.tex` / `.pdf` | matching `_notes.tex` / `.pdf` |
| Week 4 Wacky Wednesday — Mapping Arguments for Better Decisions | `slides/shared_rhythm/week04/wacky_wednesday/week04_wednesday_arguments.tex` / `.pdf` | matching `_notes.tex` / `.pdf` |
| Week 4 Fun Friday — The Outside View | `slides/shared_rhythm/week04/fun_friday/week04_friday_outside_view.tex` / `.pdf` | matching `_notes.tex` / `.pdf` |
| Week 5 Monday — AI Fluency: Select the Right Model | `slides/shared_rhythm/week05/monday_moment/week05_monday_model.tex` / `.pdf` | matching `_notes.tex` / `.pdf` |
| Week 5 Wacky Wednesday — Outcome Bias | `slides/shared_rhythm/week05/wacky_wednesday/week05_wednesday_outcome_bias.tex` / `.pdf` | matching `_notes.tex` / `.pdf` |
| Week 5 Fun Friday — Regression to the Mean | `slides/shared_rhythm/week05/fun_friday/week05_friday_regression.tex` / `.pdf` | matching `_notes.tex` / `.pdf` |

Each projector deck is 10 slides in 16:9 format. Each instructor-notes PDF is 11 letter pages: study-before-class plus one podium entry for each projector slide. Each session directory has a README with its exact source and pinned commit.

## Source pins

- Week 4/5 Monday AI Fluency packages: `jeremy-evert/ai_fluency`, commit `022262cf207c28a9504425779a24247ddcf66884`.
- Week 4/5 Wednesday/Friday Professional Minds readings and source evidence: `jeremy-evert/professional_minds`, commit `af54438aeb4bddbbceed4524bc10379b0b9d5a3c`.
- Book-backed sessions preserve the named books/chapters and distinguish source claims from instructor-created computing examples. The Week 5 Friday notes preserve the historical-material limitation.

## Verification

- Every source compiled twice with `pdflatex -interaction=nonstopmode -halt-on-error`.
- All 12 PDFs exist and are non-empty; receipt: `sidecar/evidence/012_slide_factory_receipt.json`.
- Representative rendered pages from Week 4 Friday and Week 5 Friday were inspected for hierarchy, readability, density, and clipping.
- Grace helper: `scripts/grace/review-weeks4-5-shared-rhythm-slides.ps1`.
- Shared factory: `slides/shared_rhythm/shared_rhythm_deck.tex` and `shared_rhythm_notes.tex`; accepted theme reused from `slides/week2_local_ai_workbench/commons-week2-theme.sty`.

## Boundaries

- No Week 4/5 slide artifact deployed to Canvas.
- Savnac course 18 was not mutated by Prompt 012; SWOSU production Canvas course 24298 was untouched.
- Canonical `ai_fluency`, `professional_minds`, and `swosu_cs_curriculum` repositories were read-only and unchanged.
- Quick Tune and synthetic students did not run.
