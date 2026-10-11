# Roadmap

Forward plan only; completed items move to [CHANGELOG.md](CHANGELOG.md).

## Next release

- Build the release ceremony decided in 0026: `uc-automa release bump`, `cut` and `publish` in `lib/uc_automa/release/`, replacing the copied `bump-version.py`, `cut-release.py` and `publish-release.py`, with signed tags and `SHA256SUMS` from one RSA release key.
- The `retire-copied-scripts` offering, with guarded retractions (uc-portage 0004) whose checksums come from sat-doc-automa's history; requires uc-portage 0.2.0.
- Migrate sat-doc-automa's style rules into directives, one rule per file, each with a check where one is possible: commas rather than em dashes, no horizontal rules, no hard wraps, Citation Anchor Pairs.
- `uc-automa metadata new-id`, replacing `uuidgen -r` run by hand.

## Later

- Verify end to end on macOS and Windows; uc-automa reaches 1.0.0 only when all three platforms are verified.
- `uc-automa docs fetch`, checking out the pinned version's documentation into the per-user data directory.
- A compatibility range for `automa_version`, to be reconsidered at 1.0.0.
- Publish uc-portage and uc-automa somewhere pip can install them from, so the pre-commit hook can install itself.
