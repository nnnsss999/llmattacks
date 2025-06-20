# Secure LLM Attacks v3

[![CI](https://github.com/example/llmattacks/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/example/llmattacks/actions/workflows/ci.yml)

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
pre-commit install
pytest
```
