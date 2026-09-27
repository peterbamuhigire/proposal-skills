"""Behavioural checks for the fictional proposal evidence fixture."""

from __future__ import annotations

import copy
import csv
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from scripts.proposal_fixture_check import main, validate_bid_package, validate_response_files


FIXTURE = Path(__file__).parent / "fixtures" / "fictional-bid-package.json"
SPECIMEN = Path(__file__).parent.parent / "examples" / "uganda-eoi-sanitised"


class ProposalFixtureBehaviourTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.package = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_complete_fixture_is_traceable_and_separated(self) -> None:
        self.assertEqual(validate_bid_package(self.package), [])
        response_by_requirement = {
            item["requirement_id"]: item for item in self.package["responses"]
        }
        evidence_by_id = {item["id"]: item for item in self.package["evidence"]}
        for requirement in self.package["requirements"]:
            response = response_by_requirement[requirement["id"]]
            self.assertEqual(response["envelope"], requirement["envelope"])
            self.assertEqual(response["response_location"], requirement["response_location"])
            self.assertEqual(
                evidence_by_id[response["evidence_ids"][0]]["owner"],
                requirement["evidence_owner"],
            )

        technical_files = set(self.package["envelopes"]["technical"]["files"])
        financial_files = set(self.package["envelopes"]["financial"]["files"])
        self.assertFalse(technical_files & financial_files)

    def test_response_paths_must_exist_within_package_root_when_requested(self) -> None:
        mutated = copy.deepcopy(self.package)
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            file_paths = (
                "technical/methodology.md",
                "financial/price-schedule.md",
            )
            for file_path in file_paths:
                target = root.joinpath(*file_path.split("/"))
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("synthetic test file", encoding="utf-8")
            for requirement, file_path in zip(mutated["requirements"], file_paths):
                requirement["response_location"] = file_path
            for response, file_path in zip(mutated["responses"], file_paths):
                response["response_location"] = file_path
            mutated["envelopes"]["technical"]["files"] = [file_paths[0]]
            mutated["envelopes"]["financial"]["files"] = [file_paths[1]]
            self.assertEqual(validate_response_files(mutated, root), [])

            missing_path = mutated["requirements"][0]["response_location"]
            (root / missing_path).unlink()
            self.assertIn(
                f"requirement M-TECH-01 response file does not exist: {missing_path}",
                validate_response_files(mutated, root),
            )

    def test_check_files_reports_malformed_envelope_paths_without_crashing(self) -> None:
        mutated = copy.deepcopy(self.package)
        mutated["envelopes"]["technical"]["files"] = None
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            input_path = root / "malformed-fixture.json"
            input_path.write_text(json.dumps(mutated), encoding="utf-8")
            output = io.StringIO()
            with redirect_stdout(output):
                result = main(["--input", str(input_path), "--check-files"])

        self.assertEqual(result, 1)
        self.assertIn("result: FAIL", output.getvalue())
        self.assertIn("envelope technical files must be a list of strings", output.getvalue())

    def test_synthetic_requirement_text_is_traceable_to_fictional_source(self) -> None:
        package = json.loads((SPECIMEN / "validator-input.json").read_text(encoding="utf-8"))
        source = "\n".join(
            (SPECIMEN / name).read_text(encoding="utf-8")
            for name in ("fictional-solicitation.md", "addendum-a1.md")
        ).casefold()
        for requirement in package["requirements"]:
            with self.subTest(requirement=requirement["id"]):
                self.assertIn(requirement["text"].casefold(), source)

    def test_cli_checks_the_complete_synthetic_package_paths(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            status = main([
                "--input", str(SPECIMEN / "validator-input.json"),
                "--check-files",
            ])
        self.assertEqual(status, 0)
        self.assertIn("result: PASS", output.getvalue())

    def test_matrix_and_evidence_register_match_validator_input(self) -> None:
        package = json.loads((SPECIMEN / "validator-input.json").read_text(encoding="utf-8"))
        with (SPECIMEN / "compliance-matrix.csv").open(encoding="utf-8", newline="") as handle:
            matrix = list(csv.DictReader(handle))
        with (SPECIMEN / "evidence-register.csv").open(encoding="utf-8", newline="") as handle:
            evidence_rows = {row["evidence_id"]: row for row in csv.DictReader(handle)}
        requirements = {row["id"]: row for row in package["requirements"]}
        responses = {row["requirement_id"]: row for row in package["responses"]}
        evidence = {row["id"]: row for row in package["evidence"]}

        self.assertEqual({row["requirement_id"] for row in matrix}, set(requirements))
        for row in matrix:
            requirement = requirements[row["requirement_id"]]
            response = responses[row["requirement_id"]]
            evidence_item = evidence[row["evidence_id"]]
            registered_evidence = evidence_rows[row["evidence_id"]]
            self.assertEqual(row["source_clause"], requirement["source_clause"])
            self.assertEqual(row["response_location"], requirement["response_location"])
            self.assertEqual(row["response_location"], response["response_location"])
            self.assertIn(row["evidence_id"], response["evidence_ids"])
            self.assertEqual(row["owner"], requirement["evidence_owner"])
            self.assertEqual(row["owner"], evidence_item["owner"])
            self.assertEqual(row["owner"], registered_evidence["owner"])
            self.assertEqual(row["evidence_status"], evidence_item["status"])
            self.assertEqual(row["evidence_status"], registered_evidence["status"])

    def test_duplicate_identifiers_cannot_overwrite_records(self):
        for collection in ('requirements', 'responses', 'evidence'):
            with self.subTest(collection=collection):
                mutated = copy.deepcopy(self.package)
                mutated[collection].append(copy.deepcopy(mutated[collection][0]))
                self.assertTrue(any('duplicate' in e for e in validate_bid_package(mutated)))

    def test_missing_mandatory_flag_is_not_optional(self):
        mutated = copy.deepcopy(self.package)
        del mutated['requirements'][0]['mandatory']
        self.assertTrue(any('mandatory must be boolean' in e for e in validate_bid_package(mutated)))

    def test_unavailable_evidence_cannot_support_response(self):
        mutated = copy.deepcopy(self.package)
        mutated['evidence'][0]['status'] = 'not-assessed'
        self.assertTrue(any('is not available' in e for e in validate_bid_package(mutated)))

    def test_approval_needs_named_owner(self):
        mutated = copy.deepcopy(self.package)
        mutated['approvals'][0]['owner'] = ' '
        self.assertIn('technical envelope has no approved review record', validate_bid_package(mutated))

    def test_malformed_shapes_return_findings(self):
        for value in (None, [], 'text'):
            self.assertTrue(validate_bid_package(value))
        for collection in ('requirements', 'responses', 'evidence', 'approvals', 'envelopes'):
            with self.subTest(collection=collection):
                mutated = copy.deepcopy(self.package)
                mutated[collection] = None
                self.assertTrue(validate_bid_package(mutated))

    def test_missing_mandatory_requirement_blocks(self) -> None:
        incomplete = copy.deepcopy(self.package)
        incomplete["responses"] = [
            item for item in incomplete["responses"] if item["requirement_id"] != "M-FIN-01"
        ]
        errors = validate_bid_package(incomplete)
        self.assertIn("mandatory requirement M-FIN-01 has no response", errors)

    def test_wrong_evidence_owner_blocks_for_owner_reason(self) -> None:
        mutated = copy.deepcopy(self.package)
        mutated["evidence"][0]["owner"] = "finance-lead"

        self.assertEqual(
            validate_bid_package(mutated),
            ["requirement M-TECH-01 evidence owner is not technical-lead"],
        )

    def test_evidence_owners_require_nonblank_strings(self) -> None:
        for owner in (None, '', ' \t', True, 1, ['not-a-name'], {'role': 'not-a-name'}):
            for target in ('requirements', 'evidence', 'both'):
                with self.subTest(owner=owner, target=target):
                    mutated = copy.deepcopy(self.package)
                    if target in ('requirements', 'both'):
                        mutated['requirements'][0]['evidence_owner'] = owner
                    if target in ('evidence', 'both'):
                        mutated['evidence'][0]['owner'] = owner
                    errors = validate_bid_package(mutated)
                    if target in ('requirements', 'both'):
                        self.assertIn('requirement M-TECH-01 evidence_owner must be a nonblank string', errors)
                    if target in ('evidence', 'both'):
                        self.assertIn('evidence E-TECH-01 owner must be a nonblank string', errors)

    def test_parent_traversal_is_rejected_in_all_fixture_paths(self) -> None:
        for alias in ('technical/../financial/price-schedule.md',
                      'technical\\..\\financial\\price-schedule.md'):
            for target in ('files', 'requirements', 'responses', 'all'):
                with self.subTest(alias=alias, target=target):
                    mutated = copy.deepcopy(self.package)
                    if target in ('files', 'all'):
                        mutated['envelopes']['technical']['files'][0] = alias
                    for collection in ('requirements', 'responses'):
                        if target in (collection, 'all'):
                            mutated[collection][0]['response_location'] = alias
                    errors = validate_bid_package(mutated)
                    if target in ('files', 'all'):
                        self.assertIn('envelope technical files must not contain parent traversal', errors)
                    for collection in ('requirements', 'responses'):
                        if target in (collection, 'all'):
                            self.assertIn(f'{collection} M-TECH-01 response_location must not contain parent traversal', errors)

    def test_envelope_file_leakage_blocks_for_location_reason(self) -> None:
        mutated = copy.deepcopy(self.package)
        leaked_location = "financial/price-schedule.md"
        mutated["requirements"][0]["response_location"] = leaked_location
        mutated["responses"][0]["response_location"] = leaked_location

        self.assertEqual(
            validate_bid_package(mutated),
            ["requirement M-TECH-01 response location is not in the technical envelope"],
        )

    def test_envelope_file_overlap_blocks_for_separation_reason(self) -> None:
        mutated = copy.deepcopy(self.package)
        mutated["envelopes"]["financial"]["files"].append("technical/methodology.md")

        self.assertEqual(
            validate_bid_package(mutated),
            ["technical and financial envelope files must not overlap"],
        )

    def test_missing_evidence_cannot_bypass_owner_control(self) -> None:
        mutated = copy.deepcopy(self.package)
        mutated["responses"][0]["evidence_ids"] = []

        self.assertEqual(
            validate_bid_package(mutated),
            ["requirement M-TECH-01 has no evidence"],
        )

    def test_empty_requirement_set_blocks_fixture(self) -> None:
        mutated = copy.deepcopy(self.package)
        mutated["requirements"] = []
        mutated["responses"] = []

        self.assertEqual(
            validate_bid_package(mutated),
            ["fixture must declare at least one requirement"],
        )

    def test_addendum_requirement_blocks_until_matrix_response_and_evidence_match(self) -> None:
        amended = copy.deepcopy(self.package)
        amended["amendments"] = [{
            "id": "ADD-001",
            "source_clause": "Fictional Addendum 1, clause A.1",
            "requirement_ids": ["M-TECH-02"],
        }]
        amended["requirements"].append({
            "id": "M-TECH-02",
            "text": "Provide a named delivery-risk register",
            "source_clause": "Fictional Addendum 1, clause A.1",
            "mandatory": True,
            "envelope": "technical",
            "response_location": "technical/methodology.md",
            "evidence_owner": "technical-lead",
            "amendment_id": "ADD-001",
        })
        errors = validate_bid_package(amended)
        self.assertIn("mandatory requirement M-TECH-02 has no response", errors)

        amended["responses"].append({
            "requirement_id": "M-TECH-02",
            "response_location": "technical/methodology.md",
            "envelope": "technical",
            "evidence_ids": ["E-TECH-02"],
        })
        errors = validate_bid_package(amended)
        self.assertIn("requirement M-TECH-02 cites missing evidence E-TECH-02", errors)

        amended["evidence"].append({
            "id": "E-TECH-02",
            "owner": "technical-lead",
            "status": "available",
            "label": "fictional risk-register note",
        })
        self.assertEqual(validate_bid_package(amended), [])

    def test_deadline_conflict_missing_signature_and_authority_block_readiness(self) -> None:
        mutated = copy.deepcopy(self.package)
        deadline = mutated["submission_controls"]["deadline"]
        deadline["conflicts"] = [{
            "value": "2030-01-14T17:00:00+03:00",
            "source": "Fictional Addendum 2, clause 1",
        }]
        deadline["status"] = "unresolved"
        mutated["submission_controls"]["required_signatures"][0]["status"] = "missing"
        mutated["submission_controls"]["final_authority"]["status"] = "pending"
        errors = validate_bid_package(mutated)
        self.assertIn("submission deadline conflict is unresolved", errors)
        self.assertIn("required signature authorised signatory is missing or unowned", errors)
        self.assertIn("final submission authority is not approved by a named owner", errors)

    def test_resolved_deadline_conflict_must_match_final_deadline_value(self) -> None:
        mutated = copy.deepcopy(self.package)
        deadline = mutated["submission_controls"]["deadline"]
        deadline["conflicts"] = [{
            "value": "2030-01-14T17:00:00+03:00",
            "source": "Fictional Addendum 2, clause 1",
        }]
        deadline["resolution"] = {
            "value": "2030-01-15T17:00:00+03:00",
            "source": "Fictional Addendum 2, clause 1",
            "owner": "bid-lead",
        }
        self.assertEqual(validate_bid_package(mutated), [])

        deadline["value"] = "2030-01-16T17:00:00+03:00"
        self.assertIn(
            "resolved deadline value must match the final submission deadline",
            validate_bid_package(mutated),
        )

    def test_eoi_cannot_bypass_deadline_signature_and_authority_controls(self) -> None:
        mutated = copy.deepcopy(self.package)
        del mutated["submission_controls"]
        self.assertIn("EOI package requires submission_controls", validate_bid_package(mutated))

        mutated = copy.deepcopy(self.package)
        mutated["submission_controls"]["deadline"]["value"] = "2030-01-15T17:00:00"
        self.assertIn(
            "submission deadline must include a timezone offset",
            validate_bid_package(mutated),
        )

    def test_signature_and_final_authority_require_evidence(self) -> None:
        mutated = copy.deepcopy(self.package)
        mutated["submission_controls"]["required_signatures"][0]["evidence_id"] = "E-MISSING"
        mutated["submission_controls"]["final_authority"]["evidence_id"] = "E-MISSING"
        errors = validate_bid_package(mutated)
        self.assertIn(
            "required signature authorised signatory has no available evidence",
            errors,
        )
        self.assertIn("final submission authority has no available evidence", errors)

    def test_signature_and_final_authority_evidence_owner_must_match(self) -> None:
        mutated = copy.deepcopy(self.package)
        mutated["submission_controls"]["required_signatures"][0]["owner"] = "wrong-signer"
        mutated["submission_controls"]["final_authority"]["owner"] = "wrong-approver"
        errors = validate_bid_package(mutated)
        self.assertIn(
            "required signature authorised signatory evidence owner does not match signer",
            errors,
        )
        self.assertIn(
            "final submission authority evidence owner does not match approver",
            errors,
        )

    def test_envelope_approval_evidence_owner_must_match(self) -> None:
        mutated = copy.deepcopy(self.package)
        mutated["approvals"][0]["owner"] = "wrong-reviewer"
        errors = validate_bid_package(mutated)
        self.assertIn(
            "technical approval evidence owner does not match approver",
            errors,
        )
        self.assertIn(
            "technical envelope has no approved review record",
            errors,
        )

    def test_technical_and_financial_approvals_need_separate_evidence(self) -> None:
        mutated = copy.deepcopy(self.package)
        mutated["approvals"][1]["evidence_id"] = "E-MISSING"
        errors = validate_bid_package(mutated)
        self.assertIn("financial approval has no available evidence", errors)
        self.assertIn("financial envelope has no approved review record", errors)

    def test_unsupported_experience_claim_is_excluded_from_response(self) -> None:
        mutated = copy.deepcopy(self.package)
        mutated["submission_controls"]["claims"][0]["included"] = True
        self.assertIn(
            "unsupported claim C-EXP-01 must be excluded",
            validate_bid_package(mutated),
        )

    def test_supported_claim_rejects_non_string_evidence_ids_without_crashing(self) -> None:
        for evidence_id in ({"unexpected": "object"}, ["nested"], " "):
            with self.subTest(evidence_id=evidence_id):
                mutated = copy.deepcopy(self.package)
                claim = mutated["submission_controls"]["claims"][0]
                claim["status"] = "supported"
                claim["included"] = True
                claim["evidence_ids"] = [evidence_id]
                errors = validate_bid_package(mutated)
                self.assertIn(
                    "supported claim C-EXP-01 evidence_ids must be nonblank strings",
                    errors,
                )

    def test_requirement_without_a_source_clause_is_a_gap(self) -> None:
        mutated = copy.deepcopy(self.package)
        del mutated["requirements"][0]["source_clause"]
        self.assertIn(
            "requirement M-TECH-01 requires a source_clause",
            validate_bid_package(mutated),
        )

    def test_malformed_amendment_mapping_is_reported_without_crashing(self) -> None:
        mutated = copy.deepcopy(self.package)
        mutated["amendments"] = [{
            "id": "ADD-001",
            "source_clause": "Fictional Addendum 1, clause A.1",
            "requirement_ids": None,
        }]
        self.assertIn(
            "amendment ADD-001 requires requirement_ids",
            validate_bid_package(mutated),
        )

    def test_thin_claude_bridge_preserves_generic_routing_surface(self) -> None:
        root = Path(__file__).resolve().parents[1]
        claude = (root / "CLAUDE.md").read_text(encoding="utf-8")
        self.assertLessEqual(len(claude.splitlines()), 12)
        self.assertIn("@AGENTS.md", claude)
        self.assertTrue((root / "AGENTS.md").is_file())
        self.assertTrue((root / "README.md").is_file())
        self.assertTrue((root / "skills" / "SKILL.md").is_file())
        self.assertIn("skills/SKILL.md", (root / "README.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
