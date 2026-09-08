from itertools import product

claims = (28, 27, 26, 25)
solutions = []
checked = 0

for legs in product((6, 7, 8), repeat=4):
    checked += 1
    total = sum(legs)

    statements = tuple(
        total == claim
        for claim in claims
    )

    expected_truth = tuple(
        leg in (6, 8)
        for leg in legs
    )

    if statements == expected_truth:
        solutions.append(
            (legs, total, statements)
        )

print(f"Assignments checked: {checked}")
print(f"Solutions found: {len(solutions)}")

for legs, total, statements in solutions:
    truthful_servants = [
        index + 1
        for index, value in enumerate(statements)
        if value
    ]

    print(f"legs={legs}")
    print(f"total={total}")
    print(f"truthful servants={truthful_servants}")
