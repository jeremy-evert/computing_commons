from itertools import product

CLAIMS = (28, 27, 26, 25)


def expected_truth_from_legs(leg_count):
    """Six- and eight-legged servants tell truth; seven-legged servants lie."""
    return leg_count in (6, 8)


solutions = []

for option_number, legs in enumerate(
    product((6, 7, 8), repeat=4),
    start=1
):
    total = sum(legs)

    print("=" * 72)
    print(f"OPTION {option_number:02d}: legs = {legs}")
    print(f"Total legs: {total}")

    option_works = True

    for servant_number, (leg_count, claimed_total) in enumerate(
        zip(legs, CLAIMS),
        start=1
    ):
        statement_is_true = total == claimed_total
        servant_should_tell_truth = expected_truth_from_legs(leg_count)

        if statement_is_true == servant_should_tell_truth:
            result = "PASS"
        else:
            result = "FAIL"
            option_works = False

        actual_truth_text = "TRUE" if statement_is_true else "FALSE"
        expected_truth_text = (
            "TRUE" if servant_should_tell_truth else "FALSE"
        )

        print()
        print(f"  Servant {servant_number}:")
        print(f"    Legs: {leg_count}")
        print(f"    Claims total is: {claimed_total}")
        print(f"    Actual total is: {total}")
        print(f"    Statement is actually: {actual_truth_text}")
        print(
            f"    Based on leg count, statement must be: "
            f"{expected_truth_text}"
        )
        print(f"    Result: {result}")

        if result == "FAIL":
            if leg_count == 7 and statement_is_true:
                print(
                    "    Why it fails: A seven-legged servant must lie, "
                    "but this servant's statement is true."
                )
            elif leg_count in (6, 8) and not statement_is_true:
                print(
                    "    Why it fails: A six- or eight-legged servant "
                    "must tell the truth, but this servant's statement "
                    "is false."
                )

    print()

    if option_works:
        print("OVERALL RESULT: THIS OPTION WORKS")
        solutions.append((legs, total))
    else:
        print("OVERALL RESULT: This option does not work.")

print()
print("#" * 72)
print("FINAL RESULTS")
print("#" * 72)
print(f"Assignments checked: {3 ** 4}")
print(f"Solutions found: {len(solutions)}")

for legs, total in solutions:
    truthful_servants = [
        servant_number
        for servant_number, claimed_total in enumerate(CLAIMS, start=1)
        if total == claimed_total
    ]

    print()
    print(f"Solution legs: {legs}")
    print(f"Total legs: {total}")
    print(f"Truthful servant(s): {truthful_servants}")
