---
title: "Decision: Sidecar Named for the Repository"
dc:title: "Decision: Sidecar Named for the Repository"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "SAT, sidecar, assets, repository name"
dc:description: "Every repository's SAT sidecar is .<repository>.assets/, for the name declared in .uc-automa.yaml; provisional until the SAT configuration cascade specification is written."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:c317ff85-d10a-4b0a-a8e4-000f85e1a7ed"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: Sidecar Named for the Repository

Version: 0.1.0
Status: Accepted

## Context

D2 named uc-automa's sidecar `.uc-automa.assets/`, and the first OSAT manager process used `.osat-manager-<tool>.assets/`. The base layout needed one rule for every repository. satx's own sidecars, `.satx.assets/` and `venvs/.venvs.assets/`, are named for the directory they describe.

## Decision

- The sidecar is `.{repository}.assets/`, holding `archive.yaml` and `dc.yaml`.
- `{repository}` comes from a declared name, `repository:` in `.uc-automa.yaml`, not from the name of the folder a clone sits in, since clones can live in folders of any name. The layout check confirms the sidecar is named for it.
- The rule is provisional, in the base layout and here: it follows satx's evidence, but the SAT configuration cascade specification, not yet written, has the final say.

## Consequences

- uc-automa's sidecar remains `.uc-automa.assets/`; uc-portage's is `.uc-portage.assets/`; osat-manager-restic's is `.osat-manager-restic.assets/`.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: Sidecar Named for the Repository*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
