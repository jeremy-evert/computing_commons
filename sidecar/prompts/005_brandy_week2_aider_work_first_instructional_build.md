# Prompt 005 — Brandy Week 2 Aider + Work First instructional build

## Mission

Act as Luna on **Brandy** and turn the current Computing Commons Week 2 prototype into a polished, teachable, student-hand-holding Local AI Lab experience.

The owner has visually accepted the general page grammar, especially the rendered **Success Foundations / Semester Kickoff** page in Savnac course 18. Use that page as the visual quality bar. Week 2 now needs substantially more instructional depth so Jeremy can teach students how to make Aider work, students can recover when it does not, and the week ends with students ready to adopt the Work First principle.

This mission may modify the `computing_commons` repository and the bounded Week 2 surface in **Savnac course 18**. It must not touch SWOSU production Canvas.

## Owner decisions to preserve

1. The pretty Kickoff page is good. Preserve its calm dark masthead, obvious first action, success/evidence box, recovery help, navigation, spacing, and readable Canvas-safe HTML grammar.
2. Text that is not a link must not visually impersonate a link. In particular, do not use red text merely for status words. Render a non-link failure status as ordinary black bold text in quotation marks, for example **"NOT READY"**.
3. Week 2 needs more hand holding than the current three-page prototype.
4. Jeremy needs an instructor-facing route that lets him confidently teach students how Aider works and how to recover from common failures.
5. Students should finish the Week 2 Commons path able to use a bounded local Aider workflow and ready for the later, fuller **Work First** Recitation station.
6. The owner is dogfooding from Grace. Keep the Savnac prototype small and fast enough to inspect, but do not sacrifice the needed instructional steps.

## Required reading

Read before implementation:

### Computing Commons
- `AGENTS.md`
- `design-system/README.md`
- `previews/kickoff.html`
- `previews/week2-local-ai.html`
- `curriculum/local-ai-lab.md`
- `curriculum/recitation-toolbox.md`
- `curriculum/week2/tools.md`
- `curriculum/week2/recovery.md`
- `scripts/deploy_savnac_visual_slice.py`
- latest Luna Savnac visual/link-repair reports under `sidecar/reports/luna/`

### Canonical Local AI source, read-only
Treat `jeremy-evert/local_ai_lab_setup` as canonical for the Local AI instructional product. Read at minimum:

- `packages/cs1_online/00_START_HERE.md`
- `packages/cs1_online/01_INVENTORY.md`
- `packages/cs1_online/02_VERIFY_WINDOWS_FOUNDATION.md`
- `packages/cs1_online/03_GET_OLLAMA.md`
- `packages/cs1_online/04_GET_APPROVED_MODEL.md`
- `packages/cs1_online/05_HELLO_OLLAMA.md`
- `packages/cs1_online/06_GET_AIDER.md`
- `packages/cs1_online/07_PREPARE_GIT_WORKTREE.md`
- `packages/cs1_online/08_HELLO_AIDER.md`
- `packages/cs1_online/09_AIDER_TOY_EXERCISES.md`
- `curriculum/shared/week2/07_aider_as_a_client.md`
- `curriculum/shared/week2/10_first_local_ai_interaction.md`
- `curriculum/shared/week2/11_troubleshoot_with_evidence.md`

Also inspect the current reviewed Windows boundary in `jeremy-evert/windows_classroom` when needed. Do not modify either reference repository.

## Clearinghouse boundary

**Stitch, do not fork.**

The Commons owns the student journey, visual composition, navigation, and teaching route. It does not silently invent a competing Local AI installation procedure.

When the canonical Local AI source already provides an accepted command, model tag, recovery boundary, or exercise, preserve that truth. If a canonical source is stale or internally inconsistent, report the seam rather than quietly rewriting the technical contract in Commons.

## Week 2 student journey to build

Replace the thin Week 2 prototype with a progressive path that closely follows the accepted CS1 Local AI launch package while presenting it with the Computing Commons visual grammar.

The intended student sequence is:

1. **Week 2 — Build and Verify Your Local AI Lab**
   - orientation and map;
   - what students are building;
   - Aider → Ollama → `qwen3:8b` → local machine mental model;
   - clear statement that installed is not the same as working.

2. **Inventory what you already have**
   - inspect first;
   - avoid unnecessary installs;
   - record what is present versus proven.

3. **Verify the Windows foundation**
   - PowerShell, Python, Git;
   - simple success checks;
   - recovery boundary.

4. **Get or confirm Ollama**
   - use the canonical accepted Windows route;
   - do not create an alternate installer story.

5. **Get the approved model**
   - exact model remains `qwen3:8b` unless the canonical source has been deliberately changed by the owner;
   - distinguish model listed from model successfully running.

6. **Say hello directly to Ollama**
   - first real local inference;
   - make success visible and understandable;
   - explain why this proves a different thing from installation.

7. **Get or confirm Aider**
   - explain Aider as the project-aware coding client;
   - explain that Ollama is still the local model service;
   - no cloud key/provider detour.

8. **Prepare the tiny Git worktree**
   - disposable supplied practice project only;
   - Git gives the student before/after evidence;
   - no GitHub/remote requirement.

9. **Say hello with Aider**
   - use one bounded request;
   - inspect the proposed/actual change;
   - inspect `git diff`;
   - run the independent test;
   - explicitly teach that "Aider changed it" does not mean "it is correct."

10. **Three tiny Aider wins**
    - visible edit;
    - test-backed repair;
    - student-directed harmless modification;
    - each one must follow inspect → ask → diff → test.

