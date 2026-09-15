# Task Plan: [Name]

ID: TASK-001
Status: BLOCKED | READY FOR ENGINEER | READY FOR AGENT
Parent: [EN/EP/FEAT/IMPR/BUG ID]
Requirements: [Specification IDs]
Depends on: [IDs or None]
Parallel group: [PG ID or None]
Parallelization class: Sequential | Parallel-independent | Parallel-partitioned | Parallel-coordinated | Integration-bound | Human-blocked | Environment-blocked | Unsafe-to-parallelize
Primary engineer: [Human]
Agent role/runtime: [Builder/tester/reviewer/researcher and runtime]
Agent collaboration pattern: Independent builder | Builder-verifier | Researcher-builder-verifier | Contract-first | Sequential high-risk
Agent execution size: Small | Medium | Large
Expected agent cycles: [Number or range]
Execution location: Local | Cloud | Sandbox
Repository: [Identity]
Base revision: [Verified revision]
Branch: [Proposed branch]
Worktree: [Proposed worktree]
Expected write set: [Paths/symbols/contracts]
Protected files/surfaces: [Paths/contracts]
Shared contracts: [IDs/paths or None]
Delegation level: D0 | D1 | D2 | D3 | D4 | D5
Monitoring level: M0 | M1 | M2 | M3 | M4
Supervision units: [Project-relative number]
Overnight-safe: Yes | No
Integration target/owner: [Target and human]
Human checkpoint: [Trigger or None]

## Objective

[One bounded implementation result.]

## Execution Context

[Relevant approved requirements, verified current behavior, parent decisions, and dependencies.]

## Implementation Boundary

- Must change: [Behavior/surfaces]
- May change: [Permitted boundary]
- Must not change: [Protected behavior/surfaces]

## Planned Steps

1. [Concrete action without production code]
2. [Verification action]

## Tests and Evals

- Commands: [Verified commands]
- Required cases: [Primary/edge/failure/security/regression]
- Pass thresholds: [Evidence]

## Completion Evidence

[Files/results/tests/evals/reports required for review.]

## Stop Conditions

[Unexpected architecture, contract, data, permission, secret, environment, destructive, test, or specification condition that requires a pause.]

## Risks and Escalation

[Risk, mitigation, escalation recipient, and decision required.]

## Required Handoff

[Use the agent execution report template; state reviewer and integration prerequisites.]
