"""uc-automa: the station.

Holds Vishpala's rules and offerings, and the tool that checks
repositories against them.
"""

from pathlib import Path


def _version() -> str:
    try:
        from importlib.metadata import PackageNotFoundError, version
    except ImportError:  # pragma: no cover, Python 3.8 has importlib.metadata
        return "unknown"
    try:
        return version("uc-automa")
    except PackageNotFoundError:
        # A checkout that is not installed: VERSION is the single source.
        version_file = Path(__file__).resolve().parents[2] / "VERSION"
        if version_file.is_file():
            return version_file.read_text(encoding="utf-8").strip()
        return "unknown"


__version__ = _version()
