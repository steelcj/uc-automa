---
title: "Decision: Root Licence File"
dc:title: "Decision: Root Licence File"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "licensing, LICENSE, LICENSES, REUSE, L1"
dc:description: "Every repository keeps a root LICENSE file holding the code licence, byte-identical to LICENSES/GPL-3.0-or-later.txt and delivered from the same payload."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:5b82dabb-3e67-4f11-a944-4018ae4e1dcf"
dc:relation: "urn:uuid:14f3cf06-ab5d-454e-8c00-d81c36a21d08"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
sat:decision: "L1"
---

# Decision: Root Licence File

Version: 0.1.0
Status: Accepted

## Context

REUSE keeps licence texts in `LICENSES/`, while forges look for a root `LICENSE` file to show a repository's licence. The licensing decision (uc-automa 0001) left open whether to keep one, as L1. The texts first came from two sources with different formatting: the SPDX licence list and the Free Software Foundation's copy.

## Decision

Keep a root `LICENSE` file, holding the code licence, GPL-3.0-or-later. It is byte-identical to `LICENSES/GPL-3.0-or-later.txt`, and both use the SPDX text, which is what `reuse download` produces and what `reuse lint` expects. The `license-gpl-3-0-or-later` offering delivers both from one payload file.

## Consequences

- The base layout requires `LICENSE`, marked as arriving from `license-gpl-3-0-or-later`.
- One licence text has one source.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: Root Licence File*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
