# Prompt 011 — Brandy Pretty Home + Teacher's Table

## Mission

Act as Luna on **Brandy** and make Savnac Computing Commons course 18 feel like a coherent product instead of a raw Canvas module dump.

This mission has two mandatory outcomes:

1. build a **beautiful student Home landing page** and set it as the course Home/default landing surface;
2. build an **unpublished Teacher's Table** that gives Jeremy a one-screen teaching cockpit with exact books/readings, instructor notes/study guides, slide/deck links, student routes, and readiness cues.

Use the accepted **Success Foundations / Semester Kickoff** page as the literal visual quality bar. Do not invent a second visual language.

This is a presentation/composition mission, not a curriculum rewrite.

## Writable project and Canvas target

Primary writable repository:

`/mnt/brandy_nvme/jevert/git/computing_commons`

Authorized mutable Canvas surface:

- Savnac Canvas course **18 only**

Read-only canonical source repositories as needed:

- `/mnt/brandy_nvme/jevert/git/ai_fluency`
- `/mnt/brandy_nvme/jevert/git/professional_minds`
- `/mnt/brandy_nvme/jevert/git/swosu_cs_curriculum`

Do not modify canonical source repositories.

## Required starting truth

Before mutation:

- pull/inspect current `computing_commons` truth;
- read Prompt 009 and Prompt 010 reports/readbacks/provenance/instructor guides;
- inspect the accepted Success Foundations page source/preview and its current Savnac rendering;
- inspect current course-18 module/page structure and current default view;
- inspect current Week 2 and Week 3 student routes;
- reconcile exact canonical source assets for the Teacher's Table.

If the accepted Week 3 source is on an accepted/promoted commit rather than the checkout's current branch, resolve the branch/promotion state explicitly before editing. Do not silently rebuild Week 3 from memory.

## Product architecture

### Student Home

The student should land on a **pretty, simple dashboard**, not Modules.

The page should answer three questions instantly:

1. What are we doing now?
2. What is coming next?
3. Where do I go if I am lost?

Use a structure similar to:

- dark navy Commons hero/masthead;
- **This Week** day cards;
- Monday AI Fluency card;
- Wednesday Professional Minds card;
- Friday Professional Minds card;
- Local AI Lab / current technical runway card;
- Recitation / Get Help recovery card;
- compact **Next Week** preview;
- small semester/shared-route navigation, not a wall of links.

Current Week 2 content should remain the immediate teaching week:

- Monday: AI Fluency Level 1 — Gather Context;
- Wednesday: Professional Minds — Make It Stick / retrieval practice;
- Friday: Professional Minds — Mindset at Work;
- Local AI/Aider runway remains prominent and easy to reach.

Week 3 should appear as a compact preview behind it:

- Monday: Plan the Work;
- Wednesday: Growth through mistakes / Limitless Mind;
- Friday: resilience and risk competence.

Do not make students understand repository names or source architecture.

### Teacher's Table

Create an instructor-only Canvas page titled exactly:

**Teacher's Table**

It must remain **unpublished** in Savnac.

This is Jeremy's cockpit, not a student page.

The Teacher's Table should be much more useful than a generic instructor guide. For each current/next session, include:

- **Day / strand / lesson title**
- **What I am teaching**
- **Book / canonical source / chapter or source set**
- **What Jeremy should read/study before class**
- **Direct link to instructor notes / teaching guide / study guide**
- **Direct link to the longer reading assignment or canonical reading**
- **Direct link to slides / projector deck** when present
- **Direct link to student Canvas page**
- **3–5 bullets: what I need to know to teach this**
- **one key question to ask the room**
- **one watch-for / misconception**
- **prep status** such as READY / REVIEW BEFORE CLASS

For AI Fluency, point Jeremy to the canonical `instructor_guide.md`, lesson/student activity, rubric, and portfolio/receipt artifact when useful.

For Professional Minds, point Jeremy to the exact canonical reading and compiled Beamer deck. If a book/chapter or companion-source substitution is involved, say so plainly.

The Teacher's Table should include at least **Week 2 and Week 3**.

Where a current instructor guide already exists in `computing_commons/instructor/`, link it and use it rather than duplicating it. The Canvas Teacher's Table may summarize, but the durable repo guide remains the long-form authority.

