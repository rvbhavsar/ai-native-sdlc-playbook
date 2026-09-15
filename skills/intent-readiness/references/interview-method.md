# Adaptive interview method

## Objective

Extract decision-quality intent without exhausting the user. Prefer a focused conversation over a static questionnaire.

## Maintain five ledgers

Track these explicitly during the conversation:

1. **Confirmed facts** — directly stated or evidenced.
2. **Decisions** — choices the human made.
3. **Assumptions** — provisional inferences that still need validation.
4. **Open questions** — unresolved items, each labeled `blocking` or `non-blocking`.
5. **Accepted risks/deferred items** — gaps the human explicitly chose to carry forward.

Never mix the ledgers. If the user corrects something, replace the old entry and acknowledge the correction.

## Pick the next question

Ask the question with the highest expected decision value:

`priority = impact on scope/acceptance/risk × uncertainty × cost of being wrong`

Prefer questions that distinguish between materially different intents. Delay details that can safely be determined in specification.

Ask one question by default and no more than three related questions in a turn. Offer 2–3 plausible options when they reduce effort, while always allowing free-form correction. Do not present the full question bank at once.

## Core sequence

Cover these concerns adaptively rather than mechanically:

1. **Trigger and evidence:** What happened, and what shows this is worth solving now?
2. **People and value:** Who is affected, in which context, and what meaningful result do they need?
3. **Outcome:** What must become true? How is that different from prescribing a feature or technology?
4. **Boundary:** What is included, excluded, and explicitly required to remain unchanged?
5. **Success:** What observable behavior, metric, or decision test proves the outcome?
6. **Guardrails:** What business, security, privacy, compliance, accessibility, platform, cost, or timing constraints matter?
7. **Dependencies and risk:** What external facts, teams, systems, permissions, or decisions could invalidate the intent?

## Challenge patterns

Use respectful pressure when input is weak:

- **Vague value:** “Make it better” → better for whom, in what situation, and by what observable change?
- **Solution masquerading as intent:** “Add Redis” → what user or system problem must be solved, and is Redis a constraint or only a proposed approach?
- **Unbounded scope:** “Support every integration” → which first users and workflows define the initial boundary?
- **False precision:** “Increase engagement 30%” → what is the baseline, event definition, measurement window, and causal expectation?
- **Missing preservation:** “Redesign onboarding” → which current behaviors, permissions, data, and paths must not regress?
- **Premature certainty:** “Users need this” → what evidence supports that claim and what remains an assumption?
- **Compound request:** split independent outcomes when they could be approved, built, or evaluated separately.

## Checkpoint format

Use a compact checkpoint when it helps:

```markdown
### What I understand
- ...

### Decisions you made
- ...

### Assumptions to validate
- ...

### Largest remaining gap
- ...
```

Do not force a checkpoint after every answer.

## Stop conditions

Stop questioning when additional answers would not materially change intent, scope, acceptance, guardrails, or risk. Draft with explicit `Unknown` or `Deferred` entries for noncritical gaps.

Continue questioning when any critical gap remains. If the user declines to answer, explain the specific consequence and offer to mark it as an accepted risk or pause the work. Never trap the user in an endless interview.

## Human approval gate

Present the finished draft and ask the human to choose:

- **Approve** — intent is accurate and may enter specification.
- **Revise** — identify the correction or unresolved decision.
- **Pause** — preserve the draft without progressing.

Silence, lack of objection, a high score, or “looks interesting” is not approval.
