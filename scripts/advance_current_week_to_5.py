#!/usr/bin/env python3
"""Advance Computing Commons' front page current-week marker from 4 to 5.

Narrow, single-purpose, bounded: this script does exactly three edits to
the front page body (course 24298) and nothing else --

1. Week rail: chip 4 becomes a normal link, chip 5 becomes the current
   marker.
2. "This week" section: heading, summary, and the three day cards are
   replaced with the real, already-published Week 5 Monday/Wednesday/
   Friday pages.
3. "Next week" preview: replaced with the real, already-published Week 6
   material (previously this section held what was, by then, stale
   Week 5 preview content).

All target page slugs were verified live against Canvas before writing
this script (see the evidence file this script appends to). Uses
harbor.api.update_page -- Harbor's own named, reviewed helper for this
exact kind of course-content-time write -- rather than an ad hoc raw PUT.
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path.home() / "git" / "harbor"))
from harbor import api
from harbor.client import CanvasClient
from harbor.config import load_env, read_canvas_config

COURSE_ID = 24298
EVIDENCE = (
    Path.home()
    / "git"
    / "computing_commons"
    / "sidecar"
    / "reports"
    / "advance_current_week_to_5.md"
)

OLD_CHIP4 = '<span class="week-rail-chip week-rail-current" title="Week 4" style="display:inline-block;padding:6px 11px;border:2px solid #172033;border-radius:999px;text-decoration:none;color:#fff;background:#172033;font-size:0.9em;"><strong>4</strong></span>'
NEW_CHIP4 = '<a class="week-rail-chip" href="https://swosu.instructure.com/courses/24298/pages/week-4-shared-rhythm" title="Week 4" style="display:inline-block;padding:6px 11px;border:1px solid #135c9e;border-radius:999px;text-decoration:none;color:#135c9e;background:#edf3f9;font-size:0.9em;" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/24298/pages/week-4-shared-rhythm" data-api-returntype="Page">4</a>'

OLD_CHIP5 = '<a class="week-rail-chip" href="https://swosu.instructure.com/courses/24298/pages/week-5-shared-rhythm" title="Week 5" style="display:inline-block;padding:6px 11px;border:1px solid #135c9e;border-radius:999px;text-decoration:none;color:#135c9e;background:#edf3f9;font-size:0.9em;" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/24298/pages/week-5-shared-rhythm" data-api-returntype="Page">5</a>'
NEW_CHIP5 = '<span class="week-rail-chip week-rail-current" title="Week 5" style="display:inline-block;padding:6px 11px;border:2px solid #172033;border-radius:999px;text-decoration:none;color:#fff;background:#172033;font-size:0.9em;"><strong>5</strong></span>'

OLD_THIS_WEEK_HEADER = '<h2 id="this-week" style="margin:0;color:#172033">This week · Week 4</h2>'
NEW_THIS_WEEK_HEADER = '<h2 id="this-week" style="margin:0;color:#172033">This week · Week 5</h2>'

OLD_SUMMARY = "<p style=\"margin:8px 0 14px;color:#465268\">Three short moves: decompose a task before asking AI to do it, spell out an argument's premises and conclusion, then use an outside baseline to make a better forecast.</p>"
NEW_SUMMARY = "<p style=\"margin:8px 0 14px;color:#465268\">Three short moves: choose the right model for a task instead of defaulting to one, judge a decision by its process rather than its outcome, then watch for regression to the mean before crediting a cause.</p>"

OLD_CARDS = '''      <article style="background:#e6f2fb;border-radius:12px;padding:20px;border-top:5px solid #135c9e"><p style="margin:0;color:#135c9e;font-size:13px">MONDAY · AI FLUENCY</p><h3 style="margin:8px 0 8px;font-size:21px">Decompose the Task</h3><p style="margin:0 0 16px">Split a large project into inspectable stages — input, action, output, quality check — before you ask AI to do any of it.</p><a href="https://swosu.instructure.com/courses/24298/pages/monday-ai-fluency-ai-i-week-4-decompose-the-task" style="display:inline-block;background:#135c9e;color:#fff;border-radius:7px;padding:9px 13px;text-decoration:none;" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/24298/pages/monday-ai-fluency-ai-i-week-4-decompose-the-task" data-api-returntype="Page">Open Monday route →</a></article>
      <article style="background:#e6f2fb;border-radius:12px;padding:20px;border-top:5px solid #135c9e"><p style="margin:0;color:#135c9e;font-size:13px">WEDNESDAY · PROFESSIONAL MINDS</p><h3 style="margin:8px 0 8px;font-size:21px">Mapping arguments for better decisions</h3><p style="margin:0 0 16px">Reconstruct an argument in standard form — premises, conclusion, and the assumptions doing quiet work in between.</p><a href="https://swosu.instructure.com/courses/24298/pages/wednesday-professional-minds-week-4-reading-mapping-arguments-for-better-decisions" style="display:inline-block;background:#135c9e;color:#fff;border-radius:7px;padding:9px 13px;text-decoration:none;" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/24298/pages/wednesday-professional-minds-week-4-reading-mapping-arguments-for-better-decisions" data-api-returntype="Page">Open Wednesday route →</a></article>
      <article style="background:#dff3eb;border-radius:12px;padding:20px;border-top:5px solid #23866c"><p style="margin:0;color:#165c4c;font-size:13px">FRIDAY · PROFESSIONAL MINDS</p><h3 style="margin:8px 0 8px;font-size:21px">Using the outside view for better decisions</h3><p style="margin:0 0 16px">Forecast from a reference class and a real baseline, not just the details of your own plan.</p><a href="https://swosu.instructure.com/courses/24298/pages/friday-professional-minds-week-4-reading-using-the-outside-view-for-better-decisions" style="display:inline-block;background:#23866c;color:#fff;border-radius:7px;padding:9px 13px;text-decoration:none;" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/24298/pages/friday-professional-minds-week-4-reading-using-the-outside-view-for-better-decisions" data-api-returntype="Page">Open Friday route →</a></article>'''
NEW_CARDS = '''      <article style="background:#e6f2fb;border-radius:12px;padding:20px;border-top:5px solid #135c9e"><p style="margin:0;color:#135c9e;font-size:13px">MONDAY · AI FLUENCY</p><h3 style="margin:8px 0 8px;font-size:21px">Select the Right Model</h3><p style="margin:0 0 16px">Match the model to the task instead of reaching for the same default every time.</p><a href="https://swosu.instructure.com/courses/24298/pages/monday-ai-fluency-ai-i-week-5-select-the-right-model" style="display:inline-block;background:#135c9e;color:#fff;border-radius:7px;padding:9px 13px;text-decoration:none;" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/24298/pages/monday-ai-fluency-ai-i-week-5-select-the-right-model" data-api-returntype="Page">Open Monday route →</a></article>
      <article style="background:#e6f2fb;border-radius:12px;padding:20px;border-top:5px solid #135c9e"><p style="margin:0;color:#135c9e;font-size:13px">WEDNESDAY · PROFESSIONAL MINDS</p><h3 style="margin:8px 0 8px;font-size:21px">Never judge a decision by its outcome</h3><p style="margin:0 0 16px">Judge the decision by the quality of the reasoning at the time, not just how it turned out.</p><a href="https://swosu.instructure.com/courses/24298/pages/wednesday-professional-minds-week-5-reading-never-judge-a-decision-by-its-outcome" style="display:inline-block;background:#135c9e;color:#fff;border-radius:7px;padding:9px 13px;text-decoration:none;" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/24298/pages/wednesday-professional-minds-week-5-reading-never-judge-a-decision-by-its-outcome" data-api-returntype="Page">Open Wednesday route →</a></article>
      <article style="background:#dff3eb;border-radius:12px;padding:20px;border-top:5px solid #23866c"><p style="margin:0;color:#165c4c;font-size:13px">FRIDAY · PROFESSIONAL MINDS</p><h3 style="margin:8px 0 8px;font-size:21px">The Triumph of Mediocrity: Regression to the Mean</h3><p style="margin:0 0 16px">An extreme result tends to be followed by a more ordinary one — even with no real cause behind the "correction."</p><a href="https://swosu.instructure.com/courses/24298/pages/friday-professional-minds-week-5-reading-the-triumph-of-mediocrity-regression-to-the-mean" style="display:inline-block;background:#23866c;color:#fff;border-radius:7px;padding:9px 13px;text-decoration:none;" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/24298/pages/friday-professional-minds-week-5-reading-the-triumph-of-mediocrity-regression-to-the-mean" data-api-returntype="Page">Open Friday route →</a></article>'''

OLD_NEXT_BLOCK = '''  <section aria-labelledby="next-week" style="background:#fff4df;border-left:6px solid #9a5b00;border-radius:10px;padding:18px 20px;margin-bottom:22px">
    <h2 id="next-week" style="margin:0 0 6px">Next week · Week 5 preview</h2><p style="margin:0 0 12px">Select the right model for the task, then use two decision-quality readings — judging decisions by process rather than outcome, and the regression-to-the-mean trap. These Week 5 Commons pages are optional, self-paced enrichment — not required by any home course.</p>
    <div style="display:flex;gap:10px;flex-wrap:wrap"><a href="https://swosu.instructure.com/courses/24298/pages/monday-ai-fluency-ai-i-week-5-select-the-right-model" style="color:#704400;" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/24298/pages/monday-ai-fluency-ai-i-week-5-select-the-right-model" data-api-returntype="Page">Monday · Select the Right Model</a><a href="https://swosu.instructure.com/courses/24298/pages/wednesday-professional-minds-week-5-reading-never-judge-a-decision-by-its-outcome" style="color:#704400;" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/24298/pages/wednesday-professional-minds-week-5-reading-never-judge-a-decision-by-its-outcome" data-api-returntype="Page">Wednesday · Never Judge a Decision by Its Outcome</a><a href="https://swosu.instructure.com/courses/24298/pages/friday-professional-minds-week-5-reading-the-triumph-of-mediocrity-regression-to-the-mean" style="color:#704400;" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/24298/pages/friday-professional-minds-week-5-reading-the-triumph-of-mediocrity-regression-to-the-mean" data-api-returntype="Page">Friday · The Triumph of Mediocrity: Regression to the Mean</a></div>
  </section>'''
NEW_NEXT_BLOCK = '''  <section aria-labelledby="next-week" style="background:#fff4df;border-left:6px solid #9a5b00;border-radius:10px;padding:18px 20px;margin-bottom:22px">
    <h2 id="next-week" style="margin:0 0 6px">Next week · Week 6 preview</h2><p style="margin:0 0 12px">Engineer a better prompt, then use two more reasoning-quality readings — the base rate fallacy and what it actually takes for a result to replicate. These Week 6 Commons pages are optional, self-paced enrichment — not required by any home course.</p>
    <div style="display:flex;gap:10px;flex-wrap:wrap"><a href="https://swosu.instructure.com/courses/24298/pages/monday-ai-fluency-ai-i-week-6-engineer-the-prompt" style="color:#704400;" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/24298/pages/monday-ai-fluency-ai-i-week-6-engineer-the-prompt" data-api-returntype="Page">Monday · Engineer the Prompt</a><a href="https://swosu.instructure.com/courses/24298/pages/wednesday-professional-minds-week-6-reading-the-base-rate-fallacy" style="color:#704400;" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/24298/pages/wednesday-professional-minds-week-6-reading-the-base-rate-fallacy" data-api-returntype="Page">Wednesday · The Base Rate Fallacy</a><a href="https://swosu.instructure.com/courses/24298/pages/friday-professional-minds-week-6-reading-understanding-replication" style="color:#704400;" data-api-endpoint="https://swosu.instructure.com/api/v1/courses/24298/pages/friday-professional-minds-week-6-reading-understanding-replication" data-api-returntype="Page">Friday · Understanding Replication</a></div>
  </section>'''

SUBSTITUTIONS = [
    ("week rail chip 4", OLD_CHIP4, NEW_CHIP4),
    ("week rail chip 5", OLD_CHIP5, NEW_CHIP5),
    ("this-week header", OLD_THIS_WEEK_HEADER, NEW_THIS_WEEK_HEADER),
    ("this-week summary", OLD_SUMMARY, NEW_SUMMARY),
    ("this-week cards", OLD_CARDS, NEW_CARDS),
    ("next-week block", OLD_NEXT_BLOCK, NEW_NEXT_BLOCK),
]


def die(msg):
    print("STOP:", msg)
    sys.exit(2)


def main():
    load_env()
    client = CanvasClient(read_canvas_config(enforce_course_allowlist=True))
    ev = ["", "## Advance Computing Commons current week 4 -> 5 — %s UTC" % time.strftime("%Y-%m-%dT%H:%M:%S")]

    if not client.config.api_base_url.startswith("https://swosu.instructure.com"):
        die("base_url not SWOSU")
    course = client.get(f"/api/v1/courses/{COURSE_ID}").json()
    if course.get("id") != COURSE_ID or "Computing Commons" not in (course.get("name") or ""):
        die("course identity mismatch: %r" % course.get("name"))
    ev.append("- course: %s / %s" % (course["id"], course["name"]))

    fp_before = client.get(f"/api/v1/courses/{COURSE_ID}/front_page").json()
    body = fp_before.get("body") or ""
    page_url = fp_before["url"]

    if "week-rail-current\" title=\"Week 5\"" in body or 'week-rail-current" title="Week 5"' in body:
        die("front page already shows Week 5 as current -- nothing to do (idempotent guard)")

    for label, old, new in SUBSTITUTIONS:
        if old not in body:
            die("expected content for %r not found -- front page changed since this script was written" % label)
        body = body.replace(old, new)
        ev.append("- applied: %s" % label)

    status, updated = api.update_page(client, COURSE_ID, page_url, {"wiki_page[body]": body})
    ev.append("- update_page status %s" % status)

    fp_after = client.get(f"/api/v1/courses/{COURSE_ID}/front_page").json()
    live_body = fp_after.get("body") or ""
    if live_body != body:
        die("readback mismatch: live front page body does not match what was sent")
    if 'title="Week 5"' not in live_body or "week-rail-current" not in live_body.split('title="Week 5"')[0][-200:]:
        die("readback: Week 5 current marker not confirmed in live body")
    ev.append("- readback OK: live front page body matches exactly what was sent")
    ev.append("- readback OK: Week 5 confirmed as the current-week marker")

    EVIDENCE.parent.mkdir(parents=True, exist_ok=True)
    with EVIDENCE.open("a", encoding="utf-8") as f:
        f.write("\n".join(ev) + "\n")
    print("\n".join(ev))
    print("\nDONE. Evidence appended to %s" % EVIDENCE)


if __name__ == "__main__":
    main()
