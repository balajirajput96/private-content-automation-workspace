# Historical Persistence and Credential Policy

## Purpose

This policy preserves useful historical automation knowledge without copying secrets, session material, private media, or account access data into the repository. The private repository stores **procedures, non-secret diagnostics, scripts, schemas, validation results, and safe run summaries** only.

## What Is Preserved

| Record type | Repository treatment |
|---|---|
| Runbooks, safety notices, local workflow mappings, and deterministic scripts | Version-controlled after validation. |
| Non-secret CLI capability and readiness summaries | Version-controlled or retained as workflow artifacts. |
| Repository validation reports and machine-readable schemas | Version-controlled when they describe stable rules; generated run records remain artifacts or ignored local files. |
| Historical command patterns | Converted into reviewed scripts or documented procedures only after safety classification. |
| Local catalogs, checksums, and backup manifests | Referenced by policy and validated locally; not copied with personal media. |

## What Must Never Be Preserved in Git

The repository and its workflow artifacts must never contain passwords, API keys, access tokens, OAuth authorization codes, SSH private keys, browser cookies, session exports, OTPs, personal media, raw browser profiles, or raw shell-history dumps.

## Official Credential Handling

All credentials must remain in official credential stores or other approved secure mechanisms; only non-secret references may appear in this repository.

| Integration type | Approved mechanism |
|---|---|
| GitHub Actions | Repository or environment secrets configured through GitHub's official secret-management interface, referenced only by secret name. |
| Official CLI authentication | The CLI's own local credential store or OAuth mechanism. |
| Managed connectors | The configured connector's official authorization flow. |
| Local tooling | Process environment or official secure store, never a committed `.env` file. |

No script may extract, print, copy, decrypt, upload, or enumerate secret values from terminal history, connector configuration, local credential stores, or browser profiles.

## Daily Record Rules

Each daily repository validation records the timestamp, repository revision, validator version, deterministic checks, result, and a non-secret blocker. A CLI-health record may report only **installed / absent / authenticated / unavailable / blocked** states, never account tokens, endpoint credentials, OAuth codes, or profile data.

## External-Automation Boundary

Persisting a workflow definition does not authorize public posting, account modification, rate-limit bypass, authentication bypass, connector reconfiguration, or automated retries of an account-owner verification step. Platform-specific safety notices remain authoritative.

## Incident Handling

If a secret is found in a tracked file, stop using that material, remove it through the official remediation process, rotate or revoke it through the service owner, and document only the non-secret incident category and recovery status.
