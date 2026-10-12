---
title: "Decision: Verification Without an End-to-End Scenario"
dc:title: "Decision: Verification Without an End-to-End Scenario"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "verification, platforms, Linux, macOS, Windows, Python 3.8, wheels, offline install, run records, 1.0.0"
dc:description: "Extends uc-automa 0011 to tools that have no end-to-end scenario, such as uc-portage and uc-automa: a platform is verified by a verification run of three parts, the unit tests, also on the oldest Python the tool supports, an offline install from the wheels a release of the commit would publish, inside a network cut, and the installed tool doing its job on a real repository at a recorded commit, recorded in the tool's own repository."
dc:date: "2026-10-11"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:3b8c02de-92e2-4e89-8efb-022e545075ac"
dc:relation:
  - "urn:uuid:cc8bd92f-4dcf-4263-8c8e-a62395dbc1a4"
  - "urn:uuid:a7667fcc-3e79-40d1-961a-35bd390b4137"
  - "urn:uuid:02eec912-6fb4-43f6-9a5d-db7b49e6e03c"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: Verification Without an End-to-End Scenario

Version: 0.1.0
Status: Accepted

## Context

A tool reaches 1.0.0 only when it is verified end to end on Linux, macOS and Windows, and a platform is verified by running the end-to-end scenario on it <a id="cite-steel-2026a"></a>[(Steel, 2026a)](#ref-steel-2026a). The release ceremony enforces this: `uc-automa release bump` refuses 1.0.0 unless the repository holds a passing run record for each platform under `tests/e2e/<platform>/`, one that states `Result: passed` <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b).

An OSAT manager has an end-to-end scenario, because the manager contract defines one: install, side by side versions, aliases, protection, offline restore and uninstall. uc-portage and uc-automa have none. Their commands read and write repository content, and their unit tests already run those commands in-process against scratch repositories. Until now each README carried its own Windows criteria, written on 2026-10-11, with nothing saying what verifies Linux or macOS for these tools.

The Windows run of 2026-10-11 showed what unit tests alone miss <a id="cite-steel-2026c"></a>[(Steel, 2026c)](#ref-steel-2026c). The unit tests passed in a virtual environment where PyYAML had been installed by hand, while the install the README described failed: PyYAML 6.0.3 publishes no Windows wheel for Python 3.15, and building its C extension needs a compiler that an ordinary user's machine does not have. What failed was the install a user would follow, not the code.

Both tools declare `requires-python = ">=3.8"`. On 2026-10-11 their unit tests, with install tests, were run on CPython 3.8.20 installed by manage-python, on Linux and on Windows. They passed on Windows. On Linux the install tests failed until they made their virtual environments with symbolic links, as `python -m venv` does: python-build-standalone's 3.8 finds its `libpython` relative to the interpreter, so a copied interpreter cannot start. Nothing in the tools' code needed to change.

## Decision

A tool without an end-to-end scenario is verified on a platform by a verification run. The run takes place in a clean environment restored from a snapshot, as an ordinary user who is not an administrator, with the Python that manage-python installs on that platform, and on one commit, the commit under test. It has three parts, and passes only if all three pass.

### The unit tests

- The tool's unit tests pass from a checkout of the commit under test, with their install tests switched on, and `uc-automa check` passes on the repository itself.
- This part runs twice: with manage-python's default Python, and with the oldest Python the tool's `requires-python` allows, also installed by manage-python. Today that is 3.8. The other two parts run with the default Python only.
- The record names each Python by its full version and build, since an end-of-life line may be installable only as a pinned build: manage-python installs 3.8 as `3.8.20+20241002`, the last python-build-standalone build of 3.8.

### An offline install from wheels

- The wheels are those a release of the commit under test would publish, built by the release's wheel step <a id="cite-steel-2026d"></a>[(Steel, 2026d)](#ref-steel-2026d): from the commit's tree, never from a working tree, with `SOURCE_DATE_EPOCH` set to the commit's time and the build tools pinned. They are built once, on the machine that releases the tool, and every platform installs those same files.
- Each Vishpala tool it depends on comes from that tool's signed release, as in a release.
- PyYAML is built from its source distribution as pure Python, `py3-none-any`, and the run fails if the wheel carries another tag or any compiled file.
- In a fresh virtual environment, `pip install --no-index --find-links <wheels> --require-hashes -r requirements-offline.txt` installs the tool from those wheels alone, as the README's offline install does.
- The install runs inside a network cut that lets only the host's control connection through, with the same conditions as the end-to-end scenario's offline step: probes that work before the cut, the cut re-proven at the end of the step, and the IPv6 internet path reported as verified, blocked or not testable on that network.
- The record lists each wheel with its SHA-256. A release publishes only wheels whose sums match the record (uc-automa 0028).

### The installed tool does its job

Still inside the cut, the installed command, not the checkout's, does its main job on a real repository and reports success:

| Tool | The job |
| --- | --- |
| uc-automa | `uc-automa check` on uc-automa at the commit under test conforms |
| uc-portage | `uc-portage plan`, with the offerings in uc-automa's `offerings/` as the source and uc-automa as the target, both at a recorded uc-automa commit, reports nothing to sync and no conflict |

A job that reads another repository reads it at a commit fixed before the run starts, given to the run by its full hash and named in the record, never at a branch tip resolved during the run. The job can then be repeated exactly, and a change in that repository cannot change the result of a run of this one. A later run may use a later commit, and records it.

A tool added later names its job by amending this table.

### The record

The run writes its record in the verified tool's own repository, under `tests/e2e/<platform>/`, named `YYYY-MM-DD--<platform>-verification-run.md`. It names the commit under test, any other repository's recorded commit, the platform, each Python and the user, gives each part's result, and states `Result: passed` only when all three pass, so `uc-automa release bump` reads it as it reads an end-to-end scenario's record. Account names, computer names and network addresses are replaced by placeholders.

A platform where the IPv6 internet path could not be tested is not marked verified until the run is repeated on a network with IPv6, as for the end-to-end scenario's network cut.

### Scope

This decision adds to uc-automa 0011 and changes nothing in it. Every OSAT manager keeps its end-to-end scenario. A tool that gains an end-to-end scenario later is verified by that scenario instead, and leaves the table here.

## Alternatives considered

**Unit tests alone.** Rejected. On 2026-10-11 they passed on Windows while the documented install could not succeed there. Verification has to include the install a user follows.

**An end-to-end scenario for each tool.** Not now. The unit tests already run every command in-process; what they do not show is the tool installed by an ordinary user and running from that install, which the second and third parts cover with less to maintain. A tool may still gain a scenario, which then takes over.

**Criteria in each README.** Rejected. Two READMEs carrying the same criteria drift apart, and a README cannot be cited the way a decision is. The READMEs link here instead.

**Installing from the package index during the run.** Rejected. It verifies the index and the network on the day of the run, not what a release carries, and on Windows with Python 3.15 it needs a compiler for PyYAML. The offline install shows that the wheels alone are enough.

**Raising `requires-python` instead of testing the oldest Python.** Not now. 3.8 reached its end of life in October 2024 and 3.9 in October 2025, so a raised floor would be 3.10. Raising it means a change to `requires-python` in each tool and a changelog entry, and removes no code: neither tool branches on the Python version, and only newer syntax, such as `list[str]` for `typing.List`, would become available. Testing 3.8 costs one more run of the unit tests and the pinned build above. Either is cheap; a tool that raises its floor tests the new one.

**Every part on the oldest Python.** Rejected. The offline install and the job exercise the installed tool, which the unit tests on the oldest Python already import and run; the oldest Python adds the risk of syntax and standard-library differences, which the unit tests catch.

## Consequences

- The READMEs of uc-portage and uc-automa replace their Windows criteria with a link to this decision, and their platform tables report verification runs.
- The install tests of uc-portage and uc-automa make their virtual environments with symbolic links outside Windows, as `python -m venv` does.
- The Windows driver changes: it builds wheels on the host by the release's wheel step from the commit under test rather than from the release tag; runs the unit tests a second time on the oldest Python; takes uc-automa's commit for uc-portage's job; writes a `Result:` line; and writes a record into each verified repository. Where the driver lives is decided separately.
- The Windows run of 2026-10-11 met the Windows criteria the READMEs carried that day, but its record is in osat-manager-restic, built the wheels from the v0.1.0 tags, and has no `Result:` line, so it does not count as a verification run under this decision. The next run does.
- Linux needs a verification run too: the Linux status of uc-portage and uc-automa today reports unit tests only.
- macOS needs Apple hardware, as for the end-to-end scenario.

## Open questions

- [ ] Where the Windows driver lives, and whether the Linux verification run uses the same driver.

## References

<a id="ref-steel-2026a"></a>Steel, C. (2026a). *Decision: Three platforms for 1.0.0* (Version 0.1.0) [Decision record]. uc-automa 0011. https://github.com/steelcj/uc-automa/blob/main/en-ca/docs/decisions/0011--three-platforms-for-1-0-0-v0.1.0.md [↩](#cite-steel-2026a)

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Decision: Release ceremony* (Version 0.1.0) [Decision record]. uc-automa 0026. https://github.com/steelcj/uc-automa/blob/main/en-ca/docs/decisions/0026--release-ceremony-v0.1.0.md [↩](#cite-steel-2026b)

<a id="ref-steel-2026c"></a>Steel, C. (2026c). *Windows test run, 2026-10-11* [Test record]. osat-manager-restic. https://github.com/steelcj/osat-manager-restic/blob/main/tests/e2e/windows/2026-10-11--windows-test-run.md [↩](#cite-steel-2026c)

<a id="ref-steel-2026d"></a>Steel, C. (2026d). *Decision: Wheels with each release* (Version 0.1.0) [Decision record]. uc-automa 0028. https://github.com/steelcj/uc-automa/blob/main/en-ca/docs/decisions/0028--wheels-with-each-release-v0.1.0.md [↩](#cite-steel-2026d)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-11 | Accepted | Initial version |

## License

This document, *Decision: Verification Without an End-to-End Scenario*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
