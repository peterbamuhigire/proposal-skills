import copy, json, importlib.util, unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location("commercial", Path(__file__).parents[1]/"scripts"/"validate_p0_commercial_fixture.py")
assert spec and spec.loader
module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)

class CommercialFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.data=json.loads((Path(__file__).parent/"fixtures"/"p0-commercial-fixture.json").read_text(encoding="utf-8"))
    def test_fixture_passes(self): self.assertEqual(module.validate(self.data), [])
    def test_missing_claim_file_fails(self):
        data=copy.deepcopy(self.data); data["requirements"][0]["file_ids"]=["MISSING"]
        self.assertTrue(any("missing file" in e for e in module.validate(data)))
    def test_price_mismatch_fails(self):
        data=copy.deepcopy(self.data); data["work_packages"][0]["amount"]=250
        self.assertTrue(any("amount does not equal days times rate" in e for e in module.validate(data)))
    def test_envelope_overlap_fails(self):
        data=copy.deepcopy(self.data); data["envelopes"]["financial"].append("FILE-TECH-01")
        self.assertTrue(any("envelopes overlap" in e for e in module.validate(data)))
