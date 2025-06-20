---
title: "Latent Space Attack Resources 2038"
category: "Latent Space"
source_url: ""
date_collected: 2025-07-15
license: "CC-BY-4.0"
---

The references below add further studies on latent-space exploits and defenses published after the [2037 update](latent-space-resources-2037.md). They focus on attention hijacking, diffusion-based backdoors, and other hidden-state manipulations.

- [Universal Jailbreak Suffixes Are Strong Attention Hijackers](https://arxiv.org/abs/2506.12880) – shows how optimized suffixes can seize control of latent attention.
- [Attention Hijackers: Detect and Disentangle Attention Hijacking in LVLMs](https://arxiv.org/abs/2503.08216) – framework for spotting malicious attention patterns.
- [ShadowCoT: Cognitive Hijacking for Stealthy Reasoning Backdoors in LLMs](https://arxiv.org/abs/2504.05605) – implants reasoning triggers that operate in hidden layers.
- [Pseudo-Conversation Injection for LLM Goal Hijacking](https://arxiv.org/abs/2410.23678) – demonstrates stealthy latent backdoors through fake dialogues.
- [Dynamic Attention Analysis for Backdoor Detection in Text-to-Image Diffusion Models](https://arxiv.org/abs/2504.20518) – analyzes diffusion-model activations for covert triggers.
- [Backdoor Attack Against Vision Transformers via Attention Gradient-Based Image Erosion](https://doi.org/10.1109/globecom52923.2024.10901210) – erodes attention maps to hide malicious content.
- [Attention-Imperceptible Backdoor Attacks on Vision Transformers](https://ojs.aaai.org/index.php/AAAI/article/view/32889) – manipulates hidden states without affecting observed tokens.
- [Attention-Guided Backdoor Attacks against Transformers](https://openreview.net/forum?id=pNZkow3k3BH) – uses attention guidance to craft persistent latent triggers.
- [Backdoor Attacks in Token Selection of Attention Mechanism](https://icml.cc/media/icml-2025/Slides/44868.pdf) – reveals how token-level edits corrupt hidden representations.
- [Aliasing Black Box Adversarial Attack with Joint Self-Attention](https://www.sciencedirect.com/science/article/pii/S0957417422021285) – cross-modal attack relying on latent aliasing.
- [AttentionDrag: Exploiting Latent Correlation Knowledge in Pre-trained Diffusion Models for Image Editing](https://arxiv.org/abs/2506.13301) – leverages hidden correlations to modify generated images.
