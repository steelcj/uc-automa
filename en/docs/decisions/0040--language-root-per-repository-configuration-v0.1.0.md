---
title: "Decision: Language Root as Per-Repository Configuration"
dc:title: "Decision: Language Root as Per-Repository Configuration"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "language root, dc:language, front matter, layouts, source language, configuration, en, en-ca"
dc:description: "A language root is a folder a repository configures, and dc:language is a claim uc-automa no longer checks: uc-automa's own root becomes en, layout paths are checked against the repository's language, and dc:language stays a required front-matter field whose value is not validated."
dc:date: "2026-11-07"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:6f1c9d2a-3b7e-4c58-9a1f-2d8e5b7c4a90"
dc:relation:
  - "urn:uuid:d12ace49-1a49-4acb-b67e-6fe23d9e0bf2"
  - "urn:uuid:e8cac7fd-1300-4b8e-bb35-a8cadc41c6a5"
  - "urn:uuid:e3c45b3f-7f7a-4521-9cf8-cfc8c5a9f6f8"
  - "urn:uuid:f834eafb-4b92-4bc2-a466-d014baf2f8fa"
  - "urn:uuid:ee0bb1c7-dbda-4ad9-b8cb-3da9160260a6"
dc:language: "en"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Proposed"
---

# Decision: Language Root as Per-Repository Configuration

Version: 0.1.0
Status: Proposed

## Context

