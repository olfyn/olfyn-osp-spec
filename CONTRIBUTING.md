# Contributing to OSP

Thank you for your interest in the Open Scent Protocol. OSP is an early draft, so feedback on the specification is just as valuable as code.

## Ways to help

| You are… | You could… |
|---|---|
| Anyone | Point out anything unclear, inconsistent or missing in the spec |
| Backend developer | Build a reference OSP server (REST + WebSocket, section 5 of the spec) |
| Embedded / hardware maker | Build the reference hardware or device firmware, and share your notes |
| Chemist, perfumer, sommelier | Propose predefined profiles with their sources, or challenge the 10 dimensions |
| Researcher | Share evidence on scent perception, reproduction or capture |

## Before you start

- **Search the issues** to see if someone has already raised the same thing.
- **For a change to the protocol**, open an issue with the *Spec proposal* template first. Changes to the protocol follow the process in the spec (section 12): proposal, 30-day community review, then inclusion in the next MINOR or MAJOR version.
- **For typos and small clarifications**, a pull request on its own is fine.

## Pull requests

1. Fork the repository and create a branch from `main`.
2. Keep each pull request focused on one change.
3. If you change a profile example or the schema, run the validator:
   ```bash
   pip install "jsonschema[format]"
   python tools/validate.py examples/EXAMPLES.md README.md
   ```
4. If your change affects the protocol, add an entry under **Unreleased** in [CHANGELOG.md](CHANGELOG.md).
5. Describe what you changed and why.

## Specification conventions

- The spec, schema and examples are written in **English**. The 10 dimension keys stay in Spanish because they are part of the wire format.
- Versions follow [Semantic Versioning](https://semver.org/): a breaking change needs a new MAJOR version.
- Previous versions live under `versions/` and are not edited, except to fix broken links.

## Health-related contributions

OSP makes no therapeutic or clinical claims. Contributions must not describe a profile or session as a treatment or as clinically validated unless they cite published evidence, and even then OSP itself remains a data format, not a medical device.

## License

By contributing, you agree that your contributions are licensed under the [MIT License](LICENSE).

## Code of Conduct

Everyone taking part in this project follows our [Code of Conduct](CODE_OF_CONDUCT.md).
