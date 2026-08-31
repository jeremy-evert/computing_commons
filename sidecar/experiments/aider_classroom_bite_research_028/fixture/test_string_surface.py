import importlib.util


def load_module():
    path = __file__.replace("test_string_surface.py", "string_module.py")
    spec = importlib.util.spec_from_file_location("string_surface", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_baseline_helpers_and_initials():
    module = load_module()
    assert module.join_words(["Ada", "Lovelace"]) == "Ada Lovelace"
    assert module.word_count("Ada   Lovelace") == 2
    assert module.first_word("Ada Lovelace") == "Ada"
    assert module.last_word("Ada Lovelace") == "Lovelace"
    assert module.has_word("Ada Lovelace", "Ada")
    assert module.uppercase_words(["Ada", "Lovelace"]) == ["ADA", "LOVELACE"]
