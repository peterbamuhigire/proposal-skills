"""Tests for the source-ingestion guardrail's book-extraction rule."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("guardrail", ROOT / "scripts" / "source_ingestion_guardrail.py")
guardrail = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules["guardrail"] = guardrail
SPEC.loader.exec_module(guardrail)


class BookExtractionRuleTest(unittest.TestCase):
    def test_small_file_under_book_extractions_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "book-extractions" / "note.md"
            target.parent.mkdir()
            target.write_text("# short synthesis\n", encoding="utf-8")
            codes = [finding.code for finding in guardrail.scan(Path(tmp))]
            self.assertIn("book-extraction-stored", codes)

    def test_task_reference_outside_book_paths_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "skills" / "demo" / "references" / "phrase-bank.md"
            target.parent.mkdir(parents=True)
            target.write_text("# Phrase bank\n", encoding="utf-8")
            self.assertEqual(guardrail.scan(Path(tmp)), [])

    def test_repository_has_no_book_extractions_folder(self) -> None:
        self.assertFalse((ROOT / "book-extractions").exists())


if __name__ == "__main__":
    unittest.main()
