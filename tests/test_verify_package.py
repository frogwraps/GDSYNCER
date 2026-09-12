"""Integration checks for the public-package release verifier."""

from __future__ import annotations

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
VERIFIER = REPO_ROOT / "scripts" / "verify_package.py"


class VerifyPackageTests(unittest.TestCase):
    def test_verifier_accepts_the_staged_package(self) -> None:
        result = subprocess.run(
            [sys.executable, str(VERIFIER), "--root", str(REPO_ROOT)],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PACKAGE_VALIDATION_PASS", result.stdout)

    def test_launch_material_does_not_call_the_validated_candidate_paused(self) -> None:
        stale_phrases = {
            "README.md": ("Unpublished beta staging package",),
            "BETA.md": ("Publication is paused",),
            "docs/QUICKSTART.md": ("publication is paused", "While this beta is unpublished"),
            "CHANGELOG.md": ("unpublished",),
            "workspace/PROTOCOL_VERSION.md": ("beta.3-unpublished",),
        }

        for relative_path, phrases in stale_phrases.items():
            content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for stale_phrase in phrases:
                self.assertNotIn(stale_phrase, content, f"{relative_path} still contains stale launch language")


    def test_verifier_rejects_a_copy_with_stale_launch_language(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package_copy = Path(temporary) / "package"
            shutil.copytree(
                REPO_ROOT,
                package_copy,
                ignore=shutil.ignore_patterns(".git", "_validation", "__pycache__"),
            )
            readme = package_copy / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8").replace(
                    "Validated beta release candidate", "Unpublished beta staging package"
                ),
                encoding="utf-8",
            )

            result = subprocess.run(
                [sys.executable, str(VERIFIER), "--root", str(package_copy)],
                cwd=package_copy,
                text=True,
                capture_output=True,
                check=False,
            )

        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("stale launch language", result.stdout)

    def test_quickstart_makes_python_optional_and_shows_the_release_check(self) -> None:
        quickstart = (REPO_ROOT / "docs" / "QUICKSTART.md").read_text(encoding="utf-8")
        self.assertIn("Normal use does not require Python", quickstart)
        self.assertIn("python scripts/verify_package.py --root .", quickstart)
    def test_validation_record_is_readable_and_matches_the_release_suite(self) -> None:
        validation = (REPO_ROOT / "docs" / "VALIDATION.md").read_text(encoding="utf-8")
        self.assertNotIn("`r`n", validation)
        self.assertIn("27 package checks and five regression tests", validation)
        self.assertIn("log/2026-09-12_validation-gds-shorts.md", validation)
        self.assertIn("gds-shorts-validation-2026-09-12-001", validation)
if __name__ == "__main__":
    unittest.main()
