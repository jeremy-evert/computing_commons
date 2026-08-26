# Prompt 031 — Week 2 Personal-Windows Local AI Self-Service + Copilot Review

Owner: Jeremy
Foreman: Flo
Date: 2026-08-26
Priority: **CLASSROOM DELIVERY / WEEK 2**
Owning composition repository: `jeremy-evert/computing_commons`
Production target: SWOSU Canvas course `24298`
Canonical Local AI source: `jeremy-evert/local_ai_lab_setup`
Professional Minds source: `jeremy-evert/professional_minds` (read-only for this mission)

## Owner outcome

Take the useful work from Jeremy's August 26 Local AI dogfood run and turn it into a safe, obvious, durable Week 2 student path in the live Computing Commons.

The desired student experience is:

```text
I know which path applies to my computer
-> I can get or generate the setup script
-> a second AI inspects the actual script before I run it
-> the script checks before it changes anything
-> every change requires my explicit Y
-> missing tools can be installed on my own Windows laptop
-> the local model is verified by actual inference
-> Aider is verified
-> a readable HTML receipt opens at the end
-> I know what happened and what to do next
```

This is a bounded Week 2 production pass, not a broad rewrite of Computing Commons, Professional Minds, Local AI architecture, or Canvas.

## Governing repository rule

The Commons is the composition layer. **Stitch, do not fork.**

- `local_ai_lab_setup` owns the Local AI technical/instructional source.
- `professional_minds` owns the Week 2 professional-learning source.
- `computing_commons` owns how those sources are sequenced and delivered to students in Canvas.

If the August 26 dogfood bundle needs promotion or correction before it is safe for students, make that bounded repair in `local_ai_lab_setup` first, then consume the accepted source in Commons. Do not create a contradictory Commons-only copy merely to get something onto Canvas.

## Read durable truth first

Before mutation, read:

### Foreman control plane

1. `foreman_interface/EASY.md`
2. `foreman_interface/START_FOREMAN.md`

### Computing Commons

3. `computing_commons/README.md`
4. `computing_commons/AGENTS.md`
5. `computing_commons/curriculum/local-ai-lab.md`
6. `computing_commons/sidecar/prompts/015_production_local_ai_student_path_dogfood_and_repair.md`
7. current Week 2 deployment/provenance/readback evidence

### Canonical Local AI source

Read the current `jeremy-evert/local_ai_lab_setup` repository and specifically inspect the August 26 source snapshot containing Jeremy's dogfood run.

Known durable snapshot:

```text
8a87e6c2bf67700700bd124f3db514df6fedda90
```

At minimum inspect completely:

```text
Jeremy_run_1_dump/local_ai_lab_setup.ps1
Jeremy_run_1_dump/EFxtended_notes.md
Jeremy_run_1_dump/local_ai_lab_field_guide.md
Jeremy_run_1_dump/local_ai_lab_session_notes.pdf
Jeremy_run_1_dump/local_ai_lab_receipts/2026-08-26_07-54-32/readiness_report.html
Jeremy_run_1_dump/local_ai_lab_receipts/2026-08-26_07-54-32/run_log.txt
Jeremy_run_1_dump/local_ai_lab_receipts/2026-08-26_08-46-54/readiness_report.html
Jeremy_run_1_dump/local_ai_lab_receipts/2026-08-26_08-46-54/run_log.txt
```

Also read the current canonical Week 2 material, including:

```text
README.md
AGENTS.md
docs/week2_module_plan.md
curriculum/week2_module_manifest.yml
curriculum/shared/week2/
packages/cs1_online/
instructor/windows_validation/
```

If HEAD has advanced beyond the known snapshot, inspect the diff. Changed SHA means **LOOK**, not automatic stop and not automatic GO.

### Professional Minds Week 2

Read current `jeremy-evert/professional_minds`, especially:

