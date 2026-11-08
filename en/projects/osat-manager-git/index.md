---
title: "osat-manager-git"
description: "Project to build osat-manager-git, the second manager built by the OSAT manager process: conda-forge's precompiled git on Linux, macOS and Windows, installed into user space from reviewed lock files and checked against a baseline contract."
date: 2026-10-21
lang: en-CA
tags:
  - project
  - osat-manager
  - git
dc:
  identifier: "urn:uuid:73f941dd-4bde-457e-81b9-9d6447baae54"
  title: "osat-manager-git"
  creator: "Christopher Steel"
  publisher: "Vishpala"
  date: 2026-10-21
  language: en-CA
  type: Text
  format: text/markdown
  rights: "CC BY 4.0"
  license: "https://creativecommons.org/licenses/by/4.0/"
sat:
  version: "0.2.0"
  status: provisional
  project: uc-automa
project:
  slug: osat-manager-git
  status: active              # planned | active | done | abandoned
  implements:
    - "osat-manager-git 0001, Decision: Build manage-git (urn:uuid:19425b6e-28ad-4d57-b7c1-dd4d56a7c06c)"
  scope:
    - osat-manager-git
    - uc-radar
    - the shared manager package (uc-automa 0024)
  date_started: 2026-10-21
  date_finished:
---

# osat-manager-git

This project builds `manage-git`, which installs git into a user's own account on Linux, macOS and Windows, keeps several versions side by side, and tells other managers whether git meets a baseline contract. It follows [Creating an OSAT Manager Repository](../../docs/guides/new-repository/creating-an-osat-manager-repository-v0.6.0.md), version 0.6.0, stage by stage. It is the second manager built that way, after osat-manager-restic.

Status: Active. Drafted with AI assistance (Claude Opus 5.5, Anthropic) on 2026-10-21 and provisional until Christopher Steel confirms it. Version 0.2.0 records his choice of the same day to use conda-forge's precompiled git on Windows as well.

## Where things stand

- **The earlier scoping.** Two drafts from 2026-09-30, a process overview and *Universal Cake Requirements: Add Document Slice*, are kept in osat-manager-git under `en-ca/docs/references/` as superseded. Their baseline contract, the requirement areas (ID, ML, SEC, AL, GIT) and en-ca and fr-ca messages still stand. Their build sequence does not: installing through apt, dnf, Homebrew and winget breaks the manager contract, which allows no system package manager and no elevated privilege.
- **Windows.** The radar entry *Git on Windows, Options for osat-manager-git* (uc-radar, 2026-10-11) recommends MinGit from Git for Windows releases for Trial. Christopher Steel chose conda-forge instead on 2026-10-21, so the manager has one source kind on every platform. Version 0.2.0 of the entry records that choice: conda-forge git in Trial, MinGit in Assess as the fallback, dugite-native in Hold. It restates its four questions, line endings, Git LFS, inherited system configuration and paths, for the conda-forge package.
- **Linux and macOS.** That entry left dugite-native as the candidate. It needs glibc 2.34, links the system's libcurl, and repackages builds made for GitHub Desktop. conda-forge is used instead.
- **The repository.** osat-manager-git has base files from uc-automa's offerings, decision 0001, a `manager.yaml`, and a skeleton in which `manage-git --check` works, merged on 2026-10-21. Its first commit predates this process and holds the 2026-09-30 drafts; Christopher Steel chose to build on it rather than restart the history, and the drafts are kept under `en-ca/docs/references/` as superseded.
- **Prior art.** mise's conda backend already installs conda-forge packages without conda, solving, verifying and relocating them through the rattler library. See the radar entry *Universal Cake Evaluation: mise-en-place*, drafted alongside this plan. On 2026-10-21 mise 2026.10.17 installed conda-forge git 2.56.0 on Linux: 26 packages, 55 MB downloaded, 255 MB installed, relocated and working. It locked `win-64` with the SHA-256 checked by hand and could not solve `win-arm64`, which its backend does not map.

## Sources proposed

