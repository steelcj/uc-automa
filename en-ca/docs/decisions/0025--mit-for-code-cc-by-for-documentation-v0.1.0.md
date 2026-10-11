---
title: "Decision: MIT for Code, CC BY 4.0 for Documentation"
dc:title: "Decision: MIT for Code, CC BY 4.0 for Documentation"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "licensing, MIT, CC-BY-4.0, REUSE, LICENSE, LIC-0001"
dc:description: "Code is licensed MIT and documentation and content CC BY 4.0, carrying out LIC-0001; the root LICENSE holds the MIT text, byte-identical to LICENSES/MIT.txt and delivered from one payload. Supersedes uc-automa 0001 and 0021."
dc:date: "2026-10-11"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:d064e909-8760-46b3-b149-019c3d695a4d"
dc:relation:
  - "urn:uuid:14f3cf06-ab5d-454e-8c00-d81c36a21d08"
  - "urn:uuid:5b82dabb-3e67-4f11-a944-4018ae4e1dcf"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: MIT for Code, CC BY 4.0 for Documentation

Version: 0.1.0
Status: Accepted

## Context

uc-automa 0001 licensed code GPL-3.0-or-later, documentation CC-BY-SA-4.0 and content CC-BY-4.0, and uc-automa 0021 kept a root `LICENSE` holding the code licence. Before uc-portage, uc-automa and osat-manager-restic were first published, Christopher Steel decided, as LIC-0001 in the practice's decision records, that Universal Cake's code is licensed MIT and its content CC BY 4.0, from the next version. None of the three repositories had been published, so their first public release, 0.1.0, is the first under the new licences.

## Decision

- Code is licensed under the MIT License, SPDX identifier `MIT`.
- Documentation and content are licensed under Creative Commons Attribution 4.0 International, `CC-BY-4.0`. There is no longer a separate share-alike licence for documentation.
- Licences are still marked with REUSE: `LICENSES/MIT.txt` and `LICENSES/CC-BY-4.0.txt`, `REUSE.toml` by path, and a per-file SPDX identifier only where a file differs. A document's `dc:rights` matches the licence that covers it.
- Every repository keeps a root `LICENSE`, holding the MIT text, byte-identical to `LICENSES/MIT.txt`. The MIT text carries its copyright line filled in, `Copyright (c) 2026 Christopher Steel`, in both, so both come from one payload, the `license-mit` offering.
- Contributions are accepted under the same licences: inbound equals outbound.
- The `license-gpl-3-0-or-later` and `license-cc-by-sa-4-0` offerings are withdrawn; `license-mit` and `license-cc-by-4-0` take their place, and the base layout requires both.

## Consequences

- uc-automa 0001 and 0021 are superseded; they stay as the record of the earlier decision.
- The three repositories' commit histories, before their first public release, contain work marked GPL-3.0-or-later and CC-BY-SA-4.0, all by Christopher Steel as sole author. Releases are MIT and CC BY 4.0 from 0.1.0.
- Marking the Universal Cake name and logo as excluded from the licences waits for the trademark policy to be published.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-11 | Accepted | Initial version |

## License

This document, *Decision: MIT for Code, CC BY 4.0 for Documentation*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
