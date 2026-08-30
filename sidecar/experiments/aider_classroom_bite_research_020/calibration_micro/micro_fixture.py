def label_cents(cents):
    """Return a dollar label for a non-negative integer number of cents."""
    return "${:.2f}".format(cents / 100)
