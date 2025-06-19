---
title: "Neuron-Level Manipulation Resources 2033"
category: "Latent Space"
source_url: ""
date_collected: 2025-06-19
license: "CC-BY-4.0"
---

The references below compile recent work on neuron-level attacks and defenses in large language models published after the 2032 snapshot. They highlight backdoor mitigation, neuron attribution, and advanced editing techniques.

## Research Papers

- [Gemma Scope: Open Sparse Autoencoders Everywhere All At Once on Gemma 2](https://arxiv.org/abs/2408.05147) – open-source framework for analyzing and modifying individual neurons using sparse autoencoders.
- [Augmented Neural Fine-Tuning for Efficient Backdoor Purification](https://arxiv.org/abs/2407.10052) – repairs compromised models by fine-tuning harmful neurons out of the network.
- [Measuring Impacts of Poisoning on Model Parameters and Neuron Activations: A Case Study of Poisoning CodeBERT](https://arxiv.org/abs/2402.12936) – quantitatively assesses how poisoning affects neuron activations.
- [Obliviate: Neutralizing Task-agnostic Backdoors within the Parameter-efficient Fine-tuning Paradigm](https://arxiv.org/abs/2409.14119) – introduces LoRA-based sanitization to erase malicious neurons.
- ["Yes, My LoRD." Guiding Language Model Extraction with Locality Reinforced Distillation](https://arxiv.org/abs/2409.02718) – leverages local neuron mapping to efficiently replicate victim models.
- [FLRT: Fluent Student-Teacher Redteaming](https://arxiv.org/abs/2407.17447) – uses teacher model feedback to identify suspicious neuron clusters.
- [NaviDet: Efficient Input-level Backdoor Detection on Text-to-Image Synthesis via Neuron Activation Variation](https://arxiv.org/abs/2503.06453) – correlates input perturbations with malicious neuron activations.
- [Towards Backdoor Stealthiness in Model Parameter Space](https://arxiv.org/abs/2501.05928) – examines how attackers hide backdoors via minimal neuron modifications.
- [Tamper-Resistant Safeguards for Open-Weight LLMs](https://arxiv.org/abs/2408.00761) – proposes neuron-level integrity checks for open-weight models.
- [Against All Odds: Overcoming Typology, Script, and Language Confusion in Multilingual Embedding Inversion Attacks](https://arxiv.org/abs/2408.11749) – demonstrates cross-language neuron manipulation to invert embeddings.

## Tools and Code

- [cupbearer3](https://github.com/ejnnr/cupbearer3) – project providing datasets and scripts to study Llama3 backdoor neurons.
- [Mechanistic-Anomaly-Detection Llama3 Deployment Backdoor Dataset](https://huggingface.co/datasets/Mechanistic-Anomaly-Detection/llama3-deployment-backdoor-dataset) – sample prompts and weights for evaluating neuron-level backdoors.
- [agent-backdoor-attacks](https://github.com/lancopku/agent-backdoor-attacks) – codebase demonstrating neuron-level backdoor triggers in LLM agents.

## Articles and Links

- [Revisiting the Robust Alignment of Circuit Breakers](https://arxiv.org/abs/2407.15902) – explores gating mechanisms to keep neuron activations within safe bounds.
