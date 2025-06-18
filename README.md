# LLM Attacks Catalog

This repository collects documented techniques for attacking large language models (LLMs). Each markdown file in `docs/` summarizes a known or theorized vector, linking to the original research or incident report.

The catalog is maintained for researchers and defenders who need a single reference point for adversarial methods ranging from classic prompt injection to training data poisoning.

New additions cover emerging *reinforcement-learning alignment attacks* such as [Reverse Preference Attack](docs/training-alignment/reinforcement-learning-alignment-attacks.md) and Anthropic's "Sleeper Agents." See the `training-alignment` folder for details.

## Using This Repository

- The **canonical files** reside under `docs/` and use kebab‑case names.
- Each file may include YAML front matter describing the source, category, and license.
- A compiled PDF version is provided for offline viewing.

## Contributing

Contributions are welcome! Please review [CONTRIBUTING.md](CONTRIBUTING.md) for coding style and front‑matter guidelines. All content must respect the project license and third‑party terms.

## License

All original content is licensed under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) license. Third‑party excerpts remain under their respective licenses.
