# Security Policy

## Reporting

Do not disclose a security issue in a public issue. Report it privately to the repository owner through the security contact method configured on the GitHub profile or repository.

## Security scope

The repository contains process guidance, templates, and agent skills. Treat the following as security-sensitive changes:

- agent permissions or prohibited-action boundaries;
- tenancy, identity, authorization, data, memory, or tool-use guidance;
- HIL and production authorization behavior;
- prompt-injection, data-leakage, and destructive-action safeguards;
- evaluation cases that reveal confidential production details.

Never commit credentials, customer data, private prompts, production logs, proprietary documents, or sensitive eval fixtures. Sanitize historical cases before contributing them.
