"""Envelope content scan: a leak across technical and financial envelopes is refused."""
import contextlib
import copy
import io
import json
import shutil
import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.proposal_fixture_check import main, read_scannable, validate_envelope_content

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / 'examples/uganda-eoi-sanitised'
TECHNICAL = 'technical/methodology.md'
FINANCIAL = 'financial/price-schedule.md'


def write_docx(path, parts):
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as archive:
        for name, body in parts.items():
            archive.writestr(name, body)


def paragraph(text):
    return f'<w:p><w:r><w:t>{text}</w:t></w:r></w:p>'


class EnvelopeContentTest(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name) / 'package'
        shutil.copytree(EXAMPLE, self.root)
        self.package = json.loads((self.root / 'validator-input.json').read_text(encoding='utf-8'))

    def append(self, relative, text):
        path = self.root / relative
        path.write_text(path.read_text(encoding='utf-8') + text, encoding='utf-8')

    def scan(self, **options):
        return validate_envelope_content(self.package, self.root, **options)

    def test_clean_example_package_passes(self):
        self.assertEqual(self.scan(), [])

    def test_price_in_the_technical_file_is_refused(self):
        self.append(TECHNICAL, '\nThe fee is UGX 45,000,000 for the lot.\n')
        found = self.scan()
        self.assertEqual(len(found), 1)
        self.assertIn('technical envelope file technical/methodology.md line', found[0])

    def test_amount_before_currency_and_form_id_are_refused(self):
        self.append(TECHNICAL, '\n12,500,000 UGX per lot\nSee FIN-3 for rates.\n')
        self.assertEqual(len(self.scan()), 2)

    def test_technical_form_heading_in_the_financial_file_is_refused(self):
        self.append(FINANCIAL, '\n## TECH-4 Approach and methodology\n')
        found = self.scan()
        self.assertEqual(len(found), 1)
        self.assertIn('financial envelope file financial/price-schedule.md', found[0])

    def test_passing_mention_of_a_technical_form_in_the_financial_file_is_allowed(self):
        self.append(FINANCIAL, '\nQuantities agree with the staffing in form TECH-6.\n')
        self.assertEqual(self.scan(), [])

    def test_docx_body_and_header_are_scanned(self):
        write_docx(self.root / 'technical/summary.docx', {
            'word/document.xml': f'<w:document>{paragraph("Method only")}</w:document>',
            'word/header1.xml': f'<w:hdr>{paragraph("Total USD 90,000")}</w:hdr>',
        })
        self.package['envelopes']['technical']['files'].append('technical/summary.docx')
        found = self.scan()
        self.assertEqual(len(found), 1)
        self.assertIn('summary.docx', found[0])

    def test_clean_docx_passes(self):
        write_docx(self.root / 'technical/summary.docx', {
            'word/document.xml': f'<w:document>{paragraph("Work plan with 12 activities")}</w:document>',
        })
        self.package['envelopes']['technical']['files'].append('technical/summary.docx')
        self.assertEqual(self.scan(), [])

    def test_unreadable_type_fails_closed_unless_accepted(self):
        (self.root / 'technical/annex.pdf').write_bytes(b'%PDF-1.4 binary')
        self.package['envelopes']['technical']['files'].append('technical/annex.pdf')
        found = self.scan()
        self.assertEqual(len(found), 1)
        self.assertIn('NOT_ASSESSED', found[0])
        self.assertEqual(self.scan(allow_unscanned=True), [])

    def test_oversized_document_is_refused_not_expanded(self):
        write_docx(self.root / 'technical/big.docx', {'word/document.xml': 'x' * 20000})
        self.package['envelopes']['technical']['files'].append('technical/big.docx')
        found = self.scan(max_bytes=10000)
        self.assertEqual(len(found), 1)
        self.assertIn('could not be scanned', found[0])
        with self.assertRaises(ValueError):
            read_scannable(self.root / 'technical/big.docx', 10000)

    def test_package_can_override_markers(self):
        self.package['envelope_markers'] = {'technical': [r'secret rate']}
        self.append(TECHNICAL, '\nOur secret rate card is attached.\n')
        self.assertEqual(len(self.scan()), 1)
        self.package['envelope_markers'] = {'technical': ['[unclosed']}
        self.assertTrue(any('invalid pattern' in item for item in self.scan()))
        self.package['envelope_markers'] = {'financial': 'not a list'}
        self.assertTrue(any('list of strings' in item for item in self.scan()))

    def test_missing_files_and_escaping_paths_are_skipped_here(self):
        self.package['envelopes']['technical']['files'] += ['technical/absent.md', '../outside.md']
        self.assertEqual(self.scan(), [])

    def test_command_line_passes_clean_and_fails_a_leak(self):
        spec = self.root / 'validator-input.json'
        with contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(main(['--input', str(spec), '--check-content']), 0)
        self.assertIn('result: PASS', out.getvalue())
        self.append(TECHNICAL, '\nPrice: EUR 8,000\n')
        with contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(main(['--input', str(spec), '--check-content']), 1)
        self.assertIn('belongs to the other envelope', out.getvalue())

    def test_default_run_is_unchanged_and_ignores_content(self):
        self.append(TECHNICAL, '\nPrice: EUR 8,000\n')
        spec = self.root / 'validator-input.json'
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(main(['--input', str(spec)]), 0)
            self.assertEqual(main([]), 0)


if __name__ == '__main__':
    unittest.main()
