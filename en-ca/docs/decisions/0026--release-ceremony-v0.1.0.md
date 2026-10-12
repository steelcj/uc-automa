---
title: "Decision: Release Ceremony"
dc:title: "Decision: Release Ceremony"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "release, bump, cut, publish, tags, SHA256SUMS, signing, provider interface"
dc:description: "uc-automa provides the release ceremony as installed commands, release bump, cut and publish, replacing the copied bump-version.py, cut-release.py and publish-release.py: a clean tree and conformance before cutting, archives from the tag's tree, release notes, one RSA release key, and guarded retirement of the old copies."
dc:date: "2026-10-11"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:a7667fcc-3e79-40d1-961a-35bd390b4137"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: Release Ceremony

Version: 0.1.0
Status: Accepted

## Context

Releases in Vishpala's repositories are made by three scripts, copied into each repository from sat-doc-automa <a id="cite-steel-2026a"></a>[(Steel, 2026a)](#ref-steel-2026a):

| Script | What it does |
| --- | --- |
| `bump-version.py` | Writes the next version to `VERSION`, and nothing else |
| `cut-release.py` | Guards, bumps, rolls the changelog's `[Unreleased]` section into a dated version section, commits `VERSION` and `CHANGELOG.md` only, makes an annotated tag, and stops before pushing |
| `publish-release.py` | For a pushed tag, builds the release tarball twice from `git archive` and refuses any byte difference, writes `SHA256SUMS`, optionally signs it, and publishes through a provider interface with `gh` and plain-directory backends |

The publishing design is recorded in uc-radar <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b): connectivity in two layers, git transport for preflight only and the publish channel behind a small interface, which stays honest to its narrowest backend, a plain directory.

