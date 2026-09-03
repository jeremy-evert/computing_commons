[CmdletBinding()]
param(
    [string]$DocumentName = 'hello',
    [string]$Title = 'Hello, LaTeX!',
    [string]$Author = 'Jeremy Evert',
    [switch]$Force,
    [switch]$SkipOpen
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Write-Step {
    param([string]$Message)
    Write-Host "[LATEX] $Message" -ForegroundColor Cyan
}

function Refresh-ProcessPath {
    $machinePath = [Environment]::GetEnvironmentVariable('Path', 'Machine')
    $userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
    $env:Path = @($machinePath, $userPath) -join ';'
}

function Find-LaTeXCommand {
    param([Parameter(Mandatory)][string]$Name)

    $command = Get-Command $Name -ErrorAction SilentlyContinue
    if ($command) {
        return $command.Source
    }

    $knownRoots = @(
        (Join-Path $env:ProgramFiles 'MiKTeX\miktex\bin\x64'),
        (Join-Path $env:LOCALAPPDATA 'Programs\MiKTeX\miktex\bin\x64')
    )

    foreach ($root in $knownRoots) {
        $candidate = Join-Path $root "$Name.exe"
        if (Test-Path -LiteralPath $candidate) {
            if (($env:Path -split ';') -notcontains $root) {
                $env:Path = "$root;$env:Path"
            }
            return $candidate
        }
    }

    return $null
}

function Install-MiKTeXIfNeeded {
    if (Find-LaTeXCommand -Name 'pdflatex') {
        return
    }

    Write-Warning 'pdflatex was not found. A LaTeX distribution is required.'
    $winget = Get-Command winget -ErrorAction SilentlyContinue

    if (-not $winget) {
        throw @'
pdflatex and winget were not found.
Install the Basic MiKTeX distribution from https://miktex.org/download,
then close and reopen PowerShell and run this script again.
'@
    }

    Write-Step 'Starting a per-user MiKTeX installation with winget.'
    & $winget.Source install --id MiKTeX.MiKTeX --exact --source winget --scope user --accept-package-agreements --accept-source-agreements
    if ($LASTEXITCODE -ne 0) {
        throw "winget could not install MiKTeX. winget exit code: $LASTEXITCODE"
    }

    Refresh-ProcessPath

    if (-not (Find-LaTeXCommand -Name 'pdflatex')) {
        throw @'
MiKTeX appears to have installed, but pdflatex is not visible to this PowerShell process.
Close PowerShell, open it again, return to this directory, and rerun this script.
'@
    }
}

function ConvertTo-LaTeXText {
    param([Parameter(Mandatory)][string]$Text)

    $builder = [Text.StringBuilder]::new()
    foreach ($character in $Text.ToCharArray()) {
        $replacement = switch ($character) {
            '\' { '\textbackslash{}'; break }
            '&'  { '\&'; break }
            '%'  { '\%'; break }
            '$'  { '\$'; break }
            '#'  { '\#'; break }
            '_'  { '\_'; break }
            '{'  { '\{'; break }
            '}'  { '\}'; break }
            default { [string]$character }
        }
        [void]$builder.Append($replacement)
    }
    return $builder.ToString()
}

if ($env:OS -ne 'Windows_NT') {
    throw 'This bootstrap script is designed for Windows PowerShell or PowerShell on Windows.'
}

if ($DocumentName -notmatch '^[A-Za-z0-9][A-Za-z0-9_-]*$') {
    throw 'DocumentName may contain only letters, numbers, underscores, and hyphens.'
}

Write-Step 'Checking the LaTeX toolchain.'
Install-MiKTeXIfNeeded

$requiredCommands = @('pdflatex')
$optionalCommands = @('xelatex', 'lualatex', 'latexmk')
$toolStatus = [System.Collections.Generic.List[object]]::new()

foreach ($name in $requiredCommands + $optionalCommands) {
    $path = Find-LaTeXCommand -Name $name
    $toolStatus.Add([pscustomobject]@{
        Command = $name
        Required = ($requiredCommands -contains $name)
        Status = if ($path) { 'FOUND' } else { 'MISSING' }
        Path = if ($path) { $path } else { '' }
    })
}

$toolStatus | Format-Table -AutoSize

$pdflatex = Find-LaTeXCommand -Name 'pdflatex'
if (-not $pdflatex) {
    throw 'pdflatex is required, but it is still unavailable.'
}

$texPath = Join-Path (Get-Location) "$DocumentName.tex"
$pdfPath = Join-Path (Get-Location) "$DocumentName.pdf"
$gitIgnorePath = Join-Path (Get-Location) '.gitignore'
$reportPath = Join-Path (Get-Location) 'latex_environment_report.md'

if ((Test-Path -LiteralPath $texPath) -and -not $Force) {
    Write-Step "$DocumentName.tex already exists, so it will not be overwritten. Use -Force to replace it."
}
else {
    $safeTitle = ConvertTo-LaTeXText -Text $Title
    $safeAuthor = ConvertTo-LaTeXText -Text $Author

    $latexSource = @"
\documentclass[12pt]{article}

\usepackage[T1]{fontenc}
\usepackage[margin=1in]{geometry}
\usepackage{lmodern}

\title{$safeTitle}
\author{$safeAuthor}
\date{\today}

\begin{document}

\maketitle

\section{Our First Section}

Hello, world! This document was created and compiled from PowerShell.

\section{The Build Pipeline}

The file \texttt{$DocumentName.tex} is plain-text source code. The file
\texttt{$DocumentName.pdf} is the compiled durable artifact.

\begin{itemize}
    \item Git can track meaningful changes to the source.
    \item LaTeX controls document structure and typesetting.
    \item The PDF can be rebuilt from the command line.
\end{itemize}

\section{A Tiny Bit of Mathematics}

\[
    a^2 + b^2 = c^2
\]

\end{document}
"@

    [IO.File]::WriteAllText($texPath, $latexSource, [Text.UTF8Encoding]::new($false))
    Write-Step "Created $texPath"
}

$ignoreEntries = @(
    '*.aux', '*.fdb_latexmk', '*.fls', '*.log', '*.out',
    '*.synctex.gz', '*.toc', '*.xdv'
)

$existingIgnore = if (Test-Path -LiteralPath $gitIgnorePath) {
    [IO.File]::ReadAllText($gitIgnorePath)
} else {
    ''
}

$missingEntries = $ignoreEntries | Where-Object {
    $existingIgnore -notmatch "(?m)^$([regex]::Escape($_))$"
}

if ($missingEntries) {
    $addition = if ([string]::IsNullOrWhiteSpace($existingIgnore)) {
        "# LaTeX build artifacts`r`n" + ($missingEntries -join "`r`n") + "`r`n"
    } else {
        "`r`n# LaTeX build artifacts`r`n" + ($missingEntries -join "`r`n") + "`r`n"
    }
    [IO.File]::AppendAllText($gitIgnorePath, $addition, [Text.UTF8Encoding]::new($false))
    Write-Step 'Updated .gitignore without replacing existing rules.'
}

Write-Step "Compiling $DocumentName.tex with pdflatex."
& $pdflatex -interaction=nonstopmode -halt-on-error -file-line-error $texPath
$compileExitCode = $LASTEXITCODE

$reportLines = [System.Collections.Generic.List[string]]::new()
$reportLines.Add('# LaTeX Environment Report')
$reportLines.Add('')
$reportLines.Add("- Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss K')")
$reportLines.Add("- Computer: $env:COMPUTERNAME")
$reportLines.Add("- PowerShell: $($PSVersionTable.PSVersion)")
$reportLines.Add("- Working directory: $(Get-Location)")
$reportLines.Add("- Source: $texPath")
$reportLines.Add("- Expected PDF: $pdfPath")
$reportLines.Add("- Compiler exit code: $compileExitCode")
$reportLines.Add('')
$reportLines.Add('## Toolchain')
$reportLines.Add('')
$reportLines.Add('| Command | Required | Status | Path |')
$reportLines.Add('|---|---:|---|---|')
foreach ($tool in $toolStatus) {
    $cleanPath = $tool.Path.Replace('|', '\|')
    $reportLines.Add("| $($tool.Command) | $($tool.Required) | $($tool.Status) | $cleanPath |")
}
$reportLines.Add('')
$reportLines.Add('## Result')
$reportLines.Add('')
if (($compileExitCode -eq 0) -and (Test-Path -LiteralPath $pdfPath)) {
    $reportLines.Add('- PASS: The PDF was created successfully.')
} else {
    $reportLines.Add('- FAIL: The PDF was not created successfully. Inspect the console output and the LaTeX log file.')
}

[IO.File]::WriteAllLines($reportPath, $reportLines, [Text.UTF8Encoding]::new($false))
Write-Step "Wrote $reportPath"

if (($compileExitCode -ne 0) -or -not (Test-Path -LiteralPath $pdfPath)) {
    throw "LaTeX compilation failed. Inspect $DocumentName.log and $reportPath"
}

Write-Host ''
Write-Host '[SUCCESS] LaTeX is ready and the PDF was built.' -ForegroundColor Green
Write-Host "Source: $texPath"
Write-Host "PDF:    $pdfPath"
Write-Host "Report: $reportPath"

if (-not $SkipOpen) {
    Invoke-Item -LiteralPath $pdfPath
}
