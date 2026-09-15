# Plan readiness rubric

Score each applicable dimension from 0 to 4:

- **0 — Missing:** absent or unusable.
- **1 — Vague:** aspirational, ungrounded, or contradictory.
- **2 — Partial:** useful direction but material invention remains.
- **3 — Sufficient:** executable and verifiable without material guessing.
- **4 — Strong:** repository-grounded, dependency-safe, traceable, capacity-aware, and reversible.

## Weighted dimensions

| Dimension | Weight | Critical |
|---|---:|:---:|
| Approved input and specification alignment | 10 | Yes |
| Repository and current-system grounding | 10 | Yes |
| Decomposition into enablers/epics/features/tasks | 10 | Yes |
| Dependencies, phases, critical path, and gates | 15 | Yes |
| Parallelism, worktrees, write boundaries, and integration | 15 | Yes |
| Engineer-agent allocation and supervision capacity | 10 | Yes |
| Tests, AI evals, evidence, and traceability | 15 | Yes |
| Security, data, migrations, operations, rollout, and recovery | 10 | When applicable |
| Risks, assumptions, handoffs, and human controls | 5 | Yes |

Normalize across applicable dimensions. Never label a difficult concern inapplicable to raise the score.

## Gate states

### NOT READY

Use when the score is below 90, a critical dimension is below 3, input is unapproved, repository grounding is required but absent, a dependency cycle or unsafe conflict exists, or a blocking decision/owner/evidence is missing.

### READY FOR HUMAN REVIEW

Use only when:

- score is at least 90/100;
- every critical dimension scores at least 3/4;
- specification requirements map to work and verification;
- dependencies and cycles are resolved;
- parallel lanes have non-conflicting ownership or explicit coordination;
- supervision, review, integration, and environment capacity bound concurrency;
- high-risk work has human checkpoints;
- rollback/recovery exists where needed;
- every `READY FOR AGENT` task has a complete execution contract.

### APPROVED — READY TO IMPLEMENT

Use only after explicit human approval of the exact plan version, specification version, repository base revision, execution graph, allocation, test/eval strategy, and rollout/rollback approach. The agent cannot self-approve.

## Readiness report

```markdown
## Plan Readiness

- Status: NOT READY | READY FOR HUMAN REVIEW | APPROVED — READY TO IMPLEMENT
- Plan/spec/base: [exact versions]
- Score: [0–100]
- Critical path: [summary]
- Effective concurrency and bottleneck: [lanes and limiting factor]
- Critical gaps/conflicts/cycles: [none or list]
- Proposed high-impact decisions: [none or list]
- Assumptions requiring validation: [list]
- Accepted risks/deferred matters: [list]
- Stale-baseline risk: [none or affected surfaces]
- Recommendation: [one sentence]
- Approval evidence: [pending or exact human statement]
```

Use the score as a diagnostic, not as permission to mutate or bypass human review.
