# Contributing

Contributions should strengthen human control, artifact quality, traceability, or safe execution throughput.

## Before proposing a change

- Identify the stage and boundary affected.
- Explain the failure mode or historical case the change addresses.
- Preserve the separation between intent, specification, planning, and implementation.
- Add or update eval cases for behavioral changes.
- Avoid vendor coupling in canonical artifacts unless the change is an explicit adapter.

## Pull request expectations

A pull request should describe the problem, proposed change, stage impact, HIL impact, compatibility implications, test/eval evidence, and any new risk. Changes to a skill, prompt, template, hook, model assumption, router policy, or grader should include regression coverage.

## Automatic rejection conditions

Changes should not:

- allow an agent to approve its own artifact;
- silently convert assumptions into facts;
- bypass an upstream approval gate;
- move architecture decisions into intent or implementation tasks into specification;
- authorize production or destructive actions through planning approval;
- optimize raw agent count while ignoring review, integration, or supervision capacity.
