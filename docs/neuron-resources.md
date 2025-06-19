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

## Tools and Code

- [THU-KEG/SafetyNeuron](https://github.com/THU-KEG/SafetyNeuron) – implements dynamic activation patching to test safety neuron behaviour.

## Concepts

- **Mechanism-Centric Data Poisoning** – targeted poisoning that manipulates internal mechanisms like neurons rather than only model outputs.
- **Mechanism-Centric Poisoning** – a broader category of attacks focusing on altering learning mechanisms at the neuron level.

