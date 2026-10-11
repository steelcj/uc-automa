"""The commands end to end, on scratch repositories and on uc-automa
itself."""

import contextlib
import io
import shutil
import tempfile
import unittest
from pathlib import Path

import yaml

import support

from uc_automa import __version__, cli


def run(*argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = cli.main(list(argv))
    return code, out.getvalue(), err.getvalue()


class Scratch(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "repo"
        self.root.mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def config(self):
        return yaml.safe_load((self.root / ".uc-automa.yaml").read_text())


class Init(Scratch):

    def test_init_writes_the_configuration_once(self):
        code, out, err = run("init", "--target", str(self.root),
                             "--repository", "sample-tool",
                             "--layout", "python-tool")
        self.assertEqual(code, 0, err)
        config = self.config()
        self.assertEqual(config["automa_version"], __version__)
        self.assertEqual(config["language"], "en-ca")
        self.assertIn("license-mit", config["subscribe"])
        self.assertIn("license-cc-by-4-0", config["subscribe"])
        code, out, err = run("init", "--target", str(self.root),
                             "--repository", "sample-tool",
                             "--layout", "python-tool")
        self.assertEqual(code, 1)
        self.assertIn("already exists", err)

    def test_an_unknown_layout_is_refused(self):
        code, out, err = run("init", "--target", str(self.root),
                             "--repository", "x", "--layout", "nothing")
        self.assertEqual(code, 1)
        self.assertIn("not found", err)


class Pinning(Scratch):

    def write_config(self, version):
        (self.root / ".uc-automa.yaml").write_text(
            f"format: 1\nrepository: sample-tool\nlayout: python-tool\n"
            f"automa_version: '{version}'\nlanguage: en-ca\nsubscribe: []\n")

    def test_a_different_pin_names_both_versions_and_both_fixes(self):
        self.write_config("9.9.9")
        code, out, err = run("offerings", "plan", "--target", str(self.root))
        self.assertEqual(code, 1)
        self.assertIn("9.9.9", err)
        self.assertIn(__version__, err)
        self.assertIn("install uc-automa 9.9.9", err)
        self.assertIn("update automa_version", err)

    def test_self_is_valid_only_in_uc_automa(self):
        self.write_config("self")
        code, out, err = run("check", "--target", str(self.root))
        self.assertEqual(code, 1)
        self.assertIn("valid only in uc-automa itself", err)


class Offerings(Scratch):

    def test_apply_then_plan_has_nothing_to_do(self):
        run("init", "--target", str(self.root), "--repository",
            "sample-tool", "--layout", "python-tool")
        code, out, err = run("offerings", "apply", "--yes",
                             "--target", str(self.root))
        self.assertEqual(code, 0, err)
        self.assertTrue((self.root / "LICENSE").is_file())
        self.assertEqual((self.root / "LICENSE").read_bytes(),
                         (self.root / "LICENSES" /
                          "MIT.txt").read_bytes())
        self.assertIn("uc-portage:begin uc-automa-signpost",
                      (self.root / "CLAUDE.md").read_text())
        code, out, err = run("offerings", "plan", "--target", str(self.root))
        self.assertEqual(code, 0, err)
        self.assertIn("0 item(s) would be synced", out)


class UcAutoma(unittest.TestCase):
    """The acceptance checks on uc-automa itself."""

    def test_check_passes_on_uc_automa(self):
        code, out, err = run("check", "--target", str(support.REPO))
        self.assertEqual(code, 0, out + err)

    def test_offerings_plan_has_nothing_to_do(self):
        code, out, err = run("offerings", "plan", "--target",
                             str(support.REPO))
        self.assertEqual(code, 0, err)
        self.assertIn("0 item(s) would be synced", out)
        self.assertIn("0 conflict(s)", out)

    def test_translations_report_nothing_for_en_ca(self):
        code, out, err = run("translations", "--target", str(support.REPO))
        self.assertEqual(code, 0, out + err)
        self.assertIn("0 error(s)", out)
        self.assertNotIn("stale:", out)


class DocsIndex(Scratch):

    def test_index_is_generated_from_front_matter(self):
        shutil.copytree(support.FIXTURES / "docs" / "generated-index" /
                        "fail" / "index-missing", self.root,
                        dirs_exist_ok=True)
        code, out, err = run("docs", "index", "--target", str(self.root))
        # The fixture pins 0.1.0; on another version the pin check refuses.
        if code == 0:
            text = (self.root / "en-ca/docs/README.md").read_text()
            self.assertTrue(text.startswith("<!-- Generated by uc-automa"))
            self.assertIn("[Using](guides/usage/using-v0.1.0.md)", text)
        else:
            self.assertIn("pins uc-automa", err)


if __name__ == "__main__":
    unittest.main()
