"""The extends rules (uc-automa 0013), one test per rule."""

import tempfile
import unittest
from pathlib import Path

import support  # noqa: F401

from uc_automa.conformance.layouts import load_layout
from uc_automa.errors import AutomaError

BASE = """format: 1
describes: "base"
source_language: "en-ca"
placeholders:
  language: '^[a-z]{2}(-[a-z]{2})?$'
tree:
  - path: "README.md"
    type: file
    required: false
  - path: "docs/"
    type: directory
    closed: true
    children:
      - path: "index.md"
        type: file
"""


class Extends(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.conf = Path(self._tmp.name)
        (self.conf / "layouts").mkdir()
        self.write("base", BASE)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, name, text):
        (self.conf / "layouts" / f"{name}.yaml").write_text(text)

    def child(self, tree, extra=""):
        self.write("child", 'format: 1\ndescribes: "child"\nextends: "base"\n'
                   'source_language: "en-ca"\n' + extra + "tree:\n" + tree)
        return load_layout(self.conf, "child")

    def refused(self, tree, extra="", says=""):
        with self.assertRaises(AutomaError) as caught:
            self.child(tree, extra)
        self.assertIn(says, str(caught.exception))

    def test_a_chain_resolves_parent_first(self):
        layout = self.child('  - path: "notes/"\n    type: directory\n')
        self.assertEqual(layout.chain, ["base", "child"])
        self.assertEqual(layout.own_paths["child"], {"notes/"})

    def test_a_cycle_is_an_error(self):
        self.write("base", BASE.replace('describes: "base"',
                                        'describes: "base"\nextends: "child"'))
        self.refused('  - path: "x"\n    type: file\n', says="cycle")

    def test_required_may_tighten(self):
        layout = self.child('  - path: "README.md"\n    type: file\n'
                            '    required: true\n')
        self.assertIs(layout.tree[0].required, True)

    def test_required_may_never_loosen(self):
        self.write("base", BASE.replace("required: false", "required: true"))
        self.refused('  - path: "README.md"\n    type: file\n'
                     '    required: false\n', says="never loosen")

    def test_type_may_not_change(self):
        self.refused('  - path: "docs"\n    type: file\n', says="type")

    def test_kind_may_be_set_where_none_is(self):
        layout = self.child('  - path: "README.md"\n    type: file\n'
                            '    kind: meta\n')
        self.assertEqual(layout.tree[0].kind, "meta")

    def test_kind_may_not_change(self):
        self.write("base", BASE.replace('    required: false\n',
                                        '    required: false\n    kind: read\n', 1))
        self.refused('  - path: "README.md"\n    type: file\n    kind: meta\n',
                     says="may not change kind")

    def test_kind_only_on_top_level_nodes(self):
        self.refused('  - path: "docs/"\n    type: directory\n    children:\n'
                     '      - path: "extra.md"\n        type: file\n'
                     '        kind: read\n', says="top-level")

    def test_descendants_inherit_kind(self):
        layout = self.child('  - path: "docs/"\n    type: directory\n'
                            '    kind: read\n    children:\n'
                            '      - path: "extra.md"\n        type: file\n')
        extra = [n for n in layout.nodes() if n.path == "docs/extra.md"][0]
        self.assertEqual(extra.effective_kind, "read")

    def test_from_offering_may_be_set_but_not_changed(self):
        layout = self.child('  - path: "README.md"\n    type: file\n'
                            '    from_offering: "readme"\n')
        self.assertEqual(layout.tree[0].from_offering, "readme")
        self.write("base", BASE.replace('    required: false\n',
                                        '    required: false\n'
                                        '    from_offering: "one"\n', 1))
        self.refused('  - path: "README.md"\n    type: file\n'
                     '    from_offering: "two"\n', says="from_offering")

    def test_closed_may_close_but_never_reopen(self):
        layout = self.child('  - path: "notes/"\n    type: directory\n')
        self.assertFalse(layout.tree[-1].closed)
        self.refused('  - path: "docs/"\n    type: directory\n'
                     '    closed: false\n', says="reopen")

    def test_paths_added_inside_a_closed_directory_count_as_declared(self):
        layout = self.child('  - path: "docs/"\n    type: directory\n'
                            '    children:\n      - path: "extra.md"\n'
                            '        type: file\n')
        self.assertIn("docs/extra.md", layout.own_paths["child"])

    def test_inherited_placeholders_may_not_be_redefined(self):
        self.refused('  - path: "x"\n    type: file\n',
                     extra="placeholders:\n  language: '^x$'\n",
                     says="redefines")

    def test_source_language_only_under_the_language_placeholder(self):
        self.refused('  - path: "x"\n    type: file\n'
                     '    required: source-language\n', says="source-language")

    def test_format_and_source_language_match_the_chain(self):
        self.write("child", 'format: 1\ndescribes: "child"\nextends: "base"\n'
                   'source_language: "fr-ca"\ntree: []\n')
        with self.assertRaises(AutomaError):
            load_layout(self.conf, "child")

    def test_undefined_placeholders_are_refused(self):
        self.refused('  - path: "{nothing}.md"\n    type: file\n',
                     says="undefined")


class RealLayouts(unittest.TestCase):

    def test_every_layout_resolves(self):
        for name in ("base", "python-tool", "uc-automa", "osat-manager"):
            with self.subTest(layout=name):
                load_layout(support.REPO / "conf", name)

    def test_the_chain_is_base_python_tool_then_the_type(self):
        for name in ("uc-automa", "osat-manager"):
            layout = load_layout(support.REPO / "conf", name)
            self.assertEqual(layout.chain, ["base", "python-tool", name])


if __name__ == "__main__":
    unittest.main()
