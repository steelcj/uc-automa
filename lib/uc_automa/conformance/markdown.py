"""markdown/no-heading-numbers: headings carry no section numbering.

The rule forbids numbering a section, as in "## 3. Release",
"### 3.1 Scope" or "## 4) Notes". A version number inside a heading is
not numbering and is allowed, as in "## [0.1.0] - 2026-10-09", so only
numbering patterns are flagged.
"""

from __future__ import annotations

import re

from . import Repository, check

HEADING = re.compile(r"^#{1,6}\s+(.*)$")
FENCE = re.compile(r"^\s*(```|~~~)")
NUMBERING = [
    re.compile(r"^\d+[.)]\s"),                  # 3. Release, 3) Release
    re.compile(r"^\d+\.\d+[.)]?\s"),            # 3.1 Scope, 3.1. Scope
    re.compile(r"^\d+(\.\d+){2,}[.)]\s"),       # 3.1.2. Detail
    re.compile(r"^\d+\s+[A-Za-z]"),             # 3 Release
]


def numbered(text: str) -> bool:
    return any(p.match(text) for p in NUMBERING)


@check("conformance.markdown.no_heading_numbers", "markdown/no-heading-numbers")
def no_heading_numbers(repo: Repository):
    findings = []
    for rel in repo.checked_files():
        if not rel.endswith(".md"):
            continue
        in_fence = False
        with repo.path(rel).open(encoding="utf-8") as f:
            for number, line in enumerate(f, start=1):
                if FENCE.match(line):
                    in_fence = not in_fence
                    continue
                match = None if in_fence else HEADING.match(line.rstrip("\n"))
                if match and numbered(match.group(1)):
                    findings.append((f"{rel}:{number}", "heading carries "
                                     "section numbering"))
    return findings
