# Bug intent

Use when actual behavior deviates from a credible expected behavior. Capture the defect and recovery contract, not an unverified root cause or prescribed patch.

## High-leverage questions

- What exactly was observed, and what should have happened instead?
- What is the shortest reliable reproduction path? If intermittent, what frequency or pattern is known?
- Which users, accounts, records, systems, or environments are affected, and how severe is the consequence?
- When did it last work or first appear? What changed around that time, if known?
- What evidence exists: error text, screenshot, logs, trace, request ID, timestamp, input, or affected record?
- Is there a workaround? Does retrying create duplicate, destructive, financial, privacy, or security effects?
- Which related behavior must remain unchanged after the fix?
- What proves the defect is fixed and has not regressed elsewhere?

Ask for secrets, credentials, or unnecessary personal data only when indispensable; prefer redacted evidence.

## Required structure

Use `assets/templates/bug-intent.md`. Include:

- concise problem and impact/severity;
- observed and expected behavior;
- reproduction or explicit statement that it is intermittent/unreproduced;
- relevant environment and evidence;
- workaround and risk, when known;
- scope, unchanged behavior, acceptance, regression boundary, assumptions, and open questions;
- human approval.

Do not state a root cause as fact unless verified by evidence. Put suspected causes in a clearly labeled note for later investigation.

## Specific failure modes

- “It doesn't work” without observed behavior.
- Expected behavior based only on preference rather than contract, prior behavior, or product decision.
- Severity inferred from emotion rather than impact.
- A reproduction that omits identity, state, timing, data, or environment conditions that matter.
- A proposed code change presented as the intent.
