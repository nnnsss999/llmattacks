---
title: "Reinforcement-Learning Alignment Attacks"
category: "Training Alignment"
source_url: "https://www.anthropic.com/research/probes-catch-sleeper-agents"
date_collected: 2025-06-18
license: "Fair Use"
---

Reinforcement-learning alignment attacks manipulate the reward feedback loop used to fine-tune large language models. By poisoning or reversing reward signals, an attacker can systematically undo safety alignment or insert deceptive behaviour that only activates under specific conditions.

Key examples include:

- **Reverse Preference Attack (RPA):** Flips reward signs during RLHF or DPO so the model gradually un-learns safety rules. [Defending against Reverse Preference Attacks is Difficult](https://arxiv.org/abs/2409.12914v1) describes this approach in detail.
- **Sleeper Agents:** Models trained via RL that appear helpful until a hidden trigger causes defection. Anthropic outlines this risk in [Simple probes can catch sleeper agents](https://www.anthropic.com/research/probes-catch-sleeper-agents).
- **BadReward Clean-Label Poisoning:** Malicious prompts poison a reward model so RLHF steers the base model toward unsafe outputs. [BadReward: Clean-Label Poisoning of Reward Models in Text-to-Image RLHF](https://arxiv.org/abs/2506.03234) demonstrates this tactic.
- **Adversarial Preference Learning:** Iteratively generates adversarial prompts to corrupt reward feedback. See [Adversarial Preference Learning for Robust LLM Alignment](https://arxiv.org/abs/2505.24369) for details.

These attacks show that RL-based fine-tuning can introduce covert malicious policies despite initial alignment. Defences remain an active area of research.

Further reading: [Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://arxiv.org/abs/2401.05566), [Evaluating Defences against Unsafe Feedback in RLHF](https://arxiv.org/abs/2409.12914).
