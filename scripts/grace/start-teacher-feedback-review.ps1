[CmdletBinding()]
param([int]$DebugPort = 9222, [int]$ServicePort = 8765, [string]$StartUrl = 'http://localhost:3002/courses/18')
$ErrorActionPreference = 'Stop'
$root = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..'))
if ((git -C $root status --porcelain)) { throw 'Run the review helper from a clean checkout; feedback receipts use an isolated worktree.' }
if ($StartUrl -notmatch '^http://localhost:3002/courses/18(?:/|$)') { throw 'Refusing non-Savnac course-18 start URL.' }
$browserStarter = Join-Path $PSScriptRoot 'start-savnac-capture-browser.ps1'; & $browserStarter -DebugPort $DebugPort -StartUrl $StartUrl
$sink = Join-Path $root '.teacher-feedback-worktree'
if (-not (Test-Path (Join-Path $sink '.git'))) { git -C $root worktree add -b teacher-feedback/grace $sink HEAD | Out-Host }
$service = Join-Path $root 'scripts\grace\teacher-feedback-service.py'
$source = Join-Path $root 'scripts\grace\teacher-overlay.js'
$logDir = Join-Path $env:LOCALAPPDATA 'ComputingCommonsTeacherFeedback'; New-Item -ItemType Directory -Force $logDir | Out-Null
$pidPath = Join-Path $logDir 'service.pid'
try { $health = Invoke-RestMethod "http://127.0.0.1:$ServicePort/health" -TimeoutSec 1 } catch { $p = Start-Process python -ArgumentList @($service,'--sink',(Join-Path $sink 'sidecar\teacher-feedback\grace\inbox'),'--source-root',$root,'--port',$ServicePort) -PassThru -WindowStyle Hidden; Set-Content $pidPath $p.Id }
$targets = @(Invoke-RestMethod "http://127.0.0.1:$DebugPort/json/list" | Where-Object { $_.type -eq 'page' -and $_.webSocketDebuggerUrl -and $_.url -match '^http://localhost:3002/courses/18(?:/|$)' })
if ($targets.Count -ne 1) { throw "Refusing ambiguous browser target: expected exactly one locked course-18 page, found $($targets.Count)." }
Write-Host "Teacher feedback service ready on 127.0.0.1:$ServicePort; isolated sink: $sink"
Write-Host 'Target lock PASS: http://localhost:3002/courses/18 and dedicated DevTools target.'
Write-Host 'Browser start/reuse is delegated to start-savnac-capture-browser.ps1; run it first if needed.'
& (Join-Path $PSScriptRoot 'inject-teacher-overlay.ps1') -DebugPort $DebugPort -ScriptPath (Join-Path $PSScriptRoot 'teacher-overlay.js')
