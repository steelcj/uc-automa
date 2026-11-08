---
title: "Directory Guide"
dc:title: "Directory Guide"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "uc-automa, layouts, repository layout, directories, offerings, directives"
dc:description: "What each directory of a Vishpala repository holds, by layout type, with descriptions taken from the en-ca layout words."
dc:date: "2026-10-23"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:c73e134d-11d2-44f9-a0ef-a0d446a896a3"
dc:source: "Hand-off package 2026-10-09--uc-automa-foundation, inputs/revise/automa--directory-guide-v0.1.0.md, not under version control"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.3.0"
sat:status: "Accepted"
---

# Directory Guide

Version: 0.3.0
Status: Accepted

## How to read this guide

This guide explains what each directory of a Vishpala repository holds and why. The layouts under `conf/layouts/` are the authority; the descriptions here are taken from their en-ca words, so the guide and the layouts say the same thing. Where they ever disagree, the layout wins and this guide is corrected.

Every repository has a layout type, named by `layout:` in its `.uc-automa.yaml`. The types form a chain, each adding to its parent (uc-automa 0013):

```text
base                  what every repository holds
├── python-tool       a repository whose product is a Python tool
│   ├── uc-automa     the station itself
│   └── osat-manager  a manager installing one tool into user space
└── eleventy-site     a website built with Eleventy
```

uc-automa holds three kinds of material, and each has one home (uc-automa 0014):

| Kind | Home | How a receiving repository gets it |
| --- | --- | --- |
| `runs`: things a tool runs | `lib/uc_automa/`, `conf/`, `schemas/` | Installed as the `uc-automa` package, pinned per repository |
| `read`: things people and AI read | `en-ca/docs/` | Read at the pinned version, never copied |
| `lives`: things that must live in each repository | `offerings/` | Carried in by uc-portage, by subscription |

The fourth kind, `meta`, describes or configures uc-automa itself and is not delivered anywhere. In receiving repositories, kind does not appear; a file that arrives from uc-automa is marked `from_offering` in the layout instead.

## Repository root

The root holds only files that describe the repository and files tools require at the root. It is always closed: every top-level entry must be one the layout describes.

| Path | What it holds |
| --- | --- |
| `README.md` | What the repository is, how to install or use it, and where its documentation is |
| `LICENSE` | The code licence text for forges that look for a root LICENSE file, byte-identical to LICENSES/MIT.txt |
| `LICENSES/` | Full text of every licence used in the repository, one file per SPDX identifier, as REUSE requires |
| `REUSE.toml` | The canonical record of which licence covers which paths; seeded once, then the repository's own |
| `CHANGELOG.md` | The repository's changelog in Keep a Changelog form, one entry per tagged release |
| `VERSION` | The single source of the repository's version |
| `ROADMAP.md` | Forward plan only; completed items move to CHANGELOG.md |
| `CONTRIBUTING.md` | How changes arrive and are reviewed |
| `CLAUDE.md` | Instructions for AI collaborators, ending with the signpost block from uc-automa |
| `.uc-automa.yaml` | The repository's name, layout type, uc-automa pin, language and subscriptions; written once by uc-automa init and owned by the repository |
| `.uc-portage-state.yaml` | What uc-portage last delivered, with checksums; written by uc-automa offerings apply and committed |
| `.gitattributes` | Line ending policy, LF everywhere |
| `.editorconfig` | Editor defaults: UTF-8, LF and a final newline |
| `.gitignore` | Build output, virtual environments, caches and release artefacts |
| `.pre-commit-config.yaml` | The pre-commit hooks the repository runs on itself |

`.uc-automa.yaml` is written once by `uc-automa init` and owned by the repository afterwards (uc-automa 0023):

```yaml
format: 1
repository: "osat-manager-restic"
layout: "osat-manager"
automa_version: "0.1.0"        # the installed uc-automa must match exactly
language: "en-ca"
subscribe:
  - license-mit
  - license-cc-by-4-0
  - reuse
  - changelog
  - version-file
  - claude-signpost
  - line-endings
  - editorconfig
```

## LICENSES

Full text of every licence used in the repository, one file per SPDX identifier, as REUSE requires. Licences follow the REUSE convention: `REUSE.toml` sets a licence per path, and a file that differs carries its own SPDX line. Code is licensed MIT, and documentation and content CC BY 4.0 (uc-automa 0025). The root `LICENSE` is byte-identical to `LICENSES/MIT.txt` and comes from the same offering payload.

