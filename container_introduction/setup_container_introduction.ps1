[CmdletBinding()]
param(
    [string]$ProjectRoot = (Get-Location).Path
)

$ErrorActionPreference = 'Stop'
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function Write-ProjectFile {
    param(
        [Parameter(Mandatory = $true)][string]$RelativePath,
        [Parameter(Mandatory = $true)][string]$Content
    )

    $fullPath = Join-Path $ProjectRoot $RelativePath
    $parent = Split-Path -Parent $fullPath
    if ($parent) {
        [System.IO.Directory]::CreateDirectory($parent) | Out-Null
    }
    [System.IO.File]::WriteAllText($fullPath, $Content, $utf8NoBom)
    Write-Host "WROTE  $RelativePath"
}

[System.IO.Directory]::CreateDirectory($ProjectRoot) | Out-Null
@('chapters', 'images', 'build', 'scripts') | ForEach-Object {
    [System.IO.Directory]::CreateDirectory((Join-Path $ProjectRoot $_)) | Out-Null
}

Write-ProjectFile 'main.tex' @'
\documentclass[11pt,oneside]{book}

\input{preamble}

\title{Getting Started with Containers}
\author{Jeremy Evert}
\date{\today}

\begin{document}

\frontmatter
\maketitle
\tableofcontents

\mainmatter
\include{chapters/01-what-is-a-container}
\include{chapters/02-why-containers-exist}
\include{chapters/03-prove-podman-works}
\include{chapters/04-run-your-first-container}
\include{chapters/05-read-a-containerfile}
\include{chapters/06-build-an-image}
\include{chapters/07-container-lifecycle}
\include{chapters/08-storage-and-networking}
\include{chapters/09-troubleshooting}
\include{chapters/10-next-steps}

\backmatter
\chapter*{Command Reference}
\addcontentsline{toc}{chapter}{Command Reference}
Keep a concise, tested command reference here as the document develops.

\end{document}
'@

Write-ProjectFile 'preamble.tex' @'
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[margin=1in]{geometry}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{listings}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage{microtype}

\definecolor{codebg}{HTML}{F5F7FA}
\definecolor{codeframe}{HTML}{CBD5E1}
\definecolor{codegreen}{HTML}{166534}
\definecolor{codeblue}{HTML}{1D4ED8}

\hypersetup{
  colorlinks=true,
  linkcolor=codeblue,
  urlcolor=codeblue,
  pdftitle={Getting Started with Containers},
  pdfauthor={Jeremy Evert}
}

\lstset{
  basicstyle=\ttfamily\small,
  backgroundcolor=\color{codebg},
  frame=single,
  rulecolor=\color{codeframe},
  breaklines=true,
  columns=fullflexible,
  keepspaces=true,
  showstringspaces=false,
  keywordstyle=\color{codeblue}\bfseries,
  commentstyle=\color{codegreen}
}

