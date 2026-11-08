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
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Session: uc-automa Foundation

Version: 0.1.0
Status: Accepted

## Summary

This session built uc-portage 0.1.0, uc-automa 0.1.0 and osat-manager-restic 0.1.0 from the foundation brief <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b). It was carried out by Claude Opus 5.5 in Claude Code, with Christopher Steel answering every question the brief left open. Each repository was stopped at for review before the next began. Nothing was pushed, tagged or archived, and no existing repository was changed.

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
| Where the repositories go | Beside the existing repositories | This record |
| A layout for uc-portage | `python-tool`, extended by both uc-automa and osat-manager, taken from what uc-portage holds | uc-automa 0013 |
| The extends rules, kind, from_offering and closed directories | Add or tighten, never take away; root always closed; check only the repository's files | uc-automa 0013 |
| L1, a root LICENSE | Kept, byte-identical to its `LICENSES/` copy, one payload; first GPL-3.0-or-later, MIT since uc-automa 0025 | uc-automa 0021, 0025 |
| Licences before the first publication | MIT for code, CC BY 4.0 for documentation and content, carrying out LIC-0001 | uc-automa 0025 |
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

### osat-manager-restic 0.1.0

The pilot, built by following the revised OSAT manager process stage by stage. `manage-restic` meets the manager contract. Every download is verified in two steps before it is unpacked: the OpenPGP signature on restic's `SHA256SUMS` against restic's signing key, pinned by fingerprint in `manager.yaml` and checked with the standard library, then the download's SHA-256 against the signed list. The repository subscribed through `uc-automa init` with `layout: osat-manager`, and the layout needed no change. A radar entry for restic was written as a draft at `drafts/uc-radar/uc-radar--restic--backup-tool-v0.1.0.md` in the hand-off folder, for Christopher Steel to place in uc-radar. osat-fluent-restic-tool was read for lessons only: install that did not activate, raw 404 errors, and signature checking deferred for want of `gpg`.

### Review of the OpenPGP verifier

Before osat-manager-restic was tagged, its verifier was reviewed independently three times, each time by a reviewer that had not seen it written or reviewed:

- **First review:** no way to forge a signature, but SHA-224 and signatures without an issuer were accepted, and malformed input raised other exception types. The verifier was rewritten to parse strictly and fail closed.
- **Second review, of the rewrite:** no forgery path. A fingerprint that is not text and oversized input were fixed, text signatures and duplicate time subpackets refused, and its test gaps closed.
- **Third review, of that change:** no violation of the five required properties. Its findings are 0.1.1 items in osat-manager-restic's roadmap, by the stop rule Christopher Steel set.

Every hand-crafted test vector is confirmed with `gpg --verify`. The verifier differs from gpg only under named policies, and gpg corrected several of the expected verdicts written for it. restic's real 0.19.1 signature is a regression vector.

### The offline step

`tests/incus_acl.py` in osat-manager-restic cuts an Incus instance off the network, except the host's SSH, for the scenario's offline step on machines reached over SSH. It is undone by four independent layers: a finally block, a user systemd dead-man's switch, start-up recovery and a snapshot restore. A kill test showed the dead-man's switch and start-up recovery each restore the clean state on their own. Its self-test proves the cut with probes that work before, fail during and work after. On this host, DNS to the bridge stays reachable during the cut, as Incus exempts it, and is accepted as a known channel. The cut drops rather than rejects. The IPv6 internet path is not testable, because the host has no IPv6 route.

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
| Python versions | 3.12 on the development machine, 3.8 in an AlmaLinux 8 container, for all three repositories |
| `uc-automa check` on uc-portage and osat-manager-restic | Passes, as `python-tool` and `osat-manager` |
| restic's real 0.19.1 signature | Verifies with the pure-Python verifier and with GnuPG; a changed checksum file or signature is refused |
| The OSAT end-to-end scenario on Linux amd64 | Passes, all seven steps including the offline restore, as an ordinary user in a Linux Mint 22.3 Incus container restored to a clean snapshot before and after; the account is left exactly as it was |
| macOS and Windows | Not yet verified. No Apple hardware was available. The Windows 11 virtual machine has no Incus agent and no remote access enabled, so nothing could run there without changing its setup |

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
- **The process pairs a YAML manifest with standard-library-only code.** The Python manage-python installs has no PyYAML, so manage-restic reads `manager.yaml` with a strict subset reader of its own.
- **The process asks for signature verification but forbids shell commands,** and gives no way to verify OpenPGP in the standard library. manage-restic implements the RSA verification it needs; osat-fluent-restic-tool had deferred it for this reason.
- **One resolver cannot reach a standard-library-only manager.** uc-portage is not standard-library-only, so manage-restic carries its own copy of the uc-automa 0019 lookup until a shared manager package exists.
- **Recording the decision comes before creating the repository** in the process, but the record lives in the repository; it was written after the repository existed.
- **"Nothing left behind" needs more than the contract says:** the manager has to remember the directories it creates outside its install root, such as `~/.local/bin` in a new account, to remove them when empty.
- **Upstream file names break the naming directives** when kept as test data, such as `SHA256SUMS` and `restic_0.19.1_linux_amd64.bz2`; they are kept inside zip files.
- **"A fresh Incus container"** depended on launching from the remote image server, which hung several times; restoring a container to a clean snapshot, as Christopher Steel suggested, gave the same fresh account reliably.
- **The radar entry template** still carries AGPL-3.0-or-later and the hyphenated version form, and L2 is open, so the restic entry's licence is left for placement.

## Known debt

- **A second copy of the data lookup.** osat-manager-restic finds its `manager.yaml` with its own copy of the uc-automa 0019 rule, because uc-portage's resolver is not standard-library-only. It moves into the shared manager package in osat-manager-restic 0.2.0 (uc-automa 0024), with the YAML subset reader and the OpenPGP verifier.

## Left open

- [ ] L2: are uc-radar entries content or documentation, and is the metrics document documentation?
- [ ] Where is the list of OSAT managers kept?
- [ ] Is `osat` the right directory name inside each platform's per-user data location?
- [ ] Should a future `harvest` write a branch in the automa checkout, a patch file, or both?
- [ ] How should the Windows 11 virtual machine be reached for testing: the Incus agent, OpenSSH, or another way?
- [ ] Publishing uc-portage and uc-automa somewhere pip can install them from, so the pre-commit hook can install itself.
- [ ] Placing the restic radar entry in uc-radar, adding manage-restic to the list of OSAT managers, and archiving osat-fluent-restic-tool and file-fairy with notices naming their successors: Christopher Steel's actions.
- [ ] Pushing the three repositories, after which file-fairy and osat-fluent-restic-tool are archived with notices naming their successors. uc-portage and uc-automa were tagged v0.1.0 on 2026-10-09, and osat-manager-restic on 2026-10-10, after three independent reviews of its verifier.
- [ ] Verifying Windows: Christopher Steel prepares the virtual machine's OpenSSH access from the plan in the hand-off folder, then the scenario runs there; the IPv6 cut is to be re-proven on a network with IPv6 first.
- [ ] Naming the shared manager package and its repository (uc-automa 0024).

## References

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Brief: uc-automa foundation* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96 [↩](#cite-steel-2026b)

<a id="ref-steel-2026o"></a>Steel, C. (2026o). *Overview: SAT development, current state* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:cd696843-52b7-4406-a096-fc73df3bba05 [↩](#cite-steel-2026o)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Session: uc-automa Foundation*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