```text
START_HERE.md
sidecar/PLAN.md
week-02/monday.md
week-02/wednesday.md
week-02/friday.md
week-02/synthesis.md
sidecar/prompts/020_canvas_weekly_publication_chain_gun.md
```

Known Week 2 source blobs when this prompt was authored:

```text
week-02/monday.md     11b0c61043c11bb558e670de0c2a9b1984bf07bf
week-02/wednesday.md  fe832238f0018ac49812c217f032e81f0416a982
week-02/friday.md     930b13726acbbc51e134837a88d47caf780a7926
week-02/synthesis.md  acc720ad76fb68d9c692a4ce16145f1e5f2ba9e3
```

Professional Minds is read-only here. Preserve its source authority and Canvas publication contract.

## What Jeremy's August 26 run adds

The dogfood bundle contains a promising new teaching move:

```text
DETECT -> EXPLAIN -> ASK PERMISSION -> CHANGE -> VERIFY -> RECORD
```

The candidate PowerShell script can:

1. check Python;
2. check Git;
3. check Ollama;
4. check Aider;
5. check/download an Ollama model;
6. ask before system-changing actions;
7. install missing components on a personal Windows machine;
8. test Ollama reachability separately from installation;
9. perform a small local inference check;
10. generate a styled local HTML readiness report;
11. open that report in the default browser.

The student-learning idea is also strong:

> **Builder != Inspector.**

One AI may help create a script. A different review pass inspects the actual PowerShell before the student runs it.

Preserve that idea.

## Important: the dogfood bundle is evidence, not automatically publishable truth

Do **not** upload Jeremy's raw dump wholesale to Canvas.

Classify every artifact as one of:

```text
STUDENT_CANONICAL
STUDENT_REFERENCE
INSTRUCTOR_ONLY
EVIDENCE_ONLY
REJECT / SUPERSEDED
```

Raw run logs, Jeremy-specific receipts, machine-specific paths, private machine evidence, development notes, and contradictory drafts are not automatically student material.

A student should see a clean path, not the archaeology layer.

## Required conflict ledger before publication

Resolve or surface every conflict below explicitly.

### Conflict 1 — approved model drift

The canonical Local AI curriculum currently names:

```text
qwen3:8b
```

The August 26 dogfood material contains mixed claims:

- script header says `qwen3:8b`;
- script constant uses `qwen3:1.7b`;
- field-guide text often describes `qwen3:1.7b`;
- older canonical Commons/Local-AI paths still expect `qwen3:8b`.

**Never publish a script whose header, explanation, checks, and actual model disagree.**

For this mission, preserve `qwen3:8b` as the canonical model unless current owner-approved source truth has deliberately changed it.

If the best student-laptop route genuinely requires `qwen3:1.7b`, produce one narrow HUMAN DECISION with evidence:

```text
KEEP qwen3:8b CANONICAL
or
CHANGE PERSONAL-LAPTOP LANE TO qwen3:1.7b
```

Do not silently make that curriculum-policy decision.

### Conflict 2 — verification-only versus self-service installation

The accepted classroom path has intentionally told students not to improvise installation or repair on managed systems.

Jeremy's August 26 intent now explicitly adds a self-service installation experience.

Resolve this with **two clear lanes**, not one muddled rule:

#### Lane A — SWOSU-managed / classroom computer

```text
VERIFY ONLY
```

- run the accepted checker/path;
- collect evidence;
- do not install system software;
- do not use administrator credentials;
- do not alter security/network policy;
- escalate missing infrastructure.

#### Lane B — student's own Windows 11 computer

```text
OPTIONAL SELF-SERVICE SETUP
```

- detect first;
- explain the change;
- ask explicit permission;
- install only the requested Local AI components;
- verify after installation;
- produce a receipt;
- stop cleanly when the student says N.

The student must be able to identify their lane before seeing install instructions.

### Conflict 3 — privacy overclaims

Do not publish absolute claims such as:

```text
"no FERPA concerns"
"your data is never sent anywhere"
"local means everything is private/offline"
```

