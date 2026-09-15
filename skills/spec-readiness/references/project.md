# Project or product specification

Use the project template to establish the authoritative product/system baseline inherited by child specifications.

## Resolve

- product boundary, actors, capabilities, major workflows, success contract, and non-goals;
- current versus target system context;
- tenancy and isolation model;
- language, frameworks, services, data stores, identity, integrations, infrastructure, regions, and deployment units;
- agent topology, harness, models, routing, tools, knowledge, memory, files, HIL, and evals when applicable;
- security, privacy, compliance, reliability, scale, performance, observability, recovery, cost, migration, rollout, and rollback;
- externally committed contracts and major dependencies;
- material decisions, alternatives, tradeoffs, and human ownership.

## Ask high-impact questions

- Is this a greenfield system, an extension, or a replacement, and which existing commitments must survive?
- What is the tenant/customer boundary and required isolation for every data and execution surface?
- Which stack decisions are inherited constraints versus genuinely open choices?
- What workload, availability, region, recovery, and cost envelope must the architecture support?
- Which actions or failures could harm customers, expose data, create financial effects, or become irreversible?
- What technical choices would be expensive to reverse and therefore require explicit approval now?
- Which capabilities form independently deliverable child specifications?

## Do not approve when

- the architecture is a tool list without responsibility or boundary;
- “multi-tenant,” “secure,” “scalable,” or “agentic” lacks a measurable contract;
- a core stack, isolation, data, identity, deployment, or AI-runtime decision remains silently unresolved;
- acceptance covers shipping but not behavior, operations, and risk.
