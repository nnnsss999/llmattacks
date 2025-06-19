---
title: "Fuzzing-Based LLM Attack Techniques"
category: "Inference"
source_url: ""
date_collected: 2025-06-18
license: "CC-BY-4.0"
---

Fuzzing approaches repeatedly generate slightly mutated inputs to probe a model for vulnerabilities. Recent work applies this technique to large language models, often to automate jailbreak discovery.

## Notable Resources

- **LLMFuzzer** – open-source fuzzing framework for LLM applications. It automates seed selection and prompt mutation to uncover jailbreak paths. [GitHub](https://github.com/mnns/LLMFuzzer)
- **Fuzz4All** – ICSE 2024 paper introducing a universal fuzzing loop powered by LLM autoprompting. [arXiv](https://arxiv.org/abs/2308.04748)
- **FuzzyAI Fuzzer** – CyberArk tool for automated LLM fuzzing and API security assessment. [GitHub](https://github.com/cyberark/FuzzyAI)
- **OSS-Fuzz-Gen** – Google framework that uses LLMs to create fuzz targets for OSS-Fuzz. [GitHub](https://github.com/google/oss-fuzz-gen)
- **ChatAFL** – protocol fuzzer guided by LLMs, extending AFLNet to reach new server states. [GitHub](https://github.com/ChatAFLndss/ChatAFL)
- **Large Language Models Based Fuzzing Techniques: A Survey** – overview of LLM-driven fuzzing methodologies. [arXiv](https://arxiv.org/abs/2402.00350)
- **AI-Powered Fuzzing: Breaking the Bug Hunting Barrier** – Google blog discussing fuzz target generation with generative models. [Security Blog](https://security.googleblog.com/2023/08/ai-powered-fuzzing-breaking-bug-hunting.html)
- **Evaluating Large Language Models for Enhanced Fuzzing** – IEEE paper presenting an analysis framework for LLM-driven seed generation. [IEEE Xplore](https://ieeexplore.ieee.org/document/10731701)

These references illustrate how fuzzing techniques are evolving to test LLM safety and security. Incorporating LLM-driven mutation and evaluation loops enables broader exploration of model behavior and potential jailbreaks.
