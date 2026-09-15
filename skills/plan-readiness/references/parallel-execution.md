# Parallel agent execution

## Classify parallelism

| Class | Meaning |
|---|---|
| Sequential | Must wait for a dependency or stable contract |
| Parallel-independent | No shared mutable code, contract, environment, or approval |
| Parallel-partitioned | Ownership and write sets are explicitly separated |
| Parallel-coordinated | Shared contract exists with an owner and integration cadence |
| Integration-bound | Output awaits combined verification or merge |
| Human-blocked | Waiting for decision, review, or approval |
| Environment-blocked | Waiting for credentials, data, compute, or test environment |
| Unsafe-to-parallelize | Conflict, risk, or review cost exceeds throughput benefit |

Evaluate file/schema/API/event/configuration overlap, migration order, environment contention, test fixtures, domain ownership, review capacity, security risk, and integration complexity—not only logical dependencies.

## Choose collaboration patterns

- **Independent builders:** separate work, separate worktrees, minimal shared contracts.
- **Contract-first:** approve interface/schema/event contract, then run backend, frontend, test, and documentation work in parallel.
- **Researcher → builder → verifier:** use for unfamiliar or uncertain work; pass evidence and artifacts rather than hidden reasoning.
- **Builder → independent verifier:** use for ordinary features and bug fixes.
- **Sequential high-risk:** alternate agent work with human checkpoints for identity, authorization, tenancy, migrations, production infrastructure, destructive actions, or material AI autonomy.

Do not assign several writing agents to the same worktree. Read-only research/review agents may inspect the same tree.

## Classify delegation

| Level | Meaning |
|---|---|
| `D0` | Human executes; agent may advise |
| `D1` | Agent assists while human drives |
| `D2` | Agent executes bounded steps with intermediate checkpoints |
| `D3` | Agent implements, verifies, and prepares a reviewable change |
| `D4` | Agent completes bounded reversible work asynchronously |
| `D5` | Autonomous execution prohibited; explicit authorized action required |

Assign from blast radius, reversibility, requirement clarity, test strength, code coupling, secrets/data access, external effects, agent reliability, and escalation needs. Complexity alone does not determine delegation.

## Classify monitoring

| Level | Engineer involvement |
|---|---|
| `M0` | Review final verified artifact |
| `M1` | Review defined milestones |
| `M2` | Active review of intermediate decisions and changes |
| `M3` | Paired execution throughout |
| `M4` | Human execution; agent advice only |

State what triggers a pause, what the agent may decide, what requires approval, what evidence must return, and what terminates the run.

## Determine overnight safety

Allow unattended execution only when work is isolated, bounded, reversible, non-production, free of unapproved external effects, protected from customer-data mutation, equipped with deterministic checks, subject to time/token/retry limits, and able to stop at a reviewable artifact. Require explicit escalation and recovery instructions.

Never treat merge, deployment, external sending, destructive data work, identity/permission activation, or production change as overnight-safe without explicit policy and authorization.

## Require a handoff

The future execution agent must report task, runtime, repository/base, branch/worktree, final revision, files changed, requirements implemented, tests/evals and results, decisions, assumptions, deviations, discovered risks, failed attempts, remaining work, and required human action.
