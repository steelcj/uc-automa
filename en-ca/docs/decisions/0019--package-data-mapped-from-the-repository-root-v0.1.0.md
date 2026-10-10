---
title: "Decision: Package Data Mapped from the Repository Root"
dc:title: "Decision: Package Data Mapped from the Repository Root"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "packaging, package data, pyproject.toml, setuptools, editable install, resolver"
dc:description: "Data such as schemas/ and conf/ lives once at the repository root and is mapped into the package by pyproject.toml alone; editable installs and checkouts fall back to the repository root only after proving it is the package's own checkout."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:7ba945fe-2f0d-45fb-a347-bda6d12294be"
dc:language: "en-CA"
dc:rights: "CC-BY-SA-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: Package Data Mapped from the Repository Root

Version: 0.1.0
Status: Accepted

## Context

uc-portage and uc-automa read data that lives at the repository root, where people and other tools find it: `schemas/`, `conf/`, each language's `conf/` and `offerings/`. An installed package must carry that data, and nothing may be stored twice.

Three routes were tried on uc-portage on 2026-10-09, each with a normal install and an editable install, on Python 3.12 and 3.8:

| Route | Normal install | Editable install |
| --- | --- | --- |
| `[tool.setuptools.package-dir]` mapping only | works | the package cannot be found; setuptools' editable finder maps only a nested package that has an `__init__.py` |
| Mapping plus an empty `__init__.py` in each data directory | works | works |
| A `setup.py` build hook copying the data in | works | fails in the same way as the mapping alone |

The second route puts a Python file inside data directories, including the `en-ca/` language tree.

## Decision

- `pyproject.toml` alone maps each data directory into the package, such as `"uc_portage.schemas" = "schemas"` and `"uc_automa.data.conf" = "conf"`, with `package-data` naming the files. There is no `setup.py`.
- One resolver, `uc_portage.resources.data_dir`, finds the data. uc-automa imports it rather than keeping a copy.
- An installed package reads its own copy through the mapped package.
- An editable install or a checkout run without installing falls back to the repository root, but only after proving it is in that package's checkout: the root holds a `pyproject.toml` whose project name matches. Otherwise the resolver fails with an error naming the missing data. It never reads from an unexpected directory.
- The fallback depends on decision D4's `lib/<package>/` depth (uc-automa 0005): the package sits two levels below the repository root. Changing D4 means changing the resolver.
- Tests cover all three cases: a wheel installed into a fresh virtual environment, an editable install, and a run straight from a checkout.

## Consequences

- An editable install needs pip 21.3 or later, because the project is defined by `pyproject.toml` alone. Some Python 3.8 builds bundle an older pip, which must be upgraded first.
- `setup.py` is not a path in any layout, and `schemas/` is optional in the python-tool layout.
- Paths are handled with `pathlib` throughout, so the resolver behaves the same on Windows and macOS.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | Accepted | Initial version |

## License

This document, *Decision: Package Data Mapped from the Repository Root*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
