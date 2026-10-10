"""The conformance checker: each check enforces one directive.

A check is a function taking a Repository and returning Findings. Each
is registered with the identifier of the directive it enforces, so every
finding names its directive, and every directive with a check names the
check in its sat:enforced_by front matter.
"""

from __future__ import annotations

import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Callable, Dict, List, Optional

from ..config import Config
from ..errors import AutomaError
from .layouts import Layout

FIXTURES = "tests/fixtures/"


@dataclass(frozen=True)
class Finding:
    directive: str
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.directive}: {self.path}: {self.message}"


@dataclass
class Repository:
    """What a check needs: the root, its files, its configuration, its
    merged layout and where the layouts' structure and words came from."""

    root: Path
    files: List[str]
    config: Optional[Config] = None
    layout: Optional[Layout] = None
    conf_dir: Optional[Path] = None
    text_dirs: Dict[str, Path] = field(default_factory=dict)

    def checked_files(self) -> List[str]:
        """Files a content or naming check looks at: everything except
        the conformance fixtures, which break rules on purpose."""
        return [f for f in self.files if not f.startswith(FIXTURES)]

    def path(self, rel: str) -> Path:
        return self.root.joinpath(*PurePosixPath(rel).parts)


def list_files(root: Path) -> List[str]:
    """The files a repository contains, as POSIX paths relative to root.

    In a git working tree: tracked files plus untracked files git does not
    ignore, so build output and caches listed in .gitignore are left out.
    Outside git, as in a release tarball: every file. .git/ is never
    counted.
    """
    git = shutil.which("git")
    if git and (root / ".git").exists():
        result = subprocess.run(
            [git, "-C", str(root), "ls-files", "-z", "--cached", "--others",
             "--exclude-standard"],
            capture_output=True)
        if result.returncode != 0:
            # A git working tree that git will not list is an error, not
            # a reason to count build output and caches as well.
            raise AutomaError(f"git could not list the files in {root}: "
                              f"{result.stderr.decode('utf-8').strip()}")
        names = [n.decode("utf-8") for n in result.stdout.split(b"\0") if n]
        return sorted({n for n in names
                       if root.joinpath(*n.split("/")).is_file()})
    files = []
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if rel.parts[0] == ".git" or not path.is_file():
            continue
        files.append(rel.as_posix())
    return sorted(files)


Check = Callable[[Repository], List[Finding]]


@dataclass(frozen=True)
class Registered:
    id: str               # such as conformance.naming.part_separator
    directive: str        # such as naming/part-separator
    run: Check


REGISTRY: List[Registered] = []


def check(check_id: str, directive: str):
    """Register a check under the directive it enforces. The function
    returns (path, message) pairs; each becomes a Finding naming the
    directive."""
    def wrap(func):
        def run(repo: Repository) -> List[Finding]:
            return [Finding(directive, path, message)
                    for path, message in func(repo)]
        run.__name__ = func.__name__
        run.__doc__ = func.__doc__
        REGISTRY.append(Registered(check_id, directive, run))
        return run
    return wrap


def all_checks() -> List[Registered]:
    # Importing the modules registers their checks.
    from . import (docs, layout, licensing, markdown, metadata,  # noqa: F401
                   naming, release, translations)
    return list(REGISTRY)


def run_checks(repo: Repository,
               only: Optional[List[str]] = None) -> List[Finding]:
    findings: List[Finding] = []
    for registered in all_checks():
        if only and registered.id not in only \
                and registered.directive not in only:
            continue
        findings.extend(registered.run(repo))
    return findings
