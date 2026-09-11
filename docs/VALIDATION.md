# Public package validation

Status: PASS for v2.12.0-beta.1 package validation on 2026-09-11.

This validation covers the clean public package, not the creator's private workspace. Private project history, private tool manifests, and private logs are not included.

## Static package checks

- Repository URLs point to `https://github.com/frogwraps/GDSYNCER`.
- No stale pre-public repository links remain in tracked public files.
- No launch-blocking placeholder language remains outside intentional template placeholders.
- `_validation/` is ignored so isolated proof workspaces are not shipped.
- The package contains 32 tracked public files before Git metadata or release ZIP assets.

## Isolated Shorts proof

An isolated workspace was created from `workspace/`, then the project template was copied into a new project named `GDS Shorts`. The supplied plain project name was `Shorts`; the protocol-created project root used the required `GDS <name>` pattern.

Readback confirmed these files existed in the proof project:

- `START_HERE.md`
- `NEXT_ACTION.md`
- `TOOLBOX.md`
- `PROGRESS.md`
- `AGENTS.md`
- `CLAUDE.md`
- `log/2026-09-11_validation-gds-shorts.md`
- `03_Videos/sample-001/README.md`

The proof recorded one fictional decision: each sample video keeps its sources with its script. `PROGRESS.md` cites the validation log. `NEXT_ACTION.md` was written with closed state, checkpoint `gds-shorts-validation-2026-09-11-001`, and exactly one next action: `Review the sample-001 source checklist.`

Fresh readback recovered the saved next action, followed the source citation, and found the same decision in the log and sample file. This proves the starter can preserve project state across conversations when an assistant follows the Markdown protocol and has file access.

## Limits of this proof

This proof does not claim atomic cross-device locking, live Google Drive sync to a second machine, YouTube account creation, paid-service setup, or optional Obsidian/MemPalace writes. Those remain user-specific setup checks. The lock is advisory and depends on saved files synchronizing before another surface enters.
