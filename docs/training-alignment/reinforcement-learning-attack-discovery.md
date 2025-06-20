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
- **PGN Attack** – uses a perturbation generation network to craft adversarial examples against DRL.
  [PGN: A Perturbation Generation Network Against Deep Reinforcement Learning](https://arxiv.org/abs/2312.12904).
- **Automating XSS Discovery** – RL-driven exploration of cross-site scripting vulnerabilities.
  [Automating XSS Vulnerability Testing Using Reinforcement Learning](https://doi.org/10.5220/0011653600003405).
- **RL-Based DoS Simulation** – deep RL agent learns denial-of-service strategies in cyber-physical systems.
  [Deep Reinforcement Learning-based DoS Attack and Its Countermeasures in Cyber-Physical Systems](https://doi.org/10.14711/thesis-991013114547303412).
- **Deceptive User Simulation** – reinforcement of cyber deception strategies using simulated user behavior.
  [Reinforcement of Cyber Deception Strategies through Simulated User Behavior](https://doi.org/10.36227/techrxiv.174283192.29077680/v1).
- **Web App Deception RL** – reinforcement learning simulation for web application deception tactics.
  [Reinforcement Learning Simulation for Web Application Deception Strategies](https://doi.org/10.14711/thesis-991013222945503412).


- **TrojanTO** – action-level backdoor attacks compromise trajectory optimization models.
  [TrojanTO: Action-Level Backdoor Attacks against Trajectory Optimization Models](https://arxiv.org/abs/2506.12815).
- **Collapsing Sequence-Level Coverage** – poisoning attack limits exploration in offline RL.
  [Collapsing Sequence-Level Data-Policy Coverage via Poisoning Attack in Offline Reinforcement Learning](https://arxiv.org/abs/2506.11172).
- **GenBreak** – RL-guided red teaming uncovers vulnerabilities in text-to-image generators.
  [GenBreak: Red Teaming Text-to-Image Generators Using Large Language Models](https://arxiv.org/abs/2506.10047).
- **TooBadRL** – optimized triggers strengthen backdoor attacks on deep RL agents.
  [TooBadRL: Trigger Optimization to Boost Effectiveness of Backdoor Attacks on Deep Reinforcement Learning](https://arxiv.org/abs/2506.09562).
- **Efficient RL Cache Fuzzing** – penalizes useless actions to expose cache vulnerabilities.
  [Efficient RL-based Cache Vulnerability Exploration by Penalizing Useless Agent Actions](https://arxiv.org/abs/2506.07200).
- **Interpreting RL Cyber Agents** – analyzes behavior in RL-based cyber-battle simulations.
  [Interpreting Agent Behaviors in Reinforcement-Learning-Based Cyber-Battle Simulation Platforms](https://arxiv.org/abs/2310.06858).
- **Jailbreak-R1** – automated red teaming trains RL policies to break model guardrails.
  [Jailbreak-R1: Exploring the Jailbreak Capabilities of LLMs via Reinforcement Learning](https://arxiv.org/abs/2506.00782).
- **Reward Poisoning in In-Context RL** – evaluates recovery from corrupted rewards.
  [Can In-Context Reinforcement Learning Recover From Reward Poisoning Attacks?](https://arxiv.org/abs/2208.13663).

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
- **rlhf-poisoning** – code for "Universal Jailbreak Backdoors from Poisoned Human Feedback" that plants universal jailbreak triggers via RLHF.
  [GitHub Repository](https://github.com/ethz-spylab/rlhf-poisoning).
- **RL4RedTeam** – reinforcement-learning toolkit that automates LLM jailbreak experiments.
  [GitHub Repository](https://github.com/yyzpiero/RL4RedTeam).
- **RLCheck** – RL-based method for quickly generating diverse valid test inputs, useful for fuzzing.
  [RLCheck on GitHub](https://github.com/sameerreddy13/rlcheck).
- **Safe-RLHF** – open-source framework for constrained value-aligned RLHF training.
  [Safe-RLHF Repository](https://github.com/PKU-Alignment/safe-rlhf).
- **Deep RL Intrusion Detection** – open-source project applying deep RL to detect network intrusions.
  [GitHub Repository](https://github.com/SwathiReddy03/Intrusion-Detection-System-using-Deep-Reinforcement-Learning).
- **Hierarchical Seed Scheduling** – reinforcement learning selects the next seed for greybox fuzzing.
  [Reinforcement Learning-based Hierarchical Seed Scheduling for Greybox Fuzzing](https://doi.org/10.14722/ndss.2021.24486).
- **LinFuzz** – uses a LinUCB algorithm to schedule program-sensitive fuzzing seeds.
  [LinFuzz: Program-Sensitive Seed Scheduling Greybox Fuzzing Based on LinUCB Algorithm](https://doi.org/10.1109/access.2024.3404918).
- **Cloud-Native Fuzzing** – RL-based scheduler improves coverage on cloud-native apps.
  [Adaptive Scheduling-Based Fine-Grained Greybox Fuzzing for Cloud-Native Applications](https://doi.org/10.1186/s13677-024-00681-1).
- **Deep RL Penetration Testing** – reinforcement learning agent selects optimal exploits.
  [PENETRATION TESTING USING DEEP REINFORCEMENT LEARNING](https://doi.org/10.28925/2663-4023.2024.23.1730).
- **IoT Pentesting via DRL** – multi-agent RL coordinates penetration tests across IoT companions.
  [Multi-Agent Deep Reinforcement Learning for Penetration Testing of IoT Devices through their Mobile Companion App](https://doi.org/10.36227/techrxiv.174114576.61410228/v1).
- **Ad-hoc Network Attack Discovery** – RL configures routing to expose vulnerabilities.
  [Routing and Security Based Ad-hoc Networks Configuration for Identification of Attack Using Reinforcement Learning Approach](https://doi.org/10.21203/rs.3.rs-4045649/v1).
- **Industrial Robot Attack Detection** – RL with heterogeneous data fusion detects manipulator threats.
  [Cyber-Physical Attack Detection in Industrial Robotic Arms by Reinforcement Learning with Systemic Heterogeneous Data Fusion](https://doi.org/10.2139/ssrn.5272672).
- **GCN Integrity Protection** – RL-empowered graph convolutional networks spot data integrity attacks.
  [Reinforcement Learning-Empowered Graph Convolutional Network Framework for Data Integrity Attack Detection in Cyber-Physical Systems](https://doi.org/10.17775/cseejpes.2023.01250).
- **Attack Resilience Scheduling** – federated heterogeneous multi-agent RL defends multi-integrated energy systems.
  [Federated Heterogeneous Multi-Agent Deep Reinforcement Learning-Based Attack Resilience Scheduling for Heterogeneous Multi-Integrated Energy System](https://doi.org/10.2139/ssrn.5233949).
- **Distribution Inference Attacks** – RL infers data distribution in federated learning.
  [Data Distribution Inference Attack in Federated Learning via Reinforcement Learning Support](https://doi.org/10.1016/j.hcc.2024.100235).
- **LLM-Based RL Agents for Bug Discovery** – RL-powered agents automatically uncover bugs in web applications.
  [Using LLM-Based Deep Reinforcement Learning Agents to Detect Bugs in Web Applications](https://doi.org/10.5220/0013248800003890).
- **Graph Poisoning via RL** – applies reinforcement learning to craft feature bias perturbations that degrade graph-based detectors.
  [Graph Poisoning Attack Based on Feature Bias Perturbation Via Reinforcement Learning](https://doi.org/10.2139/ssrn.5254394).
- **Ad-hoc Network Attack Identification** – reinforcement learning configures ad-hoc networks to surface malicious traffic.
  [Routing and Security Based Ad-hoc Networks Configuration for Identification of Attack Using Reinforcement Learning Approach](https://doi.org/10.21203/rs.3.rs-4045649/v1).
- **Cyber-Physical Attack Detection for Robotic Arms** – RL with heterogeneous data fusion spots anomalies in industrial robots.
  [Cyber-Physical Attack Detection in Industrial Robotic Arms by Reinforcement Learning with Systemic Heterogeneous Data Fusion](https://doi.org/10.2139/ssrn.5272672).
- **DDoS Mitigation via RL** – reinforcement learning policies counter distributed denial-of-service attacks.
  [Distributed Denial of Service Attack Mitigation Using Reinforcement Learning](https://doi.org/10.36676/j.sust.sol.v2.i1.54).
- **Risk-Sensitive RL for Smart Factories** – explores sabotage scenarios in human–robot symbiosis.
  [LLM-Guided Risk-Sensitive Reinforcement Learning for Smart Factories in the Scenario of Human-Robot Symbiosis](https://doi.org/10.2139/ssrn.5294964).
- **ProRLearn** – reinforcement learning improves prompt-tuning-based vulnerability detection.
  [ProRLearn: Boosting Prompt Tuning-based Vulnerability Detection by Reinforcement Learning](https://doi.org/10.21203/rs.3.rs-3856133/v1).
- **Deep RL Penetration Testing** – demonstrates penetration testing techniques using deep reinforcement learning.
  [PENETRATION TESTING USING DEEP REINFORCEMENT LEARNING](https://doi.org/10.28925/2663-4023.2024.23.1730).
- **Autonomous Threat Response Frameworks** – RL-enhanced cybersecurity frameworks for automated defence.
  [Reinforcement Learning Enhanced Cybersecurity Frameworks for Autonomous Threat Response Systems](https://doi.org/10.71443/9789349552319-10).
- **Deep Reinforcement Fuzzing** – early RL approach optimizing fuzzing with Q-learning.
  [Deep Reinforcement Fuzzing](https://arxiv.org/abs/1801.04589).
- **SyzVegas** – RL scheduling of syscall sequences improves kernel fuzzing odds.
  [SyzVegas: Beating Kernel Fuzzing Odds with Reinforcement Learning](https://www.usenix.org/conference/usenixsecurity21/presentation/wang-daimeng).
- **RL-Fuzz** – reinforcement learning guided fuzz testing with dynamic reward shaping.
  [RL-Fuzz: Reinforcement Learning Guided Fuzz Testing](https://doi.org/10.1016/j.jss.2024.111963).
- **Dynamic Embeddings for Ransomware** – RL with Bayesian networks enhances resilience.
  [Leveraging Dynamic Embeddings and Reinforcement Learning with Bayesian Networks for Ransomware Resiliences](https://www.sciencedirect.com/science/article/pii/S2772918425000128).
- **Deep VULMAN** – RL-enabled vulnerability management automatically prioritizes patches.
  [Deep VULMAN: A Deep Reinforcement Learning-Enabled Cyber Vulnerability Management Framework](https://www.sciencedirect.com/science/article/pii/S095741742300235X).
- **Code Vulnerability Repair** – uses RL with semantic reward to patch code.
  [LLM-Powered Code Vulnerability Repair with Reinforcement Learning and Semantic Reward](https://arxiv.org/abs/2401.03374).
- **Hierarchical MARL Defence** – organizes RL agents hierarchically to identify attack paths.
  [Hierarchical Multi-agent Reinforcement Learning for Cyber Network Defense](https://arxiv.org/abs/2410.17351).
- **Intrusion Detection in SCADA** – deep RL model locates malicious SCADA activity.
  [Leveraging Deep Reinforcement Learning Technique for Intrusion Detection in SCADA Infrastructure](https://ieeexplore.ieee.org/document/10504835).
- **Phishing Prevention via RL** – RL algorithms adapt to new phishing techniques.
  [AI-Driven Phishing Detection: Enhancing Cybersecurity with Reinforcement Learning](https://www.mdpi.com/2624-800X/5/2/26).
- **Comprehensive Survey** – classification of RL methods for cybersecurity.
  [Multi-Agent Reinforcement Learning for Cybersecurity: Classification and Survey](https://www.sciencedirect.com/science/article/pii/S2667305325000213).

- **When LLM Meets DRL** – integrates deep RL with LLM-driven search to automate jailbreak discovery.
  [When LLM Meets DRL: Advancing Jailbreaking Efficiency via DRL-guided Search](https://www.semanticscholar.org/paper/ff9854d4323e75252fec985d411f3b058eb718bf).
- **PathSeeker** – explores LLM vulnerabilities using a reinforcement learning-based jailbreak approach.
  [PathSeeker: Exploring LLM Security Vulnerabilities with a Reinforcement Learning-Based Jailbreak Approach](https://www.semanticscholar.org/paper/26c1431f46f90b29b4ee8522ebce92de68068cbb).
- **xJailbreak** – representation space guided reinforcement learning enables interpretable jailbreaks.
  [xJailbreak: Representation Space Guided Reinforcement Learning for Interpretable LLM Jailbreaking](https://www.semanticscholar.org/paper/f88411c138583c3875009db49291e1daafc825ba).
- **Modeling Behavioral Preferences** – applies inverse RL to infer attacker behavior from audit logs.
  [Modeling Behavioral Preferences of Cyber Adversaries Using Inverse Reinforcement Learning](https://arxiv.org/abs/2505.03817).
- **Quantitative Resilience Modeling** – evaluates network resilience under RL-driven attacks and defences.
  [Quantitative Resilience Modeling for Autonomous Cyber Defense](https://arxiv.org/abs/2503.02780).
- **Multi-Agent RL Defence Tactics** – cooperative RL agents learn cyber defence strategies from scratch.
  [Learning Cyber Defence Tactics from Scratch with Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2310.05939).
- **CybORG Environment** – open-source RL framework for simulating automated network attack and defence.
  [CybORG](https://github.com/cyber-phys/cyborg).

Additional recent work also explores novel RL-driven jailbreak discovery methods:

- **Adaptive RL with LLM-Augmented Rewards** – leverages language model feedback
  to guide RL agents toward exploitable behaviors.
  [Adaptive Reinforcement Learning with LLM-augmented Reward Functions](https://doi.org/10.36227/techrxiv.24708198).
- **Visual Analytics for Jailbreak Prompt Discovery** – mines large conversational
  logs to surface emergent jailbreak prompts.
  [A Visual Analytics Approach for Jailbreak Prompts Discovery from Large-Scale Human-LLM Conversational Datasets](https://doi.org/10.1109/TVCG.2025.3557568).
- **Contextual Backdoor Attacks on LLM Agents** – demonstrates RL-guided backdoor
  triggers for embodied agents.
  [Compromising LLM Driven Embodied Agents with Contextual Backdoor Attacks](https://doi.org/10.1109/TIFS.2025.3555410).
- **Communication-Efficient Multi-Agent RL with LLMs** – studies RL cooperation
  with language-model-mediated communication.
  [Towards Communication Efficient Multi-Agent Cooperations: Reinforcement Learning and LLM](https://doi.org/10.36227/techrxiv.173739115.54193062/v1).
- **Transformer RL Attacks on Fake News Detectors** – uses RL to defeat automated
  misinformation detectors.
  [Transformer Reinforcement Learning Approach to Attack Automatic Fake News Detectors](https://doi.org/10.18122/td.2140.boisestate).

These works demonstrate that reinforcement learning can actively search
for exploits, generate sophisticated jailbreak sequences, and refine
attacks over time. Defenders should audit reward models and monitor for
signs of RL-driven probing to mitigate this threat.
