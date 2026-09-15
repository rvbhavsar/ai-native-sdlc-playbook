# Diagram — End-to-End AI SDLC Flow

```mermaid
flowchart TD
    A["Idea, request, or incident"] --> I["Intent workshop"]
    I --> IG{"Human intent gate"}
    IG -->|Revise| I
    IG -->|Approve| S["Specification workshop"]
    S --> SG{"Human spec gate"}
    SG -->|Revise intent| I
    SG -->|Revise spec| S
    SG -->|Approve| P["Execution planning"]
    P --> PG{"Human plan gate"}
    PG -->|Revise spec| S
    PG -->|Revise plan| P
    PG -->|Approve| X["Authorized implementation workflow"]
    X --> V["Verify, review, and integrate"]
    V --> D{"Production authorization"}
    D --> O["Operate and observe"]
    O --> A
```

The three playbook stages end at the approved plan. Implementation and production are shown to clarify the closed loop, but require separate authorization and controls.
