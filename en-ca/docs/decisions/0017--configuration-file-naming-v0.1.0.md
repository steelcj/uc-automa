---
title: "Decision: Configuration File Naming"
dc:title: "Decision: Configuration File Naming"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "configuration, naming, yaml, D17"
dc:description: "Configuration files are named for their subject inside a directory that names the domain, use .yaml, and carry no version in the filename."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:bbf74cc7-7cb3-40a1-aeb4-863c63264871"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
sat:decision: "D17"
---

# Decision: Configuration File Naming

Version: 0.1.0
Status: Accepted

## Context

Configuration files had been named with their domain repeated and sometimes with a version, such as uc-automa--file-system-layout-v0.2.0.yaml. The decision was worked out with Christopher Steel on 2026-10-07 and 2026-10-09 and recorded in the foundation brief <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b).

## Decision

A configuration file is named for its subject inside a directory that names its domain, uses `.yaml`, and carries no version in its filename, because the repository's release versions it: `conf/layouts/osat-manager.yaml`, not `conf/uc-automa--osat-manager-layout-v0.1.0.yaml`.

## Consequences

- Versions in filenames are for documents only (uc-automa 0002).
- New YAML files use `.yaml`, never `.yml`.

## References

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Brief: uc-automa foundation* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96 [↩](#cite-steel-2026b)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: Configuration File Naming*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
