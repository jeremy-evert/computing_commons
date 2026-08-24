[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'; $pidPath = Join-Path $env:LOCALAPPDATA 'ComputingCommonsTeacherFeedback\service.pid'
if (Test-Path $pidPath) { $pid = [int](Get-Content $pidPath); Stop-Process -Id $pid -ErrorAction SilentlyContinue; Remove-Item $pidPath -Force }
Write-Host 'Teacher feedback listener stopped. The dedicated capture browser remains available.'
