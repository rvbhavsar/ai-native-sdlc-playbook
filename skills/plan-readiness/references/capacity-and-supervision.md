# Engineer-agent capacity and continuous execution

## Assess each project

Do not assume a universal number of agents per engineer. Calculate safe capacity from engineer expertise, module familiarity, task clarity, coupling, risk, test strength, agent reliability, environment stability, review time, integration load, and availability.

## Use supervision units

Suggested relative load:

| Work | Units |
|---|---:|
| Independent, reversible, strongly tested | 1 |
| Moderate ambiguity or coupling | 2 |
| Shared contract, migration, or complex integration | 3 |
| Identity, authorization, tenancy, sensitive data, or high-risk AI action | 4 |
| Production, destructive, or irreversible work | 5 |

Adjust units from project evidence. Do not invent an engineer’s capacity. Ask the human to confirm available people, expertise, review windows, and safe supervision budget.

For each engineer show active tasks, delegation/monitoring level, units, remaining capacity, conflicts, and authorized risk domains. Keep a reserve for integration and incidents.

## Calculate effective concurrency

`effective lanes = minimum(available supervision, dependency-ready work, non-conflicting ownership, review capacity, integration capacity, environment/test capacity)`

Identify the limiting factor. Do not claim linear speedup from additional agents.

## Estimate agentically

Classify work by:

- agent execution size: small, medium, large;
- expected implement→verify→correct cycles;
- human review intensity;
- dependency and integration risk;
- rework uncertainty;
- parallelizability;
- required runtime/environment.

Derive delivery windows only after dependencies, safe lanes, review cadence, and integration gates are known. Prefer ranges and assumptions over false calendar precision.

## Sustain a 24/7 queue safely

Keep more ready work than active lanes without exceeding review capacity. Queue only tasks that have stable inputs, bounded write sets, deterministic checks, stop conditions, resource limits, recovery, handoff, and no pending decision.

Separate queues:

- ready for supervised execution;
- ready for asynchronous execution;
- ready for overnight-safe execution;
- waiting for review;
- waiting for integration;
- blocked.

Unattended agents stop at reviewable artifacts. They do not merge, deploy, send, delete, modify production/customer data, or cross authorization gates unless a separate policy and explicit approval permit the exact action.

## Protect human throughput

Plan review batches and integration points. Too many simultaneously completed branches create review debt and stale work. Reduce WIP when review or integration becomes the bottleneck, even if idle agent capacity remains.
