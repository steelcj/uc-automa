---
title: "Release: README Install Tag"
dc:title: "Release: README Install Tag"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "release, README, install, tags, VERSION"
dc:description: "Wherever README.md installs its own repository from a git reference, such as git+https://github.com/steelcj/uc-automa@v0.1.0, the reference is v and the contents of VERSION; wherever it installs a dependency named in pyproject.toml that way, the reference is a release tag the dependency's range allows. The README then installs the release its commit carries, with dependencies its package accepts."
dc:date: "2026-10-11"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:0e7efe9e-7ef7-43ed-b590-af3fe97a02cf"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.2.0"
sat:status: "In force"
sat:directive: "release/readme-install-tag"
sat:enforced_by:
  - "conformance.release.readme_install_tag"
---

# Release: README Install Tag

Version: 0.2.0
Status: In force

## Rule

- Wherever `README.md` installs its own repository from a git reference in a URL, `/<repository>@<reference>` or `/<repository>.git@<reference>`, the reference is the release tag of the repository's `VERSION`: `v` and the contents of `VERSION`, with dots.
- `<repository>` is the name `.uc-automa.yaml` gives the repository.
- Wherever `README.md` installs a dependency that way, a repository whose name is a project in `pyproject.toml`'s `[project] dependencies`, the reference is a release tag, `v` and a version, and the dependency's range allows that version. Names compare as packaging compares them. A repository's name is taken to be its project's name.
- The range may use `==`, `!=`, `<`, `<=`, `>`, `>=` and `~=` on release numbers, and `==` or `!=` with a trailing `.*`; a range using anything else is reported, since the check cannot evaluate it. Environment markers after `;` are ignored.
- References to repositories that are neither this one nor a dependency are left alone.
- `uc-automa release cut` rewrites the references to the repository's own release when it bumps `VERSION`, and commits `README.md` with the release (uc-automa 0028), so the README of the release commit installs the release. A dependency's reference is changed by hand, with its range.

## Rationale

The README's install command is what a reader runs, and the verification run replays it as written (uc-automa 0027). A README left naming the previous tag installs the previous release while its `VERSION` says otherwise, and a README naming a dependency's tag outside the package's range makes pip fail to resolve, or installs a dependency the package does not accept. Christopher Steel set this rule on 2026-10-11, so that `uc-automa check` catches the mismatch on every commit, before any verification run.

## Examples

With `repository: uc-automa`, `VERSION` 0.2.0 and the dependency `uc-portage>=0.2.0,<0.3.0`:

| In `README.md` | Verdict |
| --- | --- |
| `git+https://github.com/steelcj/uc-automa@v0.2.0` | Conforms |
| `git+https://github.com/steelcj/uc-portage@v0.2.0` | Conforms: in the dependency's range |
| `git+https://github.com/steelcj/uc-portage@v0.1.0` | Outside the dependency's range |
| `git+https://github.com/steelcj/uc-portage@main` | Not a release tag |
| `git+https://github.com/steelcj/osat-manager-restic@v0.1.0` | Not checked: neither this repository nor a dependency |
| `git+https://github.com/steelcj/uc-automa@v0.1.0` | Installs the previous release |
| `git+https://github.com/steelcj/uc-automa.git@0.2.0` | Not a release tag |

## Check

`conformance.release.readme_install_tag` reads `README.md` at the repository root, line by line, when the repository has `.uc-automa.yaml` and `VERSION`; without them it has nothing to check. It reads `pyproject.toml` only as far as `[project] dependencies`, as an array of quoted strings. Its fixtures are under `tests/fixtures/conformance/release/readme-install-tag/`.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-11 | In force | Initial version |
| 0.2.0 | 2026-10-11 | In force | A dependency's install tag must be a release tag its `pyproject.toml` range allows |

## License

This document, *Release: README Install Tag*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
