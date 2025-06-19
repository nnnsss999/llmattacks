---
title: "Repository Navigation Map"
category: "Overview"
source_url: ""
date_collected: 2025-06-18
license: "CC-BY-4.0"
---

This map lists all files in the repository and briefly describes their purpose.
Directories are shown as headings with bullet points for each file.

## Root Files
- `.gitignore` — patterns of files excluded from version control
- `.pre-commit-config.yaml` — configuration for markdown linting and duplicate checks
- `CONTRIBUTING.md` — guidelines for contributing to the catalog
- `LICENSE` — repository licensing information (MIT)
- `README.md` — overview of the project and usage instructions
- `fixes-1.md` — example issue log and fix plan
- `index.json` — machine-readable index of catalog entries generated from docs
- `link_archive.json` — cached external links for offline builds
- `mkdocs.yml` — configuration for the documentation site
- `sbom.json` — CycloneDX software bill of materials

## docs/
Primary source articles grouped by theme. Markdown files include YAML front matter; HTML files mirror external sources.

### agentic/
- `index.md` — introduction to agentic and physical-world misuse
- `agent-toolchain-priv-escalation.md` — privilege escalation via agent toolchains
- `hackernews-toolchain.html` — news article on malicious toolchains
- `openai-autogpt-prompt.html` — example AutoGPT jailbreak prompt
- `wired-robot-violence.html` — Wired coverage of real-world robot misuse

### defenses/
- `attacker-disguiser.html` — paper on disguising attacker prompts
- `feta.html` — FETA defence strategy
- `rapid-response.html` — rapid defence response overview

### emerging/
- `byte-level-universal-triggers-arxiv.html` — research on universal byte triggers
- `venturebeat-diffusion-backdoor.html` — diffusion model backdoor story

### evaluation/
- `pandabench.html` — benchmark suite for LLM defences

### inference/
- `alignment-aware-mea.md` — alignment-aware model extraction attacks
- `gradient-leakage-inversion.md` — gradient leakage and inversion via LoRA
- `lord-distillation.html` — distillation-based model leakage
- `membership-inference.md` — survey of membership inference attacks
- `membership-inference.html` — news article on membership inference
- `owasp-llm04-dos.html` — OWASP denial-of-service guidance
- `safety-filter-timing-side-channel.md` — timing side-channel in safety filters
- `timing-side-channel.html` — blog post on timing attacks
- `timing-side-channel.md` — detailed timing side-channel extraction

### insecure-output/
- `crlf-injection.html` — carriage-return line-feed injection example
- `function-routing-jailbreak.html` — abuse of function-calling routing

### latent-space/
- `apexhq-latentspace.html` — attack on latent representations
- `obfuscated-activations.html` — obfuscating activations during alignment

### linguistic-manipulation/
- `language-games-arxiv.html` — paper on language games for red-teaming

### multimodal/
- `audio-steganography-jailbreak.md` — audio-based hidden prompts
- `image-obscuring-jailbreak.md` — obscured image jailbreak technique
- `imgJP.html` — visual jailbreak demonstration
- `naturalistic-patch-arxiv.html` — adversarial patch attack paper
- `visual-jailbreaking.html` — blog post on visual jailbreaks

### optimization/
- `amplegcg.html` — prompt search with Monte Carlo
- `amplegcg-repo.html` — source repository page for the above
- `brokenhill.html` — BrokenHill dataset introduction
- `jbfuzz.html` — fuzzing prompts with jbfuzz
- `obscureprompt.html` — optimization technique for hidden prompts
- `promptfuzz.html` — automated prompt fuzzing

### prompt-dialogue/
- `gpt4v-safe.html` — safe multimodal prompt
- `hiddenlayer-tokenbreak.html` — TokenBreak attack blog
- `naturalistic-patch.html` — naturalistic patch jailbreak
- `safety-chain-of-thought.html` — chain-of-thought style jailbreak
- `sasp-jailbreak.html` — SASP jailbreak example
- `techradar-tokenbreak.html` — TechRadar article on tokenbreak
- `the-register-cot.html` — chain-of-thought coverage from The Register
- `tokenbreak-single-character-bypass.md` — single-character TokenBreak bypass

### rag/
- `poisonedrag-arxiv.html` — academic work on RAG poisoning
- `poisonedrag.html` — blog post explaining PoisonedRAG

### social-engineering/
- `confident-ai-jailbreak.html` — case study of social engineering a chatbot
- `social-engineering-overview.html` — summary of social engineering risks

### supply-chain/
- `hackernews-pypi.html` — story on PyPI supply-chain risks
- `thehackernews-dependency-hijack.html` — dependency hijacking example

### token-level/
- `techradar-tokenbreak.html` — token level manipulation article

### training-alignment/
- `index.md` — overview of training-phase attacks
- `anthropic-sleeper-agents.html` — sleeper agents research summary
- `mechanism-centric-poisoning.md` — mechanism-centric poisoning methods
- `pico.md` — description of PICO data poisoning
- `reinforcement-learning-alignment-attacks.md` — RL alignment attack taxonomy
- `reverse-preference-attack.html` — deep dive on reverse preference attacks

### Other docs
- `Comprehensive Catalog of LLM Jailbreaking and Attack Techniques.md` — master catalog document
- `attack-defense-matrix.md` — mapping of attacks to defences
- `index.md` — landing page for the documentation site
- `pdf-extract.md` — plain text extracted from the PDF catalog

## original/
Original sources of the catalog in PDF and Markdown.
- `Comprehensive Catalog of LLM Jailbreaking and Attack Techniques.md` — master
  Markdown source for the catalog
- `Comprehensive Catalog of LLM Jailbreaking and Attack Techniques.pdf` — PDF
  version of the same document

## pdfs/
Local cache for PDFs.
- `README.md` — explains the hashing scheme for cached PDFs

## scripts/
Utility scripts for building and checking the catalog.
- `build_index.py` — regenerate `index.json`
- `cache_pdfs.py` — download and store external PDFs
- `check_duplicates.py` — detect duplicate content in docs
- `check_front_matter.py` — validate YAML headers
- `generate_sbom.py` — produce `sbom.json`
- `link_check.py` — scan for broken links
- `refresh_links.py` — archive and update remote URLs
- `scrub_js.py` — remove third-party JavaScript

## tests/
- `test_link_check.py` — unit test for the link checker
- `test_sbom.py` — unit test for SBOM generation
