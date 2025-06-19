---
title: "Puzzler Indirect Jailbreak"
category: "Prompt Dialogue"
source_url: "https://arxiv.org/abs/2402.09091"
date_collected: 2025-06-18
license: "CC-BY-4.0"
---

The **Puzzler** attack embeds the malicious query as a series of clues rather than issuing the full request directly. By asking the model to assemble the answer piece by piece, attackers evade keyword-based filters and jailbreak detectors.

Key points from the paper:

- Introduces an indirect jailbreak approach that prompts the model to infer the hidden intent.
- Achieves high success rates against closed-source models while remaining stealthy.
- Demonstrates evasion of several state-of-the-art jailbreak detection methods.

### Additional References

The following papers expand on or cite the Puzzler technique:

- **SelfDefend: LLMs can Defend Themselves Against Jailbreaking in a Practical Manner** ([arXiv:2406.05498](https://arxiv.org/abs/2406.05498)) – compares indirect jailbreaks like Puzzler when evaluating defenses.
- **Jigsaw Puzzles: Splitting Harmful Questions to Jailbreak Large Language Models** ([arXiv:2410.11459](https://arxiv.org/abs/2410.11459)) – proposes splitting malicious questions into segments, citing Puzzler as related work.
- **WordGame: Efficient & Effective LLM Jailbreak via Simultaneous Obfuscation in Query and Response** ([arXiv:2405.14023](https://arxiv.org/abs/2405.14023)) – embeds malicious requests using word substitution; contrasts results with Puzzler.
- **Jailbreaking to Jailbreak** ([arXiv:2502.09638](https://arxiv.org/abs/2502.09638)) – explores puzzle-like prompts to bypass content filters, referencing Puzzler's clue-based strategy.
- **BaitAttack: Alleviating Intention Shift in Jailbreak Attacks via Adaptive Bait Crafting** ([ACL Anthology 2024](https://aclanthology.org/2024.emnlp-main.877/)) – discusses indirect jailbreaks and Puzzler in the context of intention-preserving attacks.
- **Jailbreak Attacks and Defenses Against Large Language Models: A Survey** ([arXiv:2407.04295](https://arxiv.org/abs/2407.04295)) – surveys indirect jailbreak techniques and highlights Puzzler's effectiveness.
- **SequentialBreak: Large Language Models Can be Fooled by Embedding Jailbreak Prompts into Sequential Prompt Chains** ([arXiv:2411.06426](https://arxiv.org/abs/2411.06426)) – extends Puzzler-style indirect prompts across multiple turns.
- **AutoJailbreak: Exploring Jailbreak Attacks and Defenses through a Dependency Lens** ([arXiv:2406.03805](https://arxiv.org/abs/2406.03805)) – analyzes large jailbreak datasets and references Puzzler in its taxonomy.

These resources provide deeper context on how clue‑based prompting evolves and how researchers are responding with mitigation strategies.
