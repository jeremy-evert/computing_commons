[CmdletBinding()]
param()
$ErrorActionPreference='Stop';$root=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..'));$sink=Join-Path $root '.teacher-feedback-worktree'
if(-not(Test-Path(Join-Path $sink '.git'))){throw 'Feedback worktree is not prepared.'}
$status=@(git -C $sink status --porcelain);if($status.Count -eq 0){Write-Host 'No unpublished feedback receipts.';exit 0}
git -C $sink add -- sidecar/teacher-feedback/grace/inbox;git -C $sink commit -m 'teacher feedback: publish Grace receipts';git -C $sink push -u origin teacher-feedback/grace
Write-Host 'Feedback receipts published on origin/teacher-feedback/grace; course-source main was not modified.'
