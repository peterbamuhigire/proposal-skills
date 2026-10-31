"""Routing fixtures keep three positives and two owned negatives for the audited routes."""
import json
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDITED = (
    'skills/profiles-sectors/sectors/world-bank',
    'skills/profiles-sectors/sectors/ppda-uganda',
    'skills/profiles-sectors/sectors/afdb',
    'skills/pipeline/06-methodology',
)


def census(fixtures):
    positives, negatives = Counter(), Counter()
    for fixture in fixtures:
        positives[fixture['expected']] += 1
        for skill in fixture.get('forbidden_primary', []):
            negatives[skill] += 1
    return positives, negatives


class RoutingCoverageTest(unittest.TestCase):
    def setUp(self):
        data = json.loads((ROOT / 'tests/fixtures/routing-fixtures.json').read_text(encoding='utf-8'))
        self.fixtures = data['fixtures']

    def test_audited_routes_keep_three_positives_and_two_owned_negatives(self):
        positives, negatives = census(self.fixtures)
        for skill in AUDITED:
            self.assertGreaterEqual(positives[skill], 3, f'{skill} positives')
            self.assertGreaterEqual(negatives[skill], 2, f'{skill} owned negatives')

    def test_every_fixture_names_a_live_skill_and_forbidden_routes_are_live(self):
        live = {
            path.parent.relative_to(ROOT).as_posix()
            for path in (ROOT / 'skills').rglob('SKILL.md')
        }
        for fixture in self.fixtures:
            self.assertIn(fixture['expected'], live, fixture['id'])
            for skill in fixture.get('forbidden_primary', []):
                self.assertIn(skill, live, fixture['id'])
                self.assertNotEqual(skill, fixture['expected'], fixture['id'])

    def test_fixture_ids_are_unique(self):
        ids = [fixture['id'] for fixture in self.fixtures]
        self.assertEqual(len(ids), len(set(ids)))

    def test_census_would_notice_a_missing_negative(self):
        trimmed = [f for f in self.fixtures if 'forbidden_primary' not in f]
        _, negatives = census(trimmed)
        self.assertEqual(negatives['skills/profiles-sectors/sectors/afdb'], 0)


if __name__ == '__main__':
    unittest.main()
