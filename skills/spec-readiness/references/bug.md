# Bug specification

Use the bug template to define restored behavior and regression coverage. Do not require a confirmed root cause before specifying the behavioral contract, but keep cause status honest.

## Resolve

- approved defect intent, impact, observed/expected behavior, environment, reproduction, and evidence;
- containment or customer-safety requirements;
- restored behavior and unchanged related behavior;
- verified root cause, suspected causes, or investigation required—clearly distinguished;
- affected components, data, permissions, tenants, integrations, AI behavior, and operations;
- recovery, remediation, compatibility, rollout, rollback, and regression tests;
- fix acceptance under the failing and neighboring conditions.

## Ask high-impact questions

- Which evidence is verified and which detail is only reported or suspected?
- What conditions distinguish affected from unaffected executions?
- Could retries, workarounds, or remediation duplicate, delete, disclose, or corrupt data?
- Must existing affected data be detected, repaired, notified, exported, or audited?
- What related behavior must not change?
- What exact regression evidence prevents this failure from returning?

## Do not approve when

- a suspected cause is stated as fact;
- cross-tenant, security, financial, or destructive impact lacks containment and verification requirements;
- the specification prescribes a patch but fails to define restored behavior;
- acceptance proves only one example and omits the relevant regression boundary.
