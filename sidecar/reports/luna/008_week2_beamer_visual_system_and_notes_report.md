# Report: Week 2 Beamer visual system and instructor notes

## Result

Refined the accepted Week 2 deck into a 25-slide projected teaching instrument. The deck preserves the accepted curriculum and canonical local-only boundary while separating dense evidence material into before-action, after-action, and bounded-conclusion slides. A dedicated security/judgment slide distinguishes loopback reachability from application configuration, data handling, authentication, correctness, and overall security.

## Deliverables

- Projected source: `slides/week2_local_ai_workbench/week2_local_ai_workbench.tex`
- Projected PDF: `slides/week2_local_ai_workbench/week2_local_ai_workbench.pdf` (25 pages)
- Reusable visual system: `slides/week2_local_ai_workbench/commons-week2-theme.sty`
- Instructor notes source: `slides/week2_local_ai_workbench/week2_local_ai_workbench_notes.md`
- Instructor notes build source: `slides/week2_local_ai_workbench/week2_local_ai_workbench_notes.tex`
- Instructor notes PDF: `slides/week2_local_ai_workbench/week2_local_ai_workbench_notes.pdf` (26 pages: title page plus 25 slide sections)
- Grace helper: `scripts/grace/review-week2-slides.ps1`

## Build and validation

From `slides/week2_local_ai_workbench/`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error week2_local_ai_workbench.tex
pdflatex -interaction=nonstopmode -halt-on-error week2_local_ai_workbench.tex
pdflatex -interaction=nonstopmode -halt-on-error week2_local_ai_workbench_notes.tex
pdflatex -interaction=nonstopmode -halt-on-error week2_local_ai_workbench_notes.tex
```

Both PDFs compiled successfully. `pdfinfo` reports 25 projected pages and 26 notes pages. The projected deck was rendered and checked as representative families: navy hero/transition, columns/cards, stack diagram, split evidence sequence, loopback/security material, recovery, and final receipt. The source retains only sanitized generic Windows examples and no personal identity, host, credential, Canvas, or cloud-provider material. The accepted `ollama_chat/qwen3:8b`, `http://127.0.0.1:11434`, and `num_ctx: 8192` boundary remains intact.

The compiler reported existing-style overfull-box warnings on a few dense legacy lines; there were no LaTeX errors and the PDF is produced. These should receive ordinary owner projector review, with the split evidence/security slides prioritized.

`git diff --check` is required before commit.

## Grace review usage

From a clean checkout, run exactly:

```powershell
.\scripts\grace\review-week2-slides.ps1
```

It refuses dirty state, confirms both PDFs, prints the commit/path receipt, and opens both files. It does not pull or deploy.

## Canvas follow-up

No Canvas deployment was performed. Consider separate self-paced pages for evidence before model action, evidence after model action, and the security/judgment questions so exact recovery and command detail remain durable without overloading projection.

## Owner review questions

1. Are the remaining dense legacy slides readable at the intended classroom projector distance?
2. Should the owner prefer the three-part evidence sequence as a live discussion pause or as one continuous segment?

WEEK 2 VISUAL DECK + INSTRUCTOR NOTES READY FOR OWNER REVIEW
