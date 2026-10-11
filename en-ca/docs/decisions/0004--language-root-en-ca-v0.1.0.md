---
title: "Decision: Language Root en-ca"
dc:title: "Decision: Language Root en-ca"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "language, en-ca, en-CA, D3"
dc:description: "The language root is en-ca/, lowercase, and metadata uses en-CA; Canadian English is the source language."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:d12ace49-1a49-4acb-b67e-6fe23d9e0bf2"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
sat:decision: "D3"
---

# Decision: Language Root en-ca

Version: 0.1.0
Status: Accepted

## Context

Earlier repositories used en/ as the language root. Balise already uses fr-ca/ for its French tree. The decision was worked out with Christopher Steel on 2026-10-07 and 2026-10-09 and recorded in the foundation brief <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b).

## Decision

The language root is `en-ca/`, lowercase, matching Balise's `fr-ca/`. Metadata uses the standard form, `en-CA`. Canadian English is the source language, and the fallback when a translation is missing.

## Consequences

- `docs_root` is `en-ca/docs` in every repository (uc-automa 0007).
- The front matter check requires `dc:language` to match the document's language root.

## References

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Brief: uc-automa foundation* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96 [↩](#cite-steel-2026b)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: Language Root en-ca*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
