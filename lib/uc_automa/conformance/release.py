"""The release directives.

release/annotated-version-tags: release tags name and mark exactly the
release. Every tag is a release tag: "v" and the contents of VERSION,
with dots, such as v0.1.0. It is annotated, its message names the
repository and the version, and it points at a commit whose VERSION is
that version and whose CHANGELOG.md has that version's section, dated
the day the tag was made in the tagger's own time zone.

release/readme-install-tag: wherever README.md installs this repository
from a git reference, such as git+https://github.com/owner/name@v0.1.0,
the reference is "v" and the contents of VERSION.
"""

from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

from . import Repository, check

TAG = re.compile(r"^v(\d+\.\d+\.\d+)$")
# A git reference to a repository in a URL: /name@ref or /name.git@ref.
INSTALL_REF = re.compile(r"/(?P<name>[A-Za-z0-9._-]+?)(?:\.git)?@(?P<ref>[^\s\"'`<>()\[\]]+)")
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


@check("conformance.release.readme_install_tag",
       "release/readme-install-tag")
def readme_install_tag(repo: Repository):
    repository = repo.config.repository if repo.config else None
    if not repository or "README.md" not in repo.files \
            or "VERSION" not in repo.files:
        return []
    expected = "v" + repo.path("VERSION").read_text(encoding="utf-8").strip()
    findings = []
    lines = repo.path("README.md").read_text(encoding="utf-8").splitlines()
    for number, line in enumerate(lines, 1):
        for match in INSTALL_REF.finditer(line):
            if match.group("name") == repository \
                    and match.group("ref") != expected:
                findings.append(("README.md", f"line {number} installs "
                                 f"{repository}@{match.group('ref')}; "
                                 f"VERSION makes it {repository}@{expected}"))
    return findings
