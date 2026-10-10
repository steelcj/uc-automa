---
title: "Naming: SPDX Slugs"
dc:title: "Naming: SPDX Slugs"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "naming, SPDX, slugs, license, licence, offerings"
dc:description: "Identifiers follow the spelling of the standard they name, license as in SPDX and REUSE; an SPDX slug is the identifier lowercased, every other character a hyphen, repeats collapsed; a slug never contains a dot."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:427f6f92-63e1-48ba-a80a-815257467f0a"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "In force"
sat:directive: "naming/spdx-slugs"
sat:enforced_by:
  - "conformance.naming.spdx_slugs"
---

# Naming: SPDX Slugs

Version: 0.1.0
Status: In force

## Rule

- Identifiers follow the spelling of the standard they name: `license`, as in SPDX and REUSE. Prose follows Canadian English: `licence` as the noun.
- An SPDX slug is the SPDX identifier lowercased, with every character other than `a` to `z` and `0` to `9` replaced by a hyphen, and repeated hyphens collapsed into one: `GPL-3.0-or-later` becomes `gpl-3-0-or-later`.
- A slug never contains a dot. This differs from version suffixes deliberately: dots appear only inside a `-vX.Y.Z` suffix and before an extension.
- A licence offering is named `license-` and the slug of the one licence text it delivers from `LICENSES/`.

## Rationale

Written down so that it is never inferred again: the offering names had no rule until the foundation build, and two spellings and several slug shapes were possible.

## Examples

| SPDX identifier | Offering |
| --- | --- |
| `GPL-3.0-or-later` | `license-gpl-3-0-or-later` |
| `CC-BY-SA-4.0` | `license-cc-by-sa-4-0` |
| `CC-BY-4.0` | `license-cc-by-4-0` |

## Check

`conformance.naming.spdx_slugs` checks every offering under `offerings/`: none is spelled `licence`, and each `license-` offering delivers exactly one licence text whose slug matches its name. Its fixtures are under `tests/fixtures/conformance/naming/spdx-slugs/`.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | In force | Initial version |

## License

This document, *Naming: SPDX Slugs*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
