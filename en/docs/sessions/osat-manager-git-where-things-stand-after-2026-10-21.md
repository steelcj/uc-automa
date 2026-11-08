# osat-manager-git: where things stand after 2026-10-21

The full record is the uc-automa session record, `en-ca/docs/sessions/2026-10-21--osat-manager-git-and-the-manager-pattern-v0.1.0.md` (https://github.com/steelcj/uc-automa). This note is the short version, to start the next chat from.

## Decided

- **conda-forge git on Linux, macOS and Windows.** uc-radar *Git on Windows* 0.2.0: conda-forge git in Trial, MinGit in Assess as the fallback, dugite-native in Hold.
- **The package's system gitconfig is kept.** manage-git writes its own per-version file that includes the package's and sets the baseline, read through `GIT_CONFIG_SYSTEM`. Other managers start git from the `invocation` that `--check --json` reports (osat-manager-git 0001).
- **Baseline 1 and conventions** (osat-manager-git 0002, open as PR #2):
  - git 2.49.0 or later and `core.autocrlf = false`; on Windows also `core.longpaths = true` and Git Credential Manager; no `safe.directory`;
  - `manager.yaml` uses `arch` and `verification.signature`;
  - locks ship with the manager at `locks/<version>/<subdir>.json`;
  - Windows gets a real `git.exe` through a `current` junction;
  - uninstall leaves nothing behind and writes no registry;
  - gettext message catalogues come later, through osat-manager-core.
- **uc-automa 0033:** managers run on manage-python's manager runtime, never on a version they expose.
- **uc-automa 0034:** option C for mise. OSAT managers stay per-tool and standard-library on client machines; mise is the reference and an approved release-time tool for locks.
- **uc-automa 0035:** the shared package is osat-manager-core, in its own repository, installed once into the manager runtime.
- **uc-automa 0036:** a check exits 0 when ready, 2 when not ready, 1 when it could not run.
- **Process guide** *Creating an OSAT Manager Repository* is at 0.6.0.
- **No `sat:migration_status`.** satx *Ingress Verification Stamp* v0.0.1, under consideration, has SAT mark content verified at ingress, with the SAT version that ingressed it.

## Open

- [ ] Create `steelcj/osat-manager-core` on GitHub; Claude can't create repositories.

- [ ] Review and merge osat-manager-git#2.

- [ ] osat-manager-python#1: the manager runtime, `--manager-runtime VERSION`, automatic migration, `--uninstall` with a self-deleting batch file on Windows, and osat-manager-core installed into the runtime.

- [ ] The release-time lock tool, and signed locks for git 2.56.0.

- [ ] manage-git's install, switch, aliases, protection and uninstall, with the Windows launcher's ownership marker and `--check` resolving manage-git's own launchers.

- [ ] End-to-end runs, Linux in Incus first, then Windows x64 in the VM:

  - whether `%PROGRAMDATA%\Git\config` is still read when `GIT_CONFIG_SYSTEM` is set;
  - the junction with an editor.

  `win-arm64` has no reference implementation.

- [ ] The name of SAT's ingress stamp, for example `sat:conformsTo`.

- [ ] The radar entry for conda-forge as a binary source.

## Working notes for Claude

- Each repository's CLAUDE.md says to ask before pushing; Christopher has been choosing branches with PRs, merged on his say.
- Session clones are shallow, so set up branch tracking after pushing.
- manage-git's tests need Python 3.14.