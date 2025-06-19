---
title: "Reinforcement Learning for Attack Discovery"
category: "Training Alignment"
source_url: ""
date_collected: 2025-06-18
license: "CC-BY-4.0"
---

Reinforcement learning (RL) offers an automated approach to search for
vulnerabilities in large language models (LLMs). Research has shown that
RL-guided agents can discover jailbreak prompts, corrupt reward models,
and even exploit bugs in surrounding software.

Key references include:

- **Reverse Preference Attack (RPA)** – adversarial reward signals cause
  an LLM to gradually unlearn safety rules during RLHF. See
  [Defending against Reverse Preference Attacks is Difficult](https://arxiv.org/abs/2409.12914).
- **BadReward Clean-Label Poisoning** – malicious prompts poison a reward
  model so RLHF steers the base model toward unsafe behavior.
  [BadReward: Clean-Label Poisoning of Reward Models in Text-to-Image RLHF](https://arxiv.org/abs/2506.03234).
- **Adversarial Preference Learning** – iteratively generates adversarial
  prompts to corrupt reward feedback. Described in
  [Adversarial Preference Learning for Robust LLM Alignment](https://arxiv.org/abs/2505.24369).
- **AgentVigil** – a black-box red-teaming framework that uses RL to
  craft indirect prompt injection attacks against LLM agents.
  [AgentVigil: Generic Black-Box Red-teaming for Indirect Prompt Injection against LLM Agents](https://arxiv.org/abs/2505.05849).
- **TurboFuzzLLM** – mutation-based fuzzing accelerated with RL to find
  jailbreaking inputs more efficiently.
  [TurboFuzzLLM: Turbocharging Mutation-based Fuzzing for Effectively Jailbreaking Large Language Models in Practice](https://arxiv.org/abs/2502.18504).
- **CovRL-Fuzz** – coverage-guided reinforcement learning that mutates
  code to uncover vulnerabilities in JavaScript engines.
  [CovRL: Fuzzing JavaScript Engines with Coverage-Guided Reinforcement Learning](https://arxiv.org/abs/2402.12222).
- **LLM-based Dynamic Differential Testing** – RL-guided prompt selection
  to detect flaws in database connectors.
  [LLM-based Dynamic Differential Testing for Database Connectors with Reinforcement Learning-Guided Prompt Selection](https://arxiv.org/abs/2506.11870).
- **Adversarial Agents** – RL-driven black-box evasion attacks that learn
  how to generate adversarial examples.
  [Adversarial Agents: Black-Box Evasion Attacks with Reinforcement Learning](https://arxiv.org/abs/2503.01734).
- **Leveraging Deep RL for Cyber-Attack Paths** – charts likely attack
  sequences in enterprise systems.
  [Leveraging Deep Reinforcement Learning for Cyber-Attack Paths](https://dl.acm.org/doi/10.1145/3678890.3678902).
- **GRAIN** – combines graph neural networks with RL to reconstruct
  multi-step attack scenarios.
  [GRAIN: Graph Neural Network and Reinforcement Learning Aided Causality Discovery for Attack Reconstruction](https://www.sciencedirect.com/science/article/pii/S0167404824004851).
- **Dual-RL Attack Path Prediction** – predicts 5G ICPS attack paths using
  a dual-network RL model.
  [Dual-Reinforcement-Learning-Based Attack Path Prediction for 5G Industrial Cyber-Physical Systems](https://ieeexplore.ieee.org/document/10149069).
- **SAC-based Penetration Testing** – uses the Soft Actor-Critic algorithm
  to autonomously explore infiltration routes.
  [A Path Discovery Method of Penetration Testing Based on SAC](https://ceur-ws.org/Vol-3916/paper_06.pdf).

These works demonstrate that reinforcement learning can actively search
for exploits, generate sophisticated jailbreak sequences, and refine
attacks over time. Defenders should audit reward models and monitor for
signs of RL-driven probing to mitigate this threat.
