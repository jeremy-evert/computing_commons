from budget import budget_report


assert budget_report(1000, {"food": [100, 250], "books": [300]}) == {
    "limit_cents": 1000,
    "spent_cents": 650,
    "remaining_cents": 350,
    "by_category": {"food": 350, "books": 300},
    "over_budget": False,
}
