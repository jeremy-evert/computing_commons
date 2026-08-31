import importlib


def test_green_baseline_helpers():
    for name in ("neighborhood", "module"):
        surface = importlib.import_module("surfaces." + name)
        assert surface.add_expense(100, 25) == 125
        assert surface.summarize([100, 250])["total_cents"] == 350

    module = importlib.import_module("surfaces.module")
    assert module.subtract_expense(300, 100) == 200
    assert module.largest_expense([4, 9, 2]) == 9
    assert module.category_totals({"food": [100, 250]}) == {"food": 350}
    assert module.within_limit(300, 500)
    assert module.remaining_budget(500, 300) == 200

