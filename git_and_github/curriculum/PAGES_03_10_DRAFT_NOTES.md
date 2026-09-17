# Draft notes — curriculum pages 03-10 (Ivy)

**Bite:** B3.2 (`foreman_interface/jobs/tasks/b3.2_git_curriculum_pages_03_10.md`,
assigned by Anna, run `024fba48ba0195865570bc9f4d1f0837`).
**Branch:** `ivy/git-curriculum-pages-03-10` in `computing_commons`.

No Canvas contact was made to produce these pages — all eight are draft
repo files for Anna to review before any push to course 24298.

## Why I drafted these directly instead of dispatching Codex per-page

The bite flagged this as a good fit for Codex dispatch given the size (8
pages). I made the call to draft them directly instead: the README already
specifies each section in near-final depth (core question, concepts,
worked command sequences, misconceptions, completion signal), so this was
closer to "expand a tight spec into the existing page shell" than open
invention — a case where reading 00/01/02 once for voice and then writing
against a spec I already had fully in context was faster and more
reviewable than setting up eight isolated worktrees, writing eight
dispatch prompts, and reviewing eight Codex deliveries for consistency
with each other. Flagging this explicitly per the standing playbook's
"your call" — happy to redo any individual page via Codex if Anna wants a
second independent pass on one.

## Per-page: README-direct vs. filled-in

- **03 (Status and Diff Are the Truth):** Almost entirely README-direct —
  the spec's concepts, commands, and "AI-era principle" section map
  straight onto the page. What I added: a worked example showing the
  actual `git status`/`git diff`/`git diff --staged` sequence against a
  one-line edit, since the README names the commands but not a concrete
  before/after.
- **04 (Make One Tiny Human Change):** README-direct for the command
  sequence and teaching emphasis. Filled in: a suggested tiny edit
  (README or comment change) since the README doesn't specify one, and an
  explicit forward pointer connecting this loop to lesson 06's AI version
  of the same loop (continuity move, not new content).
- **05 (AI at the Keyboard):** README-direct almost entirely — the spec
  here is already close to full prose. I reused the real classroom
  scope-creep example from `02_ai_git_safety_belt_lab.md` (the
  print-statement addition) rather than inventing a new one, since it's
  the same lesson the README's stop-conditions section is clearly
  gesturing at and it's already-real evidence, not a hypothetical.
- **06 (Give AI One Bounded Change):** Structure is README-direct (the
  same bound-task / inspect / verify / commit / reflect loop as the
  integrated lab). **Filled in, with an explicit assumption stated on the
  page:** I gave this exercise its own small bounded task
  (`largest_category(pretzels, raisins, chocolate)`) rather than reusing
  02's exact `average_pieces_per_category` task, so a student who already
  did the integrated lab isn't just repeating identical work. If Anna
  wants this page to use the *same* task as 02 instead for stricter
  continuity, that's a one-function swap, not a rewrite.
- **07 (Branches, PRs, Conflicts, Recovery):** README-direct — the
  branches/PR/conflict/recovery-ladder content was already close to full
  prose in the spec. No invented content beyond connecting it back to the
  branch already created in page 06, for continuity.
- **08 (Break Something Small, Recover, Verify):** The README specifies
  the *shape* of this exercise (break, capture, diagnose, recover, verify,
  prove) but not the specific break. **Open question for Anna, stated on
  the page itself:** I invented one concrete, bounded break — changing the
  servings divisor in `trail_mix.py` from 5 to 4 — chosen because it's a
  one-line, easy-to-explain failure consistent with the functions already
  established in 02/06. If a different canonical break already exists
  elsewhere (e.g., in an instructor-only answer key I don't have access
  to), swap it in; the loop structure around it doesn't change.
- **09 (Secrets, Ignore Rules, Hygiene):** README-direct — this section
  was already near-complete prose in the spec (topics list, AI-era
  warning). What I added: explicit connective tissue back to lesson 06's
  `.gitignore` moment from the integrated lab and to lesson 05's stop
  conditions, so it doesn't read as an isolated topic.
- **10 (Publish a Git Evidence Receipt):** README-direct for the required
  receipt fields and recommended command capture (I did not change or add
  any field). Filled in: a worked example receipt at the end, since the
  README specifies the *shape* of a receipt but the existing 00/01 pages'
  voice consistently closes with a concrete worked instance rather than
  only an abstract template.

## Continuity check

All eight pages use `jeremy-evert/git-safety-belt-lab` as the sole running
example, per the requirement — no other repo is introduced. Where a page
needed its own small worked scenario not fully specified by the README
(06's task, 08's break), I said so explicitly on the page and named the
assumption, rather than presenting invented detail as settled fact.

## Open question for Anna

Whether page 06 should reuse 02's exact bounded task (`average_pieces_
per_category`) instead of the new one I gave it (`largest_category`) — see
above. Either is internally consistent; it's a continuity-vs-repetition
judgment call I made one way and am flagging rather than assuming.

IVY BITE b3.2-git-curriculum-pages-03-10 READY FOR ANNA
