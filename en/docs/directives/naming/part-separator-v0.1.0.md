---
title: "Naming: Part Separator"
dc:title: "Naming: Part Separator"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "naming, part separator, hyphens, D10"
dc:description: "A double hyphen separates the parts of a name, such as a number or date from a title; a single hyphen joins words within a part; no part is empty and no hyphen sits at either end."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:a8c9606d-8483-4dc8-beba-add335e14de1"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "In force"
sat:directive: "naming/part-separator"
sat:enforced_by:
  - "conformance.naming.part_separator"
---

# Naming: Part Separator

Version: 0.1.0
Status: In force

## Rule

A name's stem, the name without a leading dot, a version suffix or an extension, is made of parts joined by `--`. Within a part, words are joined by a single `-`. No part is empty, and the stem neither starts nor ends with a hyphen.

Inside uc-automa a directory names the domain, so a domain is never repeated as a name part: `directives/naming/part-separator-v0.1.0.md`, not `directives/naming/naming--part-separator-v0.1.0.md`.

## Rationale

This is decision D10, recorded as uc-automa 0010: it is Christopher Steel's own convention, and it lets a reader and a tool split a name into its parts without guessing.

## Examples

| Name | Verdict |
| --- | --- |
| `2026-10-09--uc-automa-foundation-v0.1.0.md` | Conforms: a date part and a title part |
| `0001--licensing-for-code-documentation-and-content-v0.1.0.md` | Conforms: a number part and a title part |
| `2026-10-09---foundation.md` | Three hyphens |
| `-draft.md` | Leading hyphen |

## Check

`conformance.naming.part_separator` checks the stem of every lowercase name. Uppercase, tool-mandated and Python names follow their own rules and are skipped. Its fixtures are under `tests/fixtures/conformance/naming/part-separator/`.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | In force | Initial version |

## License

This document, *Naming: Part Separator*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
