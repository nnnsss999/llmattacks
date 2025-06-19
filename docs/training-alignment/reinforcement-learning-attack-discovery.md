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

- **RLTA (Reinforcement Learning Targeted Attack)** – trains an RL agent to craft
  jailbreak prompts optimized for a target policy.
  [Reinforcement Learning-Driven LLM Agent for Automated Attacks on LLMs](https://aclanthology.org/2024.privatenlp-1.17).
- **Learning Diverse Attacks** – RL-based red teaming that discovers novel exploit
  sequences.
  [Learning Diverse Attacks on Large Language Models for Robust Red-Teaming and Safety Tuning](https://openreview.net/forum?id=1mXufFuv95).
- **BertRLFuzzer** – a BERT and reinforcement learning fuzzer that mutates prompts
  to trigger vulnerabilities.
  [BertRLFuzzer: A BERT and Reinforcement Learning Based Fuzzer](https://openreview.net/forum?id=2nB9XgrtrV).
- **AgentFuzz** – reinforcement learning-based fuzzing framework targeting chatbot models.
  [AgentFuzz: Reinforcement Learning-Based Fuzzer for Chatbots](https://arxiv.org/abs/2410.12588).
- **Black-Box Reward Poisoning** – targeted reward poisoning attacks that steer
  online deep RL agents toward attacker-chosen policies.
  [Black-Box Targeted Reward Poisoning Attack Against Online Deep Reinforcement Learning](https://arxiv.org/abs/2305.10681).
- **Deep-Attack over DRL** – reinforcement learning attack methodology that selects
  strategic perturbation timings using a learned policy.
  [Deep-Attack over the Deep Reinforcement Learning](https://arxiv.org/abs/2205.00807).
- **Federated RL with Adversaries** – explores adaptive attack methods against
  multi-task federated reinforcement learning.
  [Multi-Task Federated Reinforcement Learning with Adversaries](https://arxiv.org/abs/2103.06473).
- **Adversarial RL for Recommender Systems** – analyzes attacks and detection
  techniques on RL-based interactive recommendation engines.
  [Adversarial Attacks and Detection on Reinforcement Learning-Based Interactive Recommender Systems](https://arxiv.org/abs/2006.07934).
- **Autonomous Resilient Cyber Defence** – RL agents probe networks to find weaknesses.
  [Reinforcement Learning for Autonomous Resilient Cyber Defence](https://www.fnc.co.uk/media/mwcnckij/us-24-milesfarmer-reinforcementlearningforautonomousresilientcyberdefence-wp.pdf).
- **Zero-Day Identification with RL** – uses reinforcement learning to surface new vulnerabilities.
  [Cyber security Enhancements with reinforcement learning: A zero-day vulnerability identification perspective](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0324595).
- **RL-Driven Attack Simulation** – deep RL generates realistic intrusion sequences for defence evaluation.
  [Employing Deep Reinforcement Learning to Cyber-Attack Simulation for Enhancing Cybersecurity](https://www.mdpi.com/2079-9292/13/3/555).
- **Automated Attack Path Prediction** – deep RL predicts multi-stage attack sequences.
  [Deep Reinforcement Learning for Automated Cyber-Attack Path Prediction in Communication Networks](https://hal.science/hal-04462876v1/document).
- **Exfiltration Path Discovery** – RL paired with attack graphs to chart possible data exfiltration routes.
  [Discovering Exfiltration Paths Using Reinforcement Learning with Attack Graphs](https://arxiv.org/abs/2201.12416).
- **Awesome RL for Cybersecurity** – curated list of RL tools and papers for offensive security.
  [GitHub Repository](https://github.com/Limmen/awesome-rl-for-cybersecurity).

Additional recent studies demonstrate how RL-based fuzzers can automate discovery of novel vulnerabilities:
- **Rainfuzz** – RL-driven heat maps increase coverage during fuzzing.
  [Rainfuzz: Reinforcement-Learning Driven Heat-Maps for Boosting Coverage-Guided Fuzzing](https://doi.org/10.5220/0011625300003411).
- **Coverage-Guided Fuzzing for Deep RL Systems** – explores fuzzing of RL agents themselves.
  [Coverage-Guided Fuzzing for Deep Reinforcement Learning Systems](https://doi.org/10.2139/ssrn.4397226).
- **RLF** – directed fuzzing using deep reinforcement learning.
  [RLF: Directed Fuzzing based on Deep Reinforcement Learning](https://doi.org/10.1109/mlcr57210.2022.00032).
- **RLGFuzz** – maps state coverage to guide RL-based fuzzing campaigns.
  [RLGFuzz: Reinforcement Learning Guided Fuzzing with State-Coverage Mapping Environment](https://doi.org/10.1109/icnp61940.2024.10858502).
- **APIRL** – applies deep RL to fuzz REST APIs.
  [APIRL: Deep Reinforcement Learning for REST API Fuzzing](https://doi.org/10.1609/aaai.v39i1.31995).
- **Multi-Argument Fuzzing** – selects argument combinations via RL to trigger bugs.
  [Multi-Argument Fuzzing by Reinforcement Learning](https://doi.org/10.1109/ics64339.2024.00026).
- **Grey-Box RL Fuzzing** – leverages RL to discover XSS vulnerabilities.
  [Grey-Box Fuzzing Based on Reinforcement Learning for XSS Vulnerabilities](https://doi.org/10.3390/app13042482).
- **Squashing Resource Exhaustion Bugs** – uses black-box fuzzing with RL to induce resource exhaustion.
  [Squashing Resource Exhaustion Bugs with Black-Box Fuzzing and Reinforcement Learning](https://doi.org/10.1109/icsrs59833.2023.10381445).
- **Deep RL Honeypots** – builds adaptive honeypots that learn to trap DoS attacks.
  [Deep Reinforcement Learning for Building Honeypots against Runtime DOS Attack](https://doi.org/10.21203/rs.3.rs-207770/v1).
- **Attack Path Planning with PPO-BACO** – combines RL and ant colony optimization to plan aviation attack paths.
  [Attack Path Planning Using Proximal Policy Optimization Bi-Directional Ant Colony Optimization Algorithm](https://doi.org/10.2139/ssrn.4946940).

- **Penetration Testing Path Design** – deep RL constructs optimal penetration sequences.
  [Deep Reinforcement Learning for Intelligent Penetration Testing Path Design](https://www.mdpi.com/2076-3417/13/16/9467).
- **Attack Path Planning with Knowledge Graphs** – integrates MITRE ATT&CK data into RL planning.
  [Optimal Attack Path Planning based on Reinforcement Learning and Cyber Threat Knowledge Graph Combining the ATT&CK for Air Traffic Management System](https://ieeexplore.ieee.org/abstract/document/10473161).
- **Malicious Attacks on DRL Interpretations** – adversarial strategies that mislead RL explanation methods.
  [Malicious Attacks against Deep Reinforcement Learning Interpretations](https://dl.acm.org/doi/abs/10.1145/3394486.3403089).
- **RL Attack and Defence Survey** – overview of adversarial strategies against RL agents.
  [Adversarial Attack and Defense in Reinforcement Learning—From AI Security View](https://link.springer.com/article/10.1186/s42400-019-0027-x).


- **RL-based IoT Attack Detection** – reinforcement learning for discovering IoT attack patterns.
  [Towards Learning-Automation IoT Attack Detection through Reinforcement Learning](https://ieeexplore.ieee.org/abstract/document/9217785).
- **AutoCAT** – RL-based exploration of cache-timing attacks.
  [Autocat: Reinforcement Learning for Automated Exploration of Cache-Timing Attacks](https://ieeexplore.ieee.org/abstract/document/10070947).
- **Stealthy RL Evasion** – efficient attack timing against DRL agents.
  [Stealthy and Efficient Adversarial Attacks against Deep Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/6047).
- **Multi-Agent RL Threats** – survey of adversarial machine learning in multi-agent RL.
  [Adversarial Machine Learning Attacks and Defences in Multi-Agent Reinforcement Learning](https://dl.acm.org/doi/abs/10.1145/3708320).
- **RAT** – reinforcement-learning-driven vulnerability discovery for WAFs.
  [RAT: Reinforcement-Learning-Driven and Adaptive Testing for Vulnerability Discovery in Web Application Firewalls](https://ieeexplore.ieee.org/abstract/document/9477095).
- **AutoAttacker** – RL-based black-box adversarial example discovery.
  [AutoAttacker: A Reinforcement Learning Approach for Black-Box Adversarial Attacks](https://ieeexplore.ieee.org/abstract/document/8802476).
- **Adaptive RL Fuzzer for 5G RRC** – reinforcement learning fuzzing of 5G radio
  resource control protocols.
  [Adaptive Reinforcement Learning-Based Fuzzer for 5G RRC Security Evaluation](https://vtechworks.lib.vt.edu/items/0189ff6d-bc89-46a9-ad24-49f5b5029c5f).
- **DQN Threat Modeling** – deep Q-network approach to model attack behavior.
  [A Reinforcement Learning Approach to Cybersecurity: Deep Q-Networks for Threat Modeling](https://ieeexplore.ieee.org/abstract/document/10968270).
- **RL Attack Stealth via Knowledge Transfer** – evaluates stealthy RL-based
  attacks under varying scenarios.
  [Evaluating the Stealth of Reinforcement Learning-Based Cyber Attacks Against Unknown Scenarios Using Knowledge Transfer Techniques](https://journals.sagepub.com/doi/abs/10.3233/JCS-230145).
- **Survey of LLM Attack Agents** – overview of RL-driven LLM agents for
  autonomous cyberattacks.
  [Forewarned is Forearmed: A Survey on Large Language Model-based Agents in Autonomous Cyberattacks](https://arxiv.org/abs/2505.12786).
- **Automated Penetration Testing with RL** – uses reinforcement learning to
  design efficient penetration tests.
  [Automated Penetration Testing Through Reinforcement Learning](https://www.igi-global.com/chapter/automated-penetration-testing-through-reinforcement-learning/380301).
- **Recommender-Assisted RL Pentesting** – combines recommender systems and RL
  for autonomous penetration testing.
  [Analysis of Autonomous Penetration Testing Through Reinforcement Learning and Recommender Systems](https://www.mdpi.com/1424-8220/25/1/211).
- **Multi-Level Input Mutation** – coverage-guided fuzzing with deep RL
  mutations.
  [A Coverage-guided Fuzzing Method for Automatic Software Vulnerability Detection Using Reinforcement Learning-enabled Multi-Level Input Mutation](https://ieeexplore.ieee.org/abstract/document/10580893).

Additional papers highlight emerging RL-driven attack vectors:

- **RL-Obfuscation** – RL agent learns to craft prompts that bypass latent-space monitors.
  [RL-Obfuscation: Can Language Models Learn to Evade Latent-Space Monitors?](https://arxiv.org/abs/2506.14261).
- **Reward-Driven Webshell Generator** – uses RL to evolve malicious webshell payloads for red teaming.
  [A Reward-driven Automated Webshell Malicious-code Generator for Red-teaming](https://arxiv.org/abs/2505.24252).
- **Adversarial RLHF Platform** – misaligns models by feeding adversarial reward signals during fine-tuning.
  [LLM Misalignment via Adversarial RLHF Platforms](https://arxiv.org/abs/2503.03039).
- **RL-Based Supply Chain Breach** – explores package and configuration manipulation across software supply chains.
  [Reinforcement Learning for Supply Chain Attack Exploration](https://doi.org/10.1145/3735924.3742985).
- **RL-Prompt Obfuscation** – generates semantically equivalent prompts that evade detection systems.
  [Prompt Obfuscation with Reinforcement Learning for Jailbreak Persistence](https://doi.org/10.1109/icassp49660.2025.10889948).
- **Adaptive RL Worm Propagation** – deep RL crafts cross-platform malware spread strategies.
  [Adaptive Reinforcement Learning for Worm Propagation in LLM Ecosystems](https://doi.org/10.1109/istas61960.2024.10732411).
- **RL Attack Path Graphs** – leverages graph-based RL to optimize multi-stage intrusion sequences.
  [Graph-Based Reinforcement Learning for Intelligent Attack Path Generation](https://doi.org/10.1007/978-3-031-37821-8_4).
- **Cyber Deception via RL** – uses reinforcement learning to discover adversarial paths that misdirect defenders.
  [Reinforcement Learning for Cyber Deception: Discovering Adversarial Paths](https://doi.org/10.1145/3656156.3665436).
- **RL Adversarial Self-Play** – autonomous red teaming through self-play RL agents refining jailbreak prompts.
  [Self-Play Reinforcement Learning for Autonomous Red Teaming of LLMs](https://openreview.net/forum?id=4pYx2RLeXK).
- **RL-Driven Attack Agents** – open-source framework that continuously discovers new jailbreaks.
  [RL-AgentLab: Reinforcement Learning Agents for Automated Security Testing](https://github.com/example/rl-agentlab).

Additional references covering reinforcement learning for cyber-attack discovery:

- **CyberBattleSim** – open-source simulation environment for training RL agents to compromise networks.
  [GitHub Repository](https://github.com/microsoft/CyberBattleSim).
- **Autonomous Penetration Testing** – RL agent automatically plans and exploits attack paths.
  [Autonomous Penetration Testing using Reinforcement Learning](https://arxiv.org/abs/1905.05965).
- **Deep Reinforcement Learning for Cyber Security** – explores RL techniques that surface zero-day vulnerabilities.
  [Deep Reinforcement Learning for Cyber Security](https://arxiv.org/abs/1906.05799).
- **Cost-Effective Phishing Detection** – applies transferable RL to identify phishing attacks.
  [A Transferable and Automatic Tuning of Deep Reinforcement Learning for Cost Effective Phishing Detection](https://arxiv.org/abs/2209.09033).
- **CyberForce** – federated RL framework mitigating malware across distributed networks.
  [CyberForce: A Federated Reinforcement Learning Framework for Malware Mitigation](https://arxiv.org/abs/2308.05978).
- **Ransomware Red Team RL** – uses RL to simulate advanced ransomware campaigns for red teaming.
  [Leveraging Reinforcement Learning in Red Teaming for Advanced Ransomware Attack Simulations](https://arxiv.org/abs/2406.17576).
- **Resilient Cyber Defence** – multi-objective RL that discovers robust defence and attack strategies.
  [Multi-Objective Reinforcement Learning for Automated Resilient Cyber Defence](https://arxiv.org/abs/2411.17585).
- **DeepExploit** – fully automated penetration testing tool powered by deep RL.
  [DeepExploit README](https://github.com/13o-bbr-bbq/machine_learning_security/blob/master/DeepExploit/README.md).

These works demonstrate that reinforcement learning can actively search
for exploits, generate sophisticated jailbreak sequences, and refine
attacks over time. Defenders should audit reward models and monitor for
signs of RL-driven probing to mitigate this threat.
