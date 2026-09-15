# Evals and Readiness Gates

## Why evaluate artifacts

Evals make the quality bar repeatable. They do not replace judgment or approval. Use deterministic checks and semantic evaluation together.

## Evaluation layers

| Layer | Detects | Example |
|---|---|---|
| Structural | Missing headings, malformed IDs, broken links, dependency cycles | Script/linter |
| Semantic | Ambiguity, contradictions, untestable requirements, unsafe delegation | Model or expert rubric |
| Evidence | Whether claims are supported and verification is feasible | Source/repository inspection |
| Adversarial | Scope expansion, tenant leakage, prompt injection, unsafe fallback | Challenge cases |
| Human | Whether the artifact reflects intent and acceptable tradeoffs | Explicit review and approval |

## Readiness thresholds

| Stage | Threshold | Additional rule |
|---|---:|---|
| Intent | 85/100 | Every critical dimension ≥ 3/4; no material blocker |
| Specification | 90/100 | No unapproved material decision; mandatory behavior is testable |
| Planning | 90/100 | No cycles/unsafe allocations; requirement and evidence coverage complete |

A high score cannot override an automatic failure or missing human approval.

## Intent rubric

Score problem/evidence, users/impact, outcome, scope/non-goals, success, constraints, assumptions/dependencies, open decisions, and type-specific evidence. Automatic failures include invented facts, a giant generic questionnaire, silent solution selection, self-approval, or progression into specification.

## Specification rubric

Score intent fidelity, behavioral completeness, atomic requirements, architecture decisions, tenancy, stack, identity, data, interfaces, security/privacy, AI design, quality/operations, acceptance, traceability, and approval integrity. Automatic failures include starting from unapproved intent, silently selecting material design, omitting relevant tenant/security/AI risks, self-approval, or generating implementation work.

## Planning rubric

Score approved-input fidelity, verified baseline, decomposition, dependencies, critical path, parallel safety, task readiness, engineer-agent allocation, supervision, traceability, tests/evals, integration, rollout/rollback, and approval integrity. Automatic failures include mutating the project, invented paths/capacity, conflicting writers, unbounded unattended work, self-approval, or implementation.

## Eval cases for the skills

Maintain 20–50 representative historical cases across project creation, ambiguous features, measurable improvements, bugs, multi-tenancy, identity, AI agents and routing, migrations, incomplete repositories, contradictory evidence, unsafe parallelization, and cases that should stop or return upstream. Add production incidents and agent failures as permanent regression cases.

## Artifact regression policy

Changes to skills, prompts, models, routers, hooks, policies, templates, or graders should run the relevant suite. Compare gate correctness, factuality, assumption labeling, question quality, decision coverage, traceability, unsafe attempts, human effort, cost, and latency.

## Readiness report format

```markdown
Status: NOT READY | READY FOR HUMAN REVIEW
Score: NN/100
Blocking gaps: [...]
Assumptions requiring validation: [...]
Accepted risks: [...]
Deferred noncritical questions: [...]
Automatic failures: None | [...]
Recommendation: Approve | Revise | Pause
```
