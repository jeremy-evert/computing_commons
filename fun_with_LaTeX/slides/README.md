# Fun with LaTeX — companion slides

`fun_with_latex.tex` → `fun_with_latex.pdf` (15 slides, 16:9).

Companion deck for the recorded walkthrough and
[`../STUDENT_GUIDE.md`](../STUDENT_GUIDE.md). Uses the Computing Commons visual
grammar (DeepNavy / WarmGold, block / alertblock / exampleblock) established in
`slides/container_level0/`.

## Build

```
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error fun_with_latex.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error fun_with_latex.tex
```

No `latexmk` on purpose — same reason the lesson itself drops it.

## `img/`

Frames lifted from the recorded walkthrough:

| File | Moment |
| --- | --- |
| `bootstrap_success.png` | `bootstrap_latex_project.ps1` — toolchain table + `[SUCCESS] ... the PDF was built` |
| `hello_pdf.png` | the compiled `hello.pdf` open in a viewer |
| `git_receipt.png` | `git add` / `commit` / `pull --rebase` / `push` of the workflow |
| `shipped.png` | the walkthrough's closing "edit → make → hello.pdf → git" summary |

These show a real SWOSU workstation, so filesystem paths include the recorder's
Windows username and machine name. Left as recorded because Jeremy authored and
is publishing this walkthrough himself; swap in cropped/anonymized frames if a
wider audience ever needs it.
