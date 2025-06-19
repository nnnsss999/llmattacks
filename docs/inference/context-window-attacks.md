---
title: "Context Window Attacks"
category: "Inference"
source_url: "https://genai.owasp.org/llmrisk2023-24/llm04-model-denial-of-service/"
date_collected: 2025-06-18
license: "CC-BY-4.0"
---

Large language models can be subverted by manipulating their **context window**—the portion of recent tokens that influence generation. Attackers exploit long context windows to bury malicious instructions or force excessive processing, leading to denial of service or policy bypass.

Common patterns include:

- **Context-window flooding** to exhaust resources and degrade service.
- **Hidden prompts** inserted deep in long inputs that override safety systems.
- **Recursive expansion** where crafted responses trigger further context growth.

Credible references discussing these vectors:

- [OWASP LLM04: Model Denial of Service](https://genai.owasp.org/llmrisk2023-24/llm04-model-denial-of-service/)
- [Anthropic Shares Research on Technique to Exploit Long Context Windows](https://www.maginative.com/article/many-shot-jailbreaking-exploiting-long-context-windows-in-large-language-models/)
- [LLM Adversarial Attacks: Malicious Prompting](https://dev.to/gssakash/llm-adversarial-attacks-how-are-attackers-maliciously-prompting-llms-and-steps-to-safeguard-your-applications-4gfj)
- [Understanding LLM Context Windows, Tokens, Attention and Challenges](https://medium.com/@tahirbalarabe2/understanding-llm-context-windows-tokens-attention-and-challenges-c98e140f174d)
- [Many-shot Jailbreaking (NeurIPS 2024)](https://openreview.net/forum?id=cw5mgd71jW)
- [Image Hijacks: Adversarial Images can Control Generative Models](http://arxiv.org/abs/2309.00236)

These resources detail how manipulating a model's working context can produce harmful or destabilizing behavior, motivating stricter input limits and improved monitoring.