| Path | What it holds |
| --- | --- |
| `LICENSES/MIT.txt` | The code licence, with the copyright holder and year filled in |
| `LICENSES/CC-BY-4.0.txt` | The documentation and content licence, copied verbatim |
| `LICENSES/{spdx-id}.txt` | Any other licence text, for third-party material, copied verbatim |

## The SAT sidecar

The SAT sidecar for the repository as an archive, named for the repository; provisional until the SAT configuration cascade specification is written. It is named for the repository declared in `.uc-automa.yaml`, not for the folder a clone sits in (uc-automa 0022).

| Path | What it holds |
| --- | --- |
| `.{repository}.assets/archive.yaml` | Role, urn:uuid identifier, title, default language and default rights |
| `.{repository}.assets/dc.yaml` | Dublin Core defaults every document inherits unless it overrides them |

```yaml
# .uc-automa.assets/archive.yaml
sat:role: "archive"
dc:identifier: "<printed by uc-automa metadata new-id>"
dc:title: "uc-automa"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
```

## Python tools

A python-tool repository adds its package, its tests and their definition. uc-automa and every OSAT manager are python-tool repositories.

| Path | What it holds |
| --- | --- |
| `pyproject.toml` | Package definition: name, dependencies, the console-script entry point, the version read from VERSION, and any data mapped into the package |
| `lib/` | Root for installable code |
| `lib/{package}/` | The package |
| `lib/{package}/__init__.py` | Package marker and version lookup |
| `tests/` | Offline tests, run before every commit |
| `schemas/` | JSON Schema documents written in YAML: the contracts the tool reads and offers, mapped into the package |

Data a tool reads, such as `schemas/`, lives once at the repository root and is mapped into the package by `pyproject.toml`; installed, the package carries its own copy, and in a checkout the tool reads the root after proving it is its own checkout (uc-automa 0019).

## Language roots

A language root: everything in the repository written in one language. The source language is `en-ca`, with `en-CA` in metadata (uc-automa 0004). A translation, such as `fr-ca/`, mirrors the same relative paths, and a document and its translation pair by identifier.

| Path | What it holds |
| --- | --- |
| `{language}/docs/` | All reading material in this language |
| `{language}/docs/README.md` | Generated index of every document, with its version and status |
| `{language}/docs/guides/` | Explanation and procedure, by topic |
| `{language}/docs/guides/{topic}/` | The guides on one topic |
| `{language}/docs/decisions/` | Decision records for this repository, numbered within it; across repositories a record is known by its urn:uuid, and in prose by repository and number, such as uc-portage 0002 |
| `{language}/docs/references/` | Standing reference material from outside sources |
| `{language}/docs/sessions/` | Dated records of how the repository was built or changed, one per working session |

Decision records are numbered within their repository, `0001`, `0002` and so on. Only uc-automa's records are Vishpala-wide, and numbered globally. Across repositories a record is known by its `urn:uuid`, and in prose by repository and number, such as uc-portage 0002.

Versioned documents carry their version in the filename, with dots, until 1.0.0, and none from 1.0.0 (uc-automa 0002); parts of a name are joined by `--` (uc-automa 0010):

```text
en-ca/docs/
├── README.md                                        generated by uc-automa docs index
├── decisions/0001--declared-sync-policy-v0.2.0.md
├── guides/usage/using-uc-portage-v0.1.0.md
└── sessions/2026-10-09--uc-automa-foundation-v0.1.0.md
```

## OSAT managers

An osat-manager repository adds a declarative description of the managed tool and its end-to-end runs. The process for creating one is its own guide.

| Path | What it holds |
| --- | --- |
| `manager.yaml` | Declarative description of the managed tool: sources, verification, platforms, aliases and install roots |
| `tests/unit/` | Offline tests, run on every platform and before every commit |
| `tests/e2e/` | End-to-end runs of the manager contract's scenario, one directory per platform |
| `tests/e2e/linux/` | The scenario as run on Linux, in a fresh Incus container |
| `tests/e2e/windows/` | The scenario as run on Windows |
| `tests/e2e/macos/` | The scenario as run on macOS, on Apple hardware |

## Eleventy sites

An eleventy-site repository builds a static website with Eleventy. It extends base directly, since a website is not a Python tool, and holds what an Eleventy site holds when set up as Eleventy and npm expect by default (uc-automa 0037). `src/` and `themes/` are open, so their contents are the site's own. Under `src/`, the names Eleventy requires by default are accepted: the `_data/` and `_includes/` directories, and data files such as `guides.11tydata.json`. The built site and the installed dependencies, such as `_site/` and `node_modules/`, belong in `.gitignore` and are never committed.

