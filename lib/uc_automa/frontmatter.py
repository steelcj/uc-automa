"""Reading the YAML front matter of a Markdown document."""

from __future__ import annotations

from pathlib import Path
from typing import Optional, Tuple

import yaml

FENCE = "---"


def split(text: str) -> Tuple[Optional[dict], str]:
    """Return (front matter, body). Front matter is None when the text
    does not open with a --- fence; an unclosed or invalid block raises
    ValueError."""
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != FENCE:
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() == FENCE:
            data = yaml.safe_load("".join(lines[1:i])) or {}
            if not isinstance(data, dict):
                raise ValueError("front matter is not a mapping")
            return data, "".join(lines[i + 1:])
    raise ValueError("front matter is not closed with ---")


def read(path: Path) -> Tuple[Optional[dict], str]:
    with path.open(encoding="utf-8") as f:
        return split(f.read())
