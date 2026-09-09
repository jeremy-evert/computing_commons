#requires -Version 7.0
<#
.SYNOPSIS
    Course-owned Windows architecture observation command.

.DESCRIPTION
    Reports the small, inspectable set of host facts used by the computer
    architecture observation exercise. This is not the unrelated Android GPU
    project also named ArchProbe.
#>

[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$os = Get-CimInstance -ClassName Win32_OperatingSystem
$computer = Get-CimInstance -ClassName Win32_ComputerSystem
$processors = @(Get-CimInstance -ClassName Win32_Processor)
$installedBytes = [double]$computer.TotalPhysicalMemory
$freeBytes = [double]$os.FreePhysicalMemory * 1KB
$uptime = (Get-Date) - $os.LastBootUpTime

[pscustomobject]@{
    ComputerName      = $env:COMPUTERNAME
    OperatingSystem   = $os.Caption
    OSArchitecture    = $os.OSArchitecture
    InstalledRAMGiB   = [math]::Round($installedBytes / 1GB, 2)
    FreeRAMGiB        = [math]::Round($freeBytes / 1GB, 2)
    UsedRAMGiB        = [math]::Round(($installedBytes - $freeBytes) / 1GB, 2)
    CPUModels         = $processors.Name -join '; '
    PhysicalPackages  = $processors.Count
    PhysicalCores     = ($processors | Measure-Object -Property NumberOfCores -Sum).Sum
    LogicalProcessors = ($processors | Measure-Object -Property NumberOfLogicalProcessors -Sum).Sum
    LastBootTime      = $os.LastBootUpTime
    UptimeHours       = [math]::Round($uptime.TotalHours, 2)
} | Format-List

