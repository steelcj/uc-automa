---
title: "Decision: Offerings for Pinned Repositories"
dc:title: "Decision: Offerings for Pinned Repositories"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "offerings, automa_version, pinning, package data, self"
dc:description: "A repository pinned to a uc-automa release takes the offerings shipped in the installed package; below 1.0.0 the pin must equal the installed version exactly; automa_version: self is valid only in uc-automa itself."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:5e2fcdd7-2a46-4f0f-ba6f-92b6a0ec18e0"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: Offerings for Pinned Repositories

Version: 0.1.0
Status: Accepted

## Context

A repository pins `automa_version` in its `.uc-automa.yaml`. `uc-automa offerings` must find the offerings of that version to hand to uc-portage, offline if possible.

## Decision

- `offerings/` is mapped into the uc-automa package by the same mechanism as its other data (uc-automa 0019), so an installed uc-automa carries the offerings of its own version and works offline.
- The pin must equal the installed version exactly. Below 1.0.0 the offering format may change between minor versions, so nothing looser is safe. A compatibility range can be reconsidered at 1.0.0.
- When they differ, the error names both versions and the two fixes: install the pinned version, or update the pin.
- `automa_version: self` makes a repository take its own `offerings/`. It is valid only in uc-automa itself; anywhere else it is an error. A repository is uc-automa when its `pyproject.toml` names the uc-automa project, the same test the data resolver uses.

## Consequences

- One installed uc-automa serves the repositories pinned to its version. Running several uc-automa versions side by side is future work for an OSAT manager, not for uc-automa itself.
- The layouts the check uses come from the same place as the offerings, so a check and an apply always agree on the version.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: Offerings for Pinned Repositories*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
