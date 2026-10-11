---
title: "Release: Annotated Version Tags"
dc:title: "Release: Annotated Version Tags"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "release, tags, git, VERSION, changelog"
dc:description: "A release tag is v and the contents of VERSION, with dots, such as v0.1.0; it is annotated, its message names the repository and the version, and it points at the commit whose VERSION and CHANGELOG.md match it."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:bf915db5-c7a3-45f7-a360-22db45a482c3"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "In force"
sat:directive: "release/annotated-version-tags"
sat:enforced_by:
  - "conformance.release.annotated_version_tags"
---

# Release: Annotated Version Tags

Version: 0.1.0
Status: In force

## Rule

- A release tag is `v` followed by the contents of `VERSION`, with dots, as in filename suffixes: `v0.1.0`, never `0.1.0` or `v0-1-0`. Every tag in a repository is a release tag.
- Release tags are annotated, and the message names the repository and the version, such as `uc-automa 0.1.0`.
- The tag points at the release commit, whose `VERSION` is that version and whose `CHANGELOG.md` has the section `## [0.1.0] - 2026-10-09`, dated the day the tag was made, in local time.
- The release commit is surgical: it changes only `CHANGELOG.md`, and `VERSION` if it needed changing, so the tag marks exactly the release.
- Keep a Changelog's link references at the end of the changelog are left out until the repository has a remote for them to point at.

Signed tags come with the release ceremony, planned for uc-automa 0.2.0.

## Rationale

Christopher Steel set this rule on 2026-10-09, when uc-portage and uc-automa were first tagged. A tag that matches its `VERSION` and changelog lets anyone go from a release to exactly what it contained.

## Examples

| Tag | Verdict |
| --- | --- |
| annotated `v0.1.0`, message `uc-portage 0.1.0`, at a commit with `VERSION` 0.1.0 and `## [0.1.0] - 2026-10-09` | Conforms |
| lightweight `v0.1.0` | Not annotated |
| `0.1.0` or `v0-1-0` | Wrong form |
| `v0.1.0` at a commit whose `VERSION` is 0.2.0 | Does not match |

## Check

`conformance.release.annotated_version_tags` checks every tag of a git repository; outside git it has nothing to check. Its fixtures are under `tests/fixtures/conformance/release/annotated-version-tags/`, each a small repository kept as a git bundle and cloned by the tests.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | In force | Initial version |

## License

This document, *Release: Annotated Version Tags*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
