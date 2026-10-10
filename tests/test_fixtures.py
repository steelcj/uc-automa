"""Every directive with a check has pass and fail fixtures, every pass
case passes, and every fail case fails that directive's check."""

import unittest

from support import FIXTURES, fixture_repository

from uc_automa.conformance import all_checks


class Fixtures(unittest.TestCase):

    def test_every_check_has_pass_and_fail_cases(self):
        for registered in all_checks():
            domain, slug = registered.directive.split("/")
            with self.subTest(directive=registered.directive):
                for verdict in ("pass", "fail"):
                    cases = FIXTURES / domain / slug / verdict
                    self.assertTrue(cases.is_dir() and any(cases.iterdir()),
                                    f"no {verdict} fixtures in {cases}")

    def test_cases(self):
        for registered in all_checks():
            domain, slug = registered.directive.split("/")
            for verdict in ("pass", "fail"):
                cases = FIXTURES / domain / slug / verdict
                for case in sorted(p for p in cases.iterdir() if p.is_dir()):
                    with self.subTest(directive=registered.directive,
                                      case=f"{verdict}/{case.name}"):
                        findings = registered.run(fixture_repository(case))
                        if verdict == "pass":
                            self.assertEqual(findings, [])
                        else:
                            self.assertNotEqual(findings, [])
                            self.assertTrue(all(
                                f.directive == registered.directive
                                for f in findings))


if __name__ == "__main__":
    unittest.main()
