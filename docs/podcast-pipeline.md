# Podcast pipeline — script generation (NRP) + voice synthesis (Maise)

## Status

Design/handoff doc. No NRP job or TTS pipeline has been built yet. This is the plan Jeremy
takes to Maise to build with Flo. April (this host) does not run NRP jobs or TTS — it stays
scoped to student-facing Canvas writes and the lecture-distillation pipeline it already runs.

## Why this exists

A one-off pilot script (`professional_minds/presentations/podcast_pilot/week03_fri_resilience_and_risk_competence.md`,
Week 3 Friday reading, two-host format) proved the idea is worth doing. Doing it for real, every
week, across every course, should not burn Anthropic tokens on bulk generation — that work moves
to NRP (larger model, batch, cheap) with a lightweight QC pass in front of anything that publishes.

## Standing policy (set 2026-09-02)

- **Publish sooner rather than later.** Default posture has shifted toward more exposure, not
  less. Digests/notes/decks/podcasts go public once reviewed — don't hold things back by default.
- Review still gates publish (a QC pass, human or model, happens before anything goes out) — the
  change is that review should be fast and lightweight, not that review is skipped.

## Content sources (three tracks, same pipeline shape)

1. **Professional Minds weekly readings** (`professional_minds/readings/week_NN_{wed,fri}_*.md`)
   — already clean, de-identified text. Lowest-risk source, use this to validate the pipeline end
   to end first.
2. **CS1 / CS2 lecture digests** (`sidecar/lecture_notes/*_lecture_digest.md` in each course repo)
   — produced weekly by the existing lecture-distillation pipeline (see
   `sidecar/reports/*_lecture_distillation.md` in `computer_science_1` / `computer_science_2` for
   the established pattern: transcribe → de-identify → digest → deck → Canvas). Already
   de-identified by the time this pipeline sees them.
3. **New: World Bible podcast** (see below) — a weekly *concept* episode, not a lecture recap.

## New track: the World Bible podcast

Both CS1 and CS2 frame their applied work through a shared fictional "World Bible" — a
frontier-settlement / starship-log narrative students build programs inside of (CS2's Week 3
module is literally titled "Found Your World (World Bible v0.1)"; CS1's Sept. 2 lecture used the
same frontier-settlement framing to introduce that week's Python work).

The ask: **one podcast episode per week, per course (so two episodes some weeks, since CS1 and
CS2 move at different paces), that teaches that week's one fundamental technical concept through
the World Bible narrative** — not a lecture summary, a standalone "here's the idea, told as part
of the world's story" episode a student could listen to instead of / alongside reading.

Source material for each episode: that week's lecture digest (what was actually taught) plus
whatever World Bible narrative material already exists for that course/week. Do not invent
technical content that wasn't actually covered — same non-negotiable the lecture-distillation
pipeline already holds.

## Pipeline shape

```
source text (reading / digest / world-bible topic)
        |
        v
  [ NRP job: script generation ]   <- larger model, batch, one script per topic
        |
        v
  [ QC pass ]                       <- cheap model (or lightweight Claude review), checks
        |                              tone + factual fidelity against source, not a rewrite
        v
  [ Maise: XTTS-v2, GPU ]           <- two-voice synthesis, RTX 2080 Super (8GB VRAM)
        |
        v
  audio file + script committed to the owning repo, linked from Canvas
```

- **Script generation → NRP.** One job per topic (reading, digest, or World Bible concept). Keep
  the two-host script shape used in the pilot: a host who asks questions, a co-host who carries
  the source material's ideas, plain spoken language, runtime roughly matching the source reading
  time (7-9 min for Professional Minds readings; scope World Bible episodes similarly once the
  first one is timed).
- **QC pass** — checks the script doesn't drift from the source (no invented claims, no exposed
  student data if the source was a lecture digest), and that tone lands. This is the fast/cheap
  gate that keeps the "publish sooner" policy safe.
- **Voice synthesis → Maise, XTTS-v2.** GPU job, not CPU — Maise's RTX 2080 Super (8GB VRAM) is
  the only GPU in this fleet suited to it. Time-per-episode is unmeasured; expect roughly 1-3x
  realtime for a two-voice XTTS-v2 render (i.e. ballpark 10-25 min for a 9-minute episode) — get a
  real number from the first render and correct this doc.
- **April stays out of this entirely.** No NRP job, no TTS render, ever runs on April. April's
  job is: take the finished script + audio and wire it into Canvas the same additive/preflight/
  readback way the lecture-distillation pipeline already does.

## Reference: the pilot

`professional_minds/presentations/podcast_pilot/week03_fri_resilience_and_risk_competence.md` —
first full script, generated inline (not via NRP) as a proof of concept from
`professional_minds/readings/week_03_fri_resilience_and_risk_competence.md`. Use it as the shape
template for the NRP prompt: two named voices, question/answer rhythm, a concrete example beat,
a closing reflection prompt, production notes at the bottom.

## Open items for the Maise/Flo session

- Stand up the actual NRP job (model choice, batch shape, one script per topic file found in the
  three source tracks above).
- Pick and wire up the QC pass (which model, what it's allowed to change vs. just flag).
- Install/configure XTTS-v2 on Maise, pick two consistent voice profiles (reused across all
  episodes for continuity), render the pilot script as the first real timing/quality test.
- Decide episode cadence: Professional Minds already has a Wed+Fri weekly reading; decide whether
  both get episodes or just Friday initially. World Bible cadence is one per course per week where
  a lecture actually used the framing that week.
- Once a real render exists, correct the timing estimate in this doc and decide the publish path
  (where the audio file lives, how it's linked from each course's Canvas module — likely the same
  additive-item pattern as the recording/slides/notes items already in use).
