# Week 2 — Build and Verify Your Local AI Workbench

Instructor notes · Computing Commons · projected deck companion

Each move keeps the question visible: *What does this prove, and what does it not prove?*

## 1. Build and Verify Your Local AI Workbench

- **Purpose:** Set the finish line: evidence, not installation theater.
- **Say:** “Today we will trace a local request, make one bounded change, and prove a result independently. Every check has a limit.”
- **Ask:** What would count as evidence that the workflow works?
- **Do:** Tell students to keep a small receipt as they work.
- **Watch for:** Treating a green status or generated answer as a conclusion.
- **Move on when:** Students can name observation, claim, and limit.

## 2. Today's finish line

- **Purpose:** Preview the three teachable outcomes.
- **Say:** “We are not trying to master every tool today. We are practicing a repeatable loop: trace, change narrowly, test independently.”
- **Ask:** Which step is easiest to skip when you are rushed?
- **Do:** Have students predict the evidence for each outcome.
- **Watch for:** Students equating Aider’s action with correctness.
- **Move on when:** The room can repeat the evidence ladder.

## 3. Why these tools? The workbench is infrastructure

- **Purpose:** Frame tools as shared infrastructure and judgment as human work.
- **Say:** “Machines provide motion; people provide meaning, scope, and the decision that a result is good enough.”
- **Ask:** Where does responsibility remain after a tool acts?
- **Do:** Connect the rule to a recent debugging or documentation task.
- **Watch for:** “The tool said so” replacing explanation.
- **Move on when:** Students can name one human judgment they must retain.

## 4. The stack: layers, not magic

- **Purpose:** Establish the request → client → service → model path.
- **Say:** “A layer can work while the next layer fails. We will check the chain in order rather than guessing.”
- **Ask:** What does a response from one layer fail to prove about the next?
- **Do:** Point to each arrow and have students name its observable.
- **Watch for:** Calling Aider the model or treating Ollama as the whole workflow.
- **Move on when:** Students can explain the role of Aider, Ollama, and qwen3:8b.

## 5. Evidence before model action

- **Purpose:** Separate foundation/service observations from inference.
- **Say:** “python --version proves a command/runtime answered. ollama list proves a model is reported available. A loopback check proves service reachability.”
- **Ask:** What remains unproven after each check?
- **Do:** Record one bounded claim beside each observation.
- **Watch for:** “Installed” becoming “works.”
- **Move on when:** Students state the limit for all three checks.

## 6. Evidence after model action

- **Purpose:** Teach direct inference and diff as distinct evidence.
- **Say:** “A direct request proves one request completed. git diff proves text changed. Neither alone proves behavior or correctness.”
- **Ask:** Which independent check would support the behavior claim?
- **Do:** Model saving the exact tag, response, exit status, and diff.
- **Watch for:** Trusting narration instead of the artifact.
- **Move on when:** Students can distinguish generation, change, and behavior.

## 7. A chain of bounded evidence

- **Purpose:** Consolidate the evidence ladder.
- **Say:** “We are not collecting reassuring green lights. We are building a chain where each observation supports one limited conclusion.”
- **Ask:** What does this prove, and what does it not prove?
- **Do:** Ask one student to supply a claim limit for a check.
- **Watch for:** Overclaiming from several weak observations.
- **Move on when:** The class can articulate observation → claim → check → limit.

## 8. First: open PowerShell

- **Purpose:** Make the Windows launch action recognizable and low-friction.
- **Say:** “Find the supplied PowerShell 7 window and the prompt before typing. The prompt tells you where the command will run.”
- **Ask:** How can you verify which PowerShell is open?
- **Do:** Have students point to Start, PowerShell, provisioned PowerShell 7, and the prompt.
- **Watch for:** Pasting into search or the wrong shell.
- **Move on when:** Every student can identify the prompt.

## 9. Verify PowerShell itself

