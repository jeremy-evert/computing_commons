# Commons Home — Week 3 show-day update

**Date:** 2026-09-01
**Target:** production Canvas course 24298 (Computing Commons, `CC101`), front page `computing-commons-home`
**Trigger:** Jeremy wanted this ready to show in DSCT class the same day.

## What changed (all additive)

1. **"This week" moved from Week 2 to Week 3.** The three day-route cards now
   point at the already-live Week 3 shared-rhythm pages (previously shown as
   the "Next week preview"):
   - Monday — AI Fluency: Plan the Work (`monday-ai-fluency-plan-the-work`)
   - Wednesday — Professional Minds: Grow through mistakes
     (`wednesday-professional-minds-grow-through-mistakes`)
   - Friday — Professional Minds: Resilience and risk competence
     (`friday-professional-minds-resilience-and-risk-competence`)

2. **New section "This week across the courses (Week 3)"** with the two
   Monday lecture recordings (SharePoint stream links, provided by Jeremy)
   and a skimmable, per-course "what changed" summary:
   - CS1 (Week 3: Growth) — new Aug 31 lecture package (student notes,
     distilled deck with real de-identified screenshots, instructor digest,
     recording link); Week 2 assignments unchanged.
   - CS2 (Week 3 — Found Your World) — new Aug 31 lecture package (student
     notes "Runs Usefully", distilled deck, digest, recording link); existing
     "Found Your World" pages got a conservative typo/voice cleanup.

3. **"Next week" preview moved from Week 3 to Week 4**, pointing at the
   already-live, explicitly-optional Week 4 Commons enrichment pages
   (Decompose the Task / Mapping Arguments for Better Decisions / Using the
   Outside View for Better Decisions).

4. Header, "Keep your technical runway moving," and "Lost or blocked?"
   sections are unchanged.

## Verification before publish

- Confirmed course identity (`24298`, `CC101`) via a fresh `GET` immediately
  before the write.
- Confirmed the live page still said "This week · Week 2" before mutating
  (proves the read was current).
- `HEAD`/`GET`-checked all nine linked Canvas page URLs used in the new body
  (Week 3 day pages, Week 4 day pages, Local AI Lab, Aider bridge,
  Recitation/Get Help) — all returned `200` before publish.

## Verification after publish

- `PUT` succeeded; `updated_at` advanced from `2026-08-24T14:11:55Z` to
  `2026-09-01T15:09:31Z`; `published: true`.
- Independent `GET` readback confirms: "This week · Week 3" present, "This
  week · Week 2" gone, both video-link ids present, the runway and
  lost/blocked sections still present verbatim.
- Both SharePoint recording links were checked directly: each resolves (302)
  to a real, correctly-named recording matching the intended course/date —
  `.../Fall 2026 Computer Science I (COMSC-1033-1415)-20260831_095929-...`
  for CS1 and `.../Fall 2026 Computer Science II (COMSC-1053-1417)-20260831_130202-...`
  for CS2. Full playback then requires SWOSU SSO (a `401` on an anonymous,
  cookie-less fetch of the player page) — expected behavior for a signed-in
  student clicking from Canvas, not a broken link.

## Noted but out of scope for this update

Listing the course's pages during this pass turned up a page named
`week-3-shared-rhythm-2` with `updated_at: 2026-09-01T15:07:28Z` — created
almost the same minute as this edit, alongside the pre-existing
`week-3-shared-rhythm`. This was not touched and is not linked from the Home
page either before or after this change. Flagging it as a possible
concurrent-edit artifact (a job may have been running against this course at
the same time) worth a look, not something this update caused or fixed.
