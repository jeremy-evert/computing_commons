# Computing Commons source registry

The Commons is a clearinghouse. This registry records which repository is currently authoritative for each major shared capability so the student-facing Commons can stitch strong sources together without cloning them into drift.

## Canonical source map

| Shared capability | Canonical source | Commons responsibility |
|---|---|---|
| Cross-course curriculum placement and shared-course decisions | `jeremy-evert/swosu_cs_curriculum` | Translate cross-course decisions into a coherent Commons delivery map. |
| Build and Verify Your Local AI Lab | `jeremy-evert/local_ai_lab_setup` | Expose one student journey, module structure, completion model, and stable route into the lab. |
| Windows classroom implementation/evidence for Local AI | `jeremy-evert/windows_classroom` | Consume the accepted Windows contract and validated instructions rather than inventing a second Windows path. |
| AI Fluency I–V and Monday Moments | `jeremy-evert/ai_fluency` | Organize cumulative level visibility, Canvas delivery, and links from host courses. |
| Professional Minds | `jeremy-evert/professional_minds` | Deliver the shared professional-development sequence and remove unnecessary copies from course repos. |
| CS1 disciplinary curriculum | `jeremy-evert/computer_science_1` | Keep only CS1 teaching plus lightweight wrappers around Commons capabilities. |
| CS2 disciplinary curriculum | `jeremy-evert/computer_science_2` | Keep only CS2 teaching plus lightweight wrappers around Commons capabilities. |
| Discrete Structures & Critical Thinking | `jeremy-evert/discrete_structures_and_critical_thinking` | Keep DSCT teaching plus lightweight wrappers around Commons capabilities. |
| Computer Architecture | `jeremy-evert/computer_architecture` | Keep Architecture teaching and provide deeper technical applications of Linux/profiling, hardware behavior, containers, and finale work. |
| Software Engineering | `jeremy-evert/software_engineering` | Keep SWE teaching plus Level 4 applications of shared workflow capabilities. |
| Machine Learning | `jeremy-evert/machine_learning` | Keep ML teaching plus Level 5 applications and the deepest model/evaluation lens. |

## Local AI stitching contract

The Local AI experience is intentionally a multi-repository product:

### `local_ai_lab_setup`

Owns the shared instructional experience:

- what PowerShell, Python, Git, Ollama, Aider, and the approved local model do;
- the student Week 2 learning path;
- readiness/evidence distinctions;
- bounded exercises and troubleshooting guidance;
- shared teaching/support artifacts.

### `windows_classroom`

Owns the Windows classroom evidence and accepted implementation boundary:

- what the restricted Windows environment actually supports;
- reviewed Windows versions/settings;
- student/instructor Windows runbooks;
- experiments and evidence that inform what can safely be promised.

### `computing_commons`

Owns the stitching:

- where students enter;
- which Local AI source/version is the current student path;
- how the lab appears in Recitation/Canvas;
- how completion is tracked;
- which home-course wrappers remain;
- how later levels reuse the capability without reteaching setup.

The Commons should not create a third independent Local AI setup procedure.

## AI Fluency stitching contract

`ai_fluency` already defines a five-level sequence:

1. AI I — Thinking with AI
2. AI II — Improving AI Workflows
3. AI III — Engineering AI Systems
4. AI IV — Applying AI in Software Engineering
5. AI V — Machine Learning and AI Systems

The Commons should make that progression visible and cumulative rather than copying Monday Moments into every course repo.

When Level N is assigned, Levels 1 through N should remain open. Course repos point to the relevant Commons level and keep only disciplinary application/receipt material.

## Professional Minds stitching contract

`professional_minds` remains the source repository for Professional Minds content.

The Commons should provide the recurring student-facing Professional Minds route and level/progression framing. Course repositories should stop being independent authoring homes for generic Professional Minds content.

## Future shared sources

Containers, LaTeX/documentation, Work First, Linux/profiling, Git/source management, professional pathway, and the Farkle + Machine Learning finale may already have strong source material distributed across existing repositories.

Before authoring a new canonical implementation inside `computing_commons`, audit existing sources first. The preferred outcome is often to promote the strongest existing source into the appropriate shared home and have the Commons compose it.

## Registry rule

A source may move as the system matures. When it does, update this registry first so downstream Canvas/course integrations know which throat to choke.
