---
title: "Licensing: Rights Match REUSE"
dc:title: "Licensing: Rights Match REUSE"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "licensing, REUSE, SPDX, dc:rights, D6"
dc:description: "A document's dc:rights names the SPDX identifier that REUSE.toml, or the file's own SPDX line, says covers it."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:436a2aa2-2cad-4973-a359-f93f3a737c8a"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "In force"
sat:directive: "licensing/rights-match-reuse"
sat:enforced_by:
  - "conformance.licensing.rights_match_reuse"
---

# Licensing: Rights Match REUSE

Version: 0.1.0
Status: In force

## Rule

`REUSE.toml` is the canonical record of which licence covers which path. A file that differs from its path's default carries its own `SPDX-License-Identifier` line, which takes precedence. A document's `dc:rights` names exactly the SPDX identifier that covers it. When several annotations in `REUSE.toml` match one path, the last one wins.

## Rationale

Licences are set by category: code GPL-3.0-or-later, documentation CC-BY-SA-4.0, content CC-BY-4.0 (uc-automa 0001). Front matter that disagrees with the licence record misleads anyone who reuses the document.

## Examples

| Path | REUSE.toml | dc:rights | Verdict |
| --- | --- | --- | --- |
| `en-ca/docs/guides/x/y-v0.1.0.md` | `en-ca/**` is CC-BY-SA-4.0 | `CC-BY-SA-4.0` | Conforms |
| the same | the same | `AGPL-3.0-or-later` | Does not match |

## Check

`conformance.licensing.rights_match_reuse` reads each `[[annotations]]` table's `path` and `SPDX-License-Identifier` from `REUSE.toml`, and compares them with every Markdown document's `dc:rights`. Its fixtures are under `tests/fixtures/conformance/licensing/rights-match-reuse/`.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | In force | Initial version |

## License

This document, *Licensing: Rights Match REUSE*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
