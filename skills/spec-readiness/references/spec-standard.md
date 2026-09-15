# Canonical specification standard

Build `spec.md` as a product, behavioral, technical, and quality contract. Keep it human-readable and machine-actionable.

## Canonical sections

Use the applicable template and retain these concerns. Mark an irrelevant section `Not applicable — [reason]` instead of silently omitting it.

1. **Metadata and approval state** — type, owner, intent, parent spec, version, and exact approval evidence.
2. **Intent traceability** — approved outcome, scope, non-goals, success, and any contradiction discovered.
3. **System context** — current system, boundary, components, external actors, and inherited decisions.
4. **Actors, roles, and permissions** — who may see, initiate, change, approve, reverse, or administer behavior.
5. **Workflows and states** — trigger, preconditions, primary path, alternate path, failure/recovery, end state, and side effects.
6. **Requirements** — functional, business, data, integration, security, AI, operational, and non-functional requirements.
7. **Architecture** — approved target architecture and technical decisions at the level appropriate to the work type.
8. **Quality contract** — acceptance scenarios, tests, evals, performance, reliability, observability, rollout, rollback, and regression boundaries.
9. **Decision record** — inherited, approved, proposed, rejected, and deferred decisions with rationale and tradeoffs.
10. **Assumptions, dependencies, risks, and open decisions** — kept distinct and owned.
11. **Traceability and human approval** — map intent to requirements to verification, then require approval of the exact version.

## Requirement language

- Use `shall` for mandatory, testable behavior.
- Use `should` only for a deliberate recommendation whose absence does not fail acceptance.
- Avoid `may` unless it describes an explicit permission or optional behavior.
- Make every mandatory requirement atomic, unambiguous, feasible, and verifiable.
- State actor, condition, required behavior, observable result, and relevant failure behavior.
- Avoid design detail inside a behavioral requirement unless that detail is an approved constraint.

## Identifier families

| Prefix | Requirement family |
|---|---|
| `FR` | Functional behavior |
| `BR` | Business rule |
| `DR` | Data ownership, validation, retention, or lifecycle |
| `IR` | Interface or integration contract |
| `SEC` | Security, privacy, isolation, or authorization |
| `NFR` | Performance, scale, reliability, accessibility, or portability |
| `AI` | Agent, model, tool, memory, routing, or HIL behavior |
| `OBS` | Logs, metrics, traces, audit, alerting, or support diagnostics |
| `AC` | Acceptance or evaluation scenario |
| `DEC` | Material technical or product decision |

Keep identifiers stable while revising. Deprecate rather than silently repurpose an identifier that has already been reviewed.

## Traceability

Map each approved intent outcome to one or more requirements and each critical requirement to acceptance evidence. Flag:

- intent outcomes with no requirement;
- requirements with no approved reason;
- critical requirements with no test/eval;
- acceptance scenarios that do not verify a requirement.

## Existing-system evidence

For existing products, distinguish:

- **Observed:** verified from code, configuration, tests, runtime evidence, or authoritative documentation.
- **Reported:** stated by a user or stakeholder but not independently verified.
- **Proposed:** a new behavior or decision awaiting approval.
- **Assumed:** necessary working belief with a validation path.

Never present a guessed current architecture as observed fact.

## Decision depth

Keep concise decisions in `spec.md`. Recommend a separate ADR only when rationale is substantial, consequences span multiple specs, or reversal is expensive. Do not create extra ADR files unless the user requests them; link to existing ADRs when available.

## Version discipline

Increment the version for a reviewable material change. A change is material if it affects behavior, scope, data, permissions, architecture, security, cost boundary, operations, acceptance, or an approved decision. Reset approval to pending after any material change.
