---
title: "Session: osat-manager-git and the Manager Pattern"
dc:title: "Session: osat-manager-git and the Manager Pattern"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "osat-manager-git, conda-forge, mise, manager runtime, osat-manager-core, baseline, uc-radar, SAT ingress, session record"
dc:description: "The record of the 2026-10-21 evening session: the Git on Windows radar entry updated to conda-forge, mise studied and run, manage-git's system configuration and baseline settled, the manager runtime and osat-manager-core decided, uc-automa's own findings cleared, and an ingress verification stamp considered for SAT."
dc:date: "2026-10-21"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:97acb889-3ad0-4f69-84e0-181c189f3e18"
dc:relation:
  - "urn:uuid:19425b6e-28ad-4d57-b7c1-dd4d56a7c06c"
  - "urn:uuid:46a5763b-3757-45e8-9213-ef016b8922f1"
  - "urn:uuid:568f61fd-e8fb-4810-8cea-dfb86634327e"
  - "urn:uuid:7477a897-2518-4ad5-a6e2-1352818efd4d"
  - "urn:uuid:0114ad24-615b-4eb5-bee5-e70771d3fc32"
  - "urn:uuid:670760b6-2e8e-4dfd-9aa2-00b2369fcbb4"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Session: osat-manager-git and the Manager Pattern

Version: 0.1.0
Status: Accepted

## Summary

The session began with one task, bringing the uc-radar entry for Git on Windows into line with the decision to use conda-forge's git on every platform, and widened into the shape of the whole OSAT manager family. mise was read, run and compared with OSAT. That led to the decisions that managers never run on what they manage, that OSAT stays per-tool on client machines with mise as reference and release-time tool, and that shared code lives in osat-manager-core. manage-git's system configuration, baseline, launchers and conventions were settled along the way, uc-automa's own check findings were cleared, and SAT gained a note on stamping content verified at ingress.

## Inputs

- osat-manager-git decision 0001, *Build manage-git* (urn:uuid:19425b6e-28ad-4d57-b7c1-dd4d56a7c06c), and the uc-automa project plan for osat-manager-git (urn:uuid:73f941dd-4bde-457e-81b9-9d6447baae54).
- The uc-radar entry *Git on Windows, Options for osat-manager-git* 0.1.0, which recommended MinGit, and *Universal Cake Evaluation: mise-en-place* 0.1.0.
- *Creating an OSAT Manager Repository* 0.4.0, osat-manager-restic as the pilot, and osat-manager-python.
- mise 2026.10.17, its source and documentation, and conda-forge's git 2.56.0 packages for `win-64` and `linux-64`.
- SAT's sidecar specification v0.0.14, in satx.

## Decisions

- **conda-forge git on every platform**, recorded in the radar: conda-forge git in Trial, MinGit in Assess as the fallback, dugite-native in Hold.
- **The package's system configuration is kept.** Running mise's conda backend showed the Linux package's `etc/gitconfig` holds the prefix's certificate paths, so manage-git writes its own per-version file that includes the package's and sets the baseline, read through `GIT_CONFIG_SYSTEM`. Other managers start git from the `invocation` that `--check --json` reports (osat-manager-git 0001, revised before acceptance).
- **Baseline 1 and conventions** (osat-manager-git 0002): git 2.49.0, `core.autocrlf = false`, and on Windows `core.longpaths = true` and Git Credential Manager; `safe.directory` left out; `manager.yaml` uses `arch` and `verification.signature`; locks ship with the manager; a real `git.exe` on Windows through a junction; uninstall leaves nothing behind with no registry writes; gettext catalogues later, through osat-manager-core.
- **Managers run on a runtime they do not expose** (uc-automa 0033), after the finding that manage-python cannot remove its last Python.
- **OSAT managers and mise** (uc-automa 0034): option C. Per-tool, standard-library managers on client machines; mise informs the source kinds and schema and is an approved release-time tool; building on mise is revisited only if three named conditions all hold. mise needs no root by default, but can reach the system with `--system`, bootstrap and `/etc/mise/`.
- **osat-manager-core** (uc-automa 0035): the shared package, in its own repository, installed once into the manager runtime.
- **A check exits 2 when not ready** (uc-automa 0036).
- **No `sat:migration_status`.** Absence already says a document predates SAT. SAT is instead considering a stamp written at ingress that records the SAT version, in *Ingress Verification Stamp* v0.0.1.
- **Check findings are maintenance.** uc-automa's findings are fixed as they appear, not governed by a decision.

