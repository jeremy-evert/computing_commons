"""Small neighborhood surface with unrelated but readable helpers."""


def add_expense(total_cents, expense_cents):
    if expense_cents < 0:
        raise ValueError("expense must be non-negative")
    return total_cents + expense_cents


def summarize(expenses):
    values = list(expenses)
    total = sum(values)
    return {"count": len(values), "total_cents": total, "average_cents": total // len(values) if values else 0}
