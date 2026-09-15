# Product Blueprint

## Product concept

Build a vendor-neutral AI SDLC workspace that guides teams from rough request to approved implementation plan. The product coordinates conversations, artifacts, decisions, evidence, evals, approvals, and downstream agent execution without making the coding runtime the system of record.

## Primary users

- Founder or product owner defining outcomes.
- Architect or senior engineer making technical decisions.
- Delivery lead orchestrating people, agents, worktrees, and gates.
- Engineer supervising bounded coding-agent sessions.
- Reviewer, security owner, or approver validating risk and evidence.

## Core product objects

| Object | Purpose |
|---|---|
| Initiative | Project, feature, improvement, or bug lifecycle |
| Artifact version | Immutable intent/spec/plan snapshot with state |
| Requirement | Stable, traceable product or system contract |
| Decision | Options, rationale, tradeoffs, owner, approval, revisit trigger |
| Assumption/risk | Visible uncertainty and disposition |
| Evidence | Source, test, eval, observation, or approval proof |
| Gate | Conditions and authority required to progress |
| Work item | Phase, enabler, epic, feature, task, or parallel group |
| Execution lane | Engineer, agent, environment, branch/worktree, autonomy, monitoring |

## Suggested user experience

1. Intake creates an initiative and classifies its type.
2. A stage agent interviews adaptively in a conversation pane.
3. A live artifact pane updates the Markdown draft.
4. A decision pane shows choices, recommendation, tradeoffs, and unresolved items.
5. An evidence pane shows sources, assumptions, evals, and traceability.
6. A gate view summarizes changes, blockers, risks, and exact approval scope.
7. Planning adds dependency, workstream, worktree, capacity, and ready-queue views.
8. Approved artifacts can be exported to a repository and passed to runtime adapters.

## Product architecture capabilities

- Artifact/version service with immutable approvals and diffing.
- Conversation orchestration with stage-specific context assembly.
- Decision and assumption ledger.
- Read-only repository and document connectors during the three stages.
- Skill registry and runtime adapter layer.
- Policy engine and deterministic action gates.
- Eval runner, benchmark store, and evidence graph.
- Requirement and dependency graph.
- Human task/approval inbox with role-based authority.
- Audit, observability, cost, and model-routing controls.

## Minimal viable product

Start with Markdown-first workspaces, adaptive interviews, versioned decisions and approvals, readiness rubrics, repository read-only inspection, end-to-end traceability, Git export/import, and explicit `Approve`, `Revise`, and `Pause` gates. Add execution orchestration only after the planning contract and authorization model are reliable.

## Product success signals

Measure reduced clarification cycles, fewer reopened decisions, requirement-to-test coverage, planning rework, review debt, escaped defects, unsafe action attempts, human approval time, and verified delivery throughput. Avoid optimizing conversation length, agent count, or generated code volume.
