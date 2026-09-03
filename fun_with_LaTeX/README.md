# Fun with LaTeX

First content for the Computing Commons **Recitation Toolbox → Documentation
and LaTeX** station. Question: *Can another human understand and inspect what I
did?*

A student stands up a tiny LaTeX project on their own machine, compiles a
plain-text `.tex` source into a `.pdf` artifact, puts both under Git, and gets
to a one-word `make` build — working through the real snags (`latexmk` needing
Perl, a cleanup step that fails on missing files) instead of pretending the
toolchain is clean.

## Contents

| File | What it is |
| --- | --- |
| [`STUDENT_GUIDE.md`](STUDENT_GUIDE.md) | The step-by-step student walkthrough. Start here. |
| [`bootstrap_latex_project.ps1`](bootstrap_latex_project.ps1) | Windows/PowerShell bootstrap: toolchain check, optional MiKTeX install, writes `hello.tex`, updates `.gitignore`, compiles, writes an environment report. |
| [`hello.tex`](hello.tex) | The source file. |
| [`hello.pdf`](hello.pdf) | The artifact `hello.tex` builds. |
| [`Makefile`](Makefile) | Four-line `make` target — only commands proven in the walkthrough (no `latexmk`, no Perl). |
| [`latex_environment_report.md`](latex_environment_report.md) | Example environment receipt produced by the bootstrap script. |
| [`slides/`](slides/) | Companion Beamer deck (`fun_with_latex.pdf`, 15 slides). |

## Recorded walkthrough

SWOSU sign-in required:
<https://swosuits-my.sharepoint.com/:v:/g/personal/evertj_swosu_edu/IQBXxk89HZUCT78QAnL83M3RAUHZlcL6TWu2LCBdtHH0YSs?e=YnhBDo>

Real screen recording with the snags left in. See `STUDENT_GUIDE.md` §6 for
what broke and why removing machinery fixed it.

## Build the deck

TeX Live or MiKTeX with `pdflatex`:

```
cd slides
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error fun_with_latex.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error fun_with_latex.tex
```

## Status

| Field | State |
| --- | --- |
| Student guide | drafted, in review |
| Companion deck | authored, compiled (15 slides, 16:9) |
| Recorded walkthrough | recorded; hosted on SWOSU SharePoint; linked above |
| Canvas delivery | owner-authorized 2026-09-03; queued for Flo on april (`jobs/flo/april.yaml`, mission `computing_commons_fun_with_latex_canvas_load`) — one module in course 24298 |
| Cross-course announcement | authorized; posts to CS1 74029, CS2 74031, Computer Architecture 75249, DSCT 74035 after the module readback |
