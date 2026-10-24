"""The naming directives: one check each.

Names are split as the naming directives describe them: an optional
leading dot, a stem made of parts joined by --, an optional -vX.Y.Z
version suffix, and an extension. Python files and packages, the
conventional uppercase repository files and licence texts are the
written exceptions.
"""

from __future__ import annotations

import re
from pathlib import PurePosixPath
from typing import Iterable, List, Optional, Tuple

import yaml

from .. import frontmatter
from . import Repository, check

UPPERCASE_FILES = {"README.md", "LICENSE", "CHANGELOG.md", "VERSION",
                   "ROADMAP.md", "CONTRIBUTING.md", "CLAUDE.md"}
TOOL_FILES = {"REUSE.toml",      # named by the tool that reads it
              "eleventy.config.js"}
LICENCE_DIR = "LICENSES"
COMPOUND_EXTENSIONS = (".schema.yaml",)

# Names Eleventy requires by default inside an eleventy-site's input
# directory, src/ (uc-automa 0037): its data and includes directories,
# and the suffix of its directory and template data files.
ELEVENTY_LAYOUT = "eleventy-site"
ELEVENTY_INPUT = "src/"
ELEVENTY_DIRS = {"_data", "_includes"}
ELEVENTY_DATA_SUFFIXES = (".11tydata.json", ".11tydata.js")

VERSION_SUFFIX = re.compile(r"-v(\d+)\.(\d+)\.(\d+)$")
HYPHENATED_VERSION = re.compile(r"-v\d+-\d+-\d+(?=$|\.)")
LOWERCASE = re.compile(r"^[a-z0-9.-]+$")
PYTHON_NAME = re.compile(r"^[a-z_][a-z0-9_]*(\.py)?$")
WORDS = r"[a-z0-9]+(-[a-z0-9]+)*"
PARTS = re.compile(rf"^{WORDS}(--{WORDS})*$")

WINDOWS_RESERVED = {"con", "prn", "aux", "nul"} | \
    {f"com{i}" for i in range(1, 10)} | {f"lpt{i}" for i in range(1, 10)}
FORBIDDEN = set('<>:"\\|?*')
MAX_PATH = 100


def components(files: Iterable[str]) -> List[Tuple[str, str, bool]]:
    """Every distinct path component as (path so far, name, is_dir)."""
    seen = {}
    for rel in files:
        parts = rel.split("/")
        for i, name in enumerate(parts):
            shown = "/".join(parts[: i + 1])
            is_dir = i < len(parts) - 1
            seen[shown + ("/" if is_dir else "")] = (name, is_dir)
    return [(p, n, d) for p, (n, d) in sorted(seen.items())]


def exempt(path: str, name: str) -> bool:
    """The written exceptions to the lowercase rule."""
    parts = path.rstrip("/").split("/")
    if name in UPPERCASE_FILES or name in TOOL_FILES:
        return True
    if LICENCE_DIR in parts[:-1] or name == LICENCE_DIR:
        return True
    return python_name(path, name)


def is_eleventy_site(repo: Repository) -> bool:
    return repo.layout is not None and ELEVENTY_LAYOUT in repo.layout.chain


def strip_eleventy_suffix(name: str) -> str:
    """page.11tydata.json is checked as page.json: Eleventy fixes the
    .11tydata part, and the stem before it follows the rule."""
    for suffix in ELEVENTY_DATA_SUFFIXES:
        if name.endswith(suffix):
            return name[: -len(suffix)] + suffix[suffix.rfind("."):]
    return name


def python_name(path: str, name: str) -> bool:
    """Python modules and packages take underscores, because Python
    cannot import hyphens. They live under lib/ and tests/."""
    top = path.split("/")[0]
    return top in ("lib", "tests") and bool(PYTHON_NAME.match(name)) \
        and ("_" in name or name.endswith(".py"))


NAME_SHAPE = re.compile(r"^(?P<stem>.*?)(?P<version>-v\d+\.\d+\.\d+)?"
                        r"(?P<ext>\.[a-z0-9]+)?$")


def split_name(name: str, is_dir: bool):
    """Return (leading dot, stem, version suffix, extension)."""
    dot = "." if name.startswith(".") else ""
    rest = name[len(dot):]
    for compound in COMPOUND_EXTENSIONS:
        if rest.endswith(compound):
            return dot, rest[: -len(compound)], "", compound
    match = NAME_SHAPE.match(rest)
    return (dot, match.group("stem"), match.group("version") or "",
            match.group("ext") or "")


@check("conformance.naming.lowercase_names", "naming/lowercase-names")
def lowercase_names(repo: Repository):
    findings = []
    eleventy = is_eleventy_site(repo)
    for path, name, is_dir in components(repo.checked_files()):
        if exempt(path, name):
            continue
        if eleventy and path.startswith(ELEVENTY_INPUT):
            if is_dir and name in ELEVENTY_DIRS:
                continue
            name = strip_eleventy_suffix(name)
        if not LOWERCASE.match(name.lstrip(".")):
            findings.append((path, "use lowercase letters, digits and "
                                   "hyphens only"))
            continue
        dot, stem, version, ext = split_name(name, is_dir)
        if "." in stem:
            findings.append((path, "a dot may appear only inside a "
                                   "-vX.Y.Z suffix or before the "
                                   "extension"))
    return findings


