# Feature planning

Create one implementation-ready feature plan and its atomic task files. Inherit project decisions and parent execution constraints.

## Derive

- verified current behavior, reusable code, and exact affected surfaces;
- vertical implementation strategy across backend, frontend, data, integrations, agent/AI, security, observability, tests, and rollout;
- contract-first work and safe parallel groups;
- tasks with write boundaries, protected surfaces, branches/worktrees, delegation, monitoring, ownership, evidence, and handoffs;
- combined integration order and end-to-end acceptance.

## Sequence

1. stabilize or reuse shared contracts;
2. add failing/acceptance tests or fixtures where practical;
3. implement parallel-safe surfaces;
4. integrate and run combined verification;
5. validate security, permissions, tenant isolation, failure/recovery, and observability;
6. roll out and monitor using the approved strategy.

Return to specification if the feature requires an unapproved architecture, behavior, data, permission, or external-contract change.
