# AI-Native SDLC Playbook

A reusable, human-controlled operating system for turning an idea or defect into implementation-ready work through three governed artifacts:

1. `intent.md` — agree on why, who, what outcome, and boundaries.
2. `spec.md` — agree on required behavior and the product, system, and technical contract.
3. `plan.md` — agree on implementation sequence, dependencies, parallel execution, evidence, and ownership.

This kit works as a workshop guide, a blueprint for an AI-native SDLC product, and canonical guidance for agent skills.

## Start here

1. Read [Philosophy and principles](00-philosophy-and-principles.md).
2. Read the [operating model](01-operating-model.md) and [end-to-end workflow](02-end-to-end-workflow.md).
3. Copy [the workspace guide](workspace/README.md) into a new initiative.
4. Run the three stages in order. Do not advance without explicit human approval:
   - [Intent stage](stages/01-intent/README.md)
   - [Specification stage](stages/02-specification/README.md)
   - [Planning stage](stages/03-planning/README.md)

## Kit map

| Area | Purpose |
|---|---|
| `stages/` | Stage playbooks and copy-ready artifact templates |
| `governance/` | Human-in-the-loop rules, readiness scoring, and approval gates |
| `product/` | Blueprint for turning the process into a product and agent system |
| `diagrams/` | Mermaid diagrams for workshops, documentation, and product UX |
| `workspace/` | Suggested per-initiative working-folder structure |

## Non-negotiable rules

- The human owns material product, architecture, risk, staffing, and approval decisions.
- An agent may investigate, challenge, compare, recommend, draft, and evaluate; it may not approve its own artifact.
- Each stage has one job. Intent does not design; specification does not schedule; planning does not implement.
- Unknowns remain visible as `Unknown`, `Deferred`, or an assumption with an owner and validation method.
- Approval is bound to an exact artifact version. A material change reopens that gate and all affected downstream artifacts.
- Production, destructive, irreversible, or customer-impacting actions require separate authorization and controls.

## Canonical state flow

Every stage uses the same state vocabulary:

- `NOT READY`
- `READY FOR HUMAN REVIEW`
- `APPROVED — READY FOR NEXT STAGE`

The final planning state is `APPROVED — READY TO IMPLEMENT`. Implementation, delivery, and operations can be added as downstream phases without weakening these three gates.

## Recommended repository placement

```text
docs/
├── intent.md
├── spec.md
├── plan.md
├── decisions/
├── evidence/
└── plans/
    ├── enablers/
    ├── epics/
    ├── features/
    └── tasks/
```

Keep project instructions, reusable organizational skills, and deterministic controls separate. The artifacts remain the vendor-neutral system of record; coding agents are execution runtimes.

## Visual overview

See [the end-to-end lifecycle](diagrams/01-end-to-end-flow.md), [artifact state machine](diagrams/02-artifact-state-machine.md), [stage-gate model](diagrams/03-stage-gates.md), and [parallel planning model](diagrams/04-parallel-execution.md).