| Platform | Source | Why |
| --- | --- | --- |
| Linux, x86_64 and aarch64 | conda-forge `git`, subdirs `linux-64` and `linux-aarch64` | Built from the kernel.org source tarball, with its SHA-256 pinned in the recipe. Needs glibc 2.17 or later, so it runs on far older systems than dugite-native |
| macOS, x86_64 and arm64 | conda-forge `git`, subdirs `osx-64` and `osx-arm64` | Same recipe; needs macOS 11 or later |
| Windows, x64 and ARM64 | conda-forge `git`, subdirs `win-64` and `win-arm64` | One source kind and one verification path on every platform. The package is Git for Windows repackaged, about 121 MB with Git Bash, self-contained, with no dependencies and no binary placeholders. MinGit would be smaller and one link shorter, and was the radar entry's recommendation |

The principle for later managers: take upstream's own signed binaries when they exist, as restic publishes them, and use conda-forge when upstream publishes no portable binaries for every platform. git is an exception by choice: Git for Windows signs its releases, but one source on all three platforms keeps the manager and its review simpler.

## What conda-forge publishes for git

Read from the anaconda.org API and from `linux-64/git-2.56.0-pl5440h3795e67_0.conda`, downloaded and unpacked on 2026-10-21, and from the same package installed by mise on Linux.

- **Version.** 2.56.0, build 0, uploaded 2026-09-29 for `linux-64`, `linux-aarch64`, `linux-ppc64le`, `linux-riscv64`, `osx-64`, `osx-arm64`, `win-64` and `win-arm64`.
- **Format.** A `.conda` file: a zip holding `pkg-…tar.zst` and `info-…tar.zst`. Recent builds come in this format only. Python's standard library reads zstd only from 3.14, through `compression.zstd`.
- **Dependencies.** On `linux-64`, nine direct runtime dependencies: `__glibc >=2.17`, `libcurl`, `libexpat`, `libgcc`, `libiconv`, `libzlib`, `openssl`, `pcre2` and `perl 5.*`. More come in transitively (krb5, libssh2, libnghttp2, c-ares, zstd and others; not counted). macOS adds `libintl`. `win-64` and `win-arm64` declare none.
- **Windows package.** `win-64/git-2.56.0-h57928b3_0.conda`, downloaded on 2026-10-21, its SHA-256 matching repodata: 120,811,595 bytes, 9,612 files, all under `Library/` but two under `Menu/`. `Library/cmd/git.exe` is present. One text file, `Library/etc/profile.d/env.sh`, carries the build-prefix placeholder; no binary does, so relocation on Windows is a single text substitution in a Bash profile script.
- **Relocation.** `info/has_prefix` lists 32 files that contain the build prefix, 19 text and 13 binary, among them `bin/git` and `bin/git-shell`. They must be rewritten for the install location, and binary placeholders padded with null bytes. On macOS arm64, a patched binary must be re-signed ad hoc or it will not run.
- **Verification.** Each file's SHA-256 and MD5 are published in the channel's repodata and API, over HTTPS. The packages carry no signature. Whether conda-forge publishes Sigstore attestations under CEP 27, which prefix.dev's channels support in public beta, was not established.
- **Licence metadata.** The recipe labels git `GPL-2.0-or-later and LGPL-2.1-or-later`. Git is GPL-2.0-only, as the Windows entry verified from Git's own `COPYING`. `manager.yaml` records `GPL-2.0-only`, and the mislabel is worth reporting to the git-feedstock.

## What manage-git needs that manage-restic does not

