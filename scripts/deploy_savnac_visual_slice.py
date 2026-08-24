"""Idempotently deploy the bounded Commons visual slice to Savnac.

The caller must explicitly source the protected Savnac environment. This
script refuses non-Savnac URLs and writes only the named prototype course.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = ["/mnt/brandy_nvme/jevert/git/harbor", "/mnt/brandy_nvme/jevert/git/imprint"]

from harbor.api import create_course, list_modules, update_course, update_module  # type: ignore
from harbor.client import CanvasClient  # type: ignore
from harbor.config import load_env, read_canvas_config  # type: ignore
from imprint.reconcile import push_course  # type: ignore
from imprint.schema import DesiredCourse, DesiredModule, DesiredObject  # type: ignore

TITLE = "Computing Commons — Visual Prototype (Week 2)"
COURSE_ID = 18


def page(title: str, body: str, slug: str) -> DesiredObject:
    return DesiredObject(kind="page", title=title, body_markdown=body, source_ref=slug)


def canvas_links(body: str, course_id: int) -> str:
    """Translate repository preview filenames into stable Canvas page URLs."""
    root = f"/courses/{course_id}/pages/"
    mapping = {
        "start-here.html": root + "success-foundations-slash-semester-kickoff",
        "kickoff.html": root + "success-foundations-slash-semester-kickoff",
        "week2-local-ai.html": root + "week-2-build-and-verify-your-local-ai-lab",
        "week2-tools.html": root + "week-2-verify-the-tools",
        "week2-recovery.html": root + "week-2-recovery-with-evidence",
        "week2-inventory.html": root + "week-2-inventory-what-you-already-have",
        "week2-foundation.html": root + "week-2-verify-the-windows-foundation",
        "week2-ollama.html": root + "week-2-confirm-ollama",
        "week2-model.html": root + "week-2-confirm-the-approved-model",
        "week2-direct.html": root + "week-2-say-hello-directly-to-ollama",
        "week2-aider.html": root + "week-2-get-or-confirm-aider",
        "week2-worktree.html": root + "week-2-prepare-the-tiny-git-worktree",
        "week2-first-edit.html": root + "week-2-say-hello-with-aider",
        "week2-toy-wins.html": root + "week-2-three-tiny-aider-wins",
        "week2-work-first.html": root + "week-2-bridge-to-work-first",
        "week2-show-it-works.html": root + "week-2-show-that-it-works",
        "week2-shared-rhythm.html": root + "week-2-shared-rhythm",
        "week2-ai-fluency.html": root + "monday-ai-fluency-gather-context",
        "week2-make-it-stick.html": root + "wednesday-make-it-stick-retrieval-practice",
        "week2-mindset.html": root + "friday-mindset-at-work",
        "week3-shared-rhythm.html": root + "week-3-shared-rhythm",
        "week3-ai-fluency.html": root + "monday-plan-the-work",
        "week3-professional-minds-wednesday.html": root + "wednesday-grow-through-mistakes",
        "week3-professional-minds-friday.html": root + "friday-resilience-and-risk-competence",
        "recovery.md": root + "week-2-recovery-with-evidence",
        "../recitation.md": root + "recitation-slash-get-help",
        "recitation.html": root + "recitation-slash-get-help",
    }
    for old, new in mapping.items():
        body = body.replace(old, new)
    return body


def main() -> int:
    load_env()
    config = read_canvas_config()
    if config.api_base_url != "http://192.168.122.172:3000":
        raise SystemExit("refusing: CANVAS_API_BASE_URL is not the Savnac address")
    client = CanvasClient(config)
    response = client.get(f"/api/v1/courses/{COURSE_ID}")
    response.raise_for_status()
    course = response.json()
    if int(course.get("id", -1)) != COURSE_ID or course.get("name") != TITLE:
        raise SystemExit(f"refusing: course {COURSE_ID} is not the expected bounded Savnac course")
    course_id = COURSE_ID
    base = f"/courses/{course_id}/pages/"
    kickoff = f"{base}commons-kickoff"
    week2 = f"{base}week-2-local-ai"
    tools = f"{base}week-2-verify-tools"
    recovery = f"{base}week-2-recovery"
    recitation = f"{base}recitation-get-help"
    kickoff_html = canvas_links((ROOT / "previews/kickoff.html").read_text(), course_id)
    week2_html = canvas_links((ROOT / "previews/week2-local-ai.html").read_text(), course_id)
    tools_md = canvas_links((ROOT / "curriculum/week2/tools.md").read_text(), course_id)
    recovery_md = canvas_links((ROOT / "curriculum/week2/recovery.md").read_text(), course_id)
    recitation_md = (ROOT / "curriculum/recitation.md").read_text()
    week2_routes = [
        ("Week 2 — Inventory what you already have", "previews/week2-inventory.html"),
        ("Week 2 — Verify the Windows foundation", "previews/week2-foundation.html"),
        ("Week 2 — Confirm Ollama", "previews/week2-ollama.html"),
        ("Week 2 — Confirm the approved model", "previews/week2-model.html"),
        ("Week 2 — Say hello directly to Ollama", "previews/week2-direct.html"),
        ("Week 2 — Get or confirm Aider", "previews/week2-aider.html"),
        ("Week 2 — Prepare the tiny Git worktree", "previews/week2-worktree.html"),
        ("Week 2 — Say hello with Aider", "previews/week2-first-edit.html"),
        ("Week 2 — Three tiny Aider wins", "previews/week2-toy-wins.html"),
        ("Week 2 — Bridge to Work First", "previews/week2-work-first.html"),
    ]
    week2_pages = [page(title, canvas_links((ROOT / path).read_text(), course_id), path) for title, path in week2_routes]
    shared_rhythm_pages = [
        ("Week 2 — Shared Rhythm", "previews/week2-shared-rhythm.html"),
        ("Monday — AI Fluency: Gather Context", "previews/week2-ai-fluency.html"),
        ("Wednesday — Make It Stick: Retrieval Practice", "previews/week2-make-it-stick.html"),
        ("Friday — Mindset at Work", "previews/week2-mindset.html"),
    ]
    shared_rhythm_objects = [
        page(title, canvas_links((ROOT / path).read_text(), course_id), path)
        for title, path in shared_rhythm_pages
    ]
    shared_rhythm_objects.extend([
        DesiredObject(kind="file", title="Wednesday reading — Make It Stick", source_path="/mnt/brandy_nvme/jevert/git/professional_minds/readings/week_02_wed_retrieval_practice.md", file_folder_path="week_2_shared_rhythm", source_ref="professional_minds/readings/week_02_wed_retrieval_practice.md"),
        DesiredObject(kind="file", title="Wednesday slides — Make It Stick", source_path="/mnt/brandy_nvme/jevert/git/professional_minds/presentations/beamer/week_02_wed/week02_wed.pdf", file_folder_path="week_2_shared_rhythm", source_ref="professional_minds/presentations/beamer/week_02_wed/week02_wed.pdf"),
        DesiredObject(kind="file", title="Friday reading — Mindset at Work", source_path="/mnt/brandy_nvme/jevert/git/professional_minds/readings/week_02_fri_mindset_at_work.md", file_folder_path="week_2_shared_rhythm", source_ref="professional_minds/readings/week_02_fri_mindset_at_work.md"),
        DesiredObject(kind="file", title="Friday slides — Mindset at Work", source_path="/mnt/brandy_nvme/jevert/git/professional_minds/presentations/beamer/week_02_fri/week02_fri.pdf", file_folder_path="week_2_shared_rhythm", source_ref="professional_minds/presentations/beamer/week_02_fri/week02_fri.pdf"),
    ])
    week3_pages = [
        ("Week 3 — Shared Rhythm", "previews/week3-shared-rhythm.html"),
        ("Monday — AI Fluency: Plan the Work", "previews/week3-ai-fluency.html"),
        ("Wednesday — Professional Minds: Grow through mistakes", "previews/week3-professional-minds-wednesday.html"),
        ("Friday — Professional Minds: Resilience and risk competence", "previews/week3-professional-minds-friday.html"),
    ]
    week3_objects = [page(title, canvas_links((ROOT / path).read_text(), course_id), path) for title, path in week3_pages]
    week3_objects.extend([
        DesiredObject(kind="file", title="Monday source — Plan the Work", source_path="/mnt/brandy_nvme/jevert/git/ai_fluency/ai_i/monday_moments/week_03_plan_the_work/monday_moment.md", file_folder_path="week_3_shared_rhythm", source_ref="ai_fluency/ai_i/monday_moments/week_03_plan_the_work/monday_moment.md"),
        DesiredObject(kind="file", title="Monday activity — Plan the Work", source_path="/mnt/brandy_nvme/jevert/git/ai_fluency/ai_i/monday_moments/week_03_plan_the_work/student_activity.md", file_folder_path="week_3_shared_rhythm", source_ref="ai_fluency/ai_i/monday_moments/week_03_plan_the_work/student_activity.md"),
        DesiredObject(kind="file", title="Monday instructor guide — Plan the Work", source_path="/mnt/brandy_nvme/jevert/git/ai_fluency/ai_i/monday_moments/week_03_plan_the_work/instructor_guide.md", file_folder_path="week_3_shared_rhythm", source_ref="ai_fluency/ai_i/monday_moments/week_03_plan_the_work/instructor_guide.md"),
        DesiredObject(kind="file", title="Monday rubric — Plan the Work", source_path="/mnt/brandy_nvme/jevert/git/ai_fluency/ai_i/monday_moments/week_03_plan_the_work/assessment_rubric.md", file_folder_path="week_3_shared_rhythm", source_ref="ai_fluency/ai_i/monday_moments/week_03_plan_the_work/assessment_rubric.md"),
        DesiredObject(kind="file", title="Monday portfolio artifact — Plan-first Workflow", source_path="/mnt/brandy_nvme/jevert/git/ai_fluency/ai_i/monday_moments/week_03_plan_the_work/portfolio_artifact_plan_first_workflow.md", file_folder_path="week_3_shared_rhythm", source_ref="ai_fluency/ai_i/monday_moments/week_03_plan_the_work/portfolio_artifact_plan_first_workflow.md"),
        DesiredObject(kind="file", title="Wednesday reading — Grow through mistakes", source_path="/mnt/brandy_nvme/jevert/git/professional_minds/readings/week_03_wed_growing_through_mistakes.md", file_folder_path="week_3_shared_rhythm", source_ref="professional_minds/readings/week_03_wed_growing_through_mistakes.md"),
        DesiredObject(kind="file", title="Wednesday slides — Grow through mistakes", source_path="/mnt/brandy_nvme/jevert/git/professional_minds/presentations/beamer/week_03_wed/week03_wed.pdf", file_folder_path="week_3_shared_rhythm", source_ref="professional_minds/presentations/beamer/week_03_wed/week03_wed.pdf"),
        DesiredObject(kind="file", title="Friday reading — Resilience and risk competence", source_path="/mnt/brandy_nvme/jevert/git/professional_minds/readings/week_03_fri_resilience_and_risk_competence.md", file_folder_path="week_3_shared_rhythm", source_ref="professional_minds/readings/week_03_fri_resilience_and_risk_competence.md"),
        DesiredObject(kind="file", title="Friday slides — Resilience and risk competence", source_path="/mnt/brandy_nvme/jevert/git/professional_minds/presentations/beamer/week_03_fri/week03_fri.pdf", file_folder_path="week_3_shared_rhythm", source_ref="professional_minds/presentations/beamer/week_03_fri/week03_fri.pdf"),
    ])
    plan = DesiredCourse(course_label=TITLE, course_id=course_id, modules=[
        DesiredModule(title="00 — Start Here + Kickoff", position=1, objects=[page("Success Foundations / Semester Kickoff", kickoff_html, "previews/kickoff.html")]),
        DesiredModule(title="01 — Recitation / Get Help", position=2, objects=[page("Recitation / Get Help", recitation_md, "curriculum/recitation.md")]),
        DesiredModule(title="02 — Week 2: Build and Verify Local AI", position=3, objects=[
            page("Week 2 — Build and Verify Your Local AI Lab", week2_html, "previews/week2-local-ai.html"),
            page("Week 2 — Verify the tools", tools_md, "curriculum/week2/tools.md"),
            page("Week 2 — Recovery with evidence", recovery_md, "curriculum/week2/recovery.md"),
            *week2_pages,
            DesiredObject(kind="assignment", title="Week 2 — Show That It Works", body_markdown="Bring a concise evidence receipt: direct Ollama success, bounded Aider change, inspected diff, independent test, and one Work First sentence. This completion object is worth 0 points.", points_possible_override=0, grading_type="not_graded", submission_types=["online_text_entry"], source_ref="prompt-005 bounded completion"),
        ]),
        DesiredModule(title="03 — Week 2: Shared Rhythm", position=4, objects=shared_rhythm_objects),
        DesiredModule(title="04 — Week 3: Shared Rhythm", position=5, objects=week3_objects),
    ])
    result = push_course(client, plan, sandbox=True, force=True, prune_scope="module")
    update_course(client, course_id, {"course[workflow_state]": "available", "course[default_view]": "modules"})
    for live_module in list_modules(client, course_id):
        if live_module.get("name") in {m.title for m in plan.modules}:
            update_module(client, course_id, int(live_module["id"]), {"module[published]": "true"})
    manifest = {"target": config.api_base_url, "course": {"id": course_id, "title": TITLE}, "source_commit": os.popen(f"git -C {ROOT} rev-parse HEAD").read().strip(), "objects": [e.model_dump() for e in result.log], "result": result.model_dump(), "swosu_course_24298_touched": False}
    out = ROOT / "sidecar/evidence/savnac/010_deployment_manifest.json"
    out.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"course_id": course_id, "course_title": TITLE, "created": result.created_count, "updated": result.updated_count, "skipped": result.skipped_count, "manifest": str(out)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
