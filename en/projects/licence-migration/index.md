---
title: "Universal Cake licence migration"
description: "Project to move every Universal Cake component from AGPL-3.0-or-later to MIT for code and to CC BY 4.0 for content with the next version, carrying out LIC-0001."
date: 2026-10-10
lang: en-CA
tags:
  - licensing
  - project
  - checklist
dc:
  identifier: "urn:uuid:a47703aa-7797-436e-97e9-39ef82ed69f5"
  title: "Universal Cake licence migration"
  creator: "Christopher Steel"
  publisher: "Vishpala"
  date: 2026-10-10
  language: en-CA
  type: Text
  format: text/markdown
  rights: "CC BY 4.0"
  license: "https://creativecommons.org/licenses/by/4.0/"
sat:
  version: "0.2.0"
  status: provisional
  project: uc-automa
project:
  slug: licence-migration
  status: planned             # planned | active | done | abandoned
  implements:
    - LIC-0001
  scope:
    - uc-automa
    - uc-radar
    - uc-cboard
    - universal-cake-themes
  date_started:
  date_finished:
---

# Universal Cake licence migration

This project carries out [LIC-0001](https://github.com/steelcj/vishpala-decisions/blob/main/en-ca/records/lic/LIC-0001-mit-and-cc-by-4-0.md): MIT for code, CC BY 4.0 for content, and a [trademark policy](../../policies/trademark-policy.md) for the name, all from the next version. Work through it once in `uc-automa`, then apply the same steps to each component repository.

Status: Planned.

## Before changing anything

- [ ] Confirm the decision and change LIC-0001 from Proposed to Accepted.
- [ ] Change this project's status from Planned to Active and fill `date_started`.
- [ ] List every repository and document set in scope: `uc-automa`, `uc-radar`, `uc-cboard`, `universal-cake-themes`, the Evaluation Metrics document, radar evaluations and wellbeing documentation.
- [ ] Tag the last AGPL release of each repository so the boundary is a fixed, findable point.
- [ ] List outside contributors per repository from the commit history.
- [ ] Get written agreement from each outside contributor to relicense their contributions under MIT or CC BY 4.0, or plan to rewrite or remove their parts.
- [ ] Audit dependencies for GPL, LGPL or AGPL libraries that are bundled or statically linked, and replace them or document them where a distributed build would remain copyleft.
- [ ] Check third-party content (images, fonts, quoted text) in the documentation and record its licence.

## Code repositories

- [ ] Replace `LICENSE` with the MIT License text, naming the copyright holder and year.
- [ ] Replace SPDX headers with `SPDX-License-Identifier: MIT` in every source file.
- [ ] Update package metadata (`package.json`, `pyproject.toml` or equivalent) to `MIT`.
- [ ] Add a `NOTICE` or README section stating that releases up to the tagged AGPL release remain AGPL-3.0-or-later.
- [ ] Update `CONTRIBUTING.md` so new contributions are accepted under MIT, inbound equals outbound.
- [ ] Add a CI check that flags new copyleft dependencies.

## Content and documentation

- [ ] Change the licence statement in the Evaluation Metrics document from AGPL-3.0-or-later to CC BY 4.0 and record the change in its changelog.
- [ ] Change the licence statement on radar evaluations and wellbeing documentation to CC BY 4.0.
- [ ] Update `dc.rights` and `dc.license` in the front matter of every document.
- [ ] Update the licence-statement convention in `sat-doc-automa` so new documents default to CC BY 4.0.
- [ ] Add a plain statement to wellbeing pages that they are not medical or professional advice.
- [ ] Mark trademarks in licence notices as excluded from the licence, for example "Universal Cake and its logo are not covered by this licence".

## Name and marks

- [ ] Publish the [trademark policy](../../policies/trademark-policy.md) alongside the first MIT release.
- [ ] Link the trademark policy from every README and from the radar site footer.
- [ ] Decide whether to register the Universal Cake name with the Canadian Intellectual Property Office.

## Communication

- [ ] Add a changelog entry to every repository and document set naming the version where the licence changed.
- [ ] Publish a short notice on the project site explaining the change and linking the decision record.
- [ ] Tell current clients and partners who use AGPL versions what changes for them and what does not.

## After release

- [ ] Spot-check a fresh clone of each repository for leftover AGPL headers or statements.
- [ ] Record the completed migration in the LIC-0001 changelog.
- [ ] Change this project's status to Done and fill `date_finished`.
- [ ] Ask a lawyer familiar with Canadian copyright and trademark law to review the final state.

## Changelog

| Version | Date | Status | Changes |
| --- | --- | --- | --- |
| 0.2.0 | 2026-10-11 | Provisional | Moved to `uc-automa/en-ca/projects/licence-migration/` as a project; added project front matter, status and `implements: LIC-0001` |
| 0.1.0 | 2026-10-10 | Provisional | First draft of the migration checklist |

## Licence

This document is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Drafted with AI assistance (Claude, Anthropic) and reviewed by the maintainer.
