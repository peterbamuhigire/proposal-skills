"""Stale World Bank form labels are refused in any active skill (label check only)."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.check_form_labels import ROOT, RULES_PATH, load_rules, scan_text, validate


class FormLabelTest(unittest.TestCase):
    def setUp(self):
        self.rules = load_rules(ROOT)

    def messages(self, text):
        return [message for _, message in scan_text(text, self.rules)]

    def test_active_skills_are_clean(self):
        self.assertEqual(validate(ROOT), [])

    def test_retired_table_rows_refused(self):
        for row in (
            "| **TECH-5** | Team Composition and Task Assignments | `07-team-composition/` |",
            "| **TECH-7** | Staffing Schedule (person-months) | `08-work-plan/` |",
            "| **TECH-8** | Work Schedule (Gantt chart) | `08-work-plan/` |",
        ):
            self.assertTrue(self.messages(row), row)

    def test_retired_headings_and_ranges_refused(self):
        self.assertTrue(self.messages("### TECH-5/6: Key Personnel"))
        self.assertTrue(self.messages("### Work Plan (TECH-7/8) - Embedded in Methodology Score"))
        self.assertTrue(self.messages("Complete TECH-1 through TECH-8 and FIN-1 through FIN-5 forms"))

    def test_current_labels_pass(self):
        for line in (
            "| TECH-5 | Work schedule and planning for deliverables | agrees with TECH-4 |",
            "| TECH-6 | Team composition, assignment and key experts' inputs; attached CVs | x |",
            "| TECH-7 | Code of Conduct for experts | issued form |",
            "| TECH-8 | SEA/SH performance declaration | declarations |",
            "FIN-1 through FIN-4 are the financial forms.",
            "Align TECH-4 work plan with the TECH-7 Code of Conduct and TECH-5 schedule.",
        ):
            self.assertEqual(self.messages(line), [], line)

    def test_warning_paragraph_is_exempt_but_table_row_is_not(self):
        warning = (
            "Do not carry forward the older local mapping\n"
            "of TECH-5 to team composition, TECH-7 to staffing schedule or TECH-8 to Gantt.\n"
            "There is no FIN-5 in this checklist.\n"
        )
        self.assertEqual(self.messages(warning), [])
        row_inside_warning = warning + "| TECH-7 | Staffing schedule | x |\n"
        self.assertTrue(self.messages(row_inside_warning))

    def test_planted_label_in_a_skill_tree_is_found(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / RULES_PATH).parent.mkdir(parents=True)
            shutil.copy(ROOT / RULES_PATH, root / RULES_PATH)
            skill = root / "skills" / "demo" / "SKILL.md"
            skill.parent.mkdir(parents=True)
            skill.write_text("| TECH-7 | Staffing schedule | x |\n", encoding="utf-8")
            found = validate(root)
            self.assertEqual(len(found), 1)
            self.assertTrue(all("skills/demo/SKILL.md:1" in item for item in found))

    def test_parent_skill_table_agrees_with_the_form_map(self):
        text = (ROOT / "skills/profiles-sectors/sectors/world-bank/SKILL.md").read_text(encoding="utf-8")
        expected = {
            "TECH-4": "approach",
            "TECH-5": "work schedule",
            "TECH-6": "team composition",
            "TECH-7": "code of conduct",
            "TECH-8": "sexual exploitation",
        }
        for identifier, keyword in expected.items():
            rows = [row for row in text.splitlines() if row.startswith(f"| **{identifier}** |")]
            self.assertEqual(len(rows), 1, identifier)
            self.assertIn(keyword, rows[0].lower(), identifier)

    def test_missing_rules_file_fails_closed(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertTrue(validate(Path(folder)))

    def test_rules_cover_every_retired_pairing(self):
        data = json.loads((ROOT / RULES_PATH).read_text(encoding="utf-8"))
        self.assertEqual(set(data["stale_associations"]), {"TECH-5", "TECH-7", "TECH-8"})
        self.assertEqual(data["unsupported_forms"], ["FIN-5"])


if __name__ == "__main__":
    unittest.main()
