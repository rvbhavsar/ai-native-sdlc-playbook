# Improvement intent

Use when an existing behavior works but should become faster, clearer, cheaper, safer, more reliable, more accessible, or otherwise better without becoming a materially new capability.

## High-leverage questions

- What happens today, for whom, and where is the friction or limitation?
- What baseline evidence exists: time, error rate, cost, user feedback, support volume, reliability, or another signal?
- What precise delta should improve and why does it matter now?
- Which existing behavior, contract, permissions, ranking, data, or user path must remain unchanged?
- How will the delta be measured or observed, over which population and window?
- What tradeoff is acceptable, and what degradation would be a regression?
- Does the improvement change outputs, only quality attributes, or both?
- Which users, environments, or cases are excluded from this change?

## Required structure

Use `assets/templates/improvement-intent.md`. Include:

- context and evidence;
- affected users or system area;
- current experience and baseline;
- problem/limitation;
- desired improvement and measurable delta;
- scope, non-goals, preservation contract, and regression boundary;
- success/acceptance, constraints, assumptions, dependencies, and open questions;
- human approval.

If the requested delta creates a new user capability or materially different workflow, reclassify it as a feature with the user's agreement.

## Specific failure modes

- “Optimize,” “modernize,” or “improve UX” without a baseline or observable delta.
- Performance target without workload, percentile, or measurement conditions when those matter.
- Improvement achieved by breaking compatibility or changing semantics.
- Proxy metric substituted for user or business value without explanation.
