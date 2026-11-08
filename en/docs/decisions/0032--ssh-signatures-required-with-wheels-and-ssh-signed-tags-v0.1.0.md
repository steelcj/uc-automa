---
title: "Decision: SSH Signatures Required With Wheels, and SSH-Signed Tags"
dc:title: "Decision: SSH Signatures Required With Wheels, and SSH-Signed Tags"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "release, signatures, SSH, OpenPGP, tags, git, Windows"
dc:description: "Clarifies uc-automa 0028: a release that carries wheels is always SSH-signed, and the signature checked on a dependency's release is its SSH signature, while OpenPGP stays optional as uc-automa 0026 has it. Release tags are signed with the same SSH key in git's namespace, in place of OpenPGP-signed tags, and verified by exit status; for 0.2.0 tag verification is documented for Linux and macOS only, because git hangs verifying SSH signatures on Windows."
dc:date: "2026-10-11"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:a59b7366-f194-4f65-b659-3b2607587b49"
dc:relation:
  - "urn:uuid:a7667fcc-3e79-40d1-961a-35bd390b4137"
  - "urn:uuid:02eec912-6fb4-43f6-9a5d-db7b49e6e03c"
  - "urn:uuid:b330a5f8-e42b-4af0-be3d-5488a7d967b9"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: SSH Signatures Required With Wheels, and SSH-Signed Tags

Version: 0.1.0
Status: Accepted

## Context

uc-automa 0026 allows signatures without requiring them: a release tag is signed "with the release key when one is configured", and `SHA256SUMS.asc` is made by default only when the OpenPGP key is configured, with `--no-sign` to skip it <a id="cite-steel-2026a"></a>[(Steel, 2026a)](#ref-steel-2026a). uc-automa 0028 then refuses a dependency's wheel "unless the signature verifies against the release key", without saying which signature, and its offline install needs the SSH signature `requirements-offline.txt.sig` <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b). A signature is therefore needed in practice, but no decision says so.

On 2026-10-11 an SSH-signed annotated tag was made with git 2.43 and a throwaway key, and checked with `git tag -v`:

- git signs and verifies tags in the SSH namespace `git`. An allowed-signers line limited to `namespaces="vishpala-release"` was refused with "key is not permitted for use in signature namespace "git""; with `namespaces="vishpala-release,git"` the tag verified, exit status 0.
- A tag signed by another key printed `Good "git" signature with ED25519 key ...`, without a principal, and exited with status 1. The message alone is misleading; the exit status is not.
- On the clean Windows test snapshot, MinGit 2.56 hung in `git tag -v` on the same tag, with or without `gpg.ssh.program` set to `C:\Windows\System32\OpenSSH\ssh-keygen.exe`. git's trace showed `ssh-keygen -Y find-principals` finishing and `ssh-keygen -Y verify` never returning. Windows' `ssh-keygen` verified the same signature when the signed data came from a file, exit status 0, and hung when it came from a pipe, even `type payload | ssh-keygen -Y verify ...` in Command Prompt. git always passes the data through a pipe, so no `gpg.ssh.program` path alone avoids the hang.
- A small `sh` wrapper, run by MinGit's own `sh.exe`, that saved the piped data to a temporary file before calling `ssh-keygen -Y verify` or `-Y check-novalidate`, made `git tag -v` work on Windows: exit status 0 for the release key, and 1 with "No principal matched" for another key.
- Christopher Steel will create an SSH release key only for 0.2.0, and no OpenPGP key.

## Decision

### SSH signatures are required with wheels

This clarifies uc-automa 0028.

- A release that carries wheels always carries `SHA256SUMS.sig` and `requirements-offline.txt.sig`, made with the SSH release key in the namespace `vishpala-release`. For such a release, `uc-automa release publish` refuses `--no-sign` and refuses to run without the SSH key.
- The signature 0028 checks on a dependency's release is that release's `SHA256SUMS.sig`, verified with `ssh-keygen -Y verify -n vishpala-release` against the allowed-signers file of uc-automa 0030, followed by the checksum of the wheel.
- OpenPGP stays as uc-automa 0026 has it: `SHA256SUMS.asc` is made when the OpenPGP key is configured, and is never required.
- The `Install offline` section that 0028 shows creates its virtual environment with `python -m venv .venv`, as the READMEs do since 2026-10-11, since `python` is the command manage-python installs on every platform.

### Release tags signed with the SSH key

- `uc-automa release cut` signs the release tag with the SSH release key: `git -c gpg.format=ssh -c user.signingkey=<public key> tag -s`. A git tag carries one signature, so this replaces the OpenPGP-signed tag of uc-automa 0026; the OpenPGP key then signs only `SHA256SUMS`, when configured.
- The allowed-signers line names both namespaces, `namespaces="vishpala-release,git"`, so that one key signs files and tags, and one line is published.
- A tag is verified with `git -c gpg.ssh.allowedSignersFile=<allowed-signers> tag -v vX.Y.Z`, and the result is its exit status, never its message: 0 for a key in the file, anything else otherwise.
- The cut's verify step checks the new tag's signature this way, and `release publish` refuses a tag whose signature does not verify.
- A signed tag is still an annotated tag, so `release/annotated-version-tags` is unchanged.
- For 0.2.0, each README documents tag verification for Linux and macOS only, and states the Windows gap in these words or close to them: "On Windows, `git tag -v` does not finish for SSH-signed tags, because Windows' `ssh-keygen` hangs reading from a pipe. The offline install's signature check does not use tags, and works on Windows."
- With no OpenPGP key for 0.2.0, its releases carry no `SHA256SUMS.asc`, and its tags carry SSH signatures only.

## Alternatives considered

**Keep OpenPGP-signed tags.** Rejected. Windows has no gpg, and MinGit does not bring one; an OpenPGP-signed tag cannot be checked there at all.

**Unsigned tags.** Rejected. The tag is how git users find a release; a signature lets them check it without the release page.

**A separate SSH key for tags.** Rejected. One key in two namespaces means one key to create, hold, publish and rotate.

**Requiring OpenPGP signatures too.** Rejected. Nothing in the install path checks them; requiring them would add a key that every release needs and no reader on Windows can use.

## Consequences

- uc-automa 0030's allowed-signers line gains the `git` namespace.
- The cut needs the SSH release key as well as publish.
- uc-automa 0026 changes for tags: they are signed with the SSH release key, never OpenPGP. The OpenPGP key, once there is one, signs only `SHA256SUMS`.
- For 0.2.0, tag verification is documented for Linux and macOS only, with the Windows gap stated in each README.

## Open questions

- [ ] Whether a later release closes the Windows gap with the file-buffering wrapper above, set as `gpg.ssh.program`, and whether the hang is reported to Win32-OpenSSH.

## References

<a id="ref-steel-2026a"></a>Steel, C. (2026a). *Decision: Release ceremony* (Version 0.1.0) [Decision record]. uc-automa 0026. https://github.com/steelcj/uc-automa/blob/main/en-ca/docs/decisions/0026--release-ceremony-v0.1.0.md [↩](#cite-steel-2026a)

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Decision: Wheels with each release* (Version 0.1.0) [Decision record]. uc-automa 0028. https://github.com/steelcj/uc-automa/blob/main/en-ca/docs/decisions/0028--wheels-with-each-release-v0.1.0.md [↩](#cite-steel-2026b)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-11 | Accepted | Initial version |

## License

This document, *Decision: SSH Signatures Required With Wheels, and SSH-Signed Tags*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
