Below is a **production-ready work-plan** broken down into **atomic, assignable subtasks**.
Everything is filed beneath a new root folder **`secure_llmattacks_v3/`** so the legacy catalog stays untouched.
For each atomic task you will find:

* **ID** – hierarchical index (`2.1.4` etc.)
* **What** – single, clear action (code line, CLI command, or document paragraph)
* **Path / File** – exact pathname to edit or create
* **Output** – artefact(s) that prove the step is done
* **Depends on** – IDs that must finish first (use this for parallelisation)

---

## High-level architecture choices (why we do it this way)

| Decision                                                       | Rationale                                                 | Source                                                         |
| -------------------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------- |
| **Mirror repo under `secure_llmattacks_v3/`**                  | keeps Git history yet isolates new work                   | repo tree listing shows current root clutter ([github.com][1]) |
| **MkDocs Material** continues for docs                         | already configured in `mkdocs.yml` ([github.com][1])      |                                                                |
| **Python 3.11 + Poetry** for deterministic builds              | easier lockfiles & venv isolation                         |                                                                |
| **Parquet datasets** with PyArrow                              | fast I/O for 100 k-row attack corpus                      |                                                                |
| **Pydantic-v2 models** in `datasets/schema.py`                 | runtime validation, type hints                            |                                                                |
| **Hugging Face HF Hub** release for trained model              | free bandwidth, version tags                              |                                                                |
| **OWASP LLM Top-10 + MITRE ATLAS** as attack taxonomy backbone | community standard ([owasp.org][2], [atlas.mitre.org][3]) |                                                                |
| **TinyBERT-6L INT8** as final detector                         | fits <200 ms CPU, open weights ([arxiv.org][4])           |                                                                |
| **bits-and-bytes** post-training quantisation                  | saves RAM; proven in ASF defense ([arxiv.org][5])         |                                                                |

---

## 0 · Bootstrap the skeleton (2 h)

| ID  | What                                                                                                                                  | Path / File                      | Output                         | Depends on |
| --- | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ------------------------------ | ---------- |
| 0.1 | Create work branch                                                                                                                    | –                                | `secure-v3-plan` branch pushed | –          |
| 0.2 | `mkdir secure_llmattacks_v3 && cp -r * secure_llmattacks_v3/original_v2_snapshot/`                                                    | repo root                        | full snapshot committed        | 0.1        |
| 0.3 | `cd secure_llmattacks_v3 && poetry init --python=^3.11`                                                                               | `pyproject.toml`                 | dep skeleton                   | 0.2        |
| 0.4 | Add Poetry deps: `poetry add pydantic pyarrow pandas datasets sentencepiece transformers bitsandbytes scikit-learn pytest black mypy` | `pyproject.toml`                 | locked deps                    | 0.3        |
| 0.5 | Top-level dirs: `mkdir {attacks,datasets,defenses,models,scripts,docs,.github}`                                                       | fs                               | folders exist                  | 0.2        |
| 0.6 | Root README stub incl. project map                                                                                                    | `secure_llmattacks_v3/README.md` | README paragraph               | 0.5        |

---

## 1 · Exhaustive gap-matrix (1 day)

| ID   | What                                                                                                                      | Path / File                  | Output          | Depends on |
| ---- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | --------------- | ---------- |
| 1.1  | Draft header & table columns (`attack_type, risk_id, source_link, present, folder`)                                       | `docs/gap_matrix.md`         | table skeleton  | 0.6        |
| 1.2  | Fill OWASP risks LLM01-LLM10                                                                                              | same                         | 10 rows         | 1.1        |
| 1.3  | Add MITRE ATLAS `ATC-T0018` Data-Poisoning row                                                                            | same                         | row added       | 1.1        |
| 1.4  | Insert HiddenLayer prompt-taxonomy rows (indirect PI, TokenBreak, homoglyph) ([hiddenlayer.com][6], [hiddenlayer.com][7]) | same                         | 3 rows          | 1.1        |
| 1.5  | Record Many-Shot Jailbreaking gap ([www-cdn.anthropic.com][8])                                                            | same                         | row             | 1.1        |
| 1.6  | Record GCG / AmpleGCG universal suffix gaps ([arxiv.org][9])                                                              | same                         | 2 rows          | 1.1        |
| 1.7  | Record DoS / unbounded-token gaps ([arxiv.org][10], [hiddenlayer.com][11])                                                | same                         | row             | 1.1        |
| 1.8  | Record model-extraction & membership-inference gaps ([arxiv.org][12])                                                     | same                         | row             | 1.1        |
| 1.9  | Script validator `scripts/verify_coverage.py` that fails CI if any `present: ❌`                                           | `scripts/verify_coverage.py` | CI-ready script | 1.2-1.8    |
| 1.10 | Add rule to CI (`coverage.yml`) to run validator                                                                          | `.github/workflows/ci.yml`   | job passes      | 1.9        |

