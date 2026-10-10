---
title: "Decision: Versions in Filenames"
dc:title: "Decision: Versions in Filenames"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "versions, filenames, documents, D1"
dc:description: "Before 1.0.0 a versioned document's filename carries -vX.Y.Z with dots; from 1.0.0 the version leaves the filename; a bump renames the file with git mv."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:b8b52dfa-7746-4ab9-93a7-03913e0b3a63"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
sat:decision: "D1"
---

# Decision: Versions in Filenames

Version: 0.1.0
Status: Accepted

## Context

Versioned documents across Vishpala's repositories carried their version in the filename in a hyphenated form, such as -v0-1-0, which came from an earlier AI assumption, not from the spec, and had to be corrected several times. The decision was worked out with Christopher Steel on 2026-10-07 and 2026-10-09 and recorded in the foundation brief <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b).

## Decision

- A versioned document carries `-vX.Y.Z`, with dots, before the extension until 1.0.0: `directory-guide-v0.2.0.md`.
- From 1.0.0 the version leaves the filename and lives in front matter, the Changelog table and git tags: `directory-guide.md`.
- A bump renames the file with `git mv`, so history follows it, and updates every link to it in the same commit.
- The hyphenated form is never used.

## Consequences

- The directive `naming/versions-in-filenames` states the rule and its check enforces it, comparing each filename with its document's `sat:version`.
- Configuration files, schemas, templates, licence texts and code carry no version in their names; the repository's release versions them (uc-automa 0017).

## References

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Brief: uc-automa foundation* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96 [↩](#cite-steel-2026b)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: Versions in Filenames*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
