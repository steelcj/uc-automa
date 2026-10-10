---
title: "Decision: kind and from_offering"
dc:title: "Decision: kind and from_offering"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "kind, from_offering, offerings, layouts, D14"
dc:description: "kind (meta, runs, read, lives) is a uc-automa concept naming which of the station's homes a path belongs to; in receiving repositories, files that arrive from an offering are marked from_offering instead."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:6700f268-2794-454c-bea7-440786cb4595"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
sat:decision: "D14"
---

# Decision: kind and from_offering

Version: 0.1.0
Status: Accepted

## Context

kind had two meanings: in uc-automa, which home a path belongs to; in a receiving repository, that a file arrived from uc-automa. The decision was worked out with Christopher Steel on 2026-10-07 and 2026-10-09 and recorded in the foundation brief <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b).

## Decision

- `kind` is one of `meta`, `runs`, `read` and `lives`, and describes which of the station's homes a path in uc-automa belongs to. Only `uc-automa.yaml` sets it.
- In the shared layouts, a path that arrives from an offering is marked `from_offering: <offering-id>`.
- The layout check reports an error when a path marked `from_offering: X` is present or required and the repository does not subscribe to `X`.

## Consequences

- Each term has one meaning.
- `init` derives a new repository's subscriptions from the `from_offering` marks on the paths its layout requires (uc-automa 0023).

## References

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Brief: uc-automa foundation* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96 [↩](#cite-steel-2026b)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: kind and from_offering*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
