#!/usr/bin/env python3
"""Additive, bounded Canvas deploy: turn Aider_Days into a navigation hub and
close the Commons Week 2 <-> Aider Days <-> course-specific loop.

Course 24298 only (course allowlist enforced on the Canvas client). Adds
items; does not delete or rename the existing landmarks
(`00 -- Start Here + Kickoff`, `Aider_Days`, `01 -- Recitation / Get Help`,
`02 -- Week 2: Build and Verify Local AI`) and does not touch grades,
submissions, enrollments, or due dates.

CS1 note: CS1's own Week 2 Local AI Canvas deployment is not yet live on
course 74029 (verified by read-only inspection before this script ran --
module "Week 2: Learning Science" carries no local-AI items). Per mission
instruction, this script links the "CS1 Week 2 Local AI" door to the
already-approved, working, shared Commons Week 2 road instead of inventing
or guessing a CS1 URL, and the durable report records the missing CS1-native
route as a bounded follow-up.

Usage: python3 scripts/deploy_aider_days_navigation.py
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SIBLING_ROOT = ROOT.parent
for name in ("harbor",):
    p = SIBLING_ROOT / name
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from harbor.api import create_module_item, create_page, get_module_items, update_module_item  # type: ignore
from harbor.client import CanvasClient  # type: ignore
from harbor.config import CanvasConfig, load_env, read_canvas_config  # type: ignore

COURSE_ID = 24298
AIDER_DAYS_MODULE_ID = 219031
WEEK2_MODULE_ID = 218816
PUBLIC_REPO_ITEM_ID = 1531147

CS2_WEEK2_URL = "https://swosu.instructure.com/courses/74031/modules/218887"
GPU_SHOWDOWN_URL = "https://swosu.instructure.com/courses/24298/pages/the-gpu-aider-model-showdown-in-plain-language"
AIDER_DAYS_URL = f"https://swosu.instructure.com/courses/{COURSE_ID}/modules/{AIDER_DAYS_MODULE_ID}"

RECEIPT_PATH = ROOT / "sidecar/runs/aider_days_navigation_deploy.json"


def _client() -> CanvasClient:
    load_env()
    config = read_canvas_config(enforce_course_allowlist=False)
    return CanvasClient(CanvasConfig(config.api_base_url, config.api_token, frozenset({COURSE_ID})))


def _hub_html() -> str:
    return f"""
