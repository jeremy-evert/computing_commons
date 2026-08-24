#!/usr/bin/env python3
"""Local, repo-backed teacher feedback sink. Canvas is never written."""
from __future__ import annotations
import argparse, datetime as dt, json, re, subprocess, uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ORIGIN = "http://localhost:3002"
COURSE = 18
SCHEMA = "computing-commons.teacher-feedback.v1"

def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")

def locked(url: str) -> bool:
    return bool(re.match(r"^http://localhost:3002/courses/18(?:/|$)", url or ""))

def safe_text(value: object, limit: int) -> str:
    return str(value or "").strip()[:limit]

def md_text(value: str) -> str:
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("`", "&#96;")

class Handler(BaseHTTPRequestHandler):
    sink: Path
    source_root: Path
    def log_message(self, *_args): pass
    def response_headers(self, status=200):
        self.send_response(status); self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", ORIGIN); self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type"); self.end_headers()
    def do_OPTIONS(self): self.response_headers(204)
    def do_GET(self):
        self.response_headers(); self.wfile.write(b'{"ok":true,"service":"teacher-feedback","schema":"computing-commons.teacher-feedback.v1"}')
    def do_POST(self):
        if self.path != "/submit": self.response_headers(404); self.wfile.write(b'{"error":"not found"}'); return
        try:
            raw = self.rfile.read(int(self.headers.get("Content-Length", "0")))
            data = json.loads(raw.decode("utf-8"))
            url = safe_text(data.get("url"), 1000)
            if not locked(url): raise ValueError("exact Savnac course-18 lock failed")
            disposition = safe_text(data.get("disposition"), 20)
            if disposition not in {"KEEP", "CHANGE", "CONFUSING", "BROKEN", "IDEA"}: raise ValueError("invalid disposition")
            feedback = safe_text(data.get("feedback"), 12000)
            if not feedback: raise ValueError("feedback is required")
            sid = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:10]
            stamp = utc_now(); commit = subprocess.check_output(["git", "-C", str(self.source_root), "rev-parse", "HEAD"], text=True).strip()
            receipt = {"schema": SCHEMA, "submission_id": sid, "submitted_at": stamp, "source_commit": commit,
                "lock": {"expected_origin": ORIGIN, "course_id": COURSE, "allowed_path_prefix": "/courses/18", "rendered_url": url, "validated": True},
                "page": {"title": safe_text(data.get("title"), 500), "url": url}, "disposition": disposition,
                "feedback": feedback, "expected_outcome": safe_text(data.get("expected_outcome"), 12000)}
            self.sink.mkdir(parents=True, exist_ok=True)
            (self.sink / f"{sid}.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
            md = f"# Teacher Submission {sid}\n\n- Disposition: `{disposition}`\n- Submitted: `{stamp}`\n- Page: `{md_text(receipt['page']['title'])}`\n- URL: `{md_text(url)}`\n- Source commit: `{commit}`\n- Lock: PASS (`{ORIGIN}`, course 18, `/courses/18`)\n\n## What I want / do not want\n\n{md_text(feedback)}\n\n## What I expected instead\n\n{md_text(receipt['expected_outcome'] or 'Not provided.')}\n"
            (self.sink / f"{sid}.md").write_text(md, encoding="utf-8")
            with (self.sink / "index.jsonl").open("a", encoding="utf-8") as out: out.write(json.dumps(receipt, separators=(",", ":")) + "\n")
            self.response_headers(); self.wfile.write(json.dumps({"ok": True, "submission_id": sid}).encode())
        except Exception as exc:
            self.response_headers(400); self.wfile.write(json.dumps({"ok": False, "error": str(exc)}).encode())

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--sink", type=Path, required=True); ap.add_argument("--source-root", type=Path, required=True); ap.add_argument("--port", type=int, default=8765)
    args = ap.parse_args(); Handler.sink = args.sink; Handler.source_root = args.source_root
    ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever(); return 0
if __name__ == "__main__": raise SystemExit(main())
