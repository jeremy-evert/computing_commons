# Week 2 — Use Aider with Work First

## What Aider is

Aider is a project-aware coding partner. It can explain code, suggest a
change, and help write a test. You remain responsible for the goal, the files
you share, the change you accept, and the evidence that it works.

The approved Week 2 route is local:

    student → Aider → Ollama → qwen3:8b → local machine

Do not enter an API key or choose a cloud provider. If a key or cloud-provider
prompt appears, stop and use Recovery with evidence.

## The safe loop

1. Start in the supplied disposable Git exercise.
2. Check the baseline with `git status --short` and the exercise's test.
3. Ask for one change in one sentence.
4. Inspect the complete `git diff`.
5. Run the independent test yourself.
6. Keep, repair, or reject the change based on the evidence.

This is Work First: make the next useful action small, visible, and testable.

## A first session

Use the approved local launcher from the supplied package. It keeps Aider on
the local Ollama service and the approved model. In Aider:

- use `/ask` when you want an explanation without an edit;
- use `/add` for only the source and test files needed for this task;
- request one bounded change;
- use `/diff` and read what changed before running anything.

Example request:

    Change display_label so it returns title-cased text; do not edit tests.

The request names the behavior and protects the test. Aider's answer is not
the acceptance check; the diff and independent test are.

## What to look for

The intended source file changed, and unrelated files did not. The diff should
match the sentence you wrote. Then run the supplied test command without
asking Aider to report the result for you.

Evidence has limits:

- Aider launched does not prove its edit is correct.
- A diff shows text that changed, not behavior that works.
- A passing test proves the tested behavior at that moment, not every
  untested requirement.

If the result is wrong, preserve the diff and describe expected versus actual
behavior. Make the next request smaller or bring the evidence to Recitation.
Do not ask Aider to “fix everything,” accept a large unexplained rewrite, or
commit a change you have not read.

## Completion proof

You are ready to show the work when you can provide:

- the clean starting state and baseline test;
- the one-sentence Aider request;
- the bounded diff you read and understand;
- the independent test result;
- one sentence explaining what you accepted and what remains unproven.

The goal is not to outsource judgment. The goal is to make a small change easy
to inspect, easy to test, and easy to recover when it is wrong.

Continue to **Show That It Works** after the independent test passes. If a
foundation check, Ollama, model, Aider launch, or test fails, stop at that
boundary and use **Recovery with evidence**.
