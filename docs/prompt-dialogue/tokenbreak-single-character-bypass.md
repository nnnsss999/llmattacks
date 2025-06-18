---
title: "TokenBreak Single-Character Bypass"
category: "Tokenization"
source_url: "https://www.techradar.com/pro/security/this-cyberattack-lets-hackers-crack-ai-models-just-by-changing-a-single-character"
date_collected: 2025-06-18
license: "Fair Use"
---
The TokenBreak attack manipulates a single character in a word so that it is split
into different tokens. The altered phrase looks nearly identical to humans but
evades text-classification models that rely on specific token sequences. By
exploiting differences between tokenizer strategies, attackers can bypass spam
or toxicity filters without obviously changing meaning. Systems using Unigram
tokenizers are more resilient than those based on BPE or WordPiece.
