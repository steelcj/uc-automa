---
title: "Decision: Configuration Split by Language"
dc:title: "Decision: Configuration Split by Language"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "configuration, translation, conf, en-ca, source_hash, D12"
dc:description: "Configuration structure lives once, with no prose, under conf/; its words live at the same relative path under each language root; translations record a source_hash."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:d59197d3-557f-44a6-a294-c17eb47354bb"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
sat:decision: "D12"
---

# Decision: Configuration Split by Language

Version: 0.1.0
Status: Accepted

## Context

A layout mixes structure, the paths, with words, what each path holds. Translating it by copying the whole file would leave two trees that drift apart. The decision was worked out with Christopher Steel on 2026-10-07 and 2026-10-09 and recorded in the foundation brief <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b).

## Decision

- Structure lives once, with no prose, under `conf/`.
- Words live at the same relative path under each language root, such as `en-ca/conf/`.
- Paths are identifiers and are never translated.
- A language file may only describe paths the structure defines.
- `en-ca` is the source language and the fallback.
- Each translated string records a `source_hash` of the source text, so stale translations are detectable.

## Consequences

- The directive `layout/layout-translations` and its check enforce this per layout file.
- With layouts split by type (uc-automa 0013), each words file describes only the paths its own layout adds.

## References

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Brief: uc-automa foundation* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96 [↩](#cite-steel-2026b)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: Configuration Split by Language*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