@check("conformance.naming.portable_names", "naming/portable-names")
def portable_names(repo: Repository):
    findings = []
    files = repo.checked_files()
    for path, name, is_dir in components(files):
        base = name.split(".")[0].lower()
        if base in WINDOWS_RESERVED:
            findings.append((path, f"{name!r} is reserved on Windows"))
        if name.endswith(".") or name.endswith(" "):
            findings.append((path, "a name may not end with a dot or a "
                                   "space"))
        if FORBIDDEN & set(name):
            findings.append((path, "contains a character Windows forbids "
                                   "in names"))
        if " " in name or not name.isascii():
            findings.append((path, "spaces and non-ASCII characters are "
                                   "not allowed in names"))
    for rel in files:
        if len(rel) > MAX_PATH:
            findings.append((rel, f"path is {len(rel)} characters; the "
                                  f"limit is {MAX_PATH}"))
    seen = {}
    for path, name, is_dir in components(files):
        key = path.lower()
        if key in seen and seen[key] != path:
            findings.append((path, f"differs only by case from "
                                   f"{seen[key]!r}"))
        seen.setdefault(key, path)
    return findings


def document_version(repo: Repository, rel: str) -> Optional[str]:
    """The sat:version of a document under a language's docs/, or None.
    Templates and other files are versioned by the repository's release."""
    parts = rel.split("/")
    if not rel.endswith(".md") or len(parts) < 3 or parts[1] != "docs":
        return None
    try:
        data, _ = frontmatter.read(repo.path(rel))
    except (ValueError, yaml.YAMLError, UnicodeDecodeError):
        return None
    if not data or "sat:version" not in data:
        return None
    return str(data["sat:version"])


@check("conformance.naming.versions_in_filenames",
       "naming/versions-in-filenames")
def versions_in_filenames(repo: Repository):
    findings = []
    for path, name, is_dir in components(repo.checked_files()):
        if HYPHENATED_VERSION.search(name):
            findings.append((path, "a version in a filename uses dots, as "
                                   "in -v0.1.0, never -v0-1-0"))
    for rel in repo.checked_files():
        version = document_version(repo, rel)
        if version is None:
            continue
        name = PurePosixPath(rel).name
        stem = name[: -len(".md")]
        match = VERSION_SUFFIX.search(stem)
        major = int(version.split(".")[0]) if version[0].isdigit() else 0
        if major < 1:
            if match is None:
                findings.append((rel, f"sat:version is {version}, below "
                                      f"1.0.0, so the filename ends in "
                                      f"-v{version}.md"))
            elif match.group(0) != f"-v{version}":
                findings.append((rel, f"the filename says "
                                      f"{match.group(0)[2:]} but "
                                      f"sat:version is {version}"))
        elif match is not None:
            findings.append((rel, f"sat:version is {version}; from 1.0.0 "
                                  f"the filename carries no version"))
    return findings


@check("conformance.naming.part_separator", "naming/part-separator")
def part_separator(repo: Repository):
    findings = []
    for path, name, is_dir in components(repo.checked_files()):
        if exempt(path, name) or not LOWERCASE.match(name.lstrip(".")):
            continue
        dot, stem, version, ext = split_name(name, is_dir)
        if "." in stem or not stem:
            continue
        if not PARTS.match(stem):
            findings.append((path, "parts are joined by --, words within a "
                                   "part by a single -, with no hyphen at "
                                   "either end"))
    return findings


def spdx_slug(identifier: str) -> str:
    """GPL-3.0-or-later becomes gpl-3-0-or-later."""
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]", "-",
                                     identifier.lower())).strip("-")


@check("conformance.naming.spdx_slugs", "naming/spdx-slugs")
def spdx_slugs(repo: Repository):
    findings = []
    offering_ids = sorted({f.split("/")[1] for f in repo.checked_files()
                           if f.startswith("offerings/")
                           and f.count("/") >= 2})
    for offering_id in offering_ids:
        if "licence" in offering_id:
            findings.append((f"offerings/{offering_id}/", "identifiers "
                             "follow the standard they name: license, as "
                             "in SPDX and REUSE"))
        if not offering_id.startswith("license-"):
            continue
        texts = sorted({PurePosixPath(f).stem for f in repo.checked_files()
                        if f.startswith(f"offerings/{offering_id}/")
                        and f"/{LICENCE_DIR}/" in f and f.endswith(".txt")})
        if len(texts) != 1:
            findings.append((f"offerings/{offering_id}/", "a licence "
                             "offering delivers exactly one licence text "
                             "from LICENSES/"))
            continue
        want = "license-" + spdx_slug(texts[0])
        if offering_id != want:
            findings.append((f"offerings/{offering_id}/", f"delivers "
                             f"{texts[0]}, so its identifier is {want}"))
    return findings
