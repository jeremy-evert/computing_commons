# 002G Savnac read-back and owner visual handoff

Live read-back confirms course 18, three modules in order, five published
pages, and the published 0-point assignment. Evidence is in
`sidecar/evidence/savnac/002G_readback.json`; deployment identity and source
commit are in `002F_deployment_manifest.json`.

## Grace/home path

From Grace/Faith, create the approved private tunnel from the runbook:

```bash
ssh -L 3002:192.168.122.172:3000 jevert@10.2.0.48
```

Open `http://localhost:3002/login/canvas`, sign in with the protected Savnac
account, then open course 18:
`http://localhost:3002/courses/18/modules`.
Start at **00 — Start Here + Kickoff**, then inspect **02 — Week 2: Build and
Verify Local AI**. The exact Canvas destination is Savnac, not SWOSU.

Please judge: (1) whether the first action is obvious, (2) whether the dark
masthead feels calm and attractive, (3) whether spacing/cards feel easy rather
than busy, (4) whether the Week 2 route and bottom shared strip orient you, (5)
whether Home/Back/Next link affordances are clear, and (6) whether recovery
help is visible at the moment of confusion.

Course 17 is an unresolved duplicate shell from the first deployment attempt;
it has not been deleted without owner approval. Quick Tune and synthetic
students have not run. SWOSU Canvas course 24298 was untouched.

**OWNER VISUAL INSPECTION REQUIRED**
