"""Source-backed crosswalk regression, not a live bid compliance assessment."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def form_errors(text, expected):
    errors = []
    for group in ('technical', 'financial'):
        for identifier, label in expected[group].items():
            rows = [row for row in text.splitlines() if row.startswith(f'| {identifier} |')]
            if len(rows) != 1 or label not in rows[0]:
                errors.append(identifier)
    if any(row.startswith('| FIN-5 |') or row.startswith('### FIN-5:') for row in text.splitlines()):
        errors.append('unsupported FIN-5')
    return errors


class FormMapTest(unittest.TestCase):
    def setUp(self):
        self.expected = json.loads((ROOT / 'tests/fixtures/world-bank-form-map.json').read_text())
        self.text = (ROOT / 'skills/profiles-sectors/sectors/world-bank/references/tech-fin-forms-guide.md').read_text()

    def test_current_official_crosswalk(self):
        self.assertEqual(form_errors(self.text, self.expected), [])

    def test_stale_staffing_map_and_extra_financial_form_refused(self):
        stale = self.text.replace('| TECH-7 | Code of Conduct', '| TECH-7 | Staffing schedule')
        stale += '\n### FIN-5: Miscellaneous Expenses\n'
        self.assertEqual(form_errors(stale, self.expected), ['TECH-7', 'unsupported FIN-5'])

    def test_duplicate_form_refused(self):
        duplicate = self.text + '\n| TECH-5 | Work schedule and planning for deliverables | extra |\n'
        self.assertIn('TECH-5', form_errors(duplicate, self.expected))


class RatedCriteriaTest(unittest.TestCase):
    """Numbers in the parent skill and scoring guide match the inspected sources."""

    def setUp(self):
        self.data = json.loads((ROOT / 'tests/fixtures/world-bank-form-map.json').read_text())
        base = ROOT / 'skills/profiles-sectors/sectors/world-bank'
        self.skill = (base / 'SKILL.md').read_text(encoding='utf-8')
        self.guide = (base / 'references/evaluation-scoring-guide.md').read_text(encoding='utf-8')

    def test_indicative_ranges_are_stated(self):
        ranges = self.data['rated_criteria_ranges']
        for key in ('firm_experience', 'methodology', 'key_experts', 'transfer_of_knowledge', 'nationals'):
            low, high = ranges[key].split('-')
            self.assertIn(f'{low}-{high}%', self.skill, key)
        low, high = ranges['minimum_technical_score_indicative'].split('-')
        self.assertIn(f'{low}-{high}%', self.skill)
        for key in ('key_expert_general_qualifications_weight', 'key_expert_adequacy_weight'):
            low, high = ranges[key].split('-')
            self.assertIn(f'{low}-{high}%', self.skill, key)

    def test_retired_universal_claims_are_absent(self):
        for phrase in self.data['retired_phrases']:
            for name, text in (('SKILL.md', self.skill), ('scoring guide', self.guide)):
                self.assertNotIn(phrase, text.lower(), f'{name}: {phrase}')

    def test_a_retired_claim_would_be_caught(self):
        regressed = self.skill + '\nThe pass mark is typically **75 out of 100**.\n'
        hits = [p for p in self.data['retired_phrases'] if p in regressed.lower()]
        self.assertEqual(hits, ['typically **75 out of 100**'])
