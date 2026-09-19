"""Normal and failure-path checks for the Phase 1 healthcare evidence contracts."""

from __future__ import annotations

import copy
import json
import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "healthcare-evidence-packs.json"
spec = importlib.util.spec_from_file_location(
    "healthcare_evidence", ROOT / "scripts" / "validate_healthcare_evidence_packs.py"
)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class HealthcareEvidencePackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_complete_fixture_passes(self) -> None:
        self.assertEqual(module.validate(self.data), [])

    def test_wrong_tenant_read_cannot_allow_access(self) -> None:
        data = copy.deepcopy(self.data)
        data["integration_tenant_checks"]["cases"][0]["observed"] = "allow"
        self.assertTrue(any("must deny cross-tenant access" in error for error in module.validate(data)))

    def test_duplicate_and_interrupted_cases_are_required(self) -> None:
        data = copy.deepcopy(self.data)
        data["integration_tenant_checks"]["cases"] = data["integration_tenant_checks"]["cases"][:2]
        errors = module.validate(data)
        self.assertIn("missing required integration case: duplicate-event", errors)
        self.assertIn("missing required integration case: interrupted-transfer", errors)

    def test_approved_option_requires_authority_and_evidence(self) -> None:
        data = copy.deepcopy(self.data)
        data["governance_budget"]["decisions"][0]["authority"] = ""
        data["governance_budget"]["decisions"][0]["evidence_ids"] = []
        errors = module.validate(data)
        self.assertTrue(any("approved decision DEC-SYNTH-01 requires authority" in e for e in errors))
        self.assertTrue(any("decision DEC-SYNTH-01 evidence_ids" in e for e in errors))

    def test_material_budget_line_needs_basis_period_and_reviewer(self) -> None:
        data = copy.deepcopy(self.data)
        line = data["governance_budget"]["budget_lines"][0]
        line["basis_type"] = "textbook"
        line["period"] = ""
        line["reviewer"] = ""
        errors = module.validate(data)
        self.assertTrue(any("impermissible textbook basis" in e for e in errors))
        self.assertTrue(any("requires period" in e for e in errors))
        self.assertTrue(any("requires reviewer" in e for e in errors))

    def test_closed_case_and_safety_competency_cannot_bypass_gates(self) -> None:
        data = copy.deepcopy(self.data)
        data["hr_safety_metrics"]["conduct_cases"][0]["disposition"] = ""
        data["hr_safety_metrics"]["competencies"][0]["gap_status"] = "missing"
        errors = module.validate(data)
        self.assertTrue(any("closed conduct case CASE-SYNTH-01 requires disposition" in e for e in errors))
        self.assertTrue(any("safety-critical competency COMP-SYNTH-01 is not cleared" in e for e in errors))

    def test_metric_requires_second_reviewer_and_reproduction_inputs(self) -> None:
        data = copy.deepcopy(self.data)
        metric = data["hr_safety_metrics"]["metrics"][0]
        metric["second_reviewer"] = ""
        metric["reproduction_inputs_or_hash"] = ""
        errors = module.validate(data)
        self.assertTrue(any("metric METRIC-SYNTH-01 requires second_reviewer" in e for e in errors))
        self.assertTrue(any("metric METRIC-SYNTH-01 requires reproduction_inputs_or_hash" in e for e in errors))

    def test_malformed_currentness_record_is_not_a_pass(self) -> None:
        data = copy.deepcopy(self.data)
        data["evidence_records"][0]["support_review"]["source_ids"] = []
        errors = module.validate(data)
        self.assertTrue(any("non-no-source state needs a source_id" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
