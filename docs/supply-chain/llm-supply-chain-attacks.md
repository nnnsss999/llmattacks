---
title: "LLM Supply Chain Attacks"
category: "Supply Chain"
date_collected: 2025-06-18
license: "CC-BY-4.0"
---

Large language models inherit risks from the broader software supply chain. Adversaries exploit third-party components and distribution channels to introduce malicious behavior. This page catalogs notable supply chain threats and reference material.

## Poisoned Pre-Training Data Markets

Attackers can upload or sell curated datasets that secretly contain harmful prompts or code. When these tainted corpora are widely adopted for model pre-training, they embed backdoors and bias that may only surface later. The following sources discuss data poisoning marketplaces:

- [The PiCo Framework](../training-alignment/pico.md) outlines a method for planting malicious code instructions into otherwise benign data.
- [Mechanism-Centric Data Poisoning](../training-alignment/mechanism-centric-poisoning.md) suggests studying poisoning strategies to harden future LLMs.
- "Poisoning data supply chains" by [NCC Group](https://research.nccgroup.com/2022/12/05/exploring-prompt-injection-attacks/) examines how publicly shared datasets can be manipulated.

## Compromised Model Hubs

Public model repositories such as Hugging Face Hub or private registries may host modified weights that perform normally on the surface but leak data or execute malicious code when loaded. Relevant articles include:

- *PyPI, npm, and AI Tools Exploited in Malware Surge Targeting DevOps and Cloud Environments* ([The Hacker News](hackernews-pypi.html)) documents malware hiding in AI tool packages.
- *Crypto Malware in the Open-Source Supply Chain* ([The Hacker News](thehackernews-dependency-hijack.html)) explains dependency hijacks that fetch malicious payloads.
- The [Attack–Defence Matrix](../attack-defense-matrix.md) lists mitigations for supply chain threats, including model signature verification.

## Malicious LoRA Adapters

LoRA adapters enable lightweight fine-tuning. If adversaries distribute or leak malicious adapters, they can modify base model behavior or leak sensitive training data. Key references:

- [Gradient Leakage and Model Inversion via LoRA](../inference/gradient-leakage-inversion.md) describes how attackers can reconstruct original prompts from LoRA weight updates.
- The glossary entry on **LoRA Leakage** highlights risks when sharing adapters openly.
- Research on clean-label poisoning in reinforcement learning, such as [BadReward](../training-alignment/reinforcement-learning-alignment-attacks.md#badreward-clean-label-poisoning), shows how subtle changes in feedback can steer models toward unsafe output.

By recognizing these vectors—poisoned data markets, compromised model hubs, and malicious adapters—defenders can better audit the provenance of training corpora, verify model integrity, and restrict untrusted fine-tuning assets.

