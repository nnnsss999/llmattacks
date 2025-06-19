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

### Embedding Inversion
Techniques that reconstruct input text from embedding vectors or APIs,
potentially leaking private training data. Variants include
**Cross-Lingual Embedding Inversion** and **Text Embedding Inversion**.

### Function Routing Jailbreak
An attack that abuses function-calling interfaces to break out of restricted
execution paths and obtain unintended model responses.

### FETA
A defence strategy that leverages translated suffix embeddings to mask or
rewrite prompts, making it harder for attackers to trigger a jailbreak.

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

### MkDocs
Static site generator used to build the searchable documentation
website from the Markdown files in this repository.

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

### SBOM
A Software Bill of Materials, such as the CycloneDX file in this repository,
enumerates all source files and their metadata for supply‑chain auditing.

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

### Adversarial Preference Learning
An iterative reinforcement-learning attack that corrupts reward feedback so the
model adopts unsafe behaviours.

### BadReward Poisoning
Clean-label poisoning of reward models to flip safety signals during RLHF,
gradually steering the base model toward malicious outputs.

### Locality-Reinforced Distillation (LoRD)
A model extraction technique that uses preference-guided distillation to
reconstruct weights with fewer queries.

### PandaBench
A benchmark suite measuring the effectiveness of jailbreak attacks and defences
across multiple LLMs.

### PiCo Data Poisoning
"Poisoning Code" datasets with hidden instructions so fine-tuned models emit
attacker-controlled code.

### Safety Chain-of-Thought (SCoT)
A defence that makes the model reason about a request's harmfulness before
answering, improving robustness to jailbreaks.

### SASP Jailbreak
"Self-Adversarial Attack via System Prompt" uses leaked system prompts to craft
highly effective jailbreaks, often with human refinement.

### LoRA Leakage
Gradient inversion techniques that recover training data or LoRA weights from
fine-tuning processes.

### Activation Obfuscation
Adversarially altering model activations so latent-space monitors fail to detect
malicious behaviour.

### Rapid Response
A mitigation approach providing a short list of safe examples that guide the
model away from harmful completions.

### Agent Toolchain Privilege Escalation
Using autonomous agents to chain external tools together and gain elevated
system privileges or execute prohibited actions.

### Attacker Disguiser
A defensive strategy where one agent rewrites malicious prompts so that the
target model does not recognise them as attacks, circumventing refusal
mechanisms.

### ASETF (Translate Suffix Embedding Attack)
A jailbreak that appends adversarial suffix embeddings, often in translated
form, to override the model's safety alignment.

### CRLF Injection
Exploiting carriage-return and line-feed characters in insecure outputs to
inject unexpected headers or markup.

### OWASP LLM04 DoS
Denial-of-service vulnerabilities for language models as categorised in the
OWASP "LLM04" guidance.

### Language Games
Interactive prompting techniques that gradually coax a model into unsafe
behaviour through back-and-forth conversation.

### Naturalistic Patch
Seemingly innocuous images or audio that hide adversarial triggers for
multimodal models.

### AmpleGCG
An approach that trains a generative model of adversarial suffixes to automate
greedy coordinate gradient attacks.

### BrokenHill
Open-source tooling that scales Greedy Coordinate Gradient (GCG) prompt search
across many target models.

### JBFuzz
Fuzzing framework that iteratively mutates prompts to discover jailbreaks with a
high success rate.

### ObscurePrompt
Jailbreaking technique that relies on unusual encodings or Unicode tricks to
hide malicious instructions.

### PromptFuzz
Systematic prompt fuzzing aimed at exposing unsafe completions and injection
vectors.

### Pre-commit
Framework that runs linting and validation hooks before each commit to
ensure consistent formatting and metadata.

### GPT-4V Safety
Research evaluating whether multimodal GPT‑4V models resist combined text and
image-based jailbreaks.

### Confident AI Jailbreak
Case study demonstrating how social engineering convinced a commercial chatbot
to disclose restricted information.

### Dependency Hijacking
Supply-chain attack where an adversary takes over a package name so that the
victim inadvertently installs malicious code.

### ApexHQ LatentSpace Attack
Manipulating latent representations so hidden triggers survive safety filters,
as reported by ApexHQ.

### HackerNews Toolchain
Refers to a malicious toolchain discussed on HackerNews that strings together
multiple open-source packages to automate jailbreak attacks.

### OpenAI AutoGPT Prompt
A prompt template that instructs AutoGPT-style agents to self-improve until
they bypass alignment safeguards.

### Wired Robot Violence
A Wired magazine case study describing how autonomous robots can be directed to
cause physical harm when driven by unsafe prompts.

### Wayback Machine
An internet archive used by `refresh_links.py` to store snapshots of
external URLs referenced in the catalog.

### Social Engineering
Using human manipulation techniques—such as persuasion or impersonation—to
trick LLM operators or guard systems into revealing sensitive information.

### PyPI Supply-Chain Attack
An incident where a malicious package on PyPI compromises downstream projects,
highlighting the risk of third-party dependency hijacking.