- **Purpose:** Practice command, documentation, local observation, and receipt.
- **Say:** “The version command answers one narrow question. It does not prove the whole toolchain.”
- **Ask:** What official documentation supports this command?
- **Do:** Run `$PSVersionTable.PSVersion`; save timestamp and smallest useful output.
- **Watch for:** Substituting a screenshot or guessing the version.
- **Move on when:** Students have their own output and its limit.

## 10. Python: the runtime for our program

- **Purpose:** Make the command/runtime boundary explicit.
- **Say:** “python --version proves the command resolves and a runtime reports. It does not prove packages, program behavior, or tests.”
- **Ask:** What would be a separate behavior check?
- **Do:** Run the foundation check supplied by class.
- **Watch for:** Treating version output as program validation.
- **Move on when:** Students write the untested claim beside the output.

## 11. Git: the before-and-after witness

- **Purpose:** Establish baseline and diff as durable evidence.
- **Say:** “Git gives us a known starting state and a precise account of what changed. It is a witness, not a judge of behavior.”
- **Ask:** Which file and lines changed? Any extras?
- **Do:** Run status and diff in the supplied disposable exercise.
- **Watch for:** Unreviewed unrelated files or secrets in the diff.
- **Move on when:** Baseline and intended file are recorded.

## 12. Ollama: a local service on loopback

- **Purpose:** Explain local routing without overclaiming security.
- **Say:** “127.0.0.1 means this machine and the endpoint answered. That is reachability evidence, not proof of inference, privacy, or Aider integration.”
- **Ask:** What endpoint and response did you actually observe?
- **Do:** Run only the approved loopback check.
- **Watch for:** Port scanning, cloud fallback, or inventing a new command.
- **Move on when:** Students can state the reachability claim and limit.

## 13. Security is a judgment question

- **Purpose:** Make safety and security an evidence conversation.
- **Say:** “Local is a routing fact. Security also involves configuration, authentication, data handling, and correctness. We need official documentation and local verification.”
- **Ask:** Is this safe? Is this secure? How do I know? Where can I verify that?
- **Do:** Compare the official source with the observed endpoint/configuration.
- **Watch for:** Using loopback as a blanket privacy guarantee.
- **Move on when:** Students distinguish locality, application configuration, and data handling.

## 14. The exact approved model: qwen3:8b

- **Purpose:** Preserve the exact reviewed model boundary.
- **Say:** “A model listed is available according to the service. A direct request is the separate evidence that it answered.”
- **Ask:** What did inference prove that the list did not?
- **Do:** Check the exact tag and run the approved direct request.
- **Watch for:** Substitution, downloading, or provider detour.
- **Move on when:** The receipt contains tag, command, response, and exit status.

## 15. Aider is the coding client, not the model

- **Purpose:** Clarify client/service/model responsibilities and canonical boundary.
- **Say:** “Aider gathers bounded context and leaves changes for inspection. The approved path is ollama_chat/qwen3:8b at http://127.0.0.1:11434 with num_ctx 8192.”
- **Ask:** What does `aider --version` prove, and what does it not prove?
- **Do:** Confirm the approved local profile only.
- **Watch for:** Cloud keys, provider prompts, or treating the client version as integration proof.
- **Move on when:** Students can name the client, service, model, and endpoint separately.

## 16. The first Aider win: one bounded change

- **Purpose:** Show scope as a safety feature.
- **Say:** “A good request names the supplied exercise, one implementation file, and the test boundary. ‘Fix everything’ is not a testable task.”
- **Ask:** What is the smallest request that could produce a useful receipt?
- **Do:** Record baseline, make one narrow request, and forbid test edits.
- **Watch for:** Scope creep or an unknown starting state.
- **Move on when:** The requested change has a clear file and behavior.

## 17. Inspect the diff before you trust it

- **Purpose:** Put human review between generation and acceptance.
- **Say:** “Aider changed it is not the same as the change is correct. Read every changed line and explain it.”
- **Ask:** Any extra file, secret, or unrelated cleanup?
- **Do:** Exit Aider and inspect the approved diff command.
- **Watch for:** Accepting a large diff because the test was not run yet.
- **Move on when:** The diff is bounded and explainable.

