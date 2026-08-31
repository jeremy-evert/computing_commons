# Mission 028 second task family

The fresh bite is beginner-readable string processing: add `initials(full_name)` to
`fixture/string_module.py`. It returns uppercase initials from whitespace-separated
name parts, ignores repeated/leading/trailing whitespace, and raises `ValueError`
for blank input. The module has six simple neighboring helpers, no dependencies,
and one target source file. The oracle and regression proof are outside the Aider
editable scope.

Required oracle cases: Ada Lovelace, padded/repeated whitespace, Grace Brewster
Murray Hopper, Plato, blank input, and whitespace-only input.
