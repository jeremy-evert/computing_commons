[CmdletBinding()]
param(
    [int]$DebugPort = 9222,
    [string]$Url,
    [string]$OutputPath,
    [int]$LoadWaitSeconds = 5
)

$ErrorActionPreference = 'Stop'

function Invoke-CdpCommand {
    param(
        [Parameter(Mandatory)] [System.Net.WebSockets.ClientWebSocket] $Socket,
        [Parameter(Mandatory)] [int] $Id,
        [Parameter(Mandatory)] [string] $Method,
        [hashtable] $Params = @{}
    )

    $payload = @{ id = $Id; method = $Method; params = $Params } | ConvertTo-Json -Depth 20 -Compress
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($payload)
    $segment = [ArraySegment[byte]]::new($bytes)
    $Socket.SendAsync(
        $segment,
        [System.Net.WebSockets.WebSocketMessageType]::Text,
        $true,
        [System.Threading.CancellationToken]::None
    ).GetAwaiter().GetResult() | Out-Null

    while ($true) {
        $buffer = New-Object byte[] 1048576
        $stream = [System.IO.MemoryStream]::new()
        do {
            $recvSegment = [ArraySegment[byte]]::new($buffer)
            $result = $Socket.ReceiveAsync(
                $recvSegment,
                [System.Threading.CancellationToken]::None
            ).GetAwaiter().GetResult()
            if ($result.MessageType -eq [System.Net.WebSockets.WebSocketMessageType]::Close) {
                throw 'Chrome DevTools websocket closed unexpectedly.'
            }
            $stream.Write($buffer, 0, $result.Count)
        } while (-not $result.EndOfMessage)

        $text = [System.Text.Encoding]::UTF8.GetString($stream.ToArray())
        $message = $text | ConvertFrom-Json
        if ($message.id -eq $Id) {
            if ($message.error) {
                throw "CDP $Method failed: $($message.error.message)"
            }
            return $message.result
        }
    }
}

function Get-SafeSlug {
    param([string]$Value)
    $slug = $Value.ToLowerInvariant() -replace '[^a-z0-9]+', '-'
    $slug = $slug.Trim('-')
    if (-not $slug) { $slug = 'canvas-page' }
    if ($slug.Length -gt 80) { $slug = $slug.Substring(0, 80).TrimEnd('-') }
    return $slug
}

$listUrl = "http://127.0.0.1:$DebugPort/json/list"
try {
    $targets = @(Invoke-RestMethod -Uri $listUrl -TimeoutSec 3)
} catch {
    throw "No capture browser found on port $DebugPort. Launch Chrome/Edge with --remote-debugging-port=$DebugPort and a dedicated profile first, then sign in and navigate to the page you want to capture."
}

# Normalize a nested top-level array if Invoke-RestMethod returns one as a
# single pipeline object on this PowerShell build.
if ($targets.Count -eq 1 -and $targets[0] -is [System.Array]) {
    $targets = @($targets[0])
}

$target = $targets |
    Where-Object { $_.type -eq 'page' -and $_.webSocketDebuggerUrl -and $_.url -notlike 'devtools://*' } |
    Where-Object { $_.url -like 'http://localhost:3002/*' -or $_.url -like 'http://127.0.0.1:3002/*' } |
    Select-Object -First 1

if (-not $target) {
    $target = $targets |
        Where-Object { $_.type -eq 'page' -and $_.webSocketDebuggerUrl -and $_.url -notlike 'devtools://*' } |
        Select-Object -First 1
}

if (-not $target) {
    throw 'No capturable browser tab was found.'
}

$webSocketDebuggerUrl = @($target.webSocketDebuggerUrl) | Select-Object -First 1
$webSocketDebuggerUrl = [string]$webSocketDebuggerUrl
if ([string]::IsNullOrWhiteSpace($webSocketDebuggerUrl)) {
    throw 'The selected browser tab has no usable DevTools websocket URL.'
}

$socket = [System.Net.WebSockets.ClientWebSocket]::new()
$socket.ConnectAsync(
    [System.Uri]::new($webSocketDebuggerUrl),
    [System.Threading.CancellationToken]::None
).GetAwaiter().GetResult()

$nextId = 1
try {
    Invoke-CdpCommand -Socket $socket -Id $nextId -Method 'Page.enable' | Out-Null
    $nextId++

    if ($Url) {
        Invoke-CdpCommand -Socket $socket -Id $nextId -Method 'Page.navigate' -Params @{ url = $Url } | Out-Null
        $nextId++
        Start-Sleep -Seconds $LoadWaitSeconds

        for ($i = 0; $i -lt 20; $i++) {
            $ready = Invoke-CdpCommand -Socket $socket -Id $nextId -Method 'Runtime.evaluate' -Params @{ expression = 'document.readyState'; returnByValue = $true }
            $nextId++
            if ($ready.result.value -eq 'complete') { break }
            Start-Sleep -Milliseconds 250
        }
    }

    $meta = Invoke-CdpCommand -Socket $socket -Id $nextId -Method 'Runtime.evaluate' -Params @{
        expression = '({title: document.title, url: location.href})'
        returnByValue = $true
    }
    $nextId++

    $title = [string]$meta.result.value.title
    $currentUrl = [string]$meta.result.value.url

    $metrics = Invoke-CdpCommand -Socket $socket -Id $nextId -Method 'Page.getLayoutMetrics'
    $nextId++
    $contentSize = if ($metrics.cssContentSize) { $metrics.cssContentSize } else { $metrics.contentSize }

    $width = [Math]::Max(1, [Math]::Ceiling([double]$contentSize.width))
    $height = [Math]::Max(1, [Math]::Ceiling([double]$contentSize.height))

    if (-not $OutputPath) {
        $repoRoot = (& git rev-parse --show-toplevel 2>$null)
        if (-not $repoRoot) { $repoRoot = (Get-Location).Path }
        $dateDir = Join-Path $repoRoot ("sidecar/visual-review/grace/" + (Get-Date -Format 'yyyy-MM-dd'))
        New-Item -ItemType Directory -Force -Path $dateDir | Out-Null
        $stamp = Get-Date -Format 'HHmmss'
        $OutputPath = Join-Path $dateDir ("${stamp}_$(Get-SafeSlug $title).png")
    }

    $fullOutput = [System.IO.Path]::GetFullPath($OutputPath)
    New-Item -ItemType Directory -Force -Path ([System.IO.Path]::GetDirectoryName($fullOutput)) | Out-Null

    $shot = Invoke-CdpCommand -Socket $socket -Id $nextId -Method 'Page.captureScreenshot' -Params @{
        format = 'png'
        fromSurface = $true
        captureBeyondViewport = $true
        clip = @{ x = 0; y = 0; width = $width; height = $height; scale = 1 }
    }

    [System.IO.File]::WriteAllBytes($fullOutput, [Convert]::FromBase64String([string]$shot.data))

    [pscustomobject]@{
        Title = $title
        Url = $currentUrl
        Path = $fullOutput
        Width = $width
        Height = $height
    }
}
finally {
    if ($socket.State -eq [System.Net.WebSockets.WebSocketState]::Open) {
        $socket.CloseAsync(
            [System.Net.WebSockets.WebSocketCloseStatus]::NormalClosure,
            'capture complete',
            [System.Threading.CancellationToken]::None
        ).GetAwaiter().GetResult() | Out-Null
    }
    $socket.Dispose()
}
