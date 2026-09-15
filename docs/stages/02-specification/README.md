# Stage 2 — Specification Workshop

## Purpose

Transform an approved intent into a detailed, testable product, behavioral, system, and technical contract. This is where the team deliberately selects architecture, tenancy, languages, frameworks, infrastructure, data, identity, and AI-system design.

## Entry

- The exact `intent.md` version is explicitly approved.
- Critical intent blockers are closed or consciously accepted by an authorized human.
- Relevant system, repository, policy, and architecture sources are available or their absence is recorded.

## Agent workflow

1. Preserve intent outcomes, scope, non-goals, constraints, risks, and approval evidence.
2. Inspect existing repositories, contracts, schemas, tests, architecture records, and policies before interviewing.
3. Separate inherited facts from proposed and newly approved decisions.
4. Resolve behavior and risk before cosmetic design or low-impact preferences.
5. Present material choices with criteria, recommendation, alternatives, and tradeoffs.
6. Assign stable identifiers to atomic requirements and decisions.
7. Connect acceptance evidence to requirements and intent outcomes.
8. Evaluate readiness and present the exact draft for human approval.

## Required decision domains

Apply proportionally; `Not applicable — [reason]` is valid.

| Domain | Questions to resolve |
|---|---|
| Product behavior | Journeys, roles, states, rules, failure behavior, edge cases |
| Architecture | Boundaries, components, communication, deployment shape, build vs buy |
| Tenancy | Single/multi-tenant model, isolation, lifecycle, regional/data boundaries |
| Stack | Languages, frameworks, runtime, packages, monorepo/multi-repo, compatibility |
| Identity | Authentication, authorization, organizations, roles, admin, service identity |
| Data | Ownership, schemas, retention, residency, migration, deletion, recovery |
| Interfaces | APIs, events, webhooks, integrations, versioning, idempotency, failures |
| Infrastructure | Environments, compute, storage, network, secrets, CI/CD, observability |
| Security/quality | Threats, abuse, privacy, accessibility, performance, resilience, SLOs |
| AI systems | LLMs, agents, harness, router, tools, knowledge, memory, HIL, evals, cost |

## Architecture decision standard

For every material choice, record the decision and status, context and drivers, options, recommendation, rationale, tradeoffs, human evidence, consequences, and revisit trigger.

## Exit gate

Recommend `READY FOR HUMAN REVIEW` only when mandatory behavior is testable, material architecture and risk decisions are approved, acceptance covers failure and quality, and critical unknowns are closed. Explicit approval creates `APPROVED — READY FOR PLAN`.

## Prohibited actions

Do not choose material architecture silently, invent facts, create `plan.md`, assign engineers, define branches/worktrees, modify repositories, or implement the design.
