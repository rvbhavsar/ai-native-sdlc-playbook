# Agent and Skill Orchestration

## Canonical architecture

Keep organizational logic independent of execution vendors.

| Layer | Responsibility |
|---|---|
| Artifacts | Intent, spec, plan, decisions, evidence, approvals |
| Skills | Reusable interview, architecture, security, quality, planning behavior |
| Orchestrator | Stage state, context assembly, agent routing, checkpoints |
| Policy/hooks | Deterministic permissions, protected surfaces, required checks |
| Runtime adapters | Codex, Claude, Gemini, local/cloud agents, CI workers |
| Observability/evals | Traces, quality, regression, safety, cost, latency |

## Stage agents

### Intent facilitator

Inputs: rough request and evidence. It interviews, challenges, drafts `intent.md`, evaluates readiness, and stops at human approval.

### Specification facilitator

Inputs: approved intent plus product/system evidence. It compares and records material design choices, drafts `spec.md`, evaluates readiness, and stops at human approval.

### Planning orchestrator

Inputs: approved spec plus verified repository baseline. It decomposes, builds dependencies, models safe parallelism, drafts `plan.md` and necessary task packets, evaluates readiness, and stops before implementation.

## Specialist agents

Invoke only when bounded and useful: researcher, repository analyst, architect, security/privacy reviewer, data/tenancy/identity reviewer, AI safety/eval reviewer, dependency/capacity analyst, and independent traceability verifier. The stage owner synthesizes results; specialist output is never implicit approval.

## Context contract

Every invocation should receive exact artifact versions and IDs, explicit task and non-goals, authorized sources/tools, permissions and prohibited actions, output schema, pass conditions, stop/escalation triggers, and human decision points.

## Model and LLM routing

| Work | Routing consideration |
|---|---|
| Classification/extraction | Low cost, structured-output reliability |
| Ambiguous interview | Strong reasoning and conversational calibration |
| Architecture/security | High reasoning quality, grounding, independent review |
| Repository analysis | Large context, tool use, code understanding |
| Eval/grading | Independence from the drafting model where practical |
| Sensitive content | Approved provider, retention, region, and data controls |

Define fallback behavior, version pinning, budgets, timeouts, retries, and the outcome when no approved model satisfies policy.

## Harness requirements

The harness controls session state, context budgets, tool permissions, checkpoints, cancellation, retries, structured outputs, redaction, audit logging, and evidence capture. It must prevent a stage agent from crossing its mutation or approval boundary.

## Skill quality contract

Each skill should include a precise trigger, HIL rules, stage entry/exit criteria, adaptive interview method, type guides, canonical templates, readiness rubric, positive/negative/edge/HIL eval cases, and explicit prohibited actions.

## Execution handoff

After plan approval, a separate implementation orchestrator may create authorized branches/worktrees and dispatch ready task packets. Each agent returns a structured execution report with base revision, changes, tests/evals, evidence, deviations, residual risks, and next gate. That future workflow must never infer authority from planning approval alone.
