from micro_fixture import label_cents


def test_label_cents():
    assert label_cents(125) == "$1.25"
