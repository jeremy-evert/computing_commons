#!/usr/bin/env python3
"""Upload a handout PDF to Computing Commons (course 24298) and add ONE link
to the front page's current-week section.

Dry-run by default (prints the body diff, writes nothing, uploads nothing).
Pass --apply to write. Target-locked (course id AND name verified), takes a
before-backup of the front page body, idempotent (marker + existing-file
reuse), and reads back page + file URL.

Usage: add_handout_to_front_page.py [--apply]
"""
import difflib, hashlib, sys, time
from pathlib import Path

sys.path.insert(0, str(Path.home() / "git" / "harbor"))
from harbor import api
from harbor.client import CanvasClient
from harbor.config import load_env, read_canvas_config

COURSE_ID, COURSE_NAME = 24298, "Computing Commons"
REPO = Path(__file__).resolve().parent.parent
PDF = REPO / "handouts" / "AI_Decision_Lab_Student_Handout.pdf"
FOLDER = "handouts"
MARKER = 'data-handout="ai-decision-lab"'
LINK_TEXT = "AI Decision Lab (handout, 4 pages)"
CONTEXT = "In-class handout: use AI as a sparring partner to choose between inheritance and composition for a room-reservation program."
BACKUP_DIR = REPO / "sidecar" / "runs" / "front_page_backups"


def die(m):
    print("STOP:", m); sys.exit(2)


def block(file_url):
    return (f'\n    <p {MARKER} style="margin:14px 0 0;padding:12px 16px;background:#f3f6fa;border-radius:8px">'
            f'<a href="{file_url}" style="font-weight:bold">{LINK_TEXT}</a> — {CONTEXT}</p>')


def main():
    apply = "--apply" in sys.argv
    load_env()
    c = CanvasClient(read_canvas_config(enforce_course_allowlist=True))
    course = c.get(f"/api/v1/courses/{COURSE_ID}").json()
    if course.get("id") != COURSE_ID or course.get("name") != COURSE_NAME:
        die(f"course mismatch: {course.get('id')} {course.get('name')!r}")
    fp = c.get(f"/api/v1/courses/{COURSE_ID}/front_page").json()
    body, slug = fp["body"], fp["url"]
    if MARKER in body:
        die("handout link already on front page (idempotent no-op)")
    i = body.find('id="this-week"')
    if i < 0:
        die("this-week section not found")
    j = body.find("</section>", i)
    # insert after the day-cards grid: the last </div> before </section>
    k = body.rfind("</div>", i, j)
    if k < 0:
        die("cards grid end not found")
    k += len("</div>")

    size = PDF.stat().st_size
    existing = [f for f in api.list_course_files(c, COURSE_ID, search_term=PDF.name)
                if f.get("display_name") == PDF.name and f.get("size") == size]
    if existing:
        f = existing[0]; print("reusing existing Canvas file", f["id"])
    elif apply:
        f = api.upload_course_file(c, COURSE_ID, PDF, folder_path=FOLDER, on_duplicate="rename")
        print("uploaded Canvas file", f["id"], f.get("display_name"))
    else:
        f = None
    # student-facing URL: course-scoped file link (no download token)
    file_url = (f"https://swosu.instructure.com/courses/{COURSE_ID}/files/{f['id']}?wrap=1"
                if f else f"https://swosu.instructure.com/courses/{COURSE_ID}/files/<NEW_FILE_ID>?wrap=1")
    new = body[:k] + block(file_url) + body[k:]
    diff = "".join(difflib.unified_diff(body.splitlines(True), new.splitlines(True), "front_page.before", "front_page.after", n=1))
    print(diff or "(no diff)")
    if not apply:
        print("DRY RUN: nothing written to Canvas. (file would be uploaded to Files/handouts)"); return

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    bp = BACKUP_DIR / f"computing-commons-home_before_{time.strftime('%Y%m%dT%H%M%S')}.html"
    bp.write_text(body, encoding="utf-8"); print("backup:", bp)
    st, _ = api.update_page(c, COURSE_ID, slug, {"wiki_page[body]": new})
    print("update_page", st)
    live = c.get(f"/api/v1/courses/{COURSE_ID}/front_page").json()["body"]
    if MARKER not in live or f"/files/{f['id']}" not in live:  # Canvas rewrites the href (adds verifier)
        die("readback: link not found on live page")
    # remove the new block from live and compare to the backup: nothing else changed
    import re
    stripped = re.sub(r'\n    <p data-handout="ai-decision-lab".*?</p>', "", live, count=1, flags=re.S)
    print("rest of page unchanged vs backup:", stripped == body)
    meta = c.get(f"/api/v1/files/{f['id']}").json()
    print("file readback:", meta.get("display_name"), meta.get("size"), "locked=", meta.get("locked"), "hidden=", meta.get("hidden"))
    print("sha256 local:", hashlib.sha256(PDF.read_bytes()).hexdigest())
    print("readback OK")


if __name__ == "__main__":
    main()
