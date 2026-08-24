# Prompt 008 — Brandy Week 2 Beamer visual system + instructor notes

## Mission

Act as Luna on **Brandy** and turn the accepted Week 2 Local AI Beamer deck into a polished Computing Commons teaching instrument while preserving its instructional substance.

Jeremy has approved the current deck as a strong V1. The next pass is not a curriculum rewrite. The goals are:

1. make the slides feel visually related to the accepted **Success Foundations / Semester Kickoff** Canvas page;
2. make dense slides easier to teach by splitting them when useful rather than shrinking text;
3. add a slide-by-slide instructor note layer so Jeremy has something useful to say, ask, demonstrate, and watch for while projecting;
4. make the review loop easy for an exhausted human: one Grace helper should open the current deck and notes after a clean pull.

This mission is deliberately allowed to add **more slides**. Do not treat slide count as a scarcity constraint. A single clear idea per slide is preferable to a beautiful but overloaded table.

## Writable project

Primary writable repository:

`/mnt/brandy_nvme/jevert/git/computing_commons`

Do not modify Canvas, Savnac, production SWOSU Canvas, canonical Local AI repositories, or curriculum repositories in this mission.

## Required reading

Before editing, read current truth:

- `AGENTS.md`
- `slides/week2_local_ai_workbench/week2_local_ai_workbench.tex`
- `slides/week2_local_ai_workbench/README.md`
- `sidecar/reports/luna/007_week2_beamer_teaching_slides_report.md`
- `instructor/week2_aider_work_first_teaching_guide.md`
- current accepted Success Foundations / Semester Kickoff source or preview in this repository
- current Week 2 preview/page sources as needed for vocabulary and visual consistency

Read-only canonical references remain:

- `../local_ai_lab_setup`
- `../windows_classroom`
- `../swosu_cs_curriculum`

Do not silently alter canonical commands, model tags, endpoints, classroom boundaries, or security claims.

## Owner visual direction

Treat the accepted **Success Foundations / Semester Kickoff** Canvas page as the visual quality bar for Computing Commons teaching materials.

The reusable visual grammar should echo, not literally screenshot-copy, that page:

- deep navy hero/header areas;
- strong white hierarchy on dark sections;
- pale blue action/instruction surfaces;
- pale green success/evidence surfaces;
- warm cream/gold recovery or caution surfaces;
- restrained accent bars;
- generous whitespace;
- rounded cards where Beamer can support them cleanly;
- large projector-readable text;
- one dominant idea per slide;
- calm, capable, modern visual tone;
- no tiny footer machinery that competes with the lesson.

The deck and Canvas should feel like the same product family.

## Build a reusable Beamer visual system

Do not hand-style 25+ slides independently if a small reusable theme/component layer can make the right thing easy.

Create the smallest useful reusable Beamer visual system inside the deck package. It may be a theme `.sty`/`.tex` include or clean macros inside the source if that is materially simpler.

Provide reusable treatments for approximately these slide families:

1. **Hero / transition**
2. **Do-this walkthrough**
3. **Explain + evidence**
4. **Diagram / system model**
5. **Question / discussion / recovery**

Provide reusable cards/treatments for these recurring instructional roles when appropriate:

- `DO THIS`
- `WHAT THIS MEANS`
- `HOW YOU KNOW / EVIDENCE`
- `FIND THIS YOURSELF`
- `DEMAND DOCUMENTATION`
- `VERIFY ON YOUR MACHINE`
- `KEEP THE RECEIPT`
- `IF THIS FAILS / "NOT READY"`

Do **not** put every card on every slide. Use only the elements the slide needs.

## Preserve and strengthen the teaching grammar

Keep the recurring intellectual questions:

> **What does this prove, and what does it NOT prove?**

> **Do not stop at the answer. Ask how to verify it.**

Add the newly approved recurring security/judgment questions where relevant:

> **Is this safe?**
> **Is this secure?**
> **How do I know?**
> **Where can I verify that?**

These questions are especially appropriate on the Ollama/loopback/local-service material, but they should become a reusable instructor pattern rather than a slogan pasted everywhere.

Be precise: `127.0.0.1` / loopback is evidence about local routing/reachability. It does not by itself prove the whole workflow is secure, private, correctly configured, or free of cloud/provider drift. Preserve the distinction between network locality, application configuration, data handling, authentication, and correctness.

## Split dense slides freely

Jeremy explicitly authorizes more slides when that improves teaching.

Do not squeeze content to preserve the current 22-slide count. Prefer 26–34 clear slides over 22 overloaded slides if that is what the material earns.