\newcommand{\term}[1]{\textbf{#1}}
\newcommand{\checkpoint}[1]{\par\medskip\noindent\textbf{Checkpoint:} #1\par\medskip}
'@

$chapters = [ordered]@{
    'chapters/01-what-is-a-container.tex' = @'
\chapter{What Is a Container?}
\label{chap:what-is-a-container}

For today, use this working definition:

\begin{quote}
A container is a packaged environment that carries what a program needs to run.
\end{quote}

\section{Learning goals}
\begin{itemize}
  \item Distinguish a container, an image, and a container engine.
  \item Explain what a container packages and what it shares with the host.
\end{itemize}

\section{The central idea}
% TODO: Add the beginner-friendly explanation and analogy.

\checkpoint{Explain a container in your own words without using the word ``container.''}
'@
    'chapters/02-why-containers-exist.tex' = @'
\chapter{Why Containers Exist}
\label{chap:why-containers-exist}

\section{Learning goals}
\begin{itemize}
  \item Describe the problem containers were designed to address.
  \item Connect repeatability, isolation, and portability to real workflows.
\end{itemize}

\section{From ``works on my machine'' to a repeatable environment}
% TODO: Add a brief history and motivation.

\section{Guiding principles}
% TODO: Discuss small, reproducible, disposable, and observable systems.
'@
    'chapters/03-prove-podman-works.tex' = @'
\chapter{Prove Podman Works}
\label{chap:prove-podman-works}

Before building anything, ask the computer what it knows.

\begin{lstlisting}[language=bash]
podman --version
podman info
\end{lstlisting}

\section{What evidence should we keep?}
% TODO: Explain what successful output looks like and what to record.

\checkpoint{Save the command output before changing the system. Failures are data.}
'@
    'chapters/04-run-your-first-container.tex' = @'
\chapter{Run Your First Container}
\label{chap:first-container}

\section{Pull and run}
% TODO: Add the first deliberately small Podman command.

\section{Observe the result}
% TODO: Separate what the image supplied from what the container did.

\checkpoint{Identify the image name, command, output, and exit status.}
'@
    'chapters/05-read-a-containerfile.tex' = @'
\chapter{Read a Containerfile}
\label{chap:containerfile}

Our first Containerfile can be almost absurdly small.

\begin{lstlisting}
FROM alpine:latest
CMD ["echo", "Hello, world!"]
\end{lstlisting}

\section{Read it one line at a time}
% TODO: Explain FROM and CMD without adding unnecessary machinery.
'@
    'chapters/06-build-an-image.tex' = @'
\chapter{Build an Image}
\label{chap:build-image}

\section{Build}
% TODO: Add the image-build command and explain the build context.

\section{Verify}
% TODO: Inspect the image list, run the image, and preserve evidence.

\checkpoint{Can another person reproduce the same image from the repository?}
'@
    'chapters/07-container-lifecycle.tex' = @'
\chapter{The Container Lifecycle}
\label{chap:lifecycle}

\section{Create, start, stop, inspect, and remove}
% TODO: Develop a lifecycle exercise using one small container.

\section{Disposable does not mean mysterious}
% TODO: Emphasize observation and retained artifacts.
'@
    'chapters/08-storage-and-networking.tex' = @'
\chapter{Storage and Networking}
\label{chap:storage-networking}

\section{Ephemeral and persistent data}
% TODO: Introduce bind mounts and volumes carefully.

\section{Ports and service access}
% TODO: Introduce port publishing with a minimal example.

\checkpoint{State which data should survive after a container is removed.}
'@
    'chapters/09-troubleshooting.tex' = @'
\chapter{Troubleshooting Without Guessing}
\label{chap:troubleshooting}

\section{Establish the world state}
% TODO: Build a short diagnostic sequence: version, info, images, containers, logs.

\section{Keep evidence}
% TODO: Explain how command, output, environment, and hypothesis form a useful report.

\checkpoint{Record what happened before attempting a fix.}
'@
    'chapters/10-next-steps.tex' = @'
\chapter{Next Steps}
\label{chap:next-steps}

\section{Practice tasks}
% TODO: Add exercises that change one variable at a time.

\section{Reflection}
% TODO: Ask students what became more repeatable, visible, or portable.
'@
}

foreach ($entry in $chapters.GetEnumerator()) {
    Write-ProjectFile $entry.Key $entry.Value
}

$makefile = @(
    'SHELL := /bin/sh',
    'MAIN := main',
    'BUILD := build',
    '',
    '.PHONY: all pdf clean watch',
    '',
    'all: pdf',
    '',
    'pdf:',
    "`tmkdir -p `$(BUILD)",
    "`tlatexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=`$(BUILD) `$(MAIN).tex",
    '',
    'watch:',
    "`tlatexmk -pdf -pvc -interaction=nonstopmode -outdir=`$(BUILD) `$(MAIN).tex",
    '',
    'clean:',
    "`tlatexmk -C -outdir=`$(BUILD) `$(MAIN).tex",
    "`trm -rf `$(BUILD)"
) -join "`n"
Write-ProjectFile 'Makefile' $makefile

Write-ProjectFile '.gitignore' @'
/build/
*.aux
*.bbl
*.bcf
*.blg
*.fdb_latexmk
*.fls
*.log
*.out
*.run.xml
*.synctex.gz
*.toc
'@

Write-ProjectFile 'README.md' @'
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
'@

Write-Host ''
Write-Host 'Container introduction scaffold created.' -ForegroundColor Green
Write-Host "Project root: $ProjectRoot"
Write-Host 'Next: read README.md, then build with latexmk or make.'
