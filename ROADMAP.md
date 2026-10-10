# Roadmap

Forward plan only; completed items move to [CHANGELOG.md](CHANGELOG.md).

## Next release

- Port the release ceremony, `bump-version.py`, `cut-release.py` and `publish-release.py` from sat-doc-automa, into `lib/uc_automa/release/` as `uc-automa release bump`, `cut` and `publish`, with signed release tags.
- Migrate sat-doc-automa's style rules into directives, one rule per file, each with a check where one is possible: commas rather than em dashes, no horizontal rules, no hard wraps, Citation Anchor Pairs.
- `uc-automa metadata new-id`, replacing `uuidgen -r` run by hand.

## Later

- Verify end to end on macOS and Windows; uc-automa reaches 1.0.0 only when all three platforms are verified.
- `uc-automa docs fetch`, checking out the pinned version's documentation into the per-user data directory.
- A compatibility range for `automa_version`, to be reconsidered at 1.0.0.
- Publish uc-portage and uc-automa somewhere pip can install them from, so the pre-commit hook can install itself.