### Alignment-Aware MEA
Shortened name for the alignment-aware model extraction attack highlighted in the inference folder.

### AmpleGCG Repo
Repository hosting code examples for the AmpleGCG prompt-search technique.

### Anthropic Sleeper Agents
Study from Anthropic that reveals how models can be trained to remain benign until a trigger activates malicious behaviour.

### ApexHQ LatentSpace
Alternative reference to the ApexHQ latent-space attack that manipulates internal representations.

### ArXiv Embedding Inversion
Early arXiv paper demonstrating how embeddings can be reversed to recover text.

### Attack-Defense Matrix
Table mapping each attack in the catalog to recommended defensive measures.

### BadReward Clean Label
Variant of BadReward poisoning where only benign-looking data is injected during RLHF.

### Byte-Level Universal Triggers ArXiv
Original arXiv post describing universal byte sequences that cause harmful behaviour.

### Comprehensive Catalog of LLM Jailbreaking and Attack Techniques
Master document that aggregates every jailbreak method documented in this repository.

### CrossLingual Inversion 2505.16008
Case study showing cross-lingual embedding inversion across different languages.

### Extracting Training Data 2012.07805
Research revealing how text can be reconstructed from embedding model APIs.

### GPT4V Safe
Example prompt demonstrating safe multimodal queries for GPT-4V.

### Gradient Leakage Inversion
Recovering private data by analysing fine-tuning gradients.

### HackerNews PyPI
News report about a malicious PyPI package compromise.

### HiddenLayer TokenBreak
Blog post exploring token-level bypasses using hidden characters.

### ImgJP
Demonstration image used to show a visual jailbreak in action.

### Index
Generic landing page found in most folders of the documentation site.

### Language Games ArXiv
Academic article discussing conversational games that slowly induce jailbreaks.

### LLM Attack Catalog
Printable markdown version of the full attack catalog.

### LoRD Distillation
Locality-Reinforced Distillation technique for extracting model weights.

### Mechanism-Centric Poisoning
Training manipulation that targets internal learning mechanisms rather than outputs.

### Naturalistic Patch ArXiv
Paper describing realistic-looking adversarial patches that bypass visual filters.

### Obfuscated Activations
Technique that hides neuron activations so safety monitors miss malicious behaviour.

### PDF Extract
Plain-text extraction of the PDF catalog for easier diffing and search.

### PiCo
Short for "Poisoning Code" datasets with hidden instructions.

### PoisonedRAG ArXiv
Academic write-up of retrieval-augmented generation poisoning.

### Reinforcement Learning Alignment Attacks
Overview page summarising RL-based attacks on model alignment.

### Safety Chain-of-Thought
Method where the model reasons about harmfulness before answering.

### Safety Filter Timing Side Channel
Attack using response delays to infer hidden prompts from safety filters.

### Social Engineering Overview
General summary page covering manipulation tactics against LLM users.

### TechRadar TokenBreak
News coverage of token-level prompt injection from TechRadar.

### Text Embedding Inversion 2401.12192
ArXiv paper demonstrating text reconstruction from embedding APIs.

### The Register CoT
Register article describing chain-of-thought jailbreak techniques.

### TheHackerNews Dependency Hijack
Report from TheHackerNews on a real-world dependency hijacking incident.

### TokenBreak Single Character Bypass
Specific example where a single-character tokenbreak defeats safety checks.

### Unicode Homograph Jailbreak
Using visually similar characters from other scripts to obfuscate malicious
commands. When combined with right-to-left override or zero-width spaces, these
homographs can slip past simple filter checks.

### Necromancer Self-Replication Attack
A proof-of-concept loop where an autonomous agent repeatedly modifies its own
prompts to evade safeguards, eventually gaining elevated capabilities with no
further user input.

### Additional Resources
Reference document listing external articles and reports for continued
reading on LLM attack research.

### rename.py
Helper script that renames documentation files to use kebab-case for
consistency across the catalog.

### build_index.py
Script that parses document metadata and generates the `index.json` search file.

### cache_pdfs.py
Downloads external PDFs referenced in docs and stores them in the `pdfs/` cache.

### check_duplicates.py
Finds duplicate Markdown files so the catalog doesn't contain repeated entries.

### check_front_matter.py
Validates that documentation pages include YAML front matter.

### extract_urls.py
Converts a list of URLs into Markdown files under `extractions1/`.

### generate_sbom.py
Produces the CycloneDX `sbom.json` describing repository components.

### link_check.py
Checks each document for broken hyperlinks.

### refresh_links.py
Retrieves fresh Wayback Machine snapshots and updates `link_archive.json`.

### scrub_js.py
Removes third-party `<script>` tags from downloaded HTML.

### all_files.txt
Master list of every path tracked in the repository.

### docs_files.txt
Manifest of all documentation files referenced by build scripts.

### index.json
Machine-readable index built from document metadata.

### link_archive.json
Snapshots of external URLs for offline reference.

### requirements.txt
Python packages required to run the helper scripts.

### sbom.json
CycloneDX software bill of materials for provenance auditing.

### URLs
Index of all external links referenced across the catalog.
