# Bug-fix planning

Plan the smallest safe restoration of approved behavior while keeping cause evidence honest.

## Sequence

1. reproduce or capture the failing condition;
2. contain security, tenant, financial, destructive, or customer-impact risk when required by the specification;
3. create a failing regression test/eval where practical;
4. verify root cause or define a bounded investigation task;
5. implement the smallest safe correction within approved architecture;
6. run focused and neighboring regressions;
7. detect and remediate affected data or external effects;
8. roll out, observe, and roll back when gates fail.

## Parallelize carefully

Research, affected-scope analysis, test construction, and remediation planning may run in separate worktrees when they have stable evidence and non-conflicting write sets. Do not run competing speculative fixes against the same mutable surface.

## Require

- observed/reported/suspected cause separation;
- exact affected surfaces or a discovery task;
- containment and escalation ownership;
- regression boundary and evidence;
- data repair, customer notification, audit, rollback, and recovery when applicable.

Return to specification if investigation changes expected behavior, scope, security obligations, architecture, or acceptance.
