import importlib.util
import sys


path, expected_module = sys.argv[1:]
spec = importlib.util.spec_from_file_location("measured_surface", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
assert module.cents_to_label(125) == "$1.25"
assert module.cents_to_label(0) == "$0.00"

