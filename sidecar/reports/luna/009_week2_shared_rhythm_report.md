# Prompt 009 — Week 2 shared rhythm acceptance report

## Verdict

**WEEK 2 SHARED RHYTHM READY FOR OWNER DOGFOOD.**

The Computing Commons source now presents one Monday/Wednesday/Friday route while preserving the accepted Local AI/Aider runway. The delivery target was Savnac course **18** only.

## Passes

1. **PLAN:** Reconciled the exact AI Fluency Week 2 package and Professional Minds ledger/coverage matrix. The current Professional Minds artifacts are Week 2 Wednesday retrieval practice / *Make It Stick* and Week 2 Friday mindset at work / *Mindset*; no stale week-number inference was used.
2. **BUILD:** Added the shared-rhythm wrappers, instructor guide, provenance map, Savnac deployment support, and readback support. Canonical Professional Minds reading/deck files are uploaded directly from their read-only checkout as delivery assets; no canonical source was copied or edited.
3. **REVIEW:** Checked for repository-looking links, duplicate canonical teaching, dense wrapper content, missing recovery routes, and Monday/Wednesday/Friday ambiguity. One Canvas slug mismatch was found in readback and repaired in the deployment mapping.
4. **DEPLOY:** Reconciled Savnac course 18 in place. Final deployment: 0 new objects on repair pass, 24 updated; the initial pass created the fourth module, four pages, and four source files.
5. **READ BACK:** Final readback shows 4 published modules, 20 published pages, 8 published shared-rhythm items (4 pages + 4 files), and the existing published 0-point Local AI completion object.

## Student route

- **Monday — AI Fluency Level 1 / Gather Context:** compare no/some/rich context, identify guesses, deliberately omit padding, and keep a context-comparison receipt.
- **Wednesday — Professional Minds / Make It Stick:** read and view the canonical assets, retrieve one idea without notes, identify the gap, and choose a bounded practice.
- **Friday — Professional Minds / Mindset at Work:** read and view the canonical assets, apply the distinction between image-protecting and learning-oriented responses to a computing mistake or feedback moment, and keep the recovery receipt.
- Existing **Week 2 Local AI/Aider** pages, assignment, kickoff, and Recitation route remain present and published.

## Evidence

- Deployment manifest: `sidecar/evidence/savnac/009_deployment_manifest.json`
- Final Canvas readback: `sidecar/evidence/savnac/009_readback.json`
- Provenance map: `docs/week2-shared-rhythm-provenance.md`
- Instructor route: `instructor/week2_shared_rhythm_teaching_guide.md`

Readback validation found **no repository filename or `/edit` hrefs**, no bad Canvas page targets, and all four shared source files were present as published File module items. Home/Back/Next and Recitation links resolved to published course pages; course 18 remained available.

## Boundaries

- Canonical `ai_fluency` and `professional_minds` checkouts were unchanged.
- SWOSU production Canvas course 24298 was untouched.
- No live home course was touched.
- Quick Tune and synthetic students did not run.
- No credentials or private student data were added to Git or evidence.

Owner dogfood remains the deliberate next gate: walk course 18 as a student and refine only from observed evidence.
