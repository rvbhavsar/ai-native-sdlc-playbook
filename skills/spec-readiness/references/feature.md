# Feature specification

Use the feature template for a new capability inside an existing product. Inherit the approved project architecture and state only deltas or exceptions.

## Resolve

- initiating actor, preconditions, primary/alternate/failure flows, end state, and side effects;
- atomic functional and business requirements;
- roles, permissions, tenant boundaries, and administrative behavior;
- data input/output, ownership, validation, lifecycle, and audit;
- integration, event, notification, and failure contracts;
- state transitions, concurrency, retries, cancellation, and reversibility;
- architecture, AI, operational, rollout, and cost impact;
- acceptance scenarios, evals, and preservation of existing behavior.

## Ask high-impact questions

- What must be true immediately before and after the feature succeeds?
- Which actor may perform each action, and what must be denied?
- What data or external systems change, and what happens during partial failure?
- Which edge conditions affect trust, money, privacy, tenant isolation, or recoverability?
- Does the feature follow the parent stack and architecture? If not, why is an exception necessary?
- What proves the user need is met without regressing current behavior?

## Do not approve when

- only the happy path is specified;
- UI elements stand in for behavioral requirements;
- permissions, data side effects, failures, or acceptance are implicit;
- the feature changes foundational architecture without an approved decision.
