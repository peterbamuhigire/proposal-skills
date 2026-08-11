"""Behavioural checks for the fictional proposal evidence fixture."""

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from scripts.proposal_fixture_check import validate_bid_package


FIXTURE = Path(__file__).parent / "fixtures" / "fictional-bid-package.json"


class ProposalFixtureBehaviourTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.package = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_complete_fixture_is_traceable_and_separated(self) -> None:
        self.assertEqual(validate_bid_package(self.package), [])
        response_by_requirement = {
            item["requirement_id"]: item for item in self.package["responses"]
        }
        evidence_by_id = {item["id"]: item for item in self.package["evidence"]}
        for requirement in self.package["requirements"]:
            response = response_by_requirement[requirement["id"]]
            self.assertEqual(response["envelope"], requirement["envelope"])
            self.assertEqual(response["response_location"], requirement["response_location"])
            self.assertEqual(
                evidence_by_id[response["evidence_ids"][0]]["owner"],
                requirement["evidence_owner"],
            )

        technical_files = set(self.package["envelopes"]["technical"]["files"])
        financial_files = set(self.package["envelopes"]["financial"]["files"])
        self.assertFalse(technical_files & financial_files)

    def test_missing_mandatory_requirement_blocks(self) -> None:
        incomplete = copy.deepcopy(self.package)
        incomplete["responses"] = [
            item for item in incomplete["responses"] if item["requirement_id"] != "M-FIN-01"
        ]
        errors = validate_bid_package(incomplete)
        self.assertIn("mandatory requirement M-FIN-01 has no response", errors)

    def test_wrong_evidence_owner_blocks_for_owner_reason(self) -> None:
        mutated = copy.deepcopy(self.package)
        mutated["evidence"][0]["owner"] = "finance-lead"

        self.assertEqual(
            validate_bid_package(mutated),
            ["requirement M-TECH-01 evidence owner is not technical-lead"],
        )

    def test_envelope_file_leakage_blocks_for_location_reason(self) -> None:
        mutated = copy.deepcopy(self.package)
        leaked_location = "financial/price-schedule.md"
        mutated["requirements"][0]["response_location"] = leaked_location
        mutated["responses"][0]["response_location"] = leaked_location

        self.assertEqual(
            validate_bid_package(mutated),
            ["requirement M-TECH-01 response location is not in the technical envelope"],
        )

    def test_envelope_file_overlap_blocks_for_separation_reason(self) -> None:
        mutated = copy.deepcopy(self.package)
        mutated["envelopes"]["financial"]["files"].append("technical/methodology.md")

        self.assertEqual(
            validate_bid_package(mutated),
            ["technical and financial envelope files must not overlap"],
        )

    def test_missing_evidence_cannot_bypass_owner_control(self) -> None:
        mutated = copy.deepcopy(self.package)
        mutated["responses"][0]["evidence_ids"] = []

        self.assertEqual(
            validate_bid_package(mutated),
            ["requirement M-TECH-01 has no evidence"],
        )

    def test_empty_requirement_set_blocks_fixture(self) -> None:
        mutated = copy.deepcopy(self.package)
        mutated["requirements"] = []
        mutated["responses"] = []

        self.assertEqual(
            validate_bid_package(mutated),
            ["fixture must declare at least one requirement"],
        )

    def test_thin_claude_bridge_preserves_generic_routing_surface(self) -> None:
        root = Path(__file__).resolve().parents[1]
        claude = (root / "CLAUDE.md").read_text(encoding="utf-8")
        self.assertLessEqual(len(claude.splitlines()), 12)
        self.assertIn("@AGENTS.md", claude)
        self.assertTrue((root / "AGENTS.md").is_file())
        self.assertTrue((root / "README.md").is_file())
        self.assertTrue((root / "skills" / "SKILL.md").is_file())
        self.assertIn("skills/SKILL.md", (root / "README.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
