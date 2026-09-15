# Philosophy and Principles

## The problem this operating system solves

AI accelerates code generation, but it also amplifies unclear intent, unexamined architecture, scope expansion, inconsistent decisions, review debt, and unsafe automation. The objective is not to generate more code. It is to increase the rate of verified outcomes while keeping humans in control of consequential choices.

The process treats development as an evidence-producing control loop:

- Conversation discovers intent.
- Artifacts preserve decisions and boundaries.
- Evals expose ambiguity, contradictions, and regressions.
- Human gates authorize movement and risk.
- Agents perform bounded work with feedback loops.
- New evidence can reopen an earlier artifact instead of being hidden downstream.

## Core principles

### 1. Outcome before solution

Start with the problem, affected people, desired outcome, and proof of success. A proposed implementation is evidence or a constraint only when deliberately selected.

### 2. Progressive commitment

| Stage | Commitment |
|---|---|
| Intent | Problem, users, outcome, scope, non-goals, success |
| Specification | Behavior, architecture, technology, data, security, AI, quality |
| Planning | Sequence, dependencies, work units, ownership, orchestration, evidence |

### 3. Human control by design

HIL is not a final rubber stamp. The human can correct assumptions, choose between material options, accept or reject risks, defer questions, set autonomy, and pause the workflow at every stage.

### 4. Artifacts are contracts

Each Markdown artifact is both human-readable and machine-actionable. Stable identifiers, explicit state, decisions, assumptions, links, and evidence make handoffs auditable across people, agents, and runtimes.

### 5. Separate intelligence from enforcement

Skills provide judgment and guidance. Deterministic controls enforce non-negotiable rules such as protected paths, secret scanning, mandatory checks, approval boundaries, and production access.

### 6. Traceability over memory

Every mandatory intent outcome should appear in the specification. Every mandatory specification requirement should map to planned work and verification. Important decisions must not depend on a model remembering a conversation.

### 7. Parallelize independent work, not uncertainty

Parallel work begins only after dependencies, ownership, write boundaries, review capacity, integration capacity, and environments are understood.

### 8. Evidence closes every loop

A task is not complete because an agent says it is. Completion requires defined evidence: tests, evals, screenshots, logs, inspections, migration proofs, security checks, or operational signals appropriate to the risk.

### 9. Vendor-neutral by default

Canonical artifacts and policies belong to the organization. Claude, Codex, Gemini, local models, cloud agents, and CI workers are execution runtimes—not the lifecycle architecture.

### 10. Reversibility earns autonomy

Bounded, isolated, reversible, strongly tested work can receive greater autonomy. Shared-contract, identity, tenant, sensitive-data, production, destructive, and irreversible work requires tighter supervision.

## What should be automated

Automate repeatable cognitive and mechanical work:

- artifact intake, classification, and completeness checks;
- adaptive interviews and decision comparison;
- repository and documentation inspection;
- traceability and dependency analysis;
- test/eval generation and execution;
- evidence collection and readiness scoring;
- bounded coding, review preparation, and handoff reports;
- detection of drift between approved artifacts and implementation.

Do not automate away accountability. Humans retain authority over material product direction, architecture exceptions, data and security risk, agent autonomy, staffing, release policy, and production boundaries.

## Success measure

The primary measure is the sustained rate of approved, verified, safely integrated outcomes subject to human review capacity—not agent utilization, generated code, or raw concurrency.
