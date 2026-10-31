"""PPDA skill keeps the submission-method and security rules read from the 2023 Regulations."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PPDA = ROOT / 'skills/profiles-sectors/sectors/ppda-uganda'

RETIRED = (
    'all qcbs, qbs, lcs, and fbs procurements use two sealed envelopes',
    '- bid securing declaration included',
    'rather than traditional bank guarantees',
    'replaces traditional performance bank guarantee',
)
REQUIRED = (
    'one-stage, single envelope',
    'information technology systems',
    'regs 66(2) and 66(6)(a)',
    'government electronic system',
    'reg 63(9)',
    'contracts regulations 2023, reg 11',
    'not assessed',
)


def retired_hits(text):
    lowered = text.lower()
    return [phrase for phrase in RETIRED if phrase in lowered]


class PpdaSubmissionGuidanceTest(unittest.TestCase):
    def setUp(self):
        self.skill = (PPDA / 'SKILL.md').read_text(encoding='utf-8')
        self.references = '\n'.join(
            path.read_text(encoding='utf-8') for path in sorted((PPDA / 'references').glob('*.md'))
        )

    def test_regulation_anchors_are_present(self):
        lowered = self.skill.lower()
        missing = [anchor for anchor in REQUIRED if anchor not in lowered]
        self.assertEqual(missing, [])

    def test_retired_claims_are_absent(self):
        self.assertEqual(retired_hits(self.skill), [])
        self.assertEqual(retired_hits(self.references), [])

    def test_retired_claim_would_be_caught(self):
        regressed = self.skill + '\n- Bid securing declaration included\n'
        self.assertEqual(retired_hits(regressed), ['- bid securing declaration included'])

    def test_every_envelope_row_names_its_regulation(self):
        rows = [
            line for line in self.skill.splitlines()
            if line.startswith('| ') and ('envelope' in line.lower() or 'two-stage' in line.lower())
            and 'reg' in line.lower()
        ]
        self.assertGreaterEqual(len(rows), 5)


if __name__ == '__main__':
    unittest.main()
