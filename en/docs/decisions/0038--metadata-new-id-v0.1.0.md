---
title: "Decision: uc-automa metadata new-id"
dc:title: "Decision: uc-automa metadata new-id"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "metadata, identifiers, dc:identifier, UUID, urn:uuid, uuidgen"
dc:description: "uc-automa metadata new-id prints a fresh random UUID as a urn:uuid: value, ready for dc:identifier, replacing uuidgen -r run by hand."
dc:date: "2026-10-23"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:95e3d156-0c5c-42f3-9e04-b8ba7d324cba"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: uc-automa metadata new-id

Version: 0.1.0
Status: Accepted

## Context

Every document, decision record and SAT sidecar carries a `dc:identifier` holding a random UUID as a URN. Until now each one was made by running `uuidgen -r` and writing `urn:uuid:` in front of its output by hand. `uuidgen` is not installed on Windows, and the prefix is easy to leave out. The roadmap for 0.2.0 lists replacing it.

## Decision

- `uc-automa metadata new-id` prints one random (version 4) UUID as a `urn:uuid:` value, such as `urn:uuid:95e3d156-0c5c-42f3-9e04-b8ba7d324cba`, and nothing else.
- It uses Python's standard `uuid` module, so it works wherever uc-automa runs, on all three platforms.
- It reads no repository and needs no `.uc-automa.yaml`, so it can be run before `init`, as the first commit of a new repository requires.

## Alternatives considered

**Printing the bare UUID, as `uuidgen -r` does.** Rejected. Every use writes the URN form, so printing it removes the step most often forgotten.

**Writing the identifier into a file.** Rejected. Templates and sidecars are written by people; the command supplies the value and leaves the editing to them.

## Consequences

- Guides and templates that say to run `uuidgen -r` can say `uc-automa metadata new-id` instead.
- Existing identifiers are unaffected: both produce random version 4 UUIDs.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-23 | Accepted | Initial version |

## License

This document, *Decision: uc-automa metadata new-id*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
