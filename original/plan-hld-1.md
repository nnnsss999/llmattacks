Below is a **concise yet exhaustive road-map** you can hand to agents & junior devs.
It is organised as a numbered hierarchy you can copy-paste straight into an issue-tracker.
Every top-level item ends with the concrete *artefact* you should expect when the task is done.
Inline brackets (`➡️ …`) show which later tasks depend on each step, so teams can work in parallel.

---

## 0 · Validate requirements & scope (you are here)

1. **Goal recap** – *“ Ship a lean repo that: (a) has complete attack research, (b) proposes practical mitigations, (c) culminates in a small classifier that says ‘attack / not-attack’. ”*
2. **Anti-goals** – We are **not** shipping a red-team SaaS, an enterprise SIEM, or a full guard-railing framework like the competitor’s giant proposal in *llm-attacks-v2.md*&#x20;

---

## 1 · Identify missing research

| Gap                                                                | Source of truth to compare against                                      | How to close it                                                             |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Indirect / “data-layer” prompt-injection                           | OWASP LLM Top 10 – LLM01 & LLM05 ([owasp.org][1], [genai.owasp.org][2]) | Add **`attacks/indirect-inj/`** examples harvested from HTML/Markdown feeds |
| Multi-step context-switch jailbreaks                               | Jailbreak evolution study ([arxiv.org][3])                              | Script conversations that span ≥3 turns to force context reset              |
| Training-time poisoning & back-doors                               | MITRE ATLAS “Poisoning training data” technique ([atlas.mitre.org][4])  | Collect open papers & PoC datasets; add **`attacks/poisoning/`**            |
| Policy-evasion via encoding / zero-width / homoglyph               | HiddenLayer taxonomy ([hiddenlayer.com][5])                             | Auto-generate variants with encoding transforms                             |
| Gradient-based universal triggers (GCG, HotFlip, etc.)             | Original GCG repo ([github.com][6])                                     | Mirror minimal examples; create **`attacks/gcg/`**                          |
| Model extraction & membership inference                            | LLM security survey ([arxiv.org][7])                                    | Summarise attack flow; add scripts using OpenAI log-prob APIs               |
| Supply-chain / plugin compromise                                   | Barracuda blog series ([blog.barracuda.com][8])                         | Document plugin-manifest hijacks; label as **LLM09** (OWASP)                |
| Robot-control prompt bridging                                      | Wired robotics exploit story ([wired.com][9])                           | Add examples in **`attacks/physical/`** corpus                              |
| …and so on – list continues in `/docs/gap-matrix.md` (deliverable) |                                                                         |                                                                             |

*Deliverable ➡️ `docs/gap-matrix.md` – matrix of all attack types vs. repo coverage (✅ / ❌).*

---

## 2 · Proposed lean repo structure (v3)

```
llmattacks/
├── attacks/            # curated, deduped attack corpora
│   ├── prompt/         # direct & indirect prompt-level
│   ├── jailbreaking/
│   ├── poisoning/
│   ├── extraction/
│   ├── optimization/   # GCG, genetic, RL
│   └── physical/
├── datasets/           # parquet/CSV with {text,label,meta}
├── defenses/           # ONLY mitigations we will prototype
│   ├── input_filters/
│   ├── output_filters/
│   └── detection_rules/
├── models/             # detection model code & weights
│   └── small-bert-atk/
├── docs/               # markdown specs, gap-matrix, RFCs
└── scripts/            # helper CLI utilities
```

*Changes vs. competitor offer:*

* no separate “playground”, “education”, “fusion-engine”, etc. – those are out-of-scope;
* each folder has a `README.md` with DONE-criteria and test checklist.

---

## 3 · Mitigation-research work-packages

1. **Threat-model RFC** (`docs/RFC-001-threat-model.md`)
   1.1 Catalogue attacker goals & capabilities using MITRE ATLAS terminology ([atlas.mitre.org][4])
   1.2 Map each to OWASP LLM risks ([owasp.org][1]) ➡️ 3.3, 3.4
2. **Data collection pipeline** (`scripts/build_dataset.py`)
   2.1 Scrape openly published prompt corpora (arXiv, blogs) ([iterasec.com][10])
   2.2 Auto-label with heuristics; human-review 5 % sample
3. **Defense prototyping**
   3.1 **Input normaliser** – unicode-NFC, zero-width strip, homoglyph map (gap 1)
   3.2 **Context window firewall** – sliding-window check for role-swap
   3.3 **Safety-token guard** – tiny keyword model to early-abort (<1 ms)
   3.4 **Risk-score API** – output `risk ∈ [0,1]`; integrate into logging
4. **Benchmark harness** (`scripts/eval.py`)
   4.1 Run each defense against full attacks corpus
   4.2 Export ROC, confusion matrix

*Deliverables ➡️ finished RFCs, defensive scripts + pytest suite.*

---

## 4 · Small “attack-or-not” model – step-by-step

> Target: **≤ 60 M params**, <200 ms @ CPU, F1 ≥ 0.9 on held-out set.

