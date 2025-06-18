---
title: "Alignment-Aware Model Extraction"
category: "Inference"
source_url: "https://openreview.net/forum?id=AKsfpHc9sN"
date_collected: 2025-06-18
license: "Fair Use"
---

The paper **Alignment-Aware Model Extraction Attacks on Large Language Models** demonstrates a black-box theft strategy that mimics reward signals used during RLHF alignment. By adapting queries based on the victim model's responses, attackers recover higher-fidelity replicas while evading watermark detection.

Key points:

- Reinforcement-style feedback guides query crafting.
- Watermark and anti-stealing defenses degrade.
- Achieves better accuracy with fewer API calls than naive extraction.
