# Concept Hub — CS2 2026-09-14 entry draft

**Bite:** B3.1 (`foreman_interface/jobs/tasks/b3.1_concept_hub_cs2_entry.md`,
assigned by Anna, run `024fba48ba0195865570bc9f4d1f0837`).
**Target page (Anna deploys, not this draft):** Computing Commons course
24298, `concept-hub-source-control-and-github`.
**Sources used:** `discrete_structures_and_critical_thinking/planning/
git-unit-source-material.md` (real CS1 9/11 + CS2 9/14 transcript quotes)
and the live CS2 page Anna confirmed published (course 74031,
`sept-14-class-recording-recap-and-notes`).

No Canvas contact was made to produce this draft — everything below is
proposed HTML for Anna to paste into the live page body.

## (a) New `<li>` for "Where this has been taught"

Matches the CS1 entry's shape (link + one descriptive clause), and is
honest that GitHub setup was a secondary thread in the CS2 session, not
its dedicated topic — per the source material's own framing of that
session, not invented emphasis.

```html
<li><a href="https://swosu.instructure.com/courses/74031/pages/sept-14-class-recording-recap-and-notes" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/74031/pages/sept-14-class-recording-recap-and-notes" data-api-returntype="Page">CS2, Monday Sept. 14 — Class Recording, Recap &amp; Notes</a> (recording, recap, and notes; GitHub/SSH-key setup was one thread inside a broader session, not the day's dedicated topic)</li>
```

## (b) Rewritten "Backfilled from..." paragraph

Original was factually wrong once a second entry lands ("one real lecture").
Keeps the same instructive close (add an entry each time this concept comes
up again) rather than dropping the guidance.

```html
<p><em>Backfilled from real lectures as they happen — two so far (CS1, CS2). Add an entry here each time this concept comes up again in any course, rather than re-teaching it from scratch on a new page.</em></p>
```

## (c) Judgment call: does CS2 change "The mental models that actually need to land"?

**Decision: leave the six-item list untouched.** Reasoning, checked
against the source material directly rather than assuming Anna's read was
right:

- CS2's "labeled thumb drive" commit framing reinforces existing item 3
  (commit as deliberate checkpoint) — same model, better metaphor, not a
  new model.
- CS2's "push away from the laptop, pull towards the laptop" reinforces
  existing item 2 (local vs. remote is a real, physical distinction) —
  same model.
- CS2's SSH-key-as-written-consent framing reinforces existing item 6
  (asking "how can this hurt me?" as a transferable habit) — same model,
  concrete instance of it.
- The one CS2 idea genuinely *not* already on the list is "clone happens
  once, then forget it" — a real, named fix for the most common student
  confusion (re-cloning every session). I considered adding it as a 7th
  item and decided against it: the section's own framing is explicitly
  about *mental models* ("demonstrating a tool doing the work is not the
  same as a student understanding why it works"), not procedural
  workflow tips. "Don't re-clone" is a **consequence** of genuinely
  understanding item 2 (local and remote are separate, persistent, and
  nothing moves between them until you say so) — once a student has that
  model, "you don't need to re-clone" follows on its own. Adding it as a
  separate numbered item would blur the list from mental models into a
  how-to checklist, which the page already explicitly says is *not* what
  this section is for. Worth a future instructor knowing about as a
  teaching move (name the consequence out loud after teaching item 2),
  but not a new standing entry.
- The other candidate — the CS2/DSCT "Odyssey Gate" vocabulary echo — is
  explicitly out of scope: it's a DSCT-native hook, and the source
  material itself says building that hook is DSCT's own job, not
  something to graft onto the cross-course Concept Hub page.

No change proposed to that section.

## (d) What was kept vs. cut, and why

Kept: the one factual link (CS2 Sept 14 page, already live, already
verified by Anna) and the one-line factual description of what that
session actually covered. Cut: every specific analogy quote from the
source material (thumb drive, push/pull, clone-once, consent framing) —
those already proven-good framings belong in an instructor's *lesson
delivery* the next time this topic is taught, not as a paragraph of
transcript-derived prose pasted onto a standing index page. That's the
"steal the best parts, dump the rest" instruction applied literally: the
page's job is to be a thin index of *where* this has been taught and
*what already needs to land*, not a growing anthology of everyone's best
lines. The existing CS1 entry doesn't quote Jeremy's "18 inches of steel
reinforced concrete" line either, for the same reason — that line lives
in the CS1 lecture notes it links to, not on the hub page itself.

## Acceptance self-check

- Every claim above traces to `git-unit-source-material.md` or the
  already-live CS2 page — no invented content.
- Page still reads as one coherent standing index, not a transcript dump.
- The stale "one real lecture" framing is fixed, not left or silently
  deleted.
- No Canvas contact anywhere in this branch's history.

IVY BITE b3.1-concept-hub-cs2-entry READY FOR ANNA
