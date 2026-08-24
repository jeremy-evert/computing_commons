[CmdletBinding()]
param(
    [int]$DebugPort = 9222,
    [string]$StartUrl = 'http://localhost:3002/courses/18'
)

$ErrorActionPreference = 'Stop'

function Resolve-ChromiumBrowser {
    $candidates = @(
        (Join-Path ${env:ProgramFiles} 'Google\Chrome\Application\chrome.exe'),
        (Join-Path ${env:ProgramFiles(x86)} 'Google\Chrome\Application\chrome.exe'),
        (Join-Path ${env:ProgramFiles} 'Microsoft\Edge\Application\msedge.exe'),
        (Join-Path ${env:ProgramFiles(x86)} 'Microsoft\Edge\Application\msedge.exe')
    )

    foreach ($candidate in $candidates) {
        if ($candidate -and (Test-Path $candidate)) {
            return $candidate
        }
    }

    foreach ($name in @('chrome.exe', 'msedge.exe')) {
        $cmd = Get-Command $name -ErrorAction SilentlyContinue
        if ($cmd) { return $cmd.Source }
    }

    throw 'Chrome or Edge was not found. Install one of them or add it to PATH.'
}

$browser = Resolve-ChromiumBrowser
$profileRoot = Join-Path $env:LOCALAPPDATA 'ComputingCommonsCapture'
$profile = Join-Path $profileRoot 'ChromeProfile'
New-Item -ItemType Directory -Force -Path $profile | Out-Null

$debugEndpoint = "http://127.0.0.1:$DebugPort/json/version"
try {
    $existing = Invoke-RestMethod -Uri $debugEndpoint -TimeoutSec 1
    if ($existing.webSocketDebuggerUrl) {
        Write-Host "Capture browser already running on port $DebugPort."
        Start-Process $StartUrl
        exit 0
    }
} catch {
    # Expected when the capture browser is not running yet.
}

$args = @(
    "--remote-debugging-port=$DebugPort",
    "--user-data-dir=$profile",
    '--no-first-run',
    '--no-default-browser-check',
    '--new-window',
    $StartUrl
)

Start-Process -FilePath $browser -ArgumentList $args | Out-Null

$deadline = (Get-Date).AddSeconds(15)
do {
    Start-Sleep -Milliseconds 300
    try {
        $probe = Invoke-RestMethod -Uri $debugEndpoint -TimeoutSec 1
        if ($probe.webSocketDebuggerUrl) {
            Write-Host "Capture browser ready on port $DebugPort."
            Write-Host "Profile: $profile"
            Write-Host 'Log into Savnac once in this dedicated browser. The session persists in this local profile.'
            exit 0
        }
    } catch { }
} while ((Get-Date) -lt $deadline)

throw "Browser started, but the DevTools endpoint did not appear on port $DebugPort within 15 seconds."
