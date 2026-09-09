# Prompt 032 — NRP Student Launchpad Public Showcase

## Owner intent

The public `jeremy-evert/computing_commons` repository is now the student-facing home for a Computing Commons National Research Platform experience.

Jeremy wants this next slice to be ready for two things:

1. students can actually use it without needing access to Jeremy's private operator repositories;
2. Jeremy can open the public repo in class and show a polished, coherent path that feels intentional rather than like a pile of instructor notes.

A tiny starter currently exists at:

`national_research_platform/getting_started.md`

Its current owner intent is that students tell Jeremy which email they use and that they want to authenticate with GitHub so he can get them added and started. Preserve that human-friendly spirit, but verify the actual NRP authentication/onboarding truth before expanding it.

The Fall 2026 CS2 course namespace currently being proven on the operator side is:

`swosu-jevert-cs2-f26`

Treat live operator proof as evidence to verify, not assumptions to copy.

## Owning repository

`jeremy-evert/computing_commons`

Read and follow `AGENTS.md` first.

The Commons is the shared recitation, clearinghouse, and apprenticeship layer. Its rule is **stitch, do not fork**. This mission should create the public student experience, not transplant private operator infrastructure into the Commons.

## Important source boundaries

Use current truth from the relevant repositories, but respect visibility and ownership:

- `jeremy-evert/computing_commons` is public and must contain everything a student is expected to click or read without private-repo access.
- `jeremy-evert/nrp_k8s_launcher` is currently a private operator/instructor repository. It may provide verified technical evidence and patterns, but do not create public instructions that depend on students being able to open it.
- `jeremy-evert/swosu-nrp-classroom` is currently private. It may be useful as provenance/archaeology, but do not leave public dead-end links to material students cannot access.
- official public NRP/Nautilus documentation may be linked when it is the correct canonical source.
- if the Student-Zero namespace bootstrap mission/report in `nrp_k8s_launcher` exists, inspect it and use its verified results as operator-side evidence. If it is incomplete, do not invent its result.

No secrets, tokens, kubeconfigs, credential values, student private data, private URLs containing credentials, or instructor-only operational details belong in the public repository.

## Mission

Build the smallest **student-ready NRP launchpad** in `computing_commons` that Jeremy can publish to the class and confidently show live.

Do not build a platform. Build a clear front door, a safe first success, and a clean handoff into deeper work later.

### 1. Archaeology before construction

Inspect current `computing_commons` NRP material, repository navigation, visual/design conventions, student-facing writing style, relevant scripts, and any recent work that should be reused.

Inspect the current NRP operator-side truth needed to keep the public instructions technically honest. Determine what is safe and appropriate for students versus what belongs only to instructor/operator tooling.

Check repository visibility for any source you intend to link. A public student path must not depend on inaccessible private GitHub pages.

### 2. Make the public NRP area feel like a real student destination

Turn `national_research_platform/` into a coherent, polished student-facing entry point.

At minimum, a student arriving there should quickly understand:

- what the National Research Platform is in the context of this class;
- why we are using it;
- what Jeremy needs from the student before access can be provisioned;
- the difference between being added to the course namespace and authenticating from their own machine;
- what they need installed or available locally;
- how to verify that their own identity can see the intended course namespace;
- how to run one tiny, safe first workload once access is ready;
- how to prove that workload actually completed;
- how to clean up what they created;
- where to go when something fails;
- what they should never paste into GitHub, Canvas, chat, screenshots, or assignments.

Use plain student language. Assume curiosity, not Kubernetes expertise.

### 3. Give students one boringly reliable first success

Create the smallest safe public Student-One path that can be completed with a student's own identity.

Prefer a CPU-only, low-resource hello/smoke workload. No GPU is needed for the first success.

The student path should be explicit about the course namespace rather than silently relying on whatever namespace happens to be configured locally.

If a tiny manifest, script, or command sequence belongs in the Commons to make this repeatable, create it. Keep it narrow and inspectable. Do not copy the private `nrp_k8s_launcher` into the public repo.

The experience should produce a simple evidence receipt a student can understand, for example: namespace visible, workload created, completion observed, logs recovered, cleanup verified.

Do not expose or mint credentials. Do not create shared student ServiceAccounts or shared course tokens.

### 4. Separate enrollment, Kubernetes identity, and hosted-LLM identity

