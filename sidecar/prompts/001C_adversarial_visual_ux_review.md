# 001C — REVIEW — Adversarial Visual / UX / Accessibility Review

## Role

Act as a skeptical student, accessibility reviewer, Canvas maintainer, and future course author.

Review the 001B visual system and Kickoff prototype. Do not assume the builder's choices are good because they are polished.

## Inspect

Read:

- `sidecar/reports/luna/001A_visual_system_recon_and_plan_report.md`
- `sidecar/reports/luna/001B_visual_system_and_kickoff_build_report.md`
- all design/template/preview files created in 001B.

## Review questions

### Student orientation

Can a first-time student quickly answer:

- Where am I?
- What do I do now?
- How do I know I am done?
- Where do I go next?
- Where do I get help?

### Navigation

- Are Home / Back / Next positions consistent?
- Does the bottom week/semester strip help rather than confuse?
- Does it avoid implying that the Recitation Toolbox is week-locked?
- Are links deterministic and understandable?
- Is there a clear recovery route from a wrong turn?

### Accessibility

- Is heading order sensible?
- Is contrast adequate?
- Does meaning survive without color?
- Are link labels descriptive?
- Are decorative treatments separable from semantic content?
- Is the page usable on narrow screens?

### Canvas resilience

- Is the HTML likely to survive normal Canvas sanitization?
- Is required functionality independent of JavaScript/external CSS?
- Are there brittle assumptions about institutional theming?

### Maintainability

- Can another page reuse the design without copy-paste chaos?
- Can a color/navigation change be made predictably?
- Is the design system small enough to remember?
- Has visual polish created unnecessary authoring burden?

### Tone / cognitive load

- Is the page calm enough for a student who is already confused?
- Are important actions visually stronger than optional context?
- Is there too much text before the first action?

## Validation

Use available local tools to inspect/render previews as practical. Run link/basic HTML checks where possible. Preserve concrete evidence.

## Deliverable

Write:

`sidecar/reports/luna/001C_adversarial_visual_ux_review_report.md`

Return exactly one verdict:

- `PASS — READY FOR WEEK 2 APPLICATION`
- `BOUNDED REPAIR REQUIRED`
- `RETHINK REQUIRED`

If repair is needed, provide the smallest ordered repair list. Do not implement repairs in this pass.

Commit and push the review report.
