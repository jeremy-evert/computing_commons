# Instructor guide: Week 2 Aider + Work First

## The mental model

```text
student → Aider → Ollama → qwen3:8b → local machine
```

The student directs a bounded task. Aider is the project-aware client. Ollama
is the local service. `qwen3:8b` is the exact approved model. The machine
provides the runtime. Each layer can be available while the next layer is not
proven.

| Observation | Proves | Does not prove |
| --- | --- | --- |
| `python --version`, `git status` | foundation commands resolve; current Git state | Ollama, Aider, or correct code |
| Ollama loopback check | local service answered | model inference |
| exact `qwen3:8b` listed | model is reported available | model can answer |
| direct inference | one local request completed | Aider integration or code correctness |
| Aider launch | client reached the local profile | its edit is safe or correct |
| `git diff` | what text changed | behavior is correct |
| independent test | the tested behavior passes | every possible property |

## Live-demo choreography

1. Ask students to predict what each check can prove.
2. Run the approved foundation/inventory check. Stop at the first failure.
3. Check Ollama reachability, then exact model availability.
4. Run one direct `qwen3:8b` inference. Ask: “What did this prove that the model list did not?”
5. Open the supplied disposable Git exercise and record baseline status/test.
6. Launch the local-only Aider profile. The expected boundary is `ollama_chat/qwen3:8b` at `http://127.0.0.1:11434`, with the reviewed `num_ctx: 8192` settings.
7. Request one narrow change. Exit Aider, inspect `git diff`, then run the independent test.
8. Repeat the inspect → ask → diff → test loop for the three tiny wins.
9. Have students write one sentence connecting that loop to Work First.

At each checkpoint ask: “What does this evidence establish, and what remains
unproven?” Generation is not verification.

## Failure branches

- **Command missing:** preserve the command and diagnostic; do not install or switch launchers.
- **Ollama unreachable (`W2-API-001`):** confirm the supplied folder and rerun the same check once; do not scan ports or use cloud.
- **Model unavailable (`W2-MODEL-001`):** stop; staff decide provisioning. Do not download or substitute.
- **Direct inference works but Aider fails:** check the approved local launcher/config boundary; capture any cloud/key prompt without entering credentials.
- **Unexpected cloud-provider/key prompt:** stop immediately and escalate; the student path is local-only.
- **Wrong file or extra diff:** reject the change, preserve `git diff`, and reset only the disposable exercise if instructed.
- **Test fails:** treat it as evidence, not a reason to claim success. Compare the diff with the requested behavior and recover through Recitation.

The student-facing recovery receipt should contain the claim, command, exit
status, smallest useful output, and next conclusion. Bold black quoted
**"NOT READY"** is a status label, not a red fake link.

## Three-meeting route (adaptable to M/W/F)

- **Meeting 1:** orientation, inventory, Windows foundation, Ollama/model, and direct inference.
- **Meeting 2:** Aider mental model, disposable Git worktree, first bounded edit, diff, and independent test.
- **Meeting 3:** three tiny wins, recovery practice, concise completion receipt, and Work First bridge.

The Commons pages remain sequential and do not depend on a timetable.

## One-session Recitation route

Start from the student’s actual receipt. Verify baseline, rerun the smallest
failed prerequisite once, then do one bounded Aider change and inspect the diff
and test. If the issue crosses provisioning, credentials, elevation, model
download, or repeated service repair, stop and escalate rather than turning
Recitation into systems administration.

## Defer to Recitation

Defer machine repair, model provisioning, cloud/provider configuration,
advanced Git recovery, large repository work, and the full Work First station.
Week 2 only introduces the repeatable loop.

## What not to improvise live

Do not change `qwen3:8b`, the loopback endpoint, Aider’s local provider, the
reviewed settings, or the disposable-exercise contract. Do not ask students
for API keys, GitHub credentials, administrator rights, model downloads, or a
personal project. If canonical guidance changes, update the source contract
before changing this route.
