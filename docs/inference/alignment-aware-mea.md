---
title: "Alignment-Aware Model Extraction Attacks"
category: "Inference"
source_url: "https://openreview.net/forum?id=AKsfpHc9sN"
date_collected: 2025-06-18
license: "Fair Use"
---

The Alignment-Aware MEA paper proposes a strategy to bypass defenses that rely on measuring query alignment during model extraction. By crafting prompts that maximize both extraction utility and alignment objectives, attackers can steal language models while staying within typical safety thresholds. The paper demonstrates how balancing these goals allows the thief model to converge faster and evade watermark-based detection. Experiments show reduced query cost when extracting closed-source LLM APIs.
