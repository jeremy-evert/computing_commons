from html import escape
from itertools import product
from pathlib import Path


CLAIMS = (28, 27, 26, 25)

TEXT_REPORT = Path("king_octopus_bruteforce_results.txt")
HTML_REPORT = Path("king_octopus_bruteforce_results.html")


def expected_truth_from_legs(leg_count):
    """
    Return the truth value required by the servant's leg count.

    Six-legged and eight-legged servants tell the truth.
    Seven-legged servants lie.
    """
    return leg_count in (6, 8)


def truth_word(value):
    """Convert a Boolean value to a readable word."""
    return "TRUE" if value else "FALSE"


def evaluate_assignment(option_number, legs):
    """
    Evaluate one possible assignment of leg counts.

    Return a dictionary containing the total, servant-level results,
    and the overall result.
    """
    total = sum(legs)
    servant_results = []
    assignment_works = True

    for servant_number, (leg_count, claimed_total) in enumerate(
        zip(legs, CLAIMS),
        start=1,
    ):
        statement_is_true = total == claimed_total
        required_truth = expected_truth_from_legs(leg_count)
        servant_passes = statement_is_true == required_truth

        if servant_passes:
            explanation = (
                "The statement's truth value agrees with the rule "
                "for this servant's leg count."
            )
        elif leg_count == 7 and statement_is_true:
            explanation = (
                "A seven-legged servant must lie, but this servant's "
                "statement is true."
            )
        else:
            explanation = (
                "A six-legged or eight-legged servant must tell the "
                "truth, but this servant's statement is false."
            )

        if not servant_passes:
            assignment_works = False

        servant_results.append(
            {
                "servant_number": servant_number,
                "leg_count": leg_count,
                "claimed_total": claimed_total,
                "actual_total": total,
                "statement_is_true": statement_is_true,
                "required_truth": required_truth,
                "passes": servant_passes,
                "explanation": explanation,
            }
        )

    return {
        "option_number": option_number,
        "legs": legs,
        "total": total,
        "servants": servant_results,
        "works": assignment_works,
    }


def build_text_report(results):
    """Create a plain-text report suitable for inclusion in LaTeX."""
    lines = []

    lines.append("KING OCTOPUS BRUTE-FORCE SEARCH")
    lines.append("=" * 72)
    lines.append("")
    lines.append("Rules:")
    lines.append("  * Each servant has 6, 7, or 8 legs.")
    lines.append("  * A seven-legged servant always lies.")
    lines.append("  * A six-legged or eight-legged servant always tells the truth.")
    lines.append("  * The four claimed totals are 28, 27, 26, and 25.")
    lines.append("")
    lines.append(f"Assignments checked: {len(results)}")
    lines.append("")

    for result in results:
        status = "WORKS" if result["works"] else "DOES NOT WORK"

        lines.append("-" * 72)
        lines.append(
            f"OPTION {result['option_number']:02d}: "
            f"legs = {result['legs']}"
        )
        lines.append(f"Actual total: {result['total']}")
        lines.append(f"Overall result: {status}")
        lines.append("")

        for servant in result["servants"]:
            servant_status = "PASS" if servant["passes"] else "FAIL"

            lines.append(
                f"  Servant {servant['servant_number']}: "
                f"{servant['leg_count']} legs"
            )
            lines.append(
                f"    Claims that the total is "
                f"{servant['claimed_total']}."
            )
            lines.append(
                f"    The actual total is "
                f"{servant['actual_total']}."
            )
            lines.append(
                f"    Statement is actually: "
                f"{truth_word(servant['statement_is_true'])}"
            )
            lines.append(
                f"    Statement must be: "
                f"{truth_word(servant['required_truth'])}"
            )
            lines.append(f"    Result: {servant_status}")
            lines.append(
                f"    Explanation: {servant['explanation']}"
            )
            lines.append("")

    solutions = [result for result in results if result["works"]]

    lines.append("=" * 72)
    lines.append("FINAL RESULTS")
    lines.append("=" * 72)
    lines.append(f"Assignments checked: {len(results)}")
    lines.append(f"Solutions found: {len(solutions)}")
    lines.append("")

    if not solutions:
        lines.append("No assignment satisfies all of the rules.")
    else:
        for result in solutions:
            truthful_servants = [
                servant["servant_number"]
                for servant in result["servants"]
                if servant["statement_is_true"]
            ]

            lines.append(f"Solution legs: {result['legs']}")
            lines.append(f"Total legs: {result['total']}")
            lines.append(
                "Truthful servant(s): "
                + ", ".join(str(number) for number in truthful_servants)
            )
            lines.append("")

    return "\n".join(lines)


