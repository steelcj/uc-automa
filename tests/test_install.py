"""uc-automa installed from wheels into a fresh virtual environment.

Builds wheels of uc-portage and uc-automa, installs them, and runs init,
offerings apply and check in a scratch repository using only the
installed data, including dotfile payloads such as .gitattributes. An
editable install is checked too. These tests need network access for
PyYAML and take a minute, so they run when UC_AUTOMA_INSTALL_TESTS=1 is
set; uc-portage's checkout is found beside this one, or at
UC_PORTAGE_CHECKOUT.
"""

import os
import shutil
import subprocess
import tempfile
import unittest
import venv
from pathlib import Path

import support

IGNORE = shutil.ignore_patterns(".git", "__pycache__", "build", "dist",
                                "*.egg-info", ".venv*")


def python_in(env: Path) -> Path:
    scripts = env / ("Scripts" if os.name == "nt" else "bin")
    return scripts / ("python.exe" if os.name == "nt" else "python")


@unittest.skipUnless(os.environ.get("UC_AUTOMA_INSTALL_TESTS") == "1",
                     "set UC_AUTOMA_INSTALL_TESTS=1 to build and install "
                     "into fresh virtual environments (needs network)")
class Installs(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        portage = Path(os.environ.get("UC_PORTAGE_CHECKOUT",
                                      support.REPO.parent / "uc-portage"))
        self.portage = self.tmp / "uc-portage"
        self.automa = self.tmp / "uc-automa"
        shutil.copytree(portage, self.portage, ignore=IGNORE)
        shutil.copytree(support.REPO, self.automa, ignore=IGNORE)

    def tearDown(self):
        self._tmp.cleanup()

    def env(self, name):
        env = self.tmp / name
        venv.EnvBuilder(with_pip=True).create(env)
        self.run_in(env, "-m", "pip", "install", "-q", "--upgrade", "pip")
        return env

    def run_in(self, env, *args, cwd=None):
        r = subprocess.run([str(python_in(env)), *args], cwd=cwd or self.tmp,
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return r.stdout

    def cli(self, env, *args, cwd):
        return self.run_in(env, "-m", "uc_automa.cli", *args, cwd=cwd)

    def test_wheels_in_a_fresh_environment(self):
        builder = self.env("builder")
        wheels = self.tmp / "wheels"
        for src in (self.portage, self.automa):
            self.run_in(builder, "-m", "pip", "wheel", "--no-deps", "-q",
                        "-w", str(wheels), str(src))
        env = self.env("wheel")
        self.run_in(env, "-m", "pip", "install", "-q",
                    *[str(w) for w in sorted(wheels.glob("*.whl"))])
        payload = self.run_in(env, "-c", (
            "from uc_automa.paths import offerings_dir; "
            "print(offerings_dir() / 'line-endings' / 'files' / "
            "'.gitattributes')")).strip()
        self.assertTrue(Path(payload).is_file(), payload)
        self.assertTrue(str(Path(payload).resolve()).startswith(
            str(env.resolve())))

        repo = self.tmp / "sample-tool"
        repo.mkdir()
        self.cli(env, "init", "--repository", "sample-tool",
                 "--layout", "python-tool", cwd=repo)
        self.cli(env, "offerings", "apply", "--yes", cwd=repo)
        self.assertEqual((repo / ".gitattributes").read_text(),
                         "* text=auto eol=lf\n")
        out = self.cli(env, "offerings", "plan", cwd=repo)
        self.assertIn("0 item(s) would be synced", out)

    def test_editable_install(self):
        env = self.env("editable")
        self.run_in(env, "-m", "pip", "install", "-q", "-e",
                    str(self.portage), "-e", str(self.automa))
        found = self.run_in(env, "-c", (
            "from uc_automa.paths import conf_dir; print(conf_dir())")).strip()
        self.assertEqual(Path(found).resolve(),
                         (self.automa / "conf").resolve())


if __name__ == "__main__":
    unittest.main()
