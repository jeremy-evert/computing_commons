[CmdletBinding()]
param(
    [int]$DebugPort = 9222,
    [switch]$Publish
)

$ErrorActionPreference = 'Stop'

$repoRoot = (& git rev-parse --show-toplevel 2>$null)
if (-not $repoRoot) {
    throw 'Run this script from inside the computing_commons Git checkout.'
}
$repoRoot = [System.IO.Path]::GetFullPath($repoRoot)
$captureScript = Join-Path $repoRoot 'scripts/grace/capture-canvas-full-page.ps1'
if (-not (Test-Path $captureScript)) {
    throw "Missing capture helper: $captureScript"
}

if ($Publish) {
    $branch = (& git -C $repoRoot branch --show-current).Trim()
    if ($branch -ne 'main') {
        throw "-Publish is intentionally limited to main. Current branch: $branch"
    }
    $before = @(& git -C $repoRoot status --porcelain)
    if ($before.Count -gt 0) {
        throw 'Refusing -Publish because the checkout already has uncommitted changes. Commit/stash them first.'
    }
}

# Production SWOSU Canvas, Computing Commons, course 24298, module 218816
# ("02 -- Week 2: Build and Verify Local AI"). This is live, real Canvas --
# there is no localhost tunnel here. A human must already be logged into
# https://swosu.instructure.com in the dedicated capture browser on this
# machine before this script runs (see README: "Owner login step").
$base = 'https://swosu.instructure.com/courses/24298'

$targets = @(
    [pscustomobject]@{ Name = '00-modules'; Url = "$base/modules" }
    [pscustomobject]@{ Name = '01-week2-start-here'; Url = "$base/pages/week-2-start-here" }
    [pscustomobject]@{ Name = '02-week2-build-and-verify'; Url = "$base/pages/week-2-build-and-verify-your-local-ai-lab" }
    [pscustomobject]@{ Name = '03-week2-verify-the-tools'; Url = "$base/pages/week-2-verify-the-tools" }
    [pscustomobject]@{ Name = '04-week2-recovery-with-evidence'; Url = "$base/pages/week-2-recovery-with-evidence" }
    [pscustomobject]@{ Name = '05-week2-inventory'; Url = "$base/pages/week-2-inventory-what-you-already-have" }
    [pscustomobject]@{ Name = '06-week2-windows-foundation'; Url = "$base/pages/week-2-verify-the-windows-foundation" }
    [pscustomobject]@{ Name = '07-week2-confirm-ollama'; Url = "$base/pages/week-2-confirm-ollama" }
    [pscustomobject]@{ Name = '08-week2-approved-model'; Url = "$base/pages/week-2-confirm-the-approved-model" }
    [pscustomobject]@{ Name = '09-week2-hello-ollama'; Url = "$base/pages/week-2-say-hello-directly-to-ollama" }
    [pscustomobject]@{ Name = '10-week2-confirm-aider'; Url = "$base/pages/week-2-get-or-confirm-aider" }
    [pscustomobject]@{ Name = '11-week2-git-worktree'; Url = "$base/pages/week-2-prepare-the-tiny-git-worktree" }
    [pscustomobject]@{ Name = '12-week2-hello-aider'; Url = "$base/pages/week-2-say-hello-with-aider" }
    [pscustomobject]@{ Name = '13-week2-three-aider-wins'; Url = "$base/pages/week-2-three-tiny-aider-wins" }
    [pscustomobject]@{ Name = '14-week2-work-first'; Url = "$base/pages/week-2-bridge-to-work-first" }
    [pscustomobject]@{ Name = '15-week2-show-that-it-works'; Url = "$base/pages/week-2-show-that-it-works" }
    [pscustomobject]@{ Name = '16-file-day1-slides-pptx'; Url = "$base/files/6569596" }
    [pscustomobject]@{ Name = '17-file-day1-slides-pdf'; Url = "$base/files/6569597" }
    [pscustomobject]@{ Name = '18-file-field-guide'; Url = "$base/files/6569598" }
    [pscustomobject]@{ Name = '19-file-session-notes'; Url = "$base/files/6569599" }
    [pscustomobject]@{ Name = '20-file-my-field-notes'; Url = "$base/files/6569603" }
    [pscustomobject]@{ Name = '21-file-setup-script'; Url = "$base/files/6569604" }
    [pscustomobject]@{ Name = '22-file-run1-log'; Url = "$base/files/6569605" }
    [pscustomobject]@{ Name = '23-file-run1-report'; Url = "$base/files/6569606" }
    [pscustomobject]@{ Name = '24-file-run2-log'; Url = "$base/files/6569607" }
    [pscustomobject]@{ Name = '25-file-run2-report'; Url = "$base/files/6569608" }
)

$session = Get-Date -Format 'yyyy-MM-dd_HHmmss'
$relativeDir = "sidecar/visual-review/maise/$session"
$outputDir = Join-Path $repoRoot $relativeDir
New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

$manifest = @()
foreach ($target in $targets) {
    $name = [string]$target.Name
    $requestedUrl = [string]$target.Url
    Write-Host "Capturing $name..."
    $png = Join-Path $outputDir ($name + '.png')
    $capture = & $captureScript -DebugPort $DebugPort -Url $requestedUrl -OutputPath $png
    $manifest += [pscustomobject]@{
        name = $name
        requested_url = $requestedUrl
        rendered_title = $capture.Title
        rendered_url = $capture.Url
        file = [System.IO.Path]::GetRelativePath($repoRoot, $capture.Path).Replace('\','/')
        width = $capture.Width
        height = $capture.Height
    }
}

$manifestPath = Join-Path $outputDir 'manifest.json'
$manifest | ConvertTo-Json -Depth 10 | Set-Content -Path $manifestPath -Encoding UTF8

$readmePath = Join-Path $outputDir 'README.md'
$lines = @(
    '# Maise visual review capture -- PRODUCTION',
    '',
    "Captured: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')",
    'Course: SWOSU Canvas, Computing Commons (course 24298), module 02 -- Week 2: Build and Verify Local AI',
    'This is the live production course, not a Savnac staging tunnel.',
    '',
    'These screenshots are full-page browser-rendered evidence from the dedicated maise capture browser. They are visual-review evidence, not curricular source truth.',
    '',
    '| Page | Rendered title | File |',
    '| --- | --- | --- |'
)
foreach ($item in $manifest) {
    $lines += "| $($item.name) | $($item.rendered_title -replace '\|','/') | [$([System.IO.Path]::GetFileName($item.file))]($([System.IO.Path]::GetFileName($item.file))) |"
}
$lines | Set-Content -Path $readmePath -Encoding UTF8

Write-Host "Capture set written to $outputDir"

if ($Publish) {
    & git -C $repoRoot add -- $relativeDir
    $staged = @(& git -C $repoRoot diff --cached --name-only)
    if ($staged.Count -eq 0) {
        throw 'Nothing was staged; refusing empty visual-review commit.'
    }
    $message = "visual-review: capture production Computing Commons Week 2 from maise"
    & git -C $repoRoot commit -m $message
    if ($LASTEXITCODE -ne 0) { throw 'Git commit failed.' }
    & git -C $repoRoot push origin main
    if ($LASTEXITCODE -ne 0) { throw 'Git push failed. The local commit is preserved.' }
    $sha = (& git -C $repoRoot rev-parse HEAD).Trim()
    Write-Host "Published visual review to main at $sha"
}