Use scoped language:

- this lab's intended model request path is loopback/local;
- no cloud AI API key is required for the Ollama/Aider lab path;
- local operation does not grant permission to paste secrets;
- local inference does not prove every installed application is offline or incapable of telemetry;
- students should use non-sensitive course material.

### Conflict 4 — missing prompt files

The August 26 field notes refer to:

```text
setup_script_prompt.txt
safety_review_prompt.txt
```

but those files are not present in Jeremy's committed dump.

Create durable canonical student-facing versions before Canvas publication.

### Conflict 5 — `.ps1` upload behavior

Jeremy's live notes report that Copilot may block direct `.ps1` uploads.

Dogfood the current Copilot interface rather than assuming upload support.

The student instructions must provide a verified fallback:

1. attach the `.ps1` directly if the current UI accepts it;
2. otherwise paste the complete script text into a new chat; or
3. if useful, save a **copy** as `.txt` for review while preserving the original `.ps1` unchanged.

Never tell a student that attachment is required if current Copilot blocks it.

### Conflict 6 — UI/model names can drift

Jeremy's August 26 screenshot showed Microsoft Copilot exposing:

```text
GPT -> GPT 5.6 Think deeper
Anthropic -> Opus
```

The Builder/Inspector teaching path may use:

- a capable builder model for script generation;
- **GPT 5.6 Think deeper** for the independent safety/functional review when that model is available in the student's Copilot UI.

Verify the current UI during publication. Phrase directions so a minor label change does not break the lesson.

Do not claim a model is available to every student without verifying the institution-facing experience.

## Required student-facing path

The Week 2 Local AI page should become an obvious router.

### Step 0 — Which computer are you on?

Student chooses:

```text
A. SWOSU-managed/classroom Windows computer
B. My own Windows 11 computer
```

No student should accidentally run self-service installation on a managed machine because the page buried the distinction.

### Lane A — managed computer

Preserve the accepted verification-first Local AI runway from Prompt 015 and the canonical package.

Do not destabilize a working classroom route merely because Lane B now exists.

### Lane B — personal Windows computer

Create a clean student route with this grammar at every step:

```text
GO HERE
DO THIS
LOOK FOR THIS
IF NOT, DO THIS
```

The personal-laptop path should include:

1. sign in to the institution-provided Microsoft/Copilot experience;
2. open a new Copilot chat;
3. use the canonical **setup-script generation prompt** to ask for one complete Windows PowerShell `.ps1` script;
4. save the generated script as `local_ai_lab_setup.ps1` using a plain-text editor;
5. open a separate review chat;
6. select **GPT 5.6 Think deeper** when available;
7. attach or paste the actual generated script;
8. use the canonical **independent safety-review prompt**;
9. read the verdict;
10. do not run a script with unresolved high-risk findings;
11. run the reviewed script only after the review gate is satisfied;
12. answer Y/N prompts deliberately;
13. let the script check/install only the approved components;
14. inspect the final HTML readiness report;
15. keep the report as the student's receipt.

## Canonical generation-prompt requirements

Create a durable `setup_script_prompt` student artifact that tells the builder to produce one complete Windows 11 PowerShell script.

It must require the script to check, in a readable order:

```text
Python
Git
Ollama installation
Ollama service/API reachability
approved Ollama model
local inference
Aider
```

It must require, for every system-changing action:

```text
DETECT
-> EXPLAIN WHAT WAS FOUND
-> EXPLAIN WHY THE CHANGE IS NEEDED
-> SHOW WHAT WILL HAPPEN
-> ASK Y/N
-> CHANGE ONLY AFTER Y
-> VERIFY
-> RECORD
```

The prompt must prohibit:

- silent installs;
- default-yes behavior;
- privilege-escalation tricks;
- global execution-policy weakening;
- Defender/firewall/security disabling;
- broad registry/security/network changes;
- arbitrary file deletion;
- credential/token/private-key collection;
- unrelated package installation;
- GitHub credential/account configuration;
- destructive Git operations;
- hidden persistence/scheduled tasks;
- reboot without explicit user action.

