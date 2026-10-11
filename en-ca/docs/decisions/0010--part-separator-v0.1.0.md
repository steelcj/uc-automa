---
title: "Decision: Part Separator"
dc:title: "Decision: Part Separator"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "naming, part separator, hyphens, D10"
dc:description: "A double hyphen separates the parts of a name, such as a date from a title; a single hyphen joins words within a part."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:567781eb-1709-4cb7-9c2c-21c6c9f962ed"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
sat:decision: "D10"
---

# Decision: Part Separator

Version: 0.1.0
Status: Accepted

## Context

Names such as 2026-10-09--uc-automa-foundation combine parts of different kinds. Christopher Steel's own convention separates them with a double hyphen. The decision was worked out with Christopher Steel on 2026-10-07 and 2026-10-09 and recorded in the foundation brief <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b).

## Decision

`--` separates the parts of a name; `-` joins words within a part. Decision records are named `{number}--{slug}{version}.md`, with the number as its own part.

## Consequences

- The directive `naming/part-separator` states the rule and its check enforces it.
- The layout draft's `{number}-{slug}` form for decision records is replaced by `{number}--{slug}`, as Christopher Steel ruled on 2026-10-09.

## References

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Brief: uc-automa foundation* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96 [↩](#cite-steel-2026b)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: Part Separator*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
