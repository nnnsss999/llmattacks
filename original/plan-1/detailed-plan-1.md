Below is an **implementation-grade task grid** for **Steps 0 – 3** only.
Each atomic card starts with **“Act as …”** so you can drop it straight into Jira.
Dependencies are spelled out by ID; deliverables are concrete files or CI artefacts.

---

## Quick-look summary

These four steps establish the new `secure_llmattacks_v3/` workspace, lock reproducible Python tooling with Poetry 3.11, create an evidence-based **Gap Matrix** sourced from OWASP LLM Top-10 and MITRE ATLAS, pull every missing attack corpus into deterministic folders, and generate a validated Parquet dataset using a Pydantic-v2 schema.  Together they give junior teams a clean codebase, a research to-do list, and a ready-to-train dataset.  References to OWASP, ATLAS, Poetry, Pydantic and PyArrow best-practices back every design choice. ([owasp.org][1], [genai.owasp.org][2], [atlas.mitre.org][3], [pointguardai.com][4], [python-poetry.org][5], [python-poetry.org][6], [docs.pydantic.dev][7], [arrow.apache.org][8], [hiddenlayer.com][9], [anthropic.com][10])

---

## STEP 0 · Bootstrap & Folder Skeleton

| ID       | Jira Card (single-actor wording)                                                                                                                                                                                                         | Deliverable(s)                     | Depends |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ------- |
| **0.1**  | **Act as DevOps** – create feature branch `secure-v3-scaffold` from `main` and push to origin.                                                                                                                                           | Branch visible on GitHub.          | —       |
| **0.2**  | **Act as DevOps** – `mkdir secure_llmattacks_v3 && cp -r * secure_llmattacks_v3/original_v2_snapshot/` to snapshot legacy code without history rewrite.                                                                                  | Populated `original_v2_snapshot/`. | 0.1     |
| **0.3**  | **Act as DevOps** – inside new root run `poetry init --python=^3.11` ; accept defaults, commit `pyproject.toml`. Poetry is preferred for deterministic dependency graphs ([python-poetry.org][5])                                        | Versioned `pyproject.toml`.        | 0.2     |
| **0.4**  | **Act as DevOps** – add runtime deps `pydantic pyarrow pandas datasets sentencepiece transformers bitsandbytes scikit-learn` and dev-deps `pytest black mypy pre-commit` via `poetry add` / `add --group dev`.                           | Locked `poetry.lock`.              | 0.3     |
| **0.5**  | **Act as DevOps** – create canonical folders `attacks datasets defenses models scripts docs .github`.                                                                                                                                    | Directory tree exists.             | 0.2     |
| **0.6**  | **Act as Technical Writer** – draft `secure_llmattacks_v3/README.md` with project intent, folder map and quick-start (`poetry install` → `pytest`).                                                                                      | Root README.                       | 0.5     |
| **0.7**  | **Act as DevOps** – add `.gitignore` (Python, VS Code, Poetry cache) and `.editorconfig`.                                                                                                                                                | Two config files.                  | 0.5     |
| **0.8**  | **Act as DevOps** – set up `pre-commit` hooks (`black`, `flake8`, `mypy --strict`).                                                                                                                                                      | `.pre-commit-config.yaml`.         | 0.4     |
| **0.9**  | **Act as DevOps** – bootstrap GitHub Action `.github/workflows/ci.yml` that: checks out code, `poetry install`, runs `black --check`, `pytest -q`, `mypy --strict`, and posts coverage with `Pytest-Coverage-Comment` ([github.com][11]) | Passing workflow badge.            | 0.4     |
| **0.10** | **Act as DevOps** – tag CI-passing commit `v3.0.0-alpha` to prove pipeline integrity.                                                                                                                                                    | Git tag visible.                   | 0.9     |

---

## STEP 1 · Research Gap Matrix

| ID      | Jira Card                                                                                                                                 | Deliverable(s)         | Depends |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------- |
| **1.1** | **Act as Researcher** – create `docs/gap_matrix.md` table with cols `attack_type,risk_id,source,covered,folder`.                          | Empty table committed. | 0.6     |
| **1.2** | **Act as Researcher** – populate ten rows from **OWASP LLM Top-10** (LLM01-LLM10) marking existing coverage as ❌. ([owasp.org][1])        | 10 filled rows.        | 1.1     |
| **1.3** | **Act as Researcher** – add **MITRE ATLAS** “Data Poisoning” (ATC-T0018) row with ❌. ([atlas.mitre.org][3], [pointguardai.com][4])        | Row added.             | 1.1     |
| **1.4** | **Act as Researcher** – insert three HiddenLayer TokenBreak-family gaps (Indirect PI, TokenBreak, Homoglyph) as ❌. ([hiddenlayer.com][9]) | 3 rows.                | 1.1     |
| **1.5** | **Act as Researcher** – record **Many-Shot Jailbreaking** gap. ([anthropic.com][10], [theguardian.com][12])                               | Row added.             | 1.1     |
| **1.6** | **Act as Researcher** – record **Universal Suffix** gaps (GCG, AmpleGCG) as ❌.                                                            |                        |         |

[1]: https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=chatgpt.com "OWASP Top 10 for Large Language Model Applications"
[2]: https://genai.owasp.org/llm-top-10/?utm_source=chatgpt.com "2025 Top 10 Risk & Mitigations for LLMs and Gen AI Apps"
[3]: https://atlas.mitre.org/?utm_source=chatgpt.com "MITRE ATLAS™"
[4]: https://www.pointguardai.com/blog/understanding-the-mitre-atlas-matrix-for-ai-threats?utm_source=chatgpt.com "Understanding the MITRE ATLAS Matrix for AI Threats - AppSOC"
[5]: https://python-poetry.org/docs/pyproject/?utm_source=chatgpt.com "The pyproject.toml file | Documentation | Poetry"
[6]: https://python-poetry.org/docs/basic-usage/?utm_source=chatgpt.com "Basic usage | Documentation | Poetry - Python dependency ..."
[7]: https://docs.pydantic.dev/latest/concepts/models/?utm_source=chatgpt.com "Models - Pydantic"
[8]: https://arrow.apache.org/docs/python/parquet.html?utm_source=chatgpt.com "Reading and Writing the Apache Parquet Format"
[9]: https://hiddenlayer.com/innovation-hub/the-tokenbreak-attack/?utm_source=chatgpt.com "The TokenBreak Attack - HiddenLayer"
[10]: https://www.anthropic.com/research/many-shot-jailbreaking?utm_source=chatgpt.com "Many-shot jailbreaking - Anthropic"
[11]: https://github.com/marketplace/actions/pytest-coverage-comment?utm_source=chatgpt.com "Pytest Coverage Comment · Actions · GitHub Marketplace"
[12]: https://www.theguardian.com/technology/2024/apr/03/many-shot-jailbreaking-ai-artificial-intelligence-safety-features-bypass?utm_source=chatgpt.com "'Many-shot jailbreak': lab reveals how AI safety features can be easily bypassed"


