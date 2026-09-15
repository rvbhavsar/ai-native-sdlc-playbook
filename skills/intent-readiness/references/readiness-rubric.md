# Intent readiness rubric

Score each dimension from 0 to 4:

- **0 — Missing:** no usable information.
- **1 — Vague:** present but ambiguous or solution-led.
- **2 — Partial:** directionally useful; material gaps remain.
- **3 — Sufficient:** clear enough for specification without guessing.
- **4 — Strong:** clear, evidenced, bounded, and internally consistent.

## Weighted score

| Dimension | Weight | Critical |
|---|---:|:---:|
| Problem/trigger and current state | 15 | Yes |
| Users, stakeholders, or affected area | 10 | Yes |
| Desired outcome and value | 15 | Yes |
| Scope, non-goals, and unchanged behavior | 15 | Yes |
| Success/acceptance evidence | 15 | Yes |
| Constraints and guardrails | 10 | When applicable |
| Dependencies and assumptions | 5 | No |
| Risks and failure consequences | 5 | When applicable |
| Type-specific evidence | 10 | Yes |

Calculate each contribution as `weight × score / 4`. Round the total to a whole number.

## Gate states

### NOT READY

Use when the score is below 85, a critical dimension is below 3, or a blocking unknown remains.

### READY FOR HUMAN APPROVAL

Use when:

- total score is at least 85;
- every applicable critical dimension is at least 3;
- no blocking unknown could change scope, acceptance, security, compliance, permissions, or data handling;
- type-specific minimum evidence is present.

### APPROVED — READY FOR SPEC

Use only when the prior state passes and the human explicitly approves the exact intent draft. Record the approval evidence. Never infer approval.

## Type-specific minimum evidence

- **Project/product:** strategic purpose, primary users/stakeholders, outcome, initial boundary, success signal, major dependencies, and ownership.
- **Feature:** user need, entry/exit behavior, primary path, important failure/edge path, acceptance, permissions/data implications, and unchanged behavior.
- **Improvement:** current baseline, specific limitation, desired delta, preservation contract, measurement method, and regression boundary.
- **Bug:** observed versus expected behavior, impact, reproducibility or captured evidence, relevant environment, fix acceptance, and regression boundary.

## Blocking-unknown test

An unknown is blocking if different reasonable answers would produce materially different:

- target users or authorization rules;
- included/excluded behavior;
- data collection, retention, isolation, or compliance duties;
- acceptance conditions;
- rollout or compatibility commitments;
- harm, recovery, or failure handling.

The human may resolve it, narrow scope to remove it, explicitly accept the risk, or pause. Accepted risk must be documented and may still prevent readiness when safety, law, or authorization cannot be responsibly deferred.

## Readiness report

```markdown
## Intent Readiness

- Status: NOT READY | READY FOR HUMAN APPROVAL | APPROVED — READY FOR SPEC
- Score: [0–100]
- Critical gaps: [none or concise list]
- Assumptions requiring validation: [list]
- Accepted risks/deferred items: [list]
- Recommendation: [one sentence]
- Approval evidence: [pending or explicit human statement]
```

Do not inflate scores to end the interview. Do not use a score as a substitute for judgment.
