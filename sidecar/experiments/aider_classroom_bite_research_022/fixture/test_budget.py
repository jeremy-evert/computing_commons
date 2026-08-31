from budget import add_expense, label_cents, summarize


def test_label_cents():
    assert label_cents(125) == "$1.25"


def test_add_expense_rejects_negative_amounts():
    assert add_expense(100, 25) == 125
    try:
        add_expense(100, -1)
    except ValueError:
        pass
    else:
        raise AssertionError("negative expenses must be rejected")


def test_summarize_returns_total_count_and_average():
    assert summarize([100, 250]) == {
        "count": 2,
        "total_cents": 350,
        "average_cents": 175,
    }