| Path | What it holds |
| --- | --- |
| `eleventy.config.js` | The Eleventy configuration: input and output directories, collections, filters and plugins |
| `package.json` | The npm manifest: Eleventy and the site's other build dependencies, and the build scripts |
| `package-lock.json` | The npm lockfile, so every build installs the same dependency versions |
| `src/` | The site's input: content, templates, data and assets |
| `themes/` | Themes the site draws on, such as fonts, styles and images |
| `netlify.toml` | The Netlify configuration, for a site deployed to Netlify: build settings, redirects and response headers |

## uc-automa itself

uc-automa adds the layouts, the offerings, the directives and the authoring templates. It subscribes to its own offerings with `automa_version: self`, so every offering is exercised here first.

| Path | What it holds |
| --- | --- |
| `.pre-commit-hooks.yaml` | Hooks uc-automa offers to other repositories; pre-commit requires this file at the root |
| `conf/` | Language-neutral configuration: structure only, with no prose |
| `conf/layouts/` | One layout per repository type, each extending its parent |
| `conf/layouts/{layout-id}.yaml` | The structure of one repository type; its words live at the same relative path under each language root |
| `{language}/conf/layouts/{layout-id}.yaml` | Titles and descriptions for one layout, keyed by path; only for the paths and placeholders that layout adds |
| `schemas/uc-automa-config.schema.yaml` | Schema for a repository's .uc-automa.yaml |
| `schemas/front-matter.schema.yaml` | Front matter for each document type: directive, guide, decision, reference and session |
| `lib/{package}/cli.py` | The uc-automa command and its subcommands |

### Offerings

| Path | What it holds |
| --- | --- |
| `offerings/` | One self-contained directory per offering; the directory list is the catalogue |
| `offerings/{offering-id}/` | One offering |
| `offerings/{offering-id}/offering.yaml` | What the offering delivers: each file or managed block, its destination, sync mode, and the directives it implements |
| `offerings/{offering-id}/files/` | Language-neutral payload files, laid out as they land in the receiving repository |
| `offerings/{offering-id}/{language}/` | Language-specific payload text, such as signpost wording |

```yaml
# offerings/version-file/offering.yaml
format: 1
id: "version-file"
title: "VERSION file"
sync_mode: seed_if_missing        # planted once, then owned by the repository
items:
  - source: "files/VERSION"
    dest: "VERSION"
```

The format is uc-portage's: `offering.schema.yaml` lives there, because the tool that reads a format owns its contract (uc-automa 0015).

### Directives

| Path | What it holds |
| --- | --- |
| `{language}/docs/directives/` | Rules in force, one rule per file: the automa proper |
| `{language}/docs/directives/{domain}/` | The directives of one domain |
| `{language}/docs/directives/{domain}/{slug}{version}.md` | One directive; its identifier is {domain}/{slug}, and it names the check that enforces it |

Each directive names the check that enforces it in `sat:enforced_by`, and each check names its directive in every finding. `uc-automa check --list` shows the pairs.

### Fixtures and templates

| Path | What it holds |
| --- | --- |
| `tests/fixtures/conformance/{domain}/{slug}/` | Samples for one directive |
| `tests/fixtures/conformance/{domain}/{slug}/pass/` | Cases the directive's check must accept, one directory each |
| `tests/fixtures/conformance/{domain}/{slug}/fail/` | Cases the directive's check must reject, one directory each |
| `{language}/templates/` | Authoring skeletons, one per document type, carrying every front matter key its type requires, with placeholders to replace |

## What is not here

- No per-repository manifests: each repository declares its own subscriptions (uc-automa 0008).
- No copied scripts: code lives in an installed package.
- No forge-specific directories such as `.github/`.
- No empty or placeholder directories, and no drafts on the default branch.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.3.0 | 2026-10-23 | Accepted | Added the eleventy-site layout to the chain, with its own section; identifiers come from uc-automa metadata new-id |
| 0.2.0 | 2026-10-09 | Accepted | Revised to the foundation brief: uc-automa names, en-ca, the layout chain, kinds and from_offering, the licences, init; descriptions taken from the layout words; relicensed CC-BY-SA-4.0 |
| 0.1.0 | 2026-10-07 | Draft | Initial guide: one section per directory, with illustrations and YAML examples |

## License

This document, *Directory Guide*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
