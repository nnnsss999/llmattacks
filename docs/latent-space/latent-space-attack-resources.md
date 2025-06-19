---
title: "Latent Space Attack Resources"
category: "Latent Space"
source_url: ""
date_collected: 2025-06-18
license: "CC-BY-4.0"
---

The references below explore how adversaries manipulate a model's hidden representations. These resources range from obfuscating activations to recovering text from embeddings.

- [Latent Space: The New Attack Vector into Organizations](https://www.apexhq.ai/blog/blog/latent-space-the-new-attack-vector-into-organizations/) – overview of hidden-space threats for RAG and other systems.
- [Obfuscated Activations Bypass LLM Latent-Space Defenses](https://arxiv.org/abs/2412.09565) – demonstrates how modified activations evade latent-space monitors.
- [Latent Adversarial Training Improves Robustness to Persistent Harmful Behaviors in LLMs](https://paperswithcode.com/paper/targeted-latent-adversarial-training-improves) – describes targeted adversarial training on latent vectors.
- [Literature Review: Obfuscated Activations Bypass LLM Latent-Space Defenses](https://www.themoonlight.io/en/review/obfuscated-activations-bypass-llm-latent-space-defenses) – concise summary and analysis of the above paper.
- [Text Embedding Inversion Security for Multilingual Language Models](https://arxiv.org/abs/2401.12192) – recovers prompts from multilingual embeddings.
- [LAGO: Few-shot Crosslingual Embedding Inversion Attacks](https://arxiv.org/abs/2505.16008) – cross-lingual embedding inversion using graph optimization.
- [Extracting Training Data from Large Language Models](https://arxiv.org/abs/2012.07805) – early work on leaking training text via latent representations.
- [Mitigating Privacy Risks in LLM Embeddings from Embedding Inversion](https://arxiv.org/abs/2411.05034) – introduces **Eguard**, a defense that projects embeddings through a transformer network.
- [Information Leakage from Embedding in Large Language Models](https://arxiv.org/abs/2405.11916) – shows how stored embeddings can reveal private text.
- [Latent-Space Jailbreak Optimization](https://www.promptfoo.dev/lm-security-db/vuln/latent-space-jailbreak-optimization-db61455d) – gradient-based search for hidden jailbreak vectors.
- [Can Generalized Adversarial Testing Enable More Rigorous LLM Safety Evaluations?](https://www.alignmentforum.org/posts/m6poxWegJkp8LPpjw/can-generalized-adversarial-testing-enable-more-rigorous-llm) – explores latent-space attacks and few-shot tuning.
- [aengusl/latent-adversarial-training](https://github.com/aengusl/latent-adversarial-training) – implementation of latent adversarial attacks and training.
