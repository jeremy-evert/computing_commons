# Controller 002 — Brandy + Savnac Week 2 Visual Chain

## Mission

Execute the bounded campaign defined by:

`sidecar/piper/002_brandy_savnac_week2_visual_battle_map.md`

Build the reusable Computing Commons visual/navigation system, prove it on Kickoff, apply it to Week 2 Local AI, deploy the bounded slice to Savnac, verify the live test rendering structurally, and stop for Jeremy's visual inspection from Grace.

This controller authorizes continuation through normal successful child rounds without waiting for Jeremy until the explicit owner visual gate.

## Host / operating context

- Host: **Brandy**
- Owning local Git root: `/mnt/brandy_nvme/jevert/git`
- Expected Commons checkout: `/mnt/brandy_nvme/jevert/git/computing_commons`
- Savnac VM/Canvas runs on Brandy under the operating doctrine in `jeremy-evert/Savnac`.

Flo/April/S'MOOR is outside this mission.

## Required reading

Read in this order:

1. `AGENTS.md`
2. `README.md`
3. `docs/build-roadmap.md`
4. `docs/canvas-deployment-gate.md`
5. `docs/savnac-prototype-loop.md`
6. `docs/canvas-information-architecture.md`
7. `docs/source-registry.md`
8. `sidecar/raw/2026-08-23_savnac_visual_quick_tune_dogfood_owner_direction.md`
9. `sidecar/piper/002_brandy_savnac_week2_visual_battle_map.md`
10. current Savnac `START_HERE.md` and REQ-001 runbook/readiness before any live test mutation.

## Finite chain

### 002A — Visual recon

Execute the intent in:

`sidecar/prompts/001A_visual_system_recon_and_plan.md`

Required output remains:

`sidecar/reports/luna/001A_visual_system_recon_and_plan_report.md`

Efficiently hunt for the old attractive landing/week-strip pattern, including CS1/current history if locally available. Do not stall indefinitely if it cannot be recovered.

### 002B — Build visual system + Kickoff prototype

Execute:

`sidecar/prompts/001B_build_visual_system_and_kickoff_prototype.md`

Required output:

`sidecar/reports/luna/001B_visual_system_and_kickoff_build_report.md`

Commit/push accepted source state.

### 002C — Adversarial UX review

Execute:

`sidecar/prompts/001C_adversarial_visual_ux_review.md`

Required output:

`sidecar/reports/luna/001C_adversarial_visual_ux_review_report.md`

If bounded defects are found, execute `sidecar/prompts/001R_visual_system_repair.md`, write its report, and rerun the relevant review checks. Do not broaden scope.

### 002D — Build Week 2 Local AI slice

Execute:

`sidecar/prompts/001D_build_week2_local_ai_visual_slice.md`

Required output:

`sidecar/reports/luna/001D_week2_local_ai_visual_slice_report.md`

Use `local_ai_lab_setup` + `windows_classroom` as canonical technical sources. Do not invent a third Local AI procedure.

### 002E — Repository source acceptance

Execute the checks in:

`sidecar/prompts/001E_visual_vertical_slice_acceptance.md`

Required output:

`sidecar/reports/luna/001E_visual_vertical_slice_acceptance_report.md`

Proceed to Savnac only if the visual system verdict is:

`VISUAL SYSTEM ACCEPTED FOR COMMONS BUILD`

and Week 2 is at least:

`READY AS REPOSITORY SOURCE FOR LATER CANVAS DEPLOYMENT`

Within Controller 002, “later Canvas deployment” now means the bounded Savnac test deployment authorized below, **not** SWOSU Canvas 24298.

### 002F — Deploy bounded slice to Savnac

Execute:

`sidecar/prompts/002F_deploy_week2_visual_slice_to_savnac.md`

Required output:

`sidecar/reports/luna/002F_savnac_week2_deployment_report.md`

Required verdict:

`SAVNAC VISUAL SLICE DEPLOYED FOR OWNER INSPECTION`

### 002G — Live read-back + Grace visual handoff

Execute:

`sidecar/prompts/002G_savnac_readback_and_owner_visual_handoff.md`

Required output:

`sidecar/reports/luna/002G_savnac_owner_visual_handoff.md`

Required final status:

`OWNER VISUAL INSPECTION REQUIRED`

Then stop.

## Savnac authorization

The Savnac Canvas instance is an authorized mutable test range for this campaign.

Luna may create or update a clearly labeled Computing Commons prototype course and the bounded pages/modules/0-point assignments needed for this vertical slice.

Use Savnac's protected admin credential from its documented Brandy location without printing or committing it.

Do not perform VM/network/libvirt/firewall/sshd changes merely to make course content easier. If the established access path proves broken and cannot be worked around without infrastructure mutation, stop with a narrow HUMAN NUDGE and evidence.

## Repository permissions

Writable repository:

- `jeremy-evert/computing_commons`

Read-only reference repositories:

- `jeremy-evert/Savnac`
- `jeremy-evert/Savnac_quick_tune`
- `jeremy-evert/synthetic_student_laboratory`
- `jeremy-evert/computer_science_1`
- `jeremy-evert/swosu_cs_curriculum`
- `jeremy-evert/local_ai_lab_setup`
- `jeremy-evert/windows_classroom`
- `jeremy-evert/ai_fluency`
- `jeremy-evert/professional_minds`
- `jeremy-evert/swosu-computing`

Do not modify read-only repositories during this chain.

## Hard gates

Do not:

- touch `https://swosu.instructure.com/courses/24298`;
- touch any other SWOSU production Canvas state;
- enroll/remove real students;
- read/copy student submissions, grades, comments, or identities;
- execute `Savnac_quick_tune` yet;
- launch synthetic-student experiments yet;
- dogfood Grace on Jeremy's behalf;
- record final videos;
- clean/migrate CS1 or other home course repositories;
- interfere with Flo/S'MOOR work on April.

## HUMAN NUDGE threshold

Pause only for:

- Jeremy's required visual judgment after 002G;
- credential/access failure with no existing authorized lane;
- a required infrastructure mutation outside this mission;
- destructive/safety issue;
- unsafe repository state;
- unresolved consequential ambiguity.

Normal plan/build/review/repair/deploy/read-back transitions are not human gates.

## Final handoff

Return only after 002G with:

- repository visual-system verdict;
- Week 2 source verdict;
- final accepted Commons commit SHA;
- Savnac prototype course/object manifest path;
- Savnac deployment/read-back report paths;
- exact Grace/home visual access instructions;
- old landing/week-strip recovery result;
- unresolved items;
- confirmation that Quick Tune and synthetic students have **not** run yet;
- confirmation that SWOSU Canvas course 24298 was untouched;
- final sentinel: `OWNER VISUAL INSPECTION REQUIRED`.
