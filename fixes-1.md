Below is a **two-part deliverable** written entirely in Markdown:

* **Part A – Comprehensive Criticism** – what is wrong or incomplete in the repository *as-is*
* **Part B – Step-by-step Fix Plan** – an action-oriented backlog with numbered steps → sub-steps → tasks

> **Notation**
>
> * Levels: `#` = major section, `## n.` = step, `### n.m` = sub-step, `#### n.m.k` = concrete task
> * Inline citations appear at the end of the sentence they justify.
> * External references are normal Markdown links; repository evidence is cited with the `marker; web evidence with`.

---

# Part A – Comprehensive Criticism

## 1. Repository hygiene & structure flaws

* **1.1 File duplication** – The repo contains *three* copies of the same catalog file with different spellings (`Comprehensive Catalog of …`, the same name with underscores, and an extra copy in the root) .
* **1.2 Mixed conventions** – Folders use **kebab-case** (`timing-side-channel.html`), **snake\_case**, and **camelCase** interchangeably, impeding automated processing.
* **1.3 Orphan files** – `corrections-needed.md` is referenced nowhere; several HTML scraps (e.g. ACM cookie banners) were scraped verbatim and serve no catalog purpose .
* **1.4 Missing top-level README, CONTRIBUTING, LICENSE** – no onboarding guidance, legal clarity, or contribution workflow.

## 2. Content format inconsistencies

* **2.1 HTML vs. Markdown** – \~95 % of sources are raw HTML dumps; only the two/three catalog files are Markdown.
* **2.2 No front-matter metadata** – date, author, original URL, attack category, and license are lost once the HTML is converted.
* **2.3 Broken or truncated links** – long URLs were cut mid-query, yielding 404s (see many `utm_source=chatgpt.com` tails) .

## 3. Coverage gaps in the attack taxonomy

The catalog is strong on **prompt-injection** variants but misses entire classes of attacks:

| Missing class                            | Representative recent source                                             |
| ---------------------------------------- | ------------------------------------------------------------------------ |
| Model-extraction / theft                 | Alignment-Aware MEA paper (OpenReview, 2025) ([openreview.net][1])       |
| Training-data poisoning                  | Mechanism-centric poisoning study (arXiv 2025) ([arxiv.org][2])          |
| Membership-inference                     | 2025 survey on MIAs for LLMs ([arxiv.org][3])                            |
| Tokenization exploits                    | TokenBreak single-character bypass ([techradar.com][4])                  |
| Gradient leakage / model inversion       | (absent – see suggested additions in plan)                               |
| Reinforcement-learning alignment attacks | (absent)                                                                 |
| Safety-filter side-channel timing        | already partially covered (`timing-side-channel.html`) but lacks summary |

## 4. Broken knowledge graph & navigation

* **4.1 No global index.json / TOC** – users cannot query “show me all multimodal attacks.”
* **4.2 Duplicate OWASP Top-10 snapshot** – both `docs/overview/owasp-top10.html` and a *second* copy embedded in the catalog; versions differ .

## 5. Automation & CI gaps

* No link-checker, HTML→Markdown converter, dedupe linter, or coverage tests.
* `.gitignore` is Python-centric; repo is mostly documentation. Unused sections add noise .

## 6. Security & compliance concerns

* Raw HTML contains third-party scripts, cookies, and tracking pixels (e.g. **Cookiebot**, **Google Fonts**) that will load if served statically, violating researcher privacy and possibly licenses .
* No license; redistribution may infringe original articles.

---

# Part B – Step-by-step Fix Plan

> **Goal:** produce a *clean, complete, research-grade* catalog of **all** known or hypothesised LLM attacks, ready for downstream defence mapping.

---

## 1. Repository hygiene roadmap

### 1.1 ✂️ Deduplicate & normalise

1.1.1 Delete duplicate catalog files; keep **one** canonical Markdown file in `docs/`
1.1.2 Rename every file to `kebab-case.md` (attack-name.md) for consistency
1.1.3 Create a script (`scripts/rename.py`) to enforce casing rules via pre-commit

### 1.2 Add core project skeleton

1.2.1 `README.md` – purpose, scope, contribution checklist
1.2.2 `CONTRIBUTING.md` – style guide, front-matter schema, citation rules
1.2.3 `LICENSE` – choose CC-BY-4.0 (or similar) + third-party excerpt policy