The foundation brief deferred porting these scripts to uc-automa 0.2.0, into `lib/uc_automa/release/` <a id="cite-steel-2026c"></a>[(Steel, 2026c)](#ref-steel-2026c). Since then, the directive `release/annotated-version-tags` has made the release tag a checked rule <a id="cite-steel-2026d"></a>[(Steel, 2026d)](#ref-steel-2026d), and uc-portage, uc-automa and osat-manager-restic were released by hand to that rule. Copying scripts into every repository contradicts two of uc-automa's principles: code lives in one installed package (P4), and nothing is copied that can be installed.

## Decision

uc-automa provides the release ceremony as three subcommands of the installed `uc-automa` command, in `lib/uc_automa/release/`. They keep the scripts' division of labour and their refusals, and change only what the newer rules require. No repository holds a copy.

### `uc-automa release bump`

```sh
uc-automa release bump patch|minor|major|X.Y.Z
```

- Writes the next version to `VERSION`, and nothing else, as `bump-version.py` does. Version arithmetic exists in this one place.
- Refuses a version equal to the current one.
- Refuses a bump to 1.0.0 or later unless the repository holds a passing run record for each of Linux, Windows and macOS, under `tests/e2e/linux/`, `tests/e2e/windows/` and `tests/e2e/macos/`, because a tool reaches 1.0.0 only when it is verified end to end on all three (uc-automa 0011). The run records the end-to-end drivers write are the platform record; there is no other format. A run record passes when it states `Result: passed`.
- Never renames documents. Documents carry their own versions; a document's filename loses its suffix when that document reaches 1.0.0 (uc-automa 0002), not when the repository does.

### `uc-automa release cut`

```sh
uc-automa release cut patch|minor|major|X.Y.Z
```

The sequence, each step stopping the ceremony if it fails:

1. **Refuse a dirty working tree.** Any uncommitted change, staged or not, or any untracked file that git does not ignore, stops the ceremony with the message "the working tree is not clean: commit, stash or remove these first", followed by the paths. This comes before everything else, so the release is exactly what is committed.
2. **Guard the release.** The `[Unreleased]` section has content, and no tag exists for the target version, because tags are never reused.
3. **Gate on conformance.** `uc-automa check` passes. This is new: a release is a conforming state of the repository.
4. **Bump**, through the same code as `release bump`.
5. **Roll the changelog.** `## [Unreleased]` becomes `## [X.Y.Z] - YYYY-MM-DD`, dated in local time, with a fresh empty `[Unreleased]` above it. The ceremony writes headings only, never changelog prose. Keep a Changelog's link references are added only when the repository has a remote.
6. **Commit surgically.** `VERSION` and `CHANGELOG.md` only, never everything, with the message `Release X.Y.Z`.
7. **Tag.** An annotated tag `vX.Y.Z` whose message names the repository and the version, such as `uc-automa 0.2.0`, signed with the release key when one is configured.
8. **Verify.** The `release/annotated-version-tags` check passes for the new tag.
9. **Stop before pushing.** Pushing stays a deliberate act: `git push origin main vX.Y.Z`.

### `uc-automa release publish`

```sh
uc-automa release publish [--backend gh|dir] [--target DIR] [--dry-run] [--sign|--no-sign]
```

The sequence carried over from `publish-release.py`:

1. **Guard the tag.** It exists locally, and `VERSION` at the tag matches it.
2. **Transport preflight.** `git ls-remote` confirms the tag is on the remote and points at the same commit as the local tag, comparing the peeled commits. Transport is used for this and nothing else.
3. **Backend detection and preflight**, through the interface `detect(remote_url)`, `preflight()`, `publish(tag, files)` and `release_url(tag)`. The backends are `gh` and `dir`, a local directory, which is also the offline test fixture.
4. **Build the archive twice from the tag's tree and compare.** `<repository>-X.Y.Z.tar.gz` is built by `git archive` from the tree the tag points at, never from the working tree, with gzip's timestamp fixed. Two builds in one run must be byte-identical; this determinism gate is checked every run, not assumed. Identical bytes across different machines and git versions are not claimed.
5. **Release notes.** The changelog's section for the version, read from `CHANGELOG.md` at the tag, is the release notes: attached to the release by backends that have them, and written beside the archive as `release-notes.md` by the plain-directory backend.
6. **Checksums.** `SHA256SUMS` lists the archive and, where it is written as a file, `release-notes.md`.
7. **Signature.** A detached OpenPGP signature over `SHA256SUMS`, `SHA256SUMS.asc`, as restic publishes its releases, made with the release key. `--sign` requires it, `--no-sign` skips it, and by default it is made when the release key is configured.
8. **Publish**, then report the release URL.

A release is what the narrowest backend can hold: files at stable locations, the release notes, `SHA256SUMS` and an optional signature. Other provider features stay inside a backend or out of it. The ceremony never reads, stores, logs or echoes a credential; authentication belongs to the backend's own tooling and to the person releasing.

### The release key

- One OpenPGP RSA 4096 key signs both `SHA256SUMS` and release tags. RSA keeps uc releases verifiable by the same verifier manage-restic uses for restic.
- The key pinned is the key that actually signs: if a signing subkey is used, its own fingerprint is pinned, not the primary key's.
- The fingerprint is published in at least two independent places, so a reader can confirm it from more than one source.
- Christopher Steel creates and holds the key. The ceremony never creates, imports or stores a key; it signs with the one git and gpg are configured to use, and refuses `--sign` when there is none.

### Retiring the copied scripts and guides

An offering, `retire-copied-scripts`, carries `state: absent` items for the copies a repository may still hold: at its root, `bump-version.py`, `cut-release.py`, `publish-release.py`, `test_publish_release.py`, `check-conformance.py` and `normalize-metadata.py`; and the guides the old automa distributed, such as `commit-and-versioning-workflow`, at the paths sat-doc-automa's `ff-manifest-*.yaml` delivered them to.

Every item is a guarded retraction (uc-portage 0004): it lists, as `accepted_sha256`, the checksum of every version sat-doc-automa ever published at that path. A copy is removed only if its content, normalised for line endings, matches one of them. A copy that matches none is left in place and reported as "retained: content differs from every known version", by `plan`, `apply` and `harvest`, so a local edit is never lost and may be reviewed as an improvement. The guard does not change retraction elsewhere: an item without the list behaves as uc-portage 0002's ruling 3 says.

The lists are derived from sat-doc-automa's git history and committed in `offering.yaml`, never read from the repositories' `.file-fairy-state.yaml` files, which are partial, and absent from some repositories. For each path, the list is recomputed by taking every commit that touched the path, `git log --all --format=%H -- <path>`, reading the file at each with `git show <commit>:<path>`, normalising its line endings as uc-portage does, and taking each content's SHA-256, without duplicates. The offering records the sat-doc-automa commit its lists were computed at.

The guard and this first offering that uses it ship together: uc-portage 0.2.0 implements the guard, and uc-automa 0.2.0, which requires uc-portage 0.2.0 or later, carries the offering. uc-portage 0.1.0 refuses an offering that uses the guard, as uc-portage 0004 records, so an older uc-portage can never apply a guarded retraction unguarded.

### Tests

The ceremony's tests run offline: `test_publish_release.py` is ported, publishing to the `dir` backend in a scratch repository with a bare remote; every refusal has a test; a cut is followed by the tag directive's check; and the determinism gate is shown to fail on archives built with differing timestamps.

## Alternatives considered

**Keep copying the scripts, through an offering.** Rejected. Offerings carry what must live in each repository; code is installed (P4), and a copy in every repository drifts from the original.

**One command that cuts and publishes.** Rejected, as the scripts did. Pushing between the two is a human act over a transport the maintainer trusts, and a published release cannot be taken back.

**Publish wheels or source distributions to a package index.** Not now. The narrowest backend holds a tarball and its checksums; a package index is a separate decision, recorded in the roadmap.

## Consequences

- uc-automa's layout describes `lib/{package}/` as open, so `lib/uc_automa/release/` needs no layout change.
- Releasing needs git, the backend's own tool such as `gh`, and gpg when signing, on the releasing machine only. The ceremony runs on Linux first; macOS and Windows are verified before uc-automa reaches 1.0.0, like everything else.
- The OSAT manager process's release stage changes from tagging by hand to `uc-automa release cut` and `publish`.
- uc-automa 0.2.0's dependency becomes `uc-portage>=0.2.0`.
- A repository other than an OSAT manager keeps its run records under `tests/e2e/<platform>/` too, before it reaches 1.0.0; `tests/` is open in the python-tool layout, so this needs no layout change.
- Every repository releases the same way, at the uc-automa version it pins.

## Open questions

- [ ] Which two or more independent places publish the release key's fingerprint.

## References

<a id="ref-steel-2026a"></a>Steel, C. (2026a). *sat-doc-automa* [Computer software], commit fc0b72a: `bump-version.py`, `cut-release.py`, `publish-release.py`. GitHub. https://github.com/steelcj/sat-doc-automa [↩](#cite-steel-2026a)

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Decision: publish-release, a shared script with a provider interface* (Version 0.1.0) [Unpublished manuscript]. uc-radar, en/docs/decisions/devops/, commit 9a511d8. https://github.com/steelcj/uc-radar [↩](#cite-steel-2026b)

<a id="ref-steel-2026c"></a>Steel, C. (2026c). *Brief: uc-automa foundation* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96 [↩](#cite-steel-2026c)

<a id="ref-steel-2026d"></a>Steel, C. (2026d). *Release: Annotated version tags* (Version 0.1.0) [Directive]. uc-automa. https://github.com/steelcj/uc-automa/blob/aac6f83e8ec325359db050cf3b61c11d7fd14e23/en-ca/docs/directives/release/annotated-version-tags-v0.1.0.md [↩](#cite-steel-2026d)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-11 | Accepted | Initial version |

## License

This document, *Decision: Release Ceremony*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
