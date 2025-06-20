# Secure LLM Attacks v3

This workspace collects research code and datasets for studying secure large language model attacks and defenses.  It mirrors the wider `llmattacks` catalog but is structured for reproducible experimentation.

## Folder Map

- `attacks/` – curated attack prompts and corpora
- `datasets/` – processed datasets and artifacts
- `defenses/` – mitigation code and filters
- `models/` – model checkpoints and configs
- `scripts/` – helper utilities
- `docs/` – project documentation
- `.github/` – CI workflows specific to this module
- `src/secure_llmattacks_v3/` – installable Python package
- `tests/` – unit tests

## Quick Start

1. Install the package and dependencies from the project root:
   ```bash
   python3 -m pip install -e secure_llmattacks_v3
   ```
2. Run the test suite:
   ```bash
   pytest
   ```

The project uses a standard `pyproject.toml`—no Poetry workflow is required.
