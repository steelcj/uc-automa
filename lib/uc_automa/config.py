"""Loading and validating a repository's .uc-automa.yaml."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List

import yaml
from uc_portage.resources import normalise_name, project_name
from uc_portage.schema import validate

from . import __version__
from .paths import PROJECT, schemas_dir
from .errors import AutomaError

CONFIG_FILENAME = ".uc-automa.yaml"
SELF = "self"


@dataclass
class Config:
    root: Path
    repository: str
    layout: str
    automa_version: str
    language: str
    subscribe: List[str]

    @property
    def is_self(self) -> bool:
        return self.automa_version == SELF


def config_schema() -> dict:
    with (schemas_dir() / "uc-automa-config.schema.yaml").open(
            encoding="utf-8") as f:
        return yaml.safe_load(f)


def is_uc_automa(root: Path) -> bool:
    """True when root is a uc-automa checkout, by the same test the data
    resolver uses: its pyproject.toml names the uc-automa project."""
    pyproject = root / "pyproject.toml"
    if not pyproject.is_file():
        return False
    name = project_name(pyproject)
    return name is not None and normalise_name(name) == PROJECT


def load_config(root: Path, check_pin_now: bool = True) -> Config:
    path = root / CONFIG_FILENAME
    if not path.is_file():
        raise AutomaError(f"{path} not found; run uc-automa init first")
    with path.open(encoding="utf-8") as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            raise AutomaError(f"{path}: not valid YAML: {exc}") from None
    errors = validate(data, config_schema())
    if errors:
        raise AutomaError(f"{path} does not match "
                          f"uc-automa-config.schema.yaml:\n  "
                          + "\n  ".join(errors))
    if len(set(data["subscribe"])) != len(data["subscribe"]):
        raise AutomaError(f"{path}: an offering is subscribed twice")
    config = Config(root, data["repository"], data["layout"],
                    data["automa_version"], data["language"],
                    list(data["subscribe"]))
    if check_pin_now:
        check_pin(config)
    return config


def check_pin(config: Config) -> None:
    """The pin must name the installed uc-automa exactly (uc-automa 0020).

    Below 1.0.0 the offering format may change between minor versions,
    so only an exact match is safe. self is allowed only in uc-automa.
    """
    if config.is_self:
        if not is_uc_automa(config.root):
            raise AutomaError(
                f"automa_version: self is valid only in uc-automa itself; "
                f"{config.root} is not a uc-automa checkout. Pin a "
                f"released version, such as {__version__}")
        return
    if config.automa_version != __version__:
        raise AutomaError(
            f"{config.root / CONFIG_FILENAME} pins uc-automa "
            f"{config.automa_version}, but uc-automa {__version__} is "
            f"installed. Either install uc-automa {config.automa_version}, "
            f"or update automa_version to {__version__} and review what "
            f"changes")
