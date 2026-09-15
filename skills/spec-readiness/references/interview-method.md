# Agentic specification interview

## Inspect first

Before asking the user, extract answers from the approved intent and available project evidence. Do not ask the user to rediscover facts already present in code, tests, specifications, or authoritative documentation.

Start with:

- approved intent outcomes and exclusions;
- current architecture and inherited decisions;
- actors, permissions, data, integrations, and operational boundaries;
- conflicting evidence and missing decisions;
- highest-risk unknowns.

## Maintain the specification ledger

Track separately:

1. Approved intent statements.
2. Confirmed current-system facts and their source.
3. Inherited architecture decisions.
4. Hard constraints.
5. Proposed decisions awaiting a human.
6. Explicit human decisions.
7. Assumptions with validation method and owner.
8. Contradictions.
9. Blocking and non-blocking questions.
10. Accepted risks and deferred matters.

## Choose the next question

Prioritize questions using:

`priority = decision impact × uncertainty × cost of error × irreversibility`

Resolve security, tenant isolation, permissions, destructive effects, externally committed contracts, data lifecycle, and acceptance before low-risk implementation preferences.

Ask one question by default and no more than three tightly related questions per turn. Use concise choices when they reduce effort, but allow free-form correction. Do not dump the section outline as a questionnaire.

## Frame material decisions

For every material decision, present:

```markdown
### Decision: [Question]

- Why it matters: [behavior, risk, cost, or reversibility]
- Constraints: [confirmed constraints]
- Options: [2–4 credible choices]
- Recommendation: [one option and why]
- Tradeoffs: [what is gained and sacrificed]
- Human decision: Pending
```

Research uncertain or current technology claims using primary sources. Separate sourced facts from inference and recommendation. Do not manufacture precision or present preference as necessity.

## Challenge weak specifications

- **Tool-first request:** uncover required behavior and evaluation criteria before endorsing the technology.
- **“Use best practices”:** identify the applicable security, reliability, UX, or operational outcome.
- **“Make it scalable”:** establish workload, horizon, bottleneck, acceptable degradation, and cost boundary.
- **“Multi-tenant”:** specify isolation separately for runtime, database, vectors, files, memory, secrets, integrations, logs, and model context.
- **“Use the best model”:** define task, quality, latency, region, privacy, availability, and cost criteria.
- **“Fully autonomous”:** identify action risk and define approval, escalation, reversal, audit, and kill controls.
- **Inherited contradiction:** stop and ask whether to amend intent, propose an architecture exception, or narrow the spec.

## Draft and checkpoint

Draft once the primary behavior and architecture boundary are coherent. After any material decision, summarize:

- what changed;
- consequences;
- assumptions introduced or removed;
- remaining blocker.

The user may approve a recommendation in shorthand when the exact option and consequences were just presented. Do not infer approval from silence.

## Stop conditions

Stop interviewing when further answers will not materially affect behavior, scope, architecture, security, data, failure recovery, operations, acceptance, or cost. Record noncritical unknowns as deferred with owner and decision point.

Continue when reasonable answers would lead to materially different systems or tests. If the user declines, explain the consequence and allow narrowing, accepted risk when responsible, or pause.
