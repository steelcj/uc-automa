---
title: "Decision: Three Platforms for 1.0.0"
dc:title: "Decision: Three Platforms for 1.0.0"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "release, 1.0.0, Linux, macOS, Windows, platforms, D11"
dc:description: "A tool reaches 1.0.0 only when it is verified end to end on Linux, macOS and Windows; releases already at 1.0 or later are not affected retroactively."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:cc8bd92f-4dcf-4263-8c8e-a62395dbc1a4"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
sat:decision: "D11"
---

# Decision: Three Platforms for 1.0.0

Version: 0.1.0
Status: Accepted

## Context

manage-python reached 1.0 with Windows and macOS unverified. Cross-platform support was stated as a goal but not enforced. The decision was worked out with Christopher Steel on 2026-10-07 and 2026-10-09 and recorded in the foundation brief <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b).

## Decision

A tool reaches 1.0.0 only when it is verified end to end on Linux, macOS and Windows. A platform is verified by running the end-to-end scenario on it; it is never assumed. Releases already at 1.0 or later are not affected retroactively.

## Consequences

- uc-portage, uc-automa and osat-manager-restic stay below 1.0.0 until all three platforms are verified.
- Every tool's README carries a platform status table stating what was actually run.

## References

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Brief: uc-automa foundation* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96 [↩](#cite-steel-2026b)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: Three Platforms for 1.0.0*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