uc-automa 0004 made `en-ca` the language root, and 0007 put documentation under `en-ca/docs/` <a id="cite-steel-2026a"></a>[(Steel, 2026a)](#ref-steel-2026a); <a id="cite-steel-2026b"></a>[(Steel, 2026b)](#ref-steel-2026b). On 2026-11-07, uc-automa's documentation and layout text moved to `en/`, and the code did not follow. The attempt to make it follow is recorded in the session record of that day <a id="cite-steel-2026e"></a>[(Steel, 2026e)](#ref-steel-2026e). It showed that four places treat a folder's name and a document's language as one thing:

- `lib/uc_automa/paths.py` recognises language folders by the pattern `^[a-z]{2}(-[a-z]{2})?$`.
- `conformance/metadata.py` expects `dc:language` to be the folder's name with its region in capitals: `en-CA` under `en-ca/`.
- `schemas/front-matter.schema.yaml` requires `dc:language` to match `^[a-z]{2}-[A-Z]{2}$`, so a tag without a region, such as `en`, is refused. The rule is the directive `metadata/front-matter` 0.1.0's, not a decision's <a id="cite-steel-2026c"></a>[(Steel, 2026c)](#ref-steel-2026c).
- `conformance/layout.py` checks paths marked `required: source-language` against the layout's `source_language`, the language uc-automa's layout text is written in, not against the repository's. With uc-automa's text in `en`, every repository using its layouts would need an `en/` folder <a id="cite-steel-2026d"></a>[(Steel, 2026d)](#ref-steel-2026d).

While uc-automa and every repository used `en-ca`, these agreed. They no longer do. The same separation matters elsewhere: uc-processes keeps Canadian English documents, `en-CA`, under `en/`.

## Principle

A folder name and `dc:language` are different things. The language root is where documents are filed. `dc:language` is a claim about what language a document is in. The relation between them is the repository's business, and uc-automa does not police it.

## Decision

### uc-automa's own root is `en`

uc-automa's documentation and layout text live under `en/`, its `.uc-automa.yaml` declares `language: en`, its layouts' `source_language` is `en`, and `uc-automa init` writes `language: en` unless told otherwise. This supersedes 0004 and 0007.

### Layout paths follow the repository's language

A path marked `required: source-language` is checked against the repository's `language` in `.uc-automa.yaml`, not against the layout's `source_language`. The layout's `source_language` keeps one meaning only: the language its own text is written in, for `layout/layout-translations`. An `en-ca` repository needs `en-ca/`, and uc-automa needs `en/`.

### `dc:language` is not checked

`dc:language` stays a required front-matter field, so every document still declares its language. uc-automa does not validate its value:

- the schema gives it no pattern, only that it is a string;
- `metadata/front-matter` no longer compares it with the document's language root.

A repository writes whatever tag fits its documents, such as `en`, `en-CA` or `fr-CA`. A wrong or malformed tag is a matter for review, not for `uc-automa check`.

### Folder names

A language root is recognised as now, by `paths.py`'s pattern. Widening that pattern, for example to three-letter codes, is left until a repository needs it.

## Alternatives considered

**Keep `en-ca` as the root, and undo the move.** Rejected. It forces every Canadian English repository to call its root `en-ca`, and gives no way to file `en` and `en-CA` documents together.

**Check that `dc:language` is a well-formed BCP 47 tag, matching its root by default, with a `languages` key to widen a root.** Rejected by the owner: "lets drop language checking altogether". With one language per repository the check adds little. The standalone metadata checker the owner wants will not check `dc:language` either (see Open questions).

**Make `dc:language` optional.** Not chosen. A document should still say what language it is in, even when nothing checks it.

## Consequences

- `metadata/front-matter` goes from 0.1.0 to 0.2.0, since its meaning changes (uc-automa 0029) <a id="cite-steel-2026f"></a>[(Steel, 2026f)](#ref-steel-2026f): `dc:language` is required, and its value is not checked. The pattern is removed from `schemas/front-matter.schema.yaml`, and the language comparison is removed from `conformance/metadata.py`, with its fixtures.
- `layout/repository-layout` goes from 0.1.0 to 0.2.0: `required: source-language` paths are checked against the repository's `language`. The fixtures `layout/repository-layout/pass/decision-record` and `pass/python-tool`, which are `en-ca` repositories, pass again unchanged.
- Repositories pinned to an earlier uc-automa are unaffected. On upgrading, an `en-ca` repository keeps `en-ca/` and `en-CA` with no change, and any repository may keep `en-CA` documents under `en/`.
- uc-automa's own documents keep `dc:language: "en"`, as `aaa0b15` set them. They could equally say `en-CA`.
- The roadmap's "resolve soon" items under the `en/` move are the implementation of this decision. The schema item becomes "remove the pattern" instead of "widen it".

## Open questions

- [x] Whether the standalone metadata checker the owner wants checks `dc:language` at all. No, the owner answered: "So no, the standalone checker should not check dc:language at all."

## References

<a id="ref-steel-2026a"></a>Steel, C. (2026a). *Decision: Language root en-ca* (Version 0.1.0). uc-automa 0004. https://github.com/steelcj/uc-automa/blob/main/en/docs/decisions/0004--language-root-en-ca-v0.1.0.md [↩](#cite-steel-2026a)

<a id="ref-steel-2026b"></a>Steel, C. (2026b). *Decision: Documentation under en-ca/docs* (Version 0.1.0). uc-automa 0007. https://github.com/steelcj/uc-automa/blob/main/en/docs/decisions/0007--documentation-under-en-ca-docs-v0.1.0.md [↩](#cite-steel-2026b)

<a id="ref-steel-2026c"></a>Steel, C. (2026c). *Metadata: Front matter* (Version 0.1.0) [Directive]. uc-automa. https://github.com/steelcj/uc-automa/blob/main/en/docs/directives/metadata/front-matter-v0.1.0.md [↩](#cite-steel-2026c)

<a id="ref-steel-2026d"></a>Steel, C. (2026d). *Layout: Repository layout* (Version 0.1.0) [Directive]. uc-automa. https://github.com/steelcj/uc-automa/blob/main/en/docs/directives/layout/repository-layout-v0.1.0.md [↩](#cite-steel-2026d)

<a id="ref-steel-2026e"></a>Steel, C. (2026e). *Session: The metadata language check and the en/ move* (Version 0.1.0) [Session record]. uc-automa. https://github.com/steelcj/uc-automa/blob/main/en/docs/sessions/2026-11-07--metadata-language-check-v0.1.0.md [↩](#cite-steel-2026e)

<a id="ref-steel-2026f"></a>Steel, C. (2026f). *Decision: Version bumps for rule changes* (Version 0.1.0). uc-automa 0029. https://github.com/steelcj/uc-automa/blob/main/en/docs/decisions/0029--version-bumps-for-rule-changes-v0.1.0.md [↩](#cite-steel-2026f)

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-11-07 | Proposed | Initial version |

## License

This document, *Decision: Language Root as Per-Repository Configuration*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
