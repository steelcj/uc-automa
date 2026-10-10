---
title: "Session: uc-automa Foundation"
dc:title: "Session: uc-automa Foundation"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "uc-automa, uc-portage, osat-manager-restic, foundation, session record"
dc:description: "The record of building uc-portage, uc-automa and osat-manager-restic from the foundation brief: inputs by identifier, rulings, what was made and verified, what the brief and the process got wrong, and what is left open."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:aab81fdc-a837-4adb-bb33-0f991c3d5fac"
dc:relation:
  - "urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96"
  - "urn:uuid:cd696843-52b7-4406-a096-fc73df3bba05"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Session: uc-automa Foundation

Version: 0.1.0
Status: Accepted

## Summary

This session built uc-portage 0.1.0 and uc-automa 0.1.0 from the foundation brief <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b), and then osat-manager-restic 0.1.0 as the pilot. It was carried out by Claude Opus 5.5 in Claude Code, with Christopher Steel answering every question the brief left open. Each repository was stopped at for review before the next began. Nothing was pushed, tagged or archived, and no existing repository was changed.

## Inputs

The hand-off package `2026-10-09--uc-automa-foundation` held the brief, a manifest, and these inputs:

| Input | Identifier | What became of it |
| --- | --- | --- |
| Brief: uc-automa Foundation | `urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96` | The authority for the session |
| Decision: Licensing for Code, Documentation and Content | `urn:uuid:14f3cf06-ab5d-454e-8c00-d81c36a21d08` | Placed as uc-automa 0001, as it stood, with `dc:source` |
| Layout structure and words for uc-automa | none | Split into `base`, `python-tool`, `uc-automa` and `osat-manager` |
| Prototype layout and translation check | none | Grown into the layout and translation checks |
| Automa: Directory Guide | `urn:uuid:c73e134d-11d2-44f9-a0ef-a0d446a896a3` | Revised as the directory guide, version 0.2.0 |
| OSAT Manager: Creating a New Repository | `urn:uuid:b18e2ed3-b364-4880-b3c7-5676961f0174` | Revised as the OSAT manager process, version 0.2.0 |
| uc-automa: File System Layout | `urn:uuid:00c295c7-9bb9-4992-b629-bd1eb3f1a5dd` | Taken apart into decision records, directives and the layouts |
| Automa Access: Options for Sharing the Automa | `urn:uuid:c50d1c25-2536-43ed-be85-02c8249d4aa0` | Not placed; destined for uc-radar through its own review |
| Overview: SAT Development, Current State | `urn:uuid:cd696843-52b7-4406-a096-fc73df3bba05` | Background; the starting point of the later migration plan <a id="cite-steel-2026o"></a>[(Steel, 2026o)](#ref-steel-2026o) |
| Automa Access: Recommendations by Kind of Material | `urn:uuid:0c17465b-3298-408e-9ae7-715a2019a960` | Background; cited by uc-automa 0006 and 0008 |
| References: Automa Access and Sync Options | none | Superseded by the options document's reference list |

## Decisions

The brief's settled decisions D1 to D18 became uc-automa 0001 to 0018, with D6 as 0001 and D9 confirmed during the session. Christopher Steel ruled on the questions the brief left open:

| Question | Ruling | Recorded in |
| --- | --- | --- |
| Where the repositories go | Beside the existing ones, in `~/areas/development/` | This record |
| A layout for uc-portage | `python-tool`, extended by both uc-automa and osat-manager, taken from what uc-portage holds | uc-automa 0013 |
| The extends rules, kind, from_offering and closed directories | Add or tighten, never take away; root always closed; check only the repository's files | uc-automa 0013 |
| L1, a root LICENSE | Kept, byte-identical to `LICENSES/GPL-3.0-or-later.txt`, one payload | uc-automa 0021 |
| Decision record names | `{number}--{slug}{version}.md`; numbered within each repository, globally only in uc-automa | uc-automa 0010, the base layout words |
| Migrating file-fairy's decisions without identifiers | New `urn:uuid`, old identifier in `dc:source`, revised as 0.2.0 | uc-portage 0001 and 0002 |
| Destination containment | Reverses file-fairy's design note | uc-portage 0003 |
| `{language}` in offerings | The subscriber's language first, the offering's source language as fallback | the uc-portage guide |
| Packaging data | `pyproject.toml` mapping, one resolver, a proven-checkout fallback | uc-automa 0019 |
| Offerings for pinned repositories | Package data; exact pin below 1.0.0; `self` only in uc-automa | uc-automa 0020 |
| The sidecar | `.{repository}.assets/`, provisional | uc-automa 0022 |
| The uc-automa-config offering | Dropped; `uc-automa init` writes `.uc-automa.yaml` | uc-automa 0023 |
| Licence offering names | `license-` and the SPDX slug | the directive `naming/spdx-slugs` |
| Heading numbers | Section numbering only; versions in headings allowed | the directive `markdown/no-heading-numbers` |

## What was made

### uc-portage 0.1.0

The engine from file-fairy 0.7.0 with every one of its tests ported, behind a front end that reads `offering.yaml` files and subscribed identifiers. Added: `offering.schema.yaml` with a standard-library validator, checksums blind to line endings, the case-collision check, containment of destinations and sources, `{language}` with fallback, `harvest` as a report, and the shared data resolver. 58 tests, of which two build real installs.

### uc-automa 0.1.0

The four layouts and their words; eleven directives, each with a check and pass and fail fixtures; `uc-automa init`, `check`, `offerings`, `docs index` and `translations`; nine offerings; two schemas; decision records 0001 to 0023; five templates; the directory guide; the OSAT manager process; and this record. uc-automa subscribes to its own offerings with `automa_version: self`. 36 tests, of which two build real installs.

## Verification

| Check | Result |
| --- | --- |
| Every ported file-fairy test | Passes |
| CRLF reported unchanged, case collisions refused, harvest reports a target-only change and ignores a source-only one | Pass; each test fails when its feature is broken on purpose |
| Every offering in uc-portage's tests against `offering.schema.yaml` | Valid ones validate, invalid ones are refused |
| `uc-automa check` on uc-automa | Passes |
| `uc-automa offerings plan` on uc-automa after `apply` | Nothing to do |
| Translation report for `en-ca` | No errors, nothing untranslated, nothing stale |
| Every directive with a check has pass and fail fixtures | Yes; each fail case fails for its intended reason |
| Hyphenated version form in any filename | None |
| `reuse lint` | Compliant in both repositories |
| Python versions | 3.12 on the development machine, 3.8 in an AlmaLinux 8 container |
| macOS and Windows | Not yet verified. The Windows 11 virtual machine has no Incus agent and no remote access enabled, so tests could not run there without changing its setup |

## What the brief and the process got wrong

- **The uc-automa-config offering cannot work.** The file that declares subscriptions cannot arrive by subscription. It was dropped for `uc-automa init` (uc-automa 0023).
- **`offering.schema.yaml` was in uc-automa's layout,** although D15 places it in uc-portage and nothing is stored twice.
- **`lib/uc_automa/release/` was required,** although the release ceremony is deferred to 0.2.0 and P12 forbids empty directories.
- **Decision records were named `{number}-{slug}`,** a single hyphen between two parts, against D10.
- **"Decision records for D1 to D18"** included D9, which was still open.
- **The sidecar rule covered only uc-automa.** Other repositories had no rule until uc-automa 0022.
- **kind and the extends rules conflicted:** inherited paths needed a kind in uc-automa that no other repository has. Resolved by "add or tighten, never take away".
- **"A migrated document keeps its identifier"** assumed identifiers that file-fairy's documents did not have.
- **The packaging fallback assumed `setup.py` would rescue editable installs.** It fails the same way as the mapping alone (uc-automa 0019).
- **Two acceptance checks conflicted.** "No filename anywhere uses the hyphenated version form" and "every directive with a check has fail fixtures" cannot both hold with a committed fixture for that form; the case is built at test time instead.
- **Templates "already satisfy the front matter schema"** cannot hold while they carry placeholders; the words now say they carry every required key.
- **The licensing decision, placed as it stood,** still names `schemas/automa-config.schema.yaml` and a licence-block offering that do not exist; a later version should correct them.
- **The OSAT manager process** still carried AGPL-3.0-or-later in its sidecar example, `.automa.yaml`, a pre-commit offering that was never in the brief, an interim file-fairy route, and a release ceremony that does not exist yet. Its subscribe-stage gate required `automa check` to pass before the README, roadmap and index exist, which no new repository can meet; the gate is now the plan alone.
- **A Python 3.8 machine** was assumed but not available; an AlmaLinux 8 container stood in.

## Left open

- [ ] L2: are uc-radar entries content or documentation, and is the metrics document documentation?
- [ ] Should shared manager behaviour live in one installed package that every manager depends on?
- [ ] Where is the list of OSAT managers kept?
- [ ] Is `osat` the right directory name inside each platform's per-user data location?
- [ ] Should a future `harvest` write a branch in the automa checkout, a patch file, or both?
- [ ] How should the Windows 11 virtual machine be reached for testing: the Incus agent, OpenSSH, or another way?
- [ ] Publishing uc-portage and uc-automa somewhere pip can install them from, so the pre-commit hook can install itself.

## References

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Brief: uc-automa foundation* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96 [↩](#cite-steel-2026b)

<a id="ref-steel-2026o"></a>Steel, C. (2026o). *Overview: SAT development, current state* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:cd696843-52b7-4406-a096-fc73df3bba05 [↩](#cite-steel-2026o)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Session: uc-automa Foundation*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
