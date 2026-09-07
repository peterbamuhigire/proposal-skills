import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
DOC = ROOT / "docs/operations/runtime-agnostic-orchestration-2026-09-07.md"


class RuntimeOrchestrationGuidanceTests(unittest.TestCase):
    def test_contract_and_readme_link(self):
        doc = DOC.read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(DOC.name, readme)
        for marker in ("## Phase outputs", "deliverable-to-effort-price", "NOT_ASSESSED", "untrusted", "Rollback", "Claude", "Codex"):
            self.assertIn(marker, doc)
        for name in ("the-shortform-guide.md", "the-longform-guide.md", "the-security-guide.md"):
            self.assertIn("https://raw.githubusercontent.com/affaan-m/ECC/main/" + name, doc)


if __name__ == "__main__":
    unittest.main()
