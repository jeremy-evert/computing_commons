# Week 2 Local AI Workbench deck

Instructor-facing/student-facing Beamer deck for the Computing Commons Week 2 Local AI Lab. It teaches the local stack as layers and repeats the evidence ladder:

`DO THIS → WHAT THIS MEANS → FIND THIS YOURSELF → DEMAND DOCUMENTATION → VERIFY ON YOUR MACHINE → KEEP THE RECEIPT`

## Build

From this directory on Brandy:

```bash
pdflatex -interaction=nonstopmode -halt-on-error week2_local_ai_workbench.tex
pdflatex -interaction=nonstopmode -halt-on-error week2_local_ai_workbench.tex
```

The source uses standard TeX Live packages only and produces a 16:9, 25-page PDF. The PDF is checked into this repository as a review artifact; do not upload it to Canvas from this mission. The reusable visual grammar lives in `commons-week2-theme.sty`.

Instructor notes are maintained in `week2_local_ai_workbench_notes.md` and compiled from `week2_local_ai_workbench_notes.tex` to a 26-page printable PDF (title page plus one section per projected slide).

## Teaching route

Slides 1–7 establish the finish line, infrastructure rationale, stack, and split evidence rule. Slides 8–15 orient beginners to PowerShell, Python, Git, Ollama, the security judgment questions, exact `qwen3:8b` boundary, and Aider. Slides 16–20 model the bounded edit, diff/test separation, repeated loop, and recovery. Slides 21–24 fade the scaffold into prompt structure, learning-to-fish, Work First, and the final receipt. The last slide is a clean transition to student work.

## Source relationships

Technical claims were reconciled against the current local sources:

- `instructor/week2_aider_work_first_teaching_guide.md`
- current Computing Commons Week 2 previews and curriculum
- read-only `local_ai_lab_setup/docs/week2_module_plan.md`, `docs/architecture.md`, and `instructor/week2_teaching_notes.md`
- read-only `windows_classroom/docs/week2_instructor_runbook.md` and `docs/week2_student_guide.md`
- `swosu_cs_curriculum/shared/philosophy/computing_tool_access_is_curriculum_infrastructure.md`

The deck intentionally does not invent installation, provisioning, model-download, cloud, or endpoint procedures. It stops at owner review.

## Update notes

The accepted local boundary is `ollama_chat/qwen3:8b` at `http://127.0.0.1:11434` with the reviewed `num_ctx: 8192` setting. If canonical guidance changes, update the source contract and this deck together.
