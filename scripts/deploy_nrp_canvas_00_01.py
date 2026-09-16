#!/usr/bin/env python3
"""Bounded, additive Canvas deploy: NRP teaching slice 00+01 into Computing
Commons (course 24298 only).

Mission: jobs/tasks/computing_commons_nrp_canvas_00_01_deploy_033.md
Prompt:  sidecar/prompts/033_nrp_canvas_00_01_bounded_deployment.md
         (pinned dc7ad84732cd8a0c9e29abaec6cd7bd2f541753c)

Creates one new Module ("National Research Platform — Your First Remote
Workload") with exactly two published student-visible Pages, in order:
  00 — Start Here: What Are We About to Do?
  01 — Your Laptop Is Not the Whole Computer

Content fixes applied during markdown->Canvas conversion (not present in the
raw source files):
  1. 01's closing relative link `(../README.md)` is rewritten to the public
     GitHub URL for national_research_platform/README.md (relative links
     404 inside Canvas).
  2. 00's "Where to go next" cross-reference to 01 is corrected from
     "01 — Video: Your Laptop Is Not the Whole Computer" to the real page
     title "01 — Your Laptop Is Not the Whole Computer".

No assignment, points, submission, due date, rubric, or enrollment object is
created. Course allowlist is enforced on the client (24298 only).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
SIBLING_ROOT = ROOT.parent
for name in ("harbor",):
    p = SIBLING_ROOT / name
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from harbor.api import create_module, create_module_item, create_page  # type: ignore
from harbor.client import CanvasClient  # type: ignore
from harbor.config import CanvasConfig, load_env, read_canvas_config  # type: ignore

COURSE_ID = 24298
SLICE_DIR = ROOT / "national_research_platform" / "teaching_slice"
README_URL = "https://github.com/jeremy-evert/computing_commons/blob/main/national_research_platform/README.md"

RECEIPT_PATH = ROOT / "sidecar/runs/nrp_canvas_00_01_deploy.json"


def _client() -> CanvasClient:
    load_env()
    config = read_canvas_config(enforce_course_allowlist=False)
    return CanvasClient(CanvasConfig(config.api_base_url, config.api_token, frozenset({COURSE_ID})))


def _md_to_html(text: str) -> str:
    return markdown.markdown(text, extensions=["fenced_code", "tables"])


def _build_00_html() -> str:
    src = (SLICE_DIR / "00_start_here.md").read_text()
    # Drop the leading H1 (Canvas page already carries the title) and fix
    # the stale "Video:" cross-reference to 01's real title.
    body = re.sub(r"^# .*\n+", "", src, count=1)
    body = body.replace(
        "**01 — Video: Your Laptop Is Not the Whole Computer**",
        "**01 — Your Laptop Is Not the Whole Computer**",
    )
    assert "Video:" not in body, "stale cross-reference fix did not apply"
    return _md_to_html(body)


def _build_01_html() -> str:
    src = (SLICE_DIR / "01_your_laptop_is_not_the_whole_computer.md").read_text()
    body = re.sub(r"^# .*\n+", "", src, count=1)
    old_link = "[Computing Commons National Research Platform landing page](../README.md)"
    assert old_link in body, "expected relative README link not found in source"
    body = body.replace(old_link, f"[Computing Commons National Research Platform landing page]({README_URL})")
    assert "../README.md" not in body, "relative link fix did not apply"
    return _md_to_html(body)


def main() -> int:
    client = _client()

    html_00 = _build_00_html()
    html_01 = _build_01_html()

    status, page_00 = create_page(
        client,
        COURSE_ID,
        {
            "wiki_page[title]": "00 — Start Here: What Are We About to Do?",
            "wiki_page[body]": html_00,
            "wiki_page[published]": "true",
        },
    )
    print("CREATED page 00:", status, page_00["url"])

    status, page_01 = create_page(
        client,
        COURSE_ID,
        {
            "wiki_page[title]": "01 — Your Laptop Is Not the Whole Computer",
            "wiki_page[body]": html_01,
            "wiki_page[published]": "true",
        },
    )
    print("CREATED page 01:", status, page_01["url"])

    status, module = create_module(
        client,
        COURSE_ID,
        {
            "module[name]": "National Research Platform — Your First Remote Workload",
            "module[published]": "true",
        },
    )
    module_id = module["id"]
    print("CREATED module:", status, module_id, module["name"])

    status, item_00 = create_module_item(
        client,
        COURSE_ID,
        module_id,
        {
            "module_item[title]": "00 — Start Here: What Are We About to Do?",
            "module_item[type]": "Page",
            "module_item[page_url]": page_00["url"],
            "module_item[published]": "true",
            "module_item[position]": "1",
        },
    )
    print("CREATED module item 00:", status, item_00["id"], item_00.get("position"))

    status, item_01 = create_module_item(
        client,
        COURSE_ID,
        module_id,
        {
            "module_item[title]": "01 — Your Laptop Is Not the Whole Computer",
            "module_item[type]": "Page",
            "module_item[page_url]": page_01["url"],
            "module_item[published]": "true",
            "module_item[position]": "2",
        },
    )
    print("CREATED module item 01:", status, item_01["id"], item_01.get("position"))

    receipt = {
        "course_id": COURSE_ID,
        "module_id": module_id,
        "module_name": module["name"],
        "page_00": {"url": page_00["url"], "page_id": page_00["page_id"], "title": page_00["title"]},
        "page_01": {"url": page_01["url"], "page_id": page_01["page_id"], "title": page_01["title"]},
        "module_item_00": {"id": item_00["id"], "position": item_00.get("position")},
        "module_item_01": {"id": item_01["id"], "position": item_01.get("position")},
        "readme_url_used": README_URL,
    }
    RECEIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT_PATH.write_text(json.dumps(receipt, indent=2) + "\n")
    print("RECEIPT written:", RECEIPT_PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
