#!/usr/bin/env python3
"""Perform deterministic structural checks on an intent.md.

This complements, but never replaces, semantic review or human approval.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED = {
    "project": [
        "Purpose and Trigger",
        "Target Users and Stakeholders",
        "Current State and Evidence",
        "Desired Outcome",
        "Scope",
        "Non-Goals and Must Remain Unchanged",
        "Success Measures",
        "Constraints and Guardrails",
        "Dependencies",
        "Assumptions",
        "Risks and Failure Consequences",
        "Open Questions",
        "Human Approval",
    ],
    "feature": [
        "Context and Evidence",
        "User Need and Affected Roles",
        "Current State",
        "Desired Outcome",
        "Expected Behavior",
        "Key Scenarios",
        "Scope",
        "Non-Goals and Must Remain Unchanged",
        "Acceptance",
        "Constraints and Guardrails",
        "Dependencies and Assumptions",
        "Open Questions",
        "Human Approval",
    ],
    "improvement": [
        "Context and Evidence",
        "Affected Users or System Area",
        "Current Experience and Baseline",
        "Problem or Limitation",
        "Desired Improvement",
        "Scope",
        "Non-Goals and Must Remain Unchanged",
        "Success and Acceptance",
        "Regression Boundary",
        "Constraints and Guardrails",
        "Dependencies and Assumptions",
        "Open Questions",
        "Human Approval",
    ],
    "bug": [
        "Problem and Impact",
        "Observed Behavior",
        "Expected Behavior",
        "Reproduction",
        "Environment",
        "Evidence",
        "Workaround and Risk",
        "Scope and Must Remain Unchanged",
        "Acceptance and Regression Boundary",
        "Constraints, Dependencies, and Assumptions",
        "Open Questions",
        "Human Approval",
    ],
}

PLACEHOLDER_PATTERNS = [
    r"\[[^\]]+\]",
    r"\bTBD\b",
    r"\bTODO\b",
    r"\bFIXME\b",
    r"<[^>]+>",
]


def parse_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.MULTILINE))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[match.group(1).strip()] = text[start:end].strip()
    return sections


def detect_type(text: str) -> str | None:
    match = re.search(r"^Type:\s*(Project|Product|Feature|Improvement|Bug)\s*$", text, re.I | re.M)
    if not match:
        return None
    value = match.group(1).lower()
    return "project" if value == "product" else value


def meaningful(content: str) -> bool:
    if not content:
        return False
    stripped = re.sub(r"[-*#:\s]", "", content)
    if not stripped:
        return False
    return not any(re.fullmatch(pattern, content.strip(), re.I | re.S) for pattern in PLACEHOLDER_PATTERNS)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--type", choices=sorted(REQUIRED))
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    work_type = args.type or detect_type(text)
    if not work_type:
        print(json.dumps({"error": "Could not detect intent type; pass --type."}, indent=2))
        return 2

    sections = parse_sections(text)
    required = REQUIRED[work_type]
    missing = [heading for heading in required if heading not in sections]
    empty = [heading for heading in required if heading in sections and not meaningful(sections[heading])]

    unresolved = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if any(re.search(pattern, line, re.I) for pattern in PLACEHOLDER_PATTERNS):
            unresolved.append({"line": line_number, "text": line.strip()[:160]})

    approval = sections.get("Human Approval", "")
    approval_pending = not bool(re.search(r"Decision:\s*Approved\b", approval, re.I))
    completed = len(required) - len(set(missing + empty))
    coverage = round(100 * completed / len(required))

    structurally_complete = not missing and not empty and not unresolved
    result = {
        "type": work_type,
        "structural_coverage": coverage,
        "structurally_complete": structurally_complete,
        "missing_sections": missing,
        "empty_sections": empty,
        "unresolved_markers": unresolved,
        "human_approval_pending": approval_pending,
        "ready_for_spec": False,
        "note": "Semantic rubric and explicit human approval are still required.",
    }
    print(json.dumps(result, indent=2))
    return 0 if structurally_complete else 1


if __name__ == "__main__":
    sys.exit(main())