The public material must clearly distinguish these concepts without drowning students in infrastructure trivia:

- Jeremy/instructor adding the student to the appropriate NRP course/group/namespace;
- the student's personal authentication path for Kubernetes;
- the explicit course namespace, currently `swosu-jevert-cs2-f26` for the Fall 2026 CS2 proof;
- any separate personal hosted-LLM token/authentication path;
- instructor automation identities, which students should not use or receive.

If the exact student hosted-LLM onboarding flow is not yet verified, say so cleanly and make it an intentionally later step. Do not fill the gap with a shared token.

### 5. Make it show-day ready

Jeremy should be able to open the public repository in front of the class and walk through the experience in a few minutes.

Polish navigation and presentation accordingly. Favor a strong student landing page, short sections, copyable commands, meaningful headings, and visible success/failure checkpoints.

Create a short **instructor demo path** in an appropriate public-safe location that tells Jeremy what to click/run/show in roughly 3–5 minutes. It must contain no secrets and should be safe for students to read too.

Also create a compact **Canvas-ready handoff** or announcement/module copy that Jeremy can paste into the class when ready. Do not mutate production Canvas in this mission.

If the root README or other navigation should point students into the NRP launchpad, update it cleanly without turning NRP into the entire identity of Computing Commons.

### 6. Public-repository safety review

Before accepting the work, inspect all new/changed public-facing material for:

- secrets or credential-shaped text;
- private repository links that students cannot open;
- local absolute paths or hostnames that only make sense on Jeremy's machines;
- instructions that accidentally use Jeremy's personal/operator identity as the student path;
- commands that can mutate the wrong namespace because `-n/--namespace` is omitted;
- cleanup instructions that are broader than the resource the student created;
- stale or speculative claims presented as verified fact.

### 7. Leave a seam for the movie, but do not scrape it yet

Jeremy intends a later pass where we mine/scrape the existing movie/recording for useful explanations, examples, phrasing, or missing student context.

That is **not** this mission.

Make the public structure clean enough that later movie-derived material has obvious homes, but do not wait on, transcribe, scrape, or reconstruct the recording now. First get the NRP launchpad structurally and technically green.

## Durable report

Leave the detailed after-action report at:

`sidecar/reports/032_nrp_student_launchpad_public_showcase.md`

The report must include:

- current truth discovered;
- files created/changed and why;
- what the public student path now is from first click through first verified workload;
- which private/operator sources were consulted and what was intentionally not exposed;
- exact validation performed;
- any live smoke proof performed and the identity/namespace used, with secrets omitted;
- public-link/accessibility review result;
- the 3–5 minute show-day path;
- the Canvas-ready handoff location;
- what remains for the later movie/recording mining pass;
- any genuine `HUMAN_GATE` that remains.

## Acceptance criteria

The mission is green only when all applicable items are independently verified:

1. A student can start from the public `computing_commons` repository and find the NRP launchpad without instructor explanation.
2. The NRP area explains onboarding, authentication, namespace selection, first workload, verification, cleanup, and credential hygiene in student language.
3. The first workload path is CPU-only, low risk, explicitly namespace-scoped, and does not depend on private operator repositories.
4. No public instruction requires access to `nrp_k8s_launcher` or `swosu-nrp-classroom` while those repositories remain private.
5. No secret, token, kubeconfig, shared credential, student private data, or instructor automation credential is exposed.
6. Jeremy has a public-safe 3–5 minute demo path and a Canvas-ready handoff he can use after review.
7. Root/navigation links are coherent and all relevant public links are checked.
8. Repository-native validation plus `git diff --check` pass.
9. The durable report is complete and truthful.
10. Completed in-scope changes are committed and pushed normally according to repository policy.

## Boundaries

- Do not enroll students or change NRP group membership in this mission.
- Do not create shared student credentials.
- Do not create/apply broad RBAC or cluster-wide policy.
- Do not expose Jeremy's operator ServiceAccount/token/kubeconfig.
- Do not mutate production Canvas.
- Do not duplicate the private launcher into this public repository.
- Do not make GPU access part of first-day success.
- Do not scrape the movie/recording yet.
- Do not redesign all of Computing Commons merely because this slice is being polished.

The target is a front door students can actually walk through and a demo Jeremy can enjoy showing. Make the first success small, visible, and real.