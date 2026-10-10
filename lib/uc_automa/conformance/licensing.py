"""licensing/rights-match-reuse: a document's dc:rights names the
licence REUSE says covers it.

REUSE.toml sets licences by path (uc-automa 0001). A file that differs
from its path's default carries its own SPDX-License-Identifier line,
which wins. When several annotations match a path, the last one wins.

Python 3.8 has no TOML parser, so REUSE.toml is read for the keys this
check needs: each [[annotations]] table's path, as a string or an array
of strings, and its SPDX-License-Identifier.
"""

from __future__ import annotations

import re
from typing import List, Optional, Tuple

import yaml

from .. import frontmatter
from . import Repository, check

TABLE = re.compile(r"^\s*\[\[annotations\]\]\s*$", re.M)
PATH_KEY = re.compile(r'^\s*path\s*=\s*(\[.*?\]|"[^"]*")', re.M | re.S)
LICENSE_KEY = re.compile(r'^\s*SPDX-License-Identifier\s*=\s*"([^"]+)"', re.M)
# The pattern below names the tag it looks for, so REUSE is told to
# skip it rather than read it as this file's own licence.
# REUSE-IgnoreStart
FILE_TAG = re.compile(r"SPDX-License-Identifier:\s*([A-Za-z0-9.+-]+)")
# REUSE-IgnoreEnd
STRING = re.compile(r'"([^"]*)"')


def glob_regex(pattern: str) -> "re.Pattern":
    """REUSE globs: * matches within one path component, ** across them."""
    out, i = [], 0
    while i < len(pattern):
        if pattern.startswith("**", i):
            out.append(".*")
            i += 2
        elif pattern[i] == "*":
            out.append("[^/]*")
            i += 1
        else:
            out.append(re.escape(pattern[i]))
            i += 1
    return re.compile("^" + "".join(out) + "$")


def read_annotations(text: str) -> List[Tuple[List["re.Pattern"], str]]:
    annotations = []
    for chunk in TABLE.split(text)[1:]:
        path = PATH_KEY.search(chunk)
        licence = LICENSE_KEY.search(chunk)
        if not path or not licence:
            continue
        patterns = STRING.findall(path.group(1))
        annotations.append(([glob_regex(p) for p in patterns],
                            licence.group(1)))
    return annotations


def covering_licence(repo: Repository, rel: str,
                     annotations) -> Optional[str]:
    with repo.path(rel).open(encoding="utf-8") as f:
        for line in f:
            tag = FILE_TAG.search(line)
            if tag and not line.lstrip().startswith(("|", ">")):
                return tag.group(1)
    found = None
    for patterns, licence in annotations:
        if any(p.match(rel) for p in patterns):
            found = licence
    return found


@check("conformance.licensing.rights_match_reuse",
       "licensing/rights-match-reuse")
def rights_match_reuse(repo: Repository):
    reuse = repo.root / "REUSE.toml"
    if not reuse.is_file():
        return [("REUSE.toml", "missing; it records which licence covers "
                               "which paths")]
    annotations = read_annotations(reuse.read_text(encoding="utf-8"))
    findings = []
    for rel in repo.checked_files():
        if not rel.endswith(".md"):
            continue
        try:
            data, _ = frontmatter.read(repo.path(rel))
        except (ValueError, yaml.YAMLError):
            continue
        if not data or "dc:rights" not in data:
            continue
        licence = covering_licence(repo, rel, annotations)
        if licence is None:
            findings.append((rel, "no licence covers this file in "
                                  "REUSE.toml"))
        elif str(data["dc:rights"]) != licence:
            findings.append((rel, f"dc:rights is {data['dc:rights']}, but "
                                  f"REUSE.toml licenses it {licence}"))
    return findings
