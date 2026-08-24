param([switch]$Open)
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Set-Location $root
$status = git status --short
if ($status) { throw 'Refusing review from a dirty checkout.' }
$decks = @(
  'slides/shared_rhythm/week04/monday_moment/week04_monday_decompose.pdf',
  'slides/shared_rhythm/week04/wacky_wednesday/week04_wednesday_arguments.pdf',
  'slides/shared_rhythm/week04/fun_friday/week04_friday_outside_view.pdf',
  'slides/shared_rhythm/week05/monday_moment/week05_monday_model.pdf',
  'slides/shared_rhythm/week05/wacky_wednesday/week05_wednesday_outcome_bias.pdf',
  'slides/shared_rhythm/week05/fun_friday/week05_friday_regression.pdf'
)
$notes = @(
  'slides/shared_rhythm/week04/monday_moment/week04_monday_decompose_notes.pdf',
  'slides/shared_rhythm/week04/wacky_wednesday/week04_wednesday_arguments_notes.pdf',
  'slides/shared_rhythm/week04/fun_friday/week04_friday_outside_view_notes.pdf',
  'slides/shared_rhythm/week05/monday_moment/week05_monday_model_notes.pdf',
  'slides/shared_rhythm/week05/wacky_wednesday/week05_wednesday_outcome_bias_notes.pdf',
  'slides/shared_rhythm/week05/fun_friday/week05_friday_regression_notes.pdf'
)
foreach ($path in ($decks + $notes)) { if (!(Test-Path $path) -or ((Get-Item $path).Length -le 0)) { throw "Missing or empty PDF: $path" } }
Write-Host "Commit: $(git rev-parse HEAD)"
Write-Host 'Projector decks:'; $decks | ForEach-Object { Write-Host "  $_" }
Write-Host 'Instructor notes:'; $notes | ForEach-Object { Write-Host "  $_" }
if ($Open) { foreach ($path in ($decks + $notes)) { Start-Process (Join-Path $root $path) } }
