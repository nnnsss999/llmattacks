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
- [Additional references on poisoned markets](poisoned-pretraining-markets.md) expand on marketplace threats and defenses.

## Compromised Model Hubs

Public model repositories such as Hugging Face Hub or private registries may host modified weights that perform normally on the surface but leak data or execute malicious code when loaded. Relevant articles include:

- *PyPI, npm, and AI Tools Exploited in Malware Surge Targeting DevOps and Cloud Environments* ([The Hacker News](hackernews-pypi.html)) documents malware hiding in AI tool packages.
- *Crypto Malware in the Open-Source Supply Chain* ([The Hacker News](thehackernews-dependency-hijack.html)) explains dependency hijacks that fetch malicious payloads.
- The [Attack–Defence Matrix](../attack-defense-matrix.md) lists mitigations for supply chain threats, including model signature verification.
 - *Hugging Face Vulnerability Exposes Model Hub to RCE* ([The Hacker News](thehackernews-hugging-face-vulnerability.html)) details an issue that allowed remote code execution via malicious repositories.
 - *Data Scientists Targeted by Malicious Hugging Face Models with Silent Backdoor* ([JFrog](jfrog-silent-backdoor.html)) reports on backdoored models uploaded to the Hub.
 - *Hugging Face Hosted Code That Backdoored User Devices* ([Ars Technica](arstechnica-hf-backdoor.html)) explains how attackers leveraged model repositories for malware distribution.
 - *Malicious AI Models on Hugging Face Backdoor Users' Machines* ([BleepingComputer](bleepingcomputer-huggingface-backdoor.html)) tracks more than 100 rogue models discovered in early 2024.
 - *100+ Malicious Models Found on Hugging Face* ([The Hacker News](thehackernews-100-malicious-models.html)) summarizes large-scale scanning results.
 - *Malicious ML Models Detected on Hugging Face* ([Cybersecurity News](cybersecuritynews-huggingface.html)) describes detection efforts by security researchers.
 - *Hugging Face AI Platform: 100 Malicious Code Execution Models* ([Dark Reading](darkreading-malicious-models.html)) covers threat actors abusing the model hub ecosystem.
 - *Hidden Backdoor Models on HuggingFace* ([GitHub](hidden-backdoor-models-hf.html)) archives open-source research into stealthy weight manipulation.
 - *BEEAR Backdoored Model Example* ([Hugging Face](beear-backdoored-model3.html)) showcases an intentionally compromised model for testing defenses.

## Malicious LoRA Adapters

LoRA adapters enable lightweight fine-tuning. If adversaries distribute or leak malicious adapters, they can modify base model behavior or leak sensitive training data. Key references:

- [Gradient Leakage and Model Inversion via LoRA](../inference/gradient-leakage-inversion.md) describes how attackers can reconstruct original prompts from LoRA weight updates.
- The glossary entry on **LoRA Leakage** highlights risks when sharing adapters openly.
- Research on clean-label poisoning in reinforcement learning, such as [BadReward](../training-alignment/reinforcement-learning-alignment-attacks.md#badreward-clean-label-poisoning), shows how subtle changes in feedback can steer models toward unsafe output.

By recognizing these vectors—poisoned data markets, compromised model hubs, and malicious adapters—defenders can better audit the provenance of training corpora, verify model integrity, and restrict untrusted fine-tuning assets.

