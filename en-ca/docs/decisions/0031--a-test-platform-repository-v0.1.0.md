---
title: "Decision: A Test Platform Repository"
dc:title: "Decision: A Test Platform Repository"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "verification, test platform, drivers, Windows, Linux, macOS, network cut, incus"
dc:description: "Answers the open question of uc-automa 0027: the drivers that run verification runs and end-to-end scenarios, the network cut, the README replay and the recipes for the clean test instances live in one dedicated repository, a Python tool released like the others, which writes each run's record into the repository it verified."
dc:date: "2026-10-11"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:b10c3e4f-65c2-485f-b39e-c90af48242b4"
dc:relation:
  - "urn:uuid:3b8c02de-92e2-4e89-8efb-022e545075ac"
  - "urn:uuid:cc8bd92f-4dcf-4263-8c8e-a62395dbc1a4"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: A Test Platform Repository

Version: 0.1.0
Status: Accepted

## Context

The Windows driver lives in osat-manager-restic as `tests/e2e/windows/run_over_ssh.py`, beside `tests/incus_acl.py`, which cuts an instance's network and proves the cut. It also runs uc-portage's and uc-automa's tests, and builds their wheels. uc-automa 0027 asks where the driver lives, and lists what it has to learn: wheels from the commit under test, the README's install blocks replayed as written against local mirrors, the oldest Python, a `Result:` line, and a record written into each verified repository <a id="cite-steel-2026a"></a>[(Steel, 2026a)](#ref-steel-2026a). A Linux test instance is being set up, and macOS will follow. Kept in one manager's tests, this code would be copied into every repository that needs it.

## Decision

### One repository for the test platform

A new repository, `uc-test-platform`, holds everything that runs a verification or an end-to-end scenario on a clean instance, and nothing that belongs to one tool:

- **The drivers**, one per way of reaching an instance: over SSH for Windows, with `incus exec` for Linux, and later macOS.
- **The network cut**, moved from osat-manager-restic's `tests/incus_acl.py` with its self-test, and the IPv6 rule.
- **The verification run** of uc-automa 0027: the README replay (sections, one block per shell, line by line), the mirrors and their `insteadOf` mappings, the test signing key and the two bad cases, the oldest-Python pass, and the record with its placeholders and `Result:` line.
- **The recipes for the clean instances**: how each snapshot is built, the user, manage-python and the Pythons it holds, git and OpenSSH, written as scripts and documented, so a snapshot can be rebuilt rather than trusted.

### What stays in each tool

- A tool's own job for the verification run, as the table in uc-automa 0027 names it, and an OSAT manager's scenario steps, stay in that tool's repository. The platform runs them.
- The record is written into the verified tool's repository, under `tests/e2e/<platform>/`, and names the test platform's version and commit as well as the commit under test.

### The repository itself

- A Python tool with the `python-tool` layout, MIT for code and CC BY 4.0 for documentation (uc-automa 0025), released with `uc-automa release` like the others, and pinned by version in each run's record.
- It depends on uc-automa, whose wheel step it calls to build the run's wheels exactly as a release does (uc-automa 0028).
- It runs on the host that holds the instances, as the person who owns them; it never needs an administrator inside an instance.
- Its own tests run offline. Its run against uc-portage on Linux and Windows is its end-to-end test before each release.

### Before its first release

- The verification runs for uc-portage 0.2.0 and uc-automa 0.2.0 use the platform at a recorded commit, given by its full hash and named in each record, never at a branch tip resolved during the run.
- Its first release follows uc-automa 0.2.0, since it calls uc-automa's wheel step, which ships in 0.2.0; until then it uses that step from the uc-automa commit the run records.

## Alternatives considered

**Keep the driver in osat-manager-restic.** Rejected. uc-portage and uc-automa would be verified by a manager's test code, and every other manager would copy it.

**Put the platform in uc-automa.** Rejected. uc-automa is installed in every repository; the platform needs incus, SSH and test instances, which only the host running verification has, and uc-automa's releases would then wait on test infrastructure.

**One driver script per repository.** Rejected for the same reason as copied release scripts (uc-automa 0026): copies drift.

## Consequences

- osat-manager-restic's Windows driver and `tests/incus_acl.py` move to the new repository; its scenario steps stay, run by the platform.
- uc-automa 0027's open question about the driver's home is answered.
- The Windows snapshot `osat-ready-tools` and the Linux snapshot `osat-ready-tools` of the container `linux` get recipes in the new repository.

## Open questions

- [ ] Whether macOS is reached over SSH like Windows, once Apple hardware is available.

## References

<a id="ref-steel-2026a"></a>Steel, C. (2026a). *Decision: Verification without an end-to-end scenario* (Version 0.1.0) [Decision record]. uc-automa 0027. https://github.com/steelcj/uc-automa/blob/main/en-ca/docs/decisions/0027--verification-without-an-end-to-end-scenario-v0.1.0.md [↩](#cite-steel-2026a)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-11 | Accepted | Initial version |

## License

This document, *Decision: A Test Platform Repository*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
