Below is a **deep-granular task hierarchy** that rebuilds the repo under a brand-new root folder **`secure_llmattacks_v3/`**.
Every bullet is phrased as a *Jira-ready* task.
*All* paths are explicit, deliverables are concrete files, and dependencies are marked with `➡️`.
Citations anchor every research gap to high-quality sources.

---

## Summary ★

We will ❶ clone the current repo, ❷ snapshot it into `secure_llmattacks_v3/`, ❸ fill every missing attack category, ❹ add tightly-scoped mitigation prototypes, and ❺ train a ≤60 M-param “attack-or-not” detector.
The structure below lets multiple junior engineers work in parallel while preserving commit history and traceability.

---

## 0 · Bootstrap & Folder Skeleton (Day 0)

| Step | Command / Action                                                                           | Resulting Files   |
| ---- | ------------------------------------------------------------------------------------------ | ----------------- |
| 0.1  | `git checkout -b secure-v3-scaffold`                                                       | branch created    |
| 0.2  | `mkdir secure_llmattacks_v3 && cp -r * secure_llmattacks_v3/original_v2_snapshot/`         | full snapshot     |
| 0.3  | `cd secure_llmattacks_v3 && mkdir {attacks,datasets,defenses,models,scripts,docs,.github}` | top-level dirs    |
| 0.4  | `touch README.md && echo "# secure_llmattacks_v3" > README.md`                             | repo root read-me |

No coding yet—just scaffolding the playground.

---

## 1 · Research Gap Matrix (Week 1)

> *Owner → Agent Research*
> *Folder → `secure_llmattacks_v3/docs/`*

1.1 **Create** `docs/gap_matrix.md` with table columns: `Attack-Type`, `Source`, `Present?`, `Folder`, `Example-file`.
1.2 Populate rows using OWASP LLM Top-10 LLM01-LLM10 ➜ LLM05, LLM04 etc. ([owasp.org][1], [genai.owasp.org][2], [genai.owasp.org][3])
1.3 Map poisoning & back-door gaps to MITRE ATLAS tactics `ATC-T0018` “Data Poisoning” ([atlas.mitre.org][4])
1.4 Add multi-turn context-switch jailbreak gap from Anthropic “many-shot” research ([theguardian.com][5])
1.5 Note universal bypass via HiddenLayer ([hiddenlayer.com][6])
1.6 Include gradient-based universal triggers (GCG) ([arxiv.org][7]) and HotFlip variants ([cybernetist.com][8])
1.7 List model-extraction & membership-inference gap ([arxiv.org][9], [github.com][10])
1.8 Add supply-chain/plugin compromise gap (OWASP LLM05 + Cobalt blog) ([genai.owasp.org][2], [cobalt.io][11])
1.9 Capture LLM-DoS (AutoDoS, unbounded consumption) ([arxiv.org][12], [promptfoo.dev][13])
1.10 Cover physical/robot bridging risk (Wired robotics exploit) ([wired.com][14])

*Deliverable*: `docs/gap_matrix.md` ready ➡️ feeds **Step 2.4**.

---

## 2 · Curate Complete Attack Corpora (Week 1–2)

> *Owner → Agent Content*

### Folder Tree

```
secure_llmattacks_v3/attacks/
├── prompt/
│   ├── direct_prompt_injection.md
│   └── indirect_cross_context.md
├── jailbreaking/
│   ├── many_shot_chain.md
│   └── role_play_reset.md
├── poisoning/
│   ├── pretrain_poison.ipynb
│   └── finetune_backdoor.ipynb
├── extraction/
│   ├── model_leak_attack.py
│   └── membership_inference.py
├── dos/
│   ├── autodOS_black_box.md
│   └── unbounded_consumption.md
├── supply_chain/
│   └── malicious_plugin_manifest.json
├── optimization_triggers/
│   ├── gcg_suffix.txt
│   └── hotflip_example.txt
└── physical/
    └── robo_pair_prompt.md
```

**Granular tasks**

2.1 `prompt/direct_prompt_injection.md` – include 10 classic DAN-style strings.
2.2 `prompt/indirect_cross_context.md` – scrape examples embedded in HTML/Markdown.
2.3 `jailbreaking/many_shot_chain.md` – craft ≥200-example chain referencing Anthropic paper details.
2.4 **Gap-coverage validation script** `scripts/verify_coverage.py` → reads `docs/gap_matrix.md`, asserts every `Present?` ✅ has file.
2.5 Upload large artefacts (datasets ≥10 MB) to `datasets/raw/` and symlink inside `attacks/`.

