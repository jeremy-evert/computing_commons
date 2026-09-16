# smolagents learning lab

Status: **draft / instructor-first**

This Computing Commons module exists to teach agentic systems from the smallest useful pieces upward. Jeremy is the first student. The module should not be promoted as polished student curriculum until he can explain and reproduce the mechanics himself.

## Purpose

The goal is not to build an impressive agent quickly. The goal is to understand what each layer does:

```text
task
  -> agent
  -> model wrapper
  -> model/runtime
  -> generated action
  -> executor or tool
  -> observation
  -> agent memory
  -> next step
  -> final answer
```

The module uses Hugging Face `smolagents` because its abstractions are intentionally small, it supports both code agents and structured tool-calling agents, and it can use local models as well as hosted models.

## Learning rules

1. One new concept per lab whenever possible.
2. Run the smallest program that can prove the concept.
3. Keep receipts: source, command, output, and a short explanation.
4. A successful run is not mastery. The learner must explain the objects and boundaries involved.
5. The Python application owns deterministic state. The LLM does not get to hallucinate state changes.
6. Model/runtime experiments stay separate from agent-architecture lessons.
7. Large projects, D&D flavor, and names wait until the primitives are understood.

## Course arc

### 00 — Community and orientation

Read the smolagents introduction and guided tour, inspect the upstream repository, and compare the contribution posture of smolagents, MLX/MLX-LM, Transformers, and LangGraph.

Deliverable: a one-page community matrix and an explanation of why the learner chose a primary community.

### 01 — Python objects and model plumbing

Build the smallest programs that demonstrate imports, classes, instances, properties, a model wrapper, a direct model call, and a returned `ChatMessage`.

Deliverable: tiny runnable files plus plain-language explanations of what object was created, what was called, and what came back.

### 02 — The agent loop

Create a `CodeAgent` with no custom tools and inspect a multi-step run, including generated code, errors/recovery, final answer, memory, and token growth.

Deliverable: a diagram of `model(messages)` versus `agent.run(task)`.

### 03 — One tool

Create one trivial custom tool. Call the underlying function manually, inspect the tool metadata, give the tool to an agent, and deliberately break one required piece before repairing it.

Deliverable: proof that the learner understands why a tool is more than a bare Python function.

### 04 — State versus memory

Use a tiny deterministic world:

```text
room = "cell"
door = "locked"
has_key = False
```

Expose only a few operations such as `look()`, `take_key()`, and `unlock_door()`.

Deliverable: a restart experiment that distinguishes application state from agent memory.

### 05 — CodeAgent versus ToolCallingAgent

Run the same bounded task with both paradigms and compare the action representation, logs, failures, and result.

Deliverable: a short explanation of when Python actions and structured tool calls differ architecturally.

### 06 — Models and runtimes

Hold the task constant while swapping local model/runtime paths, including Ollama and MLX where practical.

Deliverable: a small evidence table with wall-clock time, token usage when available, success/failure, and observations.

### 07 — Execution and security

Inspect the local Python executor, authorized imports, and the limits of the local safety boundary. Then repeat one already-understood task in a stronger sandbox.

Deliverable: a boundary diagram showing what is trusted and what is isolated.

### 08 — One managed agent

Create a manager and exactly one specialist. Use a task that genuinely requires delegation.

Deliverable: evidence showing what context crosses the agent boundary and what remains separate.

### 09 — Open-source apprenticeship

Read the smolagents source, run its development tests/quality checks, create a source map, then choose a tiny contribution the learner fully understands.

Preferred first contributions: documentation, examples, regression tests, then narrowly scoped bug fixes.

### 10 — Student-ready module

Only after the instructor learning pass succeeds, convert these labs into polished Computing Commons material with readings, assignments, receipts, instructor notes, troubleshooting, and contribution guidance.

## Assigned upstream reading

Use canonical sources rather than copying their content into this repository:

- Introduction: https://huggingface.co/docs/smolagents/index
- Guided tour: https://huggingface.co/docs/smolagents/guided_tour
- Agents reference: https://huggingface.co/docs/smolagents/reference/agents
- Tools tutorial: https://huggingface.co/docs/smolagents/tutorials/tools
- Tools reference: https://huggingface.co/docs/smolagents/reference/tools
- Memory tutorial: https://huggingface.co/docs/smolagents/tutorials/memory
- Secure code execution: https://huggingface.co/docs/smolagents/tutorials/secure_code_execution
- Python executors: https://huggingface.co/docs/smolagents/reference/python_executors
- Multi-agent example: https://huggingface.co/docs/smolagents/examples/multiagents
- Upstream repository: https://github.com/huggingface/smolagents

## Current instructor scratch work

Jeremy's private/local scratch lab has already mechanically exercised:

- importing `CodeAgent`;
- inspecting the class;
- instantiating `LiteLLMModel` against local Ollama;
- direct model invocation and `ChatMessage` inspection;
- creating a `CodeAgent`;
- running a no-custom-tool agent and watching it fail, recover, execute code, and return `AgentText`.

Those runs are evidence of progress, but the next step is a mastery loop: rebuild the chain from memory and explain every boundary before adding more machinery.

## Capstone rule

The capstone remains unnamed until it earns one. It begins as a tiny deterministic world with a few tools and one bounded objective. Any future D&D flavor is optional and comes only after the agent mechanics are understood.

## Tracking

The instructor learning queue and mastery checks are tracked in `jeremy_task_tracking/tasks/2026-09-15_jeremy_smolagents_learning_priority.md`.
