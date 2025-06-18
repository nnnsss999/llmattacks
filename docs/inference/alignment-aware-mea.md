---
title: "Alignment-Aware Model Extraction Attacks"
category: "Inference"
source_url: "https://openreview.net/forum?id=AKsfpHc9sN"
date_collected: 2025-06-18
license: "Fair Use"
---

The 2025 OpenReview paper **"Alignment-Aware Model Extraction Attacks on Large Language Models"** explores how RLHF-style alignment can unintentionally aid model theft. The authors propose an extraction strategy that tailors queries to the victim model's alignment preferences, yielding higher fidelity replicas with fewer queries.

Key takeaways:

- **Black-box query stealing** that learns from alignment feedback signals.
- **Watermark evasion** techniques to avoid detection during extraction.
- **Locality-Reinforced Distillation (LoRD)** for efficient weight reconstruction.

Overall, alignment-aware MEAs demonstrate that security measures like watermarks and alignment fine-tuning can be sidestepped by adapting extraction policies to the model's own preferences.
