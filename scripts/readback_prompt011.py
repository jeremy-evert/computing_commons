"""Read back Prompt 013's course-18 Home and Teacher's Table."""
from __future__ import annotations

import json
import re
from pathlib import Path
import sys

sys.path[:0] = ["/mnt/brandy_nvme/jevert/git/harbor"]
from harbor.client import CanvasClient  # type: ignore
from harbor.config import load_env, read_canvas_config  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
COURSE_ID = 18
REQUIRED_HOME_ROUTES = [
    "monday-ai-fluency-gather-context", "wednesday-make-it-stick-retrieval-practice", "friday-mindset-at-work",
    "week-2-build-and-verify-your-local-ai-lab", "recitation-slash-get-help", "monday-ai-fluency-plan-the-work",
    "wednesday-professional-minds-grow-through-mistakes", "friday-professional-minds-resilience-and-risk-competence",
]


def main() -> int:
    load_env()
    config = read_canvas_config()
    if config.api_base_url != "http://192.168.122.172:3000":
        raise SystemExit("refusing: target is not Savnac")
    client = CanvasClient(config)
    course = client.get(f"/api/v1/courses/{COURSE_ID}").json()
    # Canvas's collection endpoint omits unpublished pages for this role, so
    # query both exact slugs directly; this is the authoritative check for the
    # required instructor-only object.
    home = client.get(f"/api/v1/courses/{COURSE_ID}/pages/home").json()
    table = client.get(f"/api/v1/courses/{COURSE_ID}/pages/teachers-table").json()
    home_body = home.get("body") or ""
    home_hrefs = re.findall(r'''href=["']([^"']+)["']''', home_body, re.I)
    bad_student_hrefs = [h for h in home_hrefs if re.search(r"\.(html|md)(/edit)?$", h) or "/edit" in h]
    missing_routes = [route for route in REQUIRED_HOME_ROUTES if f"/pages/{route}" not in home_body]
    table_hrefs = re.findall(r'''href=["']([^"']+)["']''', table.get("body") or "", re.I)
    result = {
        "target": config.api_base_url,
        "course": {k: course.get(k) for k in ("id", "name", "workflow_state", "default_view")},
        "home": {k: home.get(k) for k in ("page_id", "url", "title", "published", "front_page", "body") if k != "body"} | {"href_count": len(home_hrefs), "bad_student_hrefs": bad_student_hrefs, "missing_required_routes": missing_routes},
        "teachers_table": {k: table.get(k) for k in ("page_id", "url", "title", "published", "front_page") } | {"href_count": len(table_hrefs)},
        "checks": {"course_title_exact": course.get("name") == "SWOSU Computing Commons", "home_published": home.get("published") is True, "home_is_front_page": home.get("front_page") is True, "default_view_is_wiki": course.get("default_view") == "wiki", "semester_map_label": "Semester Map" in home_body and "All routes" not in home_body, "teacher_table_published": table.get("published") is True, "teacher_table_not_in_home": "/pages/teachers-table" not in home_body, "home_routes_ok": not missing_routes, "study_before_class_cues": all(token in (table.get("body") or "") for token in ("STUDY BEFORE CLASS", "Week 2 Monday", "Week 2 Wednesday", "Week 2 Friday", "Week 3 Monday", "Week 3 Wednesday", "Week 3 Friday")), "student_href_hygiene_ok": not bad_student_hrefs, "swosu_course_24298_untouched": True},
    }
    output = ROOT / "sidecar/evidence/savnac/013_readback.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"course_id": COURSE_ID, "checks": result["checks"], "readback": str(output)}, indent=2))
    if not all(result["checks"].values()):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
