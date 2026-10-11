# uc-automa

The station every Vishpala repository passes through. uc-automa defines the rules once, as directives; publishes what repositories may take from it, as offerings; and provides the `uc-automa` command, which checks a repository against the rules and carries offerings into it through [uc-portage](https://github.com/steelcj/uc-portage).

## What it holds

| Kind | Home | How a repository gets it |
| --- | --- | --- |
| Things a tool runs | `lib/uc_automa/`, `conf/`, `schemas/` | Installed as the `uc-automa` package, pinned per repository |
| Things people and AI read | `en-ca/docs/` | Read at the pinned version, never copied |
| Things that must live in each repository | `offerings/` | Carried in by subscription, declared in the repository's own `.uc-automa.yaml` |

The rules are the directives under [`en-ca/docs/directives/`](en-ca/docs/directives/). The reasons are the decision records under [`en-ca/docs/decisions/`](en-ca/docs/decisions/). [`en-ca/docs/README.md`](en-ca/docs/README.md) is the generated index of every document.

## Requirements

Python 3.8 or later, PyYAML, uc-portage 0.1.x and git.

## Install

uc-portage is not published to a package index, so install it first, from its checkout:

```sh
python3 -m pip install ../uc-portage
python3 -m pip install .
uc-automa --version
```

## Use

In a new repository:

```sh
uc-automa init --repository osat-manager-restic --layout osat-manager
uc-automa offerings apply
uc-automa docs index
uc-automa check
```

| Command | What it does |
| --- | --- |
| `uc-automa init --repository NAME --layout ID` | Writes `.uc-automa.yaml` once: the name, the layout type, the installed version as the pin, `en-ca`, and the offerings the layout requires |
| `uc-automa check` | Checks the repository against every directive that has a check; `--list` shows them |
| `uc-automa offerings plan`, `status`, `apply`, `harvest` | Carries the subscribed offerings with uc-portage |
| `uc-automa docs index` | Regenerates `en-ca/docs/README.md` |
| `uc-automa translations` | Reports untranslated and stale layout words |

The guides explain [the repository layouts](en-ca/docs/guides/repository/directory-guide-v0.2.0.md) and [creating an OSAT manager repository](en-ca/docs/guides/new-repository/creating-an-osat-manager-repository-v0.4.0.md).

## Platform status

| Platform | Status |
| --- | --- |
| Linux | Tests pass on Python 3.12 (Ubuntu 24.04) and Python 3.8 (AlmaLinux 8 container) |
| macOS | Not yet verified |
| Windows | Not yet verified |

## Develop

```sh
python3 -m pip install -e ../uc-portage -e .
python3 -m unittest discover -s tests
uc-automa check
```

uc-automa subscribes to its own offerings with `automa_version: self`, so every offering is exercised here before any other repository receives it.

## License

uc-automa follows the REUSE convention: [`REUSE.toml`](REUSE.toml) records which licence covers which paths, and [`LICENSES/`](LICENSES/) holds their texts. Code, including configuration, schemas and offering payloads, is licensed under the MIT License, whose text is also in [`LICENSE`](LICENSE). Documentation is licensed under the Creative Commons Attribution 4.0 International License. Releases are MIT and CC BY 4.0 from 0.1.0, the first public release (uc-automa 0025).

This document, *uc-automa*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
