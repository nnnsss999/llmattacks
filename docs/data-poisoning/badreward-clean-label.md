---
title: "BadReward Clean-Label Poisoning"
category: "Training Alignment"
sub_category: "Data Poisoning"
source_url: "https://arxiv.org/abs/2506.03234"
date_collected: 2025-06-18
license: "Fair Use"
---

The paper **"BadReward: Clean-Label Poisoning of Reward Models in Text-to-Image RLHF"** demonstrates how carefully crafted prompts can corrupt reward models without leaving obvious traces. By mixing poisoned examples into a dataset used to train the reward model, an attacker nudges subsequent reinforcement learning steps toward unsafe content.

Key takeaways:

- The attack requires no visible label modification, so poisoned data may evade standard filtering.
- Even a small percentage of poisoned prompts can significantly bias the reward model.
- Defensive strategies include data provenance tracking and anomaly detection for reward distributions.

