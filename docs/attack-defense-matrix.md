---
title: "Attack–Defence Matrix"
category: "Overview"
source_url: "https://github.com/example/llmattacks"
date_collected: 2025-06-18
license: "CC BY 4.0"
---

This matrix links the documented attack vectors to representative defences or mitigation techniques. It helps researchers quickly see which protections relate to each attack type.

| Attack Vector | Example File | Representative Defence |
|---------------|-------------|------------------------|
| TokenBreak single-character bypass | [tokenbreak-single-character-bypass](prompt-dialogue/tokenbreak-single-character-bypass.md) | Input normalization and tokenizer patches |
| Agent toolchain privilege escalation | [agent-toolchain-priv-escalation](agentic/agent-toolchain-priv-escalation.md) | Sandboxing of tool execution environments |
| Mechanism-centric data poisoning | [mechanism-centric-poisoning](training-alignment/mechanism-centric-poisoning.md) | Dataset provenance checks and poisoning detection |
| Reinforcement-learning alignment attacks | [reinforcement-learning-alignment-attacks](training-alignment/reinforcement-learning-alignment-attacks.md) | Reward auditing and alignment evaluation suites |
| Image obscuring jailbreak | [image-obscuring-jailbreak](multimodal/image-obscuring-jailbreak.md) | Multimodal safety filters on uploaded content |
| Audio steganography jailbreak | [audio-steganography-jailbreak](multimodal/audio-steganography-jailbreak.md) | Audio sanitization and format validation |
| Timing side-channel extraction | [timing-side-channel](inference/timing-side-channel.md) | Cache isolation and latency noise |
| Membership inference attacks | [membership-inference](inference/membership-inference.md) | Differential privacy and output perturbation |
| Safety filter timing side-channel | [safety-filter-timing-side-channel](inference/safety-filter-timing-side-channel.md) | Constant-time filtering implementations |
| Alignment-aware model extraction | [alignment-aware-mea](inference/alignment-aware-mea.md) | Watermarking and query rate limiting |
| Gradient leakage via LoRA | [gradient-leakage-inversion](inference/gradient-leakage-inversion.md) | Gradient clipping and differential privacy |

