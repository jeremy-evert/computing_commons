#requires -Version 7.0
<#
.SYNOPSIS
    Revised visible handoff for the computer-architecture observation exercise.

.DESCRIPTION
    This revised script:
      1. embeds the student's prediction file when present;
      2. tries archprobe first, then collects Windows-native fallback evidence;
      3. writes a uniquely named report before probes begin;
      4. captures native Git exit codes immediately after each Git command;
      5. uses two deliberate git-add operations rather than repeated staging;
      6. records HANDOFF COMPLETE in the saved report;
      7. attempts to commit and push the report without elevation, installs,
         destructive file operations, history rewriting, or force-push.

    Run from the directory containing this script and the prediction file:
      pwsh -NoProfile -File .\visible_archprobe_handoff_revised.ps1
#>

[CmdletBinding()]
param(
    [string]$ReportDirectory = $PSScriptRoot,
    [string]$PredictionFileName = 'morgan_windows_desktop_observations.txt',
    [ValidateRange(1, 30)]
    [int]$ProcessSampleSeconds = 3,
    [switch]$SkipGitPush
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

if ([string]::IsNullOrWhiteSpace($ReportDirectory)) {
    $ReportDirectory = (Get-Location).Path
}

$ReportDirectory = [System.IO.Path]::GetFullPath($ReportDirectory)
[System.IO.Directory]::CreateDirectory($ReportDirectory) | Out-Null

$computerName = if ([string]::IsNullOrWhiteSpace($env:COMPUTERNAME)) {
    'unknown-computer'
}
else {
    $env:COMPUTERNAME
}

$computerSafe = $computerName -replace '[^A-Za-z0-9._-]', '_'
$timestamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$reportName = "archprobe_handoff_${computerSafe}_${timestamp}.txt"
$reportPath = Join-Path $ReportDirectory $reportName
$predictionPath = Join-Path $ReportDirectory $PredictionFileName

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

function Invoke-CapturedPowerShell {
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

function Invoke-CapturedGit {
    param(
        [Parameter(Mandatory)][string]$Label,
        [Parameter(Mandatory)][string]$RepositoryRoot,
        [Parameter(Mandatory)][string[]]$GitArguments
    )

    Write-Receipt ''
    Write-Receipt ">>> $Label"

    try {
        $output = & git -C $RepositoryRoot @GitArguments 2>&1 | Out-String -Width 240
        $exitCode = $LASTEXITCODE

        if ([string]::IsNullOrWhiteSpace($output)) {
            Write-Receipt '[Command completed with no visible output.]'
        }
        else {
            Write-Receipt $output.TrimEnd()
        }

        if ($exitCode -ne 0) {
            throw "git exited with code $exitCode"
        }

        Write-Receipt '[EXIT: success]'
        return $true
    }
    catch {
        Write-Receipt ("[EXIT: failure] {0}" -f $_.Exception.Message)
        return $false
    }
}

@(
    'VISIBLE ARCHPROBE HANDOFF - REVISED SCRIPT',
    "Generated:         $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')",
    "Computer:          $computerName",
    "User:              $env:USERNAME",
    "PowerShell:        $($PSVersionTable.PSVersion)",
    "Script:            $PSCommandPath",
    "Working directory: $((Get-Location).Path)",
    "Report path:       $reportPath"
) | Out-File -LiteralPath $reportPath -Encoding utf8

Write-Host "`nVisible handoff report: $reportPath" -ForegroundColor Cyan

Write-Section '0. STUDENT PREDICTION FILE'
if (Test-Path -LiteralPath $predictionPath -PathType Leaf) {
    Write-Receipt "Prediction source: $predictionPath"
    Write-Receipt ''

    $predictionText = Get-Content -LiteralPath $predictionPath -Raw
    if ([string]::IsNullOrWhiteSpace($predictionText)) {
        Write-Receipt '[The prediction file exists but is empty.]'
    }
    else {
        Write-Receipt $predictionText.TrimEnd()
    }
}
else {
    Write-Receipt "Prediction file not found: $predictionPath"
    Write-Receipt 'Evidence collection will continue. No prediction has been invented.'
}

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
    [void](Invoke-CapturedPowerShell -Label 'archprobe' -Command { & archprobe })
}

Write-Section '2. WINDOWS-NATIVE FALLBACK EVIDENCE'

[void](Invoke-CapturedPowerShell -Label 'Memory: Win32_OperatingSystem and Win32_ComputerSystem' -Command {
    $os = Get-CimInstance -ClassName Win32_OperatingSystem
    $cs = Get-CimInstance -ClassName Win32_ComputerSystem
    $installedBytes = [double]$cs.TotalPhysicalMemory
    $freeBytes = [double]$os.FreePhysicalMemory * 1KB

    [pscustomobject]@{
        InstalledRAMGiB = [math]::Round($installedBytes / 1GB, 2)
        FreeRAMGiB      = [math]::Round($freeBytes / 1GB, 2)
        UsedRAMGiB      = [math]::Round(($installedBytes - $freeBytes) / 1GB, 2)
        UsedPercent     = [math]::Round((($installedBytes - $freeBytes) / $installedBytes) * 100, 1)
    } | Format-List
})

[void](Invoke-CapturedPowerShell -Label 'CPU topology: Win32_Processor' -Command {
    $processors = @(Get-CimInstance -ClassName Win32_Processor)

    [pscustomobject]@{
        CPUModels         = ($processors.Name -join '; ')
        PhysicalPackages  = $processors.Count
        PhysicalCores     = ($processors | Measure-Object -Property NumberOfCores -Sum).Sum
        LogicalProcessors = ($processors | Measure-Object -Property NumberOfLogicalProcessors -Sum).Sum
    } | Format-List
})

Write-Receipt ''
Write-Receipt 'Interpretation note: physical cores and logical processors are intentionally reported separately.'
Write-Receipt 'A prediction of "12 cores" may actually describe 6 physical cores and 12 logical processors.'

[void](Invoke-CapturedPowerShell -Label "Busiest processes during a ${ProcessSampleSeconds}-second sample" -Command {
    $before = @{}
    Get-Process -ErrorAction SilentlyContinue | ForEach-Object {
        try {
            $before[$_.Id] = [double]$_.CPU
        }
        catch {
            # Protected and short-lived processes may not expose CPU data.
        }
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
        catch {
            # A process may exit or become inaccessible during the sample.
        }
    }

    $samples |
        Sort-Object -Property CPUSeconds -Descending |
        Select-Object -First 10 |
        Format-Table -AutoSize
})

[void](Invoke-CapturedPowerShell -Label 'Uptime: Win32_OperatingSystem.LastBootUpTime' -Command {
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

    $repoOutput = & git -C $ReportDirectory rev-parse --show-toplevel 2>&1 | Out-String
    $repoExitCode = $LASTEXITCODE

    if ($repoExitCode -ne 0 -or [string]::IsNullOrWhiteSpace($repoOutput)) {
        Write-Receipt "No Git work tree was resolved for: $ReportDirectory"
        Write-Receipt $repoOutput.TrimEnd()
        Write-Receipt "[EXIT: failure] git exited with code $repoExitCode"
    }
    else {
        $repoRoot = [System.IO.Path]::GetFullPath($repoOutput.Trim())
        $relativeReport = [System.IO.Path]::GetRelativePath($repoRoot, $reportPath).Replace('\', '/')
        $commitMessage = "Add revised architecture probe handoff for $computerSafe at $timestamp"

        Write-Receipt "Repository root:             $repoRoot"
        Write-Receipt "Repository-relative report:  $relativeReport"
        Write-Receipt "Planned commit message:       $commitMessage"

        [void](Invoke-CapturedGit -Label 'git remote -v' -RepositoryRoot $repoRoot -GitArguments @('remote', '-v'))

        # ADD 1 OF 2: establish that Git accepts this exact report path.
        $firstAddSucceeded = Invoke-CapturedGit `
            -Label "git add -- $relativeReport (first of two deliberate adds)" `
            -RepositoryRoot $repoRoot `
            -GitArguments @('add', '--', $relativeReport)

        if (-not $firstAddSucceeded) {
            Write-Receipt 'Commit and push were not attempted because the first git add failed.'
        }
        else {
            Write-Receipt ''
            Write-Receipt 'Pre-commit Git evidence is complete.'
            Write-Receipt 'The second add will stage the report exactly as it exists at this checkpoint.'

            # ADD 2 OF 2: include the pre-commit evidence written after the first add.
            $secondAddOutput = & git -C $repoRoot add -- $relativeReport 2>&1 | Out-String -Width 240
            $secondAddExitCode = $LASTEXITCODE

            if ($secondAddExitCode -ne 0) {
                Write-Receipt $secondAddOutput.TrimEnd()
                Write-Receipt "[EXIT: failure] second git add exited with code $secondAddExitCode"
                Write-Receipt 'Commit and push were not attempted because the final staging step failed.'
            }
            else {
                # Do not append to the report between this final add and git commit.
                & git -C $repoRoot diff --cached --quiet -- $relativeReport
                $diffExitCode = $LASTEXITCODE

                if ($diffExitCode -eq 0) {
                    Write-Receipt 'No staged report change was detected, so no commit or push was attempted.'
                }
                elseif ($diffExitCode -ne 1) {
                    Write-Receipt "Unable to inspect the staged report; git diff exited with code $diffExitCode."
                }
                else {
                    # Native output is shown live. The committed report already contains the complete
                    # investigation and its pre-commit handoff checkpoint.
                    Write-Host "`n>>> git commit -- $relativeReport" -ForegroundColor Cyan
                    $commitOutput = & git -C $repoRoot commit -m $commitMessage -- $relativeReport 2>&1 | Out-String -Width 240
                    $commitExitCode = $LASTEXITCODE
                    Write-Host $commitOutput.TrimEnd()

                    if ($commitExitCode -ne 0) {
                        Write-Host "[EXIT: failure] git commit exited with code $commitExitCode" -ForegroundColor Red
                    }
                    elseif ($SkipGitPush) {
                        Write-Host '[EXIT: success] Commit created. Push skipped by -SkipGitPush.' -ForegroundColor Yellow
                    }
                    else {
                        Write-Host "`n>>> git push" -ForegroundColor Cyan
                        $pushOutput = & git -C $repoRoot push 2>&1 | Out-String -Width 240
                        $pushExitCode = $LASTEXITCODE
                        Write-Host $pushOutput.TrimEnd()

                        if ($pushExitCode -ne 0) {
                            Write-Host "[EXIT: failure] git push exited with code $pushExitCode" -ForegroundColor Red
                        }
                        else {
                            Write-Host '[EXIT: success] git push completed.' -ForegroundColor Green
                        }
                    }
                }
            }
        }
    }
}

