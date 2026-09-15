#!/usr/bin/env python3
"""Run deterministic structural checks on a spec.md.

This cannot verify truth, feasibility, semantic quality, or human approval.
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = {
    "project": [
        "Intent Traceability",
        "System Context",
        "Actors, Roles, and Permissions",
        "Capabilities and Workflows",
        "Functional and Business Requirements",
        "Architecture Overview",
        "Tenancy and Isolation Model",
        "Technology Stack",
        "Application and Service Architecture",
        "Data and Storage Architecture",
        "Identity, Access, and Authorization",
        "Integrations and Tools",
        "Agent Architecture",
        "Agent Harness and Orchestration",
        "LLM and Model Strategy",
        "LLM Router",
        "Knowledge, Context, Memory, and Files",
        "Human-in-the-Loop Controls",
        "Security, Privacy, and Compliance",
        "Infrastructure and Deployment",
        "Scalability, Reliability, Performance, and Cost",
        "Observability and Operations",
        "AI Evals and Quality Assurance",
        "Compatibility, Migration, Rollout, and Rollback",
        "Acceptance Scenarios",
        "Decision Register",
        "Constraints, Dependencies, Assumptions, and Risks",
        "Requirement Traceability",
        "Open Decisions",
        "Human Approval",
    ],
    "feature": [
        "Intent Traceability",
        "Parent Architecture and Inherited Decisions",
        "Actors, Roles, and Permissions",
        "Workflows, States, Errors, and Recovery",
        "Functional Requirements",
        "Business Rules",
        "Data Requirements",
        "Interfaces and Integrations",
        "Architecture and Technology Impact",
        "Agent, Model, Tool, Memory, and HIL Impact",
        "Security, Privacy, and Compliance",
        "Non-Functional and Operational Requirements",
        "Rollout, Migration, and Rollback",
        "Acceptance Scenarios and Evals",
        "Decision Register",
        "Constraints, Dependencies, Assumptions, and Risks",
        "Requirement Traceability",
        "Open Decisions",
        "Human Approval",
    ],
    "improvement": [
        "Intent Traceability",
        "Parent Architecture and Inherited Decisions",
        "Verified Current Behavior and Baseline",
        "Desired Delta and Invariants",
        "Architecture and Technology Impact",
        "Data, Integration, Security, and AI Impact",
        "Performance, Reliability, Scale, and Cost",
        "Regression Boundary",
        "Measurement, Observability, and Comparison",
        "Rollout and Rollback",
        "Acceptance Scenarios and Evals",
        "Decision Register",
        "Constraints, Dependencies, Assumptions, and Risks",
        "Requirement Traceability",
        "Open Decisions",
        "Human Approval",
    ],
    "bug": [
        "Intent Traceability",
        "Parent Architecture and Inherited Decisions",
        "Verified Evidence and Affected Conditions",
        "Expected and Restored Behavior",
        "Cause Status and Investigation Boundary",
        "Containment, Data Repair, and Customer Safety",
        "Architecture and Technology Impact",
        "Data, Integration, Security, and AI Impact",
        "Failure, Recovery, and Compatibility",
        "Observability and Detection",
        "Rollout, Remediation, and Rollback",
        "Acceptance and Regression Scenarios",
        "Decision Register",
        "Constraints, Dependencies, Assumptions, and Risks",
        "Requirement Traceability",
        "Open Decisions",
        "Human Approval",
    ],
}

REQUIRED_FAMILIES = {
    "project": {"FR", "AC", "DEC"},
    "feature": {"FR", "AC"},
    "improvement": {"FR", "NFR", "AC"},
    "bug": {"FR", "AC"},
}

PLACEHOLDERS = [r"\[[^\]\n]+\](?!\()", r"\bTBD\b", r"\bTODO\b", r"\bFIXME\b", r"<[^>]+>"]
ID_PATTERN = re.compile(r"\b(FR|BR|DR|IR|SEC|NFR|AI|OBS|AC|DEC)-(\d{3})\b")
DEFINITION_PATTERN = re.compile(r"^\s*-\s*`?((?:FR|BR|DR|IR|SEC|NFR|AI|OBS|AC)-\d{3})`?\s*(?::|verifies\b)", re.M)
DECISION_ROW_PATTERN = re.compile(r"^\|\s*`?(DEC-\d{3})`?\s*\|", re.M)


def sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.M))
    result: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result[match.group(1).strip()] = text[match.end():end].strip()
    return result


def detect_type(text: str) -> str | None:
    match = re.search(r"^Type:\s*(Project|Product|Feature|Improvement|Bug)\s*$", text, re.I | re.M)
    if not match:
        return None
    value = match.group(1).lower()
    return "project" if value == "product" else value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--type", choices=sorted(REQUIRED_HEADINGS))
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    work_type = args.type or detect_type(text)
    if not work_type:
        print(json.dumps({"error": "Could not detect specification type; pass --type."}, indent=2))
        return 2

    parsed = sections(text)
    required = REQUIRED_HEADINGS[work_type]
    missing_headings = [heading for heading in required if heading not in parsed]
    empty_headings = [heading for heading in required if heading in parsed and not parsed[heading].strip()]

    unresolved = []
    for number, line in enumerate(text.splitlines(), start=1):
        if any(re.search(pattern, line, re.I) for pattern in PLACEHOLDERS):
            unresolved.append({"line": number, "text": line.strip()[:160]})

    definitions = DEFINITION_PATTERN.findall(text) + DECISION_ROW_PATTERN.findall(text)
    counts = collections.Counter(definitions)
    duplicate_definitions = sorted(identifier for identifier, count in counts.items() if count > 1)
    present_families = {match.group(1) for match in ID_PATTERN.finditer(text)}
    missing_families = sorted(REQUIRED_FAMILIES[work_type] - present_families)

    intent_match = re.search(r"^Intent:\s*(.+?)\s*$", text, re.I | re.M)
    intent_reference_present = bool(intent_match and not any(re.search(p, intent_match.group(1), re.I) for p in PLACEHOLDERS))
    approval = parsed.get("Human Approval", "")
    decision_approved = bool(re.search(r"Decision:\s*Approved\b", approval, re.I))
    evidence_match = re.search(r"^\s*-?\s*Approval evidence:\s*(.*?)\s*$", approval, re.I | re.M)
    evidence_value = evidence_match.group(1).strip() if evidence_match else ""
    approval_evidence_pending = not evidence_value or evidence_value.lower() == "pending"
    approval_recorded = decision_approved and not approval_evidence_pending

    complete_headings = len(required) - len(set(missing_headings + empty_headings))
    coverage = round(100 * complete_headings / len(required))
    structurally_complete = not any(
        [missing_headings, empty_headings, unresolved, duplicate_definitions, missing_families]
    ) and intent_reference_present

    result = {
        "type": work_type,
        "heading_coverage": coverage,
        "structurally_complete": structurally_complete,
        "missing_headings": missing_headings,
        "empty_headings": empty_headings,
        "unresolved_markers": unresolved,
        "duplicate_definitions": duplicate_definitions,
        "missing_required_identifier_families": missing_families,
        "intent_reference_present": intent_reference_present,
        "human_approval_recorded": approval_recorded,
        "approval_evidence_pending": approval_evidence_pending,
        "ready_for_plan": False,
        "note": "Semantic review, source verification, feasibility, and explicit human approval of the exact version remain required.",
    }
    print(json.dumps(result, indent=2))
    return 0 if structurally_complete else 1


if __name__ == "__main__":
    sys.exit(main())
