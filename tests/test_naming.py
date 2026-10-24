"""Naming cases that cannot be committed as fixtures, because the names
themselves would break a checkout on some platform or break uc-automa's
own rule against hyphenated versions. They are built at test time."""

import tempfile
import unittest
from pathlib import Path

import support  # noqa: F401

from uc_automa.conformance import Repository
from uc_automa.conformance.layouts import load_layout
from uc_automa.conformance.naming import (lowercase_names, portable_names,
                                          spdx_slug, versions_in_filenames)


def repo(files, layout=None):
    loaded = load_layout(support.REPO / "conf", layout) if layout else None
    return Repository(Path(tempfile.gettempdir()), sorted(files),
                      layout=loaded)


class EleventyNames(unittest.TestCase):

    SITE = ["src/_data/site.json", "src/_includes/layouts/page.njk",
            "src/en/guides/guides.11tydata.json",
            "src/en/index.11tydata.js", "src/en/index.md"]

    def test_eleventy_names_pass_in_an_eleventy_site(self):
        self.assertEqual(lowercase_names(repo(self.SITE, "eleventy-site")), [])

    def test_eleventy_names_fail_elsewhere(self):
        self.assertTrue(lowercase_names(repo(self.SITE, "python-tool")))
        self.assertTrue(lowercase_names(repo(self.SITE)))

    def test_only_under_src(self):
        for name in ("_data/site.json", "docs/page.11tydata.json"):
            with self.subTest(name=name):
                self.assertTrue(lowercase_names(repo([name],
                                                     "eleventy-site")))

    def test_the_stem_still_follows_the_rule(self):
        for name in ("src/en/Guides.11tydata.json",
                     "src/en/a.b.11tydata.json", "src/_Data/site.json"):
            with self.subTest(name=name):
                self.assertTrue(lowercase_names(repo([name],
                                                     "eleventy-site")))


class Portable(unittest.TestCase):

    def test_windows_reserved_names(self):
        for name in ("aux.md", "docs/con", "lpt1.txt", "nul"):
            with self.subTest(name=name):
                self.assertTrue(portable_names(repo([name])))

    def test_forbidden_characters_and_trailing_dots(self):
        for name in ("a:b.md", "what?.md", "trailing.", "space name.md",
                     "café.md"):
            with self.subTest(name=name):
                self.assertTrue(portable_names(repo([name])))

    def test_names_differing_only_by_case(self):
        findings = portable_names(repo(["README.md", "readme.md"]))
        self.assertTrue(any("differs only by case" in f.message
                            for f in findings))


class HyphenatedVersions(unittest.TestCase):

    def test_hyphenated_version_in_any_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "using-the-tool-v0-1-0.md"
            path.write_text("x\n")
            findings = versions_in_filenames(
                Repository(Path(tmp), ["using-the-tool-v0-1-0.md"]))
        self.assertTrue(any("never -v0-1-0" in f.message for f in findings))


class Slugs(unittest.TestCase):

    def test_spdx_slug(self):
        self.assertEqual(spdx_slug("GPL-3.0-or-later"), "gpl-3-0-or-later")
        self.assertEqual(spdx_slug("CC-BY-SA-4.0"), "cc-by-sa-4-0")
        self.assertEqual(spdx_slug("LicenseRef-a..b"), "licenseref-a-b")


if __name__ == "__main__":
    unittest.main()
