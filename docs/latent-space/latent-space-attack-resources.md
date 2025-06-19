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
- [Tapping the Mind of LLMs: Latent Space Activation](https://www.richwashburn.com/post/tapping-the-mind-of-llms-latent-space-activation) – overview of manipulating hidden activations.
- [Dodging Latent Space Detectors](https://www.cognitiverevolution.ai/dodging-latent-space-detectors-obfuscated-activation-attacks-with-luke-bailey-erik-jenner-an/) – blog post summarizing obfuscated activation attacks.
- [Generating Adversarial Attacks in the Latent Space](https://openaccess.thecvf.com/content/CVPR2023W/GCV/papers/Shukla_Generating_Adversarial_Attacks_in_the_Latent_Space_CVPRW_2023_paper.pdf) – CVPR 2023 workshop paper on latent perturbations.
- [Latent Space Mysteries in Large Language Models](https://medium.com/@eugenesh4work/latent-space-mysteries-in-large-language-models-2d276c6d0708) – high-level discussion of latent representations.
- [A Guide to Mitigating LLM08:2025 Vector and Embedding Weaknesses](https://www.securityium.com/a-guide-to-mitigating-llm082025-vector-and-embedding-weaknesses/) – defensive measures for embedding attacks.
- [There and Back Again: An Embedding Attack Journey](https://ironcorelabs.com/blog/2024/text-embedding-privacy-risks/) – explains embedding inversion threats.
- [LLM-PBE: Assessing Data Privacy in Large Language Models](https://www.vldb.org/pvldb/vol17/p3201-li.pdf) – framework analyzing privacy leakage via embeddings.
- [Transferable Embedding Inversion Attack](https://aclanthology.org/2024.acl-long.230/) – cross-model inversion attack demonstration.
- [Understanding Privacy Risks of Embeddings Induced by LLMs](https://arxiv.org/html/2404.16587v1) – examines extraction risk from open-source embeddings.
- [Security and Privacy Challenges of Large Language Models: A Survey](https://dl.acm.org/doi/full/10.1145/3712001) – comprehensive overview including latent-space threats.
