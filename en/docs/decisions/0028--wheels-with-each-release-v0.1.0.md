---
title: "Decision: Wheels With Each Release"
dc:title: "Decision: Wheels With Each Release"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "release, publish, wheels, PyYAML, SHA256SUMS, offline install, reproducible builds, verification, SSH signatures"
dc:description: "Adds a step to uc-automa release publish: every release of a Python tool carries its own wheel and the wheels of everything it depends on, built twice from pinned sources with pinned build tools, refused unless their sums match the verification record of the release commit, and listed in a hash-pinned requirements file and in SHA256SUMS, both signed with an SSH key that Windows, macOS and Linux can check without gpg."
dc:date: "2026-10-11"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:02eec912-6fb4-43f6-9a5d-db7b49e6e03c"
dc:relation:
  - "urn:uuid:a7667fcc-3e79-40d1-961a-35bd390b4137"
  - "urn:uuid:3b8c02de-92e2-4e89-8efb-022e545075ac"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: Wheels With Each Release

Version: 0.1.0
Status: Accepted

## Context

`uc-automa release publish` attaches to each release an archive of the tag's tree, the release notes, `SHA256SUMS` and its OpenPGP signature <a id="cite-steel-2026a"></a>[(Steel, 2026a)](#ref-steel-2026a). Installing uc-automa still means fetching uc-portage and PyYAML from the network at install time, and on Windows with Python 3.15 PyYAML has no wheel, so pip builds it from source <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b). The verification run installs from wheels with `pip install --no-index` <a id="cite-steel-2026c"></a>[(Steel, 2026c)](#ref-steel-2026c); a user cannot do the same until releases carry those wheels.

On 2026-10-11, wheels for uc-portage 0.1.0, uc-automa 0.1.0 and PyYAML 6.0.3 were each built twice from fixed sources on one machine. Without `SOURCE_DATE_EPOCH` every pair differed; with it set, every pair was byte-identical. Built in two separate fresh environments holding only a pinned setuptools, with build isolation off, PyYAML and uc-automa again gave identical bytes, and PyYAML built as pure Python without Cython. Two things in a wheel tie it to its build: the version, which comes from `VERSION`, and the build backend's own version, which setuptools writes into the wheel's `WHEEL` file.

Windows has no gpg. On the same day, the clean Windows test snapshot's own OpenSSH client, `OpenSSH_for_Windows_9.5p2`, ran `ssh-keygen -Y verify` <a id="cite-openbsd-nd"></a>[(OpenBSD, n.d.)](#ref-openbsd-nd) on a file signed on Linux: it accepted the signature and refused a tampered file, a signature by another key and a signature made for another namespace. A refusal sets `ERRORLEVEL` to -1 in Command Prompt, which `if errorlevel 1` does not catch: a first draft of the steps below used it, and pip installed after a refused signature. Comparing `%ERRORLEVEL%` with 0, on a line of its own after the check, stopped the install in both bad cases on Windows, as `if ... then ... fi` did on Linux.

manage-python marks each Python it installs as externally managed, so pip refuses to install into it, on Linux and on Windows alike, and points to a virtual environment instead.

## Decision

`uc-automa release publish` gains a step between building the archive and writing the checksums, for a tool verified by a verification run (uc-automa 0027). A tool verified by an end-to-end scenario, such as an OSAT manager, installs itself from its checkout and carries no wheels.

### Pins

Everything the step downloads is pinned in the repository, in `[tool.uc-automa.release]` in `pyproject.toml`, by project, exact version and the SHA-256 of the file downloaded, in pip's hash form:

```toml
[tool.uc-automa.release]
build-tools = ["setuptools==X.Y.Z --hash=sha256:<sum of the wheel>"]
sources = ["PyYAML==6.0.3 --hash=sha256:d76623373421df22fb4cf8817020cbb7ef15c725b9d5e45f17e189bfc384190f"]
```

`build-tools` pins the build backend and anything else the builds need; `sources` pins each third-party dependency's source distribution. The PyYAML sum is the one PyPI publishes for `pyyaml-6.0.3.tar.gz`. A download that does not match its pin is refused. A pin is changed by a commit, never at publish time.

### Build the wheels twice and compare

- **The build environment** is a fresh virtual environment holding only the pinned build tools, installed from their pinned files. Every build runs in it with build isolation off, so nothing is resolved at build time.
- **The tool's own wheel** is built from the tag's tree, extracted from `git archive`, never from the working tree, with `SOURCE_DATE_EPOCH` set to the time of the tag's commit.
- **Each Vishpala tool it depends on** is taken from that tool's own published release, not rebuilt: the highest released version its dependency range allows, downloaded with that release's `SHA256SUMS` and signature, and refused unless the signature verifies against the release key and the checksum matches. uc-automa 0.2.0's release thus carries uc-portage's wheel exactly as uc-portage released it.
- **Each third-party dependency** is built from its pinned source distribution, with the same `SOURCE_DATE_EPOCH`. PyYAML is built with `--no-binary pyyaml` and `PYYAML_FORCE_LIBYAML=0`, and refused unless the wheel is tagged `py3-none-any` and holds no compiled file.
- Every wheel the ceremony builds is built twice in the run, and any byte difference stops the release. Identical bytes across different machines and toolchains are not claimed.

