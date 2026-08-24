# Prompt 007 — Brandy Week 2 Beamer teaching slides

## Mission

Act as Luna on **Brandy** and build the first polished instructor-facing/student-facing slide deck for the Computing Commons Week 2 Local AI Lab.

The immediate need is practical: Jeremy is teaching students tomorrow and wants a deck he can project while students build and verify the local Aider workflow. The larger opportunity is pedagogical: do not make this a deck of commands. Use the deck to teach students how to **do the thing, understand the thing, rediscover the thing, demand documentation, verify reality on their own machine, and preserve evidence**.

This is an implementation-first mission. Build the deck now, learn from the artifact, and let later curriculum doctrine fossilize what proves useful. Do not stop to create a large new philosophy framework before making the slides.

## Writable project

Primary writable repository:

`/mnt/brandy_nvme/jevert/git/computing_commons`

Do not modify production Canvas.

You may read other local repositories for authoritative source material, but do not modify them unless separately authorized.

## Required reading

Before writing slides, read current repository truth:

### Computing Commons
- `AGENTS.md`
- `instructor/week2_aider_work_first_teaching_guide.md`
- `sidecar/prompts/005_brandy_week2_aider_work_first_instructional_build.md`
- current Week 2 source/previews and deployment/readback evidence

### Canonical Local AI / Windows sources, read-only
Read the current authoritative Week 2 material from:
- `../local_ai_lab_setup`
- `../windows_classroom`

Do not silently fork their procedures or invent new model tags, endpoints, installation paths, or classroom contracts.

### Cross-course curriculum doctrine, read-only
Read:
- `../swosu_cs_curriculum/AGENTS.md`
- `../swosu_cs_curriculum/shared/philosophy/computing_tool_access_is_curriculum_infrastructure.md`
- `../swosu_cs_curriculum/shared/philosophy/work-first.md`

If a local `swosu_cs_curriculum_rag_supporter` checkout or executable actually exists, you may use it **read-only** for additional synthesis. Treat its output as advisory and reconcile it against the canonical repository sources above. Its absence is not a gate.

## Deliverables

Create a durable Beamer slide package under a clear path such as:

`slides/week2_local_ai_workbench/`

At minimum produce:

- `week2_local_ai_workbench.tex` — maintainable LaTeX/Beamer source;
- `week2_local_ai_workbench.pdf` — compiled 16:9 PDF ready for later Canvas upload;
- `README.md` — build command, source relationships, intended teaching route, and update notes;
- any small local assets needed by the deck;
- `sidecar/reports/luna/007_week2_beamer_teaching_slides_report.md`.

Do not require proprietary fonts or external runtime assets for the PDF to render.

## Visual direction

Use the accepted Computing Commons visual language as inspiration:

- dark navy mastheads / strong section dividers;
- restrained blue, green, and warm-gold accents;
- high contrast;
- large readable type for a classroom projector;
- code/commands large enough to read from the back of the room;
- clean diagrams over walls of text;
- 16:9 widescreen;
- no tiny citation footnotes that become visual dust.

The deck should feel calm, capable, modern, and teachable. It should not look like an exported textbook chapter.

For Windows UI examples, prefer clean generic/sanitized screenshot-style diagrams or vector mockups that show the important visual landmarks without exposing Jeremy's personal username, machine names, or unrelated desktop content.

## Core teaching grammar

The most important design requirement is a repeatable ladder. For each important tool or checkpoint, use some or all of the following in a visually consistent way:

### DO THIS
Give the exact action that gets a beginner moving now.

### WHAT THIS MEANS
Explain the tool/layer in plain language and why it belongs in the workflow.

### FIND THIS YOURSELF
Give a copyable question/prompt that a student could use with a search engine, Duck.ai, ChatGPT, or another assistant to rediscover the needed information.

The prompt should teach good structure, not dependency on one vendor. Where relevant it should include the student's platform/version and ask for exact steps.

### DEMAND DOCUMENTATION
Show a second question that asks for the **official/primary documentation**, current version/platform relevance, and what remains uncertain.

### VERIFY ON YOUR MACHINE
Give the independent local command/test/observation that proves what is actually true on this computer.

### KEEP THE RECEIPT
Name the smallest useful evidence to preserve when it succeeds or fails.

Use the recurring question:

> **What does this prove, and what does it NOT prove?**

And the recurring principle:

> **Do not stop at the answer. Ask how to verify it.**

## Required content arc

Build a coherent deck, roughly 18–28 slides unless a different count clearly teaches better. The deck should support Jeremy talking while students work, not require him to read paragraphs from the screen.

The arc should include at least:

