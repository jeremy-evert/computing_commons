# Mission 019 — Brandy Aider curriculum harvest and round 2

## Scope and outcome

- Prompt/work file: `scratch/anna_brandy_aider_curriculum_harvest_round2_019.md`
- Run: `5800faee6f46b6a344c44f22e6af5970`
- Role/engine: Anna / Assistant Foreman, `gpt-5.6-luna`, medium
- Host: Brandy
- Primary repository: `jeremy-evert/computing_commons`
- Result: Brandy work was already durable on `origin/assistant/luna`; this pass
  added one bounded Week 2 student proof card and this harvest map.

## Brandy repository truth

At launch, `computing_commons` was clean on `assistant/luna` at `66dbd75`,
tracking `origin/assistant/luna`. There were no stashes, no untracked files,
and no worktree dirt. No Aider, Ollama, Flo, or Foreman worker process was
active. The host had 96 CPUs, 375 GiB RAM, and 333 GiB available memory.

After refreshing remote refs, GitHub reported:

- `origin/assistant/luna` = `66dbd750fdddd28ca69dffce73e8d350746e7c59`
- `origin/main` = `e4100e0ef34bd677d3a391899abecfbfc944f63e`
- `assistant/luna` is 15 commits ahead and 1 commit behind `origin/main`.
- The newer `origin/main` commit `e4100e0` adds a separate student Aider
  guide and is already remote-durable. It was reviewed but not merged into
  this feature branch, avoiding unrelated main-history integration.

The first ordinary `git fetch origin` failed because the host SSH config
include `30-libvirt-ssh-proxy.conf` was unreadable. A retry using the normal
Git SSH path with that broken include bypassed succeeded; no history rewrite
or force push was needed.

## Harvest map

| Classification | Repository artifact / provenance | Teaching value and proof | Audience / next action |
|---|---|---|---|
| KEEP / PROVEN | `curriculum/week2/*`, `instructor/week2_aider_work_first_teaching_guide.md`, commit `4628994` | Local-AI runway from inventory through exact model, direct inference, Aider, worktree, bounded edit, diff, test, recovery, and Work First. Source-build report and existing Savnac 18 manifests/readbacks support the route. | Student + instructor. Use as the immediate runway; apply the new proof card from `fc6840e`. |
| KEEP / PROVEN | `curriculum/week2/aider-work-first.md`, `curriculum/local-ai-lab.md`, `sidecar/reports/2026-08-28_aider_work_first_commons.md`, remote commit `e4100e0` | Explicit local-only boundary, one-sentence request, `/ask`, `/add`, `/diff`, independent test, completion proof, and recovery. | Student-facing source on `origin/main`; Flo should consider it with the Week 2 runway when branches are later reconciled. |
| KEEP / PROVEN | `curriculum/week2` plus `sidecar/reports/luna/009_week2_shared_rhythm_report.md`, commit `8818978` | Monday/Wednesday/Friday shared rhythm with canonical AI Fluency and Professional Minds sources, recovery, provenance, and Savnac 18 readback. | Student + instructor. Owner dogfood remains the next gate. |
| KEEP / PROVEN | `sidecar/reports/luna/010_week3_shared_rhythm_report.md`, commit `285a724` | Week 3 plan, mistake, resilience, and risk-competence rhythm with source pins and 147-link readback. | Student + instructor. Keep as later shared-rhythm ingredient; owner dogfood remains. |
| KEEP / NEEDS OWNER DOGFOOD | `instructor/week2_shared_rhythm_teaching_guide.md`, `instructor/week3_shared_rhythm_teaching_guide.md` | Useful teaching choreography and recovery framing, but no fresh owner walk-through was recorded in this mission. | Instructor-facing. Jeremy/owner should walk the routes before further polish. |
| KEEP / NEEDS OWNER DOGFOOD | `slides/shared_rhythm/week04/`, `slides/shared_rhythm/week05/`, `sidecar/reports/luna/012_weeks4_5_shared_rhythm_slides_report.md`, commit `3f9584a` | Six compiled projector decks and six notes PDFs; double compilation and representative visual inspection were recorded. | Instructor-facing. Grace review/owner visual judgment remains. |
| KEEP / PROVEN | `sidecar/teacher-feedback/`, `sidecar/reports/luna/014_teacher_submission_feedback_loop_report.md`, commit `66dbd75` | Course-18 locked teacher feedback loop with static evidence, safe text handling, and isolated receipts. | Instructor/prototype support. Grace dogfood remains the explicit gate. |
| HISTORICAL EVIDENCE | `sidecar/reports/luna/001D*`, `002F*`, `005_savnac_week2_deployment_report.md`, and related Savnac manifests/readbacks | Shows the visual/prototype path, deployment repairs, and the distinction between repository source and Canvas evidence. | Historical/prototype-only. Preserve; do not treat deployment as source authority. |
| REVISE | Earlier Aider material that jumps from tool availability or model listing toward success without a student prediction and independent proof. | The newer doctrine requires a smaller bite and a visible LOOK → ASK → PREDICT → AIDER → DIFF → RUN → DECIDE loop. | Addressed in this mission in `curriculum/week2/tools.md`; future revisions should preserve the same boundary. |
| DEFER | Week 4/5 slide stitching, broader Commons navigation, and Brandy corpus migration ideas. | Valuable later, but outside the immediate Aider runway and this bounded pass. | Flo later; no action now. |
| REJECT / DO NOT TEACH | Cloud fallback, API-key entry, model substitution, broad “fix everything” Aider requests, or treating a passing model response as code proof. | Unsafe or misleading for the approved local-only course route. | Do not add to student or instructor paths. |

No local-only Brandy curriculum artifact was found outside tracked repository
content. The only scratch file in scope is the byte-pinned mission work file.

## Exactly one second-round target

Target: `curriculum/week2/tools.md`.

The prior route already named the checks but left the student’s prediction and
decision boundary implicit. The small repair adds a seven-step card:
`LOOK -> ASK -> PREDICT -> AIDER -> DIFF -> RUN -> DECIDE`. It also makes the
owner/role/engine/chassis/evidence distinction concrete: the model is the
engine, Ollama the local service, Aider the project-aware chassis, and the
prediction/diff/independent check the evidence. This is one file, 22 added
lines, and does not change the approved model, endpoint, launcher, or Canvas.

Implementation commit: `fc6840e3a4ff7017756eed6b182b75f485271e1b`

## Independent proof

- `git diff --check`: passed before implementation commit.
- Markdown/source review: passed; the card requires one bounded Aider change,
  complete diff inspection, and an independent check.
- `make task-check`: unavailable — exact error: `make: *** No rule to make target 'task-check'. Stop.`
- `make check`: unavailable — exact error: `make: *** No rule to make target 'check'. Stop.`
- No runtime test is defined for this Markdown-only source edit.
- No production Canvas, Savnac course 17, or SWOSU course 24298 was touched.

## Flo stitching map

Flo should later point across, not rewrite, these ingredients:

- Day 0 / machine-first foundation: `curriculum/start-here.md` and the
  canonical `local_ai_lab_setup` relationship in `curriculum/local-ai-lab.md`.
- Day 1 / conversational helper versus repository-working Aider:
  `curriculum/week2/aider-work-first.md` on `origin/main` plus the Week 2
  runway and instructor guide.
- Week 2 Local AI/Aider runway: `curriculum/week2/` and
  `sidecar/reports/luna/005_source_build_report.md`.
- Work First and the student-visible prediction/diff/proof habit:
  `curriculum/week2/tools.md`, `curriculum/week2/aider-work-first.md`, and
  `curriculum/recitation-toolbox.md`.
- Instructor guides and shared-rhythm wrappers: `instructor/` and
  `sidecar/reports/luna/009_week2_shared_rhythm_report.md` plus `010`.
- Staged Week 4/5 decks: `slides/shared_rhythm/week04/` and `week05/`, with
  report `sidecar/reports/luna/012_weeks4_5_shared_rhythm_slides_report.md`.
- Historical failure/prototype evidence: the early visual/deployment reports
  and Savnac manifests/readbacks under `sidecar/`.

Flo was not started, and no Flo keystrokes or watcher actions were sent.

## Completion state

- Commit `fc6840e` is local and intentional; the harvest report is the next
  commit.
- Push is pending until this report is committed, then both forward commits
  will be pushed to `origin/assistant/luna` and verified.
- `foreman_interface` was inspected read-only; its main branch remains
  locally behind `origin/main` and was not mutated.
- No April SSH entry occurred; no Maise migration occurred; no credentials,
  cookies, student data, or private machine state entered Git.
- AGENTS.md: read at shared and repository scope; no update required.
- Next recommended prompt: owner dogfood the Week 2 Local AI/Aider route on
  Savnac course 18, then have Flo stitch the accepted ingredients into one
  course story.

BRANDY HARVESTED — ROUND 2 PROVEN — READY FOR LATER FLO STITCHING
