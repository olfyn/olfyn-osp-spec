"""Regression tests for the profile validator (run with unittest discover)."""

import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("validate", ROOT / "tools/validate.py")
validate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate)

DIMENSIONS = (
    "floral", "frutal", "herbal", "leñoso", "ahumado",
    "especiado", "animal", "químico", "marino", "dulce",
)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.profile = {
            "osp_version": "1.1",
            "scent_id": "test-profile",
            "name": "Synthetic profile",
            "profile": dict.fromkeys(DIMENSIONS, 0.5),
            "intensity": 0.5,
            "duration_ms": 1000,
            "created_at": "2026-01-01T00:00:00Z",
        }
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)

    def run_file(self, content, name="profile.json"):
        path = self.directory / name
        path.write_text(content, encoding="utf-8")
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = validate.main([str(path)])
        return result, output.getvalue(), path

    def check_invalid(self, profile, *messages):
        result, output, path = self.run_file(json.dumps(profile))
        self.assertEqual(result, 1)
        self.assertIn(f"INVALID {path}", output)
        self.assertIn("1 profile(s) checked, 1 invalid", output)
        for message in messages:
            self.assertIn(message, output)

    def test_valid_profile(self):
        result, output, path = self.run_file(json.dumps(self.profile))
        self.assertEqual(result, 0)
        self.assertIn(f"ok      {path}", output)
        self.assertIn("1 profile(s) checked, 0 invalid", output)

    def test_dimension_bounds(self):
        for dimension in DIMENSIONS:
            for value, message in ((-0.1, "minimum"), (1.1, "maximum")):
                with self.subTest(dimension=dimension, value=value):
                    profile = copy.deepcopy(self.profile)
                    profile["profile"][dimension] = value
                    self.check_invalid(profile, f"profile/{dimension}:", message)

    def test_dimension_endpoints_are_valid(self):
        for value in (0.0, 1.0):
            with self.subTest(value=value):
                profile = copy.deepcopy(self.profile)
                profile["profile"] = dict.fromkeys(DIMENSIONS, value)
                result, output, _ = self.run_file(json.dumps(profile))
                self.assertEqual(result, 0, output)

    def test_missing_required_fields(self):
        for field in self.profile:
            with self.subTest(field=field):
                profile = copy.deepcopy(self.profile)
                del profile[field]
                self.check_invalid(profile, "(root):", f"'{field}'", "required")

    def test_missing_dimension(self):
        for dimension in DIMENSIONS:
            with self.subTest(dimension=dimension):
                profile = copy.deepcopy(self.profile)
                del profile["profile"][dimension]
                self.check_invalid(profile, "profile:", f"'{dimension}'", "required")

    def test_unknown_version(self):
        self.profile["osp_version"] = "99.0"
        self.check_invalid(self.profile, "osp_version:", "99.0")

    def test_invalid_date_time(self):
        self.profile["created_at"] = "not-a-date"
        self.check_invalid(self.profile, "created_at:", "date-time")

    def test_markdown_skips_non_profiles(self):
        snippets = [
            {"session_id": "test-session", "sequence": []},
            {"scent_id": "not-a-profile"},
            {"profile": {}},
            [],
            None,
        ]
        content = "\n".join("```json\n" + json.dumps(item) + "\n```" for item in snippets)
        result, output, _ = self.run_file(content, "session.md")
        self.assertEqual(result, 0)
        self.assertNotIn("INVALID", output)
        self.assertIn("0 profile(s) checked, 0 invalid", output)

    def test_markdown_validates_profiles_among_other_blocks(self):
        self.profile["created_at"] = "not-a-date"
        content = "# Profiles\n```json\n" + json.dumps(self.profile) + "\n```\n"
        content += '```json\n{"session_id": "test-session"}\n```\n'
        result, output, path = self.run_file(content, "mixed.md")
        self.assertEqual(result, 1)
        self.assertIn(f"INVALID {path}:2", output)
        self.assertIn("created_at:", output)
        self.assertIn("1 profile(s) checked, 1 invalid", output)

    def test_documented_examples_via_cli(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools/validate.py"),
             str(ROOT / "examples/EXAMPLES.md"), str(ROOT / "README.md")],
            cwd=self.directory, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertRegex(result.stdout, r"[1-9]\d* profile\(s\) checked, 0 invalid")


if __name__ == "__main__":
    unittest.main()
