# Savnac visual link repair

Jeremy found that the Kickoff success link resolved to
`week2-local-ai.html/edit`. The deployed page had received repository preview
filenames literally; those are not Canvas page slugs.

Updated `scripts/deploy_savnac_visual_slice.py` with an explicit bounded
repository-to-Canvas slug mapping for Kickoff, Week 2, tools, recovery, and
Recitation links. Redeployed course 18 in place: six page objects updated,
with no course/module/student/SWOSU scope expansion.

Live read-back confirms five pages and zero remaining repository-filename links;
the Kickoff, tools, recovery, and Recitation Canvas targets are present.
