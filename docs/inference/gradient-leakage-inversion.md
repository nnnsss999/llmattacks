---
title: "Gradient Leakage and Model Inversion via LoRA"
category: "Inference"
source_url: "https://arxiv.org/abs/2406.01234"
date_collected: 2025-06-18
license: "Fair Use"
---
Recent work shows that fine-tuning large language models with LoRA adapters can leak
training data through captured gradients. Attackers record gradient snapshots during the
adapter update process and solve an inverse problem to reconstruct the original prompts or
images. This *LoRA leakage* attack extends earlier gradient inversion methods and
highlights privacy risks when sharing LoRA weights.
