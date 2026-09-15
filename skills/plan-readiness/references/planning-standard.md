# Planning standard

Build an execution contract grounded in an approved specification and verified repository state.

## Preserve artifact boundaries

Include in planning:

- implementation approach within approved architecture;
- exact affected repositories, files, symbols, schemas, contracts, tests, configuration, and documentation when verifiable;
- dependency and critical-path analysis;
- phases, enablers, epics, features, tasks, gates, parallel groups, ownership, and evidence;
- test/eval, integration, migration, rollout, rollback, recovery, and operational work;
- proposed branches, worktrees, environments, delegation, monitoring, and handoffs.

Return to specification for:

- new or changed externally visible behavior;
- architecture, tenancy, data, security, AI autonomy, model-routing, or public-contract exceptions;
- missing acceptance conditions;
- requirements that are contradictory, infeasible, or unverifiable.

Do not implement, mutate, estimate false precision, or disguise specification gaps as planning decisions.

## Use evidence categories

- **Specified:** explicitly approved in the exact specification version.
- **Observed:** verified from repository, configuration, tests, runtime evidence, or authoritative documentation.
- **Reported:** provided by a human but not independently verified.
- **Proposed:** planning recommendation awaiting acceptance.
- **Assumed:** working belief with validation method and owner.

Never present an invented path, symbol, command, dependency, engineer, environment, or capacity as observed.

## Use stable identifiers

| Prefix | Meaning |
|---|---|
| `PHASE` | Dependency-bounded delivery stage |
| `EN` | Foundational enabler |
| `EP` | Epic or functionality |
| `FEAT` | Independently demonstrable feature |
| `IMPR` | Approved improvement work item |
| `BUG` | Approved defect-restoration work item |
| `TASK` | Atomic engineer-agent work packet |
| `GATE` | Evidence boundary |
| `PG` | Parallel group |
| `IMP` | Material implementation decision |

Keep identifiers stable. Retire rather than repurpose reviewed IDs.

## Layer information

- `plan.md`: master orchestration, dependency graph, critical path, phase gates, parallel lanes, capacity, integration, and approval.
- Enabler plan: foundation outcome, downstream unlocks, work packages, dependencies, and evidence.
- Epic plan: functionality boundary, feature map, shared contracts, sequencing, and integration.
- Feature plan: implementation strategy, code impact, tasks, tests/evals, and rollout.
- Task plan: self-contained execution packet for one bounded engineer-agent cycle.

Avoid copying the entire specification or parent plan into every child. Reference exact versions and IDs.

## Verify the repository baseline

Record:

- repository identity and base revision;
- relevant project instructions;
- package/dependency state;
- build, lint, test, eval, and migration commands;
- current branches or worktrees only when relevant and safe to inspect;
- code/schema/contract surfaces used by the plan.

If repository access is absent, use `PROVISIONAL — REPOSITORY VERIFICATION REQUIRED`; do not claim implementation readiness.

## Build traceability

Every mandatory specification requirement must map to:

1. at least one work item;
2. verification through a test, eval, inspection, or operational proof;
3. completion evidence;
4. release evidence when applicable.

Flag orphan work with no approved requirement and requirements with no work or verification.

## Control versions

Bind approval to plan version, specification version, parent-plan versions, and repository base revision. Reassess after material code drift. Do not invalidate a plan for unrelated commits; explain the affected surface and risk.
