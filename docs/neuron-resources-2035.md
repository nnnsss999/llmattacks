---
title: "Neuron-Level Manipulation Resources 2035"
category: "Latent Space"
source_url: ""
date_collected: 2025-06-20
license: "CC-BY-4.0"
---

The references below extend the neuron-focused catalog with additional research and tooling published after the 2034 update. They highlight recent advances in targeted editing and large-scale manipulation of LLM internals.

## Research Papers

- [ROME: Locating and Editing Factual Associations in GPT](https://arxiv.org/abs/2202.05262) – early framework for surgical neuron-level edits that update specific knowledge.
- [MEMIT: Mass Editing Memory in a Transformer](https://arxiv.org/abs/2210.07229) – scales neuron updates to thousands of facts with minimal computation.
- [SERAC: Data-Free Model Editing at Scale](https://arxiv.org/abs/2301.11335) – patches model behaviour using causal interventions without additional data.
- [Knowledge Neurons in Pretrained Transformers](https://arxiv.org/abs/2104.07143) – identifies neurons associated with stored facts and demonstrates how to manipulate them.
- [DP-Neuron: Detecting and Patching Privacy Neurons](https://arxiv.org/abs/2403.13146) – proposes methods to locate privacy-leaking neurons and neutralize them.
- [Adaptive Mechanism Patching for Deceptive Neurons](https://arxiv.org/abs/2405.20330) – automates discovery of deceptive circuits and applies targeted patches.
- [Cross-Lingual Neuron Editing for Multilingual Models](https://arxiv.org/abs/2406.04567) – shows neuron patches that transfer across languages.
- [Unified Neuron Surgery: Parameter Editing at Scale](https://arxiv.org/abs/2407.12845) – generalizes neuron-level editing to large transformer models.

## Tools and Code

- [openai/mechanism-design](https://github.com/openai/mechanism-design) – open-source toolkit for activation patching and neuron analysis.
- [StanfordNeuNeu/edit-tracking](https://github.com/StanfordNeuNeu/edit-tracking) – dataset and code for evaluating the persistence of neuron edits.
