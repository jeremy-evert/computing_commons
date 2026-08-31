Goal: add cents_to_label(cents) to the fixed MODULE fixture.
Allowed scope: the exact target module only.
Do not change: tests, oracle, unrelated behavior, or any other path.
Proof: fixed behavioral oracle plus regression proof.
For a non-negative integer number of cents, return a dollar string with exactly two decimals; for example, 125 -> '$1.25' and 0 -> '$0.00'. Reject negative cents with ValueError.
