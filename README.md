# Private Content Automation Workspace

This private repository is the **non-secret, version-controlled control plane** for the local content-automation workspace. It preserves runbooks, safety constraints, deterministic validation code, and daily repository-health records. It does not store personal media, platform credentials, browser state, OAuth codes, or social-platform publishing actions.

## Daily Repository Validation

The workflow in `.github/workflows/daily-repository-validation.yml` runs daily at **02:20 UTC** and can also be started manually from the repository's Actions tab. It uses read-only repository permissions and performs the following deterministic checks:

| Check | Purpose |
|---|---|
| Unit tests | Verifies the repository validator's pass and fail behavior. |
| Safety-policy validation | Confirms the runbook, Instagram suspension notice, local synchronization mapping, contract, and run-record schema remain present. |
| Secret-marker scan | Checks version-controlled text files for a small set of prohibited secret-marker patterns. |
| Run record artifact | Produces a non-secret JSON record retained as a 14-day workflow artifact. |

The workflow must not publish content, access browser sessions, process the local media library, authenticate to external services, modify connectors, or resume platform activity. The local media workflow remains governed by the version-controlled runbook and the active Instagram safety notice.

## Historical Records and CLI State

The repository also preserves a reviewed historical-records index and a credential policy. The daily GitHub workflow validates those policy documents as repository inputs, but it deliberately does **not** run the local CLI-health collector: GitHub-hosted runners do not represent the user's local CLI installations or official local credential stores. When a non-secret local state record is needed, run `automation/record_local_cli_health.py` from the local workspace; its generated output is ignored by Git.

## Local Validation

Run the deterministic checks from the repository root:

```bash
python3 -m unittest discover -s tests -v
python3 automation/validate_repository.py --repo . --output run-records/local-validation.json
```

The `run-records/` directory is intentionally ignored by Git. A passed record is evidence that repository safety and structure checks passed; it is not evidence that external platforms, connectors, media rendering, or publishing are operational.

## Recoverability

Development changes are made on a dedicated branch, tested locally, then committed and pushed only after successful validation. The workflow itself has `contents: read` permission and cannot push changes to the repository.

## References

[1] [GitHub Actions workflow syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)

[2] [GitHub Actions limits](https://docs.github.com/en/actions/reference/limits)