---

## 3 · Dataset Pipeline (Week 2)

> *Owner → Agent DataEng*
> *Folder → `secure_llmattacks_v3/datasets/`*

3.1 `scripts/build_dataset.py`
  • scans `attacks/**`, normalises unicode, strips zero-width chars.
  • outputs `datasets/v1/attacks.parquet` with schema `{uuid,text,label,attack_type,source_path}`.
3.2 `datasets/README.md` – document schema + how to regenerate.
3.3 Sample 5 % for manual review into `datasets/v1/hand_labeled.csv`.

---

## 4 · Mitigation Prototypes (Week 2–3)

> *Owner → Agent Backend*
> *Folder → `secure_llmattacks_v3/defenses/`*

### 4.1 Input Filters

```
defenses/input_filters/
├── zero_width_filter.py
├── homoglyph_mapper.py
└── prompt_length_guard.py
```

*Each file exports `def filter(text) -> str|None`.*

### 4.2 Context Window Firewall

```
defenses/context_firewall/context_firewall.py
```

Implements sliding-window role-swap detection (stateful).

### 4.3 Output Risk-Scorer

```
defenses/output_filters/jailguard_scoring.py
```

Implements JailGuard‐style robustness metric ([arxiv.org][15]).

### 4.4 Unit Tests

`pytest defenses/tests/test_filters.py` (≥90 % coverage).

---

## 5 · Baseline “Attack-or-Not” Model (Week 3)

> *Owner → Agent ML*

### Folder Layout

```
secure_llmattacks_v3/models/baseline/
├── train.py
├── eval.py
├── config.yaml
└── README.md
```

5.1 Fine-tune `distilroberta-base` on `datasets/v1/attacks.parquet`.
5.2 Save checkpoints to `models/baseline/checkpoints/`.
5.3 Log F1 > 0.80 to `models/baseline/metrics.json`.

---

## 6 · Distilled Tiny Model (Week 4)

> *Owner → Agent ML*

### Folder Layout

```
secure_llmattacks_v3/models/tinybert_atk/
├── distill.py
├── int8_quantize.py
├── checkpoints/
└── README.md
```

6.1 Knowledge-distill from baseline to TinyBERT-6L.
6.2 `int8_quantize.py` uses bits-and-bytes to compress; latency goal < 200 ms CPU.

---

## 7 · Evaluation Harness (Week 4)

> *Owner → Agent SecOps*

7.1 `scripts/eval_defenses.py` – loops over every filter then runs model; outputs ROC curves.
7.2 Store artefacts under `reports/eval/2025-MM-DD/`.

---

## 8 · CI/CD & Quality Gates (continuous)

> *Owner → Agent Infra*

8.1 `.github/workflows/ci.yml` – lint + pytest + coverage.
8.2 `.github/workflows/model.yml` – triggers on changes in `models/**`, pushes model artefacts to GitHub Releases.
8.3 Pre-commit config with black & flake8 (line length = 120).
8.4 `mypy --strict` in CI; fix any hint violations.

---

## 9 · Documentation Set

> *Owner → Agent Docs*
> *Folder → `secure_llmattacks_v3/docs/`*

9.1 `README.md` – high-level overview.
9.2 `threat_model.md` – maps OWASP risks to MITRE ATLAS tactics with concrete examples.
9.3 `adr/ADR-0001-folder_structure.md` – rationale for new layout.
9.4 Future RFCs live in `docs/rfc/`.

---

## 10 · Release & Handoff (Week 5)

10.1 Tag `v3.0.0` on branch merge.
10.2 Publish model card in `models/tinybert_atk/README.md`.
10.3 Archive competitor proposal to `secure_llmattacks_v3/docs/legacy/llm-attacks-v2.md`.

---

## Reading List (attach to onboarding)

