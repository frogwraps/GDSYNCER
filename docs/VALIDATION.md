# Public package validation

Status: VERIFIED for v2.12.0-beta.3 package validation on 2026-09-12. This check did not change repository visibility; publication remains an explicit owner action.

This validation page currently covers the staged package, not the creator's private workspace. Private project history, private tool manifests, and private logs are not included.

## Static package checks

- Repository URLs point to `https://github.com/frogwraps/GDSYNCER`.
- No stale pre-public repository links remain in tracked package files.
- No launch-blocking placeholder language remains outside intentional template placeholders.
- `_validation/` is ignored so isolated proof workspaces are not shipped.
- The package contains 34 tracked public files before Git metadata or release ZIP assets.
- First-time setup docs now name the mounted Google Drive workspace folder `AAA`, while project folders inside it still use `GDS <name>`.
- The intended beta.3 startup flow is: open `AAA`, run `:start`, then say `start a project`. The fresh isolated package proof passed on 2026-09-12.

## Repeatable release check

Run `python scripts/verify_package.py --root .` from the repository root. The checker uses only the Python standard library. It validates the public-file shape, nonempty project and branch templates, local documentation links, the AAA-to-`GDS Shorts` fictional installation flow, template immutability during project creation, the saved next action and citation, and the advisory-lock data shape.

On 2026-09-12 it passed 27 package checks and five regression tests against this staging package. The companion command `python -m unittest tests/test_verify_package.py -v` verifies that the checker accepts the staged package.

## Isolated Shorts proof

The 2026-09-12 checker created an isolated workspace from `workspace/`, then copied the project template into a new fictional project named `GDS Shorts`. The supplied plain project name was `Shorts`; the protocol-created project root used the required `GDS <name>` pattern.

Readback confirmed these files existed in the proof project:

- `START_HERE.md`
- `NEXT_ACTION.md`
- `TOOLBOX.md`
- `PROGRESS.md`
- `AGENTS.md`
- `CLAUDE.md`
- `log/2026-09-12_validation-gds-shorts.md`
- `03_Videos/sample-001/README.md`

The proof recorded one fictional decision: each sample video keeps its sources with its script. `PROGRESS.md` cites the validation log. `NEXT_ACTION.md` was written with closed state, checkpoint `gds-shorts-validation-2026-09-12-001`, and exactly one next action: `Review the sample-001 source checklist.`

Fresh readback recovered the saved next action, followed the source citation, and found the same decision in the log and sample file. This proves the starter can preserve project state across conversations when an assistant follows the Markdown protocol and has file access.

## Limits of this proof

This proof does not claim atomic cross-device locking, live Google Drive sync to a second machine, that every AI model obeys the Markdown protocol, YouTube account creation, paid-service setup, or optional Obsidian/MemPalace writes. Those remain user-specific setup checks. The lock is advisory and depends on saved files synchronizing before another surface enters.
