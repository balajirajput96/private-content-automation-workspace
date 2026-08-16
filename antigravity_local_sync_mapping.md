# Google Anti-Gravity Local Synchronization Mapping

## Supported Capability

The installed `agy` CLI supports workspace directories, projects, agents, models, plugins, and interactive or print-mode conversations. It does not expose a `sync`, `save`, `export`, or scheduler command.

## Safe Mapping

The local workspace `/home/ubuntu/instagram_work` is the durable source of truth. The safe equivalent of synchronization is an integrity-checked local snapshot containing the catalog, captions, research packets, draft metadata, safety notice, and checksum records.

## Non-Public Operation

For every local-only workflow run, the system may refresh a single local snapshot and checksum manifest. Repeating the same external sync operation 46 times would add no verified value and could create unnecessary account or platform risk. No external synchronizations are performed.

## Anti-Gravity Use

Anti-Gravity may reference this workspace and the operation plan in `antigravity_local_operation_plan.md` for planning. Its installed headless mode cannot safely complete its own internal command-permission prompt, so the local schedule remains the execution mechanism.

## Save Record

The current local backup manifests are retained under `/home/ubuntu/instagram_work/` and are the saved record for the workflow.
