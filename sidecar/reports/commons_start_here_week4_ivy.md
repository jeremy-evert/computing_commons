# Computing Commons Start Here refresh + week rail — Ivy evidence

Date: 2026-09-08
Role: Ivy / Foreman Intern, for Anna's bite
`jobs/anna/bites/week_rail_and_commons_start_here.md` (5-class layout
campaign, `jobs/tasks/five_class_canvas_layout_rollout.md`). No Canvas
contact of any kind — this is page-body generation only. Anna deploys
from April with read-back verification.

## Part A — reusable week-rail component

Built at `course_foundry` `course_foundry/week_rail.py`
(`render_week_rail(current_week, course_id, overview_slugs, *,
palette="plain"|"commons")`), branch `ivy/week-rail-component`, commit
`3508b3d`. Reused the Canvas-styling discipline already established in
`course_foundry/course_foundry/week_at_a_glance.py`'s
`_render_week_number_nav` rather than inventing a new pattern (checked
there first per Anna's instruction). Full detail, including two
integration fixes made after the Codex worker's first pass (a wrong test
directory, and adding `<strong>` to the current-week chip per Flo's review
comment — real semantic tags survive Canvas's sanitizer where inline
`font-weight` does not), is in that repo's own
`sidecar/reports/week_rail_component_ivy.md`. 9/9 tests pass with the real
project `pytest`.

## Part B — Computing Commons front page

`sidecar/canvas_pages/computing-commons-home.html` is the complete new
page body, ready to paste into `update_page` for course 24298, page
`computing-commons-home`. `sidecar/canvas_pages/computing-commons-home.live-2026-09-08-baseline.html`
is the exact live body Anna supplied (`jobs/anna/reports/commons_front_page_live_2026-09-08.txt`
on `foreman_interface` `anna/five-class-layout-rollout`), kept alongside for
an exact diff rather than re-deriving one.

### Verified byte-identical preservation (self-checked, not just claimed)

Compared the `<nav>` (top navigation), `<header>` (hero), `runway`
section, `lost` section, and `<footer>` between the old and new bodies as
exact substrings: **all five identical, character for character.** Only
the week rail (new), "This week" (header/description/three route cards),
"This week across the courses" (header + placeholder), and "Next week"
sections changed, matching the bite's acceptance test exactly.

### Changes made

1. **Week rail inserted** right under the header, before "This week", via
   `render_week_rail(4, 24298, overview_slugs, palette="commons")`.
2. **"This week · Week 3" → "Week 4"**, description sentence rewritten to
   the real Week 4 content (decompose the task / spell out an argument /
   outside view), replacing the stale Week 3 "grow through a mistake"
   copy.
3. **Three route cards repointed** to the confirmed-live Week 4 pages
   (`monday-ai-fluency-ai-i-week-4-decompose-the-task`,
   `wednesday-professional-minds-week-4-reading-mapping-arguments-for-better-decisions`,
   `friday-professional-minds-week-4-reading-using-the-outside-view-for-better-decisions`),
   with new copy describing each page's actual content instead of
   carrying over Week 3's.
4. **"This week across the courses" header → "(Week 4)"**, but the
   recording-links block and the two course cards were **replaced with
   `{{ANNA: confirm Week 4 CS1/CS2 recording links}}`** rather than
   guessing — I have no way to confirm live whether a Week 4 recording
   package exists per course, or what it contains, without touching
   Canvas. Per the bite: fill this in before deploy, or drop the section
   for this pass if nothing exists yet.
5. **"Next week · Week 4 preview" → "Next week · Week 5 preview"**,
   repointed to the three confirmed-live Week 5 pages Anna gave
   (`monday-ai-fluency-ai-i-week-5-select-the-right-model`,
   `wednesday-professional-minds-week-5-reading-never-judge-a-decision-by-its-outcome`,
   `friday-professional-minds-week-5-reading-the-triumph-of-mediocrity-regression-to-the-mean`),
   with new copy. Dropped the "(optional enrichment)" qualifier from the
   header since that phrasing was specific to Week 4 no-longer-being-next-week
   framing — flag if you want it kept as a standing pattern.

### Week-rail slugs used, per Anna's exact guidance

| Week | Slug | Source |
|---|---|---|
| 1 | `success-foundations-slash-semester-kickoff` | Anna's bite named this as the likely best-fit page for Week 1 content; I did not independently verify it live (can't — no Canvas access) — **please confirm before deploy**. |
| 2 | `week-2-build-and-verify-your-local-ai-lab` | Confirmed live in the body Anna supplied — it's already linked from the existing "runway" section. |
| 3–16 | `week-{N}-shared-rhythm` | Anna confirmed all fourteen live. |
| 17 | *(none — chip renders unlinked)* | Anna's bite: "only ask Anna for a stub for Week 17, which appears to have no content yet." **Missing stub — needs creation before this chip is useful**; the rail component renders it as plain unlinked text rather than a guessed/broken link, so nothing 404s in the meantime. |

### Acceptance-test self-check

- No `<script>`, no `<style>`, no external stylesheet link, no
  `font-weight`/`box-shadow`/`text-transform`/`letter-spacing` anywhere in
  the new body (grepped directly, zero matches for all six).
- Every href in the rail and the changed sections is one of the exact
  slugs Anna live-verified, or the one unverified Week-1 slug flagged
  above — no guessed URLs.
- Untouched-section byte-identity: confirmed above, not just asserted.

### Spend split

Anthropic (Ivy's own reasoning): investigation of `course_foundry` for
prior art, framing/dispatching the Part A Codex bite, reviewing and fixing
its output, and directly authoring the entire Part B page-body diff by
hand (chose direct editing over a second Codex dispatch given the
byte-identical-preservation requirement rewards precision over
generation). OpenAI (Codex, `gpt-5.6-luna`): one bite, Part A's first pass
(the component + its first test draft, before my two integration fixes).
Durable-artifact ratio: high — the rail component is reusable across all
five courses and future weeks by construction (one parameter change moves
the current week); the Commons page-body diff is course/week-specific by
nature and not meant to be reusable beyond this deploy.

## Not done here

- Building the four graded courses' own "Start Here" front pages (CS1,
  CS2, DSCT, Comp Arch) — the campaign's next bites, per the standing task
  file's course order (Commons first, then CS1 → CS2 → DSCT → Comp Arch).
- Any Weeks 1–4 overview-page content correction — separate scope per the
  standing task.
- Creating the Week 17 stub page, or confirming the Week 1 slug live —
  Anna's, since both require Canvas access.

IVY COMMONS START HERE READY FOR ANNA