1. **Reading zstd.** See decision D1 below.
2. **A fixed set of packages.** The manager cannot solve dependencies at runtime and still stay small and reviewable. It is resolved when the manager is released instead. For each git version and platform, a lock file records every package's URL, SHA-256 and size. The manager installs exactly that set into one prefix per version.
3. **Relocation.** The manager rewrites text and binary prefix placeholders in the standard library, following `info/paths.json`, and refuses any package whose `paths.json` it does not fully understand.
4. **Re-signing on macOS.** On arm64, the patched Mach-O files need an ad hoc signature. That means either running `/usr/bin/codesign`, which breaks the no-shell-commands rule, or writing a signature in Python. This is the riskiest item in the plan.
5. **A weaker trust anchor.** restic and Git for Windows give a signed checksum list or a signed tag. conda-forge gives hashes served over HTTPS. The lock file becomes the trust anchor, reviewed when it changes and signed with the release key (uc-automa 0032).
6. **CA certificates.** conda's `openssl` and `libcurl` look for certificates inside the prefix, so `ca-certificates` must be in the lock. The Linux package's own `etc/gitconfig`, written by the feedstock, points `http.sslCAInfo` and `http.sslCAPath` at that bundle; without it, HTTPS clones fail.
7. **System configuration.** The package's own system configuration stays as delivered, because of item 6 on Linux and macOS. For each version the manager writes its own file outside the prefix, which includes the package's file and then sets the baseline: line endings, `safe.directory`, credential helper, and long paths on Windows. git reads it through `GIT_CONFIG_SYSTEM`, set by launchers and reported by `manage-git --check --json` as each installation's `invocation`, so the managed git never reads another installation's system configuration, the problem the Windows entry found with MinGit. Recorded in decision 0001.
8. **One source kind.** Conda packages on every platform, so `manager.yaml` maps each platform to its subdirs and the location of `git` inside a prefix (`bin/git`, or `Library/cmd/git.exe` on Windows), with platform differences kept in one module.

## Decisions needed from Christopher Steel

D5 was decided on 2026-10-21. D1 to D4 were accepted as recommended on 2026-10-21, when Christopher Steel had the pull request introducing osat-manager-git decision 0001 merged.

| ID | Question | Recommendation |
| --- | --- | --- |
| D1 | How does a standard-library manager read zstd? | Require Python 3.14 or later for manage-git, since manage-python installs it, and use `compression.zstd`. Record this in decision 0001 as a difference from the contract. The alternative is a pure-Python zstd decoder: new, security-critical code that would need independent review, as the OpenPGP verifier did |
| D2 | What anchors trust in conda-forge packages? | A per-version lock file, reviewed and released with the manager and signed with the release key. Check attestations under CEP 27 too, if conda-forge publishes them, and make them required once they are available for every platform |
| D3 | Where does the conda logic live? | In the shared manager package (uc-automa 0024), as a `conda-forge` source kind, so later managers for git-lfs, gh, pandoc, rclone and others differ only in `manager.yaml`. That means building the shared package first, which 0024 already calls for |
| D4 | How does macOS arm64 re-signing work? | Allow one named exception, `/usr/bin/codesign -s - -f` on files the manager has just patched, and record it in 0001. Revisit if a standard-library ad hoc signer proves small enough to review |
| D5 | Windows source | Decided: conda-forge's `win-64` and `win-arm64` packages, not MinGit. The radar entry recommended MinGit |

## Before starting

- [x] D5 decided: conda-forge on Windows.
- [x] D1 to D4 confirmed, by merging decision 0001 in osat-manager-git.
- [x] Change this project's status to Active and fill `date_started`.

## Steps

The stages are those of the process guide, in order, with the shared package built before the repository. Each ends at its gate.

### Assess on the radar

- [ ] Write a uc-radar entry for conda-forge as a binary source for OSAT managers, with git as the worked case. It answers the five questions the process asks, from the facts above.
- [x] Update *Git on Windows, Options for osat-manager-git*: conda-forge chosen over MinGit, and over dugite-native for Linux and macOS. Version 0.2.0.
- [x] Gate: conda-forge git is in Trial.

### Record the decision

- [x] Draft `0001--build-manage-git-v0.1.0.md`. Written directly in the repository, on the review branch, since the repository already existed. It names the tool, the platforms targeted first (Linux x86_64 and aarch64, macOS x86_64 and arm64, Windows x64 and ARM64), and every difference from the contract: D1, D4 and conda-forge on Windows. It names both radar entries.
- [x] Carry over the baseline contract and the requirement areas from the 2026-09-30 drafts, which are kept in the repository as superseded references.
- [x] Gate: the decision record is drafted.