The script should prefer reputable normal installers such as `winget` where available and must tell the student what it is about to do.

The prompt must require friendly error handling and a standalone local HTML report that opens automatically at completion.

The report should show:

```text
PASS
FIXED
SKIPPED
WARNING
FAILED
```

and summarize versions, actions performed, actions declined, failures, and next steps without exposing secrets.

## Canonical independent-review prompt requirements

Create a durable `safety_review_prompt` student artifact.

It must instruct GPT 5.6 Think deeper, or the best available independent reviewer, to:

- read the entire attached/pasted `.ps1` before deciding;
- **not execute it**;
- audit actual commands/control flow, not comments;
- list every meaningful system change;
- inspect file deletion, registry, execution policy, firewall, Defender, services, scheduled tasks, downloaded code, credential access, telemetry/uploads, persistence, and unrelated installs;
- verify that every system-changing action is behind explicit Y;
- verify that N really means no change;
- inspect Python/Git/Ollama/model/Aider detection and installation logic;
- inspect PATH refresh behavior;
- inspect Ollama localhost binding/service behavior;
- verify actual local inference is tested;
- verify HTML output is local and non-sensitive;
- identify likely Windows 11 / PowerShell 5.1 / PowerShell 7 compatibility failures.

Require one of these exact verdict classes:

```text
SAFE TO RUN
SAFE WITH MINOR FIXES
DO NOT RUN YET
UNSAFE
```

and finish with a beginner-readable recommendation.

## Canonical PowerShell candidate requirements

Promote Jeremy's August 26 script only after review/repair.

At minimum prove:

- script parses under the supported Windows PowerShell version;
- model identity is internally consistent;
- detection happens before installation;
- every install/download/service start is individually permission-gated;
- Enter alone is not consent;
- N cleanly skips;
- no admin assumption;
- no firewall/Defender/security weakening;
- no unrelated registry modification;
- no Git credential/repository mutation;
- Ollama installation and Ollama service reachability are separate checks;
- service is expected only on loopback;
- model-list success is not treated as inference success;
- tiny inference test actually returns text;
- Aider is actually invokable;
- receipt directory is bounded under the user's profile;
- HTML is standalone/local and opens in the default browser;
- logs/reports avoid secrets and unnecessary machine identity;
- failures are understandable to a beginning student.

Do not preserve a broken generated script merely because it was useful dogfood evidence.

## What belongs in Canvas

Prefer a small set of clean Canvas items rather than dumping repository files into the module.

Expected Week 2 Local AI items may include:

1. **Build and Verify Your Local AI Lab** — router / choose-your-computer page;
2. **Managed SWOSU Computer — Verify Only** — existing accepted route;
3. **Personal Windows Computer — Safe Self-Service Setup** — new route;
4. **Prompt: Build the Setup Script** — readable/copyable generation prompt;
5. **Prompt: Review the Script Before Running It** — readable/copyable independent-review prompt;
6. **Run the Script and Read Your Receipt** — exact run/report instructions;
7. any canonical download/file link required by the accepted source.

Do not expose instructor-only field guides, raw logs, Jeremy-specific receipts, or developer plumbing as normal student module items.

A sanitized sample readiness-report screenshot or HTML example may be used only if it contains no personal/machine-specific data and materially helps students understand the finish line.

## Week 2 Professional Minds integration

Do not replace or rewrite the Professional Minds Week 2 pilot.

Preserve the existing Week 2 professional question and four-page rhythm:

```text
Monday    — Gather Context
Wednesday — Learning That Lasts
Friday    — Feedback Is Information
Synthesis — Earn One Rule
```

Use the Local AI self-service experience as a real example that reinforces those ideas:

