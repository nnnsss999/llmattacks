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
