# Per-Initiative Workspace

Copy this structure when beginning a project, feature, improvement, or bug:

```text
initiative-name/
├── README.md
├── intent.md
├── spec.md
├── plan.md
├── inputs/
├── decisions/
├── evidence/
│   ├── intent/
│   ├── specification/
│   └── planning/
├── evals/
└── plans/
    ├── enablers/
    ├── epics/
    ├── features/
    └── tasks/
```

## Workspace conventions

### `README.md`

Record the initiative type, owner, current stage, current approved versions, repository links, and next human decision.

### `inputs/`

Store or link raw requests, research, incident data, screenshots, recordings, policies, and external constraints. Inputs are evidence; they do not automatically become approved requirements.

### `decisions/`

Use one short record per material choice when the main artifact would become noisy. Include status, context, options, rationale, tradeoffs, human evidence, and revisit trigger.

### `evidence/`

Keep stage-specific sources and evaluation evidence. Reference rather than duplicate large sources where possible. Distinguish observed, reported, and inferred information.

### `evals/`

Keep readiness reports, regression cases, grader results, adversarial checks, and accepted exceptions. Evaluation output is not approval.

### `plans/`

Create child plans only after the master plan identifies a need. A project plan orchestrates; a task plan is a self-contained execution packet. Avoid generating empty hierarchy for appearance.

## Artifact promotion checklist

Before moving to the next stage:

- upstream artifact version is exact and approved;
- blockers are closed or risks explicitly accepted;
- decisions and assumptions are visible;
- traceability is current;
- readiness report passes the stage threshold;
- the human reviews the exact final version and explicitly approves it.

## Suggested first brainstorming session

1. Choose an initiative type.
2. Place all available source material in or link it from `inputs/`.
3. Copy the intent template to `intent.md`.
4. Run the intent interview until only noncritical deferred questions remain.
5. Approve the exact intent before copying the specification template.
6. Repeat the gate discipline through planning.
