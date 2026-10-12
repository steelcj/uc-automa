# Roadmap

Forward plan only; completed items move to [CHANGELOG.md](CHANGELOG.md).

## Next release

Scope approved on 2026-10-11 for 0.2.0:

- Build the release ceremony decided in 0026 and extended by 0028: `uc-automa release bump`, `cut` and `publish` in `lib/uc_automa/release/`, replacing the copied `bump-version.py`, `cut-release.py` and `publish-release.py`. The cut rewrites the README's own install tag; publish builds and compares the wheels, refuses sums that differ from the verification record, and signs with the release keys.
- `[tool.uc-automa.release]` pins in `pyproject.toml`, and the README's `Install offline` section.
- The README's `Get the release key` section (uc-automa 0030), before `Install offline`, and tag verification documented for Linux and macOS only, with the Windows gap stated (uc-automa 0032).
- `release-keys/` with the SSH release key's allowed-signers line, and its entry in the `uc-automa` layout (uc-automa 0030). Releases and tags are signed with the SSH key only; there is no OpenPGP key for 0.2.0 (uc-automa 0032).
- The verification runs use `uc-test-platform` at a recorded commit; it is released after uc-automa 0.2.0 (uc-automa 0031).
- The `retire-copied-scripts` offering, with guarded retractions (uc-portage 0004) whose checksums come from sat-doc-automa's history; requires uc-portage 0.2.0.
- `uc-automa metadata new-id`, replacing `uuidgen -r` run by hand.
- Release order, approved on 2026-10-11: uc-portage 0.2.0 is cut and published first, with the ceremony of uc-automa's candidate commit installed editable; that candidate already depends on `uc-portage>=0.2.0,<0.3.0` and its README names `uc-portage@v0.2.0`. uc-automa 0.2.0's release commit is that candidate commit plus the cut, and nothing else. If it differs, uc-portage's release runs are repeated with the new uc-automa commit.
- Before each tag is pushed, verification runs on Linux and Windows (uc-automa 0027), and the release wheels match their records (uc-automa 0028).

## Later

- In 0.3.0: migrate sat-doc-automa's style rules into directives, one rule per file, each with a check where one is possible: commas rather than em dashes, no horizontal rules, no hard wraps, Citation Anchor Pairs.
- Verify end to end on macOS and Windows; uc-automa reaches 1.0.0 only when all three platforms are verified.
- `uc-automa docs fetch`, checking out the pinned version's documentation into the per-user data directory.
- A compatibility range for `automa_version`, to be reconsidered at 1.0.0.
- Publish uc-portage and uc-automa somewhere pip can install them from, so the pre-commit hook can install itself.
