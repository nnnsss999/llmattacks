---
title: "Embedding Inversion Attacks"
category: "Latent Space"
source_url: "https://arxiv.org/abs/2401.12192"
date_collected: 2025-06-18
license: "Fair Use"
---

Embedding inversion seeks to reconstruct input text from its vector representation.
Recent work demonstrates multilingual models are vulnerable, allowing recovery of prompts across languages [^1].
Few-shot crosslingual methods such as **LAGO** further reduce the sample complexity [^2].
Earlier research extracted training data from large models via output probability leakage [^3].

[^1]: [Text Embedding Inversion Security for Multilingual Language Models](https://arxiv.org/abs/2401.12192).
[^2]: [LAGO: Few-shot Crosslingual Embedding Inversion Attacks](https://arxiv.org/abs/2505.16008).
[^3]: [Extracting Training Data from Large Language Models](https://arxiv.org/abs/2012.07805).
