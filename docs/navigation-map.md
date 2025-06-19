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
- `docs_files.txt` — list of document paths used by build scripts
- `all_files.txt` — complete inventory of repository files
- `requirements.txt` — Python dependencies for the helper scripts

## .github/workflows/
- `ci.yml` — runs linting and tests on push
- `gh-pages.yml` — deploys documentation to GitHub Pages
- `link-check.yml` — checks external links
- `refresh-links.yml` — updates archived links weekly

## docs/
Primary source articles grouped by theme. Markdown files include YAML front matter; HTML files mirror external sources.

### agentic/
- `index.md` — introduction to agentic and physical-world misuse
- `agent-toolchain-priv-escalation.md` — privilege escalation via agent toolchains
- `hackernews-toolchain.html` — news article on malicious toolchains
- `openai-autogpt-prompt.html` — example AutoGPT jailbreak prompt
- `wired-robot-violence.html` — Wired coverage of real-world robot misuse
- `necromancer-attack.md` — self-replicating agent attack

### defenses/
- `attacker-disguiser.html` — paper on disguising attacker prompts
- `feta.html` — FETA defence strategy
- `rapid-response.html` — rapid defence response overview

### embedding/
- `index.md` — overview of embedding inversion threats
- `arxiv-embedding-inversion.html` — research on embedding inversion
- `crosslingual-inversion-2505.16008.html` — cross-lingual inversion case study
- `extracting-training-data-2012.07805.html` — extracting training data from embedding models
- `text-embedding-inversion-2401.12192.html` — text embedding inversion methods

### emerging/
- `byte-level-universal-triggers-arxiv.html` — research on universal byte triggers
- `venturebeat-diffusion-backdoor.html` — diffusion model backdoor story

### evaluation/
- `pandabench.html` — benchmark suite for LLM defences

### inference/
- `alignment-aware-mea.md` — alignment-aware model extraction attacks
- `gradient-leakage-inversion.md` — gradient leakage and inversion via LoRA
- `lord-distillation.html` — distillation-based model leakage
- `malware-generation-llm.md` — abuse of jailbroken models to craft malware
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
- `latent-space-attack-resources.md` — curated latent space references
- `apexhq-latentspace.html` — attack on latent representations
- `obfuscated-activations.html` — obfuscating activations during alignment

### linguistic-manipulation/
- `language-games-arxiv.html` — paper on language games for red-teaming
- `additional-resources.md` — recent cross-lingual attack papers

### multimodal/
- `audio-steganography-jailbreak.md` — audio-based hidden prompts
- `image-obscuring-jailbreak.md` — obscured image jailbreak technique
- `imgjp.html` — visual jailbreak demonstration
- `naturalistic-patch-arxiv.html` — adversarial patch attack paper
- `visual-jailbreaking.html` — blog post on visual jailbreaks
- `visual-jailbreaking-resources.md` — curated references on multimodal jailbreaks
- `image-based-attack-resources.md` — additional references on using images for jailbreaks
- `steganography-resources-2026.md` — latest papers on covert LLM attacks

### optimization/
- `amplegcg.html` — prompt search with Monte Carlo
- `amplegcg-repo.html` — source repository page for the above
- `brokenhill.html` — BrokenHill dataset introduction
- `jbfuzz.html` — fuzzing prompts with jbfuzz
- `open-sesame-ga.md` — genetic algorithm for universal jailbreaks
- `obscureprompt.html` — optimization technique for hidden prompts
- `promptfuzz.html` — automated prompt fuzzing
- `projected-gradient-descent-attack.md` — PGD-based jailbreaks
- `tag-gradient-attack.md` — early gradient attack on transformers
- `gradient-based-adversarial-transformers.md` — adversarial distribution search
- `gradient-attack-resources.md` — additional readings on gradient-based jailbreaks

### prompt-dialogue/
- `gpt4v-safe.html` — safe multimodal prompt
- `hiddenlayer-tokenbreak.html` — TokenBreak attack blog
- `naturalistic-patch.html` — naturalistic patch jailbreak
- `safety-chain-of-thought.html` — chain-of-thought style jailbreak
- `sasp-jailbreak.html` — SASP jailbreak example
- `techradar-tokenbreak.html` — TechRadar article on tokenbreak
- `the-register-cot.html` — chain-of-thought coverage from The Register
- `tokenbreak-single-character-bypass.md` — single-character TokenBreak bypass
- `unicode-homograph-jailbreak.md` — homograph-based jailbreak technique

### rag/
- `poisonedrag-arxiv.html` — academic work on RAG poisoning
- `poisonedrag.html` — blog post explaining PoisonedRAG

### social-engineering/
- `confident-ai-jailbreak.html` — case study of social engineering a chatbot
- `social-engineering-overview.html` — summary of social engineering risks
- `emotional-manipulation-resources.md` — social engineering and emotional manipulation references

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
- `gradient-hacking.md` — discussion of gradient manipulation threats

### data-poisoning/
- `index.md` — overview of data poisoning attacks
- `badreward-clean-label.md` — clean-label poisoning of reward models
- `adversarial-preference-learning.md` — adversarial preference corruption

### Other docs
- `comprehensive-catalog-of-llm-jailbreaking-and-attack-techniques.md` — master catalog document
- `attack-defense-matrix.md` — mapping of attacks to defences
- `index.md` — landing page for the documentation site
- `pdf-extract.md` — plain text extracted from the PDF catalog
- `glossary.md` — definitions of common terms across the catalog
- `navigation-map.md` — this file describing all repository contents
- `additional-resources.md` — curated external readings
- `zero-day-resources.md` — references on newly disclosed LLM vulnerabilities
- `urls.md` — list of referenced URLs used for analysis
- `llm-attack-catalog.md` — printable markdown version of the master catalog

## original/
Original sources of the catalog in PDF and Markdown.
- `Comprehensive Catalog of LLM Jailbreaking and Attack Techniques.md` — master
  Markdown source for the catalog
- `Comprehensive Catalog of LLM Jailbreaking and Attack Techniques.pdf` — PDF
  version of the same document

## pdfs/
Local cache for PDFs.
- `README.md` — explains the hashing scheme for cached PDFs

## extractions1/
Legacy extraction directory from earlier runs.
- `.gitkeep` — placeholder so the directory remains tracked

## @extractions1/
Current output folder for URL extractions.
- `extraction_log.json` — mapping of archived URLs to hashed files
- `*.md` — hashed Markdown snapshots of the linked pages

## scripts/
Utility scripts for building and checking the catalog.
- `build_index.py` — regenerate `index.json`
- `cache_pdfs.py` — download and store external PDFs
- `extract_urls.py` — convert external links into Markdown under `extractions1/`
- `check_duplicates.py` — detect duplicate content in docs
- `check_front_matter.py` — validate YAML headers
- `generate_sbom.py` — produce `sbom.json`
- `link_check.py` — scan for broken links
- `refresh_links.py` — archive and update remote URLs
- `scrub_js.py` — remove third-party JavaScript
- `rename.py` — enforce kebab-case filenames

## tests/
- `test_link_check.py` — unit test for the link checker
- `test_sbom.py` — unit test for SBOM generation
