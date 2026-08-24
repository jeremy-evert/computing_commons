[CmdletBinding()]
param(
    [int]$CourseId = 18,
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

$base = "http://localhost:3002/courses/$CourseId"
$targets = @(
    @{ Name = '00-modules'; Url = "$base/modules" },
    @{ Name = '01-success-foundations-semester-kickoff'; Url = "$base/pages/success-foundations-slash-semester-kickoff" },
    @{ Name = '02-recitation-get-help'; Url = "$base/pages/recitation-slash-get-help" },
    @{ Name = '03-week2-local-ai-lab'; Url = "$base/pages/week-2-build-and-verify-your-local-ai-lab" },
    @{ Name = '04-week2-verify-tools'; Url = "$base/pages/week-2-verify-the-tools" },
    @{ Name = '05-week2-recovery'; Url = "$base/pages/week-2-recovery-with-evidence" }
)

$session = Get-Date -Format 'yyyy-MM-dd_HHmmss'
$relativeDir = "sidecar/visual-review/grace/$session"
$outputDir = Join-Path $repoRoot $relativeDir
New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

$manifest = @()
foreach ($target in $targets) {
    Write-Host "Capturing $($target.Name)..."
    $png = Join-Path $outputDir ($target.Name + '.png')
    $capture = & $captureScript -DebugPort $DebugPort -Url $target.Url -OutputPath $png
    $manifest += [pscustomobject]@{
        name = $target.Name
        requested_url = $target.Url
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
    '# Grace visual review capture',
    '',
    "Captured: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')",
    "Savnac course: $CourseId",
    '',
    'These screenshots are full-page browser-rendered evidence from the dedicated Grace capture browser. They are visual-review evidence, not curricular source truth.',
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

    $message = "visual-review: capture Savnac Commons course $CourseId from Grace"
    & git -C $repoRoot commit -m $message
    if ($LASTEXITCODE -ne 0) { throw 'Git commit failed.' }

    & git -C $repoRoot push origin main
    if ($LASTEXITCODE -ne 0) { throw 'Git push failed. The local commit is preserved.' }

    $sha = (& git -C $repoRoot rev-parse HEAD).Trim()
    Write-Host "Published visual review to main at $sha"
}
