from budget import add_expense, label_cents, summarize


assert label_cents(125) == "$1.25"
assert add_expense(100, 25) == 125
assert summarize([100, 250]) == {
    "count": 2,
    "total_cents": 350,
    "average_cents": 175,
}
