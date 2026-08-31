import importlib.util
import sys


path = sys.argv[1]
spec = importlib.util.spec_from_file_location("measured_string_module", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.initials("Ada Lovelace") == "AL"
assert module.initials("  Ada   Lovelace  ") == "AL"
assert module.initials("grace brewster murray hopper") == "GBMH"
assert module.initials("Plato") == "P"
for value in ("", "   \t"):
    try:
        module.initials(value)
    except ValueError:
        pass
    else:
        raise AssertionError("blank input must raise ValueError")
