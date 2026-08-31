"""Freshman-readable budget module with several neighboring responsibilities."""


def add_expense(total_cents, expense_cents):
    if expense_cents < 0:
        raise ValueError("expense must be non-negative")
    return total_cents + expense_cents


def subtract_expense(total_cents, expense_cents):
    if expense_cents < 0:
        raise ValueError("expense must be non-negative")
    return total_cents - expense_cents


def summarize(expenses):
    values = list(expenses)
    total = sum(values)
    return {"count": len(values), "total_cents": total, "average_cents": total // len(values) if values else 0}


def largest_expense(expenses):
    values = list(expenses)
    return max(values) if values else 0


def category_totals(expenses_by_category):
    return {name: sum(values) for name, values in expenses_by_category.items()}


def within_limit(total_cents, limit_cents):
    return total_cents <= limit_cents


def remaining_budget(limit_cents, spent_cents):
    return max(0, limit_cents - spent_cents)
