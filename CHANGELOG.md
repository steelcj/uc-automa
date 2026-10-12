# Changelog

All notable changes to uc-automa are recorded here, in the form of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). uc-automa follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Decision record 0026, the release ceremony: `uc-automa release bump`, `cut` and `publish`, to replace the copied scripts in 0.2.0.
- Decision record 0027, verification without an end-to-end scenario: what verifies a platform for uc-portage and uc-automa.
- Decision record 0028, wheels with each release: each release carries its wheels, matched against the verification record, with SSH signatures that Windows can check without gpg.
- The README states what verifies Windows: the unit tests, `uc-automa check` on itself, and an install from wheels with `pip install --no-index` inside a network cut.

### Changed

- The README installs into a virtual environment, `.venv`, because the Python manage-python installs, like the system Python of several Linux distributions, refuses package installs.
- The README links to uc-automa 0027 for what verifies a platform, instead of carrying its own Windows criteria.
- The README's Windows status records the Windows run of 2026-10-11, which met both criteria; Windows is not yet marked verified, pending the network cut's self-test on a network with IPv6.
- The README installs PyYAML as pure Python, with `--no-binary pyyaml` and `PYYAML_FORCE_LIBYAML=0`, so no platform needs a C compiler, and records that this costs uc-automa and uc-portage no speed.
- The README installs a release from its tag, with uc-portage, and keeps installing from checkouts for development.
- The OSAT manager process, 0.4.0: its subscribe stage installs uc-automa and uc-portage from their release tags, and removes blocks file-fairy managed, which uc-portage never takes over.

### Fixed

- The install tests make their virtual environments with symbolic links outside Windows, as `python -m venv` does, so they also run on manage-python's Python 3.8, whose interpreter cannot start when copied.

## [0.1.0] - 2026-10-11

### Added

- Layouts split by repository type: `base`, `python-tool`, `uc-automa` and `osat-manager`, with the extends rules, and their en-ca words.
- `uc-automa check`, with a check for each of twelve directives: the repository layout, layout translations, lowercase names, portable names, versions in filenames, the part separator, SPDX slugs, no heading numbers, rights matching REUSE, document front matter, the generated documentation index, and annotated version tags.
- `uc-automa init`, which writes `.uc-automa.yaml` once.
- `uc-automa offerings plan`, `status`, `apply` and `harvest`, handing off to uc-portage.
- `uc-automa docs index` and `uc-automa translations`.
- Eight offerings: line-endings, editorconfig, version-file, changelog, claude-signpost, reuse, license-mit and license-cc-by-4-0.
- `schemas/uc-automa-config.schema.yaml` and `schemas/front-matter.schema.yaml`.
- Decision records 0001 to 0025, directives, templates, the directory guide, the OSAT manager process at 0.3.0, and the session record of the foundation build, covering the three independent reviews of osat-manager-restic's verifier and the tested offline step.
- Licensed MIT for code and CC BY 4.0 for documentation and content (uc-automa 0025).
