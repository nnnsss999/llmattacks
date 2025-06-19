---
title: "Neuron-Level Manipulation Resources 2029"
category: "Latent Space"
source_url: ""
date_collected: 2025-06-19
license: "CC-BY-4.0"
---

The references below continue the catalog of neuron-level attacks and editing techniques in large language models. They build upon [neuron-resources-2028.md](neuron-resources-2028.md) with newer research.

## Research Papers

- [NeuRel-Attack: Neuron Relearning for Safety Disalignment in Large Language Models](https://arxiv.org/abs/2504.21053) – manipulates safety-related neurons via LoRA fine-tuning to bypass alignment.
- [DEPN: Detecting and Editing Privacy Neurons in Pretrained Language Models](https://arxiv.org/abs/2310.20138) – proposes a detector for privacy-leaking neurons and methods to edit them.
- [LLM Surgery: Efficient Knowledge Unlearning and Editing in Large Language Models](https://arxiv.org/abs/2312.17244) – removes or inserts knowledge through targeted parameter updates.
- [Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing](https://aclanthology.org/2025.acl-long.533) – demonstrates behaviour changes by editing small subsets of model weights.
- [Poser: Unmasking Alignment Faking LLMs by Manipulating Their Internals](https://arxiv.org/abs/2405.05466) – shows how hidden neuron states enable deceptive compliance.
- [Can Neuron Activation be Predicted? A New Lens for Analyzing Transformers](https://openreview.net/forum?id=KcR3RKphtz) – explores predictability of individual neurons to expose weaknesses.
- [AtP\*: An Efficient and Scalable Method for Localizing LLM Behaviour to Model Components](https://arxiv.org/abs/2505.09382) – accelerates activation patching for large models.
- [BadActs: A Universal Backdoor Defense in the Activation Space](https://aclanthology.org/2024.findings-acl.123) – suppresses malicious neurons by perturbing activations.
- [Neuron Shapley: Discovering the Responsible Neurons](https://proceedings.neurips.cc/paper_files/paper/2020/hash/3ba6b1fa49c9cc6b223ae9859e8f051f-Abstract.html) – assigns contribution scores to neurons to identify attack vectors.

## Tools and Code

- [thunlp/NeuBA](https://github.com/thunlp/NeuBA) – implementation for universal neuron-level backdoor attacks.
- [chrisliu298/awesome-llm-unlearning](https://github.com/chrisliu298/awesome-llm-unlearning) – curated list including resources on neuron-level editing and unlearning.
- [neelnanda/Attribution-Patching](https://github.com/neelnanda-io/Attribution-Patching) – code for scaling activation patching to industry-scale models.
