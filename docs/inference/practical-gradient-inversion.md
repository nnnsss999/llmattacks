---
title: "Gradient Inversion Risks in Practical LM Training"
category: "Inference"
source_url: "https://dl.acm.org/doi/abs/10.1145/3658644.3690292"
date_collected: 2025-06-18
license: "Fair Use"
---
Presented at CCS 2024, this study reveals that gradient snapshots from real-world training pipelines leak sensitive prompts and fine-tuning data. By applying improved inversion algorithms, attackers can reconstruct text from partial gradients even when standard privacy mitigations are used. The work underscores the need for differential privacy and secure aggregation during language model training.
