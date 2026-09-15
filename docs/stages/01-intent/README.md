# Stage 1 — Intent Discovery

## Purpose

Turn a rough project, feature, improvement, or bug request into a concise agreement about why the work matters, who or what is affected, what must change, and what must not change.

## Entry

- A request, idea, incident, user observation, or business opportunity exists.
- A human decision owner is identified or explicitly marked unknown.

## Agent workflow

1. Classify the work as project/product, feature, improvement, or bug.
2. Reuse supplied facts and inspect authorized evidence before asking questions.
3. Maintain a ledger of confirmed facts, evidence, decisions, assumptions, risks, and open questions.
4. Ask one to three high-impact questions at a time.
5. Challenge vague outcomes, solution-first framing, scope expansion, and untestable success.
6. Draft early using [the intent template](intent-template.md).
7. Evaluate semantic completeness and type-specific evidence.
8. Present readiness, blockers, accepted risks, and deferred questions.
9. Wait for `Approve`, `Revise`, or `Pause`.

## Questions that deserve priority

- What problem or opportunity triggered this now, and what evidence supports it?
- Who experiences the problem, and who decides whether the outcome is acceptable?
- What observable condition would be different if the work succeeds?
- What is included, excluded, and required to remain unchanged?
- What constraints, dependencies, data sensitivity, permissions, compliance, or risk boundaries matter?
- Which unknown could materially change scope, acceptance, security, or feasibility?

| Type | Additional evidence |
|---|---|
| Project/product | Strategic purpose, users, opportunity, capabilities, success signals |
| Feature | User need, expected behavior, primary/edge/failure scenarios |
| Improvement | Current baseline, measurable delta, invariants, regression boundary |
| Bug | Observed vs expected behavior, impact, reproduction, environment, evidence |

## Exit gate

Recommend `READY FOR HUMAN REVIEW` only when the problem, affected users or systems, outcome, scope, non-goals, success, constraints, and critical unknowns are clear. Explicit human approval creates `APPROVED — READY FOR SPEC`.

## Prohibited actions

Do not select architecture, prescribe an implementation, generate `spec.md`, break work into tasks, or write code. Record solution ideas separately as considerations for the specification workshop.
