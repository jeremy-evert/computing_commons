[CmdletBinding()]
param(
    [string]$ProjectRoot = $PSScriptRoot,
    [string]$MainFile = 'main.tex',
    [switch]$SkipGit,
    [switch]$OpenPdf
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$started = Get-Date
$script:Raw = New-Object System.Collections.Generic.List[string]
$script:Problems = New-Object System.Collections.Generic.List[string]
$script:Fixes = New-Object System.Collections.Generic.List[string]
$script:Warnings = New-Object System.Collections.Generic.List[string]
$script:BuildPassed = $false
$script:GitPassed = $false
$script:CommitCreated = $false

function Add-Raw([string]$Text) {
    if ($null -ne $Text) { $script:Raw.Add($Text) }
}

function Invoke-Captured {
    param(
        [Parameter(Mandatory=$true)][string]$Label,
        [Parameter(Mandatory=$true)][scriptblock]$Command,
        [switch]$AllowFailure
    )
    Add-Raw ""
    Add-Raw ("===== {0} =====" -f $Label)
    try {
        $savedPreference = $ErrorActionPreference
        $ErrorActionPreference = 'Continue'
        try {
            $output = & $Command 2>&1 | ForEach-Object { $_.ToString() }
            $exit = $LASTEXITCODE
        }
        finally {
            $ErrorActionPreference = $savedPreference
        }
        if ($null -eq $exit) { $exit = 0 }
        foreach ($line in $output) { Add-Raw $line }
        Add-Raw ("[exit code: {0}]" -f $exit)
        if (($exit -ne 0) -and (-not $AllowFailure)) {
            throw "$Label failed with exit code $exit"
        }
        return [pscustomobject]@{ Output = @($output); ExitCode = [int]$exit }
    }
    catch {
        Add-Raw ("[exception: {0}]" -f $_.Exception.Message)
        if (-not $AllowFailure) { throw }
        return [pscustomobject]@{ Output = @($_.Exception.Message); ExitCode = 1 }
    }
}

function Write-Utf8NoBom([string]$Path, [string]$Content) {
    [System.IO.File]::WriteAllText($Path, $Content, $utf8NoBom)
}

Set-Location $ProjectRoot
$ProjectRoot = (Get-Location).Path
$buildDir = Join-Path $ProjectRoot 'build'
$reportsDir = Join-Path $ProjectRoot 'reports'
$mainPath = Join-Path $ProjectRoot $MainFile
$pdfPath = Join-Path $buildDir ([System.IO.Path]::GetFileNameWithoutExtension($MainFile) + '.pdf')
$logPath = Join-Path $buildDir ([System.IO.Path]::GetFileNameWithoutExtension($MainFile) + '.log')
$stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$reportPath = Join-Path $reportsDir ("latex_build_report_{0}.txt" -f $stamp)
$latestReportPath = Join-Path $reportsDir 'latex_build_report_latest.txt'

[System.IO.Directory]::CreateDirectory($buildDir) | Out-Null
[System.IO.Directory]::CreateDirectory($reportsDir) | Out-Null
Add-Raw "LaTeX build and repair report"
Add-Raw ("Started: {0:o}" -f $started)
Add-Raw ("Computer: {0}" -f $env:COMPUTERNAME)
Add-Raw ("PowerShell: {0}" -f $PSVersionTable.PSVersion)
Add-Raw ("Project root: {0}" -f $ProjectRoot)
Add-Raw ("Main source: {0}" -f $mainPath)

try {
    if (-not (Test-Path -LiteralPath $mainPath -PathType Leaf)) {
        $script:Problems.Add("Missing source file: $mainPath")
        throw "Cannot build without $MainFile"
    }

    $pdfLatexCommand = Get-Command pdflatex -ErrorAction SilentlyContinue
    if (-not $pdfLatexCommand) {
        $script:Problems.Add('pdflatex was not found on PATH.')
        throw 'Install or repair MiKTeX, then ensure pdflatex is on PATH.'
    }
    Add-Raw ("pdflatex path: {0}" -f $pdfLatexCommand.Source)
    Invoke-Captured -Label 'pdflatex --version' -Command { pdflatex --version } | Out-Null

    $kpsewhichCommand = Get-Command kpsewhich -ErrorAction SilentlyContinue
    if (-not $kpsewhichCommand) {
        $script:Problems.Add('kpsewhich was not found on PATH.')
        throw 'MiKTeX is incomplete or its bin directory is not on PATH.'
    }

    $packages = @(
        'lmodern.sty','geometry.sty','xcolor.sty','hyperref.sty','listings.sty',
        'graphicx.sty','booktabs.sty','enumitem.sty','microtype.sty'
    )
    foreach ($package in $packages) {
        $check = Invoke-Captured -Label ("kpsewhich {0}" -f $package) -Command { & kpsewhich $package } -AllowFailure
        $resolved = @($check.Output | Where-Object { $_ -and ($_ -notmatch 'major issue') })
        if (($check.ExitCode -ne 0) -or ($resolved.Count -eq 0)) {
            $script:Problems.Add("Required package not found: $package")
        }
    }
    if ($script:Problems | Where-Object { $_ -like 'Required package not found:*' }) {
        $script:Warnings.Add('One or more packages are missing. MiKTeX may install them automatically during compilation if that option is enabled.')
    }

    $makefilePath = Join-Path $ProjectRoot 'Makefile'
    if (Test-Path -LiteralPath $makefilePath) {
        $makeText = [System.IO.File]::ReadAllText($makefilePath)
        $pattern = '(?ms)^pdf:\r?\n\tmkdir -p \$\(BUILD\)\r?\n\tlatexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=\$\(BUILD\) \$\(MAIN\)\.tex'
        $replacement = "pdf:`r`n`tpowershell -NoProfile -ExecutionPolicy Bypass -File .\build_and_report.ps1 -SkipGit"
        $patched = [regex]::Replace($makeText, $pattern, $replacement, 1)
        if ($patched -ne $makeText) {
            Write-Utf8NoBom $makefilePath $patched
            $script:Fixes.Add('Patched only the Makefile pdf recipe so make calls this Windows-safe build script.')
            Add-Raw '[repair] Makefile pdf recipe patched.'
        }
    }

    if (Test-Path -LiteralPath $pdfPath) {
        Remove-Item -LiteralPath $pdfPath -Force
        Add-Raw '[repair] Removed the pre-existing PDF so this run cannot report a stale artifact as success.'
    }

    $commonArgs = @(
        '-interaction=nonstopmode',
        '-halt-on-error',
        '-file-line-error',
        '-output-directory=build',
        $MainFile
    )
    $pass1 = Invoke-Captured -Label 'pdflatex pass 1' -Command { & pdflatex @commonArgs } -AllowFailure
    if ($pass1.ExitCode -ne 0) {
        $script:Problems.Add("pdflatex pass 1 failed with exit code $($pass1.ExitCode).")
    }
    else {
        $pass2 = Invoke-Captured -Label 'pdflatex pass 2' -Command { & pdflatex @commonArgs } -AllowFailure
        if ($pass2.ExitCode -ne 0) {
            $script:Problems.Add("pdflatex pass 2 failed with exit code $($pass2.ExitCode).")
        }
    }

    if (Test-Path -LiteralPath $logPath) {
        Add-Raw ''
        Add-Raw '===== RAW main.log ====='
        foreach ($line in [System.IO.File]::ReadAllLines($logPath)) { Add-Raw $line }
        $fatalPatterns = '^!|LaTeX Error|Package .* Error|Emergency stop|Fatal error'
        $fatals = Select-String -Path $logPath -Pattern $fatalPatterns
        if ($fatals) {
            foreach ($fatal in $fatals) { $script:Problems.Add("LaTeX log: $($fatal.Line.Trim())") }
        }
        $warningLines = Select-String -Path $logPath -Pattern 'Warning|duplicate ignored'
        foreach ($warning in $warningLines) { $script:Warnings.Add($warning.Line.Trim()) }
    }

    $script:BuildPassed = (Test-Path -LiteralPath $pdfPath) -and (-not ($script:Problems | Where-Object { $_ -match 'pdflatex|LaTeX log' }))
    if (-not $script:BuildPassed) { throw 'The PDF build did not pass.' }
}
catch {
    Add-Raw ("[build exception] {0}" -f $_.Exception.Message)
}
finally {
    if ($script:Warnings -match 'MiKTeX administrator has checked for updates') {
        $script:Warnings.Add('MiKTeX reports that no administrator update check has been performed. The build can still succeed, but MiKTeX maintenance should be run separately with appropriate privileges.')
    }

    $finished = Get-Date
    $summary = New-Object System.Collections.Generic.List[string]
    $summary.Add('')
    $summary.Add('===== SUMMARY =====')
    $summary.Add(("Result: {0}" -f $(if ($script:BuildPassed) { 'PASS' } else { 'FAIL' })))
    $summary.Add(("Finished: {0:o}" -f $finished))
    $summary.Add(("Duration seconds: {0:N2}" -f ($finished - $started).TotalSeconds))
    $summary.Add(("PDF exists: {0}" -f (Test-Path -LiteralPath $pdfPath)))
    $summary.Add(("PDF path: {0}" -f $pdfPath))
    $summary.Add(("Problems found: {0}" -f $script:Problems.Count))
    foreach ($item in $script:Problems) { $summary.Add("  PROBLEM: $item") }
    $summary.Add(("Repairs made: {0}" -f $script:Fixes.Count))
    foreach ($item in $script:Fixes) { $summary.Add("  FIX: $item") }
    $uniqueWarnings = @($script:Warnings | Sort-Object -Unique)
    $summary.Add(("Warnings observed: {0}" -f $uniqueWarnings.Count))
    foreach ($item in $uniqueWarnings) { $summary.Add("  WARNING: $item") }
    foreach ($line in $summary) { Add-Raw $line }

    $reportText = ($script:Raw -join [Environment]::NewLine) + [Environment]::NewLine
    Write-Utf8NoBom $reportPath $reportText
    Write-Utf8NoBom $latestReportPath $reportText

    Write-Host ''
    foreach ($line in $summary) { Write-Host $line }
    Write-Host ("Timestamped report: {0}" -f $reportPath)
    Write-Host ("Latest report:      {0}" -f $latestReportPath)
}

if (-not $SkipGit) {
    try {
        $gitCommand = Get-Command git -ErrorAction SilentlyContinue
        if (-not $gitCommand) { throw 'git was not found on PATH.' }
        $repoRootResult = Invoke-Captured -Label 'git repository root' -Command { git rev-parse --show-toplevel } -AllowFailure
        if ($repoRootResult.ExitCode -ne 0) { throw 'This project is not inside a Git repository.' }
        $repoRoot = ($repoRootResult.Output | Select-Object -First 1).Trim()

        Set-Location $repoRoot
        $relativeScript = (Resolve-Path -LiteralPath $PSCommandPath -Relative).TrimStart([char[]]@('.', [char]92, '/'))
        $relativeReport = (Resolve-Path -LiteralPath $reportPath -Relative).TrimStart([char[]]@('.', [char]92, '/'))
        $relativeLatest = (Resolve-Path -LiteralPath $latestReportPath -Relative).TrimStart([char[]]@('.', [char]92, '/'))
        $pathsToAdd = @($relativeScript, $relativeReport, $relativeLatest)
        if (Test-Path (Join-Path $ProjectRoot 'Makefile')) {
            $relativeMakefile = (Resolve-Path -LiteralPath (Join-Path $ProjectRoot 'Makefile') -Relative).TrimStart([char[]]@('.', [char]92, '/'))
            $pathsToAdd += $relativeMakefile
        }

        Set-Location $repoRoot
        Invoke-Captured -Label 'git add durable build artifacts' -Command { git add -- @pathsToAdd } | Out-Null
        $staged = Invoke-Captured -Label 'git staged diff check' -Command { git diff --cached --quiet } -AllowFailure
        if ($staged.ExitCode -eq 1) {
            $message = if ($script:BuildPassed) {
                'chore: add LaTeX build report and repair workflow'
            } else {
                'chore: record failed LaTeX build diagnostics'
            }
            Invoke-Captured -Label 'git commit' -Command { git commit -m $message } | Out-Null
            $script:CommitCreated = $true
        }
        else {
            Write-Host 'No staged changes required a new commit.'
        }
        Invoke-Captured -Label 'git push' -Command { git push } | Out-Null
        $script:GitPassed = $true
        Write-Host 'Git report publication: PASS' -ForegroundColor Green
    }
    catch {
        Write-Host ("Git report publication: FAIL - {0}" -f $_.Exception.Message) -ForegroundColor Red
        exit 2
    }
}

if ($script:BuildPassed) {
    Write-Host 'LaTeX build: PASS' -ForegroundColor Green
    if ($OpenPdf) { Invoke-Item -LiteralPath $pdfPath }
    exit 0
}
Write-Host 'LaTeX build: FAIL. Read the report summary and raw transcript.' -ForegroundColor Red
exit 1