- **Gather Context:** the setup-script prompt is better because it names audience, OS, boundaries, components, permission rules, and output requirements.
- **Learning That Lasts:** students should be able to explain what Python, Git, Ollama, the model, and Aider do rather than merely recognize the names.
- **Feedback Is Information:** the second-model safety audit and the HTML receipt turn defects into evidence for the next bounded fix.
- **Three Jobs:** Owner decides the outcome; Foreman defines boundaries/evidence; Worker produces the script. The Worker does not certify its own work.

Keep this as a short bridge, not duplicated Professional Minds prose.

## Canvas mutation boundary

Authorized production target:

```text
https://swosu.instructure.com/courses/24298
```

Before mutation:

1. read configured Canvas origin from the authorized local config;
2. GET course `24298`;
3. refuse unless numeric ID is exactly `24298` and course identity clearly indicates Computing Commons;
4. record only safe identity fields;
5. never write a token/cookie/secret to Git, logs, reports, or chat.

Authorized mutation is limited to Week 2 Local AI pages/files/module items needed for this prompt.

Do **not** touch:

- grades;
- submissions;
- enrollments;
- assignments or point values unless an already-existing Local AI assignment must receive a non-content link repair and identity is unambiguous;
- due dates;
- course settings;
- unrelated modules/pages;
- other courses;
- Professional Minds source pages except stable navigation/link composition already owned by Commons.

Prefer Pages + Files + Module items for this slice.

## Reuse the established publication seam

Inspect current `computing_commons` and Harbor tooling before coding.

Reuse existing:

- hard target locks;
- idempotent page/module reconciliation;
- Markdown/HTML rendering;
- Canvas link rewriting;
- readback receipts;
- student-view/browser verification;
- safe deployment manifests.

Do not invent a third Canvas client if the established path is healthy.

## Execution chain

### Barrel 1 — Recon + source classification

No production mutation.

Produce:

- current repo SHAs;
- August 26 artifact classification table;
- conflict ledger;
- exact current Canvas Week 2 Local AI object map;
- proposed student module order;
- identified human gates, if any.

Sentinel:

```text
WEEK2 LOCAL AI BARREL 1 — SOURCE MAP CLEAN
```

### Barrel 2 — Canonical source repair/promotion

If needed, make only bounded changes in `local_ai_lab_setup` to turn the dogfood candidate into safe canonical student assets.

Likely outputs include equivalents of:

- reviewed personal-Windows self-service page;
- reviewed `local_ai_lab_setup.ps1`;
- durable setup-script generation prompt;
- durable independent safety-review prompt;
- sanitized sample report only if useful;
- instructor notes preserving what was learned from the raw dogfood run.

Follow `local_ai_lab_setup/AGENTS.md` and its prompt/report contract when source edits occur.

Validate and push source repairs before Commons consumes them.

Sentinel:

```text
WEEK2 LOCAL AI BARREL 2 — CANONICAL SOURCE ACCEPTED
```

If model policy cannot be reconciled without owner choice, stop here with one HUMAN DECISION rather than publishing contradictory material.

### Barrel 3 — Commons composition + dry-run

Compose the accepted Local AI source into Computing Commons Week 2.

Produce a deterministic dry-run manifest showing:

- page titles/slugs;
- module placement/order;
- file uploads/links;
- canonical source commits/blobs consumed;
- existing objects to update versus new objects to create;
- confirmation no duplicate module/page set will be created.

Adversarially check:

- managed-machine student cannot wander into install lane accidentally;
- personal-laptop student can find the setup path without repository archaeology;
- prompts are copyable and complete;
- model names agree everywhere;
- no absolute privacy claims remain;
- no broken `.ps1` attachment assumption remains;
- navigation reaches the existing Week 2 shared rhythm;
- rerun is idempotent;
- forbidden Canvas surfaces remain untouched.

Sentinel:

```text
WEEK2 LOCAL AI BARREL 3 — DRY RUN ACCEPTED
```

### Barrel 4 — Production reconcile

