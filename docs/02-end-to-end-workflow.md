# End-to-End Workflow

## Stage 1 — Intent

Begin from an idea, opportunity, project, feature, improvement, defect, or incident. The agent establishes the problem, affected people or systems, desired outcome, scope, non-goals, success evidence, constraints, assumptions, dependencies, and open decisions.

Output: an approved `intent.md`. No architecture, detailed requirements, implementation plan, or code is authorized.

## Stage 2 — Specification

Begin only from approved intent. Inspect relevant products, repositories, architecture, policies, contracts, and authoritative technology sources. Conduct a decision workshop covering behavior, acceptance, architecture, tenancy, identity, stack, data, integrations, infrastructure, security, observability, reliability, and—when applicable—agents, harnesses, models, routing, tools, memory, knowledge, HIL, evals, and cost.

Output: an approved `spec.md` with stable, testable requirements and a decision register. No implementation sequence, tasks, branches, or code is authorized.

## Stage 3 — Planning

Begin only from an approved specification and verified repository baseline. Analyze what must exist first, which foundations unlock other work, what can run concurrently, how work is decomposed, what each engineer-agent pair owns, and how work will be reviewed and integrated.

Output: an approved `plan.md` and only those child work packets that add execution value. No branch, worktree, issue, infrastructure, migration, code, or deployment is created by this stage.

## Cross-stage traceability

| Intent outcome | Specification requirements | Plan work | Verification | Release evidence |
|---|---|---|---|---|
| `OUT-001` | `FR-001`, `NFR-002` | `EN-001`, `FEAT-003` | `TEST-004`, `EVAL-002` | `GATE-006` |

Flag both requirements with no planned work/evidence and planned work with no approved requirement or operational justification.

## Feedback and exception loops

A downstream stage may expose an upstream defect. Stop, identify the contradiction, and return a focused change request to the responsible artifact; never silently reinterpret the approved contract.

- Planning discovers an infeasible isolation model: return to specification.
- Specification conflicts with an intent non-goal: return to intent.
- Repository drift changes affected surfaces but not behavior: revise and reapprove the plan.

## Extension beyond the three stages

Approved task packets may later drive bounded coding-agent sessions. Each session returns an execution report and evidence; review and integration gates determine merge readiness. Production signals, incidents, and ideas start a new intent. These extensions require separate authorization and are outside the three-stage playbook.