### Build the shared package first (D3)

- [ ] Choose its name and repository, the open consequence of uc-automa 0024. Until then, the conda source kind lives in osat-manager-git as one self-contained module, listed as known debt in decision 0001, so the shared package does not block the manager.
- [ ] Move in from osat-manager-restic the YAML subset reader, the data lookup (uc-automa 0019) and the OpenPGP verifier.
- [ ] Add the `conda-forge` source kind: read a lock, download, check SHA-256 and size, unpack `.conda`, relocate through `paths.json`, and re-sign on macOS arm64.
- [ ] Unit tests offline, against small fake `.conda` packages built in the tests, including placeholders longer than the install path, which must be refused.
- [ ] Independent review of the relocation and re-signing code before any manager depending on it is tagged.

### Create the repository

- [x] The repository already had a first commit holding the drafts. Christopher Steel chose to build on it, so the drafts moved to `en-ca/docs/references/` instead of out of the repository.
- [x] Generate the identifier, write `.osat-manager-git.assets/archive.yaml` and `dc.yaml`, and place the decision record.
- [x] Gate, adapted: the sidecar and the decision record arrive before any manager code.

### Subscribe to uc-automa

- [x] Install uc-automa and uc-portage from their release tags, `uc-automa init --repository osat-manager-git --layout osat-manager`, `offerings plan`, `offerings apply`, commit.
- [x] Gate: `uc-automa offerings plan` reports nothing to do, and `uc-automa check` conforms.

### Describe the managed tool

- [x] Write `manager.yaml`, covering the conda-forge channel and all six subdirs, the lock file per version, the licence `GPL-2.0-only`, aliases `git` and `git-{major}.{minor}`, install roots under `osat/git`, and the baseline.
- [ ] Write a release-time tool, outside the runtime manager and allowed more than the standard library, that resolves the package set for each git version and platform into the lock. It runs the solve with rattler or micromamba, then cross-checks each hash against the anaconda.org API.
- [ ] Gate: no placeholders left; every lock entry has URL, SHA-256 and size.

### Implement the manager

- [ ] The contract: install into user space, versions side by side, switching, aliases, protection, nothing left behind, a verified archive kept with its lock, self-install.
- [x] `manage-git --check`: report each installation against the baseline as JSON, which is what other managers call, with each managed installation's `invocation`.
- [x] Messages from a catalogue, en-ca and fr-ca first.
- [ ] The four Windows questions, made and recorded for the conda-forge package: autocrlf (proposed `false` in the baseline), Git LFS (the Windows package ships `git-lfs.exe`; on Linux and macOS a git-lfs companion from conda-forge is the natural fix), inherited configuration (handled by `GIT_CONFIG_SYSTEM`, recorded in 0001; `%PROGRAMDATA%\Git\config` still to test on Windows), and aliases targeting `Library\cmd\git.exe` (recorded in 0001). The credential helper replacing `helper-selector` is still to name.
- [ ] Gate: `tests/unit/` passes offline.

### Test on each platform

- [ ] Linux: the scenario through uc-test-platform in an Incus container restored to a clean snapshot, on amd64, then arm64.
- [ ] Windows: the scenario over SSH in the Windows 11 virtual machine, on x64; ARM64 needs ARM hardware.
- [ ] macOS: on Apple hardware, which is not yet available. It stays Not yet verified until then.
- [ ] Every run also clones over HTTPS, which proves the certificates and libcurl in the prefix work.
- [ ] Gate: every platform is verified or has a stated reason.

### Document and release

- [ ] README with the platform status table, `using-manage-git-v0.1.0.md`, ROADMAP, CHANGELOG, `uc-automa docs index`; `uc-automa check` passes.
- [ ] 0.1.0 through the release ceremony if uc-automa 0.2.0 has shipped it, otherwise tagged by hand with approval.

### Register

- [ ] Link the manager from both radar entries and from the list of OSAT managers, wherever that list is kept (still open in the process guide).