---

## 2. Format & metadata unification

### 2.1 Convert HTML → Markdown

2.1.1 Use `pandoc --from html --to gfm` in CI
2.1.2 Strip tracking scripts and cookie banners during conversion
2.1.3 Embed YAML front-matter:

```yaml
title: "Timing Side-Channel Extraction"
category: "Inference"
source_url: "https://arxiv.org/abs/2411.18191"
date_collected: 2025-06-18
license: "Fair-Use excerpt"
```

### 2.2 Link-check & auto-fix

2.2.1 Add `lychee` to CI to detect 404s
2.2.2 Store original PDFs locally when license permits; otherwise cache metadata only

---

## 3. Attack-coverage expansion

### 3.1 Add missing theoretical / emerging vectors

#### 3.1.1 Model extraction

* Summarise Alignment-Aware MEA methods ([openreview.net][1])
* Include black-box query stealing, watermark evasion, LoRD, etc.

#### 3.1.2 Training-data poisoning

* Summarise mechanism-centric poisoning ([arxiv.org][2])
* Add *Dirty Label*, *Backdoor*, *Flash-freeze* scenarios

#### 3.1.3 Membership & property inference

* Base on 2025 survey ([arxiv.org][3]); cover preference-alignment MIAs

#### 3.1.4 Tokenization & encoding exploits

* TokenBreak single-character bypass ([techradar.com][4])
* UTF-8 homoglyph stuffing, embedding overflow

#### 3.1.5 Gradient leakage & inversion

* Add recent inversion attacks (e.g. LoRA leakage – **TODO** find latest paper)

> **Deliverable:** one new Markdown file per vector + updates to master catalog

### 3.2 Cross-modal & agentic attacks

3.2.1 Add multi-modal jailbreaks (image obscuring, audio steganography)
3.2.2 Document agent–toolchain privilege escalation (Auto-GPT / CrewAI)

---

## 4. Knowledge graph & navigation

### 4.1 TOC generator

4.1.1 Script (`scripts/build_index.py`) scans front-matter and emits `index.json` keyed by `category`, `sub_category`, `date`.

### 4.2 Visual site

4.2.1 Use **MkDocs** with `mkdocs-material` + Mermaid diagrams
4.2.2 Configure search; host via GitHub Pages

---

## 5. Continuous-integration hardening

### 5.1 Pre-commit hooks

5.1.1 markdown-lint, spell-checker, front-matter validator
5.1.2 Duplication detector (hash-based)

### 5.2 CI pipelines

5.2.1 Unit tests: link-checker must pass
5.2.2 Scheduled *weekly* GitHub Action: refresh external links & archive snapshots

---

## 6. Security & legal compliance

### 6.1 Script to scrub third-party JS

6.1.1 Regex remove `<script>` & cookie banners from converted Markdown
6.1.2 Store only *static* artifacts (images, PDFs) when license permits

### 6.2 License alignment

6.2.1 For third-party text, keep ≤ 75 words excerpt + link (“fair use”)
6.2.2 Track license in front-matter (`license:` field)

---

## 7. Stretch goals

7.1 Publish an **SBOM** (CycloneDX) of sources for traceability
7.2 Build an *attack→defence* matrix (next phase)
7.3 Expose catalog via REST/GraphQL for automated tooling

---

**Outcome:** following the backlog above, the project will evolve from a folder of scraped HTML files into a clean, version-controlled, citation-rich knowledge base that truly “explores every possible theoretical or not attack” on LLMs while remaining maintainable and legally sound.

[1]: https://openreview.net/forum?id=AKsfpHc9sN&utm_source=chatgpt.com "Alignment-Aware Model Extraction Attacks on Large Language ..."
[2]: https://arxiv.org/html/2502.14182v1?utm_source=chatgpt.com "Multi-Faceted Studies on Data Poisoning can Advance LLM ... - arXiv"
[3]: https://arxiv.org/abs/2503.19338?utm_source=chatgpt.com "Membership Inference Attacks on Large-Scale Models: A Survey"
[4]: https://www.techradar.com/pro/security/this-cyberattack-lets-hackers-crack-ai-models-just-by-changing-a-single-character?utm_source=chatgpt.com "This cyberattack lets hackers crack AI models just by changing a single character"
