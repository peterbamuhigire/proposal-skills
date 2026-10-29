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
