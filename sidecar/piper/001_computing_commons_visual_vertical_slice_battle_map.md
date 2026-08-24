# Piper Battle Map 001 — Computing Commons Visual System + First Vertical Slice

Date: 2026-08-23
Status: **AUTHORIZED BUILD CAMPAIGN / NO CANVAS DEPLOYMENT**

## Mission

Build the visual and navigation foundation for the SWOSU Computing Commons in Git first.

The first goal is not to decorate every page. The goal is to create a small, reusable Canvas-safe design system that makes the Commons easy for students and easy for Jeremy to maintain.

The first two proving surfaces are:

1. **Success Foundations / Semester Kickoff** — use this as the low-risk visual prototype because the content is already largely settled.
2. **Week 2 / Build and Verify Your Local AI Lab** — apply the accepted visual/navigation system to the first important shared technical experience.

Week 2 is the first real target. Kickoff is the design-system proving ground.

## Owner intent

Jeremy remembers a previous course landing page that was especially good and had a compact bar of weeks along the bottom. That exact artifact is not currently known. Before inventing a replacement, search the current repository set and relevant Git history for prior landing-page/week-navigation patterns worth recovering.

The new system should feel polished but not fragile. Priorities are:

1. obvious navigation;
2. consistent page grammar;
3. working links;
4. accessible contrast and headings;
5. useful color and visual hierarchy;
6. mobile-friendly behavior;
7. low maintenance cost;
8. visual polish.

Pretty is valuable only when it makes the course easier to use.

## Battlefield

### Owning repository

`jeremy-evert/computing_commons`

Expected Maise checkout:

`/mnt/nora/git/computing_commons`

### Read-only reconnaissance sources

Inspect as needed, but do not modify during this campaign:

- `jeremy-evert/computer_science_1`
- `jeremy-evert/swosu_cs_curriculum`
- `jeremy-evert/local_ai_lab_setup`
- `jeremy-evert/windows_classroom`
- `jeremy-evert/ai_fluency`
- `jeremy-evert/professional_minds`
- `jeremy-evert/swosu-computing`

Use Git history where useful to search for a lost/retired landing page, semester map, weekly pager, week strip, or similar navigation treatment.

### Future Canvas target

`https://swosu.instructure.com/courses/24298`

**Do not write to Canvas in this campaign.** Canvas deployment begins only after the Commons repository receives a separate acceptance verdict of `READY FOR COMPUTING COMMONS CANVAS DEPLOYMENT`.

## Visual design contract

Create a reusable system rather than individually styling pages.

At minimum define:

- Commons masthead/header;
- page title + short purpose line;
- primary action treatment;
- secondary/navigation links;
- information/success/warning/recovery callouts;
- evidence/completion box;
- Recitation/Get Help box;
- Next / Back navigation;
- stable Home link;
- compact bottom semester/week navigation strip;
- AI Fluency / Professional Minds / Local AI / Toolbox visual labels;
- accessible palette and contrast rules;
- Canvas-safe HTML constraints;
- mobile/narrow-width behavior.

Do not depend on custom JavaScript, external CSS that Canvas may strip, or fragile institutional theme overrides.

The bottom week strip may show the semester rhythm, but must not falsely imply that the Recitation Toolbox is locked to fixed weeks after Week 2. It is secondary navigation, not the curriculum model.

## Desired student experience

Every important page should make four answers obvious:

1. **Where am I?**
2. **What do I do?**
3. **How do I know I succeeded?**
4. **Where do I go next?**

A fifth path should always be easy to find:

**I am stuck → Recitation / Get Help**

## Campaign passes

### Pass 001A — PLAN / RECON

- inspect current Commons truth;
- search CS1 and related repos/history for prior strong landing/navigation patterns;
- inventory Canvas-safe design constraints already known in project sources;
- identify exact Kickoff and Week 2 source objects to compose;
- propose the smallest reusable visual system;
- produce a planning report and implementation plan.

