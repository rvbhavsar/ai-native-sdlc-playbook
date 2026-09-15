# Project Execution Plan: [Name]

Type: Project
Status: Draft
Version: 0.1
Owner: [Human plan owner]
Intent: [Reference/version]
Specification: [Approved reference]
Specification version: [Exact version]
Repository: [Identity]
Base revision: [Verified revision]
Last updated: [Date]

## Planning Objective

[Implementation outcome, approved scope/non-goals, and preserved behavior.]

## Approved Inputs and Baseline

- Specification approval evidence: [Evidence]
- Parent architecture/decisions: [References]
- Project instructions: [Files]
- Verified build/test/eval/migration commands: [Commands]
- Baseline confidence: Verified | Provisional

## System Decomposition

[Components/capabilities extracted from the specification and current system.]

## Foundation and Enabler Register

| ID | Enabler | Dependencies | Unlocks | Owner | Exit gate |
|---|---|---|---|---|---|
| `EN-001` | [Foundation] | None | [Downstream] | [Human] | `GATE-001` |

## Epic and Feature Map

| Epic/functionality | Features | Dependencies | Shared contracts | Owner |
|---|---|---|---|---|
| `EP-001` | `FEAT-001` | `EN-001` | [Contracts] | [Human] |

## Dependency Graph and Critical Path

- Critical path: [Ordered IDs and reason]
- Cycles: None
- Hidden/unverified dependencies: [None or list]
- Graph: [Compact Mermaid or dependency table]

## Phase Plan and Gates

### PHASE-001 — [Name]

- Objective: [Outcome]
- Entry criteria: [Evidence]
- Enablers/epics/features: [IDs]
- Sequential work: [IDs/order]
- Parallel groups: [PG IDs]
- Integration point: [Owner/target]
- Verification: [Tests/evals/inspection]
- Exit gate: `GATE-001` — [Evidence]
- Human checkpoint: Required | Not required

## Parallel Workstreams

| PG | Work items | Class | Shared surfaces | Coordination/contract owner | Integration order |
|---|---|---|---|---|---|
| `PG-001` | [IDs] | Independent/partitioned/coordinated | [Surfaces] | [Human] | [Order] |

## Engineer and Agent Capacity

| Engineer | Domain/authority | Safe supervision units | Assigned units | Agent lanes | Review capacity | Reserve |
|---|---|---:|---:|---:|---:|---:|
| [Engineer] | [Area] | [Units] | [Units] | [Count] | [Rate] | [Units] |

- Effective concurrency: [Lane count]
- Limiting factor: [Ready work/supervision/review/integration/environment]
- Delivery range and assumptions: [Only when requested]

## Execution Orchestration

| Phase | Parent | Task | Depends on | PG | Engineer | Agents/pattern/runtime | Environment | Worktree/branch | D/M | Units | Overnight | Gate |
|---|---|---|---|---|---|---|---|---|---|---:|---|---|
| [Phase] | [EN/EP/FEAT] | `TASK-001` | [IDs] | [PG] | [Human] | [Role/runtime] | [Local/cloud/sandbox] | [Proposal] | [D/M] | [Units] | Yes/No | [Gate] |

## Integration and Assembly

[Contract baselines, integration owners/targets/order/cadence, conflict rules, combined checks, rebase/revalidation, and cleanup.]

## Quality and Evidence

| Spec requirement | Work items | Test/eval/inspection | Completion evidence | Release evidence |
|---|---|---|---|---|
| [ID] | [IDs] | [Evidence ID/command] | [Result] | [Gate] |

## Environments, Rollout, and Recovery

[Local/cloud/sandbox needs, configuration/secrets, migrations, feature flags, rollout, monitoring, rollback, compensation, and recovery.]

## Risks, Assumptions, and Blockers

- Risk: [Impact, mitigation, owner]
- Assumption: [Validation, owner, deadline/gate]
- Blocker: [Required resolution]
- Accepted risk/deferred matter: [Human evidence]

## Requirement Traceability

[Confirm every mandatory requirement maps to work and evidence; list gaps or orphan work.]

## Ready Queue

| Task | State | Dependencies | Base stable | Contract stable | Execution contract complete | Owner |
|---|---|---|---|---|---|---|
| `TASK-001` | BLOCKED/READY FOR ENGINEER/READY FOR AGENT | [IDs] | Yes/No | Yes/No | Yes/No | [Human] |

## Human Checkpoints

- Decomposition review: Pending
- Execution-orchestration review: Pending
- High-risk gates: [List]

## Human Approval

- Decision: Pending
- Approver: Pending
- Approved plan version: Pending
- Specification version: [Exact version]
- Repository base revision: [Exact revision]
- Approval evidence: Pending
- Conditions and accepted risks: None
