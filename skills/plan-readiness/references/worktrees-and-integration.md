# Worktrees, branches, and integration

## Default isolation rule

Propose one isolated worktree and one dedicated branch for each concurrent writing agent. Multiple read-only agents may inspect a shared tree. Never recommend several writers in one worktree unless a human explicitly accepts a narrowly partitioned exception.

Planning does not create these resources.

## Specify each execution lane

Record:

- repository and verified base revision;
- proposed branch and worktree names;
- engineer owner and agent role/runtime;
- task and parallel group;
- expected write set;
- protected files and shared contracts;
- execution environment: local, cloud, or sandbox;
- integration target, owner, order, and required checks;
- rebase/revalidation condition;
- cleanup owner after integration.

Avoid putting secrets, personal data, or customer identifiers into names.

## Detect collisions

Treat work as coordinated or sequential when branches may independently alter:

- migrations or schema history;
- public APIs, events, or generated clients;
- authentication, authorization, or tenant context;
- global configuration, dependency manifests, lockfiles, or build systems;
- shared packages, fixtures, prompts, skills, agent-state schemas, or routing policy;
- the same deployment unit or scarce test environment.

Exact file separation is insufficient when two branches change the same logical contract.

## Plan contract-first integration

When parallel consumers need a new contract:

1. define and approve the contract;
2. assign a contract owner;
3. land or freeze the contract baseline;
4. branch dependent work from that baseline;
5. validate consumers independently;
6. integrate in an explicit order;
7. run combined contract, regression, security, and migration checks.

## Prefer short-lived work

Recommend short-lived task or feature branches with frequent integration. Use a phase/epic integration branch only when multiple coordinated streams genuinely need a temporary assembly point. Document merge order and divergence limits.

## Revalidate stale work

Require rebase and targeted revalidation when the base changes on a relevant file, schema, contract, dependency, permission, agent policy, or infrastructure surface. Do not invalidate a plan for unrelated changes without evidence.

## Assign integration ownership

Every parallel group requires a human integration owner responsible for shared-contract decisions, merge ordering, conflict resolution, combined verification, and the group exit gate. The number of active lanes must not exceed integration or review capacity.
