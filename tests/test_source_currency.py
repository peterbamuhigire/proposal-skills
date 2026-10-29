import copy
import json
import unittest
from datetime import date
from scripts.check_source_currency import ROOT, validate_records


class CurrencyTest(unittest.TestCase):
    def setUp(self):
        self.rows = json.loads((ROOT / 'docs/source-registers/2026-10-currentness.json').read_text())['records']

    def test_scoped_records_at_review(self):
        self.assertEqual(validate_records(self.rows, date(2026, 10, 29)), [])

    def test_expiry_and_false_verification_refused(self):
        self.assertTrue(validate_records(self.rows, date(2026, 11, 6)))
        rows = copy.deepcopy(self.rows)
        rows[0]['verified_date'] = '2027-01-01'
        self.assertTrue(validate_records(rows, date(2026, 10, 29)))

    def test_missing_owner_and_duplicate_refused(self):
        rows = copy.deepcopy(self.rows)
        rows[0]['owner'] = ''
        rows.append(rows[1])
        self.assertGreaterEqual(len(validate_records(rows, date(2026, 10, 29))), 2)
