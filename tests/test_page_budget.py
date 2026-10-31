"""Weighted page-budget arithmetic: proposal, checks and failure cases."""
import contextlib
import copy
import io
import json
import tempfile
import unittest
from pathlib import Path

from scripts.page_budget_check import check, main, propose, validate_spec

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / 'tests/fixtures/page-budget-example.json'
METHOD = 'methodology'
EXPERTS = 'key_experts'
NATIONAL = 'national_participation_and_knowledge_transfer'
DATA = 'data_protection_and_continuity'


class PageBudgetTest(unittest.TestCase):
    def setUp(self):
        self.spec = json.loads(FIXTURE.read_text(encoding='utf-8'))
        self.good = {METHOD: 2.0, EXPERTS: 1.5, NATIONAL: 1.5, DATA: 1.0, 'presentation': 0}

    def test_fixture_is_valid_and_labelled_fictional(self):
        self.assertEqual(validate_spec(self.spec), [])
        self.assertTrue(self.spec['label'].startswith('FICTIONAL TEST DATA'))

    def test_proposal_matches_hand_calculation(self):
        # 6 pages over 95 live points (presentation is embedded): 1.89, 1.58, 1.58, 0.95,
        # rounded to quarter pages by largest remainder: 2.0, 1.5, 1.5, 1.0.
        self.assertEqual(propose(self.spec), self.good)
        self.assertEqual(sum(propose(self.spec).values()), self.spec['page_cap'])

    def test_proposal_is_deterministic_and_checks_clean(self):
        self.assertEqual(propose(self.spec), propose(copy.deepcopy(self.spec)))
        self.assertEqual(check(self.spec, propose(self.spec)), [])

    def test_floor_overrides_proportion(self):
        spec = copy.deepcopy(self.spec)
        spec['criteria'][3]['floor_pages'] = 2.0
        result = propose(spec)
        self.assertEqual(result[DATA], 2.0)
        self.assertEqual(sum(result.values()), 6)

    def test_floors_beyond_the_cap_are_refused(self):
        spec = copy.deepcopy(self.spec)
        spec['criteria'][0]['floor_pages'] = 5.5
        with self.assertRaises(ValueError):
            propose(spec)

    def test_starved_criterion_fails(self):
        bad = {**self.good, DATA: 0, METHOD: 3.0}
        self.assertTrue(any('no pages' in error for error in check(self.spec, bad)))

    def test_over_cap_fails(self):
        bad = {**self.good, METHOD: 3.0}
        self.assertTrue(any('cap is 6' in error for error in check(self.spec, bad)))

    def test_floor_unmet_fails(self):
        bad = {**self.good, NATIONAL: 1.0, METHOD: 2.5}
        self.assertTrue(any('below its floor' in error for error in check(self.spec, bad)))

    def test_lower_weight_with_more_pages_fails(self):
        bad = {METHOD: 1.0, EXPERTS: 1.0, NATIONAL: 1.25, DATA: 2.75, 'presentation': 0}
        self.assertTrue(any('has more pages than' in error for error in check(self.spec, bad)))

    def test_share_gap_needs_a_reason(self):
        spec = copy.deepcopy(self.spec)
        spec['criteria'][0]['floor_pages'] = 0.5
        lean = {METHOD: 1.0, EXPERTS: 1.5, NATIONAL: 1.75, DATA: 1.75, 'presentation': 0}
        self.assertTrue(any('of pages for' in error for error in check(spec, lean)))
        spec['criteria'][0]['justification'] = 'method detail sits in the annex the RFP excludes from the cap'
        lean_errors = [e for e in check(spec, lean) if 'of pages for' in e]
        self.assertEqual(lean_errors, [])

    def test_unknown_and_malformed_allocations_fail(self):
        self.assertTrue(check(self.spec, {**self.good, 'extra': 1}))
        self.assertTrue(check(self.spec, {**self.good, DATA: 'one'}))
        self.assertTrue(check(self.spec, {**self.good, DATA: -1}))

    def test_invalid_specifications_are_refused(self):
        spec = copy.deepcopy(self.spec)
        spec['page_cap'] = 6.1
        self.assertTrue(validate_spec(spec))
        spec = copy.deepcopy(self.spec)
        spec['criteria'].append(dict(spec['criteria'][0]))
        self.assertTrue(any('duplicate' in e for e in validate_spec(spec)))
        spec = copy.deepcopy(self.spec)
        spec['criteria'][1]['points'] = -3
        self.assertTrue(validate_spec(spec))
        self.assertTrue(validate_spec([]))

    def test_command_line_pass_and_fail(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(main([str(FIXTURE), '--propose']), 0)
        self.assertIn('2 | 33.3%', out.getvalue())
        spec = copy.deepcopy(self.spec)
        spec['allocation'] = {**self.good, DATA: 0, METHOD: 3.0}
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'spec.json'
            path.write_text(json.dumps(spec), encoding='utf-8')
            with contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(main([str(path)]), 1)
        self.assertIn('FAIL', out.getvalue())


if __name__ == '__main__':
    unittest.main()
