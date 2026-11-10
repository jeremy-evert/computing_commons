#!/usr/bin/env python3
"""Upload a handout PDF to Computing Commons (course 24298) and add ONE link
to the front page's current-week section.

Dry-run by default (prints the body diff, writes nothing, uploads nothing).
Pass --apply to write. Target-locked (course id AND name verified), takes a
before-backup of the front page body, idempotent (marker + existing-file
reuse), and reads back page + file URL.

Usage: add_handout_to_front_page.py [--handout=ai-decision-lab|field-guide] [--apply]
"""
import difflib, hashlib, sys, time
from pathlib import Path

sys.path.insert(0, str(Path.home() / "git" / "harbor"))
from harbor import api
from harbor.client import CanvasClient
from harbor.config import load_env, read_canvas_config

COURSE_ID, COURSE_NAME = 24298, "Computing Commons"
REPO = Path(__file__).resolve().parent.parent
FOLDER = "handouts"
# key -> (pdf, link text, context line, key of the handout this one goes under or None)
HANDOUTS = {
    "ai-decision-lab": ("AI_Decision_Lab_Student_Handout.pdf",
        "AI Decision Lab (handout, 4 pages)",
        "In-class handout: use AI as a sparring partner to choose between inheritance and composition for a room-reservation program.", None),
    "field-guide": ("Deciding_with_AI_Student_Field_Guide_v1.0.2.pdf",
        "Deciding with AI: Student Field Guide (v1.0.2, 8 pages)",
        "A guide to using an AI assistant as a sparring partner on a real decision, with prompts to copy and a decision worksheet.", "ai-decision-lab"),
    # v1.0.3 REPLACES the v1.0.2 paragraph in place (old file stays in Canvas Files)
    "field-guide-v103": ("Deciding_with_AI_Student_Field_Guide_v1.0.3.pdf",
        "Deciding with AI: Student Field Guide (v1.0.3, 4 pages)",
        "A guide to using an AI assistant as a sparring partner on a real decision, with rules of thumb, prompts to copy, and practice problems.", "field-guide"),
}
REPLACES = {"field-guide-v103": "field-guide"}
KEY = "ai-decision-lab"
for a in sys.argv[1:]:
    if a.startswith("--handout="):
        KEY = a.split("=", 1)[1]
if KEY not in HANDOUTS:
    sys.exit(f"unknown handout {KEY}")
_pdf, LINK_TEXT, CONTEXT, AFTER = HANDOUTS[KEY]
PDF = REPO / "handouts" / _pdf
MARKER = f'data-handout="{KEY}"'
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
    if KEY in REPLACES:
        old = REPLACES[KEY]
        a = body.find(f'data-handout="{old}"', i, j)
        if a < 0:
            die(f"paragraph to replace ({old}) not on page")
        ps = body.rfind("\n    <p ", 0, a)
        k = body.find("</p>", a) + len("</p>")
        body_new_cut = (ps, k)
    elif AFTER:
        # insert directly after the preceding handout's paragraph
        a = body.find(f'data-handout="{AFTER}"', i, j)
        if a < 0:
            die(f"preceding handout {AFTER} not on page")
        k = body.find("</p>", a) + len("</p>")
    else:
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
    if KEY in REPLACES:
        new = body[:body_new_cut[0]] + block(file_url) + body[body_new_cut[1]:]
    else:
        new = body[:k] + block(file_url) + body[k:]
    diff = "".join(difflib.unified_diff(body.splitlines(True), new.splitlines(True), "front_page.before", "front_page.after", n=1))
    print(diff or "(no diff)")
    if not apply:
        print("DRY RUN: nothing written to Canvas. (file would be uploaded to Files/handouts)"); return

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    bp = BACKUP_DIR / f"computing-commons-home_before_{KEY}_{time.strftime('%Y%m%dT%H%M%S')}.html"
    bp.write_text(body, encoding="utf-8"); print("backup:", bp)
    st, _ = api.update_page(c, COURSE_ID, slug, {"wiki_page[body]": new})
    print("update_page", st)
    live = c.get(f"/api/v1/courses/{COURSE_ID}/front_page").json()["body"]
    if MARKER not in live or f"/files/{f['id']}" not in live:  # Canvas rewrites the href (adds verifier)
        die("readback: link not found on live page")
    # remove the new block from live and compare to the backup: nothing else changed
    import re
    if KEY in REPLACES:
        ok = (f'data-handout="{REPLACES[KEY]}"' not in live and 'data-handout="ai-decision-lab"' in live
              and live.count("data-handout=") == body.count("data-handout="))
        print("old paragraph gone, AI Decision Lab intact, same paragraph count:", ok)
        if not ok: die("readback mismatch")
        stripped = body
    else:
      stripped = re.sub(r'\n    <p ' + re.escape(MARKER) + r'.*?</p>', "", live, count=1, flags=re.S)
    print("rest of page unchanged vs backup:", stripped == body)
    meta = c.get(f"/api/v1/files/{f['id']}").json()
    print("file readback:", meta.get("display_name"), meta.get("size"), "locked=", meta.get("locked"), "hidden=", meta.get("hidden"))
    print("sha256 local:", hashlib.sha256(PDF.read_bytes()).hexdigest())
    print("readback OK")


if __name__ == "__main__":
    main()
