---
title: "Decision: Shared Manager Package"
dc:title: "Decision: Shared Manager Package"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "OSAT managers, shared package, OpenPGP, YAML, resolver"
dc:description: "Behaviour every OSAT manager shares lives in one installed, standard-library-only package that each manager depends on; the YAML subset reader, the data lookup and the OpenPGP verifier move there in 0.2.0."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:2ecde9ee-b7bb-4d51-b58b-f0ca6bc4fc85"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: Shared Manager Package

Version: 0.1.0
Status: Accepted

## Context

The OSAT manager process left open whether shared manager behaviour should live in one installed package that every manager depends on. Building osat-manager-restic answered it in practice: the manager needed a strict YAML subset reader, because the Python manage-python installs has no PyYAML; its own copy of the uc-automa 0019 data lookup, because uc-portage is not standard-library-only; and an OpenPGP signature verifier, because the process forbids shell commands. Every later manager needs the same three. Christopher Steel answered the question on 2026-10-09: yes.

## Decision

- Behaviour every OSAT manager shares lives in one installed package, standard-library-only, that each manager depends on.
- In 0.2.0 of osat-manager-restic, the YAML subset reader, the data lookup and the OpenPGP verifier move into that package.
- Until then, osat-manager-restic's copy of the data lookup is known debt against uc-automa 0019, listed in the foundation session record.

## Consequences

- The package's name and repository are still to be chosen.
- The OpenPGP verifier is reviewed independently before any manager depending on it is tagged.
- The OSAT manager process assumes the package from its next version.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: Shared Manager Package*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
