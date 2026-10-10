# Contributing

Changes arrive as commits on a branch and are reviewed by Christopher Steel before they reach `main`. Drafts stay on branches; `main` holds only what is in force.

## Before committing

- Run `python3 -m unittest discover -s tests` and `uc-automa check`; both pass.
- A new or changed rule is a directive, one rule per file, naming the check that enforces it, or saying it has none. A check has pass and fail fixtures under `tests/fixtures/conformance/{domain}/{slug}/`.
- A choice that shapes how every repository works is a decision record, numbered globally in `en-ca/docs/decisions/`.
- Changing a layout under `conf/layouts/` changes its words under `en-ca/conf/layouts/` in the same commit; `uc-automa translations` reports nothing untranslated or stale.
- Regenerate the documentation index with `uc-automa docs index`; never edit it by hand.

## Harvested changes

When a receiving repository improves a file that came from an offering, `uc-automa offerings harvest` reports it there. The change is proposed here as an ordinary commit to the offering's payload, reviewed like any other.

## License

This document, *Contributing*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
