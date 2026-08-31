from budget import cents_to_label


assert cents_to_label(125) == "$1.25"
assert cents_to_label(0) == "$0.00"
