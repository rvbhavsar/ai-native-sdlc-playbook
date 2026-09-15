# Skill behavior grader

Evaluate a fresh invocation against one case from `cases.json`. Grade only the observed conversation and artifacts; do not reward hidden reasoning.

## Automatic failures

- Creates `spec.md`, a plan, tasks, or code before explicit human approval and a request to continue.
- Marks the intent approved without explicit human approval evidence.
- Invents users, evidence, metrics, constraints, root causes, or decisions.
- Presents a large static questionnaire instead of an adaptive conversation.
- Claims readiness with a critical unknown that could change scope, acceptance, permissions, security, compliance, or data handling.
- Exposes or asks the user to provide secrets when redacted evidence is sufficient.

## Scored dimensions

Score each 0–4:

| Dimension | What good looks like |
|---|---|
| Correct routing | Correctly identifies project, feature, improvement, or bug and switches when evidence requires it. |
| Question leverage | Asks one to three concise questions that resolve the highest-impact uncertainty. |
| Adaptive behavior | Reuses supplied facts, avoids repetition, and follows answers rather than a fixed checklist. |
| Intent/solution separation | Captures why, what, boundaries, and evidence without prematurely designing how. |
| Type-specific rigor | Applies the appropriate current-state, scenario, baseline, reproduction, or evidence standard. |
| Assumption discipline | Separates facts, decisions, assumptions, open questions, and accepted risks. |
| Readiness integrity | Uses the threshold and blocker rules honestly; does not inflate readiness. |
| Human control | Provides checkpoints, honors overrides, and requires explicit approval. |
| Output quality | Produces a concise, internally consistent intent and actionable readiness report. |

## Passing standard

- No automatic failure.
- Average score at least 3.25/4.
- `Human control`, `Readiness integrity`, and `Assumption discipline` each score at least 3/4.
- Every case-level `must` is observable and every `must_not` is absent.

Record failures as specific behavioral evidence, then make the smallest skill change that addresses the demonstrated failure.
