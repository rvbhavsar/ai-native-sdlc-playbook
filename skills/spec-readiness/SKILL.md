---
name: spec-readiness
description: Transform an approved intent.md into a detailed, technically grounded, human-approved spec.md through an adaptive specification workshop. Use when defining a project, product, feature, improvement, or bug after intent approval; evaluating specification readiness; or deciding architecture, tenancy, technology stack, agent design, LLM strategy, integrations, data, security, quality, and acceptance before implementation planning. Never progress to plan.md, tasks, or code without a separate downstream workflow after explicit specification approval.
---

# Specification Workshop and Readiness

Convert approved intent into a precise product, behavioral, technical, and quality contract. Produce `spec.md`, not an implementation plan.

## Enforce the two human gates

- Require an approved `intent.md`. Accept missing approval metadata only when the user explicitly confirms that the supplied intent is the approved baseline. Otherwise stop and request intent approval.
- Treat the human as decision owner. Research, compare, recommend, challenge, and draft; do not silently make material product or architecture decisions.
- Never mark the specification approved without an explicit human statement approving the exact version.
- After any material post-approval change, return the specification to `Draft` and require renewed approval.
- Stop at `APPROVED — READY FOR PLAN`. Do not create `plan.md`, tasks, estimates, code, infrastructure, migrations, or production changes.

## Run the workshop

1. **Validate the input.** Read the complete intent and its approval evidence. Identify project/product, feature, improvement, or bug. Preserve its scope, non-goals, success conditions, accepted risks, and unresolved items.
2. **Load the standard.** Read [references/spec-standard.md](references/spec-standard.md), [references/interview-method.md](references/interview-method.md), [references/readiness-rubric.md](references/readiness-rubric.md), and exactly one type guide:
   - Project/product: [references/project.md](references/project.md)
   - Feature: [references/feature.md](references/feature.md)
   - Improvement: [references/improvement.md](references/improvement.md)
   - Bug: [references/bug.md](references/bug.md)
3. **Load technical guidance only when applicable.** Read [references/architecture-decisions.md](references/architecture-decisions.md) for project architecture or a material architecture delta. Also read [references/ai-systems.md](references/ai-systems.md) when the system uses agents, LLMs, model routing, tools, knowledge, memory, or AI-generated actions.
4. **Inspect before asking.** Read relevant project instructions, repository structure, existing specifications, architecture records, schemas, contracts, tests, and configuration. Use read-only inspection; do not alter the system. Use authoritative primary sources for time-sensitive technology facts when research is needed, and identify sourced fact versus recommendation.
5. **Build the specification ledger.** Keep approved intent, confirmed system facts, inherited decisions, constraints, proposed decisions, human decisions, assumptions, contradictions, accepted risks, and open questions separate.
6. **Interview adaptively.** Ask one to three high-impact questions per turn. Resolve behavior and risk before cosmetic or low-reversibility detail. Present concise options, evaluation criteria, recommendation, and tradeoffs for material choices. Do not repeat facts or present a giant questionnaire.
7. **Draft incrementally.** Use the matching template from `assets/templates/`. Mark information `Unknown`, `Deferred`, or `Not applicable — [reason]` rather than inventing it. Share checkpoints when a decision changes scope, architecture, cost, risk, or acceptance.
8. **Specify testably.** Give atomic requirements stable identifiers such as `FR-001`, `BR-001`, `DR-001`, `IR-001`, `SEC-001`, `NFR-001`, `AI-001`, `OBS-001`, and `AC-001`. Use mandatory language only for actual requirements. Link acceptance evidence back to requirements and approved intent outcomes.
9. **Evaluate.** Apply the semantic rubric. When a local file exists, run `python3 scripts/evaluate_spec.py <path> --type <type>` for structural and identifier checks. The script cannot verify truth, feasibility, or human approval.
10. **Close only material gaps.** Continue until additional answers would no longer change behavior, scope, architecture, security, data handling, operations, acceptance, or material cost. Let the user explicitly defer noncritical matters or accept documented risks.
11. **Present the review gate.** Deliver the complete `spec.md`, decision register, readiness report, remaining blockers, assumptions requiring validation, and accepted risks. Ask the human to choose `Approve`, `Revise`, or `Pause`.
12. **Record approval.** On explicit approval, record the version and approval evidence, set the state to `APPROVED — READY FOR PLAN`, and stop.

## Apply architecture by level

- **Project/product spec:** establish the complete architecture baseline, including tenancy, isolation, stack, languages, frameworks, services, data, identity, integrations, agent runtime, harness, model strategy, LLM router, knowledge/memory/files, HIL, infrastructure, security, observability, evals, reliability, and cost controls.
- **Feature spec:** inherit the parent baseline and document behavioral requirements plus architecture, data, permission, integration, AI, and operational deltas.
- **Improvement spec:** inherit the baseline and specify the measurable delta, invariants, affected architecture, benchmark conditions, and regression boundary.
- **Bug spec:** inherit the baseline and specify restored behavior, evidence, affected conditions, safety/containment, verified or suspected cause status, and regression coverage.

Do not reopen inherited decisions unless the current change requires an exception. Record any exception as a proposed decision requiring human approval.

## Distinguish spec from plan

| Include in spec.md | Defer to plan.md |
|---|---|
| Required behavior and acceptance | Files and code changes |
| Selected architecture and decision rationale | Implementation sequence |
| Technology constraints and approved stack | Task breakdown and estimates |
| Data, interfaces, security, failure behavior | Concrete migrations and commands |
| Deployment/rollout requirements | Execution steps |
| Tests and eval outcomes required | Test implementation details |

## Gate states

- `NOT READY`: critical gap, contradiction, unapproved material decision, or score below threshold.
- `READY FOR HUMAN REVIEW`: specification passes the readiness rubric but remains unapproved.
- `APPROVED — READY FOR PLAN`: exact specification version explicitly approved by the human.

## Evaluate the skill

Use [evals/cases.json](evals/cases.json) and [evals/grader.md](evals/grader.md) when testing or revising this skill. Starting from unapproved intent, self-approval, silently selecting architecture, bypassing tenant/security decisions, or creating implementation artifacts are automatic failures.