After Barrels 1–3 are clean:

1. re-read exact Canvas course identity;
2. re-read source HEADs and inspect drift;
3. reconcile the bounded Week 2 Local AI pages/files/module items;
4. publish the intended Week 2 Local AI student items;
5. read every touched object back through the API;
6. inspect rendered pages through the established student-view/browser path;
7. verify all links/files are student-accessible;
8. verify the existing Professional Minds Week 2 rhythm remains coherent and unbroken;
9. verify grades/enrollments/assignments/due dates/unrelated content were untouched.

After any substantive repair, replay from the Week 2 Local AI starting page.

Sentinel:

```text
WEEK2 LOCAL AI BARREL 4 — PRODUCTION READBACK CLEAN
```

### Barrel 5 — End-to-end student dogfood

Dogfood the personal-laptop route as close to a real student as safely practical.

Verify the path:

```text
Commons Week 2
-> choose personal Windows lane
-> open generation prompt
-> obtain/review setup script
-> independent GPT 5.6 Think deeper review when available
-> run reviewed PowerShell
-> permission prompts behave correctly
-> tool/model checks complete
-> local inference works
-> Aider check works
-> HTML report opens
-> student can explain READY / INCOMPLETE and the next action
```

Do not destructively reinstall working software merely to simulate a missing-tool state on a production machine. Use safe test harnesses, isolated state, mocks, or a disposable/representative Windows seat where appropriate.

Also verify the managed-machine lane still routes to the existing verification-only path.

Sentinel:

```text
WEEK2 LOCAL AI BARREL 5 — STUDENT ROAD WORKS
```

## Human gates

Yield only for a real consequential decision or authority boundary.

Known possible human gates:

1. canonical model choice if `qwen3:8b` versus `qwen3:1.7b` remains unresolved after evidence review;
2. institutional approval if self-service installation would be offered on managed SWOSU computers rather than personal devices;
3. final teaching/design judgment after clean Student View readback if Jeremy wants to inspect the exact feel before declaring the pilot accepted.

Routine source reading, prompt creation, bounded source repair, Canvas page/module publication, link checking, student-view readback, and evidence generation are not human gates.

## Required durable report

Write a concise report under:

```text
sidecar/reports/flo/2026-08-26_week2_personal_windows_local_ai_self_service_and_copilot_review.md
```

It must include:

- source SHAs/blobs actually used;
- August 26 artifact classification table;
- conflict ledger and resolutions;
- canonical Local AI files created/changed, if any;
- Canvas object IDs/slugs/files touched;
- exact Week 2 module placement/order;
- model policy used;
- safety-review findings for the PowerShell script;
- dry-run/idempotency proof;
- production readback proof;
- end-to-end student dogfood result;
- confirmation managed-machine verification lane still works;
- confirmation Professional Minds Week 2 was not rewritten;
- confirmation grades/enrollments/due dates/unrelated courses were untouched;
- remaining human gate, if any;
- final source and Commons commit(s), push verification, and clean/known final status.

## Definition of done

This mission is done only when:

1. students can clearly choose managed-machine versus personal-laptop setup;
2. the personal-laptop lane includes a complete builder prompt and independent-review prompt;
3. the PowerShell candidate is internally consistent, reviewed, and safe within the stated boundary;
4. every system change requires explicit Y and N truly skips;
5. the approved model is consistent everywhere or one human decision is precisely queued;
6. the student receives a readable local HTML receipt;
7. raw Jeremy dogfood receipts/logs are not exposed as student content;
8. Canvas Week 2 contains a coherent, accessible Local AI route;
9. existing Professional Minds Week 2 remains intact and connected;
10. production course 24298 is read back and visually/student-view checked;
11. unrelated Canvas state is untouched;
12. durable report/evidence is committed and pushed.

Final sentinel:

```text
COMPUTING COMMONS WEEK 2 LOCAL AI SELF-SERVICE ROAD WORKS.
```
