const assert = require('node:assert/strict');
const { computeWeekNumber } = require('./week-slider.js');

const data = { week1_start_date: '2026-08-17', weeks: Array.from({ length: 16 }, (_, i) => ({ week: i + 1, title: '', url: '' })) };
const local = (value) => new Date(value + '-05:00');

assert.equal(computeWeekNumber(data, local('2026-08-10T12:00:00')), 1, 'before Week 1 clamps to Week 1');
assert.equal(computeWeekNumber(data, local('2026-09-16T12:00:00')), 5, 'Wednesday remains in Week 5');
assert.equal(computeWeekNumber(data, local('2026-09-18T00:00:00')), 6, 'Friday 00:00 advances to Week 6');
assert.equal(computeWeekNumber(data, local('2026-12-31T12:00:00')), 16, 'after Week 16 clamps to Week 16');
console.log('week-slider tests: 4 passed');
