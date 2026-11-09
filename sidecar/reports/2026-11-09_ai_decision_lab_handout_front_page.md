# AI Decision Lab handout on the Computing Commons front page — 2026-11-09

Status: **COMPLETE (pending Flo's live read-back; not self-accepted)**. Run 3beb6d385e44f69cf0d57a3922dc06b3, Anna on april.

## Canvas changes (course 24298 / "Computing Commons", id and name verified before write)
- New file: Files > `handouts/AI_Decision_Lab_Student_Handout.pdf`, **file id 6722445**, 77,633 bytes, unlocked, not hidden. Byte-identical to the source PDF (cmp).
- Front page `computing-commons-home`: ONE paragraph inserted at the end of the current-week section, after the day cards. Link text "AI Decision Lab (handout, 4 pages)" plus one line of context taken from the handout itself. Link: `https://swosu.instructure.com/courses/24298/files/6722445` (Canvas added its own file verifier).
- Nothing else changed: with the inserted paragraph removed, the live body equals the pre-write backup exactly.
- Backup (before): `sidecar/runs/front_page_backups/computing-commons-home_before_20261109T095050.html`

## Verification
- Page read back: marker and file link present. File URL fetched without a Canvas token: HTTP 200, `application/pdf` from the download URL, wrap=1 preview 200 titled "AI_Decision_Lab_Student_Handout.pdf: Computing Commons" (no login redirect). Downloaded bytes identical to the source.

## Repo
- Branch `anna/commons-ai-decision-lab-20261109` (pushed). PDF at `handouts/AI_Decision_Lab_Student_Handout.pdf` (repo had no handout convention; `slides/` is for decks). Script `scripts/add_handout_to_front_page.py` (dry-run default, `--apply`, target-locked, backup, idempotent, readback). Source file in `~/` left in place.

## Gaps / notes for Flo
- **Week mismatch:** the work file said Week 5, but the live front page marker is **Week 13** ("This week · Week 13"). Following Jeremy's "this week", the link went in the current-week section, whatever its number; the marker and cards were not touched. The paragraph does not name a week.
- The Week 13 summary line above the cards looks like stale Week 6 text ("engineer the prompt..."), not mine to change; flagging it.
- First readback check in the script was too strict (Canvas rewrites hrefs); fixed in the committed script. The write itself was already correct.
- No student names or data involved. Branch not merged to main.
