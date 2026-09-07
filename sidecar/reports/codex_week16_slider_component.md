# Week 1–16 slider component

Built `templates/week-slider/` as a self-contained, dependency-free component:

- `week-slider.html` is a direct-open demo with embedded example data.
- `week-slider.js` renders 16 entries, supports buttons and a range input,
  updates the content pane without reload, exposes `getNow` injection, and
  schedules local Friday 00:00 rollover.
- `week-slider.css` follows the Computing Commons ink/paper/blue/teal/amber
  visual grammar and includes visible focus states.
- `week-data.example.json` defines the 16-entry course data shape.
- `week-slider.test.js` covers before Week 1, Wednesday mid-semester, the
  exact Friday rollover, and after Week 16.

Exact test command:

```sh
TZ=America/Chicago node week-slider.test.js
```

Actual output:

```text
week-slider tests: 4 passed
```

Assumption: `week1_start_date` uses the Monday convention. Week 1 begins on
that local Monday; the first Friday at local 00:00 advances to Week 2, and
each subsequent Friday advances one week. Dates before the supplied Monday
clamp to Week 1, and dates after Week 16 clamp to Week 16. The standalone demo
embeds the example data because browsers block local JSON fetches from a
`file:` URL; course pages can provide their own data through an inline JSON
block or their existing local page-data mechanism.

CODEX BITE week16-slider-component READY FOR IVY INTEGRATION
