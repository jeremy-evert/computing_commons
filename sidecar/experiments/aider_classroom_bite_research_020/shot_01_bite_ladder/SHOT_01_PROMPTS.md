# Frozen prompts

## MICRO
Implement only `label_cents` in `calibration_micro/micro_fixture.py`. For non-negative integer cents, return a dollar string with exactly two decimals (125 -> `$1.25`). Do not edit tests or other files.

## SMALL
Implement only `add_expense` in `fixture/budget.py`. Return the sum of two integer-cent amounts and raise `ValueError` when `expense_cents` is negative. Do not edit tests or other functions.

## MEDIUM
Implement `add_expense` and `summarize` in `fixture/budget.py` so the existing tests pass. Preserve `label_cents`; do not edit tests or other files. Use small, readable Python.

## LARGE
Implement every missing function in `fixture/budget.py` so the existing tests pass: dollar formatting, negative-expense rejection, and count/total/average summary. Do not edit tests. Keep the implementation readable and limited to this file.
