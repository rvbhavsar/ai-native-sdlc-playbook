# AI and agent-system specification

Apply when the product uses LLMs, agents, tools, model routing, knowledge, memory, generated actions, or autonomous workflows.

## Agent topology and responsibility

Define:

- deterministic workflow, single agent, supervisor/workers, peer agents, or hybrid;
- responsibility and boundary of each agent;
- triggers, inputs, outputs, state, tools, and knowledge;
- permitted, approval-required, and prohibited actions;
- handoff, escalation, cancellation, retry, replay, and recovery;
- conversation, task, workflow, and durable execution state;
- how duplicate or concurrent execution is controlled.

Prefer deterministic orchestration where behavior must be predictable. Use model reasoning only where ambiguity or judgment creates value.

## Harness and orchestration

Evaluate LangGraph, OpenAI Agents SDK, Claude Agent SDK, other frameworks, or a custom runtime against actual requirements:

- durable state and checkpointing;
- tool execution and structured output;
- interrupts and human approvals;
- background, scheduled, and event-driven work;
- retries, timeouts, cancellation, idempotency, and recovery;
- agent handoffs and streaming;
- prompt/model/tool versioning;
- tracing, testing, portability, ecosystem, and operations.

Specify required capabilities before selecting the harness. Record the selection as a human-approved decision.

## Model strategy

Classify workloads before choosing models. For each workload specify:

- required quality and error tolerance;
- tool/structured-output/multimodal needs;
- context size and grounding needs;
- latency and availability objective;
- privacy, retention, residency, and provider restrictions;
- cost or token budget;
- primary model, fallback, and model-version policy;
- upgrade, regression-eval, canary, and rollback requirements.

Do not use “best model” as a requirement.

## LLM router

Define routing using explicit inputs such as task type, capability, risk, tenant configuration, region, data sensitivity, context size, latency, quality, budget, and provider health.

For each route specify:

- primary and allowed fallback models;
- whether cross-provider fallback is permitted;
- timeout, maximum attempts, and circuit breaking;
- structured-output validation and repair limit;
- context-overflow behavior;
- rate-limit and outage behavior;
- safety refusal and escalation;
- per-tenant allowlists, quotas, and budgets;
- captured model, prompt, route, usage, latency, and outcome metadata.

Routing policy must be testable and versioned.

## Tools and integrations

For every tool define:

- credential and tenant owner;
- least-privilege scopes;
- read, draft, write, send, approve, delete, or administer risk class;
- input/output contract;
- idempotency and duplicate prevention;
- timeout, retry, partial failure, compensation, and audit behavior;
- approval and escalation policy;
- protection against untrusted instructions and data exfiltration.

Approval must bind to the exact action and payload. Approval of a goal is not blanket permission for later actions.

## Knowledge, context, memory, and files

Keep these distinct:

| Capability | Specification concern |
|---|---|
| Context | What enters one execution and why |
| Knowledge | Authoritative sources, freshness, provenance, and permissions |
| Short-term memory | Workflow/conversation scope and expiry |
| Long-term memory | Write criteria, validation, ownership, retention, and correction |
| File system | Agent/private/shared ownership, access, lifecycle, and scanning |
| Retrieval | Indexing, filters, ranking, citations, and isolation |

Specify per-tenant and per-agent read/write boundaries, sharing, deletion, export, retention, sensitive-data handling, prompt-injection defenses, retrieval authorization, and cross-tenant leakage tests.

## Human-in-the-loop matrix

Classify each consequential action:

| Level | Meaning |
|---|---|
| Autonomous | Reversible, low-risk action allowed by policy |
| Notify | Execute, then inform the responsible human |
| Confirm | Obtain approval immediately before the bound action |
| Authorized role | Require a named role and recorded approval |
| Prohibited | Agent may never execute |

Define approver identity, authorization check, payload preview, approval expiry, mutation after approval, rejection path, reapproval conditions, timeout, audit evidence, emergency stop, and reversal.

## AI eval contract

Define datasets, thresholds, and release gates for applicable dimensions:

- end-to-end task success;
- groundedness and citation correctness;
- structured-output validity;
- tool choice, arguments, and permission compliance;
- routing and fallback correctness;
- tenant isolation and data leakage;
- prompt-injection and adversarial behavior;
- refusal, escalation, and HIL compliance;
- memory write/retrieval correctness;
- latency, cost, reliability, and recovery;
- regression across prompts, skills, policies, models, tools, and harness versions.

Use production incidents and corrected failures as permanent regression cases. A high-risk action without a measurable safety/HIL eval is a specification blocker.
