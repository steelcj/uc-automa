"""Layouts: loading, the extends chain, and the merged tree.

A layout under conf/layouts/ describes what a repository of one type
contains. A layout may extend one parent; the chain is resolved parent
first, then child, into one merged tree. The extends rules (uc-automa
0013) are enforced while merging:

- one parent per layout; chains are allowed; a cycle is an error;
- format and source_language match all the way up the chain;
- a child may add paths, including children of an inherited directory,
  and may add placeholders, but may not redefine an inherited one;
- a child may tighten required (false < source-language < true) and
  never loosen it; it may close an open directory and never reopen one;
- a child may set kind or from_offering on an inherited path that has
  none, and never change one already set; it may not remove a path or
  change its type;
- kind is declared only on top-level nodes, and descendants inherit it;
- source-language is valid only on paths that begin with {language}.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set

import yaml

from ..errors import AutomaError

FILE_KEYS = {"format", "describes", "extends", "source_language", "text",
             "placeholders", "tree"}
NODE_KEYS = {"path", "type", "kind", "required", "generated", "children",
             "closed", "from_offering"}
KINDS = ("meta", "runs", "read", "lives")
TYPES = ("file", "directory")
REQUIRED_RANK = {False: 0, "source-language": 1, True: 2}
LANGUAGE_ROOT = "{language}/"
PLACEHOLDER = re.compile(r"\{([a-z-]+)\}")
OFFERING_ID = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


@dataclass
class Node:
    name: str                       # this segment, such as "docs/"
    path: str                       # the full pattern, such as "{language}/docs/"
    type: str
    added_by: str                   # the layout that introduced the path
    required: object = False
    kind: Optional[str] = None
    generated: bool = False
    closed: bool = False
    from_offering: Optional[str] = None
    parent: Optional["Node"] = None
    children: List["Node"] = field(default_factory=list)

    @property
    def top(self) -> "Node":
        node = self
        while node.parent is not None:
            node = node.parent
        return node

    @property
    def effective_kind(self) -> Optional[str]:
        return self.top.kind

    @property
    def is_literal(self) -> bool:
        return "{" not in self.name


@dataclass
class Layout:
    id: str
    chain: List[str]                         # base first
    format: int
    source_language: str
    placeholders: Dict[str, str]
    tree: List[Node]
    own_paths: Dict[str, Set[str]]           # layout id -> paths it added
    own_placeholders: Dict[str, Set[str]]    # layout id -> placeholders

    def nodes(self) -> List[Node]:
        out: List[Node] = []

        def walk(nodes):
            for node in nodes:
                out.append(node)
                walk(node.children)
        walk(self.tree)
        return out


def read_structure(conf_dir: Path, layout_id: str) -> dict:
    path = conf_dir / "layouts" / f"{layout_id}.yaml"
    if not path.is_file():
        raise AutomaError(f"layout {layout_id!r} not found: {path}")
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise AutomaError(f"{path}: a layout is a mapping")
    extra = set(data) - FILE_KEYS
    if extra:
        raise AutomaError(f"{path}: unknown keys {sorted(extra)}")
    for key in ("format", "describes", "source_language", "tree"):
        if key not in data:
            raise AutomaError(f"{path}: missing {key!r}")
    if data["describes"] != layout_id:
        raise AutomaError(f"{path}: describes {data['describes']!r}, not "
                          f"{layout_id!r}")
    return data


def load_layout(conf_dir: Path, layout_id: str) -> Layout:
    return _load(conf_dir, layout_id, [])


def _load(conf_dir: Path, layout_id: str, seen: List[str]) -> Layout:
    if layout_id in seen:
        cycle = " -> ".join(seen + [layout_id])
        raise AutomaError(f"layout extends cycle: {cycle}")
    data = read_structure(conf_dir, layout_id)
    placeholders = dict(data.get("placeholders") or {})
    parent_id = data.get("extends")
    if parent_id is not None and not isinstance(parent_id, str):
        raise AutomaError(f"layout {layout_id!r}: extends names one parent")

    if parent_id is None:
        layout = Layout(layout_id, [layout_id], data["format"],
                        data["source_language"], placeholders, [],
                        {layout_id: set()}, {layout_id: set(placeholders)})
    else:
        layout = _load(conf_dir, parent_id, seen + [layout_id])
        if data["format"] != layout.format:
            raise AutomaError(f"layout {layout_id!r} has format "
                              f"{data['format']}, its parent "
                              f"{layout.format}")
        if data["source_language"] != layout.source_language:
            raise AutomaError(f"layout {layout_id!r} has source_language "
                              f"{data['source_language']!r}, its parent "
                              f"{layout.source_language!r}")
        redefined = set(placeholders) & set(layout.placeholders)
        if redefined:
            raise AutomaError(f"layout {layout_id!r} redefines inherited "
                              f"placeholder(s) {sorted(redefined)}")
        layout.id = layout_id
        layout.chain.append(layout_id)
        layout.placeholders.update(placeholders)
        layout.own_paths[layout_id] = set()
        layout.own_placeholders[layout_id] = set(placeholders)

    merge(layout, layout.tree, data["tree"] or [], "", None, layout_id)
    used = set(PLACEHOLDER.findall(" ".join(n.path for n in layout.nodes())))
    undefined = used - set(layout.placeholders)
    if undefined:
        raise AutomaError(f"layout {layout_id!r} uses undefined "
                          f"placeholder(s) {sorted(undefined)}")
    return layout


def _where(layout_id: str, path: str) -> str:
    return f"layout {layout_id!r}, {path}"


def merge(layout: Layout, nodes: List[Node], raws: list, prefix: str,
          parent: Optional[Node], layout_id: str) -> None:
    index = {node.name.rstrip("/"): node for node in nodes}
    for raw in raws:
        if not isinstance(raw, dict) or "path" not in raw:
            raise AutomaError(f"layout {layout_id!r}: every node needs a "
                              f"path")
        full = prefix + raw["path"]
        extra = set(raw) - NODE_KEYS
        if extra:
            raise AutomaError(f"{_where(layout_id, full)}: unknown keys "
                              f"{sorted(extra)}")
        if "kind" in raw and parent is not None:
            raise AutomaError(f"{_where(layout_id, full)}: kind is declared "
                              f"only on top-level paths; descendants "
                              f"inherit it")
        if raw.get("type") not in TYPES:
            raise AutomaError(f"{_where(layout_id, full)}: type must be "
                              f"file or directory")
        if "required" in raw and raw["required"] not in REQUIRED_RANK:
            raise AutomaError(f"{_where(layout_id, full)}: required must be "
                              f"true, false or source-language")
        if raw.get("required") == "source-language" \
                and not full.startswith(LANGUAGE_ROOT):
            raise AutomaError(f"{_where(layout_id, full)}: source-language "
                              f"is valid only on paths that begin with "
                              f"{LANGUAGE_ROOT}")
        if raw.get("kind") is not None and raw["kind"] not in KINDS:
            raise AutomaError(f"{_where(layout_id, full)}: kind must be one "
                              f"of {', '.join(KINDS)}")
        if raw.get("from_offering") is not None \
                and not OFFERING_ID.match(str(raw["from_offering"])):
            raise AutomaError(f"{_where(layout_id, full)}: from_offering "
                              f"must be an offering identifier")
        if raw["type"] == "file" and (raw.get("children") or raw.get("closed")):
            raise AutomaError(f"{_where(layout_id, full)}: a file has no "
                              f"children and cannot be closed")
        if raw["type"] == "directory" and not raw["path"].endswith("/"):
            raise AutomaError(f"{_where(layout_id, full)}: a directory path "
                              f"ends with /")

        existing = index.get(raw["path"].rstrip("/"))
        if existing is None:
            node = Node(raw["path"], full, raw["type"], layout_id,
                        raw.get("required", False), raw.get("kind"),
                        bool(raw.get("generated", False)),
                        bool(raw.get("closed", False)),
                        raw.get("from_offering"), parent)
            nodes.append(node)
            index[node.name.rstrip("/")] = node
            layout.own_paths[layout_id].add(full)
        else:
            node = existing
            overlay(node, raw, layout_id, full)
        merge(layout, node.children, raw.get("children") or [], full, node,
              layout_id)


def overlay(node: Node, raw: dict, layout_id: str, full: str) -> None:
    """Apply a child layout's node to an inherited one: add or tighten,
    never take away."""
    where = _where(layout_id, full)
    if raw["type"] != node.type:
        raise AutomaError(f"{where}: may not change the type of an "
                          f"inherited path from {node.type}")
    if "required" in raw:
        if REQUIRED_RANK[raw["required"]] < REQUIRED_RANK[node.required]:
            raise AutomaError(f"{where}: may tighten required but never "
                              f"loosen it ({node.required} to "
                              f"{raw['required']})")
        node.required = raw["required"]
    if raw.get("kind") is not None:
        if node.kind is not None and node.kind != raw["kind"]:
            raise AutomaError(f"{where}: may not change kind {node.kind!r} "
                              f"set by an ancestor layout")
        node.kind = raw["kind"]
    if raw.get("from_offering") is not None:
        if node.from_offering is not None \
                and node.from_offering != raw["from_offering"]:
            raise AutomaError(f"{where}: may not change from_offering "
                              f"{node.from_offering!r}")
        node.from_offering = raw["from_offering"]
    if "closed" in raw:
        if node.closed and not raw["closed"]:
            raise AutomaError(f"{where}: may close an open directory but "
                              f"never reopen a closed one")
        node.closed = node.closed or bool(raw["closed"])
    if "generated" in raw and bool(raw["generated"]) != node.generated:
        raise AutomaError(f"{where}: may not change generated")


def segment_regex(name: str, placeholders: Dict[str, str]) -> "re.Pattern":
    """A regex for one segment pattern, such as {number}--{slug}{version}.md,
    with a named group per placeholder."""
    out = []
    pos = 0
    for match in PLACEHOLDER.finditer(name):
        out.append(re.escape(name[pos:match.start()]))
        body = placeholders[match.group(1)]
        if body.startswith("^"):
            body = body[1:]
        if body.endswith("$"):
            body = body[:-1]
        group = match.group(1).replace("-", "_")
        out.append(f"(?P<{group}>{body})")
        pos = match.end()
    out.append(re.escape(name[pos:]))
    return re.compile("^" + "".join(out) + "$")
