# Improvement planning

Build an evidence-first plan for an approved performance, reliability, UX, quality, cost, or operational delta.

## Sequence

1. verify the baseline and measurement conditions;
2. add missing instrumentation and a reproducible benchmark/eval;
3. define invariants and regression thresholds;
4. isolate the smallest change surfaces and experiments;
5. implement candidate changes in safe parallel lanes when comparison remains valid;
6. compare before/after under equivalent conditions;
7. integrate, canary, monitor, and roll back on threshold breach.

## Require

- exact baseline evidence and target from the specification;
- affected files/symbols and plausible bottleneck evidence;
- permitted tradeoffs and cost transfer;
- parallel experiments that do not corrupt shared results;
- verification of unchanged semantics, permissions, data, APIs, quality, and user behavior;
- decision rule for accepting, rejecting, or revising the change.

Do not plan optimization from intuition alone or claim delivery acceleration without accounting for measurement and review.
