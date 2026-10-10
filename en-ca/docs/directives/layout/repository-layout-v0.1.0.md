---
title: "Layout: Repository Layout"
dc:title: "Layout: Repository Layout"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "layout, base, python-tool, osat-manager, closed, required, from_offering, D13"
dc:description: "A repository holds what its layout type describes: every top-level entry is described, closed directories hold only described entries, required paths are present, the sidecar is named for the repository, and every from_offering path's offering is subscribed."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:e3c45b3f-7f7a-4521-9cf8-cfc8c5a9f6f8"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "In force"
sat:directive: "layout/repository-layout"
sat:enforced_by:
  - "conformance.layout.repository_layout"
---

# Layout: Repository Layout

Version: 0.1.0
Status: In force

## Rule

A repository names its layout type with `layout:` in `.uc-automa.yaml`. The layout, resolved through its `extends` chain (uc-automa 0013), describes what the repository contains.

- **The root is closed.** Every top-level file and directory is described by the layout. A top-level path the layout does not describe is a finding about the layout, not a reason for an exception; there is no per-repository escape hatch.
- **Closed directories.** A directory marked `closed: true` holds only entries matching a declared child. Other directories are open: entries matching a declared child are checked, others are left alone.
- **Required paths.** `required: true` paths are present. `required: source-language` paths are present in the source language's root. Inside a language root, `required: true` means required in every language root that is present.
- **The sidecar** is named `.<repository>.assets/`, for the name declared in `.uc-automa.yaml`, not the name of the folder the clone sits in.
- **Offerings.** A path the layout marks `from_offering: X` that is present or required means the repository subscribes to `X`.

Only the files the repository contains are checked. In a git working tree, that is tracked files and untracked files git does not ignore; outside git, as in a release tarball, every file. `.git/` is never counted.

## Rationale

Paths say what a thing is (P2), and each kind of material has one home (P4). A layout written as data lets a person, an AI collaborator and a tool agree on what any path holds, and lets the check say exactly what is out of place.

## Examples

| Repository holds | Verdict |
| --- | --- |
| `notes.txt` at the root of a `python-tool` repository | Not described by the layout |
| `en-ca/docs/decisions/0001-licensing-v0.1.0.md` | Not described: decisions/ is closed and expects `{number}--{slug}{version}.md` |
| `.osat-manager.assets/` with `repository: osat-manager-restic` | Sidecar named for the wrong repository |
| `CHANGELOG.md` without subscribing to `changelog` | Layout delivers it from an unsubscribed offering |

## Check

`conformance.layout.repository_layout` compares the repository's files with its merged layout. Its fixtures are under `tests/fixtures/conformance/layout/repository-layout/`; each case is a small repository.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | In force | Initial version |

## License

This document, *Layout: Repository Layout*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
