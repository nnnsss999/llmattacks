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
- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- [Mitigating Many-Shot Jailbreaking (arXiv:2504.09604)](https://arxiv.org/abs/2504.09604)
- [PANDAS: Improving Many-shot Jailbreaking via Positive Affirmation, Negative Demonstration, and Adaptive Sampling](https://arxiv.org/abs/2502.01925)
- [Compromesso! Italian Many-Shot Jailbreaks Undermine the Safety of Large Language Models](https://arxiv.org/abs/2408.04522)
- [Improved Few-Shot Jailbreaking Can Circumvent Aligned Language Models and Their Defenses](https://arxiv.org/abs/2406.01288)
- [What Really Matters in Many-Shot Attacks? An Empirical Study of Long-Context Vulnerabilities in LLMs](https://arxiv.org/abs/2505.19773)
- [New AI hacking technique: Many-shot jailbreaking (Barracuda Networks Blog)](https://blog.barracuda.com/2024/05/30/new-AI-hacking-technique-many-shot-jailbreaking)
- [Many-shot jailbreaking (HuggingFace Blog)](https://huggingface.co/blog/vladbogo/many-shot-jailbreaking)
- [What Is Anthropic’s Many-shot Jailbreaking (Dataconomy)](https://dataconomy.com/2024/04/03/anthropic-many-shot-jailbreaking/)
- [Breaking Safeguards: Unveil "Many-Shot Jailbreaking" a Method to Bypass All LLM Safety Measures (InfoSec Write-ups)](https://infosecwriteups.com/breaking-safeguards-unveil-many-shot-jailbreaking-a-method-to-bypass-all-llm-safety-measures-2d188ebc12fb)
- [Many-shot Jailbreaking in Artificial Intelligence (LinkedIn)](https://www.linkedin.com/pulse/many-shot-jailbreaking-artificial-intelligence-reem-khattab-zudpc)
- [New AI Jailbreak Method 'Bad Likert Judge' Boosts Attack Success Rates by Over 60% (The Hacker News)](https://thehackernews.com/2025/01/new-ai-jailbreak-method-bad-likert.html)
- [PANDAS Poster at ICML 2025](https://icml.cc/virtual/2025/poster/43847)
- [SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents (Anthropic Research)](https://www.anthropic.com/research/shade-arena-sabotage-monitoring)

These resources detail how manipulating a model's working context can produce harmful or destabilizing behavior, motivating stricter input limits and improved monitoring.
