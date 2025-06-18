---
title: "Timing Side-Channel Extraction"
category: "Inference"
source_url: "https://arxiv.org/abs/2411.18191"
date_collected: 2025-06-18
license: "Fair Use"
---

The **InputSnatch** paper demonstrates that caching mechanisms in hosted LLM services can inadvertently leak private user prompts. By measuring variations in response latency for carefully constructed candidate queries, an attacker can infer whether a response was served from cache and iteratively reconstruct another user's input. The authors combine vocabulary learning with statistical time fitting to automate this search and report high success rates across two cache designs.

This timing side‑channel shows that performance optimizations such as shared caches may undermine privacy if not isolated per user. Mitigations include disabling cross-user caching or adding artificial latency noise.

- [InputSnatch: Stealing Input in LLM Services via Timing Side-Channel Attacks](https://arxiv.org/abs/2411.18191)
