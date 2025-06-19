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