def build_html_report(results):
    """Create a polished HTML report suitable for a web browser."""
    solutions = [result for result in results if result["works"]]

    option_sections = []

    for result in results:
        option_class = "working-option" if result["works"] else "failed-option"
        option_status = "WORKS" if result["works"] else "DOES NOT WORK"

        servant_rows = []

        for servant in result["servants"]:
            result_class = "pass" if servant["passes"] else "fail"
            result_word = "PASS" if servant["passes"] else "FAIL"

            servant_rows.append(
                f"""
                <tr>
                    <td>{servant["servant_number"]}</td>
                    <td>{servant["leg_count"]}</td>
                    <td>{servant["claimed_total"]}</td>
                    <td>{servant["actual_total"]}</td>
                    <td>{truth_word(servant["statement_is_true"])}</td>
                    <td>{truth_word(servant["required_truth"])}</td>
                    <td class="{result_class}">{result_word}</td>
                    <td>{escape(servant["explanation"])}</td>
                </tr>
                """
            )

        servant_table = "\n".join(servant_rows)

        option_sections.append(
            f"""
            <details class="option {option_class}"
                     {"open" if result["works"] else ""}>
                <summary>
                    Option {result["option_number"]:02d}:
                    legs = {escape(str(result["legs"]))},
                    total = {result["total"]},
                    {option_status}
                </summary>

                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Servant</th>
                                <th>Legs</th>
                                <th>Claim</th>
                                <th>Actual Total</th>
                                <th>Statement</th>
                                <th>Required</th>
                                <th>Result</th>
                                <th>Explanation</th>
                            </tr>
                        </thead>
                        <tbody>
                            {servant_table}
                        </tbody>
                    </table>
                </div>
            </details>
            """
        )

    solution_items = []

    for result in solutions:
        truthful_servants = [
            servant["servant_number"]
            for servant in result["servants"]
            if servant["statement_is_true"]
        ]

        solution_items.append(
            f"""
            <li>
                Legs: <code>{escape(str(result["legs"]))}</code><br>
                Total: <strong>{result["total"]}</strong><br>
                Truthful servant(s):
                <strong>
                    {escape(", ".join(str(n) for n in truthful_servants))}
                </strong>
            </li>
            """
        )

    if solution_items:
        solution_html = "<ul>" + "\n".join(solution_items) + "</ul>"
    else:
        solution_html = "<p>No assignment satisfies all rules.</p>"

    all_options_html = "\n".join(option_sections)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>King Octopus Brute-Force Results</title>

    <style>
        :root {{
            color-scheme: light;
            font-family:
                Inter, Segoe UI, Arial, sans-serif;
            line-height: 1.5;
        }}

        body {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
            color: #172033;
            background: #f4f7fb;
        }}

        h1, h2 {{
            color: #12355b;
        }}

        .summary {{
            padding: 1.25rem;
            margin-bottom: 1.5rem;
            border-left: 6px solid #2463a7;
            border-radius: 8px;
            background: white;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        }}

        code {{
            padding: 0.15rem 0.35rem;
            border-radius: 4px;
            background: #e8eef6;
        }}

        details {{
            margin: 0.75rem 0;
            border: 1px solid #c8d1dc;
            border-radius: 8px;
            background: white;
            overflow: hidden;
        }}

        summary {{
            padding: 1rem;
            cursor: pointer;
            font-weight: 700;
        }}

        .working-option {{
            border: 3px solid #218739;
        }}

        .working-option summary {{
            color: #145c26;
            background: #eaf7ed;
        }}

        .failed-option summary {{
            background: #f8fafc;
        }}

        .table-container {{
            overflow-x: auto;
            padding: 1rem;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.92rem;
        }}

        th, td {{
            padding: 0.65rem;
            border: 1px solid #d8dee8;
            text-align: left;
            vertical-align: top;
        }}

        th {{
            color: white;
            background: #24496f;
        }}

        tr:nth-child(even) {{
            background: #f6f8fb;
        }}

        .pass {{
            color: #126b2a;
            font-weight: 700;
        }}

        .fail {{
            color: #a11b1b;
            font-weight: 700;
        }}

        footer {{
            margin-top: 2rem;
            color: #526173;
            font-size: 0.9rem;
        }}
    </style>
</head>

<body>
    <h1>King Octopus Brute-Force Search</h1>

    <section class="summary">
        <h2>Search Summary</h2>

        <p>
            The program checked all
            <strong>{len(results)}</strong>
            possible assignments.
        </p>

        <p>
            Number of solutions:
            <strong>{len(solutions)}</strong>
        </p>

        <h2>Valid Solution</h2>
        {solution_html}
    </section>

    <section>
        <h2>Every Assignment</h2>

        <p>
            Select an option to display the detailed reason that it
            works or fails. The valid option is expanded automatically.
        </p>

        {all_options_html}
    </section>

    <footer>
        Generated by king_octopus_bruteforce_report_generator.py
    </footer>
</body>
</html>
"""


def main():
    results = [
        evaluate_assignment(option_number, legs)
        for option_number, legs in enumerate(
            product((6, 7, 8), repeat=4),
            start=1,
        )
    ]

    text_report = build_text_report(results)
    html_report = build_html_report(results)

    TEXT_REPORT.write_text(text_report, encoding="utf-8")
    HTML_REPORT.write_text(html_report, encoding="utf-8")

    solutions = [result for result in results if result["works"]]

    print("King Octopus brute-force search complete.")
    print(f"Assignments checked: {len(results)}")
    print(f"Solutions found: {len(solutions)}")
    print()
    print(f"Text report: {TEXT_REPORT.resolve()}")
    print(f"HTML report: {HTML_REPORT.resolve()}")

    for result in solutions:
        truthful_servants = [
            servant["servant_number"]
            for servant in result["servants"]
            if servant["statement_is_true"]
        ]

        print()
        print(f"Solution legs: {result['legs']}")
        print(f"Total legs: {result['total']}")
        print(f"Truthful servant(s): {truthful_servants}")


if __name__ == "__main__":
    main()