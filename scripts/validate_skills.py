#!/usr/bin/env python3
"""Validate the proposal skill engine against its July 2026 local contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ACTIVE_ROOT = ROOT / "skills"
ALLOWED_FRONTMATTER = {"name", "description", "metadata"}
ALLOWED_METADATA = {"portable", "compatible_with"}
COMPATIBILITY = ["claude-code", "codex"]
ACKNOWLEDGEMENT = "Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178."
MOJIBAKE = ("Ã", "Â", "â€", "â†", "âœ", "ðŸ", "\ufffd")
SECTION_ALIASES = {
    "Use When": ("Use When",),
    "Do Not Use When": ("Do Not Use When",),
    "Inputs": ("Inputs", "Required Inputs"),
    "Outputs": ("Outputs",),
    "Evidence Produced": ("Evidence Produced",),
    "Capability Contract": ("Capability Contract", "Capability and Permission Boundaries"),
    "Degraded Mode": ("Degraded Mode",),
    "Decision Rules": ("Decision Rules",),
    "Workflow": ("Workflow",),
    "Quality Standards": ("Quality Standards",),
    "Anti-Patterns": ("Anti-Patterns", "Domain Anti-Patterns"),
    "References": ("References",),
}
MANDATORY_RESOURCES = (
    "skills/SKILL.md",
    "skills/profiles-sectors/profiles/SKILL.md",
    "skills/profiles-sectors/sectors/SKILL.md",
    "skills/strategy-positioning/critical-analysis-business-logic/SKILL.md",
    "skills/meta/anti-ai-slop/SKILL.md",
    "skills/meta/ai-slop-audit/SKILL.md",
    "docs/skill-authoring-standard.md",
    "templates/skill-template.md",
    "tests/fixtures/routing-fixtures.json",
)
FRONTMATTER_RE = re.compile(r"^\ufeff?---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)
HEADING_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--active-root", default="skills")
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--details", action="store_true")
    return parser.parse_args()


def section(body: str, heading: str) -> str | None:
    match = re.search(
        rf"^##\s+{re.escape(heading)}\s*$\r?\n([\s\S]*?)(?=^##\s+|\Z)",
        body,
        re.MULTILINE | re.IGNORECASE,
    )
    return match.group(1).strip() if match else None


def aliased_section(body: str, aliases: tuple[str, ...]) -> str | None:
    parts = [value for alias in aliases if (value := section(body, alias))]
    return "\n".join(parts) if parts else None


def parse_skill(path: Path) -> tuple[dict, str, list[str]]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    match = FRONTMATTER_RE.match(raw)
    if not match:
        return {}, raw, ["frontmatter"]
    try:
        frontmatter = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}, raw[match.end() :], ["frontmatter_yaml"]
    if not isinstance(frontmatter, dict):
        return {}, raw[match.end() :], ["frontmatter_type"]
    return frontmatter, raw[match.end() :], []


def table_headers(text: str | None) -> set[str]:
    if not text:
        return set()
    for line in text.splitlines():
        if line.strip().startswith("|"):
            headers = set()
            for cell in line.strip().strip("|").split("|"):
                normalised = re.sub(r"[^a-z0-9]+", "_", cell.strip().lower()).strip("_")
                normalised = normalised.replace("artifact", "artefact").replace("behavior", "behaviour")
                headers.add(normalised)
            return headers
    return set()


def local_links(path: Path, body: str, root: Path) -> list[str]:
    broken: list[str] = []
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
        clean = target.split("#", 1)[0].strip()
        if not clean or "://" in clean or clean.startswith(("#", "mailto:")):
            continue
        if clean.startswith("/") and clean.endswith("/") and not re.match(r"^/[A-Za-z]:/", clean):
            continue
        if clean.startswith("/") and re.match(r"^/[A-Za-z]:/", clean):
            candidate = Path(clean[1:])
        elif clean.startswith("/"):
            candidate = root / clean.lstrip("/")
        else:
            candidate = path.parent / clean
        if not candidate.resolve().exists():
            broken.append(target)
    return broken


def assess(path: Path, root: Path) -> dict:
    raw = path.read_text(encoding="utf-8", errors="replace")
    frontmatter, body, failures = parse_skill(path)
    name = frontmatter.get("name")
    description = frontmatter.get("description")
    metadata = frontmatter.get("metadata")
    metadata = metadata if isinstance(metadata, dict) else {}

    if set(frontmatter) - ALLOWED_FRONTMATTER:
        failures.append("unsupported_frontmatter")
    if set(metadata) - ALLOWED_METADATA:
        failures.append("unsupported_metadata")
    if name != path.parent.name:
        failures.append("name_mismatch")
    if not isinstance(description, str) or not description.startswith("Use when"):
        failures.append("description_trigger")
    elif len(description) > 350 or len(description) < 45 or "\n" in description:
        failures.append("description_quality")
    if metadata.get("portable") is not True or metadata.get("compatible_with") != COMPATIBILITY:
        failures.append("portable_metadata")

    title = re.search(r"^#\s+.+$", body, re.MULTILINE)
    if not title:
        failures.append("title")
    else:
        tail = body[title.end() :].lstrip("\r\n").splitlines()
        if not tail or tail[0].strip() != ACKNOWLEDGEMENT:
            failures.append("acknowledgement")

    sections = {heading: aliased_section(body, aliases) for heading, aliases in SECTION_ALIASES.items()}
    for heading, content in sections.items():
        if not content:
            failures.append("missing_" + heading.lower().replace(" ", "_"))

    inputs = sections["Inputs"]
    input_headers = table_headers(inputs)
    if not (
        any("artefact" in item for item in input_headers)
        and any("source" in item or "provider" in item for item in input_headers)
        and any("required" in item for item in input_headers)
        and any(("missing" in item and "behaviour" in item) or "absent" in item for item in input_headers)
    ):
        failures.append("input_contract")
    outputs = sections["Outputs"]
    output_headers = table_headers(outputs)
    if not (
        any("artefact" in item for item in output_headers)
        and any("consumer" in item for item in output_headers)
        and any("acceptance" in item for item in output_headers)
    ):
        failures.append("output_contract")
    evidence = sections["Evidence Produced"]
    evidence_headers = table_headers(evidence)
    if not (
        any("evidence" in item for item in evidence_headers)
        and any("consumer" in item for item in evidence_headers)
        and any("acceptance" in item for item in evidence_headers)
    ):
        failures.append("evidence_contract")

    capability = sections["Capability Contract"] or ""
    if not re.search(r"\b(read|search)\b", capability, re.IGNORECASE) or not re.search(
        r"authori[sz]|permission|read-only|mutation|edit", capability, re.IGNORECASE
    ):
        failures.append("capability_boundary")
    audit_like = bool(
        re.search(r"(?:^|-)(?:audit|review|critique|analysis)(?:-|$)", str(name), re.IGNORECASE)
        or re.match(r"Use when (?:auditing|reviewing|critiquing|analysing)", str(description), re.IGNORECASE)
    )
    if audit_like and "read-only" not in capability.lower():
        failures.append("audit_read_only")

    degraded = sections["Degraded Mode"] or ""
    if not re.search(r"unavailable|missing|cannot|without", degraded, re.IGNORECASE) or not re.search(
        r"qualif|unassessed|not assessed|narrow|gap|do not", degraded, re.IGNORECASE
    ):
        failures.append("degraded_contract")

    decision = sections["Decision Rules"]
    decision_headers = table_headers(decision)
    if not any("action" in item or "choice" in item for item in decision_headers) or not any(
        "risk" in item or "failure" in item for item in decision_headers
    ):
        failures.append("decision_contract")

    workflow = sections["Workflow"] or ""
    if len(re.findall(r"^\s*\d+\.\s+", workflow, re.MULTILINE)) < 3:
        failures.append("workflow_order")
    if not re.search(r"stop|block|do not proceed", workflow, re.IGNORECASE):
        failures.append("workflow_stop")
    if not re.search(r"recover|revise|retry|fallback|correct|return", workflow, re.IGNORECASE):
        failures.append("workflow_recovery")

    anti = sections["Anti-Patterns"] or ""
    items = re.findall(r"^\s*[-*]\s+(.+)$|^\s*\d+\.\s+(.+)$", anti, re.MULTILINE)
    flattened = [left or right for left, right in items]
    if len(flattened) < 5 or sum("fix:" in item.lower() for item in flattened) < 5:
        failures.append("anti_patterns")

    references = sections["References"] or ""
    if not re.search(r"\[[^\]]+\]\([^)]+\)", references):
        failures.append("direct_references")
    if re.search(r"^\s*-\s+.*`[^`]+\.md(?:#[^`]*)?`", references, re.IGNORECASE | re.MULTILINE):
        failures.append("unlinked_references")
    broken = local_links(path, body, root)
    if broken:
        failures.append("broken_links")

    if len(raw.splitlines()) > 500:
        failures.append("line_limit")
    if any(marker in raw for marker in MOJIBAKE):
        failures.append("encoding_noise")
    if re.search(r"\b(mcp__\w+|functions\.exec|tool_search|spawn_agent)\b", body):
        failures.append("runner_specific_instruction")

    return {
        "path": path.relative_to(root).as_posix(),
        "failed": sorted(set(failures)),
        "broken_links": broken,
        "lines": len(raw.splitlines()),
    }


def validate_references(skill_paths: list[Path], root: Path) -> list[dict]:
    findings: list[dict] = []
    for skill in skill_paths:
        for reference in sorted((skill.parent / "references").glob("*.md")) if (skill.parent / "references").exists() else []:
            text = reference.read_text(encoding="utf-8", errors="replace")
            failed: list[str] = []
            if not re.search(r"\[[^\]]+\]\(\.\./SKILL\.md(?:#[^)]+)?\)", text[:1200], re.IGNORECASE):
                failed.append("reference_backlink")
            broken = local_links(reference, text, root)
            if broken:
                failed.append("broken_links")
            if any(marker in text for marker in MOJIBAKE):
                failed.append("encoding_noise")
            if failed:
                findings.append({"path": reference.relative_to(root).as_posix(), "failed": failed, "broken_links": broken})
    return findings


def main() -> int:
    args = arguments()
    root = args.root.resolve()
    active_root = (root / args.active_root).resolve()
    skills = sorted(active_root.rglob("SKILL.md"))
    results = [assess(path, root) for path in skills]
    reference_results = validate_references(skills, root)
    missing_resources = [item for item in MANDATORY_RESOURCES if not (root / item).exists()]

    names: defaultdict[str, list[str]] = defaultdict(list)
    descriptions: defaultdict[str, list[str]] = defaultdict(list)
    for path in skills:
        fm, _, _ = parse_skill(path)
        names[str(fm.get("name", ""))].append(path.relative_to(root).as_posix())
        descriptions[str(fm.get("description", ""))].append(path.relative_to(root).as_posix())
    duplicate_names = {key: value for key, value in names.items() if key and len(value) > 1}
    duplicate_descriptions = {key: value for key, value in descriptions.items() if key and len(value) > 1}

    counts: Counter[str] = Counter()
    for result in results + reference_results:
        counts.update(result["failed"])
    if duplicate_names:
        counts["duplicate_names"] += len(duplicate_names)
    if duplicate_descriptions:
        counts["duplicate_descriptions"] += len(duplicate_descriptions)
    if missing_resources:
        counts["missing_mandatory_resources"] += len(missing_resources)

    payload = {
        "schema_version": 1,
        "root": str(root),
        "active_root": args.active_root,
        "active_skill_count": len(skills),
        "failure_counts": dict(sorted(counts.items())),
        "missing_mandatory_resources": missing_resources,
        "duplicate_names": duplicate_names,
        "duplicate_descriptions": duplicate_descriptions,
        "results": results + reference_results,
    }

    baseline_errors: list[str] = []
    if args.baseline:
        baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
        fixture_file = root / "tests" / "fixtures" / "routing-fixtures.json"
        fixture_count = len(json.loads(fixture_file.read_text(encoding="utf-8")).get("fixtures", []))
        if baseline.get("expected_active_skill_count") != len(skills):
            baseline_errors.append("active skill count differs from baseline")
        if baseline.get("failure_counts") != {}:
            baseline_errors.append("baseline must contain zero failure counts")
        if baseline.get("failure_counts", {}) != payload["failure_counts"]:
            baseline_errors.append("failure counts differ from zero-debt baseline")
        if baseline.get("routing_fixture_count") != fixture_count:
            baseline_errors.append("routing fixture count differs from baseline")

    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(f"proposal-skill-validator: {root}")
        print(f"- active skills: {len(skills)}")
        print(f"- findings: {sum(counts.values())}")
        for key, value in sorted(counts.items()):
            print(f"  - {key}: {value}")
        if args.details:
            for result in results + reference_results:
                if result["failed"]:
                    print(f"- {result['path']}: {', '.join(result['failed'])}")
        for error in baseline_errors:
            print(f"- baseline: {error}")

    return 1 if counts or baseline_errors else 0


if __name__ == "__main__":
    sys.exit(main())
