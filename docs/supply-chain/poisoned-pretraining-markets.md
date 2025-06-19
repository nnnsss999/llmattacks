---
title: "Poisoned Pre-Training Data Markets"
category: "Supply Chain"
date_collected: 2025-06-18
license: "CC-BY-4.0"
---

Adversaries increasingly target public and commercial dataset exchanges. By offering seemingly useful corpora that secretly contain malicious prompts or code, attackers can backdoor or bias large language models before fine-tuning begins. The resources below document real cases and defense guidance.

- [Persistent Pre-training Poisoning of LLMs](https://arxiv.org/abs/2410.13722) — shows how small poisoned subsets inserted during pre-training can persist through downstream fine-tuning.
- [Medical Large Language Models are Vulnerable to Data-Poisoning Attacks](https://www.nature.com/articles/s41591-024-03445-1) discusses the impact of tainted medical datasets on specialized LLMs.
- [When open source bites back: Data and model poisoning](https://www.sonatype.com/blog/the-owasp-llm-top-10-and-sonatype-data-and-model-poisoning) explains how supply chain controls can mitigate poisoned corpora.
- [Training Data Poisoning](https://www.lakera.ai/blog/training-data-poisoning) provides an overview of modern data manipulation techniques.
- [Data Poisoning 101 for LLM Evaluation](https://www.promptfoo.dev/blog/data-poisoning/) surveys methods to corrupt datasets used for benchmarking.
- [OWASP GenAI Supply Chain Risk](https://genai.owasp.org/llmrisk/llm032025-supply-chain/) offers classification guidance for poisoned dataset marketplaces.

Use these references to strengthen vetting processes for any third-party corpus or weights incorporated into your models.
