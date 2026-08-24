[CmdletBinding()]
param([int]$DebugPort = 9222, [Parameter(Mandatory)][string]$ScriptPath)
$ErrorActionPreference = 'Stop'
function Send-Cdp { param($Socket,[int]$Id,[string]$Method,[hashtable]$Params=@{})
  $bytes=[Text.Encoding]::UTF8.GetBytes((@{id=$Id;method=$Method;params=$Params}|ConvertTo-Json -Depth 20 -Compress)); $Socket.SendAsync([ArraySegment[byte]]::new($bytes),[Net.WebSockets.WebSocketMessageType]::Text,$true,[Threading.CancellationToken]::None).GetAwaiter().GetResult()|Out-Null
  do { $buf=New-Object byte[] 1048576; $stream=[IO.MemoryStream]::new(); do { $r=$Socket.ReceiveAsync([ArraySegment[byte]]::new($buf),[Threading.CancellationToken]::None).GetAwaiter().GetResult(); $stream.Write($buf,0,$r.Count) } while(-not $r.EndOfMessage); $msg=([Text.Encoding]::UTF8.GetString($stream.ToArray())|ConvertFrom-Json) } while($msg.id -ne $Id)
  if($msg.error){throw $msg.error.message}; return $msg.result
}
$targets=@(Invoke-RestMethod "http://127.0.0.1:$DebugPort/json/list"|Where-Object{$_.type -eq 'page' -and $_.webSocketDebuggerUrl -and $_.url -match '^http://localhost:3002/courses/18(?:/|$)'})
if($targets.Count -ne 1){throw "Refusing ambiguous locked target; found $($targets.Count)."}
$socket=[Net.WebSockets.ClientWebSocket]::new();$socket.ConnectAsync([Uri]$targets[0].webSocketDebuggerUrl,[Threading.CancellationToken]::None).GetAwaiter().GetResult();$js=[IO.File]::ReadAllText($ScriptPath);try{Send-Cdp $socket 1 'Page.addScriptToEvaluateOnNewDocument' @{source=$js}|Out-Null;Send-Cdp $socket 2 'Runtime.evaluate' @{expression=$js;returnByValue=$true}|Out-Null}finally{$socket.CloseAsync([Net.WebSockets.WebSocketCloseStatus]::NormalClosure,'done',[Threading.CancellationToken]::None).GetAwaiter().GetResult()|Out-Null;$socket.Dispose()}
Write-Host 'Teacher-only overlay injected with exact course-18 lock.'