# If Git committed the report, changing it afterward would make the work tree dirty.
# Therefore completion is always visible in the terminal, and it is written into the
# report whenever doing so will not alter a successfully committed artifact.
$reportIsTrackedAndClean = $false
if ($null -ne $git) {
    try {
        $rootCheck = & git -C $ReportDirectory rev-parse --show-toplevel 2>$null | Select-Object -First 1
        $rootCheckCode = $LASTEXITCODE
        if ($rootCheckCode -eq 0 -and -not [string]::IsNullOrWhiteSpace($rootCheck)) {
            $rootCheck = $rootCheck.Trim()
            $relativeCheck = [System.IO.Path]::GetRelativePath($rootCheck, $reportPath).Replace('\', '/')
            & git -C $rootCheck diff --quiet -- $relativeCheck
            $workTreeCode = $LASTEXITCODE
            & git -C $rootCheck cat-file -e "HEAD:$relativeCheck" 2>$null
            $committedCode = $LASTEXITCODE
            $reportIsTrackedAndClean = ($workTreeCode -eq 0 -and $committedCode -eq 0)
        }
    }
    catch {
        $reportIsTrackedAndClean = $false
    }
}

if (-not $reportIsTrackedAndClean) {
    Write-Section '4. VISIBLE HANDOFF SUMMARY'
    Write-Receipt 'HANDOFF COMPLETE'
    Write-Receipt "Report retained at: $reportPath"
    Write-Receipt 'Compare the embedded prediction with the measured evidence and score each claim.'
    Write-Receipt 'Any recorded failure is evidence for the next troubleshooting step.'
}

Write-Host "`nHANDOFF COMPLETE" -ForegroundColor Green
Write-Host "Report: $reportPath" -ForegroundColor Green
if ($reportIsTrackedAndClean) {
    Write-Host 'The committed report remains clean; post-commit status was left in the terminal.' -ForegroundColor Green
}
else {
    Write-Host 'The completion marker was also written into the local report.' -ForegroundColor Green
}