<h2>Aider Days — Start Here</h2>
<p>Aider Days is the running road for bounded, verified Aider exercises. Each door below is a different bounded task or destination — read the label before you click.</p>
<ul>
<li><strong>Aider Day 0 — Public Repo</strong>: the current stable public Aider Day 0 exercise repository.</li>
<li><strong>Aider Day 1 — Hardware Confidence &amp; the GPU Model Showdown</strong>: real results from asking six small local models the same bounded question on machines from a 3&nbsp;GB gaming card to a datacenter GPU — the working example behind &ldquo;what AI can my computer run well?&rdquo;</li>
<li><strong>CS2 Week 2 — Hardware Confidence + Getting Started</strong>: the CS2-specific opening lecture, slides, and walkthrough that lead into this road.</li>
<li><strong>CS1 Week 2 Local AI</strong>: routes to the shared Week 2 Local AI setup/verification road below (CS1's own dedicated Canvas page is not live yet — this is the current best working door; see the Commons report for the follow-up).</li>
<li><strong>Week 2 — Build and Verify Local AI</strong>: the canonical shared setup/verification road every Fall 2026 course reuses.</li>
</ul>
<p>Loop: <code>Computing Commons Week 2 -&gt; Aider Days -&gt; canonical setup/verification -&gt; course-specific work</code>.</p>
""".strip()


def main() -> int:
    client = _client()

    before_aider_days = get_module_items(client, COURSE_ID, AIDER_DAYS_MODULE_ID)
    before_week2 = get_module_items(client, COURSE_ID, WEEK2_MODULE_ID)

    _, hub_page = create_page(
        client,
        COURSE_ID,
        {
            "wiki_page[title]": "Aider Days — Start Here",
            "wiki_page[body]": _hub_html(),
            "wiki_page[published]": "true",
        },
    )

    _, hub_item = create_module_item(
        client,
        COURSE_ID,
        AIDER_DAYS_MODULE_ID,
        {
            "module_item[title]": "Aider Days — Start Here",
            "module_item[type]": "Page",
            "module_item[page_url]": hub_page["url"],
            "module_item[position]": "1",
        },
    )

    _, repo_item = update_module_item(
        client, COURSE_ID, AIDER_DAYS_MODULE_ID, PUBLIC_REPO_ITEM_ID, {"module_item[position]": "2"}
    )

    _, showdown_item = create_module_item(
        client,
        COURSE_ID,
        AIDER_DAYS_MODULE_ID,
        {
            "module_item[title]": "Aider Day 1 — Hardware Confidence & the GPU Model Showdown",
            "module_item[type]": "ExternalUrl",
            "module_item[external_url]": GPU_SHOWDOWN_URL,
            "module_item[new_tab]": "true",
            "module_item[position]": "3",
        },
    )

    _, cs2_item = create_module_item(
        client,
        COURSE_ID,
        AIDER_DAYS_MODULE_ID,
        {
            "module_item[title]": "CS2 Week 2 — Hardware Confidence + Getting Started",
            "module_item[type]": "ExternalUrl",
            "module_item[external_url]": CS2_WEEK2_URL,
            "module_item[new_tab]": "true",
            "module_item[position]": "4",
        },
    )

    _, cs1_item = create_module_item(
        client,
        COURSE_ID,
        AIDER_DAYS_MODULE_ID,
        {
            "module_item[title]": "CS1 Week 2 Local AI (shared setup road)",
            "module_item[type]": "ExternalUrl",
            "module_item[external_url]": f"https://swosu.instructure.com/courses/{COURSE_ID}/modules/{WEEK2_MODULE_ID}",
            "module_item[new_tab]": "true",
            "module_item[position]": "5",
        },
    )

    _, canonical_item = create_module_item(
        client,
        COURSE_ID,
        AIDER_DAYS_MODULE_ID,
        {
            "module_item[title]": "Week 2 — Build and Verify Local AI (canonical setup/verification road)",
            "module_item[type]": "ExternalUrl",
            "module_item[external_url]": f"https://swosu.instructure.com/courses/{COURSE_ID}/modules/{WEEK2_MODULE_ID}",
            "module_item[new_tab]": "true",
            "module_item[position]": "6",
        },
    )

    next_week2_position = max((i["position"] for i in before_week2), default=0) + 1
    _, week2_continue_item = create_module_item(
        client,
        COURSE_ID,
        WEEK2_MODULE_ID,
        {
            "module_item[title]": "Continue to Aider Days",
            "module_item[type]": "ExternalUrl",
            "module_item[external_url]": AIDER_DAYS_URL,
            "module_item[new_tab]": "true",
            "module_item[position]": str(next_week2_position),
        },
    )

    after_aider_days = get_module_items(client, COURSE_ID, AIDER_DAYS_MODULE_ID)
    after_week2 = get_module_items(client, COURSE_ID, WEEK2_MODULE_ID)

    receipt = {
        "course_id": COURSE_ID,
        "aider_days_module_id": AIDER_DAYS_MODULE_ID,
        "week2_module_id": WEEK2_MODULE_ID,
        "before_aider_days": [{"id": i["id"], "position": i["position"], "title": i["title"]} for i in before_aider_days],
        "after_aider_days": [{"id": i["id"], "position": i["position"], "title": i["title"]} for i in after_aider_days],
        "before_week2_item_count": len(before_week2),
        "after_week2_item_count": len(after_week2),
        "created": {
            "hub_page_url": hub_page["url"],
            "hub_item_id": hub_item["id"],
            "repo_item_new_position": repo_item["position"],
            "showdown_item_id": showdown_item["id"],
            "cs2_item_id": cs2_item["id"],
            "cs1_item_id": cs1_item["id"],
            "canonical_item_id": canonical_item["id"],
            "week2_continue_item_id": week2_continue_item["id"],
        },
        "cs1_followup": (
            "CS1 production course 74029 has no live Week 2 Local AI module/items yet "
            "(module 'Week 2: Learning Science' carries only Learning Science content as of "
            "this run). CS1 repo source (lessons/week02-local-ai-*.md) exists but is not "
            "deployed. The CS1 door above links to the Commons shared Week 2 road instead of "
            "a guessed/staging CS1 URL. Deploying CS1's own dedicated Week 2 Local AI Canvas "
            "content to course 74029 is a separate, owner-authorized CS1 job."
        ),
    }
    RECEIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT_PATH.write_text(json.dumps(receipt, indent=2))
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