1. OWASP LLM Top-10 ([owasp.org][1])
2. GenAI OWASP detailed attacks ([genai.owasp.org][16], [genai.owasp.org][17])
3. MITRE ATLAS poisoning technique ([atlas.mitre.org][4])
4. HiddenLayer universal bypass ([hiddenlayer.com][6])
5. JailGuard detection framework ([arxiv.org][15])
6. Universal adversarial triggers (GCG) ([arxiv.org][7])
7. Membership-inference survey 2025 ([arxiv.org][9])
8. Anthropic many-shot jailbreak study ([theguardian.com][5])
9. Wired robotics manipulation demo ([wired.com][14])
10. AutoDoS black-box paper ([arxiv.org][12])
11. Unbounded consumption blog ([promptfoo.dev][13])
12. LLM supply-chain vulnerability study ([arxiv.org][18])
13. Cobalt plugin attack blog ([cobalt.io][11])
14. Lilian Weng’s adversarial attack taxonomy ([lilianweng.github.io][19], [lilianweng.github.io][19])
15. HotFlip adaptation note ([cybernetist.com][8])

---

### Next Action

*Merge this scaffold PR, assign step owners, and start with Task 1.1.*

[1]: https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=chatgpt.com "OWASP Top 10 for Large Language Model Applications"
[2]: https://genai.owasp.org/llmrisk2023-24/llm05-supply-chain-vulnerabilities/?utm_source=chatgpt.com "LLM05: Supply Chain Vulnerabilities - GenAI OWASP"
[3]: https://genai.owasp.org/llmrisk2023-24/llm04-model-denial-of-service/?utm_source=chatgpt.com "LLM04: Model Denial of Service - OWASP Generative AI"
[4]: https://atlas.mitre.org/?utm_source=chatgpt.com "MITRE ATLAS™"
[5]: https://www.theguardian.com/technology/2024/apr/03/many-shot-jailbreaking-ai-artificial-intelligence-safety-features-bypass?utm_source=chatgpt.com "'Many-shot jailbreak': lab reveals how AI safety features can be easily bypassed"
[6]: https://hiddenlayer.com/innovation-hub/novel-universal-bypass-for-all-major-llms/?utm_source=chatgpt.com "Novel Universal Bypass for All Major LLMs - HiddenLayer"
[7]: https://arxiv.org/pdf/2307.15043?utm_source=chatgpt.com "[PDF] Universal and Transferable Adversarial Attacks on Aligned ... - arXiv"
[8]: https://cybernetist.com/2024/09/23/some-notes-on-adversarial-attacks-on-llms/?utm_source=chatgpt.com "Some Notes on Adversarial Attacks on LLMs - Cybernetist"
[9]: https://arxiv.org/html/2503.19338v1?utm_source=chatgpt.com "Membership Inference Attacks on Large-Scale Models: A Survey"
[10]: https://github.com/ThuCCSLab/Awesome-LM-SSP/blob/main/collection/paper/privacy/membership_inference_attacks.md?utm_source=chatgpt.com "C4. Membership Inference Attacks - GitHub"
[11]: https://www.cobalt.io/blog/llm-supply-chain-attack-prevention-strategies?utm_source=chatgpt.com "LLM Supply Chain Attack: Prevention Strategies - Cobalt"
[12]: https://arxiv.org/html/2412.13879v1?utm_source=chatgpt.com "Consuming Resrouce via Auto-generation for LLM-DoS Attack ..."
[13]: https://www.promptfoo.dev/blog/unbounded-consumption/?utm_source=chatgpt.com "How Unbounded Consumption is Reshaping LLM Security | promptfoo"
[14]: https://www.wired.com/story/researchers-llm-ai-robot-violence?utm_source=chatgpt.com "AI-Powered Robots Can Be Tricked Into Acts of Violence"
[15]: https://arxiv.org/html/2312.10766v3?utm_source=chatgpt.com "A Universal Detection Framework for LLM Prompt-based Attacks"
[16]: https://genai.owasp.org/llmrisk/llm01-prompt-injection/?utm_source=chatgpt.com "LLM01:2025 Prompt Injection - OWASP Gen AI Security Project"
[17]: https://genai.owasp.org/llmrisk/llm04-model-denial-of-service/?utm_source=chatgpt.com "LLM04:2025 Data and Model Poisoning - GenAI OWASP"
[18]: https://arxiv.org/html/2502.12497v1?utm_source=chatgpt.com "Understanding Vulnerabilities in the Large Language Model Supply ..."
[19]: https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/?utm_source=chatgpt.com "Adversarial Attacks on LLMs - Lil'Log"
