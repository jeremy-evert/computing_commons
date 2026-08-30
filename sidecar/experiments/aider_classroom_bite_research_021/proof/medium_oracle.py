from budget import by_category, remaining_cents


assert remaining_cents(1000, 275) == 725
assert by_category({"food": [100, 250], "books": [300]}) == {
    "food": 350,
    "books": 300,
}
