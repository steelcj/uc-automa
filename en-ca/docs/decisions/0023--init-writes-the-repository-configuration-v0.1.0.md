---
title: "Decision: init Writes the Repository Configuration"
dc:title: "Decision: init Writes the Repository Configuration"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "init, .uc-automa.yaml, subscriptions, offerings"
dc:description: "uc-automa init writes a repository's .uc-automa.yaml once, from its arguments; the file that declares subscriptions cannot arrive by subscription, so there is no uc-automa-config offering."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:22002b13-94b7-46e5-9d5b-e2970a49a115"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: init Writes the Repository Configuration

Version: 0.1.0
Status: Accepted

## Context

The foundation brief listed a uc-automa-config offering. But every repository writes its `.uc-automa.yaml` before it can subscribe to anything, so an offering delivering that file would always find it already present.

## Decision

- There is no uc-automa-config offering.
- `uc-automa init --repository NAME --layout ID` writes `.uc-automa.yaml` once, from no template: the repository and layout from its arguments, `automa_version` as the installed version, `language: en-ca`, and `subscribe` derived from the `from_offering` marks on the paths the layout chain requires.
- `init` refuses to run if `.uc-automa.yaml` already exists.
- `.uc-automa.yaml` is owned by the repository: no layout marks it `from_offering`.
- The layout check reports an error if a layout marks a path `from_offering: X` and the repository does not subscribe to `X`.

## Consequences

- The OSAT manager process subscribes a new repository with `init`, then `uc-automa offerings apply`.
- Optional paths, such as `LICENSES/CC-BY-4.0.txt` for content, are not subscribed by `init`; a repository that holds content adds `license-cc-by-4-0` itself.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: init Writes the Repository Configuration*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
