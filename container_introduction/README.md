# Getting Started with Containers

This folder contains a chapter-based LaTeX book for introducing containers with Podman. The source is deliberately small, readable, and friendly to version control.

## Project layout

```text
container_introduction/
|-- main.tex                 # Book structure and chapter order
|-- preamble.tex             # Packages, colors, and shared commands
|-- Makefile                 # Build, watch, and clean targets
|-- README.md                # These instructions
|-- .gitignore               # Generated LaTeX files
|-- chapters/                # One source file per chapter
|-- images/                  # Diagrams and screenshots
|-- scripts/                 # Future supporting scripts
`-- build/                   # Generated PDF and temporary build files
```

## Prerequisites

You need a working LaTeX distribution that provides `latexmk` and `pdflatex`. The Makefile also expects `make` and a POSIX-style shell. On Windows, those pieces may come from Git Bash, WSL, MSYS2, or another development environment.

Check the tools before building:

```powershell
latexmk -version
pdflatex --version
make --version
```

If `make` is unavailable but `latexmk` works, use the direct PowerShell build command below.

## Build from PowerShell

From this folder, run:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

The finished document will be:

```text
build/main.pdf
```

Open it from PowerShell with:

```powershell
Invoke-Item .\build\main.pdf
```

## Build with Make

From a shell with `make`, run:

```text
make
```

Useful targets:

```text
make pdf      Build the PDF once
make watch    Rebuild when a source file changes
make clean    Remove generated build files
```

## Writing workflow

1. Edit one file in `chapters/`.
2. Build the book.
3. Read the first LaTeX error, not the last avalanche of errors.
4. Fix one cause at a time.
5. Commit source files and durable evidence, not generated clutter.

To change chapter order, edit the `\\include{...}` lines in `main.tex`. To add a chapter, create a new `.tex` file in `chapters/` and add one matching `\\include{...}` line to `main.tex`.

## Re-run the scaffold script

The setup script writes a known clean scaffold and overwrites files with the same names. Run it only when you intentionally want to reset this starter structure:

```powershell
powershell -ExecutionPolicy Bypass -File .\setup_container_introduction.ps1
```

## First editing target

Start with:

```text
chapters/01-what-is-a-container.tex
```

The stubs use `% TODO:` comments as visible landing zones. Replace each comment with tested explanations, examples, command output, and reflection prompts as the lesson develops.