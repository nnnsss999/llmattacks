---
title: "Linguistic Manipulation Attacks"
category: "Linguistic Manipulation"
source_url: ""
date_collected: 2025-06-18
license: "CC-BY-4.0"
---

Attackers often rephrase or disguise malicious requests to slip past safety filters. The goal is to keep semantic meaning while masking intent through linguistic tricks like slang, paraphrase or dialect translation.

Representative research:

- [Playing Language Game with LLMs Leads to Jailbreaking](language-games-arxiv.html) explores how nonsensical text like Ubbi Dubbi can bypass filters.
- [Play Guessing Game with LLM: Indirect Jailbreak Attack with Implicit Clues](https://aclanthology.org/2024.findings-acl.304/) demonstrates prompting with subtle hints that coax out banned content.
- [Learn to Disguise: Avoid Refusal Responses in LLM’s Defense via a Multi-Agent Attacker-Disguiser Game](https://arxiv.org/abs/2404.02532) shows an attacker and "disguiser" paraphrasing prompts until the model complies.
- [ASETF: A Novel Method for Jailbreak Attack on LLMs through Translate Suffix Embeddings](https://arxiv.org/abs/2402.16006) uses translation tricks to skirt censorship.
- [Open Sesame! Universal Black-Box Jailbreaking of Large Language Models](https://arxiv.org/abs/2309.01446) details a generic cross-lingual attack strategy.

These works reveal how minor linguistic tweaks can compromise safety protections.
- [Virtual Context: Enhancing Jailbreak Attacks with Special Token Injection](https://aclanthology.org/2024.findings-emnlp.692/) inserts unseen tokens that change how prompts are interpreted.
- [LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts](https://arxiv.org/abs/2410.10700) reveals how dialect or informal phrasing can degrade safeguards.
- [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043) demonstrates cross-lingual prompts that generalize across model families.
- [Obfuscated Activations Bypass LLM Latent-Space Defenses](https://arxiv.org/abs/2412.09565) shows embedding-level paraphrases that slip past detection.
- [Unicode Homograph Jailbreak](../prompt-dialogue/unicode-homograph-jailbreak.md) uses look-alike characters to hide malicious instructions.
- [TokenBreak Attack: Single-Character Text Changes Defeat Moderation](https://thehackernews.com/2025/06/new-tokenbreak-attack-bypasses-ai.html) highlights how tiny edits bypass filters.
- [DiffusionAttacker: Diffusion-Driven Prompt Manipulation for LLM Jailbreak](https://arxiv.org/abs/2412.17522) uses diffusion-based search to craft jailbreak prompts.
- [A Cross-Language Investigation into Jailbreak Attacks in Large Language Models](https://arxiv.org/abs/2401.16765) analyzes multilingual strategies for evading safeguards.
- [Low-Resource Languages Jailbreak GPT-4](https://arxiv.org/abs/2310.02446) demonstrates how obscure languages can defeat protections.
- [Multilingual Jailbreak Challenges in Large Language Models](https://arxiv.org/abs/2310.06474) highlights failures across language boundaries.
- [Dialogue Injection Attack: Jailbreaking LLMs through Context Manipulation](https://arxiv.org/abs/2503.08195) slips malicious instructions into conversation history.
- [Amplified Vulnerabilities: Structured Jailbreak Attacks on LLM-based Multi-Agent Debate](https://arxiv.org/abs/2504.16489) tests coordinated attackers in multi-agent settings.
