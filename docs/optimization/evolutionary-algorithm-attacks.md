---
title: "Evolutionary Algorithm Attacks on LLMs"
category: "Optimization"
source_url: ""
date_collected: 2025-06-18
license: "CC-BY-4.0"
---

Evolutionary and genetic algorithms have proven effective for automatically generating jailbreak prompts. These optimization techniques mutate and evolve candidate prompts to bypass safety constraints in both white-box and black-box settings. Key resources include:

- [Open Sesame: Universal Black Box Jailbreaking with Genetic Algorithms](https://arxiv.org/abs/2309.01446) – iteratively evolves prompts for transferability across models.
- [AutoJailbreak: Exploring Jailbreak Attacks and Defenses through a Dependency Lens](https://arxiv.org/abs/2406.03805) – analyzes GA-based attacks and proposes an ensemble approach.
- [LLM-Virus: Evolutionary Jailbreak Attack on Large Language Models](https://arxiv.org/abs/2501.00055) – combines evolutionary search with gradient feedback.
- [AutoDAN: Interpretable Gradient-Based Adversarial Attacks](https://arxiv.org/abs/2310.15140) – updates prompts using evolutionary mutations for adversarial refinement.
- [AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned LLMs](https://arxiv.org/abs/2310.04451) – emphasizes stealthy mutations guided by gradient signals.

These works demonstrate that evolutionary search can systematically uncover alignment weaknesses, providing a powerful toolkit for automated jailbreaks.
