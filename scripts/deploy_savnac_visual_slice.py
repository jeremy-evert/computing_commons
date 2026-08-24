"""Idempotently deploy the bounded Commons visual slice to Savnac.

The caller must explicitly source the protected Savnac environment. This
script refuses non-Savnac URLs and writes only the named prototype course.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = ["/mnt/brandy_nvme/jevert/git/harbor", "/mnt/brandy_nvme/jevert/git/imprint"]

from harbor.api import create_course, list_modules, update_course, update_module  # type: ignore
from harbor.client import CanvasClient  # type: ignore
from harbor.config import load_env, read_canvas_config  # type: ignore
from imprint.reconcile import push_course  # type: ignore
from imprint.schema import DesiredCourse, DesiredModule, DesiredObject  # type: ignore

TITLE = "Computing Commons — Visual Prototype (Week 2)"


def page(title: str, body: str, slug: str) -> DesiredObject:
    return DesiredObject(kind="page", title=title, body_markdown=body, source_ref=slug)


def main() -> int:
    load_env()
    config = read_canvas_config()
    if config.api_base_url != "http://192.168.122.172:3000":
        raise SystemExit("refusing: CANVAS_API_BASE_URL is not the Savnac address")
    client = CanvasClient(config)
    response = client.get("/api/v1/accounts/1/courses?state[]=available&state[]=unpublished&per_page=100")
    response.raise_for_status()
    courses = response.json()
    course = next((c for c in courses if c.get("name") == TITLE), None)
    if course is None:
        status, course = create_course(client, 1, {"course[name]": TITLE, "course[course_code]": "COMMONS-VISUAL-W2", "course[is_public]": "false", "course[workflow_state]": "available"})
        if status >= 300:
            raise SystemExit(f"course creation failed with HTTP {status}")
    course_id = int(course["id"])
    base = f"/courses/{course_id}/pages/"
    kickoff = f"{base}commons-kickoff"
    week2 = f"{base}week-2-local-ai"
    tools = f"{base}week-2-verify-tools"
    recovery = f"{base}week-2-recovery"
    recitation = f"{base}recitation-get-help"
    kickoff_html = (ROOT / "previews/kickoff.html").read_text()
    week2_html = (ROOT / "previews/week2-local-ai.html").read_text()
    tools_md = (ROOT / "curriculum/week2/tools.md").read_text()
    recovery_md = (ROOT / "curriculum/week2/recovery.md").read_text()
    recitation_md = (ROOT / "curriculum/recitation.md").read_text()
    plan = DesiredCourse(course_label=TITLE, course_id=course_id, modules=[
        DesiredModule(title="00 — Start Here + Kickoff", position=1, objects=[page("Success Foundations / Semester Kickoff", kickoff_html, "previews/kickoff.html")]),
        DesiredModule(title="01 — Recitation / Get Help", position=2, objects=[page("Recitation / Get Help", recitation_md, "curriculum/recitation.md")]),
        DesiredModule(title="02 — Week 2: Build and Verify Local AI", position=3, objects=[
            page("Week 2 — Build and Verify Your Local AI Lab", week2_html, "previews/week2-local-ai.html"),
            page("Week 2 — Verify the tools", tools_md, "curriculum/week2/tools.md"),
            page("Week 2 — Recovery with evidence", recovery_md, "curriculum/week2/recovery.md"),
            DesiredObject(kind="assignment", title="Week 2 visual prototype check", body_markdown="Bring your evidence receipt to Recitation. This prototype is worth 0 points and exists to test the completion path.", points_possible_override=0, grading_type="not_graded", submission_types=["online_text_entry"], source_ref="controller-002 bounded prototype"),
        ]),
    ])
    result = push_course(client, plan, sandbox=True, force=True, prune_scope="module")
    update_course(client, course_id, {"course[workflow_state]": "available", "course[default_view]": "modules"})
    for live_module in list_modules(client, course_id):
        if live_module.get("name") in {m.title for m in plan.modules}:
            update_module(client, course_id, int(live_module["id"]), {"module[published]": "true"})
    manifest = {"target": config.api_base_url, "course": {"id": course_id, "title": TITLE}, "source_commit": os.popen(f"git -C {ROOT} rev-parse HEAD").read().strip(), "objects": [e.model_dump() for e in result.log], "result": result.model_dump(), "swosu_course_24298_touched": False}
    out = ROOT / "sidecar/evidence/savnac/002F_deployment_manifest.json"
    out.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"course_id": course_id, "course_title": TITLE, "created": result.created_count, "updated": result.updated_count, "skipped": result.skipped_count, "manifest": str(out)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
