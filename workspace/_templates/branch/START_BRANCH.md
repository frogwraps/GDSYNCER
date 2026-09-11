---
type: branch-entry
schema-version: v2.12
parent-root: ../..
---

# Branch {{BRANCH_NAME}}

Purpose: {{BRANCH_PURPOSE}}
Branch ID: {{BRANCH_ID}}

## Scope and entry

This folder is a separate working lane inside one project, not a Git branch. The parent is read-only during ordinary branch work even when its session is active. Sibling projects and branches are out of scope. Folder separation is not access control.

Read this branch NEXT_ACTION first for its lock. Apply the parent's START_HERE safety, current-first reading, tool checks and SAVE rules to BRANCH files, never to the parent lock. Use a unique branch session ID; stop on a different active owner, corrupt state, conflict copy or failed readback. Read branch TOOLBOX then branch PROGRESS; inherit parent START_HERE, NEXT_ACTION, PROGRESS and TOOLBOX read-only. Parent state cannot replace the branch's own next action. Check the shared version manifest; unknown drift needs a reviewed migration before branch mutation.

START BRANCH (or :start while inside this branch) opens only this branch. END BRANCH (or :end here) writes branch log, index/resources, configured branch-scoped memory citations, and branch NEXT_ACTION last; release only after verified local readback. Follow the parent's full END algorithm, with branch-local paths and identity. Output FINISHED only after that local closeout succeeds.

Keep branch-private facts, customer material and unrelated experiments here. A useful general lesson is only a candidate for promotion until MERGE BRANCH is explicitly requested.

## MERGE BRANCH — explicit, selective, recoverable

1. Require this branch closed and readable. If still active in this same session, run END BRANCH first; a foreign active owner stops the merge. Read parent SESSION STATUS: any independently active parent stops the merge. Never silently override it.
2. Check MERGE WATERMARKS below and the parent PROGRESS for a prior matching source checkpoint/merge ID. A completed merge is a no-op for content; only a specifically pending memory receipt may be retried with duplicate checks. If only one side has a watermark or a pending transaction exists, reconcile against its snapshot/receipt before any new promotion.
3. Compare current parent checkpoint AND SHA-256 hashes of its four KISS files to the branch Source parent checkpoint and hashes. Any drift stops promotion. Explain the difference and request a reviewed reconciliation; never simply replace the stored hashes to make the check pass. Reconciliation must review parent changes and branch candidates, preserve newer parent work, and record approval and a new baseline before retry.
4. Identify only reusable decisions, practices or tool references. Show the proposed selection when its scope is unclear. Never promote private customer details, credentials, full transcripts or all branch contents. Cite the exact branch log and checkpoint. Confirm promoted text itself contains no private detail; citations do not grant public access.
5. Choose one stable merge ID, retained for all retries of this branch checkpoint. Prepare a transaction receipt in branch log/ listing scope, source checkpoint, original hashes, selected content, exact files to change, and pending state. Snapshot all affected parent AND branch files into a unique branch _MERGE_BACKUP/<merge-id>/ before any parent mutation.
6. Re-read hashes/owners immediately before taking a temporary parent advisory lock with this session ID. Verify its owner by readback; if anything differs, stop without promotion. This is not an atomic cross-device lock; use one writer and healthy sync.
7. Prepare and validate complete candidates using the parent's SAFE WRITE rules: append the promoted-only summary and stable merge watermark to parent PROGRESS (and TOOLBOX only for selected reusable tools); write branch merge receipt/watermark; prepare parent NEXT_ACTION preserving the parent's existing work-unit and next action, adding the merge receipt and updated checkpoint. Do not replace the parent's plan with the branch's plan.
8. Apply with hash checks and readback at each step; write parent NEXT_ACTION LAST, releasing the temporary lock only once all other writes validate. Verify both watermarks, citations, selected-only content, preserved parent next action and closed parent state. Then mark the transaction receipt committed and verify it. If the final receipt fails, stop for recovery reconciliation; do not repeat promotion blindly.
9. On any partial write/readback failure, restore every file changed by this merge to its snapshot, including both watermarks and parent lock, ONLY when no intervening foreign changes exist. Verify original hashes. Mark the branch transaction failed/rolled back separately after restoration. Never invent a committed checkpoint or write parent memory for a failed merge. If rollback cannot be verified, retain recovery evidence, report recovery required and stop.
10. Only AFTER committed KISS validation, attempt any configured promoted-only memory checkpoint under the merge ID. Memory failure does not roll back a committed merge: record a pending receipt. A retry only reconciles missing memory by stable ID; no duplicate content promotion.

## MERGE WATERMARKS
None. For a committed merge record merge ID, branch source checkpoint, parent before/after checkpoints, cited receipt and selected content. Both parent PROGRESS and this section must agree.
