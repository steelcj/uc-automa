---
title: "Decision: uc-portage as a Separate Tool"
dc:title: "Decision: uc-portage as a Separate Tool"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "uc-portage, file-fairy, offerings, engine, D5"
dc:description: "The offering engine is a separate, generic tool, uc-portage, built from file-fairy's engine; file-fairy is archived later with a notice naming its successor."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:624d902f-2e40-457e-ad84-03ecf47c5c64"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
sat:decision: "D5"
---

# Decision: uc-portage as a Separate Tool

Version: 0.1.0
Status: Accepted

## Context

file-fairy carried shared files between repositories with a plan, apply and status cycle and checksum-based drift tracking. The question was whether its engine should merge into the automa package or stay a tool of its own. The decision was worked out with Christopher Steel on 2026-10-07 and 2026-10-09 and recorded in the foundation brief <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b). The recommendations that informed it are recorded separately <a id="cite-steel-2026r"></a>[(Steel, 2026r)](#ref-steel-2026r); their placeholder names are superseded.

## Decision

The engine stays a separate, generic tool named uc-portage, which uc-automa depends on. uc-automa keeps to rules and offerings; uc-portage knows nothing of uc-automa and stays useful outside Vishpala. A portage is the carry between two waters, in either direction, and the word is the same in French and English.

file-fairy is archived later, by Christopher Steel, with a README notice naming its successor.

## Consequences

- uc-portage is built first, because uc-automa depends on it.
- The format uc-portage reads, `offering.schema.yaml`, lives in uc-portage (uc-automa 0015).

## References

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Brief: uc-automa foundation* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96 [↩](#cite-steel-2026b)

<a id="ref-steel-2026r"></a>Steel, C. (2026r). *Automa access: Recommendations by kind of material* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:0c17465b-3298-408e-9ae7-715a2019a960 [↩](#cite-steel-2026r)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: uc-portage as a Separate Tool*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
