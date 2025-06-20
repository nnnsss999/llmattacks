---
title: "Latent Space Attack Resources 2040"
category: "Latent Space"
source_url: ""
date_collected: 2025-07-25
license: "CC-BY-4.0"
---

The references below extend the latent-space catalog with newly discovered exploits and countermeasures that emerged after the [2039 update](latent-space-resources-2039.md).
They highlight backdoor techniques in diffusion models, novel embedding leakage, and mitigation guidance.

- [SG-LSBA: Semantic Latent Space Backdoor Attack on Stable Diffusion](https://link.springer.com/chapter/10.1007/978-981-96-4509-1_8) – demonstrates semantically guided triggers hidden in diffusion latents.
- [Layer Frozen Multi-Net & Latent Space Feature-Concealed Backdoor Attack in Transformers](https://www.sciencedirect.com/science/article/pii/S0893608025003764) – hides triggers by freezing layers and manipulating latent features.
- [Backdoor Defense in Diffusion Models via Spatial Attention Unlearning](https://arxiv.org/abs/2504.18563) – unlearns malicious attention patterns to sanitize hidden representations.
- [Semantic-Guided Latent Space Backdoor Attack: a Novel Approach](https://easychair.org/publications/preprint/wfDd) – crafts targeted triggers using semantic guidance during latent optimization.
- [Latent Diffusion Shield: Mitigating Malicious Use of Diffusion Models](https://openaccess.thecvf.com/content/WACV2025W/SynRDinBAS/html/Phan_Latent_Diffusion_Shield_-_Mitigating_Malicious_Use_of_Diffusion_Models_WACVW_2025_paper.html) – defensive technique against hidden diffusion backdoors.
- [Joint Embedding vs Reconstruction: Provable Benefits of Latent Space Pre-Alignment](https://arxiv.org/abs/2505.12477) – analyzes embedding pre-alignment to resist inversion attacks.
- [Distributional Black-Box Model Inversion Attack With Multi-Agent Strategy](https://ieeexplore.ieee.org/document/10976441) – coordinates multiple queries to reconstruct latent information.
- [Poison-RAG: Adversarial Data Poisoning Attacks on Retrieval-Augmented Generation](https://arxiv.org/abs/2501.11759) – corrupts vector stores so latent retrieval pipelines output malicious context.
- [Vector Drift, Prompt Injection, and the Hidden RAG Attack Surface](https://securitysandman.com/2025/06/10/vector-drift-prompt-injection-and-the-hidden-ai-rag-attack-surface/) – discusses how latent vector drift enables stealthy RAG manipulations.
- [OWASP GenAI LLM08:2025 Vector and Embedding Weaknesses](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/) – official guidance covering latent-space vulnerabilities.
