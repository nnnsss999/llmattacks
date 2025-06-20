---
title: "Neuron-Level Manipulation Resources 2040"
category: "Latent Space"
source_url: ""
date_collected: 2025-06-24
license: "CC-BY-4.0"
---

This page extends the neuron-focused bibliography with research and tooling released after the 2039 update. These references highlight recent neuron-level attacks, defences, and analysis methods for large language models.

## Research Papers

- [Understanding and Mitigating Gender Bias in LLMs via Interpretable Neuron Editing](https://arxiv.org/abs/2501.14457) – proposes interpretable neuron adjustments to reduce gender bias.
- [Identifying Query-Relevant Neurons in Large Language Models for Long-Form Texts](https://doi.org/10.1609/aaai.v39i22.34529) – discovers neurons tied to document retrieval tasks.
- [Exploring Model Editing for LLM-based Aspect-Based Sentiment Classification](https://doi.org/10.1609/aaai.v39i23.34625) – evaluates neuron editing for sentiment models.
- [A Lightweight Method to Disrupt Memorized Sequences in LLM](https://arxiv.org/abs/2502.05159) – disrupts memorized content by selectively modifying neurons.
- [Client-Side Patching Against Backdoor Attacks in Federated Learning](https://doi.org/10.2139/ssrn.5131392) – defends neuron-level backdoors by patching local models.
- [Mitigating Backdoor Attacks in Federated Learning Through Neuron Synaptic Weight Adjustment](https://doi.org/10.1016/j.knosys.2025.113167) – adjusts suspect neuron weights to remove triggers.
- [LLMBD: Backdoor Defense via Large Language Model Paraphrasing and Data Voting in NLP](https://doi.org/10.2139/ssrn.5131766) – cleans backdoors by paraphrasing data and comparing neuron activations.
- [Two Sides of the Same Coin: Learning the Backdoor to Remove the Backdoor](https://doi.org/10.1609/aaai.v39i21.34441) – trains auxiliary models to detect and neutralize malicious neurons.
- [Stealthy Backdoor Attack against Federated Learning through Frequency Domain by Backdoor Neuron Constraint and Model Camouflage](https://doi.org/10.1109/jetcas.2024.3450527) – implants backdoors using frequency-domain neuron constraints.

## Tools and Code

- [ECNU-ICALK/MELO](https://github.com/ECNU-ICALK/MELO) – implementation of neuron-indexed dynamic LoRA for model editing.
- [opanhw/MM_Neurons](https://github.com/opanhw/MM_Neurons) – code for finding and editing multimodal neurons in transformers.
- [jianghoucheng/NSE](https://github.com/jianghoucheng/NSE) – reference implementation for Neuron-Level Sequential Editing.
- [ruchikachavhan/concept-prune](https://github.com/ruchikachavhan/concept-prune) – demonstrates concept editing via skilled neuron pruning.
- [Butanium/llm-lang-agnostic](https://github.com/Butanium/llm-lang-agnostic) – reproduces activation patching for language-agnostic neuron discovery.
