---
title: "Naming: Portable Names"
dc:title: "Naming: Portable Names"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "naming, Windows, macOS, portability, case collisions, path length"
dc:description: "Names clone and work identically on Linux, macOS and Windows: no Windows reserved names, no forbidden characters, no trailing dot or space, no two names differing only by case, and paths of at most 100 characters."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:56e38e86-f78e-4f33-94c3-27b9be24b883"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "In force"
sat:directive: "naming/portable-names"
sat:enforced_by:
  - "conformance.naming.portable_names"
---

# Naming: Portable Names

Version: 0.1.0
Status: In force

## Rule

A name must work on Linux, macOS and Windows:

- no Windows reserved name, with or without an extension: `CON`, `PRN`, `AUX`, `NUL`, `COM1` to `COM9` and `LPT1` to `LPT9`;
- none of the characters `< > : " \ | ? *`;
- no trailing dot or space, no space anywhere and no character outside ASCII;
- no two names in one directory that differ only by case;
- no path longer than 100 characters from the repository root, which leaves room under the Windows limit of 260 for deep clone locations.

## Rationale

A tool reaches 1.0.0 only when it is verified on all three platforms (uc-automa 0011). A name that one platform cannot hold breaks the clone before any code runs.

## Examples

| Path | Verdict |
| --- | --- |
| `en-ca/docs/guides/usage/using-uc-portage-v0.1.0.md` | Conforms |
| `docs/aux.md` | Reserved on Windows |
| `README.md` beside `readme.md` | Differ only by case |

## Check

`conformance.naming.portable_names` checks every path the repository contains, except the conformance fixtures. Its fixtures are under `tests/fixtures/conformance/naming/portable-names/`.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | In force | Initial version |

## License

This document, *Naming: Portable Names*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
