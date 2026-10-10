"""uc-automa offerings: resolve .uc-automa.yaml and hand off to uc-portage.

uc-automa decides which offerings a repository takes and where they come
from; uc-portage does the carrying. A repository pinned to a release
takes the offerings shipped in the installed uc-automa package; uc-automa
itself, with automa_version: self, takes its own offerings/ directory
(uc-automa 0020).
"""

from __future__ import annotations

from pathlib import Path
from typing import List

from uc_portage import cli as portage_cli

from .config import Config
from .paths import offerings_dir


def offerings_source(config: Config) -> Path:
    if config.is_self:
        return config.root / "offerings"
    return offerings_dir()


def portage_args(command: str, config: Config, extra: List[str]) -> List[str]:
    args = [command, "--source", str(offerings_source(config)),
            "--target", str(config.root), "--language", config.language]
    if config.subscribe:
        args += ["--offering", ",".join(config.subscribe)]
    return args + extra


def run(command: str, config: Config, extra: List[str]) -> int:
    if not config.subscribe:
        print("[uc-automa] the repository subscribes to no offerings")
        return 0
    return portage_cli.main(portage_args(command, config, extra))
