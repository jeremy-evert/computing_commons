# Piper Battle Map — Home/Table → Weeks 4–5 Slides

## Goal

Turn Computing Commons from a useful but module-heavy prototype into a teachable front door for students and an instructor cockpit for Jeremy, then use the recovered time to build the next six shared-rhythm projector decks.

## Barrel 1 — Prompt 011

**Student Home**

- replace the Modules-first experience with a beautiful Canvas Home;
- use Success Foundations as the visual quality bar;
- show this week's Monday / Wednesday / Friday route;
- keep Local AI and Recitation obvious;
- preview next week without overwhelming the current week.

**Teacher's Table**

- unpublished instructor-only page;
- Week 2 + Week 3 at minimum;
- exact book/source/chapter;
- what Jeremy needs to study;
- links to instructor notes/study guides;
- links to long readings and projector decks;
- student Canvas route;
- key teaching bullets, room question, misconception, prep status.

Prompt:

`sidecar/prompts/011_brandy_pretty_home_and_teachers_table.md`

Acceptance sentinel:

`PRETTY HOME + TEACHER'S TABLE ACCEPTED; CONTINUE TO PROMPT 012 IF UNGATED`

## Barrel 2 — Prompt 012

Only if Barrel 1 is fully accepted without a human/source/Canvas gate.

Build six Beamer projector decks + instructor-note companions:

### Week 4

- Monday Moment — AI Fluency: **Decompose the Task**
- Wacky Wednesday — Professional Minds: **Mapping Arguments for Better Decisions** / Tom Chatfield
- Fun Friday — Professional Minds: **The Outside View** / Daniel Kahneman

### Week 5

- Monday Moment — AI Fluency: **Select the Right Model**
- Wacky Wednesday — Professional Minds: **Outcome Bias** / Rolf Dobelli
- Fun Friday — Professional Minds: **Regression to the Mean** / Jordan Ellenberg

Use the accepted Commons Beamer theme and instructor-note grammar. Produce a Grace review helper. Do not deploy Week 4–5 slides to Canvas yet.

Prompt:

`sidecar/prompts/012_brandy_weeks4_5_mwf_beamer_slide_factory.md`

Final sentinel:

`WEEKS 4–5 M/W/F SLIDE FACTORY READY FOR GRACE REVIEW`

## Chain control

Foreman job:

`jobs/tasks/computing_commons_home_table_then_weeks4_5_slides_011_012_brandy.md`

Prompt 011 and Prompt 012 are separately blob-pinned. Prompt 012 is a true continuation: Luna must verify its pin before work and may only enter it after Prompt 011 acceptance.

## Boundaries

- Savnac course 18 is the only Canvas mutation target, and only during Prompt 011.
- Production Canvas stays untouched.
- Canonical `ai_fluency`, `professional_minds`, and `swosu_cs_curriculum` stay read-only.
- Prompt 012 produces files only, not Canvas deployment.
- Quick Tune and synthetic students remain out of scope.
