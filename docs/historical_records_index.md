# Historical Automation Records Index

This index records the categories of historical work that have been discovered and preserved through reviewed documentation or scripts. It intentionally does not reproduce raw terminal histories, credentials, OAuth material, browser data, personal media paths, or session artifacts.

## Preserved Categories

| Category | Preserved form | Current classification |
|---|---|---|
| Local content production | Catalog scripts, edit scripts, transcription helpers, quality-check procedures, integrity conventions | Preserve; local-only execution |
| Education draft production | Source-backed assembly script, briefs, captions, quality checks, backup procedure | Preserve; use only with available local evidence |
| Platform publication attempts | Manifest procedures, non-secret exception summaries, safe checkpoint rules | Preserve as manual-recovery reference; do not schedule |
| GitHub automation | Runbooks, safety notices, validation contract, workflows, schemas, tests | Preserve and run daily in the private repository |
| CLI readiness | Non-secret executable/authentication state generator and official credential policy | Preserve; collect only state, never secret values |
| Connector diagnostics | Non-secret blocker summaries and safe next conditions | Preserve; do not alter ambiguous or blocked connectors automatically |

## Historical Command Conversion Rule

A historical command becomes reusable automation only after it has been classified as non-destructive, reproducible, non-secret, and testable. Validated logic is moved into a reviewed script or documented procedure; raw terminal history remains local and is not copied into this repository.

## Run Record Locations

| Record | Storage policy |
|---|---|
| GitHub repository validation | Generated as a short-lived GitHub Actions artifact and optionally as ignored local JSON. |
| Local CLI health | Generated as ignored local JSON from `automation/record_local_cli_health.py`. |
| Stable policy and schema | Version-controlled in this repository. |
| Personal media integrity records | Retained in the local workspace and referenced by policy, not copied to GitHub. |

## Blocker Discipline

A record may identify a non-secret blocker such as an unavailable CLI, a paused schedule, an OAuth exchange failure, an account-owner verification requirement, or a platform safety notice. The record must not contain authentication codes, endpoints with embedded credentials, or any secret recovery material.
