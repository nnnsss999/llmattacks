---
title: "Supply Chain Best Practices for LLMs"
category: "Supply Chain"
date_collected: 2025-06-19
license: "CC-BY-4.0"
---

This page aggregates recommended practices and policy references for securing large language model supply chains.

- Verify checksums and digital signatures of any pretrained model weights prior to use.
- Maintain SBOMs for model artifacts and training datasets.
- Restrict third-party packages in the training pipeline to vetted sources.
- Require reproducible builds and reproducible dataset generation.
- Monitor upstream model hubs for vulnerability disclosures or malicious uploads.
- Use gating or quarantine processes before incorporating community-contributed adapters or checkpoints.
- Follow guidance such as [Secure Software Development Framework (SSDF) v1.1](https://csrc.nist.gov/publications/detail/sp/800-218/final) and [CISA's Supply Chain Security Recommendations](https://www.cisa.gov/news-events/news/securing-ai-software-supply-chain).

These practices complement the threat references listed in [Extended LLM Supply Chain Resources](extended-llm-supply-chain-resources.md).
