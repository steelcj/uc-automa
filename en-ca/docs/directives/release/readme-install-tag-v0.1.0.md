---
title: "Release: README Install Tag"
dc:title: "Release: README Install Tag"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "release, README, install, tags, VERSION"
dc:description: "Wherever README.md installs its own repository from a git reference, such as git+https://github.com/steelcj/uc-automa@v0.1.0, the reference is v and the contents of VERSION, so the README always installs the release its commit carries."
dc:date: "2026-10-11"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:0e7efe9e-7ef7-43ed-b590-af3fe97a02cf"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "In force"
sat:directive: "release/readme-install-tag"
sat:enforced_by:
  - "conformance.release.readme_install_tag"
---

# Release: README Install Tag

Version: 0.1.0
Status: In force

## Rule

- Wherever `README.md` installs its own repository from a git reference in a URL, `/<repository>@<reference>` or `/<repository>.git@<reference>`, the reference is the release tag of the repository's `VERSION`: `v` and the contents of `VERSION`, with dots.
- `<repository>` is the name `.uc-automa.yaml` gives the repository. References to other repositories, such as a dependency installed at its own tag, are left alone.
- `uc-automa release cut` rewrites these references when it bumps `VERSION`, and commits `README.md` with the release (uc-automa 0028), so the README of the release commit installs the release.

## Rationale

The README's install command is what a reader runs, and the verification run replays it as written (uc-automa 0027). A README left naming the previous tag installs the previous release while its `VERSION` says otherwise. Christopher Steel set this rule on 2026-10-11, so that `uc-automa check` catches the mismatch on every commit, before any verification run.

## Examples

With `repository: uc-automa` and `VERSION` 0.2.0:

| In `README.md` | Verdict |
| --- | --- |
| `git+https://github.com/steelcj/uc-automa@v0.2.0` | Conforms |
| `git+https://github.com/steelcj/uc-portage@v0.2.0` | Not checked: another repository |
| `git+https://github.com/steelcj/uc-automa@v0.1.0` | Installs the previous release |
| `git+https://github.com/steelcj/uc-automa.git@0.2.0` | Not a release tag |

## Check

`conformance.release.readme_install_tag` reads `README.md` at the repository root, line by line, when the repository has `.uc-automa.yaml` and `VERSION`; without them it has nothing to check. Its fixtures are under `tests/fixtures/conformance/release/readme-install-tag/`.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-11 | In force | Initial version |

## License

This document, *Release: README Install Tag*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
