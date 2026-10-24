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

Install a release from its tag, together with uc-portage, which uc-automa depends on:

```sh
python -m venv .venv
PYYAML_FORCE_LIBYAML=0 .venv/bin/python -m pip install --no-binary pyyaml \
    "git+https://github.com/steelcj/uc-portage@v0.1.0" \
    "git+https://github.com/steelcj/uc-automa@v0.1.0"
.venv/bin/uc-automa --version
```

On Windows, in Command Prompt, with Git on your `PATH`:

```bat
python -m venv .venv
set PYYAML_FORCE_LIBYAML=0
.venv\Scripts\python -m pip install --no-binary pyyaml "git+https://github.com/steelcj/uc-portage@v0.1.0" "git+https://github.com/steelcj/uc-automa@v0.1.0"
.venv\Scripts\uc-automa --version
```

pip installs into a virtual environment, `.venv` in the current directory, because the Python that manage-python installs refuses package installs, as do the system Pythons of Debian, Ubuntu and other distributions that mark theirs externally managed. Activate it to put `uc-automa` on your `PATH`: `. .venv/bin/activate`, or `.venv\Scripts\activate` in Command Prompt.

`python` is the command manage-python installs, on Linux, macOS and Windows alike. With another Python, use its own command instead, such as `python3`. On Debian and Ubuntu the system Python's `venv` module needs the `python3-venv` package first: `sudo apt install python3-venv`.

uc-portage is not published to a package index, so name both in the same command; installing uc-automa alone fails to find uc-portage.

The installed version is the one `uc-automa init` pins in a repository's `.uc-automa.yaml`, and every later command requires the installed version to match the pin (uc-automa 0020). Everyone working in a repository installs the same tag. The pre-commit hook runs the `uc-automa` installed in your environment.

To work on uc-automa itself, install both from checkouts, as [Develop](#develop) shows.

### Why PyYAML is built as pure Python

uc-automa and uc-portage depend on PyYAML, whose optional C extension, built against libyaml, needs a C compiler wherever PyPI has no PyYAML wheel for your Python: PyYAML 6.0.3 has none for Python 3.15 on Windows. `--no-binary pyyaml` with `PYYAML_FORCE_LIBYAML=0` builds PyYAML from its source as pure Python on every platform instead, giving the same `py3-none-any` wheel everywhere, with no compiler.

The speed cost is none for uc-automa or uc-portage. They read and write YAML only through `yaml.safe_load` and `yaml.safe_dump`, which run PyYAML's Python code whether or not the extension is present; the extension speeds up only the `CLoader` and `CSafeLoader` family, which they do not use. Measured on 2026-10-11 on Linux with Python 3.12, loading all 19 YAML files uc-portage and uc-automa ship, 31 KB, took 41 ms with the pure build and 43 ms with PyYAML's binary wheel; `CSafeLoader` would have taken 5 ms. Another program in the same environment that imports `CSafeLoader` without a fallback fails with `ImportError`, so give the tools their own virtual environment if anything else there needs the extension.

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

The guides explain [the repository layouts](en-ca/docs/guides/repository/directory-guide-v0.3.0.md) and [creating an OSAT manager repository](en-ca/docs/guides/new-repository/creating-an-osat-manager-repository-v0.6.0.md).

## Platform status

| Platform | Status |
| --- | --- |
| Linux | Tests pass on Python 3.12 (Ubuntu 24.04) and Python 3.8 (AlmaLinux 8 container) |
| macOS | Not yet verified |
| Windows | Not yet verified. On 2026-10-11, on Windows 11 with Python 3.15.0 from manage-python, the unit tests and an offline install from wheels passed ([record](https://github.com/steelcj/osat-manager-restic/blob/main/tests/e2e/windows/2026-10-11--windows-test-run.md)), but that run predates the verification run and does not count as one |

A platform is verified for uc-automa by a verification run: its unit tests, also on the oldest Python it supports, an offline install inside a network cut from the wheels a release would publish, and the installed tool doing its job on a real repository, recorded under `tests/e2e/<platform>/`, as [uc-automa 0027](en-ca/docs/decisions/0027--verification-without-an-end-to-end-scenario-v0.1.0.md) defines.

## Develop

From a checkout of uc-automa, with uc-portage's checkout beside it as `../uc-portage`:

```sh
python -m venv .venv
PYYAML_FORCE_LIBYAML=0 .venv/bin/python -m pip install --no-binary pyyaml -e ../uc-portage -e .
.venv/bin/python -m unittest discover -s tests
.venv/bin/uc-automa check
```

On Windows, in Command Prompt, with Git on your `PATH`:

```bat
python -m venv .venv
set PYYAML_FORCE_LIBYAML=0
.venv\Scripts\python -m pip install --no-binary pyyaml -e ..\uc-portage -e .
.venv\Scripts\python -m unittest discover -s tests
.venv\Scripts\uc-automa check
```

uc-automa subscribes to its own offerings with `automa_version: self`, so every offering is exercised here before any other repository receives it.

## License

uc-automa follows the REUSE convention: [`REUSE.toml`](REUSE.toml) records which licence covers which paths, and [`LICENSES/`](LICENSES/) holds their texts. Code, including configuration, schemas and offering payloads, is licensed under the MIT License, whose text is also in [`LICENSE`](LICENSE). Documentation is licensed under the Creative Commons Attribution 4.0 International License. Releases are MIT and CC BY 4.0 from 0.1.0, the first public release (uc-automa 0025).

This document, *uc-automa*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
