#requires -Version 7.0
<#
.SYNOPSIS
    Makes this repository's course-owned archprobe command available to the
    current Windows user.

.DESCRIPTION
    Adds the repository's tools directory to the *user* PATH. No administrator
    rights, machine-wide PATH change, or download is required. Restart the
    terminal after a successful installation.
#>

[CmdletBinding(SupportsShouldProcess)]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$toolDirectory = Join-Path $PSScriptRoot 'tools'
$toolPath = Join-Path $toolDirectory 'archprobe.ps1'
if (-not (Test-Path -LiteralPath $toolPath -PathType Leaf)) {
    throw "Course command is missing: $toolPath"
}

$currentUserPath = [Environment]::GetEnvironmentVariable('Path', 'User')
$entries = @($currentUserPath -split ';' | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
$alreadyInstalled = $entries | Where-Object {
    [string]::Equals($_.TrimEnd('\'), $toolDirectory.TrimEnd('\'), [System.StringComparison]::OrdinalIgnoreCase)
}

if ($alreadyInstalled) {
    Write-Host "archprobe is already installed for this user: $toolDirectory" -ForegroundColor Green
}
elseif ($PSCmdlet.ShouldProcess('current user PATH', "add $toolDirectory")) {
    $newUserPath = (@($entries) + $toolDirectory) -join ';'
    [Environment]::SetEnvironmentVariable('Path', $newUserPath, 'User')
    Write-Host "Installed archprobe for the current user: $toolDirectory" -ForegroundColor Green
    Write-Host 'Open a new PowerShell window, then verify with: archprobe' -ForegroundColor Cyan
}

