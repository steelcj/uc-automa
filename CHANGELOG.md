# Changelog

All notable changes to uc-automa are recorded here, in the form of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). uc-automa follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Layouts split by repository type: `base`, `python-tool`, `uc-automa` and `osat-manager`, with the extends rules, and their en-ca words.
- `uc-automa check`, with a check for each of eleven directives: the repository layout, layout translations, lowercase names, portable names, versions in filenames, the part separator, SPDX slugs, no heading numbers, rights matching REUSE, document front matter, and the generated documentation index.
- `uc-automa init`, which writes `.uc-automa.yaml` once.
- `uc-automa offerings plan`, `status`, `apply` and `harvest`, handing off to uc-portage.
- `uc-automa docs index` and `uc-automa translations`.
- Nine offerings: line-endings, editorconfig, version-file, changelog, claude-signpost, reuse, and one per licence category.
- `schemas/uc-automa-config.schema.yaml` and `schemas/front-matter.schema.yaml`.
- Decision records 0001 to 0023, directives, templates, the directory guide, the OSAT manager process, and the session record of the foundation build.