## What was made

### Merged

| Repository | Pull request | What |
| --- | --- | --- |
| osat-manager-git | #1 | Base files, decision 0001, `manager.yaml`, a working `--check`, the system configuration design, the radar entries named |
| uc-automa | #1 | The osat-manager-git plan 0.2.0, consistent with 0001 and the radar |
| uc-automa | #2 | Decisions 0033 and 0034; the process guide 0.5.0 |
| uc-automa | #3 | uc-automa's own check findings cleared: two licensing notes renamed and given front matter, the layout extended |
| uc-automa | #4 | Decisions 0035 and 0036; the process guide 0.6.0 |
| uc-automa | #5 | This session record |
| uc-radar | #1 | *Git on Windows* 0.2.0 |
| uc-radar | #2 | *mise-en-place* 0.1.1, with what running mise showed |
| satx | #1 | *Ingress Verification Stamp* v0.0.1, under consideration |

### Open for review

| Repository | Pull request or issue | What |
| --- | --- | --- |
| osat-manager-git | #2 | Decision 0002, the field renames, the Windows credential helper |
| osat-manager-python | issue #1 | The manager runtime, `--manager-runtime VERSION`, automatic migration, `--uninstall` with a self-deleting batch file on Windows, osat-manager-core installed into the runtime |

## Verification

- osat-manager-git: 41 unit tests pass on Python 3.14, and `uc-automa check` conforms. A real git read the rendered system configuration: the baseline overrode the package's `autocrlf`, the certificate path survived, and `git credential fill` showed the package's helper cleared. `--check` reported a conda-forge git installed by mise as meeting the baseline, in English and French.
- uc-automa: `uc-automa check` conforms on `main` and all tests pass, including `test_check_passes_on_uc_automa`, which had been failing.
- mise was run only on Linux, in an isolated sandbox. Nothing was run on Windows or macOS, and no platform is claimed verified.

## Known debt

- manage-git's YAML subset reader, data lookup, conda source kind and JSON catalogues, until osat-manager-core exists.
- osat-manager-restic's Unix launcher does not escape a `'` in a path; revisited once the manager pattern settles.

## Left open

- [ ] Create the repository `steelcj/osat-manager-core`; this session could not create repositories.
- [ ] Review and merge osat-manager-git#2.
- [ ] The release-time lock tool, and signed locks for git 2.56.0.
- [ ] manage-git's install, switch, aliases, protection and uninstall, with the Windows launcher's ownership marker and `--check` resolving manage-git's own launchers.
- [ ] End-to-end runs: Linux in an Incus container, then Windows x64 in the Windows 11 virtual machine, including whether `%PROGRAMDATA%\Git\config` is read when `GIT_CONFIG_SYSTEM` is set, and the junction with an editor. `win-arm64` has no working reference implementation.
- [ ] The name and home of SAT's ingress stamp, such as `sat:conformsTo`.
- [ ] The radar entry for conda-forge as a binary source, which the osat-manager-git plan still lists.

## References

- osat-manager-git: https://github.com/steelcj/osat-manager-git
- uc-automa: https://github.com/steelcj/uc-automa
- uc-radar: https://github.com/steelcj/uc-radar
- satx: https://github.com/steelcj/satx
- osat-manager-python: https://github.com/steelcj/osat-manager-python

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-21 | Accepted | Initial version |

## License

This document, *Session: osat-manager-git and the Manager Pattern*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
