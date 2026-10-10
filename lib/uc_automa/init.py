"""uc-automa init: write a repository's .uc-automa.yaml, once.

The file that declares subscriptions cannot arrive by subscription
(uc-automa 0023), so init writes it from its arguments: the repository's
name and layout type, the installed uc-automa version as the pin, en-ca
as the language, and the subscriptions the layout chain needs, which are
the offerings named by from_offering on paths the layout requires.
"""

from __future__ import annotations

from pathlib import Path
from typing import List

import yaml
from uc_portage.schema import validate

from . import __version__
from .config import CONFIG_FILENAME, SELF, config_schema, is_uc_automa
from .conformance.layouts import Layout, load_layout
from .paths import conf_dir
from .errors import AutomaError

DEFAULT_LANGUAGE = "en-ca"


def required_offerings(layout: Layout) -> List[str]:
    found: List[str] = []

    def walk(nodes):
        for node in nodes:
            if node.required is not True:
                continue
            if node.from_offering and node.from_offering not in found:
                found.append(node.from_offering)
            walk(node.children)
    walk(layout.tree)
    return found


def init(root: Path, repository: str, layout_id: str) -> Path:
    path = root / CONFIG_FILENAME
    if path.exists():
        raise AutomaError(f"{path} already exists; init writes it once and "
                          f"the repository owns it afterwards")
    self_hosted = is_uc_automa(root)
    conf = root / "conf" if self_hosted else conf_dir()
    layout = load_layout(conf, layout_id)
    data = {
        "format": 1,
        "repository": repository,
        "layout": layout_id,
        "automa_version": SELF if self_hosted else __version__,
        "language": DEFAULT_LANGUAGE,
        "subscribe": required_offerings(layout),
    }
    errors = validate(data, config_schema())
    if errors:
        raise AutomaError("the arguments do not make a valid "
                          ".uc-automa.yaml:\n  " + "\n  ".join(errors))
    with path.open("x", encoding="utf-8", newline="\n") as f:
        yaml.safe_dump(data, f, sort_keys=False)
    return path
