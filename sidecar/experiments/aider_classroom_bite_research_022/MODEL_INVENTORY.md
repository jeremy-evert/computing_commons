# Mission 022 model inventory

Captured 2026-08-30 on Brandy from loopback Ollama inventory.

| candidate | exact tag | parameters | quantization | size | decision |
|---|---|---:|---|---:|---|
| Worker A | `qwen2.5-coder-3b-cpu:latest` | 3.1B | Q4_K_M | 1.93 GB | fixed contemporary control |
| Worker B | `qwen2.5-coder-7b-cpu:latest` | 7.6B | Q4_K_M | 4.68 GB | measured crossover worker |
| possible C | `qwen2.5-coder:14b` | 14.8B | Q4_K_M | 8.99 GB | reserve only if B leaves decision unresolved |

Relevant runtime truth: Aider 0.86.2; Ollama 0.12.6; `ollama_chat/...` provider route; CPU-only because `nvidia-smi` reports no usable driver. Aider uses the same frozen Mission 021 apparatus and warm-before-each-attempt policy for both measured workers.
