# Acceptance walkthrough

Use only a fresh fictional workspace. Run [Quickstart](QUICKSTART.md) first. This is a behavioral test for an assistant, not a guarantee every model obeys the protocol.

Record the assistant/version, OS, input, actual files changed and observed result. Tests must inspect effects, not merely search instructions for keywords.

## Core lifecycle
1. Open `AAA`, run `:start`, say `start a project named Shorts`, and confirm the template's bytes stayed unchanged.
2. START, record the sample decision and exact next action, END. Inspect the log citation and closed NEXT_ACTION.
3. In a fresh conversation START and recover that next action without the prior chat.
4. With the first session active, a second session attempts START. Compare all project-file hashes before/after: the foreign owner must stop with zero project mutations.
5. Close only the owning session. Confirm an empty/corrupt NEXT_ACTION or conflict copy causes a recovery stop, not an invented reset. Use separate disposable copies for destructive fault tests.

## Branch isolation
6. START the parent and capture its file hashes. START BRANCH source-checklist. Record a reusable lesson plus a clearly private fictional detail: SAMPLE_PRIVATE_DO_NOT_PROMOTE.
7. END BRANCH. Confirm parent hashes did not change and branch has its own log, citation, checkpoint and closed lock.
8. MERGE while parent is still independently active must stop without parent mutation. Close the parent normally. Its changed checkpoint now means the branch baseline has drifted; a merge must stop until an explicit reviewed reconciliation.

## Successful merge and repeat
9. In a closed, stable parent, create a fresh branch whose source checkpoint and four hashes match. Record the reusable lesson and the private sentinel, then END BRANCH. Explicitly request promotion of only the general lesson.
10. MERGE must preserve the parent's next action, write matching stable watermarks and a cited committed receipt, release the temporary parent lock and exclude the private sentinel from all parent files and parent memory.
11. Repeat the same merge. Parent content hashes must stay identical; only a genuinely pending memory receipt may be reconciled.

## Failure injection
12. In a NEW disposable copy with a closed stable parent and an unmerged closed branch, have the test operator or file-tool harness inject failure after the first parent write (for example deny one target write, or deliberately substitute a failed readback result). Record the injection explicitly. Follow the actual candidate instructions, do not just simulate a separate ideal algorithm.
13. The assistant must restore every touched control file and watermark from the snapshots, verify original hashes, preserve the private sentinel in its branch only, write no parent memory and report failure—not completion.
14. If a foreign edit arrives during recovery, stop rather than restoring over it. Unprovable recovery must remain recovery-required.

## Optional integration checks
Memory-disabled basic use must work without palace/vault calls. Configured optional memory requires a separate live test of deduplication, write/readback, exact citations, failure receipts and retry. The release's isolated fixture does not prove these integrations or cross-device Drive synchronization. Test those on your own configured surfaces with nonsensitive data.
