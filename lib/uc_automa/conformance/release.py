"""release/annotated-version-tags: release tags name and mark exactly
the release.

Every tag is a release tag: "v" and the contents of VERSION, with dots,
such as v0.1.0. It is annotated, its message names the repository and
the version, and it points at a commit whose VERSION is that version
and whose CHANGELOG.md has that version's section, dated the day the
tag was made in the tagger's own time zone.
"""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

from . import Repository, check

TAG = re.compile(r"^v(\d+\.\d+\.\d+)$")
FIELDS = "%(refname:short)%00%(objecttype)%00%(taggerdate:format:%Y-%m-%d)%00%(contents)%01"


def git(root: Path, *args: str):
    return subprocess.run([shutil.which("git") or "git", "-C", str(root), *args],
                          capture_output=True)


@check("conformance.release.annotated_version_tags",
       "release/annotated-version-tags")
def annotated_version_tags(repo: Repository):
    if not (repo.root / ".git").exists() or shutil.which("git") is None:
        return []
    listing = git(repo.root, "for-each-ref", "refs/tags", f"--format={FIELDS}")
    if listing.returncode != 0:
        return [("refs/tags", "git could not list the tags: "
                 + listing.stderr.decode("utf-8", "replace").strip())]
    findings = []
    repository = repo.config.repository if repo.config else None
    for record in listing.stdout.decode("utf-8").split("\x01"):
        record = record.lstrip("\n")
        if not record:
            continue
        name, kind, date, message = record.split("\x00", 3)
        shown = f"refs/tags/{name}"
        match = TAG.match(name)
        if not match:
            findings.append((shown, "a release tag is v and the version with "
                                    "dots, such as v0.1.0"))
            continue
        version = match.group(1)
        if kind != "tag":
            findings.append((shown, "release tags are annotated"))
            continue
        if version not in message or (repository and repository not in message):
            findings.append((shown, f"the tag message names the repository "
                                    f"and the version: {repository} "
                                    f"{version}"))
        tagged = git(repo.root, "show", f"{name}^{{commit}}:VERSION")
        if tagged.returncode != 0 or \
                tagged.stdout.decode("utf-8").strip() != version:
            findings.append((shown, f"VERSION at the tagged commit is not "
                                    f"{version}"))
        changelog = git(repo.root, "show", f"{name}^{{commit}}:CHANGELOG.md")
        heading = f"## [{version}] - {date}"
        if changelog.returncode != 0 or \
                heading not in changelog.stdout.decode("utf-8").splitlines():
            findings.append((shown, f"CHANGELOG.md at the tagged commit has "
                                    f"no section {heading!r}"))
    return findings
