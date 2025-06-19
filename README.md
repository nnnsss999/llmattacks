# LLM Attacks Catalog

This repository collects documented techniques for attacking large language models (LLMs). Each markdown file in `docs/` summarizes a known or theorized vector, linking to the original research or incident report.

The catalog is maintained for researchers and defenders who need a single reference point for adversarial methods ranging from classic prompt injection to training data poisoning.

New additions cover emerging *reinforcement-learning alignment attacks* such as [Reverse Preference Attack](docs/training-alignment/reinforcement-learning-alignment-attacks.md), [BadReward](docs/training-alignment/reinforcement-learning-alignment-attacks.md#badreward-clean-label-poisoning), and [Adversarial Preference Learning](docs/training-alignment/reinforcement-learning-alignment-attacks.md#adversarial-preference-learning). See the `training-alignment` folder for details.

An [**Attack–Defence Matrix**](docs/attack-defense-matrix.md) cross-links each attack with representative mitigations for quick reference.

## Browse Online

A searchable website built with **MkDocs Material** is automatically deployed to GitHub Pages. Visit <https://example.github.io/llmattacks/> to explore the catalog with Mermaid diagrams enabled.

## Repository Structure and Timeline

- All documentation files under `docs/` include YAML front matter with a
  `date_collected` of **2025-06-18**, marking the snapshot used to build the
  catalog. Key folders include:

- `docs/` – canonical Markdown and HTML articles grouped into subfolders:
`agentic/`, `data-poisoning/`, `defenses/`, `emerging/`, `evaluation/`,
  `embedding/`, `inference/`, `insecure-output/`, `latent-space/`,
  `linguistic-manipulation/`, `multimodal/`, `optimization/`,
  `prompt-dialogue/`, `rag/`, `social-engineering/`, `supply-chain/`,
  `token-level/` and `training-alignment/`.
- `original/` – the original PDF and Markdown source for the catalog.
- `pdfs/` – a local cache of PDFs; see `pdfs/README.md` for details.
- `scripts/` – utility Python scripts including:
  - `build_index.py` to generate `index.json`
  - `cache_pdfs.py` to download PDF sources
  - `scrub_js.py` to remove third-party JS
  - `generate_sbom.py` to create `sbom.json`
  - `check_front_matter.py` to enforce YAML headers
  - `check_duplicates.py` to find duplicate docs
  - `link_check.py` to test URLs
  - `refresh_links.py` to update `link_archive.json`
  - `rename.py` to enforce kebab-case filenames
- `tests/` – unit tests (`test_link_check.py` and `test_sbom.py`) validating the helper scripts.
- `docs_files.txt` – manifest listing every document archived in this
  repository (59 entries).
- `llm-attack-catalog.md` – printable version of the master catalog inside `docs/`.
- `fixes-1.md` – issue log and proposed improvements.
- `link_archive.json` – Wayback Machine snapshots of referenced URLs.
- `sbom.json` – machine-readable bill of materials (CycloneDX 1.5) linking each
  document with its metadata.
- `docs/navigation-map.md` – human-readable map of every file in the
  repository with a short description.
- `index.json` – JSON index generated from the YAML front matter.
- `.github/workflows/` – GitHub Actions workflows:
  - `ci.yml` runs linting and unit tests
  - `gh-pages.yml` deploys the MkDocs site
  - `link-check.yml` scans for broken links
  - `refresh-links.yml` archives URLs weekly
- `.pre-commit-config.yaml` – pre‑commit hooks (markdownlint v0.38.0,
  codespell v2.4.1 and custom validators).
- `mkdocs.yml` – configuration for building the documentation website.

## Using This Repository

- The **canonical files** reside under `docs/` and use kebab‑case names.
- Each file may include YAML front matter describing the source, category, and license.
- A compiled PDF version is provided for offline viewing.
- Run `python scripts/build_index.py` to regenerate `index.json`, which lists all catalog entries by category and date.
- Run `python scripts/cache_pdfs.py` to locally cache PDF sources when allowed.
- Run `python scripts/scrub_js.py` to remove third-party `<script>` tags and cookie banners from HTML or Markdown files.
- Run `python scripts/generate_sbom.py` to regenerate `sbom.json`, a CycloneDX SBOM of all source files for traceability.
- Run `python scripts/check_front_matter.py` to validate YAML front matter across the catalog.
- Run `python scripts/check_duplicates.py` to detect duplicate markdown entries.
- Run `python scripts/link_check.py` to spot broken links locally.
- Run `python scripts/refresh_links.py` to update `link_archive.json` with fresh Wayback snapshots.
- Broken links are checked via `lychee` in CI.
- A scheduled workflow refreshes external links weekly and stores Wayback Machine snapshots in `link_archive.json`.

## URL Extraction

`docs/urls.md` enumerates articles and papers for future inclusion in the catalog.
Run `python scripts/extract_urls.py` to download each resource and convert it to
Markdown in the `extractions1/` directory. URLs already represented in `docs/`
are skipped automatically. A summary of processed links is written to
`extractions1/extraction_log.json`.

## Contributing

Contributions are welcome! Please review [CONTRIBUTING.md](CONTRIBUTING.md) for coding style and front‑matter guidelines. All content must respect the project license and third‑party terms.

## Development Workflow

This project uses **pre-commit** hooks for basic linting and a GitHub Actions pipeline that runs the hooks and unit tests. Run `pre-commit run --all-files` and `pytest` before committing; the CI will enforce these checks on every pull request.

## License

All original content is licensed under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) license. Third‑party excerpts remain under their respective licenses.
