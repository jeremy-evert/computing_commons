# Fun with LaTeX — Your First Document That Builds Itself

**Recitation Toolbox station: Documentation and LaTeX.**
Question: **Can another human understand and inspect what I did?**

This guide walks you through exactly what Jeremy did in the recorded
walkthrough: stand up a tiny LaTeX project on your own machine, compile a
plain-text source file into a PDF, and put both under Git — then get to a
one-word build command (`make`) without pretending your toolchain is
something it isn't.

You do **not** need to already know LaTeX. You need PowerShell, Git, and about
thirty minutes.

---

## Watch the walkthrough

**Video (SWOSU sign-in required):**
<https://swosuits-my.sharepoint.com/:v:/g/personal/evertj_swosu_edu/IQBXxk89HZUCT78QAnL83M3RAUHZlcL6TWu2LCBdtHH0YSs?e=YnhBDo>

It is a real screen recording, snags included: `latexmk` needing Perl, a
cleanup step that fails on missing files, and the decision to *remove*
machinery instead of adding more. The point of the video is not a clean demo.
The point is what a build pipeline actually feels like the first time, and how
you recover.

**Companion slides:** [`slides/fun_with_latex.pdf`](slides/fun_with_latex.pdf)

---

## The idea in one sentence

> `hello.tex` is **source code**. `hello.pdf` is a **build artifact**. Git
> tracks the source; one command rebuilds the artifact; another machine can
> reproduce the same PDF from the same source.

That is the whole lesson. LaTeX is just the concrete example.

---

## 1. Predict before you run anything

You are about to turn a text file into a PDF with a command-line program.
Before you start, write down your answers to these:

1. If `hello.tex` is the source and `hello.pdf` is built from it, **which file
   belongs in Git** and which one could you always regenerate?
2. A build tool exists on your machine (`pdflatex.exe` is on disk). Does the
   file existing on disk prove the tool actually *works*?
3. If a build step tries to delete four temporary files and only two of them
   exist, should that step **succeed** or **fail**?

Keep your answers. Section 6 comes back to them.

---

## 2. Open PowerShell and get to a working folder

If you have never opened PowerShell: press the **Windows key**, type
`powershell`, and press **Enter**. A dark window with a blinking prompt
appears. That prompt is where every command below goes.

```powershell
# Go to (or make) a "git" folder in your user directory
cd ~
mkdir git -Force
cd git

# Get the Computing Commons repository
git clone https://github.com/jeremy-evert/computing_commons.git
cd computing_commons\fun_with_LaTeX
```

**What this means.** `cd` changes directory; `~` is your user folder;
`git clone` copies a repository from GitHub to your machine. You are now
standing in the `fun_with_LaTeX` folder of your own copy of the repo.

**Find this yourself.** Run `Get-Location` (or `pwd`). The path it prints is
where your files will land. Run `ls`. You should see
`bootstrap_latex_project.ps1`.

---

## 3. Run the bootstrap script once

```powershell
.\bootstrap_latex_project.ps1
```

**What this does**, in order:

1. **Checks the LaTeX toolchain.** It looks for `pdflatex` (required) and
   `xelatex`, `lualatex`, `latexmk` (optional) and prints a table showing
   which were `FOUND` and where.
2. **Installs MiKTeX for you** *only if* `pdflatex` is missing, using `winget`.
   If MiKTeX is already there, it skips this.
3. **Writes `hello.tex`** if it does not already exist (it will not overwrite
   your edits).
4. **Adds LaTeX build junk to `.gitignore`** (`*.aux`, `*.log`, `*.out`, ...)
   without disturbing rules already there.
5. **Compiles `hello.tex` with `pdflatex`** using
   `-interaction=nonstopmode -halt-on-error -file-line-error`.
6. **Writes `latex_environment_report.md`** — a receipt: which computer, which
   PowerShell, which tools, and the compiler's exit code.

**Success looks like this** (last lines of the output):

```
[SUCCESS] LaTeX is ready and the PDF was built.
Source: ...\fun_with_LaTeX\hello.tex
PDF:    ...\fun_with_LaTeX\hello.pdf
Report: ...\fun_with_LaTeX\latex_environment_report.md
```

**Demand documentation.** You will also see one scary-looking line:

```
pdflatex: major issue: So far, no MiKTeX administrator has checked for updates.
```

That is a **warning, not a failure** — the PDF was still produced. When you
have a few minutes, open **MiKTeX Console** and check for updates. Do not let
a warning convince you a successful build failed.

---

## 4. Open the PDF you just built

```powershell
Start-Process .\hello.pdf
```

You should see a one-page document: a title, your name, today's date, three
short sections, and the line `a^2 + b^2 = c^2` typeset as real mathematics.

**Verify on your machine.** Open `latex_environment_report.md` in an editor.
Confirm `Compiler exit code: 0` and that `pdflatex` shows `FOUND`. That file
is your evidence the build worked *here*, on *your* computer.

---

## 5. Edit the source, rebuild, see the change

Open the source in your editor:

```powershell
code .\hello.tex
```

