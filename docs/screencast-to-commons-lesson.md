# Protocol: screencast dump → Computing Commons lesson

**Status: active pattern.** First run: `fun_with_LaTeX/` (Sep 2026), from a
raw PowerShell/Copilot screen recording of standing up a first LaTeX project.

This is the repeatable path for turning a thing Jeremy recorded himself doing
— plus whatever notes came with it — into a student-facing Commons lesson:
written guide, companion slides, hosted video link, and a Canvas load. It
exists so each of these does not get re-invented.

---

## Inputs Jeremy provides

1. **A screen recording** (`.mp4`), usually a real working session with the
   snags left in — not a polished demo.
2. **A notes dump** — could be a chat transcript, a scratch file, or a few
   sentences. Treated as raw material, never pasted through verbatim.
3. **A hosting link** for the video (SWOSU SharePoint / Stream, sign-in
   required) — or a request to get one made.
4. **Where it belongs**: which Commons station / module, and the module name
   to use on Canvas.
5. **Whether an announcement goes out**, and to which courses.

## What gets produced

| Artifact | Location | Notes |
| --- | --- | --- |
| `STUDENT_GUIDE.md` | `<lesson>/` in the owning repo | Learning-ladder voice (below). The notes dump, rewritten as instructions. |
| Companion deck | `<lesson>/slides/*.tex` + compiled `.pdf` | Commons visual grammar. 12–20 slides. |
| Extracted frames | `<lesson>/slides/img/` | Lifted from the video at key moments; cropped to remove webcam PiP / unrelated desktop. |
| `README.md` | `<lesson>/` and `<lesson>/slides/` | Index + build command + status table. |
| Flo Canvas mission | `foreman_interface/jobs/tasks/<name>_canvas_load.md` (+ `.writable_roots`) | Target-locked, idempotent, human gate. |
| Announcement draft | inside the Flo mission | Never sent without Jeremy's explicit course list + approval. |

---

## Steps

### 1. Ingest the video

- Probe it: `ffprobe -v error -show_entries format=duration -of default=nw=1 in.mp4`
- Contact sheet: one frame per ~20 s, tiled, timestamp burned in:
  ```
  ffmpeg -i in.mp4 -vf "fps=1/20,scale=640:-1,drawtext=text='%{pts\:hms}':x=8:y=8:fontsize=22:fontcolor=yellow:box=1:boxcolor=black@0.6" frames/f_%03d.png
  ffmpeg -start_number 1 -i frames/f_%03d.png -frames:v 1 -vf "scale=380:-1,tile=6x5:margin=6:padding=4" sheet_0.png
  ```
- Read the sheets, pick the 6–10 moments that carry the lesson (a success
  state, an error message, the fix, the receipt).
- Pull those at full res: `ffmpeg -ss <ts> -i in.mp4 -frames:v 1 -q:v 2 shot.png`
- Crop each to the relevant pane — drop the webcam picture-in-picture, browser
  chrome, taskbar, and anything unrelated on the desktop:
  `ffmpeg -i shot.png -vf "crop=W:H:X:Y" img/name.png`
- Prefer a `verbatim` block over a screenshot when you have the exact command
  or error text — it renders sharper and stays legible when projected.

### 2. Write the student guide

Rewrite the notes dump into instructions in the **Commons learning-ladder
voice** (same as `curriculum/containers-and-repeatable-environments.md`):

- Open with the station and its question.
- **Predict before you run** — 2–3 questions the lesson will answer.
- **DO THIS** (exact command) → **WHAT THIS MEANS** (one plain sentence) →
  **FIND THIS YOURSELF** (a command that shows them the state) → **VERIFY ON
  YOUR MACHINE** (the evidence/receipt) → **KEEP THE RECEIPT** (Git).
- Literally teach the prerequisite before using it (e.g. how to open
  PowerShell before giving PowerShell commands).
- **Keep the failures in.** If the recording hit a snag, the guide walks the
  snag, the real error text, and the fix. Debugging is the content.
- End with a **finish line** paragraph in the student's own voice — what they
  can now honestly claim, and what a clean exit code does *not* prove.
- An **"If something goes wrong"** table: symptom → likely cause → do this.
- A **canonical sources** list linking the real files.
- Put the **video link and the slides link** near the top.

### 3. Build the companion deck

- Copy the preamble from `slides/container_level0/container_level0_slides.tex`
  (DeepNavy / WarmGold, `\setbeamertemplate{footline}` with the Commons
  wordmark, `block` / `alertblock` / `exampleblock`).
- `\documentclass[aspectratio=169,11pt]{beamer}`.
- Title frame states **the whole idea in one sentence**.
- One frame per beat from step 1. `alertblock` for what broke, `exampleblock`
  for what success looks like.
- Define a `\shot` macro with **both** a width and a `height=...,keepaspectratio`
  clamp so a tall screenshot can't overflow the footline. Put a screenshot
  *or* a substantial text block on a frame, not both at full size — use
  `columns` if you need both.
- Build with `pdflatex` twice (no `latexmk`). Compile on Brandy if there is no
  local TeX:
  ```
  scp slides/*.tex slides/img/* brandy:~/build/ && \
  ssh brandy 'cd ~/build && pdflatex ... fun.tex && pdflatex ... fun.tex'
  ```
- Rasterize 4–6 slides (`pdftoppm -png -r 70`) and eyeball for overflow before
  committing.

### 4. Commit to the owning repo

Source, PDF, images, READMEs, in one forward commit. Update the lesson's
status table. Do **not** deploy to Canvas from here.

### 5. Stage the Flo Canvas mission

`foreman_interface/jobs/tasks/<name>_canvas_load.md` + a `.writable_roots`
naming only the april checkout. The mission must:

- **Lock the target** before any mutation: origin `https://swosu.instructure.com`,
  course `24298`, refuse unless the course name contains `Computing Commons`.
- Find or create the named **module**; add the student guide as a **Page**
  (Markdown → Canvas HTML via Harbor), the **video link**, and the **slides
  PDF** as a file item.
- Be **idempotent** — rerun updates, never duplicates. Read every object back.
- **Hard boundaries**: no assignment, gradebook, due date, enrollment,
  navigation, front-page, or other-course change; no secrets in git/chat; no
  force-push.
- **Human gate**: stop after the module is in and read back, for Jeremy to
  walk it in Student View before any class is pointed at it.

### 6. The cross-course announcement (always a gate)

If Jeremy wants students in his *other* courses told about the lesson:

- Draft the announcement text **in the mission file**.
- It does **not** send until Jeremy gives (a) the explicit list of course IDs
  and (b) approval of the wording. Blasting an announcement to a live student
  roster is consequential and outward-facing — it is never a default action.
- Once approved, Flo posts the same announcement to each named course,
  target-locked per course, and reads each one back.

### 7. Close the loop

Evidence file under the owning repo's `sidecar/reports/` (or equivalent).
Update the lesson status table to `live on Canvas` with the module/page IDs.

---

## Standing rules

- **The video shows the mess; the guide shows the recovery.** Neither hides
  the snag.
- **No leaked identifiers in agent-made visuals.** Screenshots from a video
  Jeremy recorded and is publishing himself are his call; crop anyway where
  it's easy, and note it in the slides `README`.
- **Name the artifact in the first minute** — which file, which command.
- **Canvas is downstream of Git.** If the lesson is wrong, fix the repo and
  redeploy; never hand-edit the Canvas copy into being the newer version.
- **One module, not a pile of items.** A page, the video, the deck — grouped.
- **Announcements are a human gate, every time.**
