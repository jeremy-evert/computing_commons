[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$repo = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
Set-Location $repo

if (-not (Test-Path (Join-Path $repo '.git'))) {
    throw "Run this helper from the computing_commons checkout."
}
$null = git diff --quiet
$worktreeDirty = $LASTEXITCODE -ne 0
$null = git diff --cached --quiet
$indexDirty = $LASTEXITCODE -ne 0
if ($worktreeDirty -or $indexDirty) {
    throw "Checkout is dirty. Commit or stash changes before owner review."
}
$deck = Join-Path $repo 'slides\week2_local_ai_workbench\week2_local_ai_workbench.pdf'
$notes = Join-Path $repo 'slides\week2_local_ai_workbench\week2_local_ai_workbench_notes.pdf'
if (-not (Test-Path $deck)) { throw "Projected deck PDF is missing: $deck" }
if (-not (Test-Path $notes)) { throw "Instructor notes PDF is missing: $notes" }
$sha = (git rev-parse --short HEAD).Trim()
Write-Host "Reviewing computing_commons commit $sha"
Write-Host "Deck : $deck"
Write-Host "Notes: $notes"
Start-Process $deck
Start-Process $notes