### Match the verification record

- Publishing is refused unless the repository holds a passing verification record whose commit under test is the tag's commit, and every wheel the release would carry has the SHA-256 that record lists for it. Below 1.0.0 one platform's record is enough; from 1.0.0 the release needs one for each of Linux, Windows and macOS, all listing the same sums.
- The verification run of a release therefore takes place between `uc-automa release cut` and `uc-automa release publish`, on the release commit, with wheels built by this step where the release will be published. A run on the commit before the cut cannot match, because the cut changes `VERSION` and the version is inside every wheel.
- The records are read from the current branch, under `tests/e2e/<platform>/`, since a record written after the tag is not in the tag's tree.
- A mismatch stops the release. The remedy is a new verification run with wheels built where the release is published, not a change to the record.
- The release tag stays local until the verification run passes. The run serves the README's online install from local mirrors holding the tag (uc-automa 0027), so nothing is pushed first. Only after the run passes are `main` and the tag pushed, `git push origin main vX.Y.Z`, and the release published.
- A release commit that fails verification is never pushed or published. Its tag and the release commit were never public, so they are removed and the version cut again once the fault is fixed. A pushed tag is never reused.

### The release commit updates the README's install tag

This changes the cut of uc-automa 0026. The directive `release/readme-install-tag` requires `README.md` to install the repository at `v` and its `VERSION`, so the release commit must change that tag with `VERSION`. After rolling the changelog, `uc-automa release cut` rewrites each reference in `README.md` that installs the repository's own release, `/<repository>@v<old>` or `/<repository>.git@v<old>`, to the new version, and commits `README.md` with `VERSION` and `CHANGELOG.md`, and nothing else. It reads the references exactly as the directive's check does, and after the commit that check must pass. A README with no such reference is left untouched.

### Publish them with their sums

- The wheels are attached to the release beside the archive, and written beside it by the plain-directory backend.
- `requirements-offline.txt` names each wheel's project and exact version with its SHA-256, in pip's hash-checking form, so pip checks every wheel itself, on every platform: `uc-automa==0.2.0 --hash=sha256:<sum>`.
- `SHA256SUMS` lists the archive, the release notes, every wheel and `requirements-offline.txt`, and is signed with OpenPGP as uc-automa 0026 describes.
- The release notes name each wheel's source: the tag, the dependency's release, or the pinned source distribution.

### SSH signatures

- The release also carries SSH signatures, made with `ssh-keygen -Y sign` in the namespace `vishpala-release`: `SHA256SUMS.sig` over `SHA256SUMS`, and `requirements-offline.txt.sig` over `requirements-offline.txt`. The second lets an install check the signature and then let pip check every wheel, with no sums compared by hand.
- The SSH release key is an Ed25519 key that Christopher Steel creates and holds, as he holds the OpenPGP key. The ceremony never creates, imports or stores a key; it signs with the SSH key it is given, and refuses `--sign` when there is none.
- The key's public half is published as an allowed-signers line, `chris.steel@gmail.com namespaces="vishpala-release" ssh-ed25519 <key>`, in the same independent places as the OpenPGP fingerprint.
- OpenPGP stays: release tags are signed with it, and uc-automa 0026 keeps uc releases verifiable by the verifier manage-restic uses.

### Install offline, in the README

Each such tool's README gains a section in this form, shown here for uc-automa:

```markdown
### Install offline

Each release carries uc-automa's wheel and every wheel it needs, uc-portage's and a pure-Python PyYAML, with `requirements-offline.txt` and its signature `requirements-offline.txt.sig`. Download them all from the release page into one directory, and save the release key's allowed-signers line in that directory as `allowed-signers`. Then, in that directory, on Linux or macOS:

~~~sh
python3 -m venv .venv
if ssh-keygen -Y verify -f allowed-signers -I chris.steel@gmail.com -n vishpala-release -s requirements-offline.txt.sig < requirements-offline.txt
then .venv/bin/python -m pip install --no-index --find-links . --require-hashes -r requirements-offline.txt
else echo "The signature did not verify: nothing was installed."
fi
.venv/bin/uc-automa --version
~~~

On Windows, in Command Prompt:

~~~bat
python -m venv .venv
ssh-keygen -Y verify -f allowed-signers -I chris.steel@gmail.com -n vishpala-release -s requirements-offline.txt.sig < requirements-offline.txt
if %ERRORLEVEL% neq 0 (echo The signature did not verify: nothing was installed.) else (.venv\Scripts\python -m pip install --no-index --find-links . --require-hashes -r requirements-offline.txt)
.venv\Scripts\uc-automa --version
~~~

pip installs only if `ssh-keygen` reports a good signature, which it does only if the requirements file is the one released. pip then checks every wheel against it, refuses any that differs, and installs nothing from the network. uc-automa is installed in the virtual environment `.venv`, because the Python manage-python installs does not accept packages. In Command Prompt the check compares `%ERRORLEVEL%` with 0 on its own line: a refused signature sets it to -1, which `if errorlevel 1` would miss. To check every file the release carries, verify `SHA256SUMS.sig` over `SHA256SUMS` the same way and compare the sums, or use `SHA256SUMS.asc` with gpg.
```

