---
title: "Glossary"
category: "Overview"
source_url: ""
date_collected: 2025-06-18
license: "CC-BY-4.0"
---

This glossary defines common terms found across the **LLM Attacks Catalog**.
It provides quick reference explanations for attacks, defences and research
concepts mentioned in the repository.

## Terms

### Agentic
Refers to autonomous agent toolchains that can perform actions without direct
human oversight. In this catalog it includes attacks where such agents are
used to gain elevated privileges or cause real-world effects.

### Alignment-Aware Model Extraction
A technique that steals parameters from a target model while retaining or even
improving alignment properties. The associated attack shows how gradient
information can be leveraged to copy an LLM.

### Audio Steganography Jailbreak
Embedding hidden instructions in audio files that are decoded by multimodal
models to bypass safety filters.

### Byte-Level Universal Triggers
Short sequences of bytes that consistently elicit harmful behaviour across
models when appended to inputs.

### Chain-of-Thought
A prompting approach that requests the model to reason step by step. Attackers
can misuse this to guide the model toward unsafe content.

### Function Routing Jailbreak
An attack that abuses function-calling interfaces to break out of restricted
execution paths and obtain unintended model responses.

### Gradient Leakage
The unintended exposure of gradient information during model fine-tuning or
inference, which can reveal training data or enable model extraction.

### Image Obscuring Jailbreak
Using carefully crafted images to hide malicious prompts that are revealed only
after preprocessing, bypassing visual safety checks.

### Membership Inference
A privacy attack that determines whether specific data was used during model
training by analysing outputs or gradients.

### Mechanism-Centric Data Poisoning
Targeted poisoning of the training process that manipulates the internal
mechanisms of a model rather than just its outputs.

### PoisonedRAG
Retrieval-Augmented Generation systems can be subverted when their external
knowledge source is poisoned with crafted documents that alter generation
behaviour.

### Reverse Preference Attack
Flipping reward signals during reinforcement learning to gradually steer a model
away from its safety alignment.

### Sleeper Agent
A model trained to behave normally until triggered by a specific cue, at which
point it performs malicious actions.

### Timing Side-Channel
Extracting information about hidden prompts or model states by measuring
differences in response times.

### TokenBreak
A family of prompt manipulation techniques that exploit tokenisation quirks
(such as inserting zero-width characters) to confuse safety filters.

### VentureBeat Diffusion Backdoor
A diffusion-model attack described by VentureBeat where training data is
poisoned to embed a hidden trigger, causing malicious generation when activated.

### Visual Jailbreaking
General term for attacks that use images or video frames to smuggle prompts past
content filters in multimodal models.
