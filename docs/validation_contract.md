# Daily Repository Validation Contract

## Purpose

This repository provides a **non-public control plane** for the content-automation workspace. Its daily workflow validates repository structure, safety-policy documents, and a non-secret automation run record. It does not upload, publish, browse, authenticate to social platforms, access personal media, or perform remote account actions.

## Explicit Exclusions

The automated repository workflow must never do any of the following:

1. Read or commit credentials, tokens, cookies, OAuth codes, passwords, or private media.
2. Invoke browser-publication helpers, social-platform automation, or platform-specific upload scripts.
3. Resume Instagram access while the recorded account-safety warning remains active.
4. Retry Jules CLI OAuth authorization automatically.
5. Modify external connectors, schedules, account privacy, or platform settings.

## Validation Inputs

The deterministic validator inspects only version-controlled repository files:

| Input | Required condition |
|---|---|
| Safety notice | Must exist and retain the local-only Instagram suspension condition. |
| Daily runbook | Must exist and describe local-only non-public work. |
| Local synchronization mapping | Must exist and prohibit unsafe repeated external synchronization. |
| Run-record schema | Must exist and define only non-secret fields. |
| Workflow files | Must use least-privilege permissions and a manual trigger in addition to a daily schedule. |

## Run Record Contract

Each validation run emits a JSON record that includes: timestamp, repository revision, validator version, checks performed, check results, overall result, and an optional non-secret blocker. It must not contain environment values, credential material, video paths, account identifiers, browser URLs, or external-service payloads.

## Result Rules

| Result | Meaning |
|---|---|
| `pass` | All required version-controlled safety and structure checks passed. |
| `fail` | One or more deterministic checks failed; the workflow exits non-zero. |
| `blocked` | Validation completed, but a documented external blocker prevents a separate workflow from proceeding. |

## Recoverability

Any implementation change is developed on a dedicated branch, validated locally, committed only after tests pass, and pushed only through existing GitHub authorization. The default branch is not reset, rebased, or force-pushed by this workflow.
