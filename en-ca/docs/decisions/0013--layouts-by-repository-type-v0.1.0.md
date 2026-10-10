---
title: "Decision: Layouts by Repository Type"
dc:title: "Decision: Layouts by Repository Type"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "layouts, extends, base, python-tool, uc-automa, osat-manager, closed, kind, from_offering, D13"
dc:description: "Layouts are split by repository type in a chain, base, python-tool, then uc-automa and osat-manager, each extending its parent under add-or-tighten rules; the layout check compares only the files a repository contains, with the root always closed."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:ac5f649a-9d64-476a-9ad8-5c37630b4f78"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
sat:decision: "D13"
---

# Decision: Layouts by Repository Type

Version: 0.1.0
Status: Accepted

## Context

A layout answers what a repository of one type contains. The first draft described only uc-automa, and kind of material appeared both as an attribute of paths and as a candidate for separate files. The decision was worked out with Christopher Steel on 2026-10-07 and 2026-10-09 and recorded in the foundation brief <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b). On 2026-10-09 Christopher Steel added the python-tool layout and the chain, the extends rules, how kind and from_offering are inherited, and how undescribed files are treated.

## Decision

### The chain

```text
base
└── python-tool
    ├── uc-automa
    └── osat-manager
```

`conf/layouts/base.yaml` describes what every repository holds. `python-tool.yaml` extends it with what a Python tool holds: `pyproject.toml`, `lib/{package}/`, `tests/`, and an optional `schemas/`. `uc-automa.yaml` and `osat-manager.yaml` both extend `python-tool`, since both are Python tools, and add only what is specific to them. Each is defined once (P1). python-tool is named for Python so that a non-Python tool can have its own layout later; it was taken from what uc-portage actually holds. A repository names its type with `layout:` in `.uc-automa.yaml`.

### The extends rules

- One parent per layout; chains are allowed; a cycle is an error.
- A child may add paths, including children of an inherited directory, and may add new placeholders.
- A child may tighten `required` but never loosen it, in the order `false` < `source-language` < `true`.
- `source-language` is valid only on a path that begins with the `{language}` placeholder. Inside a language root, `required: true` means required in every language root that is present.
- A child may not remove an inherited path, change its type, or redefine an inherited placeholder.
- `kind` is declared only on top-level nodes, and every descendant inherits it; a path added under an inherited directory takes that directory's kind.
- A child may set `kind` or `from_offering` on an inherited top-level path that has none, and may never change one already set: add or tighten, never take away. uc-automa uses this to give its inherited paths their kinds, since kind is a uc-automa concept (uc-automa 0014).
- A child may close an open directory, and may never reopen a closed one. Paths a child adds inside a closed directory count as declared.
- `format` and `source_language` match all the way up the chain.
- The check resolves the parent first, then the child, and checks against the merged tree.
- Each language file describes only the paths its own layout adds; inherited paths keep the parent's words. The translation check runs per file.

### What the check compares

- The root is always closed: every top-level entry must be described.
- Inside, a directory is closed only when it says `closed: true`; then every entry must match a declared child.
- Only the files the repository contains are checked: in a git working tree, `git ls-files --cached --others --exclude-standard`; outside git, as in a release tarball, every file. `.git/` is never counted.
- A top-level path a layout does not describe is a finding about the layout, not a reason for a per-repository exception. There is no escape hatch.

## Alternatives considered

**Every directory that declares children is closed.** Rejected: `lib/uc_automa/` and `tests/` would have to list every module.

**Only the root is closed.** Rejected: a misnamed file deeper down, such as a decision record with a single hyphen, would go unnoticed.

## Consequences

- The layout check enforces the directive `layout/repository-layout`.
- With `{version}` optional in the layout, a pre-1.0.0 record missing its suffix matches the layout, so the filename-version check catches it; the two checks together cover it.

## References

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Brief: uc-automa foundation* (Version 0.1.0) [Unpublished manuscript]. urn:uuid:965f6290-3d72-4631-ad66-9b4c6f63db96 [↩](#cite-steel-2026b)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: Layouts by Repository Type*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
