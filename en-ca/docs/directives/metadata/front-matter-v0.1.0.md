---
title: "Metadata: Front Matter"
dc:title: "Metadata: Front Matter"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "metadata, front matter, Dublin Core, sat:, directives, schemas"
dc:description: "Every document under a language's docs/ carries the front matter its type requires in schemas/front-matter.schema.yaml, with dc:language matching its language root and, for a directive, its own identifier and real checks."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:f834eafb-4b92-4bc2-a466-d014baf2f8fa"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "In force"
sat:directive: "metadata/front-matter"
sat:enforced_by:
  - "conformance.metadata.front_matter"
---

# Metadata: Front Matter

Version: 0.1.0
Status: In force

## Rule

A document under `{language}/docs/` carries YAML front matter matching its type's definition in `schemas/front-matter.schema.yaml`. The type is chosen by the directory: `directives/`, `guides/`, `decisions/`, `references/` or `sessions/`.

- Every type carries `title`, `dc:title`, `dc:creator`, `dc:description`, `dc:date`, `dc:type`, `dc:format`, `dc:identifier` as a `urn:uuid:` value generated with `uuidgen -r`, `dc:language`, `dc:rights`, `sat:version` and `sat:status`.
- `dc:language` matches the language root: `en-CA` under `en-ca/`.
- A migrated document keeps its identifier and gains `dc:source`, naming its old path and commit.
- A directive's `sat:directive` is its own identifier, `{domain}/{slug}`, and `sat:enforced_by` names the checks that enforce it, or is empty when the rule has no check. In uc-automa, every check is named by exactly the directive it enforces.

## Rationale

Front matter is where a document's state lives (P2): its identity, version, status and licence. Rules are traceable only if each directive names its check and each check names its directive (P9).

## Check

`conformance.metadata.front_matter` validates each document against its type's definition, checks its language and, for directives, its identifier and checks. Its fixtures are under `tests/fixtures/conformance/metadata/front-matter/`.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | In force | Initial version |

## License

This document, *Metadata: Front Matter*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
