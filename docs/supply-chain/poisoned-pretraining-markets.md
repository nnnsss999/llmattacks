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
- [Poisoning Web-Scale Training Datasets is Practical](https://arxiv.org/abs/2302.10149) demonstrates the feasibility of corrupting large public corpora.
- [Persistent Pre-Training Poisoning of LLMs | SPY Lab](https://spylab.ai/blog/poisoning-pretraining/) summarizes research findings and mitigations.
- [Pretraining-Poisoning](https://github.com/facebookresearch/pretraining-poisoning) provides code for replicating poisoning experiments.
- [Data Poisoning attacks on Enterprise LLM applications](https://www.giskard.ai/knowledge/data-poisoning-attacks-on-enterprise-llm-applications-ai-risks-detection-and-prevention) offers detection advice for commercial teams.
- [OWASP Top 10 for LLM Applications 2025: Data and Model Poisoning](https://www.checkpoint.com/cyber-hub/what-is-llm-security/data-and-model-poisoning/) covers common supply chain pitfalls.
- [Why Google’s Researchers are Intentionally Poisoning Datasets](https://lightning.ai/pages/community/why-googles-researchers-are-intentionally-poisoning-datasets-and-more/) explains deliberate poisoning for evaluation.
- [NDSS 2023 Poster: Foundation Model Poisoning](https://www.ndss-symposium.org/wp-content/uploads/2023/02/NDSS2023Poster_paper_4383.pdf) presents early insights into pre-training attacks.

Use these references to strengthen vetting processes for any third-party corpus or weights incorporated into your models.
