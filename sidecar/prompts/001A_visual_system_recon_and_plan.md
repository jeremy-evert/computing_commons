# 001A — PLAN / RECON — Visual System and Lost Navigation Hunt

## Purpose

Before building a new visual language, inspect current truth and look for the strong prior landing/navigation treatment Jeremy remembers.

## Read first

- `AGENTS.md`
- `docs/canvas-information-architecture.md`
- `curriculum/start-here.md`
- `curriculum/success-foundations.md`
- `curriculum/local-ai-lab.md`
- `sidecar/piper/001_computing_commons_visual_vertical_slice_battle_map.md`

## Recon

Inspect current files and Git history in the authorized read-only repositories, especially `computer_science_1`, `swosu_cs_curriculum`, and `swosu-computing`, for useful prior patterns such as:

- semester landing page;
- Week at a Glance;
- weekly pager;
- week strip/bar;
- semester map;
- Next/Back navigation;
- Start Here tiles/cards;
- visually strong Canvas-ready HTML.

Search deleted/history content as practical. Do not spend the whole mission archaeologizing. If the old page cannot be recovered efficiently, document that and proceed with a new design grounded in the owner's remembered feature: a compact bottom week bar.

## Plan

Propose one small design system suitable for Canvas content pages.

It must prioritize:

- accessibility;
- simple visual hierarchy;
- consistent navigation;
- reliable links;
- mobile/narrow screens;
- Canvas-safe HTML;
- low maintenance;
- reusable components;
- restrained colors rather than decoration for decoration's sake.

Explicitly decide how to represent the bottom semester/week strip without implying that the post-Week-2 Recitation Toolbox is a rigid week-by-week curriculum.

Identify exact source files for the Kickoff prototype and Week 2 Local AI slice.

## Do not

- build the final pages yet;
- modify Canvas;
- modify reference repositories;
- introduce external JavaScript or required external CSS;
- rewrite source curriculum merely to fit a design idea.

## Deliverable

Write:

`sidecar/reports/luna/001A_visual_system_recon_and_plan_report.md`

Include:

- repositories/paths/history inspected;
- whether the old landing/week bar was recovered;
- useful patterns found;
- proposed palette/component grammar;
- proposed navigation grammar;
- Canvas-safe implementation strategy;
- Kickoff source map;
- Week 2 source map;
- implementation file plan for 001B and 001D;
- unresolved risks;
- verdict `READY FOR 001B BUILD` or `HUMAN NUDGE REQUIRED`.

Commit and push the report before continuing.
