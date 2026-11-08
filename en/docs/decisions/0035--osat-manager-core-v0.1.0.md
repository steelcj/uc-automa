---
title: "Decision: osat-manager-core, the Shared Manager Package"
dc:title: "Decision: osat-manager-core, the Shared Manager Package"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "OSAT managers, shared package, osat-manager-core, manager runtime, source kinds, gettext"
dc:description: "Names the shared manager package osat-manager-core, in its own repository with the python-tool layout, installed once into manage-python's manager runtime; lists what it holds, including the source kinds, the manager.yaml schema, launcher rendering, lock verification and gettext message catalogues."
dc:date: "2026-10-21"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:0114ad24-615b-4eb5-bee5-e70771d3fc32"
dc:relation: "urn:uuid:2ecde9ee-b7bb-4d51-b58b-f0ca6bc4fc85"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: osat-manager-core, the Shared Manager Package

Version: 0.1.0
Status: Accepted, on merge of the pull request that introduces it

## Context

uc-automa 0024 decided that behaviour every OSAT manager shares lives in one installed, standard-library-only package, and left its name and repository open. Since then, osat-manager-restic and osat-manager-git have each carried copies of the YAML subset reader and the data lookup, and the copies have already drifted. uc-automa 0033 gave every manager one runtime to run on, manage-python's manager runtime, and 0034 gave the package more to hold: source kinds modelled on mise's backends, and one `manager.yaml` schema. On 2026-10-21 Christopher Steel asked for the recommended choices.

## Decision

- The package is **osat-manager-core**, imported as `osat_manager_core`, in its own repository, `steelcj/osat-manager-core`, with uc-automa's python-tool layout.
- It is installed **once, into the manager runtime** (uc-automa 0033), from its release wheel (uc-automa 0028), rather than copied into each manager. Each manager states the range of osat-manager-core versions it accepts, and refuses to run, with a message saying which version it needs, outside that range.
- It is standard-library-only at run time, like the managers. Its release tooling may use more.
- It holds:
  - the YAML subset reader, and the data lookup of uc-automa 0019;
  - the OpenPGP verifier, reviewed independently before any manager relying on it is tagged;
  - the **source kinds**, starting with `github-release`, for restic, and `conda`, for git, including lock reading, size and SHA-256 checks, `.conda` unpacking and relocation;
  - the **`manager.yaml` schema**, with the field names settled once for every manager;
  - **launcher rendering** for each platform, with the ownership marker every manager checks before overwriting or removing a launcher;
  - **message catalogues**: gettext `.po` files under each language root, `{language}/messages/LC_MESSAGES/<domain>.po`, a template at `lib/locale/<domain>.pot`, compiled to `.mo` by release tooling and read with the standard library's `gettext`, as SAT's sidecar specification lays out for interface translations.
- Code moves into osat-manager-core from the managers that hold it today, with their tests; it is not rewritten from scratch.

## Consequences

- The repository `steelcj/osat-manager-core` has to be created, and its decision record placed in its first commit, as the OSAT manager process asks of a new repository.
- manage-python installs osat-manager-core into the manager runtime when it creates or replaces that runtime, so osat-manager-python#1 gains a step.
- osat-manager-restic and osat-manager-git drop their copies as known debt is paid. Their `manager.yaml` files move to the shared schema in the same change.
- Every manager's messages become gettext catalogues; manage-git's JSON catalogues and restic's fixed English strings both change once.
- A breaking change to osat-manager-core needs a coordinated release of every manager that depends on it, which is what the version range makes visible.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-21 | Accepted | Initial version, settling the name, repository and installation left open by 0024 |

## License

This document, *Decision: osat-manager-core, the Shared Manager Package*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
