# Weeks 1–16 slider

This self-contained component renders a keyboard-operable Weeks 1–16 selector. It has no dependencies, network calls, external fonts, or CDN scripts. `week-slider.html` is a standalone browser demo; it embeds a sample data object so it also works when opened directly as a `file:` URL. The sample object mirrors `week-data.example.json`.

## Data shape

```json
{
  "week1_start_date": "2026-08-17",
  "weeks": [
    { "week": 1, "title": "Week title", "url": "/course/week-1" }
  ]
}
```

`weeks` must contain exactly 16 ordered entries, each with `week`, `title`, and `url`. `week1_start_date` uses the Monday convention: it is the local Monday on which Week 1 starts. The component clamps earlier dates to Week 1. The first Friday at local 00:00 advances to Week 2; each following Friday at local 00:00 advances one more week, through Week 16. This matches the settled Friday rollover rule while keeping the course's Week 1 date unambiguous.

## Include it on a course page

Include the CSS and component script, provide one container, and pass that course's own JSON data through the page's existing data mechanism (for a static page, an inline `application/json` block is the no-network option):

```html
<link rel="stylesheet" href="/templates/week-slider/week-slider.css">
<script src="/templates/week-slider/week-slider.js"></script>
<div id="course-week-slider"></div>
<script type="application/json" id="course-week-data">{ "week1_start_date": "2026-08-17", "weeks": [] }</script>
<script>
  const data = JSON.parse(document.getElementById('course-week-data').textContent);
  WeekSlider.mount(document.getElementById('course-week-slider'), data);
</script>
```

The component's date seam is `getNow`: tests or an integration harness can pass `{ getNow: () => fixedDate }` to `WeekSlider.mount`. The pure `computeWeekNumber(data, now)` function is also exported in Node.js.

## Test

From this directory, run:

```sh
TZ=America/Chicago node week-slider.test.js
```