No student-facing build in this pass except tiny throwaway experiments needed to validate feasibility.

### Pass 001B — BUILD / VISUAL SYSTEM + KICKOFF PROTOTYPE

- implement the reusable visual system in the Commons repo;
- create templates/components and documentation;
- build a polished Kickoff/Success Foundations prototype using real content;
- include the bottom week/semester strip;
- generate local preview artifacts suitable for visual inspection;
- keep all links deterministic and repo-relative where possible.

### Pass 001C — REVIEW / ADVERSARIAL UX + ACCESSIBILITY

Review 001B as a skeptical student and maintainer.

Check:

- navigation consistency;
- link integrity;
- accessibility/contrast/heading order;
- mobile/narrow layout;
- Canvas sanitizer compatibility assumptions;
- visual noise;
- whether the week strip helps or confuses;
- whether Recitation/help is easy to find;
- whether templates are actually reusable;
- whether a maintainer can change one component without hand-editing dozens of pages.

Return PASS or a bounded repair list.

### Pass 001R — REPAIR, only if needed

Apply the smallest repair set needed to clear 001C, then re-run the relevant checks.

### Pass 001D — BUILD / WEEK 2 LOCAL AI VERTICAL SLICE

Apply the accepted design system to the Week 2 Local AI experience.

Use canonical source truth from:

- `local_ai_lab_setup` for the instructional product;
- `windows_classroom` for accepted Windows evidence/contract;
- current Commons source registry and Local AI composition page.

Do not invent a third Local AI procedure.

Create a polished Week 2 landing/student route showing:

- what Week 2 is for;
- the ordered student path;
- completion/evidence expectations;
- recovery/help route;
- clear navigation in/out;
- the same visual grammar as Kickoff.

### Pass 001E — ACCEPTANCE

Perform a final campaign acceptance review of the visual system + Kickoff + Week 2 slice.

Required verdicts:

- `VISUAL SYSTEM ACCEPTED FOR COMMONS BUILD`, or
- `REPAIR REQUIRED`.

Also state separately whether Week 2 is:

- `READY AS REPOSITORY SOURCE FOR LATER CANVAS DEPLOYMENT`, or
- `MORE SOURCE RECONCILIATION REQUIRED`.

This is **not** the full Commons Canvas deployment gate.

## Required durable outputs

Luna may choose exact supporting filenames, but the campaign must leave at minimum:

- a visual/design-system specification;
- reusable Canvas-safe page templates/components;
- a polished Kickoff/Success Foundations prototype;
- a polished Week 2 Local AI prototype;
- local preview artifacts or renderable HTML for both;
- automated/basic link checks where practical;
- a planning report;
- an adversarial review report;
- a final acceptance report/manifest.

Keep project evidence under the owning repository, preferably `sidecar/reports/luna/` and reusable product material under appropriate `design/`, `curriculum/`, or `canvas/` paths.

## Hard boundaries

Do not:

- mutate Canvas course 24298;
- enroll or remove students;
- change production gradebooks;
- delete/migrate CS1 material in this campaign;
- rewrite canonical Local AI, AI Fluency, or Professional Minds source repositories;
- introduce ZyBooks dependencies;
- use external JavaScript or fragile CSS hacks as required functionality;
- claim the whole Commons is complete;
- record final instructional videos.

## Git / durability

- Protect pre-existing work.
- Use forward commits only.
- Commit and push accepted pass outputs.
- Record exact source commits/paths used when composing shared material.
- A worker `DONE` is a claim, not acceptance.
- Stop only at a genuine human/production/destructive/capability gate.

## Definition of victory

At the end of this campaign, Jeremy should be able to open two local/repository previews, Kickoff and Week 2, and say:

> “Yes. This is what Computing Commons should feel like.”

The design should then be reusable across the remaining Commons build without turning every page into a custom web-design project.
