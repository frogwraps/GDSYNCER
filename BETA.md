# Beta status and acceptance

Release candidate: v2.12.0-beta.3. Protocol schema: v2.12. The package passed its isolated AAA workspace-manager validation on 2026-09-12. Publication remains an explicit owner action.

The underlying protocol has been used in the creator's Windows/Google Drive workspace across multiple projects. The private development suites most recently passed 15 context checks and 43 branch-fixture checks on 2026-09-10. Those results cover that development surface; they do not prove this new package or every assistant. Private tests and logs are deliberately excluded.

Public-package validation is recorded in [release validation](docs/VALIDATION.md): file/link/privacy checks and an isolated fictional-project walkthrough. An agent following Markdown can still skip a step. Simulated locks/merges do not prove atomic cross-device locking. Optional Obsidian and MemPalace connections require user-specific installation and read/write verification. End-to-end Google Drive synchronization on a second computer is outside the isolated walkthrough.

## Before using real work

Complete [the walkthrough](docs/WALKTHROUGH.md), reopen the result in a fresh conversation, and confirm the saved next step and citations. If switching devices, confirm Drive is caught up on both sides first. Ask the assistant to show a save receipt if anything is unclear. Keep recoverable backups of important files.

## Maintainer publication steps

Verify the clean Git history and tracked-file allowlist; run the package checker and walkthrough; attach the clean ZIP and SHA-256 file to a draft prerelease. Read back repository visibility and release draft state. When the owner approves public launch, change only this clean repository to public, publish the prerelease, and verify the README and asset download without authentication. Public URLs in this candidate become accessible to other people only after that step.
