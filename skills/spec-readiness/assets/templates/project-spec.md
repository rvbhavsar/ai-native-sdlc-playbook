# Specification: [Project or Product Name]

Type: Project
Status: Draft
Version: 0.1
Owner: [Human decision owner]
Intent: [Approved intent path/link and version]
Parent specification: Not applicable
Last updated: [Date]

## Intent Traceability

- Approved problem/outcome: [Summary]
- In scope: [Boundary]
- Non-goals: [Exclusions]
- Must remain unchanged: [Preservation contract]
- Success contract: [Intent-level success]
- Intent contradictions discovered: None

## System Context

[Verified current state, system boundary, external actors, and target context. Label observed, reported, proposed, and assumed facts.]

## Actors, Roles, and Permissions

| Actor/role | Context | Allowed | Approval required | Denied |
|---|---|---|---|---|
| [Role] | [Context] | [Actions/data] | [Actions] | [Boundary] |

## Capabilities and Workflows

[Major capabilities, triggers, primary/alternate/failure workflows, states, side effects, and child specification boundaries.]

## Functional and Business Requirements

- `FR-001`: [The system shall...]
- `BR-001`: [Business rule]

## Architecture Overview

[Target components, responsibilities, boundaries, trust zones, data/event flow, and a diagram when useful.]

## Tenancy and Isolation Model

- Selected model: [Single-tenant/shared/siloed/hybrid — decision reference]
- Tenant unit: [Definition]
- Runtime isolation: [Requirement]
- Transactional data isolation: [Requirement]
- Vector/search isolation: [Requirement]
- Object/file isolation: [Requirement]
- Agent state/memory isolation: [Requirement]
- Model-context isolation: [Requirement]
- Secrets/integration isolation: [Requirement]
- Logs/telemetry isolation: [Requirement]
- Encryption/network isolation: [Requirement]
- Provisioning/export/deletion/backup: [Lifecycle]
- Quotas/noisy-neighbor/region: [Controls]

## Technology Stack

| Layer | Selected technology | Status | Rationale | Alternatives/tradeoffs | Exit path |
|---|---|---|---|---|---|
| [Layer] | [Technology] | Proposed | [Why] | [Options] | [Migration/revisit trigger] |

## Application and Service Architecture

[Clients, APIs, services, workers, schedulers, execution modes, contracts, ownership, and failure domains.]

## Data and Storage Architecture

- `DR-001`: [System of record, ownership, validation, lifecycle, retention, deletion, audit, backup, and residency requirement]
- Stores and responsibilities: [Transactional/vector/cache/object/event/analytics]

## Identity, Access, and Authorization

- `SEC-001`: [Authentication, authorization, tenant/role/resource enforcement, administrative access, and audit requirement]

## Integrations and Tools

- `IR-001`: [Connection owner, scopes, contract, idempotency, timeout, retry, partial failure, revocation, and audit]

## Agent Architecture

- `AI-001`: [Agent topology, responsibility, boundary, triggers, state, tools, prohibited actions, handoffs, and recovery]

## Agent Harness and Orchestration

[Required capabilities, selected/proposed harness, durable state, interrupts, retries, schedules/events, portability, versioning, and decision reference.]

## LLM and Model Strategy

| Workload | Quality/risk | Capability/context | Latency/availability | Privacy/region | Primary/fallback | Budget |
|---|---|---|---|---|---|---|
| [Task] | [Need] | [Need] | [Target] | [Boundary] | [Models/status] | [Limit] |

## LLM Router

- `AI-002`: [Routing inputs, policies, allowed models, fallback, attempts, timeout, circuit breaking, validation, quotas, telemetry, and versioning]

## Knowledge, Context, Memory, and Files

[Authoritative sources, provenance, freshness, retrieval, context assembly, short/long-term memory, file ownership, read/write/share/delete rules, retention, and isolation.]

## Human-in-the-Loop Controls

| Action | Risk | Autonomy level | Approver | Bound payload/evidence | Expiry/reapproval | Reversal |
|---|---|---|---|---|---|---|
| [Action] | [Risk] | [Autonomous/notify/confirm/role/prohibited] | [Role] | [Evidence] | [Rule] | [Method] |

## Security, Privacy, and Compliance

- `SEC-002`: [Threat, control, evidence, owner, and release condition]

## Infrastructure and Deployment

[Environments, platform, regions, deployment units, configuration/secrets, network, infrastructure ownership, and recovery requirements.]

## Scalability, Reliability, Performance, and Cost

- `NFR-001`: [Workload, target, measurement conditions, degradation, recovery, and cost boundary]

## Observability and Operations

- `OBS-001`: [Logs, metrics, traces, audit, correlation, alert, dashboard, support, and runbook requirements]

## AI Evals and Quality Assurance

[Datasets, task success, groundedness, tool/routing/permission/isolation/HIL tests, thresholds, release gates, regression, sampling, latency, and cost.]

## Compatibility, Migration, Rollout, and Rollback

[Existing commitments, data migration, versioning, flags, pilot/phases, rollback triggers, remediation, and customer impact.]

## Acceptance Scenarios

- `AC-001` verifies `[FR/SEC/AI/NFR IDs]`: [Given/When/Then or other observable scenario]

## Decision Register

| ID | Decision | Status | Owner | Recommendation/choice | Evidence |
|---|---|---|---|---|---|
| `DEC-001` | [Decision] | Proposed | [Human] | [Option] | Pending |

## Constraints, Dependencies, Assumptions, and Risks

- Constraint: [Hard boundary]
- Dependency: [External prerequisite and owner]
- Assumption: [Belief, validation, owner, decision point]
- Risk: [Likelihood/impact, mitigation, acceptance owner]

## Requirement Traceability

| Intent outcome | Requirements/decisions | Acceptance/eval evidence |
|---|---|---|
| [Outcome] | `[IDs]` | `[AC/eval IDs]` |

## Open Decisions

- [Blocking/non-blocking, owner, options, and required decision point]

## Human Approval

- Decision: Pending
- Approver: Pending
- Approved version: Pending
- Approval evidence: Pending
- Conditions and accepted risks: None
