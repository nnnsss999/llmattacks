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
- [LLM Embedding Attack Repository](https://github.com/SchwinnL/LLM_Embedding_Attack) – toolkit for crafting and evaluating embedding-based adversarial examples.
- [Membership Inference Attacks on Large-Scale Models: A Survey](https://arxiv.org/abs/2503.19338) – overview of attacks that query latent representations to detect training membership.
- [Attacking Large Language Models with Projected Gradient Descent](https://arxiv.org/abs/2402.09154) – demonstrates gradient-descent optimization directly in latent space.
- [TAG: Gradient Attack on Transformer-based Language Models](https://aclanthology.org/2021.findings-emnlp.305/) – early work on gradient attacks targeting text transformers.
- [Gradient-based Adversarial Attacks against Text Transformers](https://blogs.night-wolf.io/gradient-based-adversarial-attacks-against-text-transformers) – blog post exploring hidden-state manipulations.
- [Uncovering Gradient Inversion Risks in Practical Language Model Training](https://dl.acm.org/doi/abs/10.1145/3658644.3690292) – shows how gradient updates can leak private training data.
- [PoisonedRAG Dataset](https://github.com/sleeepeer/PoisonedRAG) – resources for poisoning retrieval-augmented generation via manipulated embeddings.
- [LLM Vector and Embedding Risks and How to Defend Against Them](https://www.sonatype.com/blog/llm-vector-and-embedding-risks-and-how-to-defend-against-them) – analysis of embedding threats and mitigation strategies.
