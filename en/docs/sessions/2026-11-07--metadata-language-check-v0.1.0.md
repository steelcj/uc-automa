---
title: "Session: The Metadata Language Check and the en/ Move"
dc:title: "Session: The Metadata Language Check and the en/ Move"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "metadata, front matter, dc:language, language root, en, en-ca, layouts, source language, conformance, session record"
dc:description: "The record of the 2026-11-07 attempt to make uc-automa's code follow the move of its documentation from en-ca/ to en/: how the language folder and dc:language are tied together, what the move broke, the two blockers found, the value of the language check, and the owner's direction to make the metadata checker a standalone, configurable tool."
dc:date: "2026-11-07"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:ee0bb1c7-dbda-4ad9-b8cb-3da9160260a6"
dc:relation:
  - "urn:uuid:d12ace49-1a49-4acb-b67e-6fe23d9e0bf2"
  - "urn:uuid:e8cac7fd-1300-4b8e-bb35-a8cadc41c6a5"
  - "urn:uuid:e3c45b3f-7f7a-4521-9cf8-cfc8c5a9f6f8"
  - "urn:uuid:f834eafb-4b92-4bc2-a466-d014baf2f8fa"
dc:language: "en"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Session: The Metadata Language Check and the en/ Move

Version: 0.1.0
Status: Accepted

## Summary

uc-automa's documentation and layout text moved from `en-ca/` to `en/` in `c9e4ea3`. The code did not follow. uc-automa treats a language folder's name and its language tag as one thing, so after the move its own check reported 132 findings, and a test that had passed began to fail.

The fix chosen, "option 1", makes `en` both the folder and the tag. It was partly applied in `aaa0b15`, which brings the findings down to 63. Two blockers stop it there:

- a layout rule that ties every repository to uc-automa's own text language;
- a front-matter schema that refuses a language tag without a region.

Both are on the roadmap, marked "resolve soon". For the longer term, the owner wants the metadata checker as a standalone, configurable tool.

This record itself shows the problem. It declares `dc:language: "en"` because it sits under `en/`, and today's schema refuses that value.

## Inputs

- uc-automa 0004, *Language root en-ca*: the language root is `en-ca`.
- uc-automa 0007, *Documentation under en-ca/docs*.
- The directive `metadata/front-matter` 0.1.0, whose rule includes "`dc:language` matches the language root: `en-CA` under `en-ca/`".
- The directive `layout/repository-layout` 0.1.0.
- The move commit `c9e4ea3`. Its message stated that the code still used `en-ca`.

## How the folder and the tag are tied

Four places assume that the folder name is the language tag:

| Where | What it does |
|---|---|
| `lib/uc_automa/paths.py` | Finds language folders by pattern, `^[a-z]{2}(-[a-z]{2})?$`, and keys them by folder name. `text/<tag with underscore>/` when installed, `<tag>/conf/` in a checkout |
| `lib/uc_automa/conformance/metadata.py` | Takes the language from a document's first path segment, and expects `dc:language` to be that tag with its region in capitals: `en-ca/` → `en-CA`, `en/` → `en` |
| `schemas/front-matter.schema.yaml` | Requires `dc:language` to match `^[a-z]{2}-[A-Z]{2}$`, a region included |
| `conf/layouts/*.yaml` → `conformance/layout.py` | A layout's `source_language` names the language of its text. Paths marked `required: source-language` are checked against it |

While every repository and uc-automa itself used `en-ca`, these assumptions agreed with each other. The move is the first time they disagree.

## What the move broke

`uc-automa check` on uc-automa after `c9e4ea3`:

| Findings | Directive | Cause |
|---|---|---|
| 64 | `licensing/rights-match-reuse` | `REUSE.toml` covered `en-ca/**`, so nothing licensed `en/` |
| 59 | `metadata/front-matter` | `dc:language: "en-CA"` under `en/`, where `en` was expected |
| 5 | `layout/layout-translations` | The layouts' `source_language` was `en-ca`, but their text was in `en/conf/` |
| 3 | `layout/repository-layout` | `.uc-automa.yaml` still said `language: en-ca`, so `en-ca/` was required |
| 1 | `docs/generated-index` | `en-ca/docs/README.md` was missing |

Tests: 45 run, 2 failures. `test_translations_report_nothing_for_en_ca` failed because of the move. `test_check_passes_on_uc_automa` was already failing, because `218bdec` had added `docs/overviews/` without describing it in the layout.

## Options considered

1. **`en` is both the folder and the tag.** Chosen, "for now".
2. **`en` is a folder name that still holds `en-CA` text.** This would mean separating folders from tags in the code, which goes against 0004 and 0012.
3. **Undo the move.**

## The value of the language check

The `dc:language` rule in `metadata/front-matter` catches two mistakes: a document saved in the wrong language folder, and a translation copied without its metadata being updated. That keeps `dc:language` reliable for translation tracking, the docs index and, later, the `lang` of a published page.

With one language per repository it adds little. It earns its place once a repository has two language folders, such as `en/` and `fr-ca/`.

