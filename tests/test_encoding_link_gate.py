"""Regression checks for the repository encoding and route gate."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.encoding_link_gate import check


class EncodingLinkGateTests(unittest.TestCase):
    def test_gate_rejects_invalid_encoding_stale_route_and_broken_link(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text(
                "[missing](missing.md)\n"
                "C:\\Users\\Peter\\source\\repos\\social-media-skills\n",
                encoding="utf-8",
            )
            (root / "broken.md").write_bytes(b"invalid utf-8: \xff")
            findings = check(root)

        self.assertTrue(any("broken local Markdown link" in item for item in findings))
        self.assertTrue(any("stale device-specific sibling route" in item for item in findings))
        self.assertTrue(any("invalid UTF-8" in item for item in findings))

    def test_stale_route_is_the_only_reported_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text(
                "https://github.com/peterbamuhigire/social-media-skills\n"
                "https://github.com/peterbamuhigire/business-plan-skills\n"
                "C:\\Users\\Peter\\source\\repos\\social-media-skills\n",
                encoding="utf-8",
            )

            self.assertEqual(check(root), ["stale device-specific sibling route: README.md"])

    def test_bad_encoding_is_the_only_reported_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text(
                "https://github.com/peterbamuhigire/social-media-skills\n"
                "https://github.com/peterbamuhigire/business-plan-skills\n",
                encoding="utf-8",
            )
            (root / "bad.md").write_bytes(b"invalid utf-8: \xff")

            findings = check(root)

        self.assertEqual(len(findings), 1)
        self.assertTrue(findings[0].startswith("invalid UTF-8: bad.md:"))


ROUTES = (
    "https://github.com/peterbamuhigire/social-media-skills\n"
    "https://github.com/peterbamuhigire/business-plan-skills\n"
)


class MachinePathTests(unittest.TestCase):
    def findings_for(self, relative: str, text: str) -> list[str]:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text(ROUTES, encoding="utf-8")
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
            return check(root)

    def test_drive_and_home_paths_in_a_skill_are_refused(self) -> None:
        for text in (
            "Local copy at C:\\Users\\Someone\\skills\\x\n",
            "Local copy at C:/projects/engine/x\n",
            "Local copy at /home/someone/engines/x/\n",
            "Local copy at /Users/someone/engines/x/\n",
        ):
            self.assertEqual(
                self.findings_for("skills/demo/SKILL.md", text),
                ["machine-specific path: skills/demo/SKILL.md:1"],
                text,
            )

    def test_urls_and_generic_install_paths_are_not_machine_paths(self) -> None:
        text = (
            "https://developers.example.org/guides/image\n"
            "Install into ~/.claude or .claude under the project.\n"
            "Resolve <chwezi-dev-engine>/skills/x through the routing table.\n"
        )
        self.assertEqual(self.findings_for("skills/demo/SKILL.md", text), [])

    def test_dated_records_scripts_and_tests_are_exempt(self) -> None:
        text = "Run at C:\\Users\\Someone\\work\n"
        for relative in ("docs/audits/old.md", "docs/kaizen/run/00.md", "scripts/probe.py", "tests/probe.py"):
            self.assertEqual(self.findings_for(relative, text), [], relative)

    def test_active_docs_outside_the_record_folders_are_checked(self) -> None:
        text = "Standard held at C:\\wamp64\\www\\engine\n"
        self.assertEqual(
            self.findings_for("docs/skill-authoring-standard.md", text),
            ["machine-specific path: docs/skill-authoring-standard.md:1"],
        )


if __name__ == "__main__":
    unittest.main()
