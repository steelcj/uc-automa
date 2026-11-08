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

- The metadata checker as its own repository and executable, with all the resources it needs and its own configuration (the owner's direction of 2026-11-07). It does not check `dc:language` (uc-automa 0040).
- Make `test_check_passes_on_uc_automa` pass again: `uc-automa check` must find nothing in uc-automa itself. It has failed since `218bdec` (2026-11-07), which added `docs/overviews/` without describing it in the `uc-automa` layout ("layout/repository-layout: en-ca/docs/overviews/: not described by layout 'uc-automa'", one of 2 findings). Since 0040 was implemented, 4 findings remain, all content: describe `overviews/` in `conf/layouts/uc-automa.yaml` (or move the overview somewhere the layout already allows); give `en/docs/sessions/osat-manager-git-where-things-stand-after-2026-10-21.md` front matter and a session record's name; and settle the overview's `dc:rights`, AGPL-3.0-or-later, against `REUSE.toml`'s CC-BY-4.0.
- `uc-automa docs index` lists only files git tracks. Today it also lists untracked files git does not ignore, so a draft left in a checkout lands in the generated index; on 2026-10-11 it picked up two untracked session notes.
- A decision on how a decision's version changes after it is accepted: uc-automa 0029 covers directives only, and 0030's open question was answered in place on 2026-10-11 with its version left at 0.1.0.
- In the release after the ceremony: migrate sat-doc-automa's style rules into directives, one rule per file, each with a check where one is possible: commas rather than em dashes, no horizontal rules, no hard wraps, Citation Anchor Pairs.
- Verify end to end on macOS and Windows; uc-automa reaches 1.0.0 only when all three platforms are verified.
- `uc-automa docs fetch`, checking out the pinned version's documentation into the per-user data directory.
- A compatibility range for `automa_version`, to be reconsidered at 1.0.0.
- Publish uc-portage and uc-automa somewhere pip can install them from, so the pre-commit hook can install itself.