---

## 2 · Curate attack corpora (3 days)

### 2.0 Folder map

```
secure_llmattacks_v3/attacks/
  prompt/{direct,indirect}/
  jailbreaking/{many_shot,role_play}/
  poisoning/{pretrain,finetune}/
  suffixes/{gcg,amplegcg,hotflip}/
  extraction/{model_leak,membership_inf}/
  dos/{autodos,token_flood}/
  physical/robotics/
  supply_chain/plugin/
```

| ID    | What                                                                                     | Path / File                                      | Output          | Depends    |
| ----- | ---------------------------------------------------------------------------------------- | ------------------------------------------------ | --------------- | ---------- |
| 2.1.1 | Copy existing `docs/prompt-injection.md` into `attacks/prompt/direct/001_classic_dan.md` | fs                                               | md file         | 0.5        |
| 2.1.2 | Crawl 50 HTML-embedded PI examples, save each as numbered md                             | `attacks/prompt/indirect/`                       | 50 md files     | 1.4        |
| 2.2.1 | Convert Anthropic MSJ paper examples to md                                               | `attacks/jailbreaking/many_shot/001_msj_base.md` | file            | 1.5        |
| 2.2.2 | Script `scripts/generate_msj_variants.py` (auto shot-count)                              | script file                                      | 100 txt prompts | 2.2.1      |
| 2.3.1 | Download AmpleGCG suffix list (200 lines) ([arxiv.org][9])                               | `attacks/suffixes/amplegcg/suffixes.txt`         | txt file        | 1.6        |
| 2.3.2 | Port GCG default suffix ([arxiv.org][4])                                                 | `attacks/suffixes/gcg/default_suffix.txt`        | txt             | 1.6        |
| 2.4.1 | Create poisoning notebook with synthetic dataset gen                                     | `attacks/poisoning/pretrain/gen_dataset.ipynb`   | ipynb           | 1.3        |
| 2.5.1 | Collect HiddenLayer TokenBreak prompts                                                   | `attacks/prompt/indirect/tokenbreak.txt`         | txt             | 1.4        |
| 2.6.1 | Gather model-leak PoC from Llama2 leak paper                                             | `attacks/extraction/model_leak/leak_attack.py`   | script          | 1.8        |
| 2.7.1 | Build symlinks ≥10 MB to `datasets/raw/` to avoid git-LFS                                | fs                                               | symlinks        | 2.\* tasks |

---

## 3 · Dataset build pipeline (1 day)

| ID    | What                                                                | Path / File                    | Output                                                                         | Depends |
| ----- | ------------------------------------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------ | ------- |
| 3.1.1 | Define Pydantic schema                                              | `datasets/schema.py`           | `class AttackSample(BaseModel)` with `uuid text label attack_type source_path` | 0.4     |
| 3.1.2 | Implement `scripts/build_dataset.py` reading `attacks/**` → Parquet | script                         | `datasets/v1/attacks.parquet`                                                  | 2.\*    |
| 3.1.3 | Generate 5 % sample CSV (`datasets/v1/sample_for_review.csv`)       | script                         | csv                                                                            | 3.1.2   |
| 3.1.4 | Unit-test dataset row count ≥ rows in attacks dir                   | `tests/test_dataset_counts.py` | pytest file                                                                    | 3.1.2   |
| 3.1.5 | Update CI to run tests                                              | `.github/workflows/ci.yml`     | green build                                                                    | 3.1.4   |

---

## 4 · Defensive filters (2 days)

