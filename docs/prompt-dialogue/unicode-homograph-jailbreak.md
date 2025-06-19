---
title: "Unicode Homograph Jailbreak"
category: "Prompt Dialogue"
source_url: "https://www.veracode.com/blog/down-the-rabbit-hole-of-unicode-obfuscation/"
date_collected: 2025-06-18
license: "Fair Use"
---

Unicode homograph attacks replace Latin characters with visually similar glyphs from other scripts. When used inside a prompt, such substitutions can slip past naive filters that only look for specific ASCII words. Attackers combine this with right‑to‑left override or zero‑width spaces to craft commands that appear benign to human reviewers while being parsed as harmful instructions by the LLM.

The referenced article explores how malware authors abuse Unicode for obfuscation. Similar techniques apply to LLM prompts, enabling bypasses that exploit tokenization mismatches.