### Tests

Offline, with the `dir` backend: the wheels, `requirements-offline.txt` and both SSH signatures are published, and every file is listed in `SHA256SUMS`; the determinism gate stops a release whose two builds differ; a download that does not match its pin is refused; a PyYAML wheel with another tag or a compiled file is refused; a dependency's wheel whose signature or checksum fails is refused; a release with no verification record for the tag's commit, or with a sum that differs from it, is refused; the cut rewrites the README's install tag and the release commit passes `release/readme-install-tag`; `ssh-keygen -Y verify` accepts the published signatures; and the README's commands install from the published directory into a fresh virtual environment, and install nothing when the requirements file or its signature has been altered.
## Alternatives considered

**Publish to a package index.** Not now, as uc-automa 0026 recorded. A release page can hold wheels without one, and an index is a separate decision.

**Rebuild each Vishpala dependency instead of taking its release.** Rejected as the default. Two builds of one version on different machines are not claimed identical, so a rebuilt uc-portage wheel could differ from the one uc-portage released. Taking the signed release keeps one wheel per version. A rebuild compared with the release is a possible later check.

**Let pip build PyYAML on the user's machine, as the README does today.** Kept as the online install, but not for offline install: building needs setuptools from the network, and the result differs from machine to machine.

**Build with pip's build isolation.** Rejected. pip would fetch the newest build backend the range allows, and its version is written into every wheel, so a wheel built for the verification run and one built at publish time could differ.

**Verify before the cut.** Rejected. The cut writes the new version into `VERSION`, and from there into every wheel, so only the release commit can be verified with the wheels it publishes.

**`SHA256SUMS` alone, without a requirements file.** Rejected. Windows has no `sha256sum`, and comparing sums by eye is unreliable. pip's hash-checking mode compares them on every platform.

**OpenPGP alone, with a gpg-free verifier in the release.** Rejected. A verifier delivered with the release it verifies proves nothing about that release, and gpg is not part of Windows. `ssh-keygen` is part of Windows, macOS and Linux.

**SSH signatures in place of OpenPGP.** Not now. Release tags and manage-restic's verifier use OpenPGP, so replacing it changes uc-automa 0026 and is a decision of its own.

## Consequences

- Ships with the release ceremony in uc-automa 0.2.0. uc-portage 0.2.0 is released first, so uc-automa 0.2.0's release can take its wheel.
- Every release of such a tool needs a verification run on its release commit, on at least one platform, before it can be published; before this decision only 1.0.0 needed any.
- The 1.0.0 gate of `uc-automa release bump` reads records of commits before the cut; the 1.0.0 release itself then needs its own three records before it is published.
- A release is published from the machine that built its verification wheels.
- Publishing needs network access for the dependencies' releases, the pinned source distributions and the pinned build tools, on the releasing machine only.
- Christopher Steel creates the SSH release key before the first release that carries wheels, and its allowed-signers line is published with the OpenPGP fingerprint.
- The verification run of uc-automa 0027 builds its wheels with this step.

## Open questions

- [ ] Which two or more independent places publish the OpenPGP fingerprint and the SSH allowed-signers line, carried over from uc-automa 0026.

## References

<a id="ref-openbsd-nd"></a>OpenBSD. (n.d.). *ssh-keygen(1)* [Manual page]. https://man.openbsd.org/ssh-keygen [↩](#cite-openbsd-nd)

<a id="ref-steel-2026a"></a>Steel, C. (2026a). *Decision: Release ceremony* (Version 0.1.0) [Decision record]. uc-automa 0026. https://github.com/steelcj/uc-automa/blob/main/en-ca/docs/decisions/0026--release-ceremony-v0.1.0.md [↩](#cite-steel-2026a)

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Windows test run, 2026-10-11* [Test record]. osat-manager-restic. https://github.com/steelcj/osat-manager-restic/blob/main/tests/e2e/windows/2026-10-11--windows-test-run.md [↩](#cite-steel-2026b)

<a id="ref-steel-2026c"></a>Steel, C. (2026c). *Decision: Verification without an end-to-end scenario* (Version 0.1.0) [Decision record]. uc-automa 0027. https://github.com/steelcj/uc-automa/blob/main/en-ca/docs/decisions/0027--verification-without-an-end-to-end-scenario-v0.1.0.md [↩](#cite-steel-2026c)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-11 | Accepted | Initial version |

## License

This document, *Decision: Wheels With Each Release*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
