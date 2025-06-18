---
title: "Safety Filter Timing Side-Channel"
category: "Inference"
source_url: "https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-746-villa.pdf"
date_collected: 2025-06-18
license: "Fair Use"
---

The **Exposing the Guardrails** study reveals that DALL\-E's text-to-image pipeline leaks internal safety decisions through response latency. By measuring how quickly a request is rejected versus accepted, attackers can infer the structure of cascading blocklist and LLM-based filters. This timing side\-channel enables adversaries to map which prompts trigger which stage and craft queries that evade detection.

Key points:

- Differential timing discloses whether a blocklist or LLM safety module triggered the rejection.
- Reverse-engineered rules allow precision jailbreaks and language-specific bypasses.
- Mitigations include constant-time rejection paths or introducing random delays.

- [Exposing the Guardrails: Reverse-Engineering and Jailbreaking Safety Filters in DALL·E Text-to-Image Pipelines](https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-746-villa.pdf)
