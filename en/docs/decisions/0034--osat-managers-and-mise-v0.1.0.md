---
title: "Decision: OSAT Managers and mise"
dc:title: "Decision: OSAT Managers and mise"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "OSAT managers, mise, shared manager package, source kinds, lock files, release-time tools"
dc:description: "OSAT managers stay governed, per-tool, standard-library managers on client machines. mise is not a runtime dependency; its backends and registry inform the shared manager package's source kinds and manager.yaml schema, and it is an approved release-time tool for producing and cross-checking lock files."
dc:date: "2026-10-21"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:7477a897-2518-4ad5-a6e2-1352818efd4d"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: OSAT Managers and mise

Version: 0.1.0
Status: Accepted, on merge of the pull request that introduces it

## Context

mise-en-place, mise, installs and switches developer tools from many sources through backends, and records per-tool knowledge in a curated registry: which commands a package exposes, how its versions order, how to test an install, and which operating systems it supports. Its radar entry, *Universal Cake Evaluation: mise-en-place*, keeps it in Assess. On 2026-10-21 its conda backend installed, locked and removed conda-forge git on Linux; it gave machine-readable answers through `mise ls --json`, `mise tool <name> --json`, `mise where` and `mise which`.

Like OSAT managers, mise installs into the user's own directories and needs no administrator rights by default. It can also act on the system when asked: `mise install --system` uses `sudo` to place tools in `/usr/local/share/mise`, its bootstrap can add apt and dnf repositories, and a system `config.toml` under `/etc/mise/` is read by every user.

Three targets were weighed on 2026-10-21: keep per-tool managers and rebuild every source kind by hand; build OSAT as a policy layer over mise; or a hybrid. Against mise as a runtime on client machines: one person holds write access to its core; some registry tools still resolve to asdf plugins, which run third-party shell code; its checksum check passes when a lock records no checksum; its conda backend does not map Windows ARM64; it reads project configuration that can set environment variables and run hooks; and its messages are English only. It also has no baseline contract of the kind other managers ask manage-git about. Christopher Steel chose the hybrid.

## Decision

- OSAT managers remain governed, per-tool, standard-library managers, and they are what runs on client machines. mise is not a runtime dependency of any OSAT manager.
- The shared manager package (uc-automa 0024) takes its **source kinds** from mise's backends, starting with `github-release`, for restic, and `conda`, for git, each named in `manager.yaml` as `sources.kind`.
- The `manager.yaml` schema borrows the fields mise's registry found necessary where an OSAT manager needs them: the commands a package exposes, how versions order, a test command, and the operating systems supported. Field names are settled once, in the shared package, before a second manager adopts them.
- mise is an approved **release-time tool**: a manager's release tooling may use it, alongside or instead of rattler or micromamba, to produce or cross-check lock files. It never ships to client machines, and its output is a reviewed input, never trusted as is.
- OSAT locks record each file's size as well as its SHA-256, and a manager refuses an entry with no checksum instead of letting it pass, where mise's lock and verification do not.
- Building OSAT on top of mise is revisited when all three hold: a second person has write access to mise's core, asdf plugins are gone from its registry, and its verification refuses a missing checksum. Even then, it would be considered for developer machines first.

## Consequences

- The radar entry for mise records the 2026-10-21 observations and these revisit conditions in its next version.
- osat-manager-git's `manager.yaml` moves to the shared schema when the shared package exists; field names chosen in it now are provisional.
- *Creating an OSAT Manager Repository* names source kinds and the approved release-time tools from its version 0.5.0.
- OSAT gives up mise's breadth: each new source kind is still written, reviewed and tested in the shared package, at the pace of review.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-21 | Accepted | Initial version: option C of the 2026-10-21 review, agreed by Christopher Steel |

## License

This document, *Decision: OSAT Managers and mise*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
