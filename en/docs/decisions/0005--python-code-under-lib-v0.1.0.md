---
title: "Decision: Python Code under lib"
dc:title: "Decision: Python Code under lib"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "Python, lib, src, layout, D4"
dc:description: "Python code lives under lib/, as lib/<package>/."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:0d933062-9129-4bea-b002-21c50f3174a3"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
sat:decision: "D4"
---

# Decision: Python Code under lib

Version: 0.1.0
Status: Accepted

## Context

A Python package can live under src/ or lib/. satx keeps its language-neutral bin/ and lib/. The decision was worked out with Christopher Steel on 2026-10-07 and 2026-10-09 and recorded in the foundation brief <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b).

## Decision

Python code lives under `lib/`, as `lib/<package>/`, for parity with satx.

## Consequences

- The `python-tool` layout requires `lib/{package}/`.
- The data resolver relies on this depth: in a checkout, the package sits two levels below the repository root (uc-automa 0019). Changing this decision means changing the resolver.

## References

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Brief: uc-automa foundation* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96 [↩](#cite-steel-2026b)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: Python Code under lib*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
