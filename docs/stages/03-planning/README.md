# Stage 3 — Execution Planning

## Purpose

Transform an approved specification into a repository-grounded execution system: what must exist first, what unlocks what, what can run in parallel, how work is packaged for engineers and agents, and what evidence permits progress.

## Entry

- The exact `spec.md` version is explicitly approved.
- The repository or system baseline can be inspected and identified.
- Critical behavior, architecture, tenancy, security, data, interface, AI-autonomy, and acceptance choices are not left for the implementer to guess.

## Planning hierarchy

| Level | Meaning |
|---|---|
| Phase | Dependency-bounded stage with entry and evidence-based exit gate |
| Workstream | Concurrent ownership lane, not a backlog hierarchy level |
| Enabler | Foundational capability that unlocks downstream work |
| Epic/functionality | Large coherent product or system capability |
| Feature | Independently demonstrable behavior or outcome |
| Task | Atomic engineer-agent execution packet |
| Gate | Evidence required before dependent work can progress |

Repository structure, environments, CI/CD, tenancy, identity, observability, harness, router, and eval infrastructure are enablers—not fake user features.

## Agent workflow

1. Validate spec approval and preserve requirements, decisions, invariants, risks, and acceptance conditions.
2. Inspect repository instructions, base revision, structure, symbols, schemas, contracts, dependencies, tests, CI/CD, infrastructure, and deployment conventions read-only.
3. Return contradictions or architecture exceptions to specification.
4. Decompose top-down into phases, enablers, epics, features, tasks, and gates.
5. Build the dependency graph, detect cycles, and identify the critical path.
6. Identify safe parallel groups and expected write boundaries.
7. Allocate engineer-agent pairs based on supervision, risk, review, integration, and environment capacity.
8. Map requirements to work, verification, completion evidence, and release evidence.
9. Create a ready queue and define stop/escalation conditions.
10. Obtain human agreement first on decomposition/dependencies, then on execution topology/allocation.

## Safe concurrency model

```text
effective lanes = minimum(
  dependency-ready work,
  available supervision,
  non-conflicting ownership,
  review capacity,
  integration capacity,
  environment/test capacity
)
```

Use one concurrent writing agent per branch/worktree. Read-only researchers and reviewers may share the same baseline. Treat review and integration as constrained work.

## Delegation and monitoring

| Level | Meaning |
|---|---|
| `D0` | Human executes; agent advises |
| `D1` | Agent drafts; human directs each major step |
| `D2` | Agent implements bounded work; frequent checkpoints |
| `D3` | Agent completes task and checks; human reviews result |
| `D4` | Agent works asynchronously within strict sandbox and stop rules |
| `D5` | Policy-authorized automation through an external gate; never implied by planning approval |

Monitoring should specify event-driven checks, milestone review, periodic review, or continuous supervision. Overnight work must be isolated, reversible, bounded, resource-limited, and forbidden from merging, deploying, deleting, sending, or touching production/customer data.

## Exit gate

The plan is ready only when dependencies are acyclic, critical paths and parallel groups are credible, every mandatory requirement maps to work and evidence, tasks have bounded write sets and owners, review/integration capacity is feasible, and rollout/rollback are covered. Explicit human approval creates `APPROVED — READY TO IMPLEMENT`.

## Prohibited actions

Do not create branches, worktrees, issues, code, infrastructure, migrations, deployments, or other implementation changes. Planning proposes those actions; a separate authorized workflow performs them.