In particular, inspect the current **Evidence has layers too** slide and strongly consider splitting it into a sequence such as:

- evidence before model action: command/service/model observations;
- evidence after model action: generation/diff/test;
- conclusion: each observation supports one bounded claim.

Likewise split any other slide where the projected audience must parse too much at once.

The deck should support live discussion and student action, not reward information density.

## Instructor notes deliverable

Create a coordinated instructor note layer for **every projected slide**.

Preferred durable deliverables:

- `week2_local_ai_workbench_notes.md` — human-readable source;
- `week2_local_ai_workbench_notes.pdf` — compact printable/readable instructor notes;

A different exact implementation is acceptable if it is simpler and equally durable, but do not hide the notes only in fragile PDF metadata.

For each slide include concise fields such as:

- **Purpose** — why this slide exists;
- **Say** — approximately 30–120 seconds of useful narration, not a transcript of the slide;
- **Ask** — one question for the room when useful;
- **Do** — what students should do on their machines, if anything;
- **Watch for** — likely misconception/failure;
- **Move on when** — observable evidence that the class is ready to continue.

Not every slide needs all six fields, but each slide should give Jeremy enough support that he does not have to invent the teaching move while standing at the front of the room.

For the current evidence slide sequence, the notes should explicitly teach that:

- `python --version` proves a command/runtime answered, not program correctness;
- `ollama list` proves a model is reported available, not that it can infer;
- a loopback/service check proves service reachability, not Aider integration or overall security;
- direct inference proves one request completed, not that the answer is correct;
- `git diff` proves what text changed, not behavior;
- an independent test supports only the tested behavior, not every possible property;
- the class is building a **chain of bounded evidence**, not collecting reassuring green lights.

For the Ollama/loopback slide, include a conversational teaching move around:

- Is this safe?
- Is this secure?
- How do I know?
- Where can I verify that?

and then distinguish official documentation from local-machine verification.

## Slide/content division of labor

Do not make the deck carry every self-paced detail.

Use this principle:

- **Slides** support projection, explanation, discussion, prediction, and live action.
- **Canvas / Commons pages** remain the durable student route for exact steps, recovery, and later return.

If you discover material that clearly belongs as additional self-paced Canvas pages rather than projected slides, do **not** modify Canvas in this mission. Record a short `Canvas follow-up` section in the report with recommended page splits/additions.

## Visual examples

The PowerShell walkthrough should feel friendlier than a list of terminal trivia. The student should be able to recognize:

- Windows Start;
- typing `PowerShell`;
- choosing the provisioned PowerShell 7 option;
- the opened terminal prompt;
- where commands are typed.

Use generic/sanitized visual examples. Do not leak Jeremy usernames, hostnames, account data, unrelated desktop items, or credentials.

## Grace one-command review helper

Jeremy liked the existing capture workflow because Piper could give him one command on Grace and then review the result.

Add the smallest useful Grace review helper, for example:

`scripts/grace/review-week2-slides.ps1`

It should be boring and safe. Suggested behavior:

1. require/run from the `computing_commons` checkout;
2. refuse to disturb a dirty checkout;
3. optionally `git pull --ff-only` or clearly tell the operator to pull first, whichever is safer with current repo convention;
4. confirm the deck PDF and notes PDF exist;
5. open the projected deck and instructor notes for owner review;
6. print the current commit SHA and paths.

Do not build a general slide management framework. This is a small human-energy-saving helper.

## Build and validation

Brandy has LaTeX/Beamer. Build the actual deliverables there.

At minimum:

1. compile the projected deck successfully;
2. compile instructor notes PDF successfully;
3. fail on LaTeX errors rather than leaving stale outputs;
4. inspect compile output for overfull boxes and obvious layout failures;
5. render/inspect representative slides from every slide family;
6. inspect all newly split evidence/security slides;
7. verify readable type size from a classroom projector perspective;
8. verify no personal identity/machine-name leakage;
9. verify current canonical commands/model/endpoints remain intact;
10. `git diff --check` passes.

## Git / acceptance

Before stopping:

- commit all in-scope theme/source/PDF/notes/helper/report changes;
- push accepted work to `origin/main`;
- remote/read-back verify the report and key source file;
- report exact deck page count, note page count, build commands, paths, commit SHA, and any genuine owner questions;
- do not deploy to Canvas.

Report path:

`sidecar/reports/luna/008_week2_beamer_visual_system_and_notes_report.md`

Final sentinel:

`WEEK 2 VISUAL DECK + INSTRUCTOR NOTES READY FOR OWNER REVIEW`
