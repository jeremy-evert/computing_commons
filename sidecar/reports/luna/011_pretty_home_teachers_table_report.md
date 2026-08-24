# Prompt 011 — Pretty Home + Teacher's Table acceptance report

## Verdict

**PRETTY HOME + TEACHER'S TABLE ACCEPTED; CONTINUE TO PROMPT 012 IF UNGATED**

Prompt 011 was completed against Savnac Canvas course **18** only.

## Deliverables

- Student Home source/preview: `previews/home.html`
- Instructor cockpit source/preview: `previews/teacher-table.html`
- Pre-mutation plan: `sidecar/reports/luna/011_pretty_home_teachers_table_plan.md`
- Deployment manifest: `sidecar/evidence/savnac/011_deployment_manifest.json`
- Canvas readback: `sidecar/evidence/savnac/011_readback.json`
- Deployment/readback tooling: `scripts/deploy_prompt011.py`, `scripts/readback_prompt011.py`

## Readback acceptance

- Home route: `/courses/18/pages/home`; title `Computing Commons Home`; published; `front_page=true`.
- Course default view: `wiki`, so course 18 opens at the Home page rather than Modules.
- Teacher's Table route: `/courses/18/pages/teachers-table`; title exactly `Teacher's Table`; unpublished and not placed in a student module.
- Home contains current Week 2 Monday/Wednesday/Friday cards, Local AI/Aider runway, Recitation/Get Help recovery, and compact Week 3 Monday/Wednesday/Friday preview routes.
- Exact-slug readback passed all checks: home publication, front-page marker, default view, Teacher's Table unpublished state, required route presence, and student-facing href hygiene.

## Boundaries

- Canonical `ai_fluency`, `professional_minds`, and `swosu_cs_curriculum` repositories unchanged.
- SWOSU production Canvas course 24298 untouched; Savnac course 17 untouched.
- Quick Tune and synthetic students did not run.
- No credentials, private paths, or student data entered source/evidence.

Prompt 011 leaves no source, provenance, Canvas-health, or human-decision gate. Prompt 012 may continue.
