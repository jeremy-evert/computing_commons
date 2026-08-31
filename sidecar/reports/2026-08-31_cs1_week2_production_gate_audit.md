# CS1 Week 2 Local AI production gate audit

Date: 2026-08-31
Run: `1e0f7082696bd2135180863e010ec540`

## Result

`HUMAN_GATE — preserve the current Commons fallback until CS1's approved qwen3:8b Windows gate is accepted.`

No Commons Canvas object was changed by this audit.

The same-day Aider Days deployment report records the existing door as
`Aider_Days` module `219031`, item `1531238`, title `CS1 Week 2 Local AI`,
published, targeting the shared Commons Week 2 module
`https://swosu.instructure.com/courses/24298/modules/218816`. That was the
correct safe fallback while CS1 had no dedicated production destination.

The CS1-owned Windows evidence reviewed for this run proves a non-admin tool
path and successful `qwen3:1.7b` inference after the exact accepted
`qwen3:8b` inference failed with a CUDA/PTX unsupported-toolchain error. The
later recovery report still records CS1 at the owner Windows dry-run gate.
Because the CS1 source contract remains exact-model `qwen3:8b`, this evidence
does not justify repointing the door to a new CS1 URL.

Once the owner records successful current-package `qwen3:8b` inference and the
bounded Aider exercise, the existing item can be updated in place to the
verified CS1 Canvas destination and explicitly read back as published.
