---
title: "Neuron-Level Manipulation Resources"
category: "Latent Space"
source_url: ""
date_collected: 2025-06-19
license: "CC-BY-4.0"
---

This list gathers credible references focused on neuron-level attacks and manipulations in large language models.


## Research Papers

- [Finding Safety Neurons in Large Language Models](https://arxiv.org/abs/2406.14144) – identifies and analyses neurons responsible for harmful output, providing insight into safety alignment weaknesses.
- [Understanding and Enhancing Safety Mechanisms of LLMs via Safety-Specific Neuron](https://openreview.net/forum?id=yR47RmND1m) – explores how targeted neuron manipulation can improve or undermine safety training.
- [Obfuscated Activations Bypass LLM Latent-Space Defenses](https://arxiv.org/abs/2412.09565) – shows how adversaries can hide malicious behaviour by altering neuron activations.
- [Autodan: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models](https://arxiv.org/abs/2310.04451) – demonstrates methods for evading safety filters through neuron-level adjustments.
- [Piccolo: Exposing Complex Backdoors in NLP Transformer Models](https://arxiv.org/abs/2202.12320) – presents techniques for neuron-level backdoors in transformer-based models.
- [NLSR: Neuron-Level Safety Realignment of Large Language Models Against Harmful Fine-Tuning](https://arxiv.org/abs/2412.12497) – proposes a training-free framework that restores safety-critical neurons when fine-tuning introduces malicious behaviour.
- [Holes in Latent Space: Topological Signatures Under Adversarial Influence](https://arxiv.org/abs/2505.20435) – analyzes neuron-level activation patterns with persistent homology to detect backdoor and prompt-injection attacks.
- [BDefects4NN: A Backdoor Defect Database for Controlled Localization Studies in Neural Networks](https://arxiv.org/abs/2412.00746) – curates neuron-level backdoor examples to support systematic evaluation.
- [Neuron-level LLM Patching for Code Generation](https://www.semanticscholar.org/paper/Neuron-level-LLM-Patching-for-Code-Generation-Gu-Chen/d500c6d85d8de0a17761bc26d863c72f7106402e) – demonstrates how editing specific neurons can change code-generation behaviour.
- [Fight Perturbations With Perturbations: Defending Adversarial Attacks Using Neuron-level Inverse Perturbation](https://ieeexplore.ieee.org/abstract/document/10640242) – introduces a defense that adjusts neuron activations based on influence scores.

## Tools and Code

- [THU-KEG/SafetyNeuron](https://github.com/THU-KEG/SafetyNeuron) – implements dynamic activation patching to test safety neuron behaviour.
- [Neuronpedia](https://www.neuronpedia.org/) – provides an interactive interface for exploring and editing neuron activations across multiple models.

## Concepts

- **Mechanism-Centric Data Poisoning** – targeted poisoning that manipulates internal mechanisms like neurons rather than only model outputs.
- **Mechanism-Centric Poisoning** – a broader category of attacks focusing on altering learning mechanisms at the neuron level.

