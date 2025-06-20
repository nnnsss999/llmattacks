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
- [Long-Context LLMs and RAG (deepset Blog)](https://www.deepset.ai/blog/long-context-llms-rag)

- [Membership Inference Attack against Long-Context Large Language Models (arXiv:2411.11424)](https://arxiv.org/abs/2411.11424)
- [Context is the Key: Backdoor Attacks for In-Context Learning with Vision Transformers (arXiv:2409.04142)](https://arxiv.org/abs/2409.04142)
- [Exploiting Long Context Windows for Harmful Outputs (Prompt Engineering Institute)](https://promptengineering.org/exploiting-long-context-windows-for-harmful-outputs/)
- [Anthropic: Large context LLMs vulnerable to many-shot jailbreak (DailyAI)](https://dailyai.com/2024/04/anthropic-large-context-llms-vulnerable-to-many-shot-jailbreak/)
- [Many-shot jailbreaking - Anthropic](https://www.anthropic.com/research/many-shot-jailbreaking)
- [Many Shot Jailbreaking—analysis by Rylan Schaeffer](http://rylanschaeffer.github.io/content/research/2024_arxiv_many_shot_jailbreaking/main.html)
- [LLM Security: Vulnerabilities, Attacks, Defenses, and Countermeasures](https://arxiv.org/pdf/2505.01177)
- [greshake/llm-security: New ways of breaking app-integrated LLMs (GitHub)](https://github.com/greshake/llm-security)
- [How to red team RAG applications (Promptfoo)](https://www.promptfoo.dev/docs/red-team/rag/)
- [Context windows – Anthropic Documentation](https://docs.anthropic.com/en/docs/build-with-claude/context-windows)
- [Context Injection Attacks on Large Language Models (arXiv:2405.20234)](https://arxiv.org/abs/2405.20234)
- [Evaluating Large Language Models in Vulnerability Detection Under Variable Context Windows (arXiv:2502.00064)](https://arxiv.org/abs/2502.00064)
- [Token-Efficient Prompt Injection Attack: Provoking Cessation in LLM Reasoning via Adaptive Token Compression (arXiv:2504.20493)](https://arxiv.org/abs/2504.20493)
- [Overflow Prevention Enhances Long-Context Recurrent LLMs (arXiv:2505.07793)](https://arxiv.org/abs/2505.07793)
- [Long Context vs. RAG for LLMs: An Evaluation and Revisits (arXiv:2501.01880)](https://arxiv.org/abs/2501.01880)
- [What is a long context window? Google DeepMind engineers explain](https://blog.google/technology/ai/long-context-window-ai-models/)
- [LLMs with Largest Context Windows (Codingscape Blog)](https://codingscape.com/blog/llms-with-largest-context-windows)
- [Long-context LLMs Struggle with Long In-context Learning (OpenReview)](https://openreview.net/forum?id=Cw2xlg0e46)
- [LongWriter: Unleashing 10,000+ Word Generation from Long Context LLMs (OpenReview)](https://openreview.net/forum?id=kQ5s9Yh0WI)
- [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization (OpenReview)](https://openreview.net/forum?id=qTrEq31Shm)
- [Retrieval meets Long Context Large Language Models (OpenReview)](https://openreview.net/forum?id=xw5nxFWMlo)
- [InfLLM: Training-Free Long-Context Extrapolation for LLMs with an Efficient Context Memory (OpenReview)](https://openreview.net/forum?id=bTHFrqhASY)
- [LLM Context Window Threats and Mitigations (BlackBerry Blog)](https://blogs.blackberry.com/en/2024/06/large-language-model-context-window-threats)
- [Long Context LLMs: Tools and Challenges (HuggingFace Blog)](https://huggingface.co/blog/long-context-llms)
- [Large Context Window LLMs - Developer's Perspective (NVIDIA Blog)](https://developer.nvidia.com/blog/large-context-window-llms)
- [Gemini 1.5 Pro's Million Token Context Window (Google Cloud Blog)](https://cloud.google.com/blog/products/ai-machine-learning/gemini-1-5-pro-context-window)
- [Securing Long Context Windows in LLM Applications (Microsoft Tech Community)](https://techcommunity.microsoft.com/t5/security-compliance-and-identity/long-context-windows-in-llms-security/ba-p/4040000)
- [Token Smuggling Attack Explained (Prompt Security Blog)](https://www.promptsecurity.com/blog/token-smuggling-explained)
- [Token Smuggling for Prompt Injection (Lakera AI)](https://www.lakera.ai/blog/token-smuggling)
- [Token-Smuggling: The Hidden Threat to A.I. and GPT Models (Hashdork)](https://hashdork.com/token-smuggling/)
- [AI Guardrail Vulnerability Exposed: How Emoji Smuggling Bypasses LLM Safety Filters (WindowsForum)](https://windowsforum.com/threads/ai-guardrail-vulnerability-exposed-how-emoji-smuggling-bypasses-llm-safety-filters.365061/)
- [Context Overflow Attack (Learn Prompting)](https://learnprompting.org/docs/prompt_hacking/offensive_measures/context_overflow_attack)
- [Context Overflow: Conditional Prompt Injection (ContextOverflow Newsletter)](https://contextoverflow.com/p/context-overflow-attack)
- [LLM Flowbreaking Attacks (Knostic AI Blog)](https://www.knostic.ai/blog/flowbreaking)
- [LLM Scope Violation: Expanding Attack Surface (Aim Security)](https://www.aim.security/blog/llm-scope-violation)
- [Zero-click Copilot flaw reveals LLM Scope Violation (CSO Online)](https://www.csoonline.com/article/4005965/first-ever-zero-click-attack-targets-microsoft-365-copilot.html)
- [Context Degradation Syndrome: When Large Language Models Lose the Plot](https://jameshoward.us/2024/11/26/context-degradation-syndrome-when-large-language-models-lose-the-plot)
- [Understanding LLM context windows: tokens, attention, and challenges (IBM Think Blog)](https://www.ibm.com/think/topics/context-window)
- [Many-shot jailbreaking: A new LLM vulnerability (Prompt Security Blog)](https://www.prompt.security/blog/many-shot-jailbreaking-a-new-llm-vulnerability)
- [LLM System Prompt Leakage: Understanding the Hidden Threat (VirtualCyberLabs)](https://virtualcyberlabs.com/llm-system-prompt-leakage/)
- [Why Do LLMs Forget? Context Window Challenges, Risks (LinkedIn)](https://www.linkedin.com/pulse/magic-madness-context-windows-your-llms-memory-explained-katira-kixgf/)
- [LLM Security Guide - Understanding the Risks of Prompt Injections and Other Attacks (MLOps Audits)](https://www.mlopsaudits.com/blog/llm-security-guide-understanding-the-risks-of-prompt-injections-and-other-attacks-on-large-language-models)
- [Tokens and Context Windows in LLMs (GeeksforGeeks)](https://www.geeksforgeeks.org/artificial-intelligence/tokens-and-context-windows-in-llms/)
- [LooGLE: Can Long-Context Language Models Understand Long Contexts? (arXiv:2311.04939)](https://arxiv.org/abs/2311.04939)
- [LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models (arXiv:2309.12307)](https://arxiv.org/abs/2309.12307)
- [Augmenting Language Models with Long-Term Memory (arXiv:2306.07174)](https://arxiv.org/abs/2306.07174)
- [Why Use Retrieval Instead of Larger Context? (Pinecone Blog)](https://www.pinecone.io/blog/why-use-retrieval-instead-of-larger-context/)
- [DeepSpeed Blog on Long-Context Transformers](https://www.deepspeed.ai/2024/03/18/long-context-transformers/)

- [Zero-click AI data leak flaw uncovered in Microsoft 365 Copilot (BleepingComputer)](https://www.bleepingcomputer.com/news/security/zero-click-ai-data-leak-flaw-uncovered-in-microsoft-365-copilot/)
- [How to Overcome LLM Context Window Limitations (Medium)](https://medium.com/the-business-of-ai/how-to-overcome-llm-context-window-limitations-dc94f4cc6509)
- [The Double-Edged Sword of Massive Context Windows in Modern LLMs (Medium)](https://medium.com/@wmechem/the-double-edged-sword-of-massive-context-windows-in-modern-llms-cd3dbe36c954)
- [LLM Prompt Best Practices – Large Context Windows (Winder AI)](https://winder.ai/llm-prompt-best-practices-large-context-windows/)
- [Beyond the Boundaries of Code: The Quest for Longer Context Windows in Large Language Models (LLM Reporter)](https://www.llmreporter.com/posts/beyond-the-boundaries-of-code-the-quest-for-longer-context-windows-in-large-language-models/)
- [Do Enormous LLM Context Windows Spell the End of RAG? (The New Stack)](https://thenewstack.io/do-enormous-llm-context-windows-spell-the-end-of-rag/)
- [Evaluating Long Context Lengths in LLMs: Challenges and Benchmarks (Medium)](https://onnyunhui.medium.com/evaluating-long-context-lengths-in-llms-challenges-and-benchmarks-ef77a220d34d)
