#!/usr/bin/env python3
"""Validate structural and dependency invariants in planning artifacts.

This cannot verify feasibility, capacity truth, code correctness, or human approval.
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path


HEADINGS = {
    "project": [
        "Planning Objective", "Approved Inputs and Baseline", "System Decomposition",
        "Foundation and Enabler Register", "Epic and Feature Map",
        "Dependency Graph and Critical Path", "Phase Plan and Gates",
        "Parallel Workstreams", "Engineer and Agent Capacity", "Execution Orchestration",
        "Integration and Assembly", "Quality and Evidence",
        "Environments, Rollout, and Recovery", "Risks, Assumptions, and Blockers",
        "Requirement Traceability", "Ready Queue", "Human Checkpoints", "Human Approval",
    ],
    "feature": [
        "Outcome and Scope", "Current-System Findings", "Implementation Strategy",
        "Change-Impact Map", "Task Map and Dependencies",
        "Data, API, Event, and Integration Work",
        "Security, Permissions, and Tenant Isolation",
        "Agent, Harness, LLM, Tool, Memory, and HIL Work", "UI and Experience Work",
        "Tests, Evals, and Evidence", "Integration, Rollout, and Rollback",
        "Risks, Assumptions, and Human Checkpoints", "Human Checkpoints",
        "Completion Gate", "Human Approval",
    ],
    "improvement": [
        "Planning Objective", "Approved Inputs and Baseline", "Current-System Findings",
        "Measurement and Benchmark Foundation", "Implementation Strategy and Experiments",
        "Dependency Graph and Task Plan", "Parallel Execution and Capacity",
        "Invariants and Regression Protection", "Tests, Evals, and Acceptance Evidence",
        "Integration, Rollout, and Rollback", "Risks, Assumptions, and Blockers",
        "Requirement Traceability", "Human Checkpoints", "Human Approval",
    ],
    "bug": [
        "Planning Objective", "Approved Inputs and Evidence", "Reproduction and Containment",
        "Root-Cause Verification", "Current-System and Impact Findings", "Correction Strategy",
        "Dependency Graph and Task Plan", "Parallel Execution and Capacity",
        "Data Repair and External Effects", "Tests, Evals, and Regression Evidence",
        "Integration, Rollout, and Recovery", "Risks, Assumptions, and Blockers",
        "Requirement Traceability", "Human Checkpoints", "Human Approval",
    ],
}

REQUIRED_FAMILIES = {
    "project": {"PHASE", "EN", "EP", "FEAT", "TASK", "GATE"},
    "feature": {"FEAT", "TASK"},
    "improvement": {"IMPR", "TASK"},
    "bug": {"BUG", "TASK"},
}

TASK_FIELDS = [
    "ID", "Status", "Parent", "Requirements", "Depends on", "Parallel group",
    "Parallelization class",
    "Primary engineer", "Agent role/runtime", "Agent collaboration pattern",
    "Agent execution size", "Expected agent cycles", "Execution location", "Repository",
    "Base revision", "Branch", "Worktree", "Expected write set",
    "Protected files/surfaces", "Shared contracts", "Delegation level",
    "Monitoring level", "Supervision units", "Overnight-safe",
    "Integration target/owner", "Human checkpoint",
]

TASK_HEADINGS = [
    "Objective", "Execution Context", "Implementation Boundary", "Planned Steps",
    "Tests and Evals", "Completion Evidence", "Stop Conditions",
    "Risks and Escalation", "Required Handoff",
]

WORK_ID = r"(?:PHASE|EN|EP|FEAT|IMPR|BUG|TASK|GATE)-\d{3}"
WORK_ID_RE = re.compile(rf"\b({WORK_ID})\b")
PLACEHOLDERS = [r"\[[^\]\n]+\](?!\()", r"\bTBD\b", r"\bTODO\b", r"\bFIXME\b", r"<[^>]+>"]


def parse_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, re.M))
    result: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result[match.group(1).strip()] = text[match.end():end].strip()
    return result


def field(text: str, name: str) -> str:
    match = re.search(rf"^{re.escape(name)}:\s*(.*?)\s*$", text, re.I | re.M)
    return match.group(1).strip() if match else ""


def substantive(value: str) -> bool:
    return bool(value) and not any(re.search(pattern, value, re.I) for pattern in PLACEHOLDERS)


def detect_type(text: str) -> str | None:
    value = field(text, "Type").lower()
    if value == "product":
        return "project"
    return value if value in HEADINGS else None


def collect_files(target: Path) -> tuple[Path, list[Path]]:
    if target.is_file():
        return target, [target]
    master = target / "plan.md"
    if not master.exists():
        raise FileNotFoundError(f"Missing master plan: {master}")
    children = sorted((target / "plans").rglob("*.md")) if (target / "plans").exists() else []
    return master, [master, *children]


def extract_definitions(path: Path, text: str) -> list[str]:
    definitions = []
    direct_id = field(text, "ID")
    if re.fullmatch(WORK_ID, direct_id):
        definitions.append(direct_id)
    definitions.extend(re.findall(rf"^###\s+({WORK_ID})\b", text, re.M))
    return definitions


def parse_dependencies(text: str) -> list[str]:
    value = field(text, "Depends on")
    if not value or value.lower() == "none":
        return []
    return WORK_ID_RE.findall(value)


def find_cycles(graph: dict[str, list[str]]) -> list[list[str]]:
    cycles: list[list[str]] = []
    visiting: list[str] = []
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visiting:
            start = visiting.index(node)
            cycle = visiting[start:] + [node]
            if cycle not in cycles:
                cycles.append(cycle)
            return
        if node in visited:
            return
        visiting.append(node)
        for dependency in graph.get(node, []):
            if dependency in graph:
                visit(dependency)
        visiting.pop()
        visited.add(node)

    for node in graph:
        visit(node)
    return cycles


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("planning_root", type=Path)
    parser.add_argument("--type", choices=sorted(HEADINGS))
    args = parser.parse_args()

    try:
        master, paths = collect_files(args.planning_root)
    except FileNotFoundError as error:
        print(json.dumps({"error": str(error)}, indent=2))
        return 2

    texts = {path: path.read_text(encoding="utf-8") for path in paths}
    master_text = texts[master]
    work_type = args.type or detect_type(master_text)
    if not work_type:
        print(json.dumps({"error": "Could not detect plan type; pass --type."}, indent=2))
        return 2

    master_sections = parse_sections(master_text)
    missing_headings = [heading for heading in HEADINGS[work_type] if heading not in master_sections]
    empty_headings = [heading for heading in HEADINGS[work_type] if heading in master_sections and not master_sections[heading].strip()]

    unresolved = []
    definitions_by_id: dict[str, list[str]] = collections.defaultdict(list)
    graph: dict[str, list[str]] = {}
    task_issues: dict[str, list[str]] = {}
    task_parent_refs: set[str] = set()
    ready_worktrees: dict[str, list[str]] = collections.defaultdict(list)
    ready_write_sets: dict[tuple[str, str], list[str]] = collections.defaultdict(list)

    for path, text in texts.items():
        for number, line in enumerate(text.splitlines(), start=1):
            if any(re.search(pattern, line, re.I) for pattern in PLACEHOLDERS):
                unresolved.append({"file": str(path), "line": number, "text": line.strip()[:160]})
        definitions = extract_definitions(path, text)
        for identifier in definitions:
            definitions_by_id[identifier].append(str(path))
        direct_id = field(text, "ID")
        if re.fullmatch(WORK_ID, direct_id):
            graph[direct_id] = parse_dependencies(text)
        if direct_id.startswith("TASK-"):
            issues = []
            for name in TASK_FIELDS:
                if not substantive(field(text, name)):
                    issues.append(f"missing or provisional field: {name}")
            task_status = field(text, "Status").upper()
            execution_location = field(text, "Execution location")
            parallel_class = field(text, "Parallelization class")
            collaboration_pattern = field(text, "Agent collaboration pattern")
            execution_size = field(text, "Agent execution size")
            delegation = field(text, "Delegation level").upper()
            monitoring = field(text, "Monitoring level").upper()
            overnight = field(text, "Overnight-safe").lower()
            if task_status not in {"BLOCKED", "READY FOR ENGINEER", "READY FOR AGENT"}:
                issues.append("invalid or multiple-choice field: Status")
            if execution_location not in {"Local", "Cloud", "Sandbox"}:
                issues.append("invalid or multiple-choice field: Execution location")
            if parallel_class not in {
                "Sequential", "Parallel-independent", "Parallel-partitioned",
                "Parallel-coordinated", "Integration-bound", "Human-blocked",
                "Environment-blocked", "Unsafe-to-parallelize",
            }:
                issues.append("invalid or multiple-choice field: Parallelization class")
            if collaboration_pattern not in {
                "Independent builder", "Builder-verifier", "Researcher-builder-verifier",
                "Contract-first", "Sequential high-risk",
            }:
                issues.append("invalid or multiple-choice field: Agent collaboration pattern")
            if execution_size not in {"Small", "Medium", "Large"}:
                issues.append("invalid or multiple-choice field: Agent execution size")
            if not re.fullmatch(r"D[0-5]", delegation):
                issues.append("invalid or multiple-choice field: Delegation level")
            if not re.fullmatch(r"M[0-4]", monitoring):
                issues.append("invalid or multiple-choice field: Monitoring level")
            if overnight not in {"yes", "no"}:
                issues.append("invalid or multiple-choice field: Overnight-safe")
            if task_status == "READY FOR AGENT" and delegation in {"D0", "D5"}:
                issues.append("READY FOR AGENT conflicts with delegation level")
            if overnight == "yes" and delegation not in {"D3", "D4"}:
                issues.append("overnight-safe work requires D3 or D4 delegation")
            if overnight == "yes" and monitoring not in {"M0", "M1"}:
                issues.append("overnight-safe work requires M0 or M1 monitoring")
            task_sections = parse_sections(text)
            for heading in TASK_HEADINGS:
                if heading not in task_sections or not task_sections[heading].strip():
                    issues.append(f"missing or empty heading: {heading}")
            task_issues[direct_id] = issues
            parent_value = field(text, "Parent")
            parent_match = WORK_ID_RE.search(parent_value)
            if parent_match:
                task_parent_refs.add(parent_match.group(1))
            else:
                issues.append("missing valid Parent work ID")
            if task_status == "READY FOR AGENT" and substantive(field(text, "Worktree")):
                ready_worktrees[field(text, "Worktree")].append(direct_id)
            if task_status == "READY FOR AGENT":
                pg = field(text, "Parallel group")
                write_set = field(text, "Expected write set").lower()
                if substantive(pg) and pg.lower() != "none" and substantive(write_set):
                    ready_write_sets[(pg, write_set)].append(direct_id)

    duplicate_ids = {identifier: files for identifier, files in definitions_by_id.items() if len(files) > 1}
    defined = set(definitions_by_id)
    referenced_dependencies = {dependency for deps in graph.values() for dependency in deps}
    missing_dependencies = sorted(referenced_dependencies - defined)
    missing_task_parents = sorted(task_parent_refs - defined)
    cycles = find_cycles(graph)
    worktree_collisions = {name: ids for name, ids in ready_worktrees.items() if len(ids) > 1}
    write_set_collisions = {
        f"{pg}::{write_set}": ids
        for (pg, write_set), ids in ready_write_sets.items()
        if len(ids) > 1
    }
    all_work_ids = {identifier for text in texts.values() for identifier in WORK_ID_RE.findall(text)}
    present_families = {identifier.split("-", 1)[0] for identifier in all_work_ids}
    missing_families = sorted(REQUIRED_FAMILIES[work_type] - present_families)

    metadata = {
        name: field(master_text, name)
        for name in ("Specification", "Specification version", "Base revision")
    }
    missing_metadata = [name for name, value in metadata.items() if not substantive(value)]
    approval = master_sections.get("Human Approval", "")
    decision_approved = bool(re.search(r"Decision:\s*Approved\b", approval, re.I))
    evidence_match = re.search(r"^\s*-?\s*Approval evidence:\s*(.*?)\s*$", approval, re.I | re.M)
    evidence = evidence_match.group(1).strip() if evidence_match else ""
    approval_recorded = decision_approved and substantive(evidence) and evidence.lower() != "pending"

    blocking_task_issues = {identifier: issues for identifier, issues in task_issues.items() if issues}
    task_plan_count = len(task_issues)
    missing_task_plans = task_plan_count == 0
    heading_coverage = round(100 * (len(HEADINGS[work_type]) - len(set(missing_headings + empty_headings))) / len(HEADINGS[work_type]))
    structurally_complete = not any([
        missing_headings, empty_headings, unresolved, duplicate_ids, missing_dependencies,
        cycles, worktree_collisions, write_set_collisions, missing_families,
        missing_metadata, missing_task_parents, missing_task_plans,
        blocking_task_issues,
    ])

    result = {
        "type": work_type,
        "files_checked": len(paths),
        "heading_coverage": heading_coverage,
        "structurally_complete": structurally_complete,
        "missing_headings": missing_headings,
        "empty_headings": empty_headings,
        "unresolved_markers": unresolved,
        "duplicate_ids": duplicate_ids,
        "missing_dependencies": missing_dependencies,
        "missing_task_parents": missing_task_parents,
        "dependency_cycles": cycles,
        "ready_worktree_collisions": worktree_collisions,
        "ready_write_set_collisions": write_set_collisions,
        "missing_required_work_families": missing_families,
        "missing_baseline_metadata": missing_metadata,
        "task_issues": blocking_task_issues,
        "task_plan_count": task_plan_count,
        "missing_task_plans": missing_task_plans,
        "human_approval_recorded": approval_recorded,
        "ready_to_implement": False,
        "note": "Semantic review, repository truth, safe capacity, and explicit human approval of the exact plan/spec/base remain required.",
    }
    print(json.dumps(result, indent=2))
    return 0 if structurally_complete else 1


if __name__ == "__main__":
    sys.exit(main())