It cannot express a folder whose documents use a more specific tag than the folder's name, such as `en-CA` documents under `en/`, the way uc-processes keeps them. That needs configuration.

## Decisions

- **Option 1, for now.** The owner: "option 1, but we need a config file for that check. In some cases it will be different as you mentioned."
- **A standalone checker, later.** The owner: "I think metadata checker should be it's own stand alone repository / executable. It should include all of the resources it needs and it should be configurable."
- **Stop at the blockers and track them.** The owner: "do nothing, if you think this issue needs to be resolved now or very soon add it to the roadmap", and then: "keep them, update the session reports, commit and push".

## What was made

In `aaa0b15`:

- `en` throughout:
  - `.uc-automa.yaml`;
  - the five layouts' `source_language` and the five layout texts' `language`;
  - `DEFAULT_LANGUAGE` in `lib/uc_automa/init.py`, so `init` gives new repositories `en`;
  - the package data, now `uc_automa.data.text.en` from `en/conf`.
- The `claude-signpost` and `changelog` offerings' text folders, renamed from `en-ca/` to `en/`, with `source_language: "en"`. uc-portage falls back to an offering's `source_language` when a subscriber has no folder for its own language, so `en-ca` subscribers still get the text.
- `REUSE.toml` and the `reuse` offering's `REUSE.toml`, which now cover `en/**`.
- Every document's `dc:language`, now `"en"` (66 lines).
- `tests/test_commands.py`: `init`'s default language is `en`, and the translations test is renamed `test_translations_report_nothing_for_en`.
- A `ROADMAP.md` item for each blocker, under the `en/` move.

`uc-automa check` on uc-automa now reports 63 findings.

## The blockers

### `source-language` paths are checked against the layout's language

`conformance/layout.py` checks paths marked `required: source-language` against `layout.source_language`, the language of uc-automa's own layout text. Once that is `en`, every repository using uc-automa's layouts must have an `en/` folder, whatever language it declares.

The fixtures `layout/repository-layout/pass/decision-record` and `pass/python-tool` are `en-ca` repositories, and now fail with "`en/`: required by layout 'python-tool' but missing". Every downstream `en-ca` repository would fail the same way when it upgrades past its pin.

The likely fix is to check these paths against the repository's configured language, `.uc-automa.yaml`'s `language`. That changes the meaning of `layout/repository-layout`, so it gets a minor bump under uc-automa 0029.

### The schema requires a region

`schemas/front-matter.schema.yaml` refuses `dc:language: "en"`, which accounts for 59 of the 63 findings. Widen the pattern to `^[a-z]{2}(-[A-Z]{2})?$`, which matches how `paths.py` already recognises language folders. `metadata/front-matter` gets a minor bump, with its rule reading "`en` under `en/`, `en-CA` under `en-ca/`".

## Verification

| State | `uc-automa check` on uc-automa | Tests (45) |
|---|---|---|
| Before the move (`c9e4ea3~1`) | 2 findings | 1 failure |
| After the move (`c9e4ea3`) | 132 findings | 2 failures |
| After option 1 so far (`aaa0b15`) | 63 findings | 4 failures |

The 4 failures in `aaa0b15`:

- `test_check_passes_on_uc_automa`: the 63 findings.
- `test_offerings_plan_has_nothing_to_do`: the signpost's text changed, and uc-automa's own `CLAUDE.md` block was not synced.
- The two `layout/repository-layout` pass fixtures: the first blocker.

The tests were run with `python -m unittest discover` from `tests/`.

## Known debt

Content that fails uc-automa's check on its own, unrelated to the language:

- `en/docs/overviews/` is not described by the `uc-automa` layout.
- `en/docs/sessions/osat-manager-git-where-things-stand-after-2026-10-21.md` has no front matter, and its name is not a session record's.
- `en/docs/overviews/overview--sat-development-current-state-v0.1.0.md` declares `dc:rights` AGPL-3.0-or-later, where `REUSE.toml` says CC-BY-4.0.

## Left open

Tracked in `ROADMAP.md` under the `en/` move:

- [ ] **Resolve soon:** check `source-language` layout paths against the repository's own language.
- [ ] **Resolve soon:** widen the front-matter schema's `dc:language` pattern.
- [ ] Then:
  - [ ] run `uc-automa offerings apply` and `uc-automa docs index`;
  - [ ] write decision 0040, *Language root en*, superseding 0004 and 0007;
  - [ ] add a `CHANGELOG.md` entry.
- [ ] Make `test_check_passes_on_uc_automa` pass, which includes the known debt above.
- [ ] Longer term: a standalone, configurable metadata checker. It would be its own repository and executable, carry its schema and vocabularies, and read a configuration that can map a folder to a different `dc:language`, such as `en/` → `en-CA`. Its first questions are the configuration's form and where it lives, and how `uc-automa check` calls it.

## References

- uc-automa: https://github.com/steelcj/uc-automa
- uc-portage: https://github.com/steelcj/uc-portage
- uc-processes: https://github.com/steelcj/uc-processes, where the same session's process work is recorded

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-11-07 | Accepted | Initial version |

## License

This document, *Session: The Metadata Language Check and the en/ Move*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
