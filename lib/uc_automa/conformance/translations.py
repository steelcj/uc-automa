"""layout/layout-translations: each layout's words match its structure.

Structure lives once under conf/layouts/; words live at the same
relative path under each language root (uc-automa 0012). The check runs
per layout file:

- a words file describes only the paths and placeholders its own layout
  adds; inherited paths keep their parent's words;
- the source language describes all of them;
- another language may leave some untranslated, which is reported but
  is not an error;
- each translated entry records the source_hash of the source text, and
  a hash that no longer matches marks the translation stale.

The check applies to the repository that holds the layouts, uc-automa
itself, so it runs only when automa_version is self.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Dict, List, Tuple

import yaml

from . import Repository, check
from .layouts import Layout, load_layout

TEXT_KEYS = {"language", "translates", "title", "purpose", "values",
             "placeholders", "paths"}
VALUE_KEYS = {"kind", "required", "generated", "closed", "from_offering"}


def source_hash(text: str) -> str:
    """The first twelve hex digits of the SHA-256 of the source text."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def holds(entry) -> str:
    return entry.get("holds", "") if isinstance(entry, dict) else ""


def placeholder_text(entry) -> str:
    return entry.get("text", "") if isinstance(entry, dict) else str(entry)


def read_words(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ValueError("a words file is a mapping")
    return data


def check_layout_words(layout: Layout, layout_id: str,
                       text_dirs: Dict[str, Path]) -> Tuple[list, dict]:
    """Return (errors, report) for one layout file across all languages.
    errors are (path, message) pairs; report maps a language to its
    untranslated and stale paths."""
    errors: List[tuple] = []
    report: Dict[str, dict] = {}
    own_paths = layout.own_paths[layout_id]
    own_placeholders = layout.own_placeholders[layout_id]
    inherited = {n.path for n in layout.nodes()} - own_paths
    source = layout.source_language
    rel = f"conf/layouts/{layout_id}.yaml"

    if source not in text_dirs:
        return [(f"{source}/{rel}", "the source language has no words for "
                                    "this layout")], report
    words: Dict[str, dict] = {}
    for language, conf in sorted(text_dirs.items()):
        path = conf / "layouts" / f"{layout_id}.yaml"
        shown = f"{language}/{rel}"
        if not path.is_file():
            if language == source:
                errors.append((shown, "missing; the source language "
                                      "describes every layout"))
            else:
                report[language] = {"untranslated": sorted(own_paths),
                                    "stale": []}
            continue
        try:
            words[language] = read_words(path)
        except (ValueError, yaml.YAMLError) as exc:
            errors.append((shown, f"not readable: {exc}"))
            continue
        data = words[language]
        extra = set(data) - TEXT_KEYS
        if extra:
            errors.append((shown, f"unknown keys {sorted(extra)}"))
        if data.get("language") != language:
            errors.append((shown, f"language is {data.get('language')!r}, "
                                  f"expected {language!r}"))
        if data.get("translates") != rel:
            errors.append((shown, f"translates {data.get('translates')!r}, "
                                  f"expected {rel!r}"))
        extra_values = set(data.get("values") or {}) - VALUE_KEYS
        if extra_values:
            errors.append((shown, f"describes unknown value(s) "
                                  f"{sorted(extra_values)}"))
        described = set(data.get("paths") or {})
        for p in sorted(described & inherited):
            errors.append((shown, f"describes inherited path {p!r}; "
                                  f"inherited paths keep the words of the "
                                  f"layout that adds them"))
        for p in sorted(described - own_paths - inherited):
            errors.append((shown, f"describes a path the structure lacks: "
                                  f"{p!r}"))
        described_ph = set(data.get("placeholders") or {})
        for p in sorted(described_ph - own_placeholders):
            errors.append((shown, f"describes placeholder {p!r}, which "
                                  f"this layout does not define"))
        if language == source:
            for p in sorted(own_paths - described):
                errors.append((shown, f"the source language misses words "
                                      f"for {p!r}"))
            for p in sorted(own_placeholders - described_ph):
                errors.append((shown, f"the source language misses words "
                                      f"for placeholder {p!r}"))

    src = words.get(source)
    for language, data in sorted(words.items()):
        if language == source or src is None:
            continue
        paths = data.get("paths") or {}
        phs = data.get("placeholders") or {}
        stale = []
        for p, entry in paths.items():
            want = source_hash(holds((src.get("paths") or {}).get(p, {})))
            if not isinstance(entry, dict) or entry.get("source_hash") != want:
                stale.append(p)
        for p, entry in phs.items():
            want = source_hash(placeholder_text(
                (src.get("placeholders") or {}).get(p, "")))
            if not isinstance(entry, dict) or entry.get("source_hash") != want:
                stale.append(f"{{{p}}}")
        report[language] = {
            "untranslated": sorted(own_paths - set(paths)),
            "stale": sorted(stale),
        }
    return errors, report


def layouts_in(conf_dir: Path) -> List[str]:
    return sorted(p.stem for p in (conf_dir / "layouts").glob("*.yaml"))


def translation_report(conf_dir: Path, text_dirs: Dict[str, Path]):
    """Errors and per-language report for every layout under conf_dir."""
    errors: List[tuple] = []
    reports: Dict[str, Dict[str, dict]] = {}
    for layout_id in layouts_in(conf_dir):
        layout = load_layout(conf_dir, layout_id)
        errs, report = check_layout_words(layout, layout_id, text_dirs)
        errors.extend(errs)
        reports[layout_id] = report
    return errors, reports


@check("conformance.layout.translations", "layout/layout-translations")
def layout_translations(repo: Repository):
    if repo.config is None or not repo.config.is_self \
            or repo.conf_dir is None:
        return []
    errors, reports = translation_report(repo.conf_dir, repo.text_dirs)
    findings = list(errors)
    for layout_id, report in reports.items():
        for language, entry in report.items():
            for p in entry["stale"]:
                findings.append((f"{language}/conf/layouts/{layout_id}.yaml",
                                 f"stale translation of {p!r}: the source "
                                 f"text changed"))
    return findings
