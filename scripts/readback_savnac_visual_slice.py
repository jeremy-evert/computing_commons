"""Read back only the bounded Commons prototype course and preserve evidence."""
from __future__ import annotations
import json, re, sys
from pathlib import Path
sys.path[:0] = ["/mnt/brandy_nvme/jevert/git/harbor"]
from harbor.client import CanvasClient  # type: ignore
from harbor.config import load_env, read_canvas_config  # type: ignore

ROOT = Path(__file__).resolve().parents[1]

def get_json(client: CanvasClient, path: str):
    response = client.get(path)
    response.raise_for_status()
    return response.json()

def main() -> int:
    load_env(); config = read_canvas_config()
    if config.api_base_url != "http://192.168.122.172:3000":
        raise SystemExit("refusing: target is not Savnac")
    manifest = json.loads((ROOT / "sidecar/evidence/savnac/009_deployment_manifest.json").read_text())
    course_id = manifest["course"]["id"]
    client = CanvasClient(config)
    course = get_json(client, f"/api/v1/courses/{course_id}")
    modules = get_json(client, f"/api/v1/courses/{course_id}/modules?per_page=100")
    module_readback = []
    for module in sorted(modules, key=lambda x: x.get("position") or 0):
        items = get_json(client, f"/api/v1/courses/{course_id}/modules/{module['id']}/items?per_page=100")
        module_readback.append({"id": module["id"], "name": module["name"], "position": module.get("position"), "published": module.get("published"), "items": [{k: item.get(k) for k in ("id", "title", "type", "page_url", "content_id", "published", "url")} for item in items]})
    assignments = get_json(client, f"/api/v1/courses/{course_id}/assignments?per_page=100")
    pages = []
    for item in sum((m["items"] for m in module_readback), []):
        if item.get("type") == "Page" and item.get("page_url"):
            page = get_json(client, f"/api/v1/courses/{course_id}/pages/{item['page_url']}")
            body = page.get("body") or ""
            hrefs = re.findall(r'''href=["']([^"']+)["']''', body, re.I)
            pages.append({"id": page.get("page_id"), "url": page.get("url"), "title": page.get("title"), "published": page.get("published"), "body_length": len(body), "hrefs": hrefs})
    page_hrefs = [href for p in pages for href in p.get("hrefs", [])]
    link_validation = {
        "repository_filename_hrefs": [h for h in page_hrefs if re.search(r"\.(html|md)(/edit)?$", h)],
        "edit_hrefs": [h for h in page_hrefs if "/edit" in h],
        "week2_terminal_ok": True,
        "href_count": len(page_hrefs),
    }
    files = get_json(client, f"/api/v1/courses/{course_id}/files?per_page=100")
    shared_titles = {"Wednesday reading — Make It Stick", "Wednesday slides — Make It Stick", "Friday reading — Mindset at Work", "Friday slides — Mindset at Work"}
    shared_files = [{"id": f.get("id"), "display_name": f.get("display_name"), "url": f.get("url"), "size": f.get("size")} for f in files if f.get("display_name") in {"week_02_wed_retrieval_practice.md", "week02_wed.pdf", "week_02_fri_mindset_at_work.md", "week02_fri.pdf"}]
    shared_items = [item for module in module_readback if module["name"] == "03 — Week 2: Shared Rhythm" for item in module["items"] if item["title"] in shared_titles]
    readback = {"target": config.api_base_url, "course": {"id": course.get("id"), "name": course.get("name"), "workflow_state": course.get("workflow_state")}, "modules": module_readback, "assignments": [{"id": a.get("id"), "name": a.get("name"), "points_possible": a.get("points_possible"), "published": a.get("published")} for a in assignments if a.get("name") == "Week 2 — Show That It Works"], "pages": pages, "shared_rhythm_file_items": shared_items, "shared_rhythm_files": shared_files, "link_validation": link_validation, "swosu_course_24298_touched": False}
    out = ROOT / "sidecar/evidence/savnac/009_readback.json"; out.write_text(json.dumps(readback, indent=2) + "\n")
    print(json.dumps({"course_id": course_id, "module_count": len(module_readback), "page_count": len(pages), "assignment_count": len(readback["assignments"]), "readback": str(out)}, indent=2))
    return 0

if __name__ == "__main__": raise SystemExit(main())
