---
title: "Token-Level Attack Resources"
category: "Tokenization"
source_url: ""
date_collected: 2025-06-19
license: "CC-BY-4.0"
---

The following references provide further background on tokenization-based attacks against large language models (LLMs). They expand on the TokenBreak example already included in this catalog and highlight a range of token-level manipulation techniques and research efforts.

- [Limitations of Data Tokenization in NLP](https://www.linkedin.com/pulse/limitations-data-tokenization-pranav-rupani-3vcmf) - Overview of token segmentation weaknesses that can lead to filter bypasses.
- [The TokenBreak Attack](https://hiddenlayer.com/innovation-hub/the-tokenbreak-attack/) - Demonstrates how single-character changes defeat keyword-based defenses.
- [New TokenBreak Attack Bypasses AI Moderation](https://thehackernews.com/2025/06/new-tokenbreak-attack-bypasses-ai.html) - Coverage of real-world TokenBreak exploits.
- [This Cyberattack Lets Hackers Crack AI Models with One Character](https://www.techradar.com/pro/security/this-cyberattack-lets-hackers-crack-ai-models-just-by-changing-a-single-character) - TechRadar report on TokenBreak.
- [Emoji-based Adversarial Attacks on LLMs](https://www.semanticscholar.org/paper/5b539b4e1b9f677301ac815d41677fb4ec040f4b) - Research showing how emoji insertion can systematically evade token filters.
- [Unicode Encoding Attacks](https://owasp.org/www-community/attacks/Unicode_Encoding) - OWASP reference on using unusual byte sequences to confuse tokenizers.
- [Special Tokens for Jailbreak Prompt Boosting](https://aclanthology.org/2024.findings-emnlp.692/) - EMNLP 2024 paper describing reserved-token strategies for jailbreaks.
- [Enhancing Prompt Attacks with Reserved Tokens](https://arxiv.org/abs/2406.19845) - Follow-up work exploring special token injection in depth.
- [JailMine: Automated Token-Level Manipulation for Jailbreaking](https://arxiv.org/abs/2505.02101) - Efficient approach to discovering token-level jailbreak prompts.
- [Byte-Level Universal Triggers](https://www.techradar.com/pro/security/this-cyberattack-lets-hackers-crack-ai-models-just-by-changing-a-single-character) - Typo trojans using rare Unicode bytes to flip model behaviour.
- [OpenAI tiktoken Repository](https://github.com/openai/tiktoken) - Source code for common tokenizers used in many LLM systems.
- [TokenBreak: Bypassing Text Classification Models Through Token Manipulation](https://arxiv.org/abs/2506.07948) - ArXiv paper providing an in-depth analysis of the TokenBreak technique.
- [Lockpicking LLMs: A Logit-Based Jailbreak Using Token-level Manipulation](https://arxiv.org/abs/2405.13068) - Gradient-guided jailbreak that directly modifies token logits.
- [A Peek into Token Bias: Large Language Models Are Not Yet Genuine Reasoners](https://arxiv.org/abs/2406.11050) - Study exposing bias effects that enable token-level exploits.
- [Emoji Attack: Enhancing Jailbreak Attacks Against Judge LLM Detection](https://openreview.net/forum?id=Q0rKYiVEZq) - Explores how emoji sequences bypass safety detectors.
- [Tokenization Matters! Degrading Large Language Models through Challenging Their Tokenization](https://openreview.net/forum?id=grO9s3lESV) - Shows that unexpected tokenization can degrade and subvert models.
- [DeSparsify: Adversarial Attack Against Token Sparsification Mechanisms](https://openreview.net/forum?id=D4yRz3s7UL) - Attack targeting tokenizer sparsification defences.
- [BOOST: Enhanced Jailbreak of Large Language Model via Slient eos Tokens](https://openreview.net/forum?id=JqKh7FLUw1) - Describes injecting hidden end-of-sequence tokens for jailbreaking.
- [Universal Adversarial Triggers Are Not Universal](https://openreview.net/forum?id=sKlMMzp4QI) - Discusses limits of universal token triggers and how they relate to LLM attacks.

- [Defining The Token-level AI Jailbreaking Techniques](https://briandcolwell.com/defining-the-token-level-ai-jailbreaking-techniques/) - Blog post summarizing token-level jailbreak methods and optimizations.
- [The Silent Threat: When Tokens Become Weapons](https://blog.ailab.sh/2024/11/the-silent-threat-when-tokens-become.html) - Detailed look at tokenization vulnerabilities in LLMs.
- [Understanding Token Splitting Attacks in LLMs](https://www.proventra-ai.com/blog/understanding-token-splitting-attacks-llms) - Walkthrough of token-splitting to insert malicious content.
- [Some Notes on Adversarial Attacks on LLMs](https://cybernetist.com/2024/09/23/some-notes-on-adversarial-attacks-on-llms/) - Practitioner notes covering token-level manipulations.
- [Beware of Special Token Injections in LLMs](https://medium.com/@_jeremy_/beware-of-special-token-injections-in-llms-a-new-form-of-sql-injection-like-attack-d0bceb8bda94) - Medium article describing reserved-token injection risks.
- [The Subtle Art of Jailbreaking LLMs](https://andpalmier.com/posts/jailbreaking-llms/) - High-level guide to jailbreak strategies including token-focused tricks.
- [Novel TokenBreak Attack Method Can Bypass LLM Security Features](https://securityboulevard.com/2025/06/novel-tokenbreak-attack-method-can-bypass-llm-security-features/) - Security Boulevard's analysis of a TokenBreak variant.
- [TokenBreak Attack - Single Character Bypass Defeats LLM Safety](https://www.cyberkendra.com/2025/06/tokenbreak-attack-single-character.html) - Explanation of the single-character trick.
- [Simple Typo Breaks AI Safety Via TokenBreak](https://cybermaterial.com/simple-typo-breaks-ai-safety-via-tokenbreak/) - Demonstration of the bypass in practice.
- [TokenBreak Exploit Tricks AI Models Using Minimal Input Changes](https://gbhackers.com/tokenbreak-exploit-tricks-ai-models/) - Step-by-step demonstration of the exploit.
- [TokenBreak Attack Bypasses AI Models with a Single Character](https://cyberpress.org/tokenbreak-attack-bypasses-ai-models/) - Security blog summary of the weakness.
- [TokenBreak Attack Bypasses LLM Protective Guardrails](https://www.spartechsoftware.com/cybersecurity-news/new-tokenbreak-attack-bypasses-llm-protective-guardrails/) - Coverage of defensive shortcomings.
- [Emoji Jailbreaks: Are Your AI Models Vulnerable?](https://medium.com/google-cloud/emoji-jailbreaks-b3b5b295f38b) - Google Cloud article on emoji-based bypasses.
- [Hackers Can Bypass Microsoft, Nvidia, & Meta AI Filters With a Simple Emoji](https://cybersecuritynews.com/hackers-can-bypass-microsoft-nvidia-meta-ai-filters/) - News report on real-world emoji attacks.
- [AI Guardrail Vulnerability Exposed: How Emoji Smuggling Bypasses LLM Safety Filters](https://windowsforum.com/threads/ai-guardrail-vulnerability-exposed-how-emoji-smuggling-bypasses-llm-safety-filters.365061/) - Discussion of smuggling vulnerabilities.
- [Understanding Emoji AI Hacking: How Unicode Threatens AI](https://www.geeky-gadgets.com/emoji-exploits-in-ai-security/) - Technical overview of emoji exploits.
- [The Emoji Attack: A New Threat Vector in AI Safety Evaluation](https://medium.com/@bhargavaganti/the-emoji-attack-a-new-threat-vector-in-ai-safety-evaluation-6ab07ff4f107) - Analysis of emoji sequences in jailbreaks.
- [The Hidden Dangers of Adversarial Tokenization](https://medium.com/data-science-collective/the-hidden-dangers-of-adversarial-tokenization-how-token-splitting-bypasses-ai-safeguards-4e3b651f6a22) - In-depth look at token-splitting risks.
- [Adversarial Attacks on LLMs | Lil'Log](https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/)
- [A Deep Dive into LLM Attacks and Countermeasures](https://medium.com/@nirvana.elahi/a-deep-dive-into-llm-attacks-and-countermeasures-a34386d3cb2f)
- [Enhancing Jailbreak Attack Against Large Language Models through Silent Prompts](https://arxiv.org/abs/2405.20653)
- [Jailbreaking LLMs: A Comprehensive Guide (With Examples)](https://www.promptfoo.dev/blog/how-to-jailbreak-llms/)
