# Specification readiness rubric

Score applicable dimensions from 0 to 4:

- **0 — Missing:** absent or unusable.
- **1 — Vague:** ambiguous, contradictory, or mostly aspirational.
- **2 — Partial:** useful direction with material guessing still required.
- **3 — Sufficient:** implementable and testable without material product or architecture invention.
- **4 — Strong:** precise, evidenced, internally consistent, traceable, and risk-aware.

## Weighted dimensions

| Dimension | Weight | Critical |
|---|---:|:---:|
| Intent alignment, scope, and non-goals | 10 | Yes |
| Functional behavior and business rules | 15 | Yes |
| Workflows, states, errors, and recovery | 10 | Yes |
| Architecture and technology decisions | 15 | Yes for projects/deltas |
| Tenancy, data, permissions, and security | 15 | When applicable |
| Agent, model, routing, tools, memory, and HIL | 10 | For AI systems |
| Non-functional, operations, rollout, and cost | 10 | When applicable |
| Acceptance, tests, evals, and traceability | 15 | Yes |

When a dimension is genuinely inapplicable, redistribute its weight proportionally across applicable dimensions. Do not label a difficult unknown inapplicable to raise the score.

## Gate states

### NOT READY

Use when the normalized score is below 85, an applicable critical dimension is below 3, a contradiction remains, or a blocking decision is unapproved.

### READY FOR HUMAN REVIEW

Use only when:

- score is at least 85/100;
- every applicable critical dimension scores at least 3/4;
- all mandatory requirements are testable;
- each critical requirement has acceptance or evaluation evidence;
- no blocker remains in scope, behavior, tenancy, data, permissions, security, architecture, AI action control, or rollout safety;
- decisions are marked inherited, approved, proposed, rejected, or deferred accurately.

### APPROVED — READY FOR PLAN

Use only after the human explicitly approves the exact specification version. The agent cannot self-approve. A material edit invalidates prior approval.

## Blocking decision test

A decision is blocking when different reasonable answers change any of:

- externally visible behavior or acceptance;
- authorization, tenant isolation, or sensitive-data handling;
- irreversible or destructive effects;
- externally committed interfaces or compatibility;
- core architecture, operational ownership, or recovery model;
- AI autonomy, tool permissions, model privacy, fallback, or HIL;
- material cost, scale, availability, or regional commitments.

## Readiness report

```markdown
## Specification Readiness

- Status: NOT READY | READY FOR HUMAN REVIEW | APPROVED — READY FOR PLAN
- Version: [exact version]
- Score: [0–100]
- Critical gaps: [none or list]
- Proposed decisions awaiting approval: [none or list]
- Assumptions requiring validation: [list]
- Accepted risks/deferred matters: [list]
- Contradictions with intent or parent spec: [none or list]
- Recommendation: [one sentence]
- Approval evidence: [pending or exact human statement]
```

Use scoring as a diagnostic, never as permission to bypass judgment or human approval.
