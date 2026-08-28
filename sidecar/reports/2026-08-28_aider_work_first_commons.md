# Aider Work First guide — 2026-08-28

## Outcome

Added a student-facing Computing Commons guide for the Aider portion of the
Week 2 Local AI path. It carries the safe method from the completed Brandy
write-up into the Commons delivery layer while keeping Local AI setup
canonical in `local_ai_lab_setup`.

## Changes

- Added `curriculum/week2/aider-work-first.md`.
- Linked it from `curriculum/local-ai-lab.md`.
- Covered the local-only Aider/Ollama boundary, `/ask`, `/add`, `/diff`, one
  bounded request, diff inspection, independent testing, recovery, and the
  completion proof.
- Did not copy internal book content, raw experiment output, credentials, or
  private machine details.
- Did not write to Canvas.

## Validation

- `git diff --check` passed.
- Reviewed the new guide for cloud/API-key instructions and duplicate setup
  procedures; it points students to the approved launcher and canonical
  Recovery path.
- No runtime test was required for Markdown-only source changes.

## Handoff

This is a repository source change and is ready for the existing bounded
Computing Commons publication path. Canvas publication remains a separate
production action and was not performed by this pass.