Below is a **deep-dive, implementation-grade task grid** for **Steps 2 – 5**.
Copy each row into Jira as its own card: every card begins with **“Act as …”**, states precise context, lists *atomic* work, outputs, and blocking IDs (use these for the “Blocks / Is blocked by” fields).

> **TL;DR** Step 2 seeds a *complete* attack corpus, Step 3 turns it into a validated Parquet dataset, Step 4 ships production-quality defensive filters, and Step 5 trains & CI-deploys a baseline DistilRoBERTa detector.  All hard choices (folder layout, Parquet + PyArrow, Pydantic-v2, bits-and-bytes INT-8, HF Hub) are justified by best-practice sources from OWASP LLM Top-10, MITRE ATLAS, Arrow docs, and state-of-the-art jailbreak research. ([arxiv.org][1], [owasp.org][2], [atlas.mitre.org][3], [hiddenlayer.com][4], [anthropic.com][5], [arrow.apache.org][6], [docs.pydantic.dev][7], [huggingface.co][8], [huggingface.co][9], [arxiv.org][10], [pointguardai.com][11])

---

## STEP 2 · Curate **attack corpora** (`secure_llmattacks_v3/attacks/…`)

| ID         | Jira Card (one per cell)                                                                                                                                                                                                    | Output artefact(s)            | Depends on          |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------- |
| **2.1.1**  | **Act as Researcher** – extract ten classic “DAN” direct-prompt-injection strings; save as `attacks/prompt/direct/001_dan.md`; add YAML front-matter (`attack_type: direct_pi`).                                            | `001_dan.md` committed.       | 1.2                 |
| **2.1.2**  | **Act as Researcher** – scrape 50 HTML & Markdown pages where user-supplied text contaminates an embedded LLM prompt (Indirect PI LLM01). Cite each URL in file header; save one per file under `attacks/prompt/indirect/`. | 50 markdown files.            | 1.4                 |
| **2.2.1**  | **Act as Researcher** – copy Anthropic’s *many-shot jailbreak* transcript ([anthropic.com][5]) into `attacks/jailbreaking/many_shot/001_base.md`.                                                                           | `001_base.md`.                | 1.5                 |
| **2.2.2**  | **Act as Python Dev** – write `scripts/generate_msj_variants.py` to programmatically duplicate the base prompt with shot-counts {32, 64, 128}; output \*.txt under same folder.                                             | 3 variant txt files + script. | 2.2.1               |
| **2.3.1**  | **Act as Researcher** – download GCG universal adversarial suffix list (arXiv 2307.15043) ([arxiv.org][1]) and store as `attacks/suffixes/gcg/suffixes.txt` (one per line).                                                 | `suffixes.txt`.               | 1.6                 |
| **2.3.2**  | **Act as Researcher** – clone *AmpleGCG* repo → extract 200 generated suffixes → `attacks/suffixes/amplegcg/`. ([arxiv.org][12])                                                                                            | 200-line txt.                 | 1.6                 |
| **2.3.3**  | **Act as Researcher** – add 25 HotFlip trigger examples for text-classification bypass ([arxiv.org][10]) under `attacks/suffixes/hotflip/`.                                                                                 | `hotflip.txt`.                | 1.6                 |
| **2.4.1**  | **Act as Researcher** – reproduce HiddenLayer **TokenBreak** cases (homoglyph + spacer) ([hiddenlayer.com][4]) → `attacks/prompt/indirect/tokenbreak.md`.                                                                   | `tokenbreak.md`.              | 1.4                 |
| **2.5.1**  | **Act as Researcher** – notebook `poison_gen.ipynb` that synthesises poisoned training samples (ATLAS T0018) ([pointguardai.com][11]); save under `attacks/poisoning/pretrain/`.                                            | `.ipynb` committed.           | 1.3                 |
| **2.6.1**  | **Act as Researcher** – implement `membership_inference.py` PoC against Hugging Face API; store in `attacks/extraction/membership_inf/`.                                                                                    | runnable PoC.                 | 1.8                 |
| **2.7.1**  | **Act as Researcher** – create DoS prompt (∞-loop or token-flood) and AutoDoS black-box script; save under `attacks/dos/token_flood/`.                                                                                      | flood prompt + script.        | 1.7                 |
| **2.8.1**  | **Act as Researcher** – craft “robot-arm control” prompt bridging LLM → physical actuator (Wired/FT cases) ([theguardian.com][13], [ft.com][14]); store `attacks/physical/robotics/robot_arm.md`.                           | `robot_arm.md`.               | 1.4                 |
| **2.9.1**  | **Act as Researcher** – add malicious SketchUp plugin manifest JSON (LLM05 supply-chain) under `attacks/supply_chain/plugin/manifest.json`.                                                                                 | `manifest.json`.              | 1.4                 |
| **2.10.1** | **Act as Python Dev** – update `scripts/verify_coverage.py` to assert every ❌ in `docs/gap_matrix.md` now has a matching path; exit ≠ 0 on failure.                                                                         | Updated script.               | 2.\* tasks complete |
| **2.11.1** | **Act as DevOps** – add `attacks/**` to `.pre-commit` “check-yaml-front-matter” hook.                                                                                                                                       | Hook passes.                  | 0.8                 |

