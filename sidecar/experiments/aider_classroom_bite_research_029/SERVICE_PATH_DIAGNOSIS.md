# Mission 029 service-path diagnosis

## Scope and preserved failure

Mission 028 remains immutable on `anna/aider-diff-second-task-family-028` at
remote tip `f45a9376199cb1061ce775ce1b402b859fa3242f`. Its two first scored
attempts were `INVALID_TIMEOUT`: whole and diff each reached the preregistered
360-second ceiling, were process-group terminated, and were reaped. The two
non-scored verification attempts had completed lifecycle receipts, so the
failure is not relabeled as a model result.

## Live apparatus truth at Mission 029 start

- Aider: `/home/jevert/.local/bin/aider`, version 0.86.2.
- Ollama: `/usr/local/bin/ollama`, version 0.12.6.
- Endpoint: `http://127.0.0.1:11434`; `OLLAMA_HOST` is inherited as
  `0.0.0.0:11434`, while the caller uses the local endpoint.
- Exact model present: `qwen2.5-coder-3b-cpu:latest`; 3.1B, GGUF, Q4_K_M,
  digest `6a345c984a47cb18293f2537da3cf1fa907bfb590342703d21c973828aeb006f`.
- Local service health responded with Ollama API version 0.12.6.
- No competing Aider/Ollama/experiment worker was visible in the process
  inventory at inspection time.
- Host memory had approximately 332 GiB available. GPU inspection reported no
  usable NVIDIA driver; this mission remains CPU-only.
- Flo job files were inspected. No Flo handoff is authorized or needed; Flo
  ownership is preserved.

## Diagnosis

The strongest supported explanation for Mission 028 is a transient local
model-service/caller-path availability failure, potentially involving cold
load or contention, rather than a scored whole-vs-diff model outcome. The
simultaneous format failures at the identical 360-second bound, combined with
the later responsive local API and exact model inventory, do not isolate cold
load, contention, provider drift, PTY defect, or Aider deadlock individually.
Mission 028's verification receipts show the PTY/reset/proof apparatus could
complete, which weakens a blanket PTY lifecycle diagnosis. The evidence does
not justify changing a scientific variable or claiming the model failed the
task.

## Repair boundary

No model, Aider/Ollama version, prompt, task fixture, edit format, timeout, or
CPU treatment was changed. The permitted repair is restoration of the local
service path by using the responsive existing service, serializing this run
against absent competing experiment workers, and carrying forward the repaired
025-derived caller with explicit process reaping and complete evidence capture.
No service restart or repeated lucky retry was performed.

## Pre-scored gate

One tiny direct exact-model responsiveness check and one fresh non-scored
verification per format must complete before scored attempts. The direct check
is apparatus evidence only. If the exact model again fails the apparatus
preflight window, Mission 029 stops as infrastructure failure.
