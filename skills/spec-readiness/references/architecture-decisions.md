# Architecture and technology decisions

Apply this guide to a project/product specification or any change that alters the architecture baseline.

## Architecture baseline

Specify the target system at the component and contract level. Include a concise diagram when relationships or event flow would otherwise be ambiguous. Cover:

- control plane and tenant/data plane;
- client applications, APIs, services, workers, and schedulers;
- synchronous, asynchronous, event-driven, and background execution;
- system-of-record, vector, cache, object, event, and analytical stores;
- identity, authorization, secrets, integrations, and external services;
- deployment units, network boundaries, regions, and failure domains;
- observability, operations, backup, recovery, rollout, and rollback.

Do not turn architecture into a file tree or implementation sequence.

## Tenancy and isolation

Make an explicit decision among single-tenant, shared multi-tenant, siloed multi-tenant, or hybrid. Define the tenant unit and isolation separately for:

| Boundary | Required decision |
|---|---|
| Runtime/compute | Shared process, namespace, container, cluster, or dedicated deployment |
| Transactional data | Shared tables with enforced key, schema per tenant, or database per tenant |
| Vector/search data | Namespace/index/collection/store isolation and retrieval filters |
| Object/file storage | Prefix/bucket/account isolation and access enforcement |
| Agent state and memory | Ownership, read/write scope, retention, and cross-agent sharing |
| Model context | Tenant-safe assembly, caching, logging, and provider transmission |
| Credentials and secrets | Per-user, per-agent, per-tenant, or platform credentials |
| Integrations | Connection ownership, scopes, token lifecycle, and revocation |
| Logs and telemetry | Tenant attribution, redaction, access, and retention |
| Encryption | Keys, rotation, and customer-managed requirements |
| Network | Shared or isolated paths, ingress/egress, and private connectivity |

Also specify provisioning, configuration, suspension, export, deletion, backup/restore, noisy-neighbor controls, quotas, regional placement, and expected tenant/workload envelope.

“Multi-tenant” alone is not a specification.

## Technology stack

For each layer, capture selected technology, status, rationale, constraints, alternatives, tradeoffs, operational owner, and exit path:

- client and frontend framework;
- backend language and framework;
- API and contract approach;
- workflow/job runtime;
- transactional, vector, cache, object, event, and analytical storage;
- identity and policy enforcement;
- integration/MCP layer;
- AI/agent runtime;
- deployment platform and infrastructure management;
- testing, eval, observability, and security tooling.

Evaluate choices using the criteria that actually matter: existing system fit, team capability, ecosystem, security, data residency, reliability, scale, latency, cost, portability, vendor dependence, licensing, operability, and migration difficulty.

Do not introduce a new tool when the existing stack meets the requirements unless the human approves the added complexity.

## Decision record

```markdown
### DEC-[NNN] — [Decision name]

- Status: Inherited | Proposed | Approved | Rejected | Deferred
- Decision owner: [Human]
- Decision required: [Precise question]
- Drivers: [Requirements/constraints]
- Options considered: [Credible options]
- Recommendation: [Option and evidence-based rationale]
- Tradeoffs: [Benefits, costs, risks, reversibility]
- Consequences: [System and operational effects]
- Validation/exit trigger: [How to revisit safely]
- Human decision evidence: Pending
```

Never write `Approved` without explicit human evidence. A preference is not a constraint, and a recommendation is not a decision.

## Project versus child specifications

- Establish the baseline once in the project specification.
- Reference inherited decisions in child specs rather than copying them.
- Document only the delta or exception for a feature, improvement, or bug.
- Treat an exception affecting isolation, security, data, public contracts, or core runtime as a material decision requiring approval.
- If no parent baseline exists, include the minimum architecture needed to make the current change safe and flag creation of the baseline as a blocking or owned follow-up.
