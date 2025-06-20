# Secure LLM Attacks v3

This workspace provides a trimmed snapshot of the `llmattacks` project focused on reproducible experimentation with large language model security.  All dependencies are declared in `pyproject.toml` so installation works with standard `pip` tooling—no Poetry setup required.  Development occurs on the `master` branch.

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
