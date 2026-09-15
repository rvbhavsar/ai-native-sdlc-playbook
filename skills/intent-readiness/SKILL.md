---
name: intent-readiness
description: Interview, challenge, structure, and evaluate a rough product, project, feature, improvement, or bug request into a concise intent.md that is ready for specification. Use when a user wants to clarify an idea, define a change, improve a ticket, capture intent before spec.md, or assess whether requirements are mature enough to enter specification. Keep the human in control and never advance past the intent approval gate without explicit approval.
---

# Intent Discovery and Readiness

Turn incomplete requests into an accurate, bounded, testable `intent.md`. Capture why and what; defer solution design and implementation detail to `spec.md` and later artifacts.

## Non-negotiable human-control contract

- Treat the user as the decision owner. Interview, challenge, summarize, recommend, and evaluate; do not silently decide material product choices.
- This skill stops at the intent gate. Never create `spec.md`, an implementation plan, tasks, or code; a downstream specification workflow may begin only after explicit human approval.
- Never mark the approval field yourself. Record approval only after an explicit user statement such as “approved” or “this intent is correct.”
- Label every material inference as an assumption. Do not convert an assumption into a fact through repetition.
- Let the user skip, defer, override, or accept a documented risk. Preserve that decision in the intent.
- Do not claim readiness while a critical unknown could change the problem, user, outcome, scope, acceptance, security posture, or affected data.

## Run the workflow

1. **Orient.** Reuse facts already provided. Determine the work type: `project`, `feature`, `improvement`, or `bug`. Ask only if the classification changes the interview materially.
2. **Load the playbook.** Read [references/interview-method.md](references/interview-method.md), [references/readiness-rubric.md](references/readiness-rubric.md), and exactly one type guide:
   - Project/product: [references/project.md](references/project.md)
   - Feature: [references/feature.md](references/feature.md)
   - Improvement: [references/improvement.md](references/improvement.md)
   - Bug: [references/bug.md](references/bug.md)
3. **Build the evidence map.** Separate confirmed facts, user decisions, evidence, assumptions, and unresolved questions. Inspect provided artifacts or the authorized codebase when they can answer factual questions, but do not modify anything.
4. **Interview adaptively.** Ask one to three high-leverage questions per turn. Select questions by decision impact, not template order. Challenge vague language, solution-first framing, unbounded scope, and untestable success. Do not repeat answered questions.
5. **Checkpoint.** After each meaningful round, briefly reflect the current understanding, decisions, assumptions, and next largest gap. Give the user a chance to correct course.
6. **Draft early.** Once the core problem, user, outcome, and boundary are reasonably clear, create or update the matching template from `assets/templates/`. Keep it concise; use `Unknown`, `Deferred`, or `Not applicable` honestly instead of inventing content.
7. **Evaluate.** Apply the semantic readiness rubric. If a local intent file exists, also run `python3 scripts/evaluate_intent.py <path> --type <type>` for structural checks. A script result is never human approval.
8. **Close gaps.** Ask only questions needed to resolve critical gaps or materially improve the intent. If a metric cannot reasonably be quantified, define an observable behavior or decision test instead.
9. **Present the gate.** Show the final draft plus a compact readiness report: score, blocking gaps, accepted risks, deferred noncritical questions, and recommendation.
10. **Wait for the human.** Ask for one of: `Approve`, `Revise`, or `Pause`. On approval, update only the approval record and state that the intent is ready to hand to specification. Do not generate the specification unless separately requested.

## Keep intent separate from solution

Include implementation details only when they are true constraints or already-approved decisions. Otherwise move suggestions into a clearly labeled `Design considerations for spec.md` note outside the canonical intent.

| Belongs in intent.md | Belongs later |
|---|---|
| Problem, affected people, evidence | Architecture and component design |
| Desired outcome and observable success | API/schema/file design |
| Scope, non-goals, and unchanged behavior | Implementation sequence and estimates |
| Constraints, dependencies, risks | Detailed test cases and code tasks |
| Assumptions and open decisions | Vendor/tool selection unless constrained |

## Readiness rule

Recommend `READY FOR HUMAN APPROVAL` only when all of these hold:

- Semantic score is at least 85/100.
- Every critical dimension scores at least 3/4.
- No unresolved blocker can materially alter scope, acceptance, security, compliance, permissions, or data handling.
- The applicable type-specific minimum evidence is present.

Declare `APPROVED — READY FOR SPEC` only after the user explicitly approves. Otherwise use `NOT READY` or `READY FOR HUMAN APPROVAL`.

## Output standard

Return or save:

1. A concise canonical `intent.md` based on the matching template.
2. A readiness report with status, score, blockers, assumptions requiring validation, accepted risks, and deferred questions.
3. A human approval prompt with the three decisions: `Approve`, `Revise`, or `Pause`.

Do not expose the full internal question bank or scoring deliberation unless the user asks. Ask natural questions in plain language.

## Evaluate the skill itself

Use [evals/cases.json](evals/cases.json) and [evals/grader.md](evals/grader.md) when testing or revising this skill. HIL violations, invented facts, giant questionnaires, or unauthorized progression to specification are automatic failures.
