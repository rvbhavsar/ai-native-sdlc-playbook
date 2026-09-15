# Diagram — Dependency-Aware Parallel Planning

```mermaid
flowchart TD
    F["PHASE-001 foundations"] --> G1{"Foundation gate"}
    G1 --> A["Lane A: identity"]
    G1 --> B["Lane B: core data"]
    G1 --> C["Lane C: UI shell"]
    A --> G2{"Integration gate"}
    B --> G2
    C --> G2
    G2 --> E1["Feature stream 1"]
    G2 --> E2["Feature stream 2"]
    E1 --> R["Review and release evidence"]
    E2 --> R
```

Parallelism begins only when the dependency gate is satisfied and lanes have non-conflicting ownership. Effective concurrency is limited by supervision, review, integration, and environment capacity—not merely available agents.
