---
title: "Decision: Version Bumps for Rule Changes"
dc:title: "Decision: Version Bumps for Rule Changes"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "versions, directives, rules, semantic versioning, filenames"
dc:description: "Extends uc-automa 0002 with which part of a directive's version changes before 1.0.0: the minor version when the rule's meaning changes, so that some repository's verdict or a reader's action would differ, and the patch version when only the wording changes."
dc:date: "2026-10-11"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:4ee74a63-4d4d-4b47-8229-ef5ecf7cf1ab"
dc:relation:
  - "urn:uuid:b8b52dfa-7746-4ab9-93a7-03913e0b3a63"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: Version Bumps for Rule Changes

Version: 0.1.0
Status: Accepted

## Context

uc-automa 0002 puts a document's version in its filename before 1.0.0 and renames the file with `git mv` at each bump <a id="cite-steel-2026a"></a>[(Steel, 2026a)](#ref-steel-2026a). It does not say which part of the version a change bumps.

On 2026-10-11 the directive `release/annotated-version-tags` went from 0.1.0 to 0.2.0, when its rule began to let the release commit update `README.md`'s install references <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b). The minor version was chosen without a written rule. A directive is what `uc-automa check` enforces, so a reader comparing two versions of one needs to tell from the numbers alone whether what conforms has changed.

Accepted decisions in uc-automa are not revised; a later decision extends or supersedes them, as uc-automa 0025 superseded 0001 and 0021, and uc-automa 0027 extends 0011. This decision extends 0002 the same way.

## Decision

Before 1.0.0, a directive's version, its `sat:version` and its filename suffix, changes as follows.

### The minor version, when the meaning changes

`0.X.Y` becomes `0.(X+1).0` when the rule's meaning changes: some repository that conformed would no longer conform, or one that did not would now conform, or a reader following the text would act differently. That includes:

- adding, removing or changing a requirement, an exception or the rule's scope;
- changing what the check looks at or what it accepts, as the text describes it;
- changing the check named in `sat:enforced_by`.

### The patch version, for wording only

`0.X.Y` becomes `0.X.(Y+1)` when only the wording changes and every repository's verdict stays the same: a clearer sentence, a corrected typo or link, a new example of what the rule already said, or a rationale added.

### When unsure

The test is one question: would any repository's verdict change, or would anyone following the text do something differently? If yes, or if the answer is unclear, the change is minor.

### Every bump

- The file is renamed with `git mv`, and every link to it is updated in the same commit, as 0002 requires. A link that cites a specific earlier version keeps that version, pointing at it by commit.
- The Changelog table gains a row whose note says, in one line, what changed in meaning, or "Wording only".
- The status stays "In force".

### A check fixed without changing the rule

A check corrected so that it does what its unchanged text already says changes no document; the fix ships in uc-automa's release, whose changelog names the directive whose check changed (uc-automa 0017). If the text has to change to explain the fix, that change is a patch.

## Alternatives considered

**A minor bump for every change.** Rejected. The number would no longer tell a reader whether to check a repository again.

**Patch bumps for everything below 1.0.0.** Rejected. A change of meaning would look like a correction.

**Amending 0002 in place.** Rejected. Accepted decisions in uc-automa are not revised; extending one with a new decision keeps the record of what was decided when.

## Consequences

- `release/annotated-version-tags` 0.2.0 conforms: its meaning changed, so its minor version did.
- No check can tell a meaning change from a wording change; `naming/versions-in-filenames` goes on checking only that the filename matches `sat:version`. Review applies this rule.

## Open questions

- [ ] Whether the same rule applies to other versioned documents, such as guides.
- [ ] How a directive's version changes from 1.0.0, and what brings a directive to 1.0.0.

## References

<a id="ref-steel-2026a"></a>Steel, C. (2026a). *Decision: Versions in filenames* (Version 0.1.0) [Decision record]. uc-automa 0002. https://github.com/steelcj/uc-automa/blob/main/en-ca/docs/decisions/0002--versions-in-filenames-v0.1.0.md [↩](#cite-steel-2026a)

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Release: Annotated version tags* (Version 0.2.0) [Directive]. uc-automa. https://github.com/steelcj/uc-automa/blob/main/en-ca/docs/directives/release/annotated-version-tags-v0.2.0.md [↩](#cite-steel-2026b)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-11 | Accepted | Initial version |

## License

This document, *Decision: Version Bumps for Rule Changes*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
