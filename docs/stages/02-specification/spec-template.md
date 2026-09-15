# Specification: [Name]

## Control

| Field | Value |
|---|---|
| Type | Project / Feature / Improvement / Bug |
| Status | Draft / Ready for Human Review / Approved — Ready for Plan |
| Version | `0.1` |
| Intent baseline | `[intent version/link]` |
| Decision owner | [Name/role] |
| Technical owner | [Name/role] |
| Last updated | YYYY-MM-DD |

## Executive summary

[What the system/change must accomplish and the major approved design choices.]

## Intent traceability and boundaries

| Intent item | Specification response |
|---|---|
| `OUT-001` | [Requirements that realize it] |
| Non-goal/invariant | [How the design preserves it] |

## Users, actors, roles, and permissions

| Actor | Goal | Authentication | Authorized actions | Prohibited actions |
|---|---|---|---|---|
| [Actor] | [Goal] | [Method] | [Actions] | [Boundaries] |

## Journeys, states, and behavior

### Primary journey

1. [User/system action]
2. [Expected response]

### Edge and failure behavior

- [Condition] → [Required behavior, recovery, and user feedback]

## Functional and business requirements

| ID | Requirement | Priority | Source | Verification |
|---|---|---|---|---|
| `FR-001` | The system shall [atomic behavior]. | Must | `OUT-001` | `AC-001` |
| `BR-001` | [Business rule and boundary.] | Must | [Source] | [Evidence] |

## System architecture

- Context and boundaries: [System and external actors]
- Components/services: [Responsibilities and boundaries]
- Communication: [Synchronous, asynchronous, events, queues]
- Deployment shape: [Runtime topology]
- Existing architecture inherited: [Reference]
- Approved exceptions: [Decision ID or `None`]

## Tenancy and isolation

- Model: Single-tenant / Multi-tenant / Hybrid
- Tenant identity and lifecycle: [Provisioning, suspension, deletion]
- Data isolation: [Database/schema/row/log/cache/file/vector boundaries]
- Compute and network isolation: [Boundary]
- Configuration/customization: [Per-tenant controls]
- Cross-tenant administration and support: [Controls and audit]
- Regional/residency requirements: [Requirement]

## Technology stack and repository strategy

| Layer | Decision | Version/constraint | Rationale | Alternatives/tradeoffs | Decision ID |
|---|---|---|---|---|---|
| Repository | Monorepo / Multi-repo | [Constraint] | [Why] | [Tradeoffs] | `DEC-001` |
| Frontend | [Language/framework] | [Version] | [Why] | [Tradeoffs] | `DEC-002` |
| Backend/API | [Language/framework] | [Version] | [Why] | [Tradeoffs] | `DEC-003` |
| Data | [Store/ORM] | [Version] | [Why] | [Tradeoffs] | `DEC-004` |
| Infrastructure | [Platform/IaC] | [Constraint] | [Why] | [Tradeoffs] | `DEC-005` |

## Identity, organization, and administration

- Authentication: [Provider/protocol/session model]
- Authorization: [RBAC/ABAC/policy model]
- Organization structure: [B2B tenant, team, workspace, hierarchy]
- User lifecycle: [Invite, activate, suspend, remove, recover]
- Administrative roles: [Platform, tenant, support, audit]
- Service/workload identity: [Method]
- Audit requirements: [Events and retention]

## Data design and lifecycle

| ID | Data/domain | Owner | Classification | Storage | Retention/deletion | Migration |
|---|---|---|---|---|---|---|
| `DR-001` | [Data] | [Owner] | [Class] | [System] | [Policy] | [Requirement] |

Cover schemas and invariants, consistency, encryption, backup/recovery, import/export, residency, and test data.

## Interfaces and integrations

| ID | Interface | Contract | Auth | Versioning | Failure/idempotency |
|---|---|---|---|---|---|
| `IR-001` | [API/event/tool] | [Reference/shape] | [Method] | [Policy] | [Behavior] |

## AI, agent, and LLM subsystem

> Use `Not applicable — [reason]` when the product has no AI behavior.

- User value and bounded AI responsibility: [Purpose]
- Agent topology: [Single agent, supervisor-workers, workflow graph]
- Harness/runtime: [Session lifecycle, context assembly, checkpoints, retries, cancellation]
- Model strategy: [Capability tiers, providers, versions, fallbacks]
- LLM router: [Selection inputs, policy, fallback, latency/cost/quality rules]
- Tools/actions: [Allowlist, permissions, scopes, confirmation]
- Knowledge/retrieval: [Sources, freshness, access filtering, citations]
- Memory: [Scope, retention, user/tenant isolation, deletion]
- Structured output: [Schemas, validation, repair/failure behavior]
- Human-in-the-loop: [Review/approval/edit/escalation points]
- Safety: [Prompt injection, data leakage, harmful actions, abuse]
- Observability: [Traces, prompts/models, redaction, feedback]
- Cost controls: [Budgets, quotas, caching, limits]

| ID | AI requirement | Risk | Eval/acceptance evidence |
|---|---|---|---|
| `AI-001` | [Requirement] | [Risk] | [Evidence] |

## Security, privacy, compliance, and abuse

| ID | Requirement/threat | Control | Verification | Owner |
|---|---|---|---|---|
| `SEC-001` | [Requirement] | [Control] | [Evidence] | [Owner] |

## Non-functional and operational requirements

| ID | Quality attribute | Target and conditions | Evidence |
|---|---|---|---|
| `NFR-001` | Performance | [Target under defined load] | [Benchmark] |
| `OBS-001` | Observability | [Logs/metrics/traces/alerts] | [Operational proof] |

Include reliability, availability, scalability, accessibility, localization, compatibility, supportability, recovery objectives, and cost where applicable.

## Acceptance, testing, and eval contract

| ID | Scenario/requirement | Evidence type | Pass condition | Environment |
|---|---|---|---|---|
| `AC-001` | [Scenario] | Test / Eval / Inspection / Operational proof | [Condition] | [Where] |

Define unit, integration, contract, end-to-end, security, tenant-isolation, migration, AI eval, regression, and human acceptance coverage proportionally.

## Rollout, compatibility, migration, and rollback requirements

- Compatibility: [Requirement]
- Migration behavior: [Requirement]
- Rollout controls: [Flags, cohorts, canary, approval]
- Rollback/recovery outcome: [Required capability and data treatment]

## Decision register

| ID | Decision | Options considered | Rationale/tradeoffs | Status | Human evidence | Revisit trigger |
|---|---|---|---|---|---|---|
| `DEC-001` | [Decision] | [Options] | [Why/consequences] | Proposed / Approved | [Evidence] | [Trigger] |

## Assumptions, dependencies, risks, and open questions

| ID | Type | Item | Impact | Owner | Validation/disposition |
|---|---|---|---|---|---|
| `RSK-001` | Assumption / Dependency / Risk / Open | [Item] | [Impact] | [Owner] | [Method/status] |

## Readiness and approval

- Readiness status: `NOT READY` / `READY FOR HUMAN REVIEW`
- Score: [0–100]
- Blocking gaps: [List or `None`]
- Approved by: [Human only]
- Approved version and statement/date: [Evidence]
