---
name: plan-readiness
description: Transform an approved spec.md into a dependency-aware, implementation-ready plan through repository inspection and an adaptive planning workshop. Use when decomposing a project, feature, improvement, or bug into phases, foundation enablers, epics, features, tasks, gates, parallel workstreams, engineer-agent allocations, branches, worktrees, tests, evals, integration, rollout, and rollback. Optimize safe agentic throughput and 24/7 execution while preserving human control. Never create branches, worktrees, external tasks, code, infrastructure, migrations, deployments, or other implementation changes.
---

# Execution Planning and Readiness

Convert an approved specification into a codebase-grounded execution system. Determine what must exist first, what depends on it, what can run safely in parallel, and how engineers supervise agents. Produce planning artifacts only.

## Enforce human and mutation boundaries

- Require an approved `spec.md` and exact version. Accept missing approval metadata only when the human explicitly confirms the supplied specification is the approved baseline.
- Inspect repositories, environments, and project artifacts read-only. Do not create branches, worktrees, tasks, issues, code, migrations, infrastructure, deployments, messages, or external side effects.
- Treat the human as owner of decomposition, high-impact implementation decisions, staffing, risk acceptance, and final plan approval.
- Never mark the plan approved without explicit approval of the exact plan version, specification version, and repository base revision.
- Reset approval to `Draft` after a material change to specification, repository baseline, dependency graph, strategy, migration, security control, allocation, rollout, or rollback.
- Stop at `APPROVED — READY TO IMPLEMENT`.

## Run the planning workshop

1. **Validate entry.** Read the complete approved specification, its intent reference, parent architecture, decisions, risks, deferred items, acceptance contract, and approval evidence. Stop if approval is absent or a critical specification decision remains open.
2. **Load the standard.** Read [references/planning-standard.md](references/planning-standard.md), [references/decomposition.md](references/decomposition.md), [references/readiness-rubric.md](references/readiness-rubric.md), and the relevant mode:
   - Project/product: [references/project.md](references/project.md)
   - Feature: [references/feature.md](references/feature.md)
   - Improvement: [references/improvement.md](references/improvement.md)
   - Bug: [references/bug.md](references/bug.md)
3. **Inspect the actual system.** Read project instructions, repository structure, base revision, relevant code and symbols, schemas, contracts, dependencies, tests, CI/CD, infrastructure, security controls, deployment conventions, and previous plans. Use `rg`/`rg --files` first for local discovery. Label observed, reported, proposed, and assumed information.
4. **Check feasibility.** Identify contradictions, missing decisions, architecture exceptions, unavailable capabilities, unsafe migrations, unverifiable requirements, and code/documentation drift. Return material gaps to specification rather than silently reinterpreting them.
5. **Decompose top-down.** Convert requirements into phases, first-class foundation enablers, epics/functionality, independently demonstrable features, atomic tasks, and evidence gates. Assign stable IDs: `PHASE`, `EN`, `EP`, `FEAT`, `TASK`, `GATE`, and `PG` for parallel groups.
6. **Build the dependency graph.** Record prerequisites and outputs, detect cycles, identify the critical path, and explain why sequential work cannot move earlier. Derive phases from dependencies rather than using a fixed lifecycle.
7. **Design execution orchestration.** Read [references/parallel-execution.md](references/parallel-execution.md), [references/worktrees-and-integration.md](references/worktrees-and-integration.md), and [references/capacity-and-supervision.md](references/capacity-and-supervision.md). Classify parallelism, delegation, monitoring, execution environment, expected write set, protected surfaces, branch/worktree, integration owner, and overnight safety.
8. **Interview adaptively.** Ask one to three high-impact questions per turn only after inspection. Prioritize missing team capacity, ownership, execution environments, branch protections, review capacity, integration constraints, and risk boundaries. Present recommendations and tradeoffs; do not invent engineer availability or agent reliability.
9. **Create layered artifacts.** Select the primary `plan.md` template: [project](assets/templates/master-plan.md), [feature](assets/templates/feature-plan.md), [improvement](assets/templates/improvement-plan.md), or [bug](assets/templates/bug-plan.md). For projects, create only necessary child plans from the [enabler](assets/templates/enabler-plan.md), [epic](assets/templates/epic-plan.md), [feature](assets/templates/feature-plan.md), and [task](assets/templates/task-plan.md) templates. Require future agents to return the [execution report](assets/templates/agent-execution-report.md). Project plans orchestrate; task plans execute. Avoid duplicating parent content.
10. **Plan verification with the work.** Map every mandatory specification requirement to implementation tasks, tests/evals, completion evidence, and release evidence. Include security, tenant isolation, agent/HIL, migration, observability, compatibility, rollout, rollback, and documentation work where applicable.
11. **Model throughput.** Determine dependency-ready work, non-conflicting execution lanes, engineer supervision budget, review capacity, integration capacity, and environment/test capacity. Optimize the safe bottleneck—not raw agent count or speculative dates.
12. **Create the ready queue.** Mark a task `READY FOR AGENT` only when its dependencies, verified base, write boundary, protected files, tests/evals, stop conditions, handoff, owner, autonomy, and escalation are complete. Unattended work must meet the overnight-safety contract.
13. **Evaluate.** Apply the semantic rubric. When local files exist, run `python3 scripts/evaluate_plan.py <planning-root> --type <type>` to validate structure, identifiers, references, and dependency cycles. A structural pass does not prove feasibility or approval.
14. **Review in two checkpoints.** First obtain human agreement on phases, enablers, epics, dependency graph, and gates. Then obtain agreement on parallel lanes, engineer-agent allocation, worktree topology, supervision load, integration, and risk controls.
15. **Present the final gate.** Deliver the planning artifacts and readiness report. Ask the human to choose `Approve`, `Revise`, or `Pause`. On approval, record exact versions and stop.

## Use the planning hierarchy

| Level | Meaning |
|---|---|
| Phase | Dependency-based stage with entry and evidence-based exit gate |
| Workstream | Concurrent ownership lane, not a backlog hierarchy level |
| Enabler | Foundational capability that unlocks downstream work |
| Epic/functionality | Large coherent product or system capability |
| Feature | Independently demonstrable behavior or outcome |
| Task | Atomic engineer-agent execution unit |
| Gate | Evidence required before dependent work progresses |

Do not disguise foundations such as repository, environments, tenancy, identity, CI/CD, observability, harness, or eval infrastructure as user features.

## Produce layered outputs

```text
plan.md
plans/
├── enablers/EN-NNN-name.md
├── epics/EP-NNN-name.md
├── features/FEAT-NNN-name.md
└── tasks/TASK-NNN-name.md
```

- Use the master plan for decomposition, sequencing, critical path, parallel groups, capacity, gates, and orchestration.
- Use child plans for the detail required by their level.
- Make task files self-contained context packets for a coding agent while preserving links to specification and parent work.
- Do not create child files that add no execution value.

## Gate states

- `NOT READY`: unapproved input, critical gap, cycle, conflict, missing owner/evidence, unsafe allocation, or readiness score below threshold.
- `READY FOR HUMAN REVIEW`: plan is complete enough to approve but remains unapproved.
- `APPROVED — READY TO IMPLEMENT`: the human explicitly approves the exact plan/spec/base combination.

## Evaluate the skill

Use [evals/cases.json](evals/cases.json) and [evals/grader.md](evals/grader.md) when testing or revising this skill. Mutating the project, planning from unapproved specifications, inventing repository paths or capacity, optimizing raw agent count, allowing conflicting writers, self-approval, or crossing into implementation are automatic failures.