| ID    | What                                                                    | Path / File                            | Output               | Depends     |
| ----- | ----------------------------------------------------------------------- | -------------------------------------- | -------------------- | ----------- |
| 4.1.1 | `defenses/input_filters/zero_width.py` removes U+200B etc.              | py                                     | function & unit test | 1.4         |
| 4.1.2 | `defenses/input_filters/homoglyph.py` normalises latin/greek homoglyphs | py                                     | function             | 1.4         |
| 4.1.3 | `defenses/input_filters/length_guard.py` truncates >8k tokens           | py                                     | func                 | 1.7         |
| 4.2.1 | Stateful `ContextFirewall` class detecting role swaps                   | `defenses/context/window_firewall.py`  | py                   | 1.5         |
| 4.3.1 | Output‐side JailGuard risk-score implementation ([arxiv.org][5])        | `defenses/output_filters/jailguard.py` | py                   | 1.6         |
| 4.4.1 | Parametrize above filters for CLI usage                                 | `scripts/run_filters.py`               | script               | 4.1.*-4.3.* |
| 4.5.1 | `tests/test_filters.py` achieving ≥90 % coverage                        | pytest                                 | test files           | 4.\*        |

---

## 5 · Baseline detector model (2 days)

| ID    | What                                           | Path / File                   | Output                                      | Depends |
| ----- | ---------------------------------------------- | ----------------------------- | ------------------------------------------- | ------- |
| 5.1.1 | Config YAML referencing DistilRoBERTa          | `models/baseline/config.yaml` | config                                      | 0.4     |
| 5.1.2 | Training script loads Parquet, splits 80/20    | `models/baseline/train.py`    | checkpoint dir                              | 3.1.2   |
| 5.1.3 | Eval script prints F1, ROC                     | `models/baseline/eval.py`     | `models/baseline/metrics.json` with F1≥0.80 | 5.1.2   |
| 5.1.4 | Upload checkpoint to HF Hub via token          | HF artefact                   | public model                                | 5.1.3   |
| 5.1.5 | Add GitHub Action to retrain on dataset change | `.github/workflows/model.yml` | CI workflow                                 | 5.1.2   |

---

## 6 · Distilled TinyBERT-INT8 (3 days)

| ID    | What                                         | Path / File                    | Output                     | Depends |
| ----- | -------------------------------------------- | ------------------------------ | -------------------------- | ------- |
| 6.1.1 | Distillation script uses baseline as teacher | `models/tiny/train_distill.py` | `models/tiny/checkpoints/` | 5.1.3   |
| 6.1.2 | Quantise to INT8 with bits-and-bytes         | `models/tiny/quantize.py`      | `models/tiny/int8/`        | 6.1.1   |
| 6.1.3 | Runtime benchmark script ensures <200 ms p95 | `models/tiny/bench.py`         | report                     | 6.1.2   |

---

## 7 · Evaluation harness (1 day)

| ID    | What                                                    | Path / File | Output                            | Depends   |
| ----- | ------------------------------------------------------- | ----------- | --------------------------------- | --------- |
| 7.1.1 | `scripts/eval_defenses.py` matrix-runs (model × filter) | script      | `reports/eval/YYYY-MM-DD/roc.png` | 4.\* 5.\* |
| 7.1.2 | Save confusion matrix CSV                               | same dir    | csv                               | 7.1.1     |
| 7.1.3 | Fail CI if F1 drop >2 % after new commit                | CI rule     | updated workflow                  | 7.1.1     |

---

## 8 · Documentation & ADRs (continuous)

| ID    | What                                                 | Path / File                         | Output           | Depends |
| ----- | ---------------------------------------------------- | ----------------------------------- | ---------------- | ------- |
| 8.1.1 | Threat-model doc mapping OWASP → ATLAS → mitigations | `docs/threat_model.md`              | md file          | 1.\*    |
| 8.1.2 | ADR-0001 explaining folder redesign                  | `docs/adr/ADR-0001-folders.md`      | md               | 0.6     |
| 8.1.3 | ADR-0002 why TinyBERT-6L                             | `docs/adr/ADR-0002-model_choice.md` | md               | 6.\*    |
| 8.1.4 | MkDocs nav update                                    | `mkdocs.yml`                        | docs site builds | 8.1.\*  |

---

## 9 · Release & hand-off (½ day)

