Goal: add initials(full_name) to the fixed string MODULE fixture at sidecar/experiments/aider_classroom_bite_research_028/fixture/string_module.py.
Behavior: return uppercase initials for each whitespace-separated name part; ignore repeated/leading/trailing whitespace; raise ValueError for blank/whitespace-only input.
Allowed scope: the exact target module only.
Do not change: tests, oracle, unrelated helpers, unrelated behavior, or any other path.
Proof: fixed behavioral oracle plus regression proof.
