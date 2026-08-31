# 2026-08-31 — Aider Days navigation hub + CS1/CS2 links

Mission: `foreman_interface/jobs/tasks/cs2_week2_hardware_confidence_and_commons_aider_links_april_20260831.md`
(Phase 2). Urgent, for the 2026-08-31 11:00 CS2 class.

## Source HEAD

- `computing_commons` HEAD at deploy time: `e4100e0ef34bd677d3a391899abecfbfc944f63a`
- New source added this run (committed alongside this report):
  - `scripts/deploy_aider_days_navigation.py`
  - `sidecar/runs/aider_days_navigation_deploy.json` (raw before/after receipt)
- Read-only inputs consulted, not modified: `curriculum/local-ai-lab.md`, `curriculum/week2/aider-work-first.md`, `curriculum/week2/tools.md`, `computer_science_1/lessons/week02-local-ai-*.md`, `computer_science_1` live Canvas course `74029` (read-only).

## Canvas target

Course `24298` (Computing Commons). Course allowlisted on the Canvas client
for this run — no other course id was reachable through the script's
client.

## Before / after module truth

`Aider_Days` (module `219031`) before (1 item):

| position | item id | type | title |
|---|---|---|---|
| 1 | 1531147 | ExternalUrl | aider_day_00_Public_Repo |

`Aider_Days` (module `219031`) after (6 items):

| position | item id | type | title |
|---|---|---|---|
| 1 | 1531235 | Page | Aider Days — Start Here |
| 2 | 1531147 | ExternalUrl | aider_day_00_Public_Repo (unchanged content, repositioned only) |
| 3 | 1531236 | ExternalUrl | Aider Day 1 — Hardware Confidence & the GPU Model Showdown |
| 4 | 1531237 | ExternalUrl | CS2 Week 2 — Hardware Confidence + Getting Started |
| 5 | 1531238 | ExternalUrl | CS1 Week 2 Local AI (shared setup road) |
| 6 | 1531239 | ExternalUrl | Week 2 — Build and Verify Local AI (canonical setup/verification road) |

`02 — Week 2: Build and Verify Local AI` (module `218816`): unchanged
items 1–25 (see prior module truth), plus one new item:

| position | item id | type | title |
|---|---|---|---|
| 26 | 1531240 | ExternalUrl | Continue to Aider Days |

## Defect found and fixed during verification

Canvas creates `ExternalUrl` module items with `published: false` by
default (`Page` items came back published from this run's create call;
`ExternalUrl` items did not). Items 3–6 in `Aider_Days` and the new
`Continue to Aider Days` item in module `218816` were therefore invisible
to students immediately after the initial deploy. Found during the
acceptance readback pass, fixed with `update_module_item` calls setting
`module_item[published]=true` on each, confirmed by re-fetching every
item. All items in both modules are published as of this report.

## Artifacts

- Hub page: `https://swosu.instructure.com/courses/24298/pages/aider-days-start-here` — published, 1294-char body, opened and read back.
- `Aider Day 1` link target (pre-existing, not created this run):
  `https://swosu.instructure.com/courses/24298/pages/the-gpu-aider-model-showdown-in-plain-language` — opened and confirmed live.
- `CS2 Week 2` link target: `https://swosu.instructure.com/courses/74031/modules/218887` — opened and confirmed live (5 items, see CS2 report).
- `CS1 Week 2 Local AI` and `canonical setup road` links both target `https://swosu.instructure.com/courses/24298/modules/218816` — opened and confirmed live (26 items).
- `Continue to Aider Days` link target: `https://swosu.instructure.com/courses/24298/modules/219031` — opened and confirmed live (the hub above).

## Validation / readback evidence

- Read back all `Aider_Days` and Week 2 module items by exact id/position after the write; matches the receipt in `sidecar/runs/aider_days_navigation_deploy.json`.
- Fetched the new hub page directly via the Canvas API: `published: true`.
- Re-listed course `24298` modules: count unchanged at 21 (only modules `219031` and `218816` had item changes; item counts recorded above).
- Re-listed assignment groups for course `24298`: 3 (untouched by this run — this script never calls any assignment/grade/enrollment endpoint).
- The Canvas client used by `scripts/deploy_aider_days_navigation.py` is allowlisted to course `24298` only, so no other course, including CS1 (`74029`), was reachable for a write during this run. CS1 was only ever read through a separate, unrestricted read-only client used for Phase-0/Phase-2 recon.

## What was intentionally not changed

- No grade, submission, enrollment, due date, rubric, or assignment-group object.
- No other Computing Commons module (`00 — Start Here + Kickoff`, `01 — Recitation / Get Help`, Week 3–16 shared-rhythm modules, `04 — Aider Deep Dive & the GPU Model Showdown`, `19 — Professional Pathway`).
- The existing `aider_day_00_Public_Repo` link's own target (`https://github.com/jeremy-evert/aider_day_00`) — only its module-item position moved (1 → 2).
- CS1 production course `74029` — read-only inspection only; no write call was possible (client allowlist) and none was attempted.

## CS1 link — bounded follow-up (not a mission gate)

CS1's production Canvas course (`74029`) has no live Week 2 Local AI
module or items as of this run — its `Week 2: Learning Science` module
(id `218504`) contains only Learning Science content (verified by
listing its 17 items). `computer_science_1`'s own repository already has
substantial Week 2 Local AI lesson source
(`lessons/week02-local-ai-00-start-here.md` through
`week02-local-ai-09-aider-toy-exercises.md`, plus matching exit-ticket
assignments), but it has not been deployed to production Canvas.

Per the mission's explicit instruction ("if the intended final CS1 route
is still behind a real owner/Windows/production gate, link to the best
already-approved durable student-facing artifact that actually works...
do not publish a broken promise"), the `CS1 Week 2 Local AI` door in
`Aider_Days` currently points at the Commons shared Week 2 road
(`218816`) rather than a guessed or staging CS1 URL. This phase did not
mutate CS1 production Canvas, per the mission's firewall.

**Follow-up (not blocking this mission):** deploying CS1's own dedicated
Week 2 Local AI Canvas content to course `74029` is a separate,
owner-authorized CS1 job. Once that lands, the `Aider_Days` hub's CS1
door should be repointed from the shared road to CS1's own live URL.

## Remaining gate / follow-up

One narrow, non-blocking follow-up recorded above (CS1's own Week 2
Local AI Canvas deployment does not yet exist). Every other Phase 2
acceptance-checklist item is satisfied: Aider Days is a real navigation
hub, the Commons Week 2 <-> Aider Days <-> course-specific loop is closed
in both directions, and every new/changed link was opened and read back.
