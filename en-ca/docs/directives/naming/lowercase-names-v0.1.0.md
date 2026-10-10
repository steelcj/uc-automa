---
title: "Naming: Lowercase Names"
dc:title: "Naming: Lowercase Names"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "naming, lowercase, characters, dots, exceptions"
dc:description: "Names use lowercase letters, digits and hyphens, with a dot only inside a version suffix or before an extension; the conventional uppercase files, tool-mandated names, licence texts and Python names are the written exceptions."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:66c97c8d-e1cb-4652-91a8-25279a1dacdd"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "In force"
sat:directive: "naming/lowercase-names"
sat:enforced_by:
  - "conformance.naming.lowercase_names"
---

# Naming: Lowercase Names

Version: 0.1.0
Status: In force

## Rule

Every file and directory name uses lowercase letters `a` to `z`, digits and hyphens. A dot appears only inside a `-vX.Y.Z` version suffix, before the extension, or at the start of a dotfile or SAT sidecar. `.schema.yaml` counts as one extension.

The written exceptions:

- the conventional uppercase repository files, wherever they appear: `README.md`, `LICENSE`, `CHANGELOG.md`, `VERSION`, `ROADMAP.md`, `CONTRIBUTING.md` and `CLAUDE.md`;
- names a tool requires, such as `REUSE.toml`;
- licence texts in a `LICENSES/` directory, which keep their SPDX identifiers, such as `GPL-3.0-or-later.txt`;
- Python modules and packages under `lib/` and `tests/`, which use underscores because Python cannot import hyphens.

## Rationale

Lowercase names behave the same on file systems that ignore case and on those that do not, and a reader can tell what a path holds from the path alone. The exceptions are names tools and forges look for, or names another standard fixes.

## Examples

| Name | Verdict |
| --- | --- |
| `using-uc-portage-v0.1.0.md` | Conforms |
| `offering.schema.yaml` | Conforms |
| `Using-UC-Portage.md` | Uppercase letters |
| `using_uc_portage.md` | Underscore outside Python code |
| `using.uc.portage.md` | Dots in the stem |

## Check

`conformance.naming.lowercase_names` looks at every path component of every file the repository contains, except the conformance fixtures, and reports any name outside the rule and its exceptions. Its fixtures are under `tests/fixtures/conformance/naming/lowercase-names/`.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | In force | Initial version |

## License

This document, *Naming: Lowercase Names*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
