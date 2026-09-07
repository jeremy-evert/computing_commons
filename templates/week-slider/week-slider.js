(function (root, createWeekSlider) {
  if (typeof module === 'object' && module.exports) module.exports = createWeekSlider();
  else root.WeekSlider = createWeekSlider();
})(typeof globalThis === 'object' ? globalThis : this, function () {
  'use strict';

  function dateOnly(date) {
    return Date.UTC(date.getFullYear(), date.getMonth(), date.getDate());
  }

  function parseStartDate(value) {
    var parts = String(value || '').split('-').map(Number);
    if (parts.length !== 3 || parts.some(function (part) { return !Number.isFinite(part); })) {
      throw new Error('week1_start_date must be an ISO date (YYYY-MM-DD)');
    }
    return new Date(parts[0], parts[1] - 1, parts[2]);
  }

  // The documented convention is Monday. The first Friday after that Monday
  // is the first Friday rollover; every later rollover is seven days apart.
  function computeWeekNumber(data, now) {
    var start = parseStartDate(data.week1_start_date);
    var elapsedDays = Math.floor((dateOnly(now) - dateOnly(start)) / 86400000);
    if (elapsedDays < 0) return 1;
    var week = Math.floor((elapsedDays - 4) / 7) + 2;
    return Math.max(1, Math.min(16, week));
  }

  function validateData(data) {
    if (!data || !Array.isArray(data.weeks) || data.weeks.length !== 16) {
      throw new Error('week data must contain exactly 16 weeks');
    }
    data.weeks.forEach(function (entry, index) {
      if (entry.week !== index + 1 || typeof entry.title !== 'string' || typeof entry.url !== 'string') {
        throw new Error('week data entries must contain ordered week, title, and url fields');
      }
    });
  }

  function nextFriday(now) {
    var result = new Date(now.getTime());
    result.setHours(0, 0, 0, 0);
    var daysUntilFriday = (5 - result.getDay() + 7) % 7;
    if (daysUntilFriday === 0) daysUntilFriday = 7;
    result.setDate(result.getDate() + daysUntilFriday);
    return result;
  }

  function WeekSlider(container, data, options) {
    if (!container || typeof document === 'undefined') throw new Error('a browser container is required');
    validateData(data);
    options = options || {};
    var getNow = options.getNow || function () { return new Date(); };
    var selected = computeWeekNumber(data, getNow());
    var range = document.createElement('input');
    range.type = 'range'; range.min = '1'; range.max = '16'; range.step = '1';
    range.className = 'week-slider__range'; range.setAttribute('aria-label', 'Select a week');
    var weekList = document.createElement('div'); weekList.className = 'week-slider__weeks';
    var content = document.createElement('article'); content.className = 'week-slider__content';
    var timer;

    function draw() {
      range.value = String(selected);
      Array.prototype.forEach.call(weekList.children, function (button, index) {
        button.setAttribute('aria-selected', String(index + 1 === selected));
        button.setAttribute('aria-current', String(index + 1 === computeWeekNumber(data, getNow())));
      });
      var entry = data.weeks[selected - 1];
      content.innerHTML = '<h2>Week ' + entry.week + ': ' + escapeHtml(entry.title) + '</h2>' +
        '<p><a href="' + escapeAttribute(entry.url) + '">Open Week ' + entry.week + ' material</a></p>';
    }
    function choose(week) { selected = Math.max(1, Math.min(16, Number(week))); draw(); }
    function refreshCurrent() { selected = computeWeekNumber(data, getNow()); draw(); schedule(); }
    function schedule() {
      if (timer) clearTimeout(timer);
      timer = setTimeout(refreshCurrent, Math.max(0, nextFriday(getNow()).getTime() - getNow().getTime()));
    }
    function escapeHtml(value) { return String(value).replace(/[&<>"']/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]; }); }
    function escapeAttribute(value) { return escapeHtml(value); }

    container.classList.add('week-slider');
    var label = document.createElement('label'); label.className = 'week-slider__label'; label.textContent = 'Course weeks';
    label.appendChild(range); container.appendChild(label); container.appendChild(weekList); container.appendChild(content);
    for (var week = 1; week <= 16; week += 1) {
      var button = document.createElement('button'); button.type = 'button'; button.className = 'week-slider__week';
      button.textContent = 'Week ' + week; button.setAttribute('aria-label', 'Week ' + week);
      button.addEventListener('click', (function (value) { return function () { choose(value); }; })(week));
      weekList.appendChild(button);
    }
    range.addEventListener('input', function () { choose(range.value); });
    draw(); schedule();
    return { select: choose, getSelectedWeek: function () { return selected; }, refresh: refreshCurrent };
  }

  return { computeWeekNumber: computeWeekNumber, validateData: validateData, mount: function (container, data, options) { return new WeekSlider(container, data, options); } };
});
