import json
import unittest
from pathlib import Path


class ApprovalAdapterTests(unittest.TestCase):
    def test_submission_and_pricing_actions_are_gated(self):
        payload = json.loads((Path(__file__).parents[1] / "docs" / "approval-adapter.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["engine"], "proposal")
        actions = {item["action_type"]: item for item in payload["actions"]}
        for action_type in ("proposal.pricing.approve", "proposal.tender.submit", "proposal.procurement.terms.accept"):
            action = actions[action_type]
            self.assertEqual(action["class"], "L3")
            self.assertTrue(action["requires_dual_approval"] and action["verification"])


if __name__ == "__main__":
    unittest.main()
