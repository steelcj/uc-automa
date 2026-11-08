# Roadmap

Forward plan only; completed items move to [CHANGELOG.md](CHANGELOG.md).

## Next release

Scope approved on 2026-10-11 for 0.2.0, and moved unchanged to 0.3.0 when 0.2.0 was cut by hand (uc-automa 0039):

- Build the release ceremony decided in 0026 and extended by 0028: `uc-automa release bump`, `cut` and `publish` in `lib/uc_automa/release/`, replacing the copied `bump-version.py`, `cut-release.py` and `publish-release.py`. The cut rewrites the README's own install tag; publish builds and compares the wheels, refuses sums that differ from the verification record, and signs with the release keys.
- `[tool.uc-automa.release]` pins in `pyproject.toml`, and the README's `Install offline` section.
- The README's `Get the release key` section (uc-automa 0030), before `Install offline`, and tag verification documented for Linux and macOS only, with the Windows gap stated (uc-automa 0032).
- `release-keys/` with the SSH release key's allowed-signers line, and its entry in the `uc-automa` layout (uc-automa 0030). Releases and tags are signed with the SSH key only; there is no OpenPGP key for 0.3.0 (uc-automa 0032).
- Decide the allowed-signers principal before `release-keys/` is created: 0028 and 0030 use the owner's email address, and uc-processes' release-key guide uses `vishpala-release`. A decision record settles it; `release-keys/`, the README sections and the guide follow it. Raised in uc-processes' *Process: Releasing a Repository* on 2026-11-07.
- The verification runs use `uc-test-platform` at a recorded commit; it is released after uc-automa 0.3.0 (uc-automa 0031).
- The `retire-copied-scripts` offering, with guarded retractions (uc-portage 0004) whose checksums come from sat-doc-automa's history; requires uc-portage 0.2.0.
- Release order, approved on 2026-10-11: uc-portage 0.2.0 is cut and published first, with the ceremony of uc-automa's candidate commit installed editable; that candidate already depends on `uc-portage>=0.2.0,<0.3.0` and its README names `uc-portage@v0.2.0`. uc-automa 0.3.0's release commit is that candidate commit plus the cut, and nothing else. If it differs, uc-portage's release runs are repeated with the new uc-automa commit.
- Before each tag is pushed, verification runs on Linux and Windows (uc-automa 0027), and the release wheels match their records (uc-automa 0028).

## Later

- Follow the documentation's move from `en-ca/` to `en/` in the code: `DEFAULT_LANGUAGE` in `lib/uc_automa/init.py` is still `en-ca`, so `uc-automa translations` reports "the source language has no words for this layout" for every layout, and `test_translations_report_nothing_for_en_ca` fails since the move (2026-11-07). That needs a decision record superseding 0004 (*Language root en-ca*), then the code, the tests and their fixtures updated to match. It probably also affects how `conformance/metadata.py` maps a language folder to `dc:language`.
  - Found on 2026-11-07 while trying it ("option 1": `en` is both the folder and the language tag): the config, layouts, packaging (`uc_automa.data.text.en` from `en/conf`), offerings, `REUSE.toml`, `DEFAULT_LANGUAGE` and every document's `dc:language` can move to `en`, which takes `uc-automa check` from 132 findings to 63. Two things still block it:
  - **Resolve soon: `source-language` paths are checked against the layout's language, not the repository's.** `conformance/layout.py` checks paths marked `required: source-language` against `layout.source_language`, the language of uc-automa's own layout text. Once that is `en`, every repository using uc-automa's layouts needs an `en/` folder: the `pass/decision-record` and `pass/python-tool` fixtures, which are `en-ca`, fail with "`en/`: required by layout 'python-tool' but missing", and so would every downstream `en-ca` repository on upgrading. The likely fix is to check against the repository's configured language instead (the two were both `en-ca` until now, so the difference never showed), with a minor bump of `layout/repository-layout`.
  - **The front-matter schema requires a region:** `dc:language` must match `^[a-z]{2}-[A-Z]{2}$` in `schemas/front-matter.schema.yaml`, so `en` is refused (59 findings). Widen it to `^[a-z]{2}(-[A-Z]{2})?$`, as language folders are already matched, and bump `metadata/front-matter` (minor), whose rule says "`en-CA` under `en-ca/`".
  - Then: `uc-automa offerings apply` (the signpost's text changes), `uc-automa docs index`, and decision 0040 superseding 0004 and 0007.
  - Longer term, the owner wants the metadata checker as its own repository and executable, with all the resources it needs and its own configuration, so that a folder and its `dc:language` can differ where a repository needs that, such as `en-CA` documents under `en/`.
- Make `test_check_passes_on_uc_automa` pass again: `uc-automa check` must find nothing in uc-automa itself. It has failed since `218bdec` (2026-11-07), which added `docs/overviews/` without describing it in the `uc-automa` layout ("layout/repository-layout: en-ca/docs/overviews/: not described by layout 'uc-automa'", one of 2 findings). Since the `en/` move above, the check reports 132 findings against 13 directives, so fix the move first, then describe `overviews/` in `conf/layouts/uc-automa.yaml` (or move the overview somewhere the layout already allows).
- `uc-automa docs index` lists only files git tracks. Today it also lists untracked files git does not ignore, so a draft left in a checkout lands in the generated index; on 2026-10-11 it picked up two untracked session notes.
- A decision on how a decision's version changes after it is accepted: uc-automa 0029 covers directives only, and 0030's open question was answered in place on 2026-10-11 with its version left at 0.1.0.
- In the release after the ceremony: migrate sat-doc-automa's style rules into directives, one rule per file, each with a check where one is possible: commas rather than em dashes, no horizontal rules, no hard wraps, Citation Anchor Pairs.
- Verify end to end on macOS and Windows; uc-automa reaches 1.0.0 only when all three platforms are verified.
- `uc-automa docs fetch`, checking out the pinned version's documentation into the per-user data directory.
- A compatibility range for `automa_version`, to be reconsidered at 1.0.0.
- Publish uc-portage and uc-automa somewhere pip can install them from, so the pre-commit hook can install itself.
