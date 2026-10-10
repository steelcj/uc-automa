---
title: "Naming: Versions in Filenames"
dc:title: "Naming: Versions in Filenames"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "naming, versions, filenames, D1"
dc:description: "Before 1.0.0 a versioned document's filename ends in -vX.Y.Z with dots, matching its sat:version; from 1.0.0 the filename carries no version; the hyphenated form -vX-Y-Z is never used."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:da71b33c-cd19-4a36-bdcb-cba940739632"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "In force"
sat:directive: "naming/versions-in-filenames"
sat:enforced_by:
  - "conformance.naming.versions_in_filenames"
---

# Naming: Versions in Filenames

Version: 0.1.0
Status: In force

## Rule

A versioned document is one under a language's `docs/` whose front matter carries `sat:version`. Templates, schemas, configuration, licence texts and code are versioned by the repository's release and carry no version in their names.

- Below 1.0.0, its filename ends in `-v` and its version with dots, before the extension, and that version equals `sat:version`: `directory-guide-v0.2.0.md` holds `sat:version: "0.2.0"`.
- From 1.0.0, its filename carries no version: `directory-guide.md`. The version lives in front matter, the Changelog table and git tags.
- No filename anywhere uses the hyphenated form, such as `-v0-2-0`.

A version bump renames the file with `git mv` and updates links to it in the same commit. Tools find the version with the pattern `-v(\d+)\.(\d+)\.(\d+)` immediately before the extension, never by splitting the name on dots.

## Rationale

This is decision D1, recorded as uc-automa 0002. The hyphenated form came from an earlier assumption and has had to be corrected several times; the check makes the correction permanent.

## Examples

| Filename | Front matter | Verdict |
| --- | --- | --- |
| `0001--licensing-v0.1.0.md` | `sat:version: "0.1.0"` | Conforms |
| `0001--licensing.md` | `sat:version: "0.1.0"` | Missing suffix below 1.0.0 |
| `0001--licensing-v0.1.0.md` | `sat:version: "0.2.0"` | Suffix does not match |
| `guide-v1.0.0.md` | `sat:version: "1.0.0"` | Version in the filename from 1.0.0 |
| `guide-v0-1-0.md` | any | Hyphenated version |

## Check

`conformance.naming.versions_in_filenames` reports any hyphenated version in any name, and compares every Markdown document's filename with its `sat:version`. The layout check accepts a decision record without a suffix, because `{version}` is optional in the layout to allow for 1.0.0 and later; this check catches the record that is still below 1.0.0. Its fixtures are under `tests/fixtures/conformance/naming/versions-in-filenames/`, including that exact case.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | In force | Initial version |

## License

This document, *Naming: Versions in Filenames*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
