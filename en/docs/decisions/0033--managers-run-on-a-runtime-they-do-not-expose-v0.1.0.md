---
title: "Decision: Managers Run on a Runtime They Do Not Expose"
dc:title: "Decision: Managers Run on a Runtime They Do Not Expose"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "OSAT managers, manager runtime, removal, uninstall, osat-manager-python"
dc:description: "An OSAT manager never runs on a version of a tool it exposes to the user. Managers run on a pinned manager runtime that manage-python keeps apart from the user's Python versions, so every user-facing version, including the last, can be removed, and uninstalling leaves nothing behind."
dc:date: "2026-10-21"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:568f61fd-e8fb-4810-8cea-dfb86634327e"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: Managers Run on a Runtime They Do Not Expose

Version: 0.1.0
Status: Accepted, on merge of the pull request that introduces it

## Context

Christopher Steel found on 2026-10-21 that osat-manager-python cannot remove its last Python. Its `--remove` refuses the default version, because the `manage-python` launcher runs the manager on that same default runtime, and the manager has no `--uninstall`. A manager that runs on what it manages can never remove the last of it, which breaks the contract's "nothing left behind".

The dependency reaches further than one manager. Every OSAT manager is standard-library Python, and osat-manager-git requires Python 3.14 from manage-python (its decision 0001). If managers run on whatever Python is the user's default, removing or switching that Python can break every manager at once.

mise, evaluated on the radar, does not have the problem: it is one static binary that runs on nothing it installs, and on 2026-10-21 it removed the only installed version of a tool without complaint.

## Decision

- An OSAT manager never runs on a version of a tool that it exposes to the user, through an alias, as the active version, or in a listing of installed versions.
- manage-python keeps a **manager runtime**: one pinned CPython under its install root's `manager/` directory, installed and verified like any other version, not listed among the user's versions, and not affected by `--switch` or `--remove`. Every user-facing version, including the last, can then be removed.
- Every OSAT manager's own launcher runs it on the manager runtime, named by path, never on the first `python` on `PATH` or on the user's default.
- The manager runtime is replaced only by `manage-python --update-manager-runtime` (name to be settled in osat-manager-python), which verifies the new runtime, health-checks it, runs each installed manager's `--version` on it, and only then switches the launchers.
- `--uninstall` removes the manager runtime last. Where a running interpreter cannot delete itself, as on Windows, it stages what remains for removal and says exactly which directory is left, so nothing is left behind silently.

## Consequences

- osat-manager-python needs the manager runtime, `--uninstall`, and a migration that moves an existing installation's manager onto it. That work is the first application of this decision.
- The contract in *Creating an OSAT Manager Repository* gains a row, "Independent runtime", from its version 0.5.0.
- A manager's minimum Python, such as 3.14 for manage-git, is a requirement on the manager runtime, not on the user's Python.
- The manager runtime costs one extra CPython of disk space, about the size of one user version.
- Managers keep depending on manage-python being installed first. That ordering is unchanged; only which Python they run on changes.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-21 | Accepted | Initial version, from the osat-manager-python removal problem; option C of the 2026-10-21 review, agreed by Christopher Steel |

## License

This document, *Decision: Managers Run on a Runtime They Do Not Expose*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
