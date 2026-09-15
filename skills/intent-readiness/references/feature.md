# Feature intent

Use for a new user- or system-visible capability within an existing product or project.

## High-leverage questions

- Who initiates the capability, in what context, and what are they trying to accomplish?
- What can they do today, and why is it insufficient?
- What is the entry condition, desired end state, and value produced?
- What is the simplest primary journey from trigger to outcome?
- Which edge or failure paths materially affect trust, money, data, permissions, or recoverability?
- Which roles may view, create, change, approve, or reverse the result?
- What information enters, changes, leaves, or is retained?
- What is in the first release, what is explicitly excluded, and what must remain unchanged?
- What observable acceptance conditions prove the feature satisfies the need?

## Required structure

Use `assets/templates/feature-intent.md`. Include:

- context and evidence;
- user need and affected roles;
- current state and desired outcome;
- expected behavior at intent level;
- primary, edge, and failure scenarios;
- scope, non-goals, and preservation contract;
- acceptance, guardrails, dependencies, assumptions, and open questions;
- human approval.

Describe behavior, not screens, endpoints, database tables, frameworks, or component structure unless one is a hard constraint.

## Specific failure modes

- “As a user” without a real user or context.
- A UI control mistaken for an outcome.
- Happy path only.
- Permissions and data effects omitted.
- Acceptance criteria that restate the feature title.
- Scope that quietly redesigns neighboring workflows.
