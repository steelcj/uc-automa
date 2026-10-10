"""Shared scaffolding for the uc-automa tests.

The tests run from a checkout: lib/ is put first on the import path. They
need uc-portage importable, installed or editable.
"""

from __future__ import annotations

import contextlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LIB = REPO / "lib"
FIXTURES = REPO / "tests" / "fixtures" / "conformance"
if str(LIB) not in sys.path:
    sys.path.insert(0, str(LIB))

from uc_automa.config import load_config  # noqa: E402
from uc_automa.conformance import Repository, list_files  # noqa: E402
from uc_automa.conformance.layouts import load_layout  # noqa: E402
from uc_automa.paths import text_dirs_in  # noqa: E402


def fixture_repository(case: Path) -> Repository:
    """A fixture case as a repository. Its layouts come from the case's
    own conf/ when it has one, otherwise from uc-automa's."""
    config = None
    if (case / ".uc-automa.yaml").is_file():
        config = load_config(case, check_pin_now=False)
    if (case / "conf").is_dir():
        conf, texts = case / "conf", text_dirs_in(case)
    else:
        conf, texts = REPO / "conf", text_dirs_in(REPO)
    layout = load_layout(conf, config.layout) if config else None
    return Repository(case, list_files(case), config, layout, conf, texts)


@contextlib.contextmanager
def materialised(case: Path):
    """A fixture case ready to check. A case holding repo.bundle is a git
    repository, kept as a bundle so that no nested repository is
    committed; it is cloned into a scratch directory first."""
    bundle = case / "repo.bundle"
    if not bundle.is_file():
        yield case
        return
    with tempfile.TemporaryDirectory() as tmp:
        clone = Path(tmp) / case.name
        subprocess.run([shutil.which("git") or "git", "clone", "-q",
                        str(bundle), str(clone)], check=True,
                       capture_output=True)
        subprocess.run([shutil.which("git") or "git", "-C", str(clone),
                        "fetch", "-q", "--tags", str(bundle)],
                       check=True, capture_output=True)
        yield clone
