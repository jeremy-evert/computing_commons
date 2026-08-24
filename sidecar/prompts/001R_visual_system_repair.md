# 001R — REPAIR — Visual System

## Trigger

Execute only if 001C returns `BOUNDED REPAIR REQUIRED`.

If 001C returns `RETHINK REQUIRED`, stop and HUMAN NUDGE rather than using this prompt to smuggle in a redesign.

## Task

Read the ordered repair list in:

`sidecar/reports/luna/001C_adversarial_visual_ux_review_report.md`

Apply only the smallest changes needed to clear those defects.

Do not broaden scope, add new features, or redesign unrelated Commons content.

Re-run the relevant checks from 001C after repair.

## Deliverable

Write:

`sidecar/reports/luna/001R_visual_system_repair_report.md`

Include:

- defects addressed;
- exact files changed;
- checks rerun;
- remaining limitations;
- commit SHA;
- verdict `REPAIR COMPLETE — 001C CHECKS CLEAR` or `REPAIR INCOMPLETE`.

Commit and push before continuing.
