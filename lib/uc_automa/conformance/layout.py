"""layout/repository-layout: the repository holds what its layout says.

The root is always closed: every top-level entry must be described by
the layout. Inside, a directory marked closed: true admits only entries
matching a declared child; other directories are open. Required paths
must be present, source-language paths in the source language's root,
and required paths inside a language root in every language root that
is present. A path marked from_offering: X, when present or required,
needs the repository to subscribe to X. The sidecar must be named for
the repository declared in .uc-automa.yaml.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

from . import Repository, check
from .layouts import LANGUAGE_ROOT, Layout, Node, segment_regex

Tree = Dict[str, Optional[dict]]


def build_tree(files: List[str]) -> Tree:
    tree: Tree = {}
    for rel in files:
        parts = rel.split("/")
        here = tree
        for part in parts[:-1]:
            here = here.setdefault(part, {})
        here[parts[-1]] = None
    return tree


def matching_node(nodes: List[Node], entry: str, is_dir: bool,
                  layout: Layout) -> Tuple[Optional[Node], dict]:
    """The node an entry matches, literal names before patterns."""
    name = entry + "/" if is_dir else entry
    wanted = "directory" if is_dir else "file"
    ordered = [n for n in nodes if n.is_literal] + \
              [n for n in nodes if not n.is_literal]
    for node in ordered:
        if node.type != wanted:
            continue
        if node.is_literal:
            if node.name == name:
                return node, {}
            continue
        match = segment_regex(node.name, layout.placeholders).match(name)
        if match:
            return node, match.groupdict()
    return None, {}


@check("conformance.layout.repository_layout", "layout/repository-layout")
def repository_layout(repo: Repository):
    layout, config = repo.layout, repo.config
    if layout is None or config is None:
        return [(".uc-automa.yaml", "no layout to check against; run "
                                    "uc-automa init")]
    findings = set()
    walk(layout.tree, build_tree(repo.files), "", True, None, layout,
         config, findings)
    for node in always_required(layout.tree):
        if node.from_offering and node.from_offering not in config.subscribe:
            findings.add((node.path, f"layout {layout.id!r} delivers this "
                          f"path from offering {node.from_offering!r}, "
                          f"which the repository does not subscribe to"))
    return sorted(findings)


def always_required(nodes: List[Node]) -> List[Node]:
    out = []
    for node in nodes:
        if node.required is True:
            out.append(node)
            out.extend(always_required(node.children))
    return out


def walk(nodes: List[Node], entries: Tree, prefix: str, closed: bool,
         language: Optional[str], layout: Layout, config, findings: set):
    present: Dict[str, List[dict]] = {}
    for entry in sorted(entries):
        sub = entries[entry]
        is_dir = sub is not None
        shown = prefix + entry + ("/" if is_dir else "")
        node, groups = matching_node(nodes, entry, is_dir, layout)
        if node is None:
            if closed:
                findings.add((shown, f"not described by layout "
                                     f"{layout.id!r}"))
            continue
        present.setdefault(node.name, []).append(groups)
        if "repository" in groups and groups["repository"] != config.repository:
            findings.add((shown, f"named for repository "
                                 f"{groups['repository']!r}, but "
                                 f".uc-automa.yaml declares "
                                 f"{config.repository!r}; expected "
                                 f".{config.repository}.assets/"))
        if node.from_offering and node.from_offering not in config.subscribe:
            findings.add((shown, f"layout {layout.id!r} delivers this path "
                                 f"from offering {node.from_offering!r}, "
                                 f"which the repository does not subscribe "
                                 f"to"))
        if is_dir:
            walk(node.children, sub, shown, node.closed,
                 groups.get("language", language), layout, config, findings)

    for node in nodes:
        found = present.get(node.name, [])
        if node.required is True:
            missing = not found
        elif node.required == "source-language":
            if node.path.startswith(LANGUAGE_ROOT) and node.parent is None:
                missing = not any(g.get("language") == layout.source_language
                                  for g in found)
            else:
                missing = language == layout.source_language and not found
        else:
            missing = False
        if missing:
            shown = prefix + (node.name if node.is_literal else node.name)
            if node.required == "source-language" and node.parent is None:
                shown = node.name.replace("{language}",
                                          layout.source_language)
            findings.add((shown, f"required by layout {layout.id!r} but "
                                 f"missing"))
