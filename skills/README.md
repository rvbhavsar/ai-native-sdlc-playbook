# Skills

These three skills implement the playbook as bounded, human-controlled agent workflows.

## Skill sequence

| Order | Skill | Entry gate | Exit artifact |
|---:|---|---|---|
| 1 | [`intent-readiness`](intent-readiness/SKILL.md) | Rough request exists | Approved `intent.md` |
| 2 | [`spec-readiness`](spec-readiness/SKILL.md) | Exact intent version approved | Approved `spec.md` |
| 3 | [`plan-readiness`](plan-readiness/SKILL.md) | Exact spec version approved | Approved `plan.md` |

## Installation

Copy each complete skill directory into the skill location supported by your agent runtime. Preserve all relative files because each `SKILL.md` references its own `assets/`, `references/`, `evals/`, and `scripts/` directories.

Example vendor-neutral project layout:

```text
.agents/
└── skills/
    ├── intent-readiness/
    ├── spec-readiness/
    └── plan-readiness/
```

Add runtime-specific adapters only when required, such as `.claude/skills/` or another supported skill directory. Keep this repository as the canonical source to prevent vendor-specific copies from drifting.

## Expected behavior

All three skills:

- ask one to three high-impact questions per turn;
- inspect authorized evidence before asking the user for facts already available;
- distinguish confirmed, observed, reported, proposed, assumed, and deferred information;
- draft incrementally and preserve unknowns honestly;
- produce readiness reports and expose blockers;
- require explicit human approval of the exact artifact;
- stop before the next stage or any unauthorized mutation.

## Evaluation

Every skill includes representative cases and a grader. Use the bundled evaluator for structural checks on generated artifacts, then apply the semantic grader and human review. A script pass is not evidence that the content is true, feasible, safe, or approved.

## Customization

Organization-specific architecture, security, UX, compliance, testing, and deployment standards should be added as separate reusable skills or references. Deterministic requirements that must never be violated should also be enforced with hooks, permissions, CI checks, or policy controls.
