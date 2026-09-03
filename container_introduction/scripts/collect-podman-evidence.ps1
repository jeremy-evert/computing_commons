# collect-podman-evidence.ps1
#
# Purpose:
# Establish the current Podman world state and record evidence.
#
# Philosophy:
# Failures are data.
# Record observations before making changes.

$ErrorActionPreference = "Continue"

$projectRoot = Split-Path -Parent $PSScriptRoot
$reportsDir = Join-Path $projectRoot "reports"

New-Item -ItemType Directory -Force -Path $reportsDir | Out-Null

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"

$reportFile = Join-Path $reportsDir "podman_observations_$timestamp.txt"
$latestFile = Join-Path $reportsDir "podman_observations_latest.txt"

function Add-Section {
    param([string]$Title)

    Add-Content $reportFile ""
    Add-Content $reportFile "=================================================="
    Add-Content $reportFile $Title
    Add-Content $reportFile "=================================================="
    Add-Content $reportFile ""
}

function Run-And-Capture {
    param(
        [string]$Title,
        [string]$Explanation,
        [scriptblock]$Command
    )

    Add-Section $Title

    Add-Content $reportFile "WHY THIS MATTERS:"
    Add-Content $reportFile $Explanation
    Add-Content $reportFile ""

    try {
        $output = & $Command 2>&1

        Add-Content $reportFile "OUTPUT:"
        Add-Content $reportFile "----------------------------------------"

        if ($output) {
            $output | Out-File -FilePath $reportFile -Append
        }
        else {
            Add-Content $reportFile "(no output)"
        }
    }
    catch {
        Add-Content $reportFile ""
        Add-Content $reportFile "EXCEPTION:"
        Add-Content $reportFile $_
    }

    Add-Content $reportFile ""
}

"Podman Observation Report" | Out-File $reportFile
"Generated: $(Get-Date)" | Out-File $reportFile -Append
"Computer: $env:COMPUTERNAME" | Out-File $reportFile -Append
"" | Out-File $reportFile -Append

Run-And-Capture `
    "Podman Version" `
    "Verifies that the Podman client exists and records the installed version." `
    { podman --version }

Run-And-Capture `
    "Podman Machine List" `
    "Identifies available Podman virtual machines and whether they are running." `
    { podman machine list }

Run-And-Capture `
    "Podman Connections" `
    "Shows where the client expects the Podman service to be running." `
    { podman system connection list }

Run-And-Capture `
    "WSL Status" `
    "Shows WSL distributions and whether they are running." `
    { wsl -l -v }

Run-And-Capture `
    "Podman Info" `
    "Reports operating system, provider, runtime details, and connection health." `
    { podman info }

Run-And-Capture `
    "Podman Images" `
    "Lists locally available container images." `
    { podman images }

Run-And-Capture `
    "Podman Containers" `
    "Lists existing containers including exited containers." `
    { podman ps -a }

Run-And-Capture `
    "Podman Storage Usage" `
    "Shows how much storage images, containers, and volumes consume." `
    { podman system df }

Add-Content $reportFile ""
Add-Content $reportFile "=================================================="
Add-Content $reportFile "END OF REPORT"
Add-Content $reportFile "=================================================="

Copy-Item $reportFile $latestFile -Force

Write-Host ""
Write-Host "Report written:"
Write-Host $reportFile
Write-Host ""
Write-Host "Latest copy written:"
Write-Host $latestFile