---
title: "Decision: Documentation under en-ca/docs"
dc:title: "Decision: Documentation under en-ca/docs"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "documentation, docs_root, en-ca, D7"
dc:description: "Documentation lives at en-ca/docs/, so docs_root is the same in every repository."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:e8cac7fd-1300-4b8e-bb35-a8cadc41c6a5"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
sat:decision: "D7"
---

# Decision: Documentation under en-ca/docs

Version: 0.1.0
Status: Accepted

## Context

The documentation tree could sit directly under the language root or one level down, under docs/. The decision was worked out with Christopher Steel on 2026-10-07 and 2026-10-09 and recorded in the foundation brief <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b).

## Decision

Documentation lives at `{language}/docs/`, which is `en-ca/docs/` for the source language, in every repository.

## Consequences

- A tool or a person finds a repository's documentation without reading its configuration.
- The language root has room for siblings, such as `en-ca/conf/` for layout words and `en-ca/templates/` for authoring skeletons.

## References

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Brief: uc-automa foundation* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96 [↩](#cite-steel-2026b)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: Documentation under en-ca/docs*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
