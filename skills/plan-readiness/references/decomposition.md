# Dependency-aware decomposition

## Decompose in this order

1. Extract specification requirements, decisions, components, interfaces, quality gates, and risks.
2. Build a system/capability inventory before naming tasks.
3. Identify foundations that unlock several downstream capabilities.
4. Define epics/functionality and independently demonstrable features.
5. Map dependencies and outputs among enablers, epics, and features.
6. Derive phases from dependency boundaries.
7. Decompose features and enablers into atomic execution tasks.
8. Add verification, integration, rollout, recovery, documentation, and human gates.

Do not start from a generic phase template or implementation file list.

## Recognize first-class enablers

Common enablers include repository strategy, application shells, environments, CI/CD, configuration, secrets, database/migrations, tenancy, identity, authorization, design system, integration framework, agent harness, model router, knowledge/memory/files, event/scheduling, observability, test/eval infrastructure, and deployment controls.

For each enabler specify:

- outcome and approved requirements;
- dependencies and produced contracts;
- downstream work unlocked;
- work packages and parallelization;
- completion evidence and exit gate;
- owner, risk, and architecture constraints.

## Define useful levels

- **Phase:** a set of work governed by a shared entry/exit gate; not merely a time period.
- **Epic/functionality:** a coherent large capability composed of multiple features.
- **Feature:** an independently demonstrable behavior or system outcome.
- **Task:** one bounded execution packet with a single primary outcome, explicit write boundary, tests/evals, and handoff.

Allow enablers to contain tasks directly. Do not invent artificial user features beneath foundational work.

## Build the dependency graph

Record each node’s direct dependencies and outputs. Reject:

- cycles;
- hidden dependencies described only in prose;
- a task that depends on an unapproved contract;
- a phase whose entry or exit criteria cannot be observed;
- tasks labeled parallel while competing for the same mutable contract or environment.

Identify the critical path and explain why each critical dependency is sequential. Find opportunities to split contracts, fixtures, interfaces, or ownership to reduce coupling without changing the approved architecture.

## Define phase gates

Each phase requires:

- objective;
- entry criteria;
- included enablers/epics/features;
- sequential and parallel work;
- shared contracts and integration point;
- verification evidence;
- exit gate;
- human checkpoint when risk or downstream impact warrants it.

## Build atomic tasks

A task is ready only when it has:

- parent, requirements, dependencies, objective, and expected output;
- verified repository/base and relevant files or an explicit discovery subtask;
- expected write set and protected surfaces;
- implementation boundary without writing the code;
- test/eval commands and completion evidence;
- execution location, branch/worktree proposal, delegation, monitoring, owner, and stop conditions;
- risks, escalation, integration target, and handoff contract.

Split tasks when they have independent outcomes, different risk/owners, or can run safely in parallel. Keep them together when splitting would create unstable shared state or excessive integration overhead.

## Create the ready queue

Use states:

`BLOCKED → READY FOR ENGINEER → READY FOR AGENT → RUNNING → CHECKPOINT → VERIFICATION → HUMAN REVIEW → INTEGRATION READY → INTEGRATED`

Only `READY FOR AGENT` work may enter an unattended queue. Recompute readiness when dependencies, specifications, base revisions, or shared contracts change.
