# 001B — BUILD — Reusable Visual System + Kickoff Prototype

## Preconditions

Read and honor:

- `sidecar/reports/luna/001A_visual_system_recon_and_plan_report.md`
- `sidecar/piper/001_computing_commons_visual_vertical_slice_battle_map.md`

Proceed only if 001A says `READY FOR 001B BUILD`.

## Build objective

Create the smallest reusable visual/navigation system that can make Computing Commons pages polished, consistent, accessible, and easy to maintain.

Then prove it on **Success Foundations / Semester Kickoff** using real Commons content.

## Required design-system outputs

Create durable project material for at least:

- visual palette and contrast rules;
- typography/heading grammar compatible with Canvas;
- masthead/header pattern;
- primary/secondary action patterns;
- callouts for information, evidence/success, warning, and recovery;
- Recitation/Get Help treatment;
- Next / Back / Home navigation;
- compact bottom semester/week strip;
- labels/treatments for AI Fluency, Professional Minds, Local AI Lab, and Recitation Toolbox;
- Canvas-safe HTML guidance;
- reusable landing/content/activity page templates.

Prefer plain HTML with inline or Canvas-safe styling that survives normal Canvas sanitization. Do not require JavaScript.

## Kickoff prototype

Use current `curriculum/success-foundations.md` and related current Commons truth to create a polished student-facing Kickoff landing experience.

The page should answer immediately:

1. Where am I?
2. What do I do?
3. How do I know I succeeded?
4. Where do I go next?
5. Where do I get help?

Include the bottom semester/week strip as designed in 001A.

Create a local/repository preview that can be opened outside Canvas for visual inspection.

## Validation

At minimum validate:

- internal links resolve where practical;
- headings are structurally ordered;
- contrast choices are documented and defensible;
- content remains usable without color;
- layout degrades cleanly at narrow width;
- no required external JavaScript/CSS dependency exists;
- the template is clearly reusable rather than hard-coded only for Kickoff.

## Do not

- write to Canvas;
- alter shared source repositories;
- migrate CS1 material;
- redesign every Commons page;
- add decorative complexity that increases maintenance without improving orientation.

## Deliverable

Write:

`sidecar/reports/luna/001B_visual_system_and_kickoff_build_report.md`

Include exact created/changed paths, validation performed, preview path, known limitations, and commit SHA.

Commit and push the build before handing to 001C.
