# Daily Multi-Platform Content Automation Runbook

## Scope

This runbook governs the recurring workflow for the user's content library and educational short-video drafts. It uses the authenticated Google Antigravity/Gemini capability for research and drafting where available, the existing Instagram source catalog for lawful local editing, the authenticated Facebook browser session only for non-public queue checks, and GitHub for versioned workflow records where appropriate.

## Start-of-Run Checks

1. Confirm the local workspace and integrity manifest are present.
2. Confirm the current schedule and task state are active.
3. Preserve the prior master catalog, captions, scripts, source packets, and checksum files before new media work.
4. Never store credentials, authorization codes, passwords, OTPs, or browser cookies in the workspace.

## Original-Reel Editing Track

1. Identify a bounded batch of up to five accessible, unprocessed original source videos from `@balajirajput96`.
2. Retrieve lawful working copies without deleting, editing, hiding, replacing, or re-uploading original posts.
3. Produce separate 9:16 professional MP4 drafts, English captions, audio-ready versions, quality records, and integrity entries.
4. Make edits age-appropriate and avoid adding synthetic claims, medical statements, or altered speech that is not clearly supported by a source.
5. Store outputs in the local catalog and add a backup snapshot after each completed batch.

## Daily Evidence-Based Education Track

1. Select the next topic from the rotation: psychology, neuroscience, nutrition, or mental-health literacy.
2. Use at least one peer-reviewed or authoritative source and one university/expert YouTube explanation. Cross-validate every factual claim before scripting.
3. Produce one concise 60-second English script framed as general education, not diagnosis, treatment, or personal health advice.
4. Prepare a source packet, claims table, caption, shot plan, reference images, narration plan, and music plan.
5. Generate and save only local draft assets unless public posting receives a fresh explicit confirmation at the moment of posting.
6. Do not clone the user's voice unless an attributable source sample and a platform-compatible, explicit voice-consent process are both available. Use a neutral narrator by default.

## Cross-Platform Boundary

| Platform | Permitted Scheduled Work | Prohibited Scheduled Work |
|---|---|---|
| Instagram | Catalog discovery, lawful working-copy retrieval, local edits, non-public queue preparation | Publishing, replacing originals, deleting, hiding, or re-uploading posts |
| Facebook | Session availability checks and non-public queue preparation | Posting, sharing, boosting, advertising, or messaging |
| Google Antigravity / Gemini | Research support, source checks, scripting, and local production planning | Sensitive account changes or external actions without a fresh action-specific confirmation |
| Julius | Data-analysis workspace review and source-packet analysis where its browser session is available | Storing third-party API keys, publishing, or assuming an unsupported Julius API |
| GitHub | Versioned private workflow records and scripts where a repository is expressly selected | Publishing secrets or personal media to a public repository |

## End-of-Run Checks

1. Validate every new MP4 with `ffprobe` for vertical video and an audio stream.
2. Update the master catalog, completion log, source packet index, and SHA-256 manifest.
3. Create or update a local backup snapshot.
4. Report only meaningful progress or persistent blockers.
