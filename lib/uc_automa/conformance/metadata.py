"""metadata/front-matter: documents carry the front matter of their type.

A document under {language}/docs/ is checked against the definition for
its type in schemas/front-matter.schema.yaml, chosen by its directory.
Its dc:language matches its language root. A directive's sat:directive
is its own path, {domain}/{slug}, and every check it names in
sat:enforced_by exists. In uc-automa itself, every check is named by
the directive it enforces.
"""

from __future__ import annotations

from typing import Dict

import yaml
from uc_portage.schema import validate

from .. import frontmatter
from ..paths import schemas_dir
from . import Repository, all_checks, check
from .naming import VERSION_SUFFIX

TYPES = {"directives": "directive", "guides": "guide",
         "decisions": "decision", "references": "reference",
         "sessions": "session"}


def front_matter_schema(repo: Repository) -> dict:
    base = repo.root / "schemas" if repo.config and repo.config.is_self \
        else schemas_dir()
    with (base / "front-matter.schema.yaml").open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def doc_type(rel: str):
    """(language, type) for a path such as en-ca/docs/guides/x/y.md."""
    parts = rel.split("/")
    if len(parts) >= 4 and parts[1] == "docs" and parts[2] in TYPES:
        return parts[0], TYPES[parts[2]]
    return None, None


def language_tag(language: str) -> str:
    """en-ca becomes en-CA."""
    head, _, tail = language.partition("-")
    return head + ("-" + tail.upper() if tail else "")


@check("conformance.metadata.front_matter", "metadata/front-matter")
def front_matter(repo: Repository):
    findings = []
    schema = None
    enforced: Dict[str, str] = {}
    for rel in repo.checked_files():
        if not rel.endswith(".md"):
            continue
        language, kind = doc_type(rel)
        if kind is None:
            continue
        if schema is None:
            schema = front_matter_schema(repo)
        try:
            data, _ = frontmatter.read(repo.path(rel))
        except (ValueError, yaml.YAMLError) as exc:
            findings.append((rel, f"front matter is not readable: {exc}"))
            continue
        if data is None:
            findings.append((rel, "has no front matter"))
            continue
        sub = dict(schema["$defs"][kind], **{"$defs": schema["$defs"]})
        for error in validate(data, sub):
            findings.append((rel, f"{kind} front matter: {error}"))
        if data.get("dc:language") != language_tag(language):
            findings.append((rel, f"dc:language is "
                                  f"{data.get('dc:language')!r} in the "
                                  f"{language}/ root, expected "
                                  f"{language_tag(language)!r}"))
        if kind == "directive":
            parts = rel.split("/")
            stem = parts[-1][: -len(".md")]
            stem = VERSION_SUFFIX.sub("", stem)
            want = f"{parts[3]}/{stem}" if len(parts) == 5 else None
            if data.get("sat:directive") != want:
                findings.append((rel, f"sat:directive is "
                                      f"{data.get('sat:directive')!r}, "
                                      f"expected {want!r}"))
            for check_id in data.get("sat:enforced_by") or []:
                enforced[check_id] = data.get("sat:directive")
    if repo.config is not None and repo.config.is_self:
        registered = {r.id: r.directive for r in all_checks()}
        for check_id, directive in sorted(enforced.items()):
            if check_id not in registered:
                findings.append((directive or "", f"names check "
                                 f"{check_id!r}, which does not exist"))
            elif registered[check_id] != directive:
                findings.append((directive or "", f"names check "
                                 f"{check_id!r}, which enforces "
                                 f"{registered[check_id]!r}"))
        for check_id, directive in sorted(registered.items()):
            if check_id not in enforced:
                findings.append((directive, f"no directive names check "
                                 f"{check_id!r} in sat:enforced_by"))
    return findings
