# Controller 001 — Computing Commons Visual System + First Vertical Slice

## Mission

Execute the finite campaign defined by:

`sidecar/piper/001_computing_commons_visual_vertical_slice_battle_map.md`

The campaign builds and accepts a reusable visual/navigation system for Computing Commons, proves it on Success Foundations/Kickoff, then applies it to Week 2 Local AI.

This controller authorizes continuation through successful child rounds without waiting for Jeremy between rounds.

## Required reading

Read in this order:

1. `AGENTS.md`
2. `README.md`
3. `docs/build-roadmap.md`
4. `docs/canvas-deployment-gate.md`
5. `docs/canvas-information-architecture.md`
6. `docs/source-registry.md`
7. `sidecar/piper/001_computing_commons_visual_vertical_slice_battle_map.md`
8. `curriculum/start-here.md`
9. `curriculum/success-foundations.md`
10. `curriculum/local-ai-lab.md`

Then execute the child passes below.

## Finite chain

### 001A — Planning / Recon

Execute:

`sidecar/prompts/001A_visual_system_recon_and_plan.md`

Required output:

`sidecar/reports/luna/001A_visual_system_recon_and_plan_report.md`

If the report finds a consequential unresolved owner preference that cannot be safely defaulted, HUMAN NUDGE. Otherwise continue.

### 001B — Build / Visual System + Kickoff

Execute:

`sidecar/prompts/001B_build_visual_system_and_kickoff_prototype.md`

Required output:

`sidecar/reports/luna/001B_visual_system_and_kickoff_build_report.md`

Commit/push accepted build state, then continue.

### 001C — Adversarial Review

Execute:

`sidecar/prompts/001C_adversarial_visual_ux_review.md`

Required output:

`sidecar/reports/luna/001C_adversarial_visual_ux_review_report.md`

If PASS, continue to 001D.

If bounded repairs are required, execute 001R and then re-run the relevant 001C checks before proceeding.

### 001R — Repair, conditional

Execute only when 001C identifies bounded defects:

`sidecar/prompts/001R_visual_system_repair.md`

Required output:

`sidecar/reports/luna/001R_visual_system_repair_report.md`

Do not broaden scope while repairing.

### 001D — Build / Week 2 Local AI Slice

Execute:

`sidecar/prompts/001D_build_week2_local_ai_visual_slice.md`

Required output:

`sidecar/reports/luna/001D_week2_local_ai_visual_slice_report.md`

Commit/push accepted build state, then continue.

### 001E — Acceptance

Execute:

`sidecar/prompts/001E_visual_vertical_slice_acceptance.md`

Required output:

`sidecar/reports/luna/001E_visual_vertical_slice_acceptance_report.md`

Required final verdict:

- `VISUAL SYSTEM ACCEPTED FOR COMMONS BUILD`, or
- `REPAIR REQUIRED`.

Also separately classify Week 2 repository readiness:

- `READY AS REPOSITORY SOURCE FOR LATER CANVAS DEPLOYMENT`, or
- `MORE SOURCE RECONCILIATION REQUIRED`.

## Chain-gun continuation rule

Normal successful completion of a child pass is not a human gate.

Pattern:

**PLAN -> BUILD -> REVIEW -> REPAIR IF NEEDED -> WEEK 2 BUILD -> ACCEPT -> STOP**

Do not expand this campaign into full Commons construction or Canvas deployment.

## Authorized repository posture

Writable:

- `jeremy-evert/computing_commons`

Read-only references as needed:

- `jeremy-evert/computer_science_1`
- `jeremy-evert/swosu_cs_curriculum`
- `jeremy-evert/local_ai_lab_setup`
- `jeremy-evert/windows_classroom`
- `jeremy-evert/ai_fluency`
- `jeremy-evert/professional_minds`
- `jeremy-evert/swosu-computing`

Do not modify the read-only reference repositories.

## Canvas hard gate

Do not write to `https://swosu.instructure.com/courses/24298` or any other production/test Canvas course during this campaign.

This campaign produces repository truth and previews only.

## Final compact handoff

At completion return:

- final verdict;
- final accepted commit SHA;
- design-system path(s);
- Kickoff preview/source path(s);
- Week 2 preview/source path(s);
- review/acceptance report paths;
- whether any old landing/week-navigation pattern was recovered;
- unresolved items;
- confirmation that Canvas was not mutated.
