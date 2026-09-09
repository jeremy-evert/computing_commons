#requires -Version 7.0
<#
.SYNOPSIS
    Collects a visible, durable computer-architecture handoff receipt.

.DESCRIPTION
    1. Tries the course-provided archprobe command first.
    2. Runs Windows-native fallback checks for memory, processors, process activity,
       and uptime.
    3. Writes all evidence to an automatically named text report.
    4. Attempts to add, commit, and push only that report with Git/GitHub.

    The script records failures in the report instead of hiding them. It does not
    install software, elevate privileges, rewrite Git history, or force-push.

    Run from the repository directory where the report should be stored:
        pwsh -NoProfile -File .\visible_archprobe_handoff.ps1
#>

[CmdletBinding()]
param(
    [string]$ReportDirectory = (Get-Location).Path,
    [int]$ProcessSampleSeconds = 3,
    [switch]$SkipGitPush
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ($ProcessSampleSeconds -lt 1) {
    throw 'ProcessSampleSeconds must be at least 1.'
}

$ReportDirectory = [System.IO.Path]::GetFullPath($ReportDirectory)
[System.IO.Directory]::CreateDirectory($ReportDirectory) | Out-Null

$computerSafe = if ($env:COMPUTERNAME) { $env:COMPUTERNAME } else { 'unknown-computer' }
$computerSafe = $computerSafe -replace '[^A-Za-z0-9._-]', '_'
$stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$reportName = "archprobe_handoff_${computerSafe}_${stamp}.txt"
$reportPath = Join-Path $ReportDirectory $reportName

function Write-Receipt {
    param([Parameter(Mandatory)][AllowEmptyString()][string]$Text)
    $Text | Out-File -LiteralPath $reportPath -Append -Encoding utf8
    Write-Host $Text
}

function Write-Section {
    param([Parameter(Mandatory)][string]$Title)
    Write-Receipt ''
    Write-Receipt ('=' * 72)
    Write-Receipt $Title
    Write-Receipt ('=' * 72)
}

function Invoke-CapturedCommand {
    param(
        [Parameter(Mandatory)][string]$Label,
        [Parameter(Mandatory)][scriptblock]$Command
    )

    Write-Receipt ''
    Write-Receipt ">>> $Label"
    try {
        $output = & $Command 2>&1 | Out-String -Width 240
        if ([string]::IsNullOrWhiteSpace($output)) {
            Write-Receipt '[Command completed with no visible output.]'
        }
        else {
            Write-Receipt $output.TrimEnd()
        }
        Write-Receipt '[EXIT: success]'
        return $true
    }
    catch {
        Write-Receipt ("[EXIT: failure] {0}" -f $_.Exception.Message)
        return $false
    }
}

# Create the receipt before any probes so even an interrupted run leaves evidence.
@(
    'VISIBLE ARCHPROBE HANDOFF',
    "Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')",
    "Computer:  $computerSafe",
    "User:      $env:USERNAME",
    "PowerShell: $($PSVersionTable.PSVersion)",
    "Working directory: $((Get-Location).Path)",
    "Report path: $reportPath"
) | Out-File -LiteralPath $reportPath -Encoding utf8

Write-Host "`nVisible handoff report: $reportPath" -ForegroundColor Cyan

Write-Section '1. REQUIRED COURSE SURFACE: ARCHPROBE'
$archprobe = Get-Command archprobe -ErrorAction SilentlyContinue
if ($null -eq $archprobe) {
    Write-Receipt 'archprobe was not found in the current PATH.'
    Write-Receipt ("Install the course-owned command once with: pwsh -NoProfile -File `"{0}`"" -f (Join-Path $PSScriptRoot 'Install-ArchProbe.ps1'))
    Write-Receipt 'Then open a new PowerShell window and rerun this handoff.'
    Write-Receipt 'The Windows-native fallback evidence will still be collected below.'
}
else {
    Write-Receipt ("Resolved command: {0}" -f $archprobe.Source)
    [void](Invoke-CapturedCommand -Label 'archprobe' -Command { & archprobe })
}

Write-Section '2. WINDOWS-NATIVE FALLBACK EVIDENCE'

[void](Invoke-CapturedCommand -Label 'Memory: Get-CimInstance Win32_OperatingSystem and Win32_ComputerSystem' -Command {
    $os = Get-CimInstance -ClassName Win32_OperatingSystem
    $cs = Get-CimInstance -ClassName Win32_ComputerSystem
    $installed = [double]$cs.TotalPhysicalMemory
    $free = [double]$os.FreePhysicalMemory * 1KB
    [pscustomobject]@{
        InstalledRAMGiB = [math]::Round($installed / 1GB, 2)
        FreeRAMGiB      = [math]::Round($free / 1GB, 2)
        UsedRAMGiB      = [math]::Round(($installed - $free) / 1GB, 2)
        UsedPercent     = [math]::Round((($installed - $free) / $installed) * 100, 1)
    } | Format-List
})

[void](Invoke-CapturedCommand -Label 'CPU topology: Get-CimInstance Win32_Processor' -Command {
    $processors = @(Get-CimInstance -ClassName Win32_Processor)
    [pscustomobject]@{
        CPUModels         = ($processors.Name -join '; ')
        PhysicalPackages  = $processors.Count
        PhysicalCores     = ($processors | Measure-Object NumberOfCores -Sum).Sum
        LogicalProcessors = ($processors | Measure-Object NumberOfLogicalProcessors -Sum).Sum
    } | Format-List
})

[void](Invoke-CapturedCommand -Label "Busiest process during a ${ProcessSampleSeconds}-second sample" -Command {
    $before = @{}
    Get-Process -ErrorAction SilentlyContinue | ForEach-Object {
        try { $before[$_.Id] = [double]$_.CPU } catch { }
    }

    Start-Sleep -Seconds $ProcessSampleSeconds

    $samples = foreach ($process in Get-Process -ErrorAction SilentlyContinue) {
        try {
            if ($before.ContainsKey($process.Id) -and $null -ne $process.CPU) {
                [pscustomobject]@{
                    ProcessName = $process.ProcessName
                    PID         = $process.Id
                    CPUSeconds  = [math]::Round(([double]$process.CPU - $before[$process.Id]), 4)
                }
            }
        }
        catch { }
    }

    $samples | Sort-Object CPUSeconds -Descending | Select-Object -First 10 | Format-Table -AutoSize
})

[void](Invoke-CapturedCommand -Label 'Uptime: Win32_OperatingSystem.LastBootUpTime' -Command {
    $os = Get-CimInstance -ClassName Win32_OperatingSystem
    $uptime = (Get-Date) - $os.LastBootUpTime
    [pscustomobject]@{
        LastBootTime = $os.LastBootUpTime
        Days         = [math]::Floor($uptime.TotalDays)
        Hours        = $uptime.Hours
        Minutes      = $uptime.Minutes
        TotalHours   = [math]::Round($uptime.TotalHours, 2)
    } | Format-List
})

Write-Section '3. GIT AND GITHUB HANDOFF ATTEMPT'

$git = Get-Command git -ErrorAction SilentlyContinue
if ($null -eq $git) {
    Write-Receipt 'Git was not found in PATH. The report exists locally, but tracking was not attempted.'
}
else {
    Write-Receipt ("Git command: {0}" -f $git.Source)

    $repoRoot = (& git -C $ReportDirectory rev-parse --show-toplevel 2>$null | Select-Object -First 1)
    if ([string]::IsNullOrWhiteSpace($repoRoot)) {
        Write-Receipt "No Git work tree contains $ReportDirectory. The report exists locally, but tracking was not attempted."
    }
    else {
        $repoRoot = [System.IO.Path]::GetFullPath($repoRoot.Trim())
        $relativeReport = [System.IO.Path]::GetRelativePath($repoRoot, $reportPath).Replace('\', '/')
        Write-Receipt "Repository root: $repoRoot"
        Write-Receipt "Repository-relative report: $relativeReport"

        [void](Invoke-CapturedCommand -Label 'git remote -v' -Command {
            & git -C $repoRoot remote -v
        })

        $addSucceeded = Invoke-CapturedCommand -Label "git add -- $relativeReport" -Command {
            & git -C $repoRoot add -- $relativeReport
            if ($LASTEXITCODE -ne 0) { throw "git add exited with code $LASTEXITCODE" }
        }

        if ($addSucceeded) {
            # This section changes the tracked report after the first add. Add it again
            # so the staged copy includes the full Git handoff evidence up to this point.
            & git -C $repoRoot add -- $relativeReport 2>&1 | Out-Null

            & git -C $repoRoot diff --cached --quiet -- $relativeReport
            $hasStagedReport = ($LASTEXITCODE -eq 1)

            if (-not $hasStagedReport) {
                Write-Receipt 'No staged report change was detected, so no commit was created.'
            }
            else {
                $commitMessage = "Add architecture probe handoff for $computerSafe at $stamp"
                Write-Receipt "Commit message: $commitMessage"

                # Add once more to include the commit-message line in the committed receipt.
                & git -C $repoRoot add -- $relativeReport 2>&1 | Out-Null

                $commitSucceeded = Invoke-CapturedCommand -Label 'git commit (report only)' -Command {
                    & git -C $repoRoot commit -m $commitMessage -- $relativeReport
                    if ($LASTEXITCODE -ne 0) { throw "git commit exited with code $LASTEXITCODE" }
                }

                if ($commitSucceeded) {
                    if ($SkipGitPush) {
                        Write-Receipt 'Git push skipped because -SkipGitPush was supplied.'
                    }
                    else {
                        [void](Invoke-CapturedCommand -Label 'git push' -Command {
                            & git -C $repoRoot push
                            if ($LASTEXITCODE -ne 0) { throw "git push exited with code $LASTEXITCODE" }
                        })
                    }
                }
                else {
                    Write-Receipt 'Push was not attempted because the commit did not succeed.'
                }
            }
        }
        else {
            Write-Receipt 'Commit and push were not attempted because git add did not succeed.'
        }
    }
}

Write-Section '4. VISIBLE HANDOFF SUMMARY'
Write-Receipt "Report retained at: $reportPath"
Write-Receipt 'Open the report, compare the evidence with the prediction file, and score each prediction.'
Write-Receipt 'If Git or GitHub failed, the exact failure is preserved above for troubleshooting.'

Write-Host "`nHANDOFF COMPLETE" -ForegroundColor Green
Write-Host "Report: $reportPath" -ForegroundColor Green
Write-Host 'The report remains available even if Git or GitHub was unavailable.' -ForegroundColor Green
