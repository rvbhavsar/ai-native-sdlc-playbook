# Human-in-the-Loop Governance

## Control model

Human control means informed, version-specific authority—not passive observation. The system must show what is known, proposed, assumed, risky, and blocked before requesting a decision.

## Rights of the human decision owner

At every stage, the human may:

- correct facts and interpretations;
- request evidence or alternatives;
- accept, reject, or modify recommendations;
- defer a noncritical question with a recorded consequence;
- accept a documented risk when authorized;
- reduce agent autonomy or require additional review;
- approve, revise, or pause the stage.

## Agent obligations

The agent must:

- distinguish facts, observations, reports, proposals, and assumptions;
- ask focused questions only when the answer could materially change the artifact;
- recommend a choice when useful, with criteria and tradeoffs;
- surface contradictions and uncertainty instead of smoothing them over;
- identify what approval authorizes and what it does not;
- preserve approval evidence and exact version bindings;
- stop at the stage boundary.

## Approval record

| Field | Requirement |
|---|---|
| Artifact | Name and path |
| Version | Exact semantic/document version |
| Upstream baseline | Exact approved source version(s) |
| Repository baseline | Required for planning approval |
| Approver | Named human or authorized role |
| Statement | Explicit approval of the exact artifact |
| Date | Timestamp or recorded date |
| Accepted risks | IDs and authority |

Silence, continuation, or an agent readiness score is not approval.

## Escalation triggers

Stop and request a human decision for:

- new externally visible behavior or a scope change;
- architecture, tenancy, security, privacy, compliance, or data exceptions;
- expanded AI agency, tool permissions, memory, or reduced review;
- shared contracts, identity/authorization, sensitive migrations, or production access;
- destructive, irreversible, external, or customer-impacting actions;
- insufficient evidence to assess risk or acceptance.

## Minimal approval UX

Every gate should show what changed, decisions being approved, remaining assumptions and risks, score and blockers, exact artifact version, and three choices: `Approve`, `Revise`, or `Pause`.

## Automation never inherits authority

Approval of intent does not approve the specification. Approval of the specification does not approve the plan. Approval of the plan does not authorize merge, deploy, data mutation, external communication, or production access. Each requires its own workflow and policy.
