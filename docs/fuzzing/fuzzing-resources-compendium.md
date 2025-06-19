---
title: "Fuzzing Resources Compendium"
category: "Fuzzing"
source_url: ""
date_collected: 2025-06-19
license: "CC-BY-4.0"
---

This document aggregates references on fuzzing techniques for large language models from across the repository.

## Papers and Articles
- [LLM-Fuzzer: Scaling Assessment of Large Language Model Jailbreaks](https://www.usenix.org/conference/usenixsecurity24/presentation/yu-jbfuzz)
- [JBFuzz: Jailbreaking LLMs Efficiently and Effectively Using Fuzzing](https://arxiv.org/abs/2403.11315)
- [Large Language Models Based Fuzzing Techniques: A Survey](https://arxiv.org/abs/2402.00350)
- [Fuzz4All: Universal Fuzzing with Large Language Models](https://arxiv.org/abs/2308.04748)
- [TurboFuzzLLM: Turbocharging Mutation-based Fuzzing for Effectively Jailbreaking Large Language Models in Practice](https://arxiv.org/abs/2502.18504)
- [ProphetFuzz: Fully Automated Prediction and Fuzzing of High-Risk Option Combinations](https://arxiv.org/abs/2409.00922)
- [PromptFuzz: Coverage-Guided Fuzz Driver Generation with LLMs](https://dl.acm.org/doi/10.1109/ICSE-Companion.2025.0079)
- [AgentVigil: Generic Black-Box Red-teaming for Indirect Prompt Injection against LLM Agents](https://arxiv.org/abs/2505.05849)
- [Feedback-Guided Fuzzing Reveals LLM Blind Spots](https://www.crowdstrike.com/en-us/blog/feedback-guided-fuzzing-reveals-llm-blind-spots/)
- [LLAMAFUZZ: Large Language Model Enhanced Greybox Fuzzing](https://arxiv.org/abs/2406.07714)
- [KernelGPT: Enhanced Kernel Fuzzing via Large Language Models](https://arxiv.org/abs/2401.00563)
- [Towards Reliable LLM-Driven Fuzz Testing: Vision and Road Ahead](https://arxiv.org/abs/2503.00795)
- [How Effective Are They? Exploring Large Language Model Based Fuzz Driver Generation](https://arxiv.org/abs/2307.12469)
- [When Fuzzing Meets LLMs: Challenges and Opportunities](https://arxiv.org/abs/2404.16297)
- [Does Fuzzing LLMs Actually Work?](https://www.promptfoo.dev/blog/llm-fuzzing/)
- [FuzzMeetLLM FSE24 Paper](http://www.wingtecher.com/themes/WingTecherResearch/assets/papers/paper_from_24/FuzzMeetLLM_FSE24.pdf)
- [LLM4Fuzz: Guided Fuzzing of Smart Contracts with Large Language Models](https://arxiv.org/abs/2401.11108)
- [ClusterFuzzAI: Scaling Fuzzing with LLM-Augmented Agents](https://github.com/google/clusterfuzzai)
- [FlowFuzz: LLM-Aware Data-Flow Fuzzing](https://arxiv.org/abs/2412.18001)
- [Neural FuzzLab: Auto-scaling LLM Fuzzing Benchmarks](https://arxiv.org/abs/2411.20052)
- [ChatHTTPFuzz: Large Language Model-Assisted IoT HTTP Fuzzing](https://doi.org/10.1007/s13042-024-02527-3)
- [N\u00fcwa: Enhancing MLIR Fuzzing with LLM-Driven Generation and Adaptive Mutation](https://conf.researchr.org/details/icsme-2025/icsme-2025-papers/36/N-wa-Enhancing-MLIR-Fuzzing-with-LLM-Driven-Generation-and-Adaptive-Mutation)
- [Magneto: A Step-Wise Approach to Exploit Vulnerabilities in Dependent Libraries via LLM-Empowered Directed Fuzzing](https://ieeexplore.ieee.org/document/10764966)
- [FuzzLGen: Logical Seed Generation for Smart Contract Fuzzing](https://www.ndss-symposium.org/wp-content/uploads/2025-poster-23.pdf)
- [LLM-guided Wi-Fi Fuzzing](https://www.esat.kuleuven.be/cosic/thesis/2026/LLM-guided_Wi-Fi_Fuzzing.pdf)
- [Fuzzing LLMs Sometimes Makes Them Reveal Their Secrets](https://www.lesswrong.com/posts/GE6pcmmLc3kdpNJja/fuzzing-llms-sometimes-makes-them-reveal-their-secrets)
- [Fuzzylabs Blog: Jailbreak Attacks on Large Language Models](https://www.fuzzylabs.ai/blog-post/jailbreak-attacks-on-large-language-models)
- [AI-based Vulnerability Fuzzer Discovers Critical Zero-Day](https://www.securityweek.com/ai-based-vulnerability-fuzzer-discovers-critical-zero-day/)

### Additional Papers and Industry Articles
- [Minimal LLM-based Fuzz Harness Generator](https://adalogics.com/blog/minimal-llm-based-fuzz-harness-generator)
- [Documentation-Driven Compiler Fuzzing with Large Language Models](https://gusarich.com/blog/fuzzing-with-llms/)
- [Brainstorm Tool Release: Optimizing Web Fuzzing With Local LLMs](https://www.invicti.com/blog/security-labs/brainstorm-tool-release-optimizing-web-fuzzing-with-local-llms/)
- [AI-based fuzzing targets open-source LLM vulnerabilities](https://www.reversinglabs.com/blog/automated-ai-fuzzing-targets-open-source-llm-vulnerabilities)
- [Fuzzing Workshop 2025](https://fuzzingworkshop.github.io/)
- [ISSTA 2025 Fuzzing Track](https://conf.researchr.org/home/issta-2025/fuzzing-2025)
- [Leveling Up Fuzzing: Finding more vulnerabilities with AI](https://security.googleblog.com/2024/11/leveling-up-fuzzing-finding-more.html)
- [2025-01-8091: LLM-Powered Fuzz Testing of Automotive Diagnostic Protocols](https://saemobilus.sae.org/papers/llm-powered-fuzz-testing-automotive-diagnostic-protocols-2025-01-8091)
- [FuzzyAI: Open-source Tool for Automated LLM Fuzzing](https://www.helpnetsecurity.com/2024/12/13/fuzzyai-automated-llm-fuzzing/)

## Tools and Repositories
- [FuzzAI Project](https://github.com/cyberark/FuzzyAI)
- [Prompt Fuzzer](https://www.prompt.security/fuzzer)
- [PromptFuzz GitHub repository](https://github.com/prompt-security/ps-fuzz)
- [OSS-Fuzz-Gen: LLM-Based Fuzz Target Generation](https://github.com/google/oss-fuzz-gen)
- [GPTFuzz Project](https://github.com/sherdencooper/GPTFuzz)
- [TurboFuzzLLM Project](https://github.com/amazon-science/TurboFuzzLLM)
- [CKGFuzzer Project](https://github.com/security-pride/CKGFuzzer)
- [LLMFuzzer](https://github.com/mnns/LLMFuzzer)
- [LLAMAFUZZ Repository](https://github.com/SecurityLab-UCD/LLAMAFUZZ)
- [KernelGPT Repository](https://github.com/ise-uiuc/KernelGPT)
- [CovRL-Fuzz Repository](https://github.com/seclab-yonsei/CovRL-Fuzz)
- [SyzLLM Repository](https://github.com/SpencerL-Y/SyzLLM)
- [PromptFuzz2 Repository](https://github.com/sherdencooper/PromptFuzz2)
- [Google ClusterFuzz Documentation](https://google.github.io/clusterfuzz/)
- [Honggfuzz Project](https://honggfuzz.dev)
- [LLVM LibFuzzer Guide](https://llvm.org/docs/LibFuzzer.html)
- [LLM-FuzzX Repository](https://github.com/Windy3f3f3f3f/LLM-FuzzX)
- [Fuzz Introspector Project](https://github.com/ossf/fuzz-introspector)
- [Fuzz4All Project Website](https://fuzz4all.github.io/)

These references consolidate the fuzzing resources spread across multiple documents in this repository, giving researchers a centralized starting point for further exploration.
