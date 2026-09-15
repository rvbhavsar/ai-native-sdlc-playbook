# Improvement specification

Use the improvement template when existing behavior remains conceptually the same but a quality attribute or experience must improve.

## Resolve

- verified current behavior and measurement baseline;
- target delta, population/workload, conditions, and measurement window;
- functional invariants and behavior that must remain unchanged;
- affected architecture, data, integration, AI, operations, and cost;
- acceptable tradeoffs and explicit regression thresholds;
- benchmark/test environment and reproducibility;
- rollout, comparison, monitoring, rollback, and acceptance.

## Ask high-impact questions

- What verified evidence establishes the current baseline?
- What exact improvement matters to users or the business, under which conditions?
- Which semantics, ranking, permissions, data, APIs, or workflows must not change?
- Which tradeoffs are permitted, and what degradation is an automatic failure?
- Does the improvement require a stack or architecture exception?
- How will the before/after difference be measured reliably?

## Do not approve when

- “faster,” “better,” “simpler,” or “more scalable” lacks a measurable or observable delta;
- the benchmark conditions make the target meaningless;
- the change can pass by breaking compatibility or shifting cost elsewhere;
- regression and rollback are undefined.
