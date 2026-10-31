import copy
import json
import unittest
from datetime import date, timedelta
from scripts.check_source_currency import ROOT, validate_records


class CurrencyTest(unittest.TestCase):
    def setUp(self):
        self.rows = json.loads((ROOT / 'docs/source-registers/2026-10-currentness.json').read_text())['records']
        self.latest_verified = max(date.fromisoformat(r['verified_date']) for r in self.rows if r['verified_date'])
        self.last_review = max(date.fromisoformat(r['review_date']) for r in self.rows)

    def test_scoped_records_at_review(self):
        self.assertEqual(validate_records(self.rows, self.latest_verified), [])

    def test_expiry_and_false_verification_refused(self):
        self.assertTrue(validate_records(self.rows, self.last_review + timedelta(days=1)))
        rows = copy.deepcopy(self.rows)
        scoped = next(r for r in rows if r['support_state'] == 'SCOPED')
        scoped['verified_date'] = '2027-01-01'
        self.assertTrue(validate_records(rows, self.latest_verified))

    def test_missing_owner_and_duplicate_refused(self):
        rows = copy.deepcopy(self.rows)
        rows[0]['owner'] = ''
        rows.append(rows[1])
        self.assertGreaterEqual(len(validate_records(rows, self.latest_verified)), 2)

    def test_not_assessed_with_a_verified_date_is_refused(self):
        rows = copy.deepcopy(self.rows)
        row = next(r for r in rows if r['support_state'] == 'NOT_ASSESSED')
        row['verified_date'] = '2026-10-31'
        self.assertTrue(any('must not carry a verified date' in e for e in validate_records(rows, self.latest_verified)))

    def test_review_window_cannot_be_stretched(self):
        rows = copy.deepcopy(self.rows)
        row = next(r for r in rows if r['support_state'] == 'SCOPED')
        row['review_date'] = '2027-12-31'
        self.assertTrue(any('too far after verification' in e for e in validate_records(rows, self.latest_verified)))

    def test_non_https_url_and_unknown_class_refused(self):
        rows = copy.deepcopy(self.rows)
        rows[0]['url'] = 'http://example.org/page'
        rows[1]['freshness_class'] = 'forever'
        errors = validate_records(rows, self.latest_verified)
        self.assertTrue(any('url must be https' in e for e in errors))
        self.assertTrue(any('unknown freshness class' in e for e in errors))

    def test_records_cover_the_claims_the_skills_rely_on(self):
        ids = {r['id'] for r in self.rows}
        self.assertTrue({'PPDA-ACT', 'PPDA-REGS-2023', 'PPDA-EGP', 'WB-RFP', 'WB-IPF', 'AI-ACT', 'ISO-42001'} <= ids)
