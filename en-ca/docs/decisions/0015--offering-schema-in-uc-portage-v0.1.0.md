---
title: "Decision: Offering Schema in uc-portage"
dc:title: "Decision: Offering Schema in uc-portage"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "offering schema, uc-portage, contracts, D15"
dc:description: "offering.schema.yaml lives in uc-portage, which reads offerings; uc-automa uses it and keeps no copy."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:3999c8a7-d425-4e4f-97f3-1e385763b92e"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
sat:decision: "D15"
---

# Decision: Offering Schema in uc-portage

Version: 0.1.0
Status: Accepted

## Context

The first layout draft listed offering.schema.yaml among uc-automa's schemas, although uc-portage is the tool that reads offerings. The decision was worked out with Christopher Steel on 2026-10-07 and 2026-10-09 and recorded in the foundation brief <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b).

## Decision

The tool that reads a format owns its contract. `offering.schema.yaml` lives in uc-portage, under `schemas/`. uc-automa validates its offerings through uc-portage and keeps no copy, since nothing is stored in two places.

## Consequences

- uc-automa's layout requires only its own schemas: `uc-automa-config.schema.yaml` and `front-matter.schema.yaml`.
- uc-automa validates its own schemas with uc-portage's validator, so the supported subset of JSON Schema is defined once.

## References

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Brief: uc-automa foundation* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96 [↩](#cite-steel-2026b)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: Offering Schema in uc-portage*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
