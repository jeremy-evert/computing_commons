"""Deploy Prompt 011's Home and unpublished Teacher's Table to Savnac course 18."""
from __future__ import annotations

import json
import os
from pathlib import Path
import sys

sys.path[:0] = ["/mnt/brandy_nvme/jevert/git/harbor"]
from harbor.api import create_page, get_page, update_course, update_page  # type: ignore
from harbor.client import CanvasClient  # type: ignore
from harbor.config import load_env, read_canvas_config  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
COURSE_ID = 18
COURSE_TITLE = "Computing Commons — Visual Prototype (Week 2)"


def ensure_page(client: CanvasClient, title: str, slug: str, body: str, published: bool, front_page: bool = False) -> dict:
    try:
        _, current = get_page(client, COURSE_ID, slug)
        update_page(client, COURSE_ID, slug, {
            "wiki_page[title]": title,
            "wiki_page[body]": body,
            "wiki_page[published]": "true" if published else "false",
            "wiki_page[front_page]": "true" if front_page else "false",
        })
        return {"action": "update", "page_id": current.get("page_id"), "url": current.get("url"), "title": title, "published": published, "front_page": front_page}
    except Exception as exc:
        if "404" not in str(exc) and "page not found" not in str(exc).lower():
            raise
        _, created = create_page(client, COURSE_ID, {
            "wiki_page[title]": "Home" if front_page else title,
            "wiki_page[body]": body,
            "wiki_page[published]": "true" if published else "false",
        })
        actual_slug = created.get("url")
        if not actual_slug:
            raise RuntimeError(f"Canvas did not return a page slug for {title!r}")
        if actual_slug != slug:
            raise RuntimeError(f"Canvas generated unexpected slug {actual_slug!r}; expected {slug!r}")
        update_page(client, COURSE_ID, slug, {
            "wiki_page[title]": title,
            "wiki_page[body]": body,
            "wiki_page[published]": "true" if published else "false",
            "wiki_page[front_page]": "true" if front_page else "false",
        })
        return {"action": "create", "page_id": created.get("page_id"), "url": actual_slug, "title": title, "published": published, "front_page": front_page}


def main() -> int:
    load_env()
    config = read_canvas_config()
    if config.api_base_url != "http://192.168.122.172:3000":
        raise SystemExit("refusing: CANVAS_API_BASE_URL is not the Savnac address")
    client = CanvasClient(config)
    course_response = client.get(f"/api/v1/courses/{COURSE_ID}")
    course_response.raise_for_status()
    course = course_response.json()
    if int(course.get("id", -1)) != COURSE_ID or course.get("name") != COURSE_TITLE:
        raise SystemExit("refusing: course 18 is not the expected bounded Savnac prototype")

    home = ensure_page(client, "Computing Commons Home", "home", (ROOT / "previews/home.html").read_text(), True, True)
    table = ensure_page(client, "Teacher's Table", "teachers-table", (ROOT / "previews/teacher-table.html").read_text(), False, False)
    update_course(client, COURSE_ID, {"course[workflow_state]": "available", "course[default_view]": "wiki"})

    manifest = {
        "target": config.api_base_url,
        "course": {"id": COURSE_ID, "title": COURSE_TITLE, "default_view_requested": "wiki"},
        "source_commit": os.popen(f"git -C {ROOT} rev-parse HEAD").read().strip(),
        "pages": [home, table],
        "boundaries": {"savnac_course_18_only": True, "swosu_course_24298_touched": False, "course_17_touched": False, "canonical_repositories_touched": False, "quick_tune_run": False, "synthetic_students_run": False},
    }
    output = ROOT / "sidecar/evidence/savnac/011_deployment_manifest.json"
    output.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"course_id": COURSE_ID, "pages": manifest["pages"], "manifest": str(output)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
