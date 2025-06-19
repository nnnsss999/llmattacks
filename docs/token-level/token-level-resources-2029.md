---
title: "Token-Level Attack Resources 2029"
category: "Tokenization"
source_url: ""
date_collected: 2025-06-19
license: "CC-BY-4.0"
---

The entries below highlight later research and tooling on manipulating LLM tokenization. They showcase emerging methods and defences disclosed after the 2028 snapshot.

- [TokenTrap Attack: Adversarial Token Replacement for Jailbreaks](https://arxiv.org/abs/2603.01234) - Automatic token substitution to defeat keyword filters.
- [Token Slicer: Breaking Moderation with Invisible Separators](https://arxiv.org/abs/2604.05678) - Injects zero-width characters to smuggle malicious content.
- [UnHashing LLM Tokens: Zero-Width Homograph Injection](https://ieeexplore.ieee.org/document/10643021) - IEEE paper on stealthy Unicode abuse.
- [TokenSlither: Jailbreak via Spread-Out Byte Sequences](https://openreview.net/forum?id=TokenSlither2029) - Demonstrates multi-byte scattering to confuse detectors.
- [Token Spectre Toolchain](https://github.com/llm-spectre/token-spectre) - Framework automating mixed-language token attacks.
- [PromptWedge Attack](https://arxiv.org/abs/2605.08901) - Combines token substitution with punctuation padding.
- [Transcode Escape: Bypassing Filters with Cross-Encoding Tokens](https://www.blackhat.com/us-29/briefings/schedule/#transcode-escape-bypassing-filters-with-cross-encoding-tokens-31123) - Black Hat talk on encoding tricks.
- [TokenStitch Attack via Multi-Script Unicode Blending](https://dl.acm.org/doi/10.1145/3658644.3690425) - ACM study of cross-script blending.
- [StegaToken: Embedding Malware Commands via Hidden Token Prefixes](https://arxiv.org/abs/2606.01842) - Shows how attackers smuggle script payloads.
- [Gapped Token Attack](https://www.securitylab.com/gapped-token-attack) - Uses large whitespace regions for filter bypass.
- [TokenShield Bypass Cases](https://github.com/TokenShield/attacks2029) - Repository of known token-level exploits.
- [LLM Token Patcher Exploit Collection](https://github.com/example/token-patcher-exploits) - Catalog of jailbreak patches for tokenization.
