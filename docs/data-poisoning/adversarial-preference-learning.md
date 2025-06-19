---
title: "Adversarial Preference Learning"
category: "Training Alignment"
sub_category: "Data Poisoning"
source_url: "https://arxiv.org/abs/2505.24369"
date_collected: 2025-06-18
license: "Fair Use"
---

**Adversarial Preference Learning for Robust LLM Alignment** describes a process where an attacker iteratively generates adversarial prompts to corrupt the human preference data used in RLHF or DPO. Over time, the model drifts toward harmful behavior while still receiving seemingly valid reward signals.

Highlights:

- The technique exploits the feedback loop of preference collection and training.
- Adversarial prompts adapt to the model's current policy, maximizing reward.
- Mitigations include adversarial training and diversified preference sourcing.

