"""The uc-automa command.

    uc-automa init --repository NAME --layout ID
    uc-automa check [--only CHECK-OR-DIRECTIVE ...] [--list]
    uc-automa translations
    uc-automa offerings {plan,status,apply,harvest} [--yes] [--force]
    uc-automa docs index

Every command works on the repository at --target, the current
directory by default.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List, Optional

from uc_portage.errors import PortageError

from . import __version__
from . import offerings as offerings_cmd
from .config import load_config
from .conformance import Repository, all_checks, list_files, run_checks
from .conformance.layouts import load_layout
from .conformance.translations import translation_report
from .paths import conf_dir, text_dirs, text_dirs_in
from .docs import IndexError_, write_index
from .errors import AutomaError
from .init import init


def log(message: str) -> None:
    print(f"[uc-automa] {message}")


def load_repository(root: Path) -> Repository:
    config = load_config(root)
    if config.is_self:
        conf, texts = root / "conf", text_dirs_in(root)
    else:
        conf, texts = conf_dir(), text_dirs()
    layout = load_layout(conf, config.layout)
    return Repository(root, list_files(root), config, layout, conf, texts)


def cmd_init(args) -> int:
    path = init(Path(args.target), args.repository, args.layout)
    log(f"wrote {path}; next, uc-automa offerings apply")
    return 0


def cmd_check(args) -> int:
    if args.list:
        for registered in all_checks():
            print(f"{registered.directive}  ({registered.id})")
        return 0
    repo = load_repository(Path(args.target))
    findings = run_checks(repo, args.only)
    for finding in findings:
        print(finding)
    names = {r.directive for r in all_checks()}
    if args.only:
        names = {n for n in names if n in args.only} | \
                {r.directive for r in all_checks() if r.id in args.only}
    if findings:
        log(f"{len(findings)} finding(s) against {len(names)} directive(s)")
        return 1
    log(f"conforms: {len(names)} directive(s) checked, layout "
        f"{repo.config.layout!r}")
    return 0


def cmd_translations(args) -> int:
    repo = load_repository(Path(args.target))
    errors, reports = translation_report(repo.conf_dir, repo.text_dirs)
    for path, message in errors:
        print(f"  error: {path}: {message}")
    for layout_id, report in sorted(reports.items()):
        for language, entry in sorted(report.items()):
            print(f"{language}/conf/layouts/{layout_id}.yaml: "
                  f"{len(entry['untranslated'])} untranslated, "
                  f"{len(entry['stale'])} stale")
        if repo.layout and repo.layout.source_language not in report:
            print(f"{repo.layout.source_language}/conf/layouts/"
                  f"{layout_id}.yaml: source language, 0 untranslated, "
                  f"0 stale")
    log(f"{len(errors)} error(s)")
    return 1 if errors else 0


def cmd_offerings(args) -> int:
    config = load_config(Path(args.target))
    extra: List[str] = []
    if args.action == "apply":
        extra += ["--yes"] if args.yes else []
        extra += ["--force"] if args.force else []
    return offerings_cmd.run(args.action, config, extra)


def cmd_docs(args) -> int:
    config = load_config(Path(args.target))
    path = write_index(config.root, config.language)
    log(f"wrote {path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="uc-automa",
        description="The station: Vishpala's rules and offerings, and the "
                    "tool that checks repositories against them.")
    parser.add_argument("--version", action="version",
                        version=f"uc-automa {__version__}")
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--target", default=".", metavar="DIR",
                        help="The repository (default: the current "
                             "directory).")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("init", parents=[common],
                       help="Write .uc-automa.yaml, once.")
    p.add_argument("--repository", required=True, metavar="NAME")
    p.add_argument("--layout", required=True, metavar="ID")
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("check", parents=[common],
                       help="Check the repository against the directives.")
    p.add_argument("--only", action="append", metavar="ID",
                   help="Run only this check or directive; repeatable.")
    p.add_argument("--list", action="store_true",
                   help="List each directive and the check enforcing it.")
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("translations", parents=[common],
                       help="Report untranslated and stale layout words.")
    p.set_defaults(func=cmd_translations)

    p = sub.add_parser("offerings", parents=[common],
                       help="Carry subscribed offerings with uc-portage.")
    p.add_argument("action", choices=["plan", "status", "apply", "harvest"])
    p.add_argument("--yes", action="store_true",
                   help="apply: skip the confirmation prompt.")
    p.add_argument("--force", action="store_true",
                   help="apply: overwrite mirror conflicts this once.")
    p.set_defaults(func=cmd_offerings)

    p = sub.add_parser("docs", parents=[common],
                       help="Documentation tools.")
    p.add_argument("action", choices=["index"])
    p.set_defaults(func=cmd_docs)
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except (AutomaError, PortageError, IndexError_) as exc:
        print(f"[uc-automa ERROR] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