## Later managers that conda-forge could serve

Latest version on conda-forge, as listed by the anaconda.org API on 2026-10-21. A tool whose upstream already signs its binaries keeps upstream as its source.

| Tool | Version | Licence (as labelled) | Platforms | Note |
| --- | --- | --- | --- | --- |
| git-lfs | 3.8.0 | MIT | Linux, macOS, Windows x64 and ARM64 | A companion to manage-git |
| gh | 2.102.1 | Apache-2.0 | Linux, macOS, Windows x64 and ARM64 | Release publishing, see the release-publishing radar entries |
| pandoc | 3.12.1 | GPL-2.0-or-later | Linux, macOS, Windows x64 | Document conversion; no Windows ARM64 |
| rclone | 1.75.2 | MIT | Linux, macOS, Windows x64 | Resilience Pack, beside restic |
| age | 1.3.2 | BSD-3-Clause | Linux, macOS, Windows x64 and ARM64 | File encryption |
| typst | 0.15.1 | Apache-2.0 | Linux, macOS, Windows x64 and ARM64 | Document typesetting |
| hugo | 0.167.0 | Apache-2.0 | Linux, macOS, Windows x64 and ARM64 | Static sites |
| nodejs | 26.10.0 | MIT | Linux, macOS, Windows x64 and ARM64 | Eleventy and other site tooling |
| ripgrep | 15.2.0 | MIT | Linux, macOS, Windows x64 and ARM64 | Search |
| restic | 0.19.1 | BSD-2-Clause | Linux, macOS, Windows x64 | Already managed from restic's signed releases; conda-forge would be weaker |
| jq, gnupg, openssh | 1.8.2, 2.5.24, 8.7p1 | various | Linux and macOS only | No Windows build, so not a three-platform source |

## Risks

- macOS arm64 re-signing may not be doable in the standard library at a size worth reviewing, which leaves D4's exception in place.
- On Windows, conda-forge adds a link to the chain between Git for Windows and the user, can lag Git for Windows' own patch releases, and costs about 121 MB per archived version. Its 9,612 files also need a short install root, since long paths are not assumed.
- A transitive dependency's build can change under the same version, so a lock is valid only for the exact builds it names. Refreshing it is a reviewed change.
- conda-forge's git can lag upstream. A security fix reaches users only after the feedstock rebuilds and the lock is refreshed.
- Perl comes with git on Linux and macOS as a sizeable extra dependency. With icu, krb5 and the rest, the Linux prefix is 255 MB from 55 MB of packages (measured through mise on 2026-10-21). Dropping perl would break `git send-email`, `git svn` and other Perl commands.
- A managed git started without `GIT_CONFIG_SYSTEM`, by a program that finds the executable some other way, reads only the package's configuration, without the baseline.
- `win-arm64` has no working reference implementation: mise's conda backend maps only `win-64`.
- If conda-forge ends anonymous access to anaconda.org or changes the `.conda` format, the verified archive still restores installed versions offline, but new versions stop until the source changes.

## Finishing

- [ ] Record completion in the changelog of the decision this project carries out.
- [ ] Change this project's status to Done and fill `date_finished`.

Questions that come up while the project runs and need a lasting answer become new decision records, linked from here, rather than notes in this file.

## Changelog

| Version | Date | Status | Changes |
| --- | --- | --- | --- |
| 0.2.0 | 2026-10-21 | Active | conda-forge on Windows as well (D5 decided), one source kind; Windows package facts; steps done in osat-manager-git checked off; D1 to D4 accepted with decision 0001; the radar entry updated; the system configuration kept and included by a manager-owned file, after mise showed the Linux package's file holds the certificate paths; Linux size measured; the `win-arm64` gap |
| 0.1.0 | 2026-10-21 | Planned | First draft: conda-forge for Linux and macOS, MinGit for Windows, five decisions with recommendations, steps by process stage, later conda-forge candidates |

## Licence

This document is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Drafted with AI assistance (Claude Opus 5.5, Anthropic) and to be reviewed by the maintainer.
