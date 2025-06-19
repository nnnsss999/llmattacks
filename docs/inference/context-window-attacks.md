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

These resources detail how manipulating a model's working context can produce harmful or destabilizing behavior, motivating stricter input limits and improved monitoring.
- [Context window overflow: Breaking the barrier (AWS Security Blog)](https://aws.amazon.com/blogs/security/context-window-overflow-breaking-the-barrier/)
- [RAG in the Era of LLMs with 10 Million Token Context Windows (F5 Blog)](https://www.f5.com/company/blog/rag-in-the-era-of-llms-with-10-million-token-context-windows)
- [Guide to Context in LLMs (Symbl.ai)](https://symbl.ai/developers/blog/guide-to-context-in-llms/)
- [Virtual Context: Enhancing Jailbreak Attacks with Special Token Injection (arXiv:2406.19845)](https://arxiv.org/abs/2406.19845)
- [Dialogue Injection Attack: Jailbreaking LLMs through Context Manipulation (arXiv:2503.08195)](https://arxiv.org/abs/2503.08195)
- [Cognitive Overload Attack: Prompt Injection for Long Context (SAIL Lab)](https://sail-lab.org/cognitive-overload-attack-prompt-injection-for-long-context/)
- [LongSafety: Evaluating Long-Context Safety of Large Language Models (arXiv:2502.16971)](https://arxiv.org/abs/2502.16971)
- [Illusions of Relevance: Using Content Injection Attacks to Deceive Retrievers, Rerankers, and LLM Judges (arXiv:2501.18536)](https://arxiv.org/abs/2501.18536)
- [Understanding the Impact of Increasing LLM Context Windows (Meibel)](https://www.meibel.ai/post/understanding-the-impact-of-increasing-llm-context-windows)
- [Analysis of Llama 4's 10 Million Token Context Window Claim (Medium)](https://sandar-ali.medium.com/analysis-of-llama-4s-10-million-token-context-window-claim-9e68ee5abcde)
- [Context Window: The Essential Guide (Nightfall AI)](https://www.nightfall.ai/ai-security-101/context-window)
- [Prompt Injection: What It Is and How to Prevent It (Coralogix)](https://coralogix.com/ai-blog/prompt-injection-attacks-in-llms-what-are-they-and-how-to-prevent-them/)
- [Indirect Prompt Injection: Generative AI’s Greatest Security Flaw (Alan Turing Institute)](https://cetas.turing.ac.uk/publications/indirect-prompt-injection-generative-ais-greatest-security-flaw)
- [Artifacts and Long Context Windows (Weights & Biases)](https://wandb.ai/wandb_ai/artifacts-and-long-context-windows)
