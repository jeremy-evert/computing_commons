"""A tiny freshman-readable budget helper used as a disposable Aider fixture."""


def label_cents(cents):
    """Format a non-negative integer number of cents as dollars."""
    if cents < 0:
        raise ValueError("cents must be non-negative")
    return "${}.{:02d}".format(cents // 100, cents % 100)


def add_expense(total_cents, expense_cents):
    """Add one expense, rejecting negative amounts."""
    if expense_cents < 0:
        raise ValueError("expense must be non-negative")
    return total_cents + expense_cents


def summarize(expenses):
    """Return a small summary for a list of integer-cent expenses."""
    values = list(expenses)
    total = sum(values)
    return {
        "count": len(values),
        "total_cents": total,
        "average_cents": total // len(values) if values else 0,
    }
