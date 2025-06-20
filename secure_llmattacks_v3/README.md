# Secure LLM Attacks v3

This directory is a clean workspace for the third major iteration of the project. It isolates new code and datasets from the legacy catalog found in `original_v2_snapshot/`.

The goal is to research and develop techniques for detecting and mitigating adversarial prompts against large language models. All experiments and artifacts are organised in the subfolders listed below.

## Folder structure

- `attacks/` – attack corpora and scripts
- `datasets/` – processed datasets
- `defenses/` – mitigation code
- `models/` – model checkpoints and training outputs
- `scripts/` – utility scripts and CLI tools
- `docs/` – documentation and research notes
- `.github/` – CI workflows and configuration
- `original_v2_snapshot/` – placeholder snapshot of the previous version

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
```

Running the tests confirms that your environment and dependencies are set up correctly.
