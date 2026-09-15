# Operating Model

## Roles

A person may hold multiple roles, but the responsibilities remain distinct.

| Role | Accountable for |
|---|---|
| Decision owner | Product intent, material choices, risk acceptance, approvals |
| Facilitating agent | Interviewing, challenging, synthesizing, drafting, evaluating |
| Product/subject expert | User, market, process, policy, and operational truth |
| Technical owner | Architecture, feasibility, security, operability, technical decisions |
| Planning/orchestration owner | Dependencies, work design, allocation, integration flow |
| Execution agent | Bounded implementation and verification within an approved task packet |
| Reviewer/integrator | Independent review, conflict resolution, merge readiness, evidence acceptance |

## Canonical artifacts

| Artifact | Input | Output contract | Approval binds to |
|---|---|---|---|
| `intent.md` | Rough idea, problem, request, incident | Approved outcome and boundary | Intent version |
| `spec.md` | Approved intent and system evidence | Approved behavioral and technical contract | Intent + spec version |
| `plan.md` | Approved spec and verified baseline | Approved execution and verification system | Spec + plan + repository revision |

Supporting records include decision records, assumption ledgers, readiness reports, eval evidence, repository observations, and task execution reports.

## Stage contract

Every stage declares:

1. Entry criteria.
2. Inputs and authoritative sources.
3. Questions and decisions owned by the human.
4. Agent permissions and prohibited actions.
5. Required output and stable identifiers.
6. Readiness criteria and blocking conditions.
7. Explicit approval evidence.
8. Conditions that reopen the artifact.

## Decision and evidence ledger

| Category | Meaning |
|---|---|
| Confirmed | Established by an authoritative source or decision owner |
| Observed | Verified from repository, configuration, runtime, tests, or documentation |
| Reported | Supplied by a person but not independently verified |
| Proposed | Recommended choice awaiting human decision |
| Assumed | Working belief with owner, impact, and validation method |
| Deferred | Postponed with consequence and revisit point |
| Accepted risk | Known exposure accepted by an authorized human |

## Change control

| Change | Required action |
|---|---|
| Intent outcome, users, scope, non-goal, or success | Reapprove intent; reassess spec and plan |
| Architecture, tenancy, data, security, AI autonomy, interface, or acceptance | Reapprove spec; reassess plan |
| Repository baseline, dependency graph, migration, allocation, rollout, or rollback | Reapprove affected plan |
| Editorial clarification with no semantic effect | Record revision; approval may remain if policy permits |

## Automation boundary classes

| Class | Example | Default control |
|---|---|---|
| Advisory | Research, options, gap detection | Agent may proceed and report |
| Reversible artifact | Drafting Markdown, local analysis | Agent may proceed within scope |
| Isolated implementation | Worktree change with tests | Approved task packet and review |
| Shared or sensitive change | Contracts, identity, tenancy, migrations | Named supervision and integration gate |
| External or production action | Deploy, send, delete, customer data | Exact authorization plus deterministic controls |

## Operating cadence

- Ask one to three high-impact questions.
- Reflect the current understanding and unresolved decisions.
- Draft early with visible unknowns.
- Evaluate and close only material gaps.
- Present a concise readiness report.
- Ask the human to `Approve`, `Revise`, or `Pause`.
