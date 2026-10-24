# Changelog

All notable changes to uc-automa are recorded here, in the form of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). uc-automa follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Decision record 0026, the release ceremony: `uc-automa release bump`, `cut` and `publish`, to replace the copied scripts in 0.2.0.
- Decision record 0027, verification without an end-to-end scenario: what verifies a platform for uc-portage and uc-automa.
- Decision record 0028, wheels with each release: each release carries its wheels, matched against the verification record, with SSH signatures that Windows can check without gpg.
- Decision record 0029, version bumps for rule changes: before 1.0.0 a directive's minor version changes when its meaning changes, its patch version for wording only.
- Decision record 0030, where the release keys are published: `release-keys/` in uc-automa and a page on vishpala.com, with the README fetching the key by `git clone` and the fingerprint compared by hand.
- Decision record 0031, a test platform repository: `uc-test-platform` holds the drivers, the network cut, the verification run and the instance recipes.
- Decision record 0032, SSH signatures required with wheels, and SSH-signed tags; tag verification is documented for Linux and macOS only in 0.2.0.
- The directive `release/readme-install-tag` and its check: `uc-automa check` fails when `README.md` installs the repository at any tag but `v` and its `VERSION`.
- Decision record 0037 and the `eleventy-site` layout, extending `base`: an Eleventy website requires `eleventy.config.js`, `package.json`, `package-lock.json` and `src/`, and may hold `themes/` and, for a site deployed to Netlify, `netlify.toml`, with en-ca words for each path.
- Decision record 0038 and `uc-automa metadata new-id`, which prints a fresh random UUID as a `urn:uuid:` value, replacing `uuidgen -r` run by hand. The templates and the directory guide now name it.
- The README states what verifies Windows: the unit tests, `uc-automa check` on itself, and an install from wheels with `pip install --no-index` inside a network cut.

### Changed

- `naming/lowercase-names`: its check now also accepts the names Eleventy requires by default as names a tool requires, as the directive's text already allows: `eleventy.config.js`, and in an eleventy-site repository `src/`'s `_data/` and `_includes/` and the `.11tydata.json` and `.11tydata.js` suffixes. The directive keeps its version (uc-automa 0029).
- Directory guide 0.3.0: the eleventy-site layout in the chain and in its own section. The OSAT manager guide's reference to the guide's version 0.2.0 now points at that version by commit.
- `release/readme-install-tag` 0.2.0: wherever the README installs a dependency from a git reference, the reference is a release tag the dependency's `pyproject.toml` range allows.
- `release/annotated-version-tags` 0.2.0: the release commit may also update `README.md`'s install references to the new tag.
- Decisions 0027 and 0028: the verification run serves the README's online install from local mirrors, so the release tag is pushed only after the run passes, and the cut rewrites the README's install tag.
- The README's Linux and macOS commands run `python`, the command manage-python installs, as the Windows ones do: on Ubuntu `python3` is the system Python, whose `venv` needs `python3-venv`. A note covers other Pythons.
- The README installs into a virtual environment, `.venv`, because the Python manage-python installs, like the system Python of several Linux distributions, refuses package installs.
- The README's Develop section creates the virtual environment too, gives the Command Prompt commands, and holds the install from checkouts, which the Install section now points to.
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