## 18. Independent test: a different claim

- **Purpose:** Separate behavior evidence from the model’s narration.
- **Say:** “A passing test supports only the behavior it defines. It does not certify every input or every property.”
- **Ask:** What exactly does this test exercise?
- **Do:** Run the supplied independent final test and preserve exit status/output.
- **Watch for:** Calling a partial test proof of the entire project.
- **Move on when:** Students can state the test’s coverage boundary.

## 19. Three tiny wins: repeat the loop

- **Purpose:** Build confidence through repeated bounded cycles.
- **Say:** “Independence grows one loop at a time: baseline, bounded ask, inspect, test, accept or recover.”
- **Ask:** Which evidence is carried into the next win?
- **Do:** Repeat only the approved tiny exercise route.
- **Watch for:** Increasing scope before the prior receipt is complete.
- **Move on when:** Students can narrate all five stages.

## 20. Recovery is part of the workflow

- **Purpose:** Normalize a bounded stop and escalation.
- **Say:** “NOT READY is useful evidence. Stop at the first failed check, preserve the diagnostic, and do one documented retry.”
- **Ask:** Which failures belong with staff rather than improvisation?
- **Do:** Practice claim, command, exit status, output, and next conclusion.
- **Watch for:** Switching models, scanning ports, installing, or repeated repair.
- **Move on when:** Students can produce a failure receipt.

## 21. Prompt structure: from answer to evidence

- **Purpose:** Turn vague questions into verifiable requests.
- **Say:** “A strong prompt supplies platform, version, action, observation, primary source, and limits.”
- **Ask:** How would you ask for an independent check?
- **Do:** Upgrade one weak question as a class.
- **Watch for:** Citation without local verification or local output without source authority.
- **Move on when:** The revised question contains a check and a limit.

## 22. Learning to fish: the scaffold fades

- **Purpose:** Show how the same evidence habit produces independence.
- **Say:** “The scaffold changes from action and prompt to student-selected checks. The habit remains claim, observation, limit, conclusion.”
- **Ask:** What responsibility increases at each stage?
- **Do:** Have students place their current task on the line.
- **Watch for:** Confusing less scaffolding with less verification.
- **Move on when:** Students can defend one chosen check.

## 23. Work First: the bridge

- **Purpose:** Connect this small exercise to professional practice.
- **Say:** “Work First means knowing the starting state, bounding work, inspecting evidence, testing independently, and preserving what remains true.”
- **Ask:** Which step protects the next person who has to continue?
- **Do:** Map one student receipt onto the pipeline.
- **Watch for:** Treating durable truth as optional documentation.
- **Move on when:** Students can connect their loop to a handoff.

## 24. Show that it works: the Week 2 receipt

- **Purpose:** Define the observable completion target.
- **Say:** “A small receipt beats a confident story: claim, command, status, smallest output, conclusion, and limit.”
- **Ask:** What evidence is still missing from your receipt?
- **Do:** Give students time to assemble and read their receipt.
- **Watch for:** Omitting failure evidence or exact model identity.
- **Move on when:** Each student can demonstrate the bounded change and its independent test.

## 25. Your turn

- **Purpose:** Hand the room from explanation to student work.
- **Say:** “Ask narrowly, inspect honestly, test independently, and keep the receipt. We will stop at the first meaningful failure and use the recovery path.”
- **Ask:** What does this prove?
- **Do:** Release students to the supplied exercise.
- **Watch for:** Students starting outside the supplied folder or changing the approved boundary.
- **Move on when:** Students have begun with a baseline receipt.

## Canvas follow-up

Keep exact recovery and self-paced command detail in Canvas/Commons pages. Consider separate student pages for evidence-before-action, evidence-after-action, and security judgment so projected discussion does not carry every procedural branch.