11. **Bridge to Work First**
    - do not attempt the entire future Work First Recitation station here;
    - introduce the repeatable habit students just practiced:
      1. know the starting state;
      2. state one bounded desired change;
      3. give the tool only the context it needs;
      4. let the tool do bounded work;
      5. inspect the diff/evidence;
      6. test independently;
      7. accept, repair, or recover;
      8. preserve durable truth outside transient chat.
    - connect this explicitly to the later Work First station in `curriculum/recitation-toolbox.md`.

12. **Recovery with evidence**
    - stop at the first failed check;
    - preserve the command, exit status, and smallest useful output;
    - use bold black quoted **"NOT READY"** rather than red non-link status decoration;
    - make Recitation the obvious recovery path.

13. **Week 2 — Show That It Works**
    - 0-point Fall 2026 completion object;
    - concise evidence receipt, not a giant report;
    - student should be able to show: direct Ollama success, bounded Aider change, inspected diff, independent test, and one sentence explaining the Work First loop.

## Page grammar

Every student-facing Week 2 page should use a consistent, Canvas-safe composition based on the accepted Kickoff page:

- compact Home / Back / Next navigation;
- dark masthead with strand + step label;
- plain-language one-sentence purpose;
- **Do this** or **Do this first** callout;
- **What success looks like** / **Evidence of success** callout;
- **If this fails** or recovery callout;
- no decorative color whose meaning depends on color alone;
- no fake links;
- no duplicate H1/page-title treatment unless it adds different information;
- mobile/narrow-window tolerance;
- compact shared-route/week strip at the bottom.

Prefer a calm workshop feel over a giant wall of prose. Split material into more pages rather than making one enormous page.

## Instructor teaching guide

Create an instructor-facing Week 2 guide in Computing Commons, not a student Canvas page, that makes Jeremy ready to teach this live.

Preferred path:

`instructor/week2_aider_work_first_teaching_guide.md`

It should include:

- the simple mental model: **student → Aider → Ollama → qwen3:8b → local machine**;
- what each layer proves and does not prove;
- a live-demo choreography from direct Ollama through Aider, diff, and test;
- exact checkpoints where Jeremy should stop and ask students what the evidence proves;
- common failure branches: command missing, Ollama unreachable, model unavailable, direct inference works but Aider fails, unexpected cloud-provider/key prompt, Aider edits the wrong file, test fails;
- a short three-meeting teaching route that can map naturally to a M/W/F course without making Commons itself dependent on M/W/F scheduling;
- a compressed one-session Recitation route;
- what to defer to Recitation instead of consuming class time;
- how to transition from the third toy win into the Work First habit;
- a small "what not to improvise live" box for canonical model/endpoint/install boundaries.

The guide should help the instructor teach, not merely summarize student pages.

## Savnac deployment

Update the existing bounded deployment tooling so this expanded Week 2 journey is deployed **in place to Savnac course 18**.

Do not create a replacement prototype course.

Requirements:

- preserve the current pretty Kickoff page;
- keep Recitation available;
- expand Week 2 with the new student pages in sequence;
- keep the completion assignment 0 points, rename it to **Week 2 — Show That It Works** unless Canvas constraints require an equivalent title;
- map repository routes to actual Canvas page slugs explicitly;
- run live read-back/link validation after deployment;
- verify no repository `.html`/`.md` filenames leak into Canvas hrefs;
- verify no page points to an `/edit` route;
- verify every Week 2 page has a working Next path except the final completion/recovery terminal routes;
- preserve a non-secret deployment/read-back report.

## Grace capture pacing repair

Jeremy observed that the Grace capture loop can navigate faster than Canvas visibly settles. Make the smallest safe repository-side improvement so the batch capture gives each target enough settling time before capture. A default around **5 seconds** is appropriate unless a stronger rendered-state check is straightforward and more reliable.

Do not turn the capture helper into a large browser-automation framework.

Do not publish or delete Jeremy's existing Grace capture bundles from Brandy.

## Review pass

Before declaring completion, perform an adversarial pass on:

- beginner comprehensibility;
- Aider instructions;
- technical consistency with canonical Local AI sources;
- visual consistency with Kickoff;
- navigation and link integrity;
- duplicate headings;
- fake-link styling;
- recovery language;
- whether the Work First bridge is understandable without becoming a second full curriculum strand;
- whether Jeremy's instructor guide is genuinely teachable.

Repair defects found inside scope, redeploy course 18, and read back again.

## Hard boundaries

Do not:

- touch `https://swosu.instructure.com/courses/24298` or any production SWOSU Canvas state;
- modify `local_ai_lab_setup`, `windows_classroom`, home-course repos, AI Fluency, Professional Minds, or `swosu_cs_curriculum`;
- enroll/remove students;
- alter grades beyond the existing bounded 0-point prototype object;
- rotate credentials;
- run Quick Tune yet;
- run synthetic students yet;
- delete prototype course 17;
- record final videos;
- redesign Kickoff merely because Week 2 is changing.

## Durable evidence

Write concise source/build and Savnac deployment/read-back reports under `sidecar/reports/luna/`.

At minimum preserve:

- source commit SHA;
- pages created/updated;
- instructor-guide path;
- Savnac course 18 object/read-back summary;
- link-validation result;
- Grace capture pacing change;
- canonical-source seams, if any;
- confirmation production Canvas was untouched.

## Completion gate

Stop only when the expanded Week 2 source is committed/pushed, the bounded Savnac course-18 deployment is read back successfully, and the experience is ready for Jeremy to walk through on Grace.

Final sentinel:

`OWNER WEEK 2 DOGFOOD REQUIRED`
