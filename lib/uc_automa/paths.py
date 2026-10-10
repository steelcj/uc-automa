"""Where uc-automa's data lives: conf/, each language's conf/, schemas/
and offerings/.

Each is kept once, in the repository, and mapped into the package by
pyproject.toml under uc_automa.data. uc-portage's resolver finds it in an
installed package, or in a proven checkout of uc-automa (uc-automa 0019).
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict

from uc_portage.errors import PortageError
from uc_portage.resources import data_dir

from .errors import AutomaError

PACKAGE = "uc_automa"
PROJECT = "uc-automa"
LANGUAGE_DIR = re.compile(r"^[a-z]{2}(-[a-z]{2})?$")


def _find(subpackage: str, repo_path: str) -> Path:
    try:
        return data_dir(PACKAGE, PROJECT, f"uc_automa.data.{subpackage}",
                        repo_path)
    except PortageError as exc:
        raise AutomaError(str(exc)) from None


def conf_dir() -> Path:
    return _find("conf", "conf")


def schemas_dir() -> Path:
    return _find("schemas", "schemas")


def offerings_dir() -> Path:
    return _find("offerings", "offerings")


def text_dirs() -> Dict[str, Path]:
    """Each language's conf/ directory, keyed by language tag.

    Installed, they sit under uc_automa/data/text/<tag with underscore>/;
    in a checkout, at <tag>/conf/ beside conf/.
    """
    conf = conf_dir()
    packaged = conf.parent / "text"
    if conf.parent.name == "data" and packaged.is_dir():
        return {d.name.replace("_", "-"): d for d in sorted(packaged.iterdir())
                if d.is_dir() and LANGUAGE_DIR.match(d.name.replace("_", "-"))}
    return text_dirs_in(conf.parent)


def text_dirs_in(root: Path) -> Dict[str, Path]:
    """Language conf/ directories at the root of a repository."""
    return {d.name: d / "conf" for d in sorted(root.iterdir())
            if d.is_dir() and LANGUAGE_DIR.match(d.name)
            and (d / "conf").is_dir()}
