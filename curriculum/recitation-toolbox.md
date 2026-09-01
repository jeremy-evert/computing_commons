# Recitation Toolbox

After the initial shared runway, the Computing Commons should behave like a reusable workshop rather than a rigid week-by-week course.

Home courses call the recitation they need when they need it.

## Stations

### [Containers and repeatable environments](containers-and-repeatable-environments.md) — LIVE

Question: **Can another environment reproduce what I just did?**

Shared outcomes:

- understand host vs environment/container;
- run a bounded containerized task;
- understand files/mounts practically;
- capture evidence about what environment ran the task;
- use containers for repeatability, not vocabulary trivia.

Canonical shared module, deck, and pinned/published container image are
live; Architecture and DSCT link back to it rather than forking their own
copy. See [`containers-and-repeatable-environments.md`](containers-and-repeatable-environments.md).

## Candidate stations

### Documentation and LaTeX

Question: **Can another human understand and inspect what I did?**

Shared outcomes:

- useful Markdown;
- useful README structure;
- minimum-useful LaTeX;
- commands/results/assumptions/captions/evidence;
- documentation as part of the work.

### Work First

Question: **Can I organize work so tools help without taking control?**

Shared outcomes:

- distinguish the project/product from the workspace/process around it;
- keep source, plans, prompts, evidence, and reports understandable;
- delegate bounded details while retaining direction and verification;
- narrow tasks enough that local/smaller models can succeed;
- preserve durable truth outside transient chat.

### Linux command line and profiling

Question: **Can I look under the dashboard when the machine behaves strangely?**

Shared outcomes:

- navigate with `pwd`, `ls`, and `cd`;
- inspect text/files;
- locate files/processes;
- inspect CPU, memory, disk, and process behavior;
- use timing/profiling evidence;
- recognize GPU visibility where appropriate;
- begin with inspection rather than broad administration.

Computer Architecture is the strongest deeper technical lens for this station.

### Git / source-code management

Question: **Can I change something without being afraid of losing yesterday?**

Shared outcomes:

- repository/worktree/state;
- status/diff before acting;
- useful commits;
- history;
- practical branching;
- bounded recovery;
- Git before GitHub.

## Source audit rule

Before authoring these stations from scratch in this repository, audit the existing course/shared repositories for the strongest current material.

The preferred architecture is:

**strong canonical source → Computing Commons station → course-specific application**.

Do not copy six half-overlapping tutorials into a seventh folder and call that centralization.
