---
title: "Decision: Pull Model for Offerings"
dc:title: "Decision: Pull Model for Offerings"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "pull model, subscriptions, offerings, .uc-automa.yaml, D8"
dc:description: "Each receiving repository declares its subscriptions and its layout in its own .uc-automa.yaml; uc-automa holds no per-repository manifests."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:91e864a2-fb2a-4e56-8591-60e36720111a"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
sat:decision: "D8"
---

# Decision: Pull Model for Offerings

Version: 0.1.0
Status: Accepted

## Context

file-fairy's manifests lived in sat-doc-automa, one per receiving repository, so adding a repository meant changing the source. The decision was worked out with Christopher Steel on 2026-10-07 and 2026-10-09 and recorded in the foundation brief <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b). The recommendations that informed it are recorded separately <a id="cite-steel-2026r"></a>[(Steel, 2026r)](#ref-steel-2026r).

## Decision

Each receiving repository declares what it is and what it takes, in its own `.uc-automa.yaml`. uc-automa publishes offerings and holds no per-repository manifests.

## Consequences

- Adding a repository never requires a change to uc-automa.
- uc-automa subscribes to its own offerings, so every offering is exercised before any other repository receives it.

## References

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Brief: uc-automa foundation* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96 [↩](#cite-steel-2026b)

<a id="ref-steel-2026r"></a>Steel, C. (2026r). *Automa access: Recommendations by kind of material* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:0c17465b-3298-408e-9ae7-715a2019a960 [↩](#cite-steel-2026r)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: Pull Model for Offerings*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
