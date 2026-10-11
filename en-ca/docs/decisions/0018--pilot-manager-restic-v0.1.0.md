---
title: "Decision: Pilot Manager restic"
dc:title: "Decision: Pilot Manager restic"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "OSAT manager, restic, pilot, D18"
dc:description: "The pilot OSAT manager is restic, as osat-manager-restic, succeeding osat-fluent-restic-tool."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:d23f6735-0dc3-4a96-ac2d-f1ce7b22aea3"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
sat:decision: "D18"
---

# Decision: Pilot Manager restic

Version: 0.1.0
Status: Accepted

## Context

The osat-manager process needed a first repository built entirely by the new approach, to test both the tooling and the process itself. The decision was worked out with Christopher Steel on 2026-10-07 and 2026-10-09 and recorded in the foundation brief <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b).

## Decision

The pilot manager is restic, as `osat-manager-restic`, succeeding osat-fluent-restic-tool. restic is a single binary, published for all three platforms with checksums, fits the Resilience Pack, and exercises retiring a predecessor.

## Consequences

- osat-manager-restic is built third, after uc-portage and uc-automa, following the OSAT manager process stage by stage.
- osat-fluent-restic-tool is read for lessons only, and archived later by Christopher Steel with a notice naming its successor.

## References

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Brief: uc-automa foundation* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96 [↩](#cite-steel-2026b)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: Pilot Manager restic*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
