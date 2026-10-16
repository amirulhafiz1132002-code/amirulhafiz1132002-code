# Security Policy

## Scope

This repository contains the AMRHZ profile documentation and project references. Security status varies by linked project and release. Do not assume every linked repository or deployment has the same support level.

## Supported versions

There is currently no blanket version-support promise for all AMRHZ repositories. Check the individual repository's README and release notes for its current development state. A status such as `DEVELOPMENT`, `PARTIAL`, `VERIFIED`, or `LIVE` must be supported by evidence for that specific artifact or runtime.

## Reporting a vulnerability

Please do not publish credentials, personal data, or an unpatched exploitable detail in a public issue.

1. If GitHub private vulnerability reporting is enabled for the affected repository, use that channel.
2. Otherwise, contact the repository maintainer privately through an available GitHub contact channel and include the affected repository, path/component, impact, reproduction conditions, and any safe supporting evidence.
3. Do not include live tokens, passwords, or full secret values in the report. Redact them and identify the provider/service instead.
4. Allow the maintainer reasonable time to investigate before public disclosure. Acknowledgement and remediation timing depend on severity, evidence, and maintainer availability; no fixed response-time SLA is promised here.

## Secret exposure

If a credential may have been committed or published:

- Revoke or rotate it with the issuing provider first.
- Remove it from the current tracked files and prevent re-commit with appropriate ignore rules.
- Inspect relevant Git history, branches, tags, forks, logs, and deployment configuration.
- Treat file deletion from the latest commit as insufficient to prove historical removal.
- Record the remediation and verification evidence without repeating the secret.

## Disclosure and evidence

AMRHZ follows an evidence-first development approach. Bugs, failed checks, and engineering lessons may remain documented for transparency, but real credentials, precise personal information, and other unnecessary sensitive data should not be exposed as part of that record.

A report or proposed fix is not proof that a vulnerability is resolved. Resolution should be stated only after the relevant change and verification evidence are available.