| #   | Step                                                                                        | Responsible    | Output                        |
| --- | ------------------------------------------------------------------------------------------- | -------------- | ----------------------------- |
| 4.1 | Dataset v1 export (`datasets/v1.parquet`) – 100 k rows balanced                             | Agent D        | Parquet + README              |
| 4.2 | Baseline fine-tune on *DistilRoBERTa-base* ([willowtreeapps.com][11])                       | Agent ML       | `models/baseline/`            |
| 4.3 | Hard-negative mining from “edge cases” (legitimate pentest queries)                         | Agent Research | patch to dataset              |
| 4.4 | Knowledge-distill into **TinyBERT-LLMAtk-6L**                                               | Agent ML       | `models/small-bert-atk/`      |
| 4.5 | Eval vs. jailbreak-detection paper test-set ([arxiv.org][3])                                | Agent SecOps   | `reports/eval.md`             |
| 4.6 | Optimise latency: quantise to INT8 using bits-and-bytes                                     | Agent Infra    | `models/int8/`                |
| 4.7 | CI/CD: GitHub Actions workflow triggers on push; runs pytest + eval; uploads model artefact | Agent Infra    | `.github/workflows/model.yml` |

---

## 5 · Timeline & milestones

| Week | Milestone                                       | Blocking       |
| ---- | ----------------------------------------------- | -------------- |
| 1    | Gap-matrix complete, repo folders scaffolded    | –              |
| 2    | Dataset v1 + baseline defense scripts           | gap-matrix     |
| 3    | Baseline model F1 > 0.8, defense ROC logged     | dataset v1     |
| 4    | TinyBERT distillation, INT8 quantisation        | baseline model |
| 5    | Final evaluation + docs; tag **v3.0.0** release | all            |

---

## 6 · Quality gates

* **Coverage** – pytest ≥ 90 %; mypy strict; pre-commit flake8 / black;
* **Perf** – classifier p95 latency < 200 ms on Intel i5;
* **Docs** – every folder gets its own `README.md`; ADRs live in `docs/adr/`.

---

## 7 · Reading list for implementers

1. OWASP LLM Top 10  ([owasp.org][1])
2. Prompt-injection taxonomy  ([hiddenlayer.com][5])
3. MITRE ATLAS knowledge-base  ([atlas.mitre.org][4])
4. Jailbreak detection study  ([arxiv.org][3])
5. Adaptive jailbreak attack paper  ([arxiv.org][12])
6. Comprehensive LLM security survey  ([arxiv.org][7])
7. Practical attack roundup  ([iterasec.com][10])
8. Red-team NER categorisation article  ([willowtreeapps.com][11])
9. Wired prompt-injection feature  ([wired.com][13])
10. Robots-gone-rogue case study  ([wired.com][9])

---

### What next?

*Open issues:*

* assign teams to sections above,
* lock “overkill” competitor file in `/docs/legacy/` for reference only,
* start with week 1 checklist – once gap-matrix is merged we can parallelise.

Good luck – and ping me if priorities shift.

[1]: https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=chatgpt.com "OWASP Top 10 for Large Language Model Applications"
[2]: https://genai.owasp.org/llmrisk/llm01-prompt-injection/?utm_source=chatgpt.com "LLM01:2025 Prompt Injection - OWASP Gen AI Security Project"
[3]: https://arxiv.org/html/2504.02080v1?utm_source=chatgpt.com "Evolving Security in LLMs: A Study of Jailbreak Attacks and ... - arXiv"
[4]: https://atlas.mitre.org/?utm_source=chatgpt.com "MITRE ATLAS™"
[5]: https://hiddenlayer.com/innovation-hub/introducing-a-taxonomy-of-adversarial-prompt-engineering/?utm_source=chatgpt.com "Introducing a Taxonomy of Adversarial Prompt Engineering"
[6]: https://github.com/llm-attacks/llm-attacks "GitHub - llm-attacks/llm-attacks: Universal and Transferable Attacks on Aligned Language Models"
[7]: https://arxiv.org/html/2505.01177v1?utm_source=chatgpt.com "LLM Security: Vulnerabilities, Attacks, Defenses, and ... - arXiv"
[8]: https://blog.barracuda.com/Series/series-llm-attacks-jailbreaks-ai-backdoors-supply-chain-attacks?utm_source=chatgpt.com "Series: LLM Attacks - Jailbreaks, AI backdoors, and supply chain ..."
[9]: https://www.wired.com/story/researchers-llm-ai-robot-violence?utm_source=chatgpt.com "AI-Powered Robots Can Be Tricked Into Acts of Violence"
[10]: https://iterasec.com/blog/practical-attacks-on-llms/?utm_source=chatgpt.com "Practical Attacks on LLMs: Full Guide to LLM Attacks - Iterasec"
[11]: https://www.willowtreeapps.com/craft/llm-attack-evaluation-for-ai-red-teams?utm_source=chatgpt.com "Next-Level AI Red Teaming: Categorizing LLM Attack Methods"
[12]: https://arxiv.org/abs/2404.02151?utm_source=chatgpt.com "Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive ..."
[13]: https://www.wired.com/story/generative-ai-prompt-injection-hacking?utm_source=chatgpt.com "Generative AI's Biggest Security Flaw Is Not Easy to Fix"
