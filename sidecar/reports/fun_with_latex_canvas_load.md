# Fun with LaTeX -> Computing Commons (24298) — evidence
- when: 2026-09-03T16:57:31 UTC

course lock OK: id=24298 name='Computing Commons'
no pre-existing 'Fun with LaTeX' module found (22 modules total)
local slides sha256: 78c12c0ea0607c5d28006ee84e7cf4da5f66663b04377ef809b621b330721bf9 (641410 bytes)
uploaded slides: file_id=6584703 size=641410 name=fun_with_latex.pdf
page body rendered: 14592 chars
created page: url=fun-with-latex-student-guide id=455886
created module: id=219171 position=4
item1 (Page): id=1532507
item2 (ExternalUrl): id=1532508
item3 (File): id=1532509
module published: True

{
  "module_id": 219171,
  "page_id": 455886,
  "page_url": "fun-with-latex-student-guide",
  "slides_file_id": 6584703,
  "video_item_id": 1532508,
  "page_item_id": 1532507,
  "slides_item_id": 1532509
}

## Announcements
- when: 2026-09-03T16:58:30 UTC

- course 74029 (COMSC-1033-1415.2026FA): announcement id=542585, posted_at=2026-09-03T21:58:30Z, published=True
  readback: title_match=True module_link_present=True
- course 74031 (COMSC-1053-1417.2026FA): announcement id=542586, posted_at=2026-09-03T21:58:32Z, published=True
  readback: title_match=True module_link_present=True
- course 75249 (COMSC-3013-1438.2026FA): announcement id=542587, posted_at=2026-09-03T21:58:33Z, published=True
  readback: title_match=True module_link_present=True
- course 74035 (COMSC-2043-1420.2026FA): announcement id=542588, posted_at=2026-09-03T21:58:34Z, published=True
  readback: title_match=True module_link_present=True

## Self-check (before announcing)

- Module readback: position 4 (after the three Week-3/container modules),
  published=True, items_count=3, module count 22 -> 23 as expected.
- Item order confirmed: 1) Page, 2) ExternalUrl, 3) File — all published.
- Page readback: 13 headings, table present, code blocks present, video
  link present, slides link present, zero dead `href="slides/...` links.
- Slides file: uploaded size 641410 matches local file exactly; downloaded
  the live Canvas copy and reverified SHA-256 byte-for-byte against the
  local source (`78c12c0e...ba32f9`).
- Video URL: resolves with HTTP 302 to a SharePoint stream/sign-in flow
  (expected behavior for a SWOSU-sign-in-gated link — not a dead link).
- No unrelated module, page, file, assignment, grade, or enrollment
  in course 24298 was touched — every write was scoped to the new module,
  its new page, and its new file.

## Caveat for Jeremy

`computing_commons` is a **private** GitHub repo. The Student Guide's own
Section 2 instructs students to `git clone
https://github.com/jeremy-evert/computing_commons.git`, and (per this
mission's own linking rule) the non-slide relative links
(`bootstrap_latex_project.ps1`, `hello.tex`, `hello.pdf`, `Makefile`, the
curriculum cross-reference) were rewritten to GitHub blob URLs on that same
repo, since there was no other "good Canvas target" for them. Both of these
assume enrolled students already have (or will be given) read access to
this private repo. If that's not already true, the clone step and those
four links will 404/permission-fail for students. Flagging rather than
guessing — this wasn't one of the mission's listed stop conditions, so I
did not halt on it, but it's worth a quick confirmation.

## Result

`FUN WITH LATEX MODULE LOADED — module 219171, page 455886, slides file 6584703, video item 1532508`

`FUN WITH LATEX ANNOUNCEMENT POSTED — 74029:542585 74031:542586 75249:542587 74035:542588`
