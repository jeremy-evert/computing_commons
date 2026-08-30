# Week 2 — Verify the tools

Follow the current `local_ai_lab_setup` sequence and reviewed `windows_classroom`
contract. Inventory first, then distinguish presence, reachability, inference,
and correctness. The approved model is `qwen3:8b`; another tag is not a
substitute.

1. Record the Windows/Python/Git foundation actually available.
2. Check Ollama reachability.
3. Check the exact approved model and perform direct local inference.
4. Continue to the bounded Aider/Git change only after preserving receipts.
5. Independently inspect the diff and run the relevant test.

## The student loop for one tiny change

Use this card for each Aider bite:

`LOOK -> ASK -> PREDICT -> AIDER -> DIFF -> RUN -> DECIDE`

- **LOOK:** inspect the starting status and the one file or behavior in scope.
- **ASK:** give Aider one small, concrete change; do not ask it to design the
  whole exercise.
- **PREDICT:** write down the expected file, shape of the diff, and check you
  expect to pass before Aider edits anything.
- **AIDER:** let the approved local Aider workflow make that bounded edit.
- **DIFF:** inspect the actual diff and reject extra files or surprising text.
- **RUN:** perform the independent check you named, not just another model
  request.
- **DECIDE:** keep the change only when the diff and check support the claim;
  otherwise preserve the evidence and recover.

The model is the engine, Ollama is the local service, and Aider is the
project-aware chassis. Your prediction, diff, and independent check are the
evidence. One small bite is enough to learn the loop.

An accurate `NOT READY` receipt is useful evidence. Use [Recovery](recovery.md)
when a check fails.