| ID    | What                   | Path / File                     | Output     | Depends   |
| ----- | ---------------------- | ------------------------------- | ---------- | --------- |
| 9.1.1 | Tag v3.0.0             | git tag                         | release    | 7.\* 8.\* |
| 9.1.2 | Archive competitor doc | `docs/legacy/llm-attacks-v2.md` | file moved | 0.2       |

---

## 10 · Enforcement gates (always)

* **CI** runs black, mypy `--strict`, pytest, dataset validator, model benchmark.
* **Coverage** ≥ 90 %, enforced in workflow.
* **Security audit** on dependencies via `poetry export --format=requirements.txt | pip-audit`.
* **SBOM** regenerated (`scripts/gen_sbom.py`) -> `sbom.json`.

---

## External references used while designing the plan

* OWASP Top-10 for LLM Apps ([owasp.org][2])
* OWASP 2025 Gen-AI update ([genai.owasp.org][13])
* MITRE ATLAS portal ([atlas.mitre.org][3])
* HiddenLayer prompt-taxonomy & TokenBreak ([hiddenlayer.com][6], [hiddenlayer.com][7])
* Anthropic Many-Shot jailbreaking paper ([www-cdn.anthropic.com][8])
* Universal GCG adversarial suffix study (arXiv 2307.15043) ([arxiv.org][4])
* AmpleGCG universal attack ([arxiv.org][9])
* JailGuard adversarial-suffix filtering defense ([arxiv.org][5])
* Membership-inference survey 2025 ([arxiv.org][12])
* Repo tree showing existing files & MkDocs config ([github.com][1])

---

### How to use this grid

1. **Create issues**: each atomic ID → one GitHub issue; label with folder (`attacks`, `defenses` …).
2. **Assign junior devs** according to dependencies; anything without a blocking column can start in parallel.
3. **Track progress** via CI; commits that violate a gate will block merge.

You now have a line-item-level blueprint ready for immediate execution.

[1]: https://github.com/nnnsss999/llmattacks "GitHub - nnnsss999/llmattacks"
[2]: https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=chatgpt.com "OWASP Top 10 for Large Language Model Applications"
[3]: https://atlas.mitre.org/?utm_source=chatgpt.com "MITRE ATLAS™"
[4]: https://arxiv.org/pdf/2307.15043?utm_source=chatgpt.com "[PDF] Universal and Transferable Adversarial Attacks on Aligned ... - arXiv"
[5]: https://arxiv.org/html/2505.09602v1?utm_source=chatgpt.com "Adversarial Suffix Filtering: a Defense Pipeline for LLMs - arXiv"
[6]: https://hiddenlayer.com/innovation-hub/introducing-a-taxonomy-of-adversarial-prompt-engineering/?utm_source=chatgpt.com "Introducing a Taxonomy of Adversarial Prompt Engineering"
[7]: https://hiddenlayer.com/innovation-hub/new-tokenbreak-attack-bypasses-ai-moderation-with-single-character-text-changes/?utm_source=chatgpt.com "New TokenBreak Attack Bypasses AI Moderation with Single ..."
[8]: https://www-cdn.anthropic.com/af5633c94ed2beb282f6a53c595eb437e8e7b630/Many_Shot_Jailbreaking__2024_04_02_0936.pdf?utm_source=chatgpt.com "[PDF] Many-shot Jailbreaking | Anthropic"
[9]: https://arxiv.org/abs/2404.07921?utm_source=chatgpt.com "[2404.07921] AmpleGCG: Learning a Universal and Transferable ..."
[10]: https://arxiv.org/html/2505.15738v1?utm_source=chatgpt.com "The Case for Informed Adversaries When Evaluating LLM Defenses"
[11]: https://hiddenlayer.com/innovation-hub/novel-universal-bypass-for-all-major-llms/?utm_source=chatgpt.com "Novel Universal Bypass for All Major LLMs - HiddenLayer"
[12]: https://arxiv.org/abs/2503.19338?utm_source=chatgpt.com "Membership Inference Attacks on Large-Scale Models: A Survey"
[13]: https://genai.owasp.org/llm-top-10/?utm_source=chatgpt.com "2025 Top 10 Risk & Mitigations for LLMs and Gen AI Apps"
