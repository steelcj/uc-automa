---
title: "Layout: Layout Translations"
dc:title: "Layout: Layout Translations"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "layout, translations, en-ca, source_hash, D12"
dc:description: "Each layout's words describe exactly the paths and placeholders that layout adds; the source language describes all of them, and every translated entry carries the source_hash of the text it translates."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:f5c53be4-4e35-43d8-9e3f-704e37ba9f4f"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "In force"
sat:directive: "layout/layout-translations"
sat:enforced_by:
  - "conformance.layout.translations"
---

# Layout: Layout Translations

Version: 0.1.0
Status: In force

## Rule

Structure lives once, with no prose, under `conf/layouts/`. Words live at the same relative path under each language root, such as `en-ca/conf/layouts/` (uc-automa 0012). For each layout file:

- its words describe only the paths and placeholders that layout adds; inherited paths keep the words of the layout that adds them;
- the source language, `en-ca`, describes every one of them;
- another language may leave some untranslated, which `uc-automa translations` reports and which is not an error;
- every translated entry records `source_hash`, the first twelve hexadecimal digits of the SHA-256 of the source text, and an entry whose hash no longer matches is stale.

Paths are identifiers and are never translated.

## Rationale

Splitting structure from words lets layouts be translated without a second copy of the tree drifting from the first, and the hash makes a stale translation detectable rather than silently wrong.

## Examples

| Words file | Verdict |
| --- | --- |
| `en-ca/conf/layouts/python-tool.yaml` describing `pyproject.toml` | Conforms: python-tool adds it |
| `en-ca/conf/layouts/uc-automa.yaml` describing `README.md` | Describes an inherited path |
| `fr-ca/conf/layouts/base.yaml` with an old `source_hash` | Stale |

## Check

`conformance.layout.translations` runs per layout file, in uc-automa itself, which is where layouts live. Its fixtures are under `tests/fixtures/conformance/layout/layout-translations/`.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | In force | Initial version |

## License

This document, *Layout: Layout Translations*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
