---
title: "Decision: Where the Release Keys Are Published"
dc:title: "Decision: Where the Release Keys Are Published"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "release, keys, SSH, OpenPGP, allowed signers, fingerprints, offline install"
dc:description: "Answers the open question of uc-automa 0026 and 0028: the SSH allowed-signers line, and the OpenPGP key when there is one, are published in uc-automa's repository and on vishpala.com, two places on different hosts, and the README fetches the line from the repository with git, which the verification run can serve from a mirror, and has the reader compare its fingerprint with the site's by hand, never taking it from the release directory it is about to verify."
dc:date: "2026-10-11"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:b330a5f8-e42b-4af0-be3d-5488a7d967b9"
dc:relation:
  - "urn:uuid:a7667fcc-3e79-40d1-961a-35bd390b4137"
  - "urn:uuid:02eec912-6fb4-43f6-9a5d-db7b49e6e03c"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: Where the Release Keys Are Published

Version: 0.1.0
Status: Accepted

## Context

uc-automa 0026 requires the release key's fingerprint to be published in at least two independent places and leaves open which <a id="cite-steel-2026a"></a>[(Steel, 2026a)](#ref-steel-2026a). uc-automa 0028 adds an SSH release key, whose allowed-signers line the README's offline install needs, and carries the same question <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b). A key taken from the release directory it is meant to verify proves nothing: whoever could replace the release could replace the key beside it.

## Decision

### Two places, on different hosts

- **uc-automa's repository**, in a directory `release-keys/` at its root, added to the `uc-automa` layout as meta:
  - `release-keys/allowed-signers`: one line per SSH release key, `chris.steel@gmail.com namespaces="vishpala-release,git" ssh-ed25519 <key>`, the `git` namespace for signed tags (uc-automa 0032);
  - `release-keys/openpgp-key.asc`: the OpenPGP release key, ASCII-armoured, public part only, once there is one; 0.2.0 is released with the SSH key alone;
  - `release-keys/README.md`: each key's fingerprint, as `ssh-keygen -lf` prints it, or `gpg --fingerprint` for an OpenPGP key, and the date each was added.
- **vishpala.com**, Vishpala's site, on a page that shows the same allowed-signers line and every fingerprint `release-keys/README.md` lists.

One key pair of each kind signs every Vishpala release (uc-automa 0026, 0028), so the keys live once, in uc-automa, and every tool's README points there.

### The README fetches the key with git

Each Python tool's README gains a section `Get the release key`, just before `Install offline`, holding one block for each shell:

```markdown
### Get the release key

In the directory of release files:

~~~sh
git clone --depth 1 https://github.com/steelcj/uc-automa uc-automa-keys
ssh-keygen -lf uc-automa-keys/release-keys/allowed-signers
~~~

On Windows, in Command Prompt:

~~~bat
git clone --depth 1 https://github.com/steelcj/uc-automa uc-automa-keys
ssh-keygen -lf uc-automa-keys\release-keys\allowed-signers
~~~

Compare the fingerprint `ssh-keygen` prints with the one on vishpala.com, at <page>. If they differ, stop: do not install.
```

The `Install offline` block then names that file: `ssh-keygen -Y verify -f uc-automa-keys/release-keys/allowed-signers ...`, and `uc-automa-keys\release-keys\allowed-signers` in Command Prompt.

- **A git command, so the mirror covers it.** The verification run (uc-automa 0027) replays `Get the release key` unchanged, inside the network cut and before `Install offline`. The `insteadOf` mapping it already makes for uc-automa sends the clone to uc-automa's mirror, whose default branch carries one extra commit, made by the run with the throwaway identity it uses for the mirror's tag, that replaces `release-keys/allowed-signers` with the run's test key. A shallow clone through such a mapping was shown to work on 2026-10-11.
- **The comparison is a manual step, never replayed.** It is written as prose after the block, not as a command, because only a person can compare against the site. The run does not replay it, and its record lists it as a manual step not replayed. This adds `Get the release key` to the sections 0027 replays.
- A fingerprint, 43 characters after `SHA256:`, is compared once per key, rather than a whole key line.

### Rotating a key

A new key is added as a new line, and the old line gains `valid-before="<date>"`, so releases signed before the change still verify and releases after it do not accept the old key. The site and `release-keys/README.md` change in the same day. `release-keys/` is changed only by commits Christopher Steel makes or approves.

## Alternatives considered

**The release directory.** Rejected, as above.

**A copy in every tool's repository, delivered by an offering.** Not now. uc-portage would keep the copies identical, but a reader gains no independence from a second copy on the same host, and a rotation would wait for every repository to apply the offering.

**The site alone.** Rejected. 0026 asks for two places, and a reader without the site's address can still find uc-automa's repository from any tool's README.

## Consequences

- The `uc-automa` layout gains `release-keys/` as meta, which is a change to a layout file and ships with uc-automa 0.2.0.
- The README gains `Get the release key`, and 0028's `Install offline` block names the cloned file. uc-automa 0027 replays the new section, and its record lists the fingerprint comparison as a manual step not replayed.
- Christopher Steel creates the SSH release key, and the page on vishpala.com, before uc-portage 0.2.0 is published. There is no OpenPGP key for 0.2.0, so its releases carry no `SHA256SUMS.asc` (uc-automa 0032).

## Open questions

- [ ] The path of the page on vishpala.com, written `<page>` above, once the rebuilt site has it.

## References

<a id="ref-steel-2026a"></a>Steel, C. (2026a). *Decision: Release ceremony* (Version 0.1.0) [Decision record]. uc-automa 0026. https://github.com/steelcj/uc-automa/blob/main/en-ca/docs/decisions/0026--release-ceremony-v0.1.0.md [↩](#cite-steel-2026a)

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Decision: Wheels with each release* (Version 0.1.0) [Decision record]. uc-automa 0028. https://github.com/steelcj/uc-automa/blob/main/en-ca/docs/decisions/0028--wheels-with-each-release-v0.1.0.md [↩](#cite-steel-2026b)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-11 | Accepted | Initial version |

## License

This document, *Decision: Where the Release Keys Are Published*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