1. **Week 2 mission** — build a local AI workbench you can prove works.
2. **Why these tools** — the workbench is curriculum infrastructure, not random software collecting.
3. **The stack / mental model** — `student → PowerShell → Aider → Ollama → qwen3:8b → local machine`, with a clear explanation of each layer and the fact that one layer working does not prove the next.
4. **Our evidence rule** — installed/listed/open is not the same as working; generation is not verification.
5. **How to open PowerShell** — literally show: click Start, type `PowerShell`, select PowerShell 7, what the terminal should look like, and how to recognize the prompt. Do not assume students know how to open a shell.
6. **Verify PowerShell itself** — use `$PSVersionTable.PSVersion`, explain what that proves, and model the Find / Documentation / Verify ladder.
7. **Python** — what it is in this workflow, why we need it, how to check it, how students could rediscover that check, and what `python --version` does/does not prove.
8. **Git** — what source control is doing for us, why Aider needs a safe worktree/undo trail, how to inspect state, how to ask for authoritative Git guidance, and what `git status`/`git diff` prove.
9. **Ollama** — local model service, loopback boundary, what reachability proves and does not prove.
10. **`qwen3:8b`** — exact approved model, listed vs actual inference, why a real request is stronger evidence than `ollama list`.
11. **Aider** — what it is, why it is not the model itself, how it talks to Ollama, why we bound its context/files, and how the local-only profile protects the exercise from accidental cloud drift.
12. **First Aider win** — one tiny bounded change in the disposable Git exercise.
13. **Inspect the diff** — the model's claim is not the receipt; show how to inspect what changed.
14. **Independent test** — code generation and code correctness are different claims.
15. **Three tiny wins / repeatable loop** — ask → bounded change → diff → test → accept/recover.
16. **Recovery** — bold black quoted **"NOT READY"** is useful evidence; stop at the first failed check; preserve command, exit status, smallest useful output; Recitation is the recovery seam.
17. **Prompt structure lesson** — show a weak search/AI question, a better structured question, and a verification-oriented question. Make the contrast visually obvious.
18. **Learning to fish** — explain that early in the program we give the action + prompt + docs + verification, then progressively remove pieces until students can formulate the question, find authority, design the check, and defend the conclusion themselves.
19. **Work First bridge** — baseline → bounded request → context → tool works → inspect diff → test → accept/recover → preserve durable truth.
20. **Show That It Works** — the Week 2 completion receipt and what students should be able to demonstrate by the end.

You may split or combine these into more effective visual sequences.

## Prompt examples

Include student-usable prompts, but keep them short enough for slides. Favor structure such as:

```text
I am using Windows 11 and PowerShell 7.
How do I verify which PowerShell version is actually running?
Give me:
1. the exact command,
2. what output I should expect,
3. the official Microsoft documentation,
4. what this check proves and does not prove.
```

Then visibly separate the **answer-finding prompt** from the **verification step performed on the machine**.

When external documentation is cited, use primary/official sources whenever practical (Microsoft PowerShell, Python, Git, Ollama, Aider). Do not use random tutorials as authority when the official source is adequate.

## Scaffold fading

The deck itself should model progressive independence:

- early slides: Jeremy gives the action, explanation, sample prompt, documentation habit, verification, and receipt;
- middle slides: give the task and a prompt structure, but make students fill one or two fields;
- later slides: ask students to propose the question and verification before revealing the instructor version.

The objective is not to create permanent dependence on the deck. The objective is to teach a repeatable method for finding and verifying technical truth.

## Instructor usability

The deck should make Jeremy's live teaching easier.

Where helpful, include subtle instructor cues in Beamer notes/comments or in the accompanying README, such as:
- what question to ask the room;
- where to pause for student prediction;
- what misconception to surface;
- when to let students run the command;
- when to stop and route a **"NOT READY"** student to recovery rather than turning class into machine repair.

Do not clutter projected slides with paragraphs of speaker notes.

## Safety / boundaries

- Do not touch SWOSU production Canvas.
- Do not ask students for API keys, administrator credentials, or cloud-provider secrets.
- Do not replace the canonical `qwen3:8b` / loopback / local-Aider boundary without current source authority.
- Do not turn the deck into an installation free-for-all. The classroom contract remains bounded.
- Do not claim a tool is working because it is installed, opens, or appears in a list.
- Do not copy large chunks of external documentation into the slides. Summarize and link/cite appropriately.

## Build and visual validation

Brandy has LaTeX/Beamer. Build the actual PDF there.

At minimum:

1. compile successfully with the repository/environment's normal LaTeX tooling (prefer `latexmk` if available);
2. fail on LaTeX errors rather than leaving a stale PDF;
3. inspect compile output for overfull boxes and obvious layout failures;
4. render representative PDF pages to images or otherwise inspect the resulting slides visually, especially slides containing code, diagrams, prompt boxes, and the PowerShell walkthrough;
5. verify the final PDF opens and page count is plausible;
6. confirm no personal username/machine-name leakage in student-facing visuals;
7. confirm source and PDF are both committed.

If the deck reveals a curriculum-content conflict, follow the canonical source rather than silently changing the procedure.

## Git / acceptance

Before stopping:

- `git diff --check` must pass;
- commit all in-scope source, assets, PDF, README, and report;
- push the accepted commit to `origin/main`;
- remotely/read-back verify the source and report;
- report exact deck path, PDF path, page count, build command, commit SHA, and any remaining owner-review questions.

Do not deploy the PDF to Canvas in this mission. It is an artifact for owner review first.

Final sentinel:

`WEEK 2 TEACHING SLIDES READY FOR OWNER REVIEW`