Change something small and true — add a sentence to a section, or add a new
bullet to the list. Save. Then rebuild with the exact command the bootstrap
used:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error hello.tex
Start-Process .\hello.pdf
```

The PDF changes. **That loop — edit source, run one command, inspect the
artifact — is the entire skill.**

---

## 6. The Makefile detour: what broke, and why subtraction fixed it

Typing that long `pdflatex` line every time is tedious, so the natural next
move is a `Makefile` so you can just type `make`. In the video this took a few
tries. The failures are the lesson.

### Snag 1 — `latexmk` needs Perl

The first `Makefile` called `latexmk`. `latexmk.exe` **was on disk**, so it
looked usable. It is not — on MiKTeX it is a wrapper that still needs a Perl
interpreter, and Perl was not installed:

```
MiKTeX could not find the script engine 'perl' which is required to execute 'latexmk'.
```

**Answer to prediction #2:** finding an executable does not prove its
dependencies are satisfied. `pdflatex` alone already builds this document, so
the fix was to call `pdflatex` directly and not depend on Perl at all.

### Snag 2 — cleanup that fails when there is nothing to clean

The next `Makefile` had a `clean` step that deleted `*.aux`, `*.log`, `*.out`,
`*.toc`, `*.synctex.gz`. When some of those files did not exist, the cleanup
command returned a non-zero exit code, and `make` correctly treated that as a
failed step:

```
make: *** [Makefile:32: clean] Error 1
```

Because `rebuild` depended on `clean`, a harmless "nothing to delete" stopped
the build before `pdflatex` ever ran.

**Answer to prediction #3:** "delete these files if they exist" should
*succeed* when they are already gone. The recipe was asking a tool to remove
files that were not there and treating the complaint as fatal.

### The fix was to remove machinery, not add it

The working `Makefile` is four functional lines — only commands proven to work
in the video:

```make
.PHONY: all

all:
	pdflatex -interaction=nonstopmode -halt-on-error -file-line-error hello.tex
	powershell.exe -NoProfile -Command "Start-Process -FilePath (Resolve-Path 'hello.pdf')"
```

`make` now compiles the document and opens the PDF. No `latexmk`, no Perl, no
cleanup target, no dependency graph. (The indentation before each command must
be a real **tab** — `make` requires it.)

> **Start with the command that works. Automate that command. Add complexity
> only when the project demonstrates a real need for it.**

---

## 7. Keep the receipt (Git)

At each working step in the video, the change was committed and pushed:

```powershell
git status
git add .\hello.tex .\hello.pdf .\Makefile
git diff --cached --stat
git commit -m "docs: revise LaTeX example"
git pull --rebase
git push
git status        # ends: "working tree clean"
```

Two things worth noticing:

- The Git history now records **both** the failed `latexmk` abstraction and
  the simpler repair. That is real engineering history, not something to hide.
- `git diff --cached` reports on **content**. If a file you thought you edited
  is not in the staged diff, its contents already match what is committed —
  Git is telling the truth regardless of what you remember doing.

---

## 8. The finish line

You are done when you can honestly say:

> I turned a plain-text file into a PDF on my own machine with one command. I
> can point to `latex_environment_report.md` as evidence it built here. I know
> which file is source and which is the artifact, and I have both under Git. I
> hit a build failure, read the actual error, removed the part that did not
> earn its place, and got to a working `make`.

Not "LaTeX is installed." Not "the command exited, so it must be right." Open
the artifact and check that it is what you meant to produce.

---

## If something goes wrong

| Symptom | Most likely cause | Do this |
| --- | --- | --- |
| `pdflatex` / `.ps1` "not recognized" | MiKTeX not on this shell's PATH yet | Close PowerShell, reopen it, `cd` back, try again |
| `winget` not found during install | No winget on this machine | Install **Basic MiKTeX** from <https://miktex.org/download>, reopen PowerShell, rerun the script |
| `... script engine 'perl' ... required to execute 'latexmk'` | A recipe is calling `latexmk` | Use `pdflatex` directly (Section 6, Snag 1) |
| `make: *** [Makefile:NN: clean] Error 1` | Cleanup step fails on missing files | Drop the cleanup target; use the four-line `Makefile` (Section 6) |
| `make` complains about "missing separator" | Recipe lines indented with spaces | Re-indent recipe lines with a real **tab** |
| `no MiKTeX administrator has checked for updates` | Informational warning only | Ignore for now; check updates in MiKTeX Console later |
| Editor `code` not found | VS Code not on PATH | Open the file from VS Code's **File → Open**, or install "code" command from VS Code |

---

## Canonical sources

- [`bootstrap_latex_project.ps1`](bootstrap_latex_project.ps1) — the script
  you run; toolchain check, optional MiKTeX install, `hello.tex`,
  `.gitignore`, compile, environment report.
- [`hello.tex`](hello.tex) / [`hello.pdf`](hello.pdf) — the source and the
  artifact it builds.
- [`Makefile`](Makefile) — the four-line `make` target, built only from
  commands proven in the walkthrough.
- [`slides/fun_with_latex.pdf`](slides/fun_with_latex.pdf) — companion deck.
- [`../curriculum/recitation-toolbox.md`](../curriculum/recitation-toolbox.md)
  — where the Documentation and LaTeX station lives in the Commons.
