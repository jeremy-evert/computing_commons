# Aider Classroom Bite Research 020 — Control

Run: `8623fc51cb3e80fe6df1ed6ef8efc02d`; work-file SHA-256: `007cb649a3c45f9cc4379d091d1d397df51496230834ae258f5dc70c08f15707`.

Host truth: Brandy, 96 logical CPUs, 375 GiB RAM, no usable NVIDIA driver, Ollama 0.12.6 on `127.0.0.1:11434`.

Owning repository: `jeremy-evert/computing_commons`; campaign branch `anna/aider-bite-020`; baseline fixture commit `a230e578b81670037e14b1306e1fd8c951845479`.

Measured worker for Shots 1–3: Aider 0.86.2, `ollama_chat/qwen2.5-coder-3b-cpu:latest` (Ollama ID `6a345c984a47`), `whole` edit format, local endpoint, independent process per attempt, no auto-commits, warmed Ollama policy after the calibration.

Milestone reviewer candidate: `ollama_chat/qwen2.5:14b` (installed Ollama ID `7cdf5a0187d5`), review-only, separate from measured worker latency. The reviewer contract is `foreman_interface/sidecar/prompts/025_aider_classroom_bite_research_reviewer.md`.

Calibration: the original multi-function MICRO context produced scope-drift deletion under both `diff` and `whole`; a preserved one-function MICRO fixture then passed with corrected `ollama_chat/` transport and whole format. This campaign therefore records transport and visible-surface failures separately from task-size conclusions.

Teaching fixture: disposable, freshman-readable integer-cent budget helper and independent pytest oracle under this directory. The oracle is never supplied as an editable Aider file.
