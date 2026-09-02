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
- **Voice synthesis → GPU, XTTS-v2.** Runs on **brandy** (Tesla T4, 16GB), not Maise: Maise
  reaches the cluster through a mgmt jump service that mangles long-lived streams, so the NRP
  script/QC jobs have to be driven from brandy anyway, and keeping synthesis on the same host
  avoids a cross-machine handoff. Maise's RTX 2080 Super can be a second synth node once its
  network path is fixed. **Measured on the first real render (Week 3 Fri pilot):** ~0.38x
  realtime — an 8-minute episode rendered in ~3 minutes (30 turns, model load included).
  Two-voice full episodes are cheap; batching the back-catalog is a few GPU-minutes each.
- **April stays out of this entirely.** No NRP job, no TTS render, ever runs on April. April's
  job is: take the finished script + audio and wire it into Canvas the same additive/preflight/
  readback way the lecture-distillation pipeline already does.

## Reference: the pilot

Hand-written shape template:
`professional_minds/presentations/podcast_pilot/week03_fri_resilience_and_risk_competence.md`
— two named voices, question/answer rhythm, a concrete example beat, a closing reflection prompt,
production notes at the bottom.

**First episode built by the real pipeline (2026-09-02):**
`professional_minds/presentations/podcasts/week03_fri/` — script + `.mp3` + QC verdict +
`episode.meta.json`, tracked in `professional_minds/presentations/podcasts/INDEX.md`. Merged to
`main`, ready for April to link from the Week 3 Canvas module.

- Generation: `gpt-oss` via NRP eLLM, 2-stage (beat outline → script), ~22s, verdict PASS.
- QC: `gemma4-12b` via NRP eLLM (independent model), ~4s. Rubric is parser-aware — it judges only
  the `**DANA:**` / `**MARCUS:**` turns, since the synth strips all other scaffolding.
- Synthesis: XTTS-v2 on brandy's T4, voices **Rosemary Okafor** (Dana) / **Viktor Menelaos**
  (Marcus) — built-in speakers, a pilot pick. 8:00, rendered in ~3 min.
- Next voice pass: clone real narrator voices (an instructor + a second reader) — see
  `professional_minds/presentations/podcasts/voices/narration_reference_script.md`. F5-TTS is also
  installed on brandy for a model comparison.

## eLLM access (learned building the pilot)

- `https://ellm.nrp-nautilus.io/v1` — `/chat/completions` **only answers from inside an NRP pod**
  (403 from any workstation); `/models` is open. So generation + QC run as NRP Jobs, never as
  local HTTP.
- Those jobs are driven from **brandy** (public IP). From Maise they fail: `kubectl logs`/`wait`
  route through node kubelets on port 10250, which Maise's mgmt-jump egress can't hold open.
- Non-GPU pods, token from the in-cluster Secret `nrp-llm-token`. Launcher:
  `nrp_k8s_launcher/scripts/nrp_launch_job.py` (needed a TTL/`kubectl wait` robustness fix —
  branch `fix/ttl-and-wait-hang`).

## Open items

- Decide episode cadence: Professional Minds has a Wed+Fri weekly reading — both, or Friday only
  to start? World Bible cadence is one per course per week where a lecture used the framing.
- Batch the remaining Professional Minds readings once cadence is set (one NRP job per reading).
- Wire CS1/CS2 lecture-digest and World Bible tracks in.
- Lock final voices (cloned) and, if F5-TTS wins the comparison, switch the synth engine.
- April: link the Week 3 Fri `.mp3` from its Canvas module (additive item, same pattern as
  recording/slides/notes), then repeat per episode as they land in `INDEX.md`.