## Visual grammar

Student Home should look like the accepted Success Foundations page:

- deep navy hero;
- strong white typography;
- pale blue action surfaces;
- pale green success/evidence surfaces;
- warm cream/gold recovery/caution surfaces;
- restrained rounded cards;
- generous whitespace;
- one obvious primary action per card;
- accessible contrast;
- no fake links or color-only semantics;
- Canvas-safe inline HTML only;
- mobile/narrow friendly.

The Teacher's Table can be denser than the student Home but must still be skimmable at the podium. Use strong section/day hierarchy and compact cards/tables rather than a prose swamp.

## Home behavior

Set course 18 so the pretty Home page is the actual course Home/default view.

Do not require Jeremy to click Modules first.

Keep Modules available for backstage/navigation, but the front door is Home.

## Navigation

Student Home links must resolve to published course-18 routes.

At minimum:

- Monday current route;
- Wednesday current route;
- Friday current route;
- Local AI Lab;
- Recitation / Get Help;
- Week 3 preview routes.

Teacher's Table links may point to unpublished Teacher-only Canvas surfaces and canonical source assets as appropriate, but do not expose private machine paths to students.

No `.md`, `.html`, repository-looking, or `/edit` href leakage in student-facing pages.

## Chain-gun passes

### Pass 1 — PLAN

Inventory current course Home/default view, exact page slugs, current/next week routes, source assets, and intended Teacher's Table links. Record the plan before mutation.

### Pass 2 — BUILD STUDENT HOME

Create the polished Home first.

### Pass 3 — REVIEW STUDENT HOME

Adversarially inspect hierarchy, density, obvious next click, current-vs-next-week confusion, recovery visibility, and mobile behavior. Repair.

### Pass 4 — BUILD TEACHER'S TABLE

Create the unpublished instructor cockpit with exact study/read/deck/note links.

### Pass 5 — REVIEW TEACHER'S TABLE

Check every day/session for:

- actual book/source named;
- exact reading/study item;
- instructor notes/study guide link;
- slide/deck link where available;
- student route;
- concise teaching cues;
- no stale Professional Minds week-number assumptions.

### Pass 6 — DEPLOY

Deploy only to Savnac course 18. Set Home/default view appropriately.

### Pass 7 — READ BACK

Read back Home, Teacher's Table, course default view, and all linked course routes.

Verify:

- Home is published and used as course Home;
- Teacher's Table exists and is unpublished;
- current Week 2 cards work;
- Week 3 preview cards work;
- Recitation and Local AI links work;
- no repository-looking student hrefs;
- no `/edit` links;
- no broken Canvas page targets.

### Pass 8 — ACCEPT

Write evidence/report, commit/push accepted project work, and return exact commit SHA.

## Deliverables

At minimum:

- durable student Home source/preview;
- durable Teacher's Table source/preview;
- deployment/readback support;
- updated/linked instructor metadata as needed;
- `sidecar/reports/luna/011_pretty_home_teachers_table_report.md`;
- Savnac deployment/readback evidence.

## Hard boundaries

Do not:

- touch SWOSU production Canvas or live home courses;
- modify canonical `ai_fluency` / `professional_minds` sources;
- rewrite Week 2/3 curriculum;
- redesign the slide decks in this mission;
- run Quick Tune or synthetic students;
- delete Savnac course 17;
- expose credentials or private student data;
- publish Teacher's Table to students.

## Continuation gate

This mission is the first barrel of a chain-gun sequence.

If and only if all of the following are true:

- Student Home is accepted by Luna's review/readback;
- Teacher's Table is accepted by Luna's review/readback;
- no real human-decision gate remains;
- no source/provenance ambiguity remains;
- course 18 is healthy;

then continue immediately to the separately pinned Prompt 012 mission for Weeks 4–5 Monday/Wednesday/Friday slide production.

If any real gate remains, stop here and report it. Do not weaken this mission merely to reach Prompt 012.

Final sentinel for this mission:

`PRETTY HOME + TEACHER'S TABLE ACCEPTED; CONTINUE TO PROMPT 012 IF UNGATED`
