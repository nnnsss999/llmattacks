# Secure LLM Attacks v3

This workspace contains code and datasets for exploring secure large language model attacks and defenses. It is a self-contained snapshot of the broader `llmattacks` project with a focus on reproducible experiments. All tooling is defined in a simple `pyproject.toml`, so no Poetry workflow is required.

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

1. Ensure Python 3.11 is available and install the package from the repository root:
   ```bash
   python3 -m pip install -e secure_llmattacks_v3
   ```
2. Run the test suite:
   ```bash
   pytest
   ```

