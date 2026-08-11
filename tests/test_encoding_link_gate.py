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


if __name__ == "__main__":
    unittest.main()
