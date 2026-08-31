# Mission 028 control

Run: `4e2a43e519380d96798997747e23ee53`
Work-file SHA-256: `2a151e2c407b9cd0edce220efb0e592ae2eb8956b1fcb3a3acbf6a1c722ab019`
Control lineage: Mission 025 payload `98ef24e66a4ff1f4d8aae90dfce219181d192922` on
`anna/aider-edit-transport-replication-025`.

Frozen scored variables: Aider 0.86.2, Ollama 0.12.6, local CPU-only route,
`ollama_chat/qwen2.5-coder-3b-cpu:latest` (3.1B Q4_K_M, digest prefix `6a345c`),
exact-model warm-up before each attempt, fresh PTY-backed Aider process/context,
`--no-auto-commits`, 360-second timeout, deterministic reset, complete Git/path
accounting, independent oracle and regression proof. The sole scored treatment
variable is `--edit-format whole` versus `--edit-format diff`.

## Surface comparison

| condition | source lines | baseline neighboring helpers | target | dependencies |
|---|---:|---:|---|---|
| Mission 025 MODULE | 37 | 7 | `cents_to_label` | none |
| Mission 028 string MODULE | 27 | 6 | `initials` | none |

The new module is shorter by ten lines and one neighboring helper, but remains a
single beginner-readable module with the same small-helper arrangement and no
framework or dependency burden. It is rated SMALL: one straightforward function
with six adjacent examples of the local style.

The allocator first created this worktree before its external state manifest write
was blocked by sandbox policy; the escalated retry verified the clean requested
worktree and branch but reported `reused_existing_worktree: true` with no metadata
path. This limitation is preserved rather than hidden.
