from budget import remaining_cents


assert remaining_cents(1000, 275) == 725
assert remaining_cents(275, 1000) == 0
