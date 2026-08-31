# Mission 023 run plan

Prediction registered before scoring: ISOLATED should be dependable; NEIGHBORHOOD may remain workable but slower; MODULE should show more scope/transport failure. The same formatter behavior, examples, proof, worker, prompt skeleton, warm policy, and reset were held constant.

Non-scored calibration history is preserved under `calibration/`, `calibration2/`, and the post-repair verification under `attempts/isolated/valid_000/`. The verification passed its independent oracle and regression, with complete three-way diff capture and no forbidden paths. Scored repetitions are `attempts/{isolated,neighborhood,module}/valid_{001,002,003}`.

Stop after three repetitions per condition unless variance could change the teaching decision. The decision rule is machine-side only: compare oracle/regression success, malformed transport, unexpected scope, wall time, diff inspectability, and proof burden. No claim about freshman comprehension is permitted.

