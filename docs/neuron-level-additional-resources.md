---
title: "Additional Neuron-Level Manipulation Resources"
category: "Latent Space"
source_url: ""
date_collected: 2025-06-20
license: "CC-BY-4.0"
---

This supplement aggregates neuron-level manipulation references from across the repository and adds a handful of recent papers, tools, and articles published after the 2035 snapshot. These works highlight current directions in neuron-level attacks, defences, and interpretability.

## Research Papers

- [NeuRel-Attack: Neuron Relearning for Safety Disalignment in Large Language Models](https://arxiv.org/abs/2504.21053) – manipulates safety-related neurons via LoRA to bypass alignment.
- [BAN: Detecting Backdoors Activated by Adversarial Neuron Noise](https://arxiv.org/abs/2405.19928) – identifies hidden triggers by injecting noise into suspect neurons.
- [DEPN: Detecting and Editing Privacy Neurons in Pretrained Language Models](https://arxiv.org/abs/2310.20138) – provides a framework to locate and modify privacy-leaking neurons.
- [BadAgent: Inserting and Activating Backdoor Attacks in LLM Agents](https://arxiv.org/abs/2406.03007) – implants persistent neuron hooks inside autonomous agents.
- [Neuron Empirical Gradient: Discovering and Quantifying Neurons' Global Linear Controllability](https://arxiv.org/abs/2412.18053) – measures how specific neurons influence overall model behaviour.
- [SECNEURON: Reliable and Flexible Abuse Control in Local LLMs via Hybrid Neuron Encryption](https://arxiv.org/abs/2506.05242) – uses neuron-level encryption to prevent malicious modification.
- [Neuron-Level Sequential Editing for Large Language Models](https://arxiv.org/abs/2410.04045) – proposes stepwise neuron modifications to steer model outputs.
- [Reconstructive Neuron Pruning for Backdoor Defense](https://proceedings.mlr.press/v202/li23v.html) – reconstructs benign behaviour after removing compromised neurons.
- [Holes in Latent Space: Topological Signatures Under Adversarial Influence](https://arxiv.org/abs/2505.20435) – analyses neuron-activation patterns with persistent homology to detect backdoor attacks.

## Tools and Code

- [Massive Activations in Large Language Models](https://github.com/locuslab/massive-activations) – explores large-scale neuron activations.
- [Framework for Neuron-Level Interpretability and Robustness in LLMs](https://github.com/kikaymusic/Framework-for-Neuron-Level-Interpretability-and-Robustness-in-LLMs) – toolkit for analysing and hardening critical neurons.
- [THU-KEG/SafetyNeuron](https://github.com/THU-KEG/SafetyNeuron) – dynamic activation patching to test safety neuron behaviour.
- [neelnanda/Attribution-Patching](https://github.com/neelnanda-io/Attribution-Patching) – code for scaling activation patching to industry-scale models.
- [LLM Causal Neuron Attack](https://www.promptfoo.dev/lm-security-db/vuln/llm-causal-neuron-attack-92701d5e) – database entry describing a causal neuron manipulation attack.

## Articles and Links

- [Activation Patching. Illuminating the Hidden Pathways of Language Models](https://medium.com/everyday-ai/activation-patching-d916e7777e66) – practical guide to neuron patching.
- [An Introduction to Representation Engineering – an activation-based paradigm for controlling LLMs](https://www.alignmentforum.org/posts/3ghj8EuKzwD3MQR5G/an-introduction-to-representation-engineering-an-activation) – overview of activation-based steering methods.
- [Language models can explain neurons in language models](https://openai.com/index/language-models-can-explain-neurons-in-language-models/) – blog post discussing neuron interpretation and control.
- [Patchscopes Demo](https://pair.withgoogle.com/explorables/patchscopes/) – interactive environment for neuron patching experiments.
- [Causality Analysis for LLMs](https://casperllm.github.io/) – project applying causal techniques to map dangerous neuron dependencies.
