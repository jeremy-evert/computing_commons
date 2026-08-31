# Apparatus repair

Mission 024 exposed a long-tail PTY/caller hang and incomplete lifecycle accounting. Mission 025's caller launches Aider in a new process group, drains the PTY, applies a pre-registered 360-second timeout, terminates and explicitly reaps the process group on timeout, and records `process_lifecycle.log`. Every attempt receives a terminal receipt even when invalid.

Before each attempt the target and known placeholder path are restored from the fixed baseline and baseline proof is captured. After each attempt all three target diff views, staged/unstaged/HEAD path lists, raw output scans, independent proof, receipt, cleanup log, and post-cleanup status are captured. The runner refuses to overwrite an existing attempt directory.
