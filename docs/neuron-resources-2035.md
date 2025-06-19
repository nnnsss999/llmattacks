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
The references below extend the neuron-focused bibliography with papers and articles published after the 2034 update. They highlight recent work on neuron-level backdoors, activation patching, and causal analysis in large language models.

## Research Papers

- [BAN: Detecting Backdoors Activated by Adversarial Neuron Noise](https://arxiv.org/abs/2405.19928) – identifies hidden triggers by injecting noise into suspect neurons.
- [Instruction Backdoor Attacks Against Customized LLMs](https://www.usenix.org/conference/usenixsecurity24/presentation/zhang-rui) – demonstrates instruction-tuned neuron backdoors at scale.
- [BadAgent: Inserting and Activating Backdoor Attacks in LLM Agents](https://arxiv.org/abs/2406.03007) – implants persistent neuron hooks inside autonomous agents.
- [SPIRIT: Patching Speech Language Models against Jailbreak Attacks](https://arxiv.org/abs/2505.13541) – patches neuron activations in speech models to resist jailbreak prompts.
- [SECNEURON: Reliable and Flexible Abuse Control in Local LLMs via Hybrid Neuron Encryption](https://arxiv.org/abs/2506.05242) – proposes neuron-level encryption to prevent malicious modifications.

## Tools and Code

- [Massive Activations in Large Language Models](https://github.com/locuslab/massive-activations) – code exploring large-scale neuron activations.
- [Framework for Neuron-Level Interpretability and Robustness in LLMs](https://github.com/kikaymusic/Framework-for-Neuron-Level-Interpretability-and-Robustness-in-LLMs) – tools for analyzing and hardening critical neurons.
- [LLM Causal Neuron Attack](https://www.promptfoo.dev/lm-security-db/vuln/llm-causal-neuron-attack-92701d5e) – database entry describing an attack that manipulates causal neuron pathways.

## Articles and Links

- [Activation Patching. Illuminating the Hidden Pathways of Language Models](https://medium.com/everyday-ai/activation-patching-d916e7777e66) – blog post explaining practical neuron patching.
- [An Introduction to Representation Engineering – an activation-based paradigm for controlling LLMs](https://www.alignmentforum.org/posts/3ghj8EuKzwD3MQR5G/an-introduction-to-representation-engineering-an-activation) – overview of activation-based steering methods.
- [How to Think About Activation Patching](https://www.alignmentforum.org/posts/xh85KbTFhbCz7taD4/how-to-think-about-activation-patching) – discusses conceptual frameworks for neuron patching.
- [Explaining Neurons in LLMs with LLMs](https://medium.com/@ashkangolgoon/explaining-neurons-in-llms-with-llms-e541c233bbac) – explores using LLMs themselves to interpret neuron behaviour.
- [Causality Analysis for LLMs](https://casperllm.github.io/) – project applying causal techniques to map dangerous neuron dependencies.
