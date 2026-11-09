# Deciding with AI Field Guide (v1.0.2) added to the Computing Commons front page — 2026-11-09

Status: **COMPLETE (pending Flo's live read-back; not self-accepted)**. Anna on april, follow-up to `2026-11-09_ai_decision_lab_handout_front_page.md`.

## Canvas changes (course 24298 / "Computing Commons", id and name verified before write)
- New file: Files > `handouts/Deciding_with_AI_Student_Field_Guide_v1.0.2.pdf`, **file id 6722661**, 103,227 bytes, unlocked, not hidden. sha256 `669b7d4a53ee8637…` matches the source and the downloaded copy.
- Front page `computing-commons-home`: ONE paragraph inserted directly under the AI Decision Lab paragraph, same card style. Text: "Deciding with AI: Student Field Guide (v1.0.2, 8 pages)" plus one line (a guide to using an AI assistant as a sparring partner on a real decision, with prompts to copy and a decision worksheet; written from the PDF's own content).
- AI Decision Lab paragraph and link (file 6722445) unchanged. With the new paragraph removed, the live body equals the pre-write backup exactly.
- Backup (before): `sidecar/runs/front_page_backups/computing-commons-home_before_field-guide_20261109T114816.html`

## Verification
- Page read back with both paragraphs in order. Both links, fetched with no Canvas token: wrap preview HTTP 200; download HTTP 200 `application/pdf`. Downloaded bytes: field guide hash matches the source; AI Decision Lab hash matches its source.

## Repo
- Branch `anna/commons-ai-decision-lab-20261109`. PDF at `handouts/Deciding_with_AI_Student_Field_Guide_v1.0.2.pdf`. The script `scripts/add_handout_to_front_page.py` now takes `--handout=<key>` (`ai-decision-lab` default, `field-guide`); same dry-run default, backup, idempotency marker and readback.

## Notes
- No student data; no other page or course. Branch not merged to main. Source PDF in `~/` left in place.
- The Week 13 summary line oddity from the first report is still unaddressed (Flo's call).
