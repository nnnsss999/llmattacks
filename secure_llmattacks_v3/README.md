# Secure LLM Attacks v3

This directory contains a clean workspace for the next version of the project.
Legacy files from v2 are referenced under `original_v2_snapshot/`.

## Folder layout

- `attacks/` – attack corpora and scripts
- `datasets/` – processed datasets
- `defenses/` – mitigation code
- `models/` – training outputs
- `scripts/` – utility scripts
- `docs/` – documentation

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ./secure_llmattacks_v3[dev]
pytest
```
