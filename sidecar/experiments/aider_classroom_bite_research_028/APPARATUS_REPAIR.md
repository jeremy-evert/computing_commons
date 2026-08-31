# Mission 028 apparatus checkpoint

The runner is adapted from the repaired Mission 025 runner without changing the
PTY lifecycle, child reaping, 360-second timeout, deterministic reset, complete
staged/unstaged/HEAD diff capture, raw/filesystem placeholder scan, independent
oracle/regression proof, or terminal receipt lifecycle. Only the concrete target,
prompt semantics, fixture proof path, and evidence namespace changed.

The baseline payload is commit `2ebab93`. No scored run starts until both format
verification attempts complete and the final reset returns the clean baseline.