---

## STEP 3 · **Dataset pipeline** (`datasets/`)

| ID        | Jira Card                                                                                                                                                                                                                                          | Output                   | Depends                                                                                                                                                                                                                                                              |                    |              |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------ |
| **3.1.1** | **Act as Python Dev** – create `datasets/schema.py` defining `class AttackSample(BaseModel)` (Pydantic-v2) with fields `uuid:str, text:str, label:int, attack_type:str, source_path:str`. Use Pydantic schema facilities ([docs.pydantic.dev][7]). | `schema.py` + unit-test. | 0.4                                                                                                                                                                                                                                                                  |                    |              |
| **3.1.2** | **Act as Python Dev** – implement `scripts/build_dataset.py`: <br>• walk \`attacks/\*\*/\*.md                                                                                                                                                      | txt                      | py`<br>• normalise Unicode (NFC) and strip zero-width chars<br>• auto-label`label=1`for attack folder,`0`for control (empty for now)<br>• validate each sample with`AttackSample`<br>• write `datasets/v1/attacks.parquet\` via PyArrow API ([arrow.apache.org][6]). | `attacks.parquet`. | 2.\* , 3.1.1 |
| **3.1.3** | **Act as Python Dev** – add CLI flags (`--out-dir`, `--format {parquet,csv}`) and docstring usage; update README.                                                                                                                                  | documented script.       | 3.1.2                                                                                                                                                                                                                                                                |                    |              |
| **3.1.4** | **Act as QA Engineer** – write `tests/test_dataset_counts.py`: assert row-count ≥ file-count and all UUIDs unique.                                                                                                                                 | pytest file.             | 3.1.2                                                                                                                                                                                                                                                                |                    |              |
| **3.1.5** | **Act as DevOps** – extend CI (`ci.yml`) to run `python scripts/build_dataset.py --check-only` on every push; fails if schema invalid.                                                                                                             | CI gate green.           | 3.1.2                                                                                                                                                                                                                                                                |                    |              |
| **3.1.6** | **Act as Data Steward** – manually review 5 % random sample; save approvals into `datasets/v1/sample_for_review.csv`.                                                                                                                              | CSV file.                | 3.1.2                                                                                                                                                                                                                                                                |                    |              |

---

## STEP 4 · **Defensive filters** (`defenses/`)

| ID        | Jira Card                                                                                                                                                                            | Output           | Depends     |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- | ----------- |
| **4.1.1** | **Act as Python Dev** – implement `defenses/input_filters/zero_width.py` (`strip_zero_width(text:str)->str`). Include unit tests for `\u200B\u200C`.                                 | py + test.       | 1.4         |
| **4.1.2** | **Act as Python Dev** – create `homoglyph_map.json` (latin-greek confusables); implement `defenses/input_filters/homoglyph.py` that replaces mapped chars.                           | py + JSON.       | 1.4         |
| **4.1.3** | **Act as Python Dev** – build `defenses/input_filters/length_guard.py` (`abort_if_exceeds(tokens>8192)`).                                                                            | py + test.       | 1.7         |
| **4.2.1** | **Act as Python Dev** – write stateful `ContextFirewall` class in `defenses/context/window_firewall.py`; detects role-swap tokens like “### Assistant:” across sliding window (N=4). | py + docstring.  | 1.5         |
| **4.3.1** | **Act as Python Dev** – port JailGuard risk-score (token overlap + suspicious suffix detection) into `defenses/output_filters/jailguard.py`. ([huggingface.co][9])                   | py + docstring.  | 1.6         |
| **4.4.1** | **Act as Python Dev** – CLI wrapper `scripts/run_filters.py` (args: `--filter zero_width,homoglyph,…`) reading stdin → stdout / exit-code ≠ 0 if blocked.                            | runnable script. | 4.1.*-4.3.* |
| **4.5.1** | **Act as QA Engineer** – aggregate `tests/test_filters.py` with 20+ test-cases covering edge inputs; ensure `pytest --cov=defenses` ≥ 90 %.                                          | tests pass.      | 4.\*        |
| **4.6.1** | **Act as DevOps** – add `scripts/run_filters.py` smoke-run in CI pipeline.                                                                                                           | CI update.       | 4.4.1       |

---

## STEP 5 · **Baseline detector model** (`models/baseline/`)

| ID        | Jira Card                                                                                                                                                        | Output                         | Depends    |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ---------- |
| **5.1.1** | **Act as ML Engineer** – author `models/baseline/config.yaml` (batch\_size=32, lr=2e-5, epochs=3, model=distilroberta-base HF ID). ([huggingface.co][8])         | YAML committed.                | 0.4, 3.1.2 |
| **5.1.2** | **Act as ML Engineer** – implement `train.py`: Hugging Face `Trainer`, 80/20 split, early-stop on val F1. Save checkpoints under `models/baseline/checkpoints/`. | training script + checkpoints. | 5.1.1      |
| **5.1.3** | **Act as ML Engineer** – implement `eval.py` that outputs `metrics.json` (precision, recall, F1, ROC-AUC) and human-readable `eval.md`. Require F1 ≥ 0.80.       | metrics file + md report.      | 5.1.2      |
| **5.1.4** | **Act as ML-Ops** – push best checkpoint to HF Hub (`org/secure-llmattacks-baseline`); register tag `v0.1.0`.                                                    | HF model card live.            | 5.1.3      |
| **5.1.5** | **Act as DevOps** – extend `.github/workflows/model.yml`: retrain if `datasets/**` or `models/baseline/**` changes; upload new artefact to Release.              | CI workflow.                   | 5.1.2      |
| **5.1.6** | **Act as QA Engineer** – benchmark inference speed on Intel i5 CPU; ensure p95 < 400 ms (baseline pass-mark before INT8). Attach results to `eval.md`.           | timing numbers.                | 5.1.3      |

---

[1]: https://arxiv.org/abs/2307.15043?utm_source=chatgpt.com "Universal and Transferable Adversarial Attacks on Aligned Language Models"
[2]: https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf?utm_source=chatgpt.com "[PDF] OWASP Top 10 for LLM Applications 2025"
[3]: https://atlas.mitre.org/?utm_source=chatgpt.com "MITRE ATLAS™"
[4]: https://hiddenlayer.com/innovation-hub/the-tokenbreak-attack/?utm_source=chatgpt.com "The TokenBreak Attack - HiddenLayer"
[5]: https://www.anthropic.com/research/many-shot-jailbreaking?utm_source=chatgpt.com "Many-shot jailbreaking - Anthropic"
[6]: https://arrow.apache.org/docs/python/parquet.html?utm_source=chatgpt.com "Reading and Writing the Apache Parquet Format"
[7]: https://docs.pydantic.dev/1.10/usage/schema/?utm_source=chatgpt.com "Schema - Pydantic"
[8]: https://huggingface.co/distilbert/distilroberta-base?utm_source=chatgpt.com "distilbert/distilroberta-base - Hugging Face"
[9]: https://huggingface.co/docs/transformers/main/quantization/bitsandbytes?utm_source=chatgpt.com "Bitsandbytes - Hugging Face"
[10]: https://arxiv.org/abs/1712.06751?utm_source=chatgpt.com "HotFlip: White-Box Adversarial Examples for Text Classification"
[11]: https://www.pointguardai.com/blog/understanding-the-mitre-atlas-matrix-for-ai-threats?utm_source=chatgpt.com "Understanding the MITRE ATLAS Matrix for AI Threats - AppSOC"
[12]: https://arxiv.org/html/2404.07921v3?utm_source=chatgpt.com "AmpleGCG: Learning a Universal and Transferable Generative ..."
[13]: https://www.theguardian.com/technology/2024/apr/03/many-shot-jailbreaking-ai-artificial-intelligence-safety-features-bypass?utm_source=chatgpt.com "'Many-shot jailbreak': lab reveals how AI safety features can be easily bypassed"
[14]: https://www.ft.com/content/14a2c98b-c8d5-4e5b-a7b0-30f0a05ec432?utm_source=chatgpt.com "Hackers 'jailbreak' powerful AI models in global effort to highlight flaws"

---

## Step 6 · Distilled **TinyBERT-INT8** model (`models/tinybert_int8/`)

TinyBERT gives \~96 % of BERT accuracy at 7× speed-up ([arxiv.org][1]), while **bits-and-bytes** INT8 keeps the footprint under 500 MB RAM without large accuracy loss ([huggingface.co][2]).
We therefore distil from the baseline (Step 5) into a 6-layer TinyBERT student and quantise to INT8.

| ID        | Jira Card (atomic)                                                                                                                                                                                                                                | Output                   | Depends |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------- |
| **6.1.1** | **Act as ML Engineer** – create `models/tinybert_int8/config_distill.yaml` (teacher = `baseline/checkpoints/best`, student = `huawei-noah/TinyBERT_General_6L_768D`, T = 2, α logits = 0.7, α hidden = 0.3).                                      | YAML file committed.     | 5.1.3   |
| **6.1.2** | **Act as ML Engineer** – implement `distill.py`: wraps HF **Trainer** with knowledge-distillation loss (KD-logits + KD-hidden) as per HF recipe ([huggingface.co][3]); logs to Weights & Biases sweep.                                            | `distill.py` + W\&B run. | 6.1.1   |
| **6.1.3** | **Act as ML Engineer** – run hyper-parameter sweep (`lr ∈ {2e-5,1e-5}, epochs ∈ {4,6}`); keep checkpoint with best F1 on val set; store under `models/tinybert_int8/checkpoints/`.                                                                | Best checkpoint dir.     | 6.1.2   |
| **6.1.4** | **Act as ML Engineer** – implement `eval_distilled.py`; must output `metrics.json` with F1 ≥ 0.88; abort if drop > 2 % vs. teacher.                                                                                                               | metrics file.            | 6.1.3   |
| **6.2.1** | **Act as ML Engineer** – write `quantize.py` calling `bitsandbytes.quantization.llm_int8()` to convert checkpoint to INT8; save to `models/tinybert_int8/int8/`. ([huggingface.co][4])                                                            | INT8 model files.        | 6.1.3   |
| **6.2.2** | **Act as QA Engineer** – benchmark latency via `bench.py` (1000 sentences, batch=8, CPU); assert p95 < 200 ms; record in `bench_report.md`.                                                                                                       | timing report.           | 6.2.1   |
| **6.2.3** | **Act as ML-Ops** – publish INT8 model to HF Hub under tag `v1.0.0-int8`; include `README.md` with task, dataset, metrics.                                                                                                                        | HF model card live.      | 6.2.2   |
| **6.3.1** | **Act as DevOps** – extend `.github/workflows/model.yml`: if `datasets/**` OR `models/tinybert_int8/**` change, re-run `distill.py`, `quantize.py`, `eval_distilled.py`; upload artefacts using `actions/upload-artifact`. ([docs.github.com][5]) | CI workflow updated.     | 6.2.3   |

*Why benchmarks & gates?*
Latency and F1 thresholds guarantee the small model is production-ready before we wire it into any API.

---

## Step 7 · **Evaluation harness** (`scripts/eval_defenses.py`)

We need a repeatable harness that runs every *filter × model* pair against the attack corpus, then produces ROC & confusion-matrix artefacts using **scikit-learn** visual API ([scikit-learn.org][6]) and **evaluate-roc\_auc** ([huggingface.co][7]).

| ID        | Jira Card                                                                                                                                                                                      | Output            | Depends          |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------- |
| **7.1.1** | **Act as Python Dev** – write `eval_defenses.py`: iterates over models (`baseline`,`tinybert_int8`), pipelines text through selected input-filters, then calls model; collects probs & labels. | script committed. | 4.\* 5.1.3 6.2.3 |
| **7.1.2** | **Act as Python Dev** – add helper `metrics.py` (`compute_roc`, `compute_confusion`) using scikit-learn’s `roc_auc_score`, `confusion_matrix` ([scikit-learn.org][8]).                         | `metrics.py`.     | 7.1.1            |
| **7.2.1** | **Act as Python Dev** – generate ROC curve png via `sklearn.metrics.RocCurveDisplay` into `reports/eval/YYYY-MM-DD/roc_{model}_{filter}.png`.                                                  | ROC images.       | 7.1.2            |
| **7.2.2** | **Act as Python Dev** – generate confusion-matrix png via `ConfusionMatrixDisplay`.                                                                                                            | CM images.        | 7.1.2            |
| **7.3.1** | **Act as Technical Writer** – compile Markdown report `reports/eval/YYYY-MM-DD/index.md` embedding images and key metrics.                                                                     | report md.        | 7.2.\*           |
| **7.4.1** | **Act as DevOps** – extend CI: run harness nightly (`schedule: cron '0 2 * * *'`), upload artefacts; fail job if F1 (tinybert + full-filter-stack) < 0.86 or latency > 200 ms.                 | nightly CI job.   | 7.1.*-7.3.*      |

*Why scikit-learn plots?*
They require **no extra JS libs**, render deterministically in CI, and are familiar to every ML engineer.

---

## Step 8 · **Documentation & ADRs** (`docs/`)

Quality documentation guarantees maintainability. **MkDocs Material** handles the static site ([squidfunk.github.io][9]). ADRs follow the lightweight template by Nygard ([adr.github.io][10]).

| ID        | Jira Card                                                                                                                                              | Output               | Depends        |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------- | -------------- |
| **8.1.1** | **Act as Security Architect** – write `docs/threat_model.md`: map each OWASP LLM risk to MITRE ATLAS tactics and our mitigations (filters + detector). | threat\_model.md.    | 1.\* 4.\* 6.\* |
| **8.2.1** | **Act as Architect** – add `docs/adr/_template.md` (status, context, decision, consequences).                                                          | template file.       | 0.6            |
| **8.2.2** | **Act as Architect** – create `ADR-0001-folder_structure.md` (why `/secure_llmattacks_v3`).                                                            | ADR-1 md.            | 0.\*           |
| **8.2.3** | **Act as Architect** – create `ADR-0002-model_choice.md` (TinyBERT 6L + INT8).                                                                         | ADR-2 md.            | 6.\*           |
| **8.2.4** | **Act as Architect** – create `ADR-0003-filter_stack.md` (zero-width → homoglyph → length → context FW).                                               | ADR-3 md.            | 4.\*           |
| **8.3.1** | **Act as Tech Writer** – update `mkdocs.yml`: add nav sections for “Threat Model”, “ADRs”, “Eval Reports”.                                             | mkdocs config.       | 8.1.\* 8.2.\*  |
| **8.3.2** | **Act as DevOps** – add GitHub Pages workflow `.github/workflows/docs.yml`: builds MkDocs, deploys to `gh-pages`.                                      | workflow file.       | 8.3.1          |
| **8.4.1** | **Act as Tech Writer** – create `docs/contributing.md`: describe `poetry install`, `pre-commit`, CI rules, issue labels.                               | contributing.md.     | 0.8            |
| **8.4.2** | **Act as DevOps** – add issue & PR templates (`.github/ISSUE_TEMPLATE/*.yml`).                                                                         | templates committed. | 8.4.1          |
| **8.5.1** | **Act as DevOps** – gate docs build in CI; fail if MkDocs warnings > 0.                                                                                | CI update.           | 8.3.2          |

*Why ADRs now?*
Formalising choices *before* code locks in avoids “why did we do this?” six months later.

---

### Dependency Graph Snapshot

```
0.*  → 1.*  → 2.*  → 3.*  → 4.*  → 5.*
                     ↘                ↘
                      6.*  → 7.*  → 8.*
```

Parallel work is possible wherever IDs have satisfied “Depends on”.
With these cards in Jira, every junior or agent knows **exactly** what file to touch, what test to write, and what CI gate must stay green.

[1]: https://arxiv.org/abs/1909.10351?utm_source=chatgpt.com "TinyBERT: Distilling BERT for Natural Language Understanding"
[2]: https://huggingface.co/docs/transformers/en/quantization/bitsandbytes?utm_source=chatgpt.com "bitsandbytes - Hugging Face"
[3]: https://huggingface.co/docs/transformers/tasks/knowledge_distillation_for_image_classification?utm_source=chatgpt.com "Knowledge Distillation for Computer Vision - Hugging Face"
[4]: https://huggingface.co/docs/transformers/main_classes/quantization?utm_source=chatgpt.com "Quantization - Hugging Face"
[5]: https://docs.github.com/actions/using-workflows/storing-workflow-data-as-artifacts?utm_source=chatgpt.com "Storing and sharing data from a workflow - GitHub Docs"
[6]: https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html?utm_source=chatgpt.com "ROC Curve with Visualization API - Scikit-learn"
[7]: https://huggingface.co/spaces/evaluate-metric/roc_auc?utm_source=chatgpt.com "ROC AUC - a Hugging Face Space by evaluate-metric"
[8]: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html?utm_source=chatgpt.com "confusion_matrix — scikit-learn 1.7.0 documentation"
[9]: https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/?utm_source=chatgpt.com "Setting up navigation - Material for MkDocs - GitHub Pages"
[10]: https://adr.github.io/?utm_source=chatgpt.com "Architectural Decision Records"

---

## 🗂️ Step 9 · Release & Handoff (`v3.0.0`)

| ID        | Jira Card (single action)                                                                                                                                                                         | Output / Path                   | Depends        |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | -------------- |
| **9.1.1** | **Act as Release Manager** – create **semantic version tag** `v3.0.0` with message summarising changelog.<br>Use annotated tag (`git tag -a`).                                                    | Git tag visible on GitHub.      | 6.\* 7.\* 8.\* |
| **9.1.2** | **Act as Release Manager** – draft **GitHub Release** from tag; attach compiled artefacts:<br> • `models/tinybert_int8/int8/` zip<br> • `datasets/v1/attacks.parquet`<br> • `reports/eval/*`      | Release page with binaries.     | 9.1.1          |
| **9.1.3** | **Act as DevOps** – add workflow step `actions/upload-artifact@v4` to publish build outputs into the Release. ([github.com][1])                                                                   | `.github/workflows/release.yml` | 9.1.2          |
| **9.1.4** | **Act as Security Engineer** – generate **CycloneDX SBOM** (`sbom.cdx.json`) for runtime deps via `cyclonedx-py` and attach to Release. ([github.com][2], [cyclonedx-bom-tool.readthedocs.io][3]) | SBOM file.                      | 9.1.2          |
| **9.1.5** | **Act as Security Engineer** – add **build-provenance attestation** step (`actions/attest-build-provenance`) for SLSA Level 2 compliance. ([docs.github.com][4], [github.com][5])                 | provenance `.intoto.jsonl`.     | 9.1.3          |
| **9.1.6** | **Act as Product Owner** – update `docs/RELEASE_NOTES.md` summarising features, security highlights (SBOM, attestation).                                                                          | Markdown notes.                 | 9.1.2          |

*Why?* Semantic tags make releases traceable ([gitkraken.com][6]), GitHub Releases surface binaries to users ([docs.github.com][7]), and SBOM + SLSA evidence satisfy modern supply-chain policies.

---

## 🛡️ Step 10 · Enforcement Gates (always-on CI)

| ID         | Jira Card                                                                                                                                                                      | Output / Path                      | Depends       |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- | ------------- |
| **10.1.1** | **Act as DevOps** – integrate **pip-audit** in CI; fail if vulnerabilities ≥ HIGH. ([pypi.org][8])                                                                             | CI job.                            | 0.9           |
| **10.1.2** | **Act as DevOps** – schedule **Dependabot security updates** (`security_updates: daily`) for both Python and GitHub Actions. ([docs.github.com][9], [docs.github.com][10])     | `.github/dependabot.yml`.          | 0.9           |
| **10.1.3** | **Act as Security Engineer** – add **OpenSSF Scorecard** GitHub Action; block PR if score < 7. ([github.com][11], [github.com][12])                                            | new workflow.                      | 0.9           |
| **10.1.4** | **Act as Security Engineer** – add **detect-secrets** pre-commit hook; CI fails on leaked creds. ([github.com][13])                                                            | `.pre-commit-config.yaml` updated. | 0.8           |
| **10.1.5** | **Act as Security Engineer** – enable **CodeQL** default analysis for Python & YAML; run on PR + weekly cron. ([github.com][14], [docs.github.com][15], [docs.github.com][16]) | `codeql-analysis.yml`.             | 0.9           |
| **10.1.6** | **Act as DevOps** – add gate that rejects merge if CodeQL or Scorecard raises *critical* issues.                                                                               | CI rule.                           | 10.1.3 10.1.5 |
| **10.1.7** | **Act as Tech Writer** – update `docs/contributing.md` to reflect new security gates and how to fix failures.                                                                  | contributing.md.                   | 8.4.1         |

*Why?* These tools ensure the repo stays patched (**pip-audit**) ([blog.inedo.com][17]), auto-updates vulnerable dependencies (**Dependabot**) ([docs.github.com][9]), monitors OSS best-practices (**Scorecard**) ([github.com][11]), blocks secret leaks (**detect-secrets**) ([github.com][13]), and performs static security analysis (**CodeQL**) ([github.blog][18]).

---

## 🔄 Step 11 · Post-release Monitoring & Improvement

| ID         | Jira Card                                                                                                                              | Output / Path                               | Depends |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | ------- |
| **11.1.1** | **Act as ML-Ops** – schedule **monthly re-training cron**; retrain TinyBERT if `datasets/` grows by ≥ 5 %.                             | cron job in `model.yml`.                    | 6.3.1   |
| **11.1.2** | **Act as Data Steward** – implement `scripts/check_dataset_drift.py`; runs KS-test on feature lengths, alerts on drift p < 0.05.       | script + CI.                                | 3.1.2   |
| **11.1.3** | **Act as Security Ops** – subscribe repo to **GitHub Security Advisories**; triage within 24 h.                                        | process doc in `docs/security_response.md`. | 10.\*   |
| **11.1.4** | **Act as DevOps** – run **Scorecard Action** weekly via `cron '0 3 * * 1'`; store results in `reports/scorecard/`.                     | report JSON.                                | 10.1.3  |
| **11.1.5** | **Act as Security Researcher** – open quarterly issue **“New LLM attack vectors Qn-YYYY”**; review new papers; update `gap_matrix.md`. | GitHub discussion template.                 | 1.\*    |
| **11.1.6** | **Act as Community Manager** – monitor HF Hub model page; respond to issues; mirror changelog.                                         | community replies.                          | 6.2.3   |
| **11.1.7** | **Act as Product Owner** – conduct post-mortem for any CI security gate failure; record in `docs/postmortems/`.                        | retrospective docs.                         | 10.\*   |

*Why?* Regular retrain / drift checks keep the detector relevant, Scorecard & Advisories surface ecosystem risks, and a formal response loop ensures institutional learning.

---

### Final dependency snapshot

```
6.* → 9.* → 10.* → 11.*
            ↘
             8.*
```

With these cards imported into Jira, every actor—Dev Ops, ML Ops, Security, Docs—knows **exactly what to ship, where to commit, and which gates must remain green**.

[1]: https://github.com/actions/upload-artifact?utm_source=chatgpt.com "actions/upload-artifact - GitHub"
[2]: https://github.com/CycloneDX/cyclonedx-python?utm_source=chatgpt.com "CycloneDX Software Bill of Materials (SBOM) generator for Python ..."
[3]: https://cyclonedx-bom-tool.readthedocs.io/?utm_source=chatgpt.com "CycloneDX SBOM Generation Tool for Python — CycloneDX Python ..."
[4]: https://docs.github.com/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds?utm_source=chatgpt.com "Using artifact attestations to establish provenance for builds"
[5]: https://github.com/actions/attest-build-provenance?utm_source=chatgpt.com "actions/attest-build-provenance - GitHub"
[6]: https://www.gitkraken.com/gitkon/semantic-versioning-git-tags?utm_source=chatgpt.com "Managing Releases with Semantic Versioning and Git Tags"
[7]: https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository?utm_source=chatgpt.com "Managing releases in a repository - GitHub Docs"
[8]: https://pypi.org/project/pip-audit/?utm_source=chatgpt.com "pip-audit - PyPI"
[9]: https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates?utm_source=chatgpt.com "About Dependabot security updates - GitHub Docs"
[10]: https://docs.github.com/github/managing-security-vulnerabilities/configuring-dependabot-security-updates?utm_source=chatgpt.com "Configuring Dependabot security updates - GitHub Docs"
[11]: https://github.com/ossf/scorecard-action?utm_source=chatgpt.com "ossf/scorecard-action: Official GitHub Action for OpenSSF Scorecard."
[12]: https://github.com/ossf/scorecard?utm_source=chatgpt.com "OpenSSF Scorecard - Security health metrics for Open Source"
[13]: https://github.com/Yelp/detect-secrets?utm_source=chatgpt.com "Yelp/detect-secrets - GitHub"
[14]: https://github.com/github/codeql-action?utm_source=chatgpt.com "Actions for running CodeQL analysis - GitHub"
[15]: https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql?utm_source=chatgpt.com "About code scanning with CodeQL - GitHub Docs"
[16]: https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning?utm_source=chatgpt.com "Customizing your advanced setup for code scanning - GitHub Docs"
[17]: https://blog.inedo.com/python/pypi-package-vulnerabilities/?utm_source=chatgpt.com "Python Package Vulnerabilities: Where pip audit Falls Short and ..."
[18]: https://github.blog/changelog/2025-04-22-github-actions-workflow-security-analysis-with-codeql-is-now-generally-available/?utm_source=chatgpt.com "GitHub Actions workflow security analysis with CodeQL is now ..."

---

## Step 12 · Production Inference API & Gateway (`secure_llmattacks_v3/api/`)

| ID         | Jira Card                                                                                                                                                                                                                                           | Output            | Depends |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ------- |
| **12.1.1** | **Act as Backend Dev** – scaffold `api/server.py`: load `models/tinybert_int8/int8/` once, expose `/v1/detect` (POST {text}) returning `{score,attack}`; FastAPI auto-docs enabled.                                                                 | server.py         | 6.2.1   |
| **12.1.2** | **Act as DevOps** – create `Dockerfile`: `python:3.11-slim`, `poetry install --no-dev`, run `gunicorn -k uvicorn.workers.UvicornWorker -w 4 -b 0.0.0.0:8000 api.server:app` per FastAPI prod guidance ([fastapi.tiangolo.com][1], [medium.com][2])  | Dockerfile        | 12.1.1  |
| **12.1.3** | **Act as DevOps** – K8s Helm chart `deploy/helm/inference/` with HPA triggered on CPU & p95 latency; fallback option: HF Inference Endpoint values yaml if self-hosted not desired ([huggingface.co][3], [huggingface.co][4])                       | Helm chart        | 12.1.2  |
| **12.1.4** | **Act as DevOps** – wire **Prometheus-FastAPI-Instrumentator** for `/metrics`; add to `server.py`. ([github.com][5])                                                                                                                                | metrics endpoint  | 12.1.1  |
| **12.1.5** | **Act as DevOps** – integrate **OpenTelemetry** traces (`OTEL_EXPORTER_OTLP_ENDPOINT`) with SigNoz recipe. ([signoz.io][6])                                                                                                                         | tracing code      | 12.1.1  |
| **12.1.6** | **Act as Security Eng** – implement middleware: <br>• Rate-limit 30 r/s/ip (`async-limiter`) <br>• JWT Bearer auth header.<br>• Reject requests > 8 k tokens.<br>Map measures to OWASP API Top-10 (API4/Rate Limiting, API1/Auth). ([owasp.org][7]) | `api/security.py` | 12.1.1  |
| **12.1.7** | **Act as SRE** – write `locust/locustfile.py`; run soak test 50 rps, 10 min; assert p95 latency < 300 ms (benchmark numbers from bits-and-bytes INT8 perf). ([github.com][8], [medium.com][9])                                                      | test report       | 6.2.2   |
| **12.1.8** | **Act as DevOps** – extend CI: build/push `ghcr.io/org/secure-llmattacks-infer:sha` on PR; run container health-check (`/healthz`) in workflow.                                                                                                     | CI job            | 12.1.2  |
| **12.1.9** | **Act as QA Eng** – integration test `tests/api/test_detect.py` hitting live container via `pytest-docker`; assert 200, schema, JWT required.                                                                                                       | pytest file       | 12.1.8  |

---

## Step 13 · SDKs & Client Integration

| ID         | Jira Card                                                                                                                                                       | Output             | Depends       |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------- |
| **13.1.1** | **Act as SDK Eng** – generate OpenAPI spec (`openapi.json`) from FastAPI; store under `api/schema/`.                                                            | openapi.json       | 12.1.1        |
| **13.1.2** | **Act as Python SDK Eng** – auto-generate client via `openapi-python-client`, publish to PyPI as `secure-llmattacks-sdk`.                                       | PyPI release       | 13.1.1        |
| **13.1.3** | **Act as Front-end Eng** – generate TypeScript SDK via `openapi-typescript-codegen`, publish to npm `@secure/llmattacks-sdk`.                                   | npm package        | 13.1.1        |
| **13.1.4** | **Act as DevOps** – GitHub Action to release SDKs on tag; sign packages with Sigstore keyless.                                                                  | workflow file      | 13.1.2 13.1.3 |
| **13.2.1** | **Act as Solutions Arch** – sample CI/CD integration: GitLab CI job that scans commit messages and blocks merge if `score > 0.7`. Add under `examples/gitlab/`. | example yml        | 13.1.2        |
| **13.2.2** | **Act as Product Owner** – build demo Jupyter notebook (`examples/notebooks/demo.ipynb`) that loops over text list and visualises risk scores.                  | notebook           | 13.1.2        |
| **13.3.1** | **Act as Tech Writer** – expand docs: “Getting Started (Python, JS, CI)”; embed code snippets.                                                                  | docs/sdk\_guide.md | 13.\*         |

---

## Step 14 · Legal · Privacy · Compliance

| ID         | Jira Card                                                                                                                                                                                                                                    | Output                      | Depends    |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ---------- |
| **14.1.1** | **Act as Privacy Officer** – perform GDPR data-minimisation assessment; document flows, retention, pseudonymisation measures, referencing ICO guidelines. ([ico.org.uk][10])                                                                 | `docs/privacy/gdpr_dpia.md` | 3.\* 12.\* |
| **14.1.2** | **Act as Legal Counsel** – draft **CPRA compliance memo**: how logs, user IDs, model outputs qualify as personal info (PI) per amended CCPA §1798.140; reference CA AG advisories. ([iapp.org][11], [sfchronicle.com][12], [apnews.com][13]) | `docs/privacy/cpra_memo.md` | 14.1.1     |
| **14.1.3** | **Act as Compliance Eng** – map ISO 27001:2022 Annex A controls (esp. 8.25 Secure coding, 5.20 Data deletion) to repo artefacts; store `docs/compliance/iso27001_mapping.xlsx`. ([dev.to][14])                                               | mapping file                | 9.1.4      |
| **14.2.1** | **Act as Sec Researcher** – update `docs/gap_matrix.md` with any new ATLAS attack IDs from 2025 release. ([last9.io][15])                                                                                                                    | gap matrix updated          | 11.1.5     |
| **14.3.1** | **Act as DevOps** – run `license-scanner` workflow (e.g. FOSSA) on every PR; fail if forbidden licences.                                                                                                                                     | CI job                      | 9.1.4      |
| **14.3.2** | **Act as Security Eng** – add “Responsible AI use” section to `README.md` (no medical/legal advice, bias testing).                                                                                                                           | README updated              | 14.1.2     |
| **14.4.1** | **Act as Compliance Lead** – schedule annual external pentest & policy review; generate ticket in GitHub Projects with due-date.                                                                                                             | project task                | 14.\*      |

---

### Key References

* FastAPI + Gunicorn/Uvicorn prod deployment guides ([fastapi.tiangolo.com][1], [medium.com][2])
* HF Inference Endpoint patterns for autoscaling ([huggingface.co][3], [huggingface.co][4])
* Bits-and-bytes latency & quantisation notes ([github.com][8], [medium.com][9])
* Prometheus instrumentation lib for FastAPI ([github.com][5])
* OpenTelemetry FastAPI tracing tutorial ([signoz.io][6])
* OWASP API Security Top 10 (2023) ([owasp.org][7])
* ICO guidance on data minimisation for AI ([ico.org.uk][10])
* California CPRA / AG AI advisories ([iapp.org][11], [sfchronicle.com][12], [apnews.com][13])
* CycloneDX & SBOM practices (ISO 27001 link) ([medium.com][9])
* MITRE ATLAS 2025 update roadmap ([last9.io][15])

These three steps complete the **operational, integrative, and regulatory** layers required for enterprise-ready LLM-attack detection. Import each ID into Jira, wire dependencies, and keep CI gates green.

[1]: https://fastapi.tiangolo.com/deployment/server-workers/?utm_source=chatgpt.com "Server Workers - Uvicorn with Workers - FastAPI"
[2]: https://medium.com/%40rameshkannanyt0078/deploying-fastapi-with-gunicorn-and-uvicorn-a-production-ready-guide-8610be9a603e?utm_source=chatgpt.com "Deploying FastAPI with Gunicorn and Uvicorn: A Production-Ready ..."
[3]: https://huggingface.co/docs/inference-endpoints/en/index?utm_source=chatgpt.com "Inference Endpoints - Hugging Face"
[4]: https://huggingface.co/inference-endpoints/dedicated?utm_source=chatgpt.com "Inference Endpoints - Hugging Face"
[5]: https://github.com/trallnag/prometheus-fastapi-instrumentator?utm_source=chatgpt.com "trallnag/prometheus-fastapi-instrumentator - GitHub"
[6]: https://signoz.io/blog/opentelemetry-fastapi/?utm_source=chatgpt.com "Implementing OpenTelemetry in FastAPI - A Practical Guide - SigNoz"
[7]: https://owasp.org/API-Security/editions/2023/en/0x11-t10/?utm_source=chatgpt.com "OWASP Top 10 API Security Risks – 2023"
[8]: https://github.com/TimDettmers/bitsandbytes/issues/6?utm_source=chatgpt.com "Memory Decreases! But Latency Increases.... · Issue #6 - GitHub"
[9]: https://medium.com/byte-sized-ai/vllm-quantization-bitsandbytes-efaec31f00df?utm_source=chatgpt.com "[vLLM — Quantization] bitsandbytes: 8-bit Optimizers, LLM.int8 ..."
[10]: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/how-should-we-assess-security-and-data-minimisation-in-ai/?utm_source=chatgpt.com "How should we assess security and data minimisation in AI? | ICO"
[11]: https://iapp.org/news/a/new-laws-in-california-look-to-the-future-of-privacy-and-ai?utm_source=chatgpt.com "New laws in California look to the future of privacy and AI - IAPP"
[12]: https://www.sfchronicle.com/california/article/ai-bonta-laws-attorney-general-20027662.php?utm_source=chatgpt.com "Exclusive: AG Bonta puts health care, other industries on notice on use of AI"
[13]: https://apnews.com/article/4d94c4c18167ee624ddb193d4fcd7394?utm_source=chatgpt.com "California advances measures targeting AI discrimination and deepfakes"
[14]: https://dev.to/ken_mwaura1/getting-started-monitoring-a-fastapi-app-with-grafana-and-prometheus-a-step-by-step-guide-3fbn?utm_source=chatgpt.com "Getting Started: Monitoring a FastAPI App with Grafana and ..."
[15]: https://last9.io/blog/integrating-opentelemetry-with-fastapi/?utm_source=chatgpt.com "A Complete Guide to Integrating OpenTelemetry with FastAPI - Last9"
