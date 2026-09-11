# Add Obsidian and MemPalace

This optional arrangement follows the creator's setup: project files carry current work, Obsidian keeps browsable session notes, and MemPalace helps find relevant past context. The basic protocol works without either memory store.

## Configure your own tools

Install and connect your chosen tools using their official instructions: [Obsidian](https://help.obsidian.md/) and your current MemPalace distribution/source. Tool names below describe capabilities, not guaranteed API signatures. Use your installed tool's actual schema and verify read/write on each machine before marking memory enabled.

Keep the active MemPalace database on a local, non-synced disk. Never put live SQLite files in Google Drive or an Obsidian-synced vault. Exchange supported exports or consistent backups if needed; file sync does not merge separate palace databases. Choose a single synchronization method for an Obsidian vault—do not run two sync engines over it. Obsidian does not have to be open for native file writes, but any app/plugin-dependent connection may require it. Verify your chosen connection on each machine.

In the existing workspace TOOLBOX, set memory to enabled only after confirming:

- The absolute vault path on each surface and a dedicated `_gds-sessions/` directory for append-only notes.
- The reachable MemPalace connection and its health/integrity check.
- A chosen wing and a distinct room/topic for each project; stable agent identity where the diary API requires one.
- Actual read, checkpoint/write, duplicate lookup, and diary-read capabilities. Tools and parameters vary by installation; never invent a successful connection.

Record names and paths only, never secrets. Start with a harmless fictional checkpoint, read it back, and cite the returned identifier plus exact vault path. If the tools cannot verify the save, mark that part pending.

## Startup: follow the links

After the KISS current-first cascade, read the most recent PROGRESS memory citations. Fetch the exact drawer/entry where the API supports it; for a diary API indexed by agent rather than entry ID, read that agent's scoped diary and match the stable checkpoint. Read the cited vault paragraph. Use a small scoped search only for additional relevant context. Memory is advisory and cannot override current NEXT_ACTION.

## Closeout: write once and cite it

After the project log, PROGRESS summary and TOOLBOX updates:

1. Choose a stable identifier such as `my-project/session-2026-09-10-001`. A retried closeout reuses it.
2. Check both destinations for that identifier before writing. If a prior request timed out, query its result before retrying.
3. Check palace integrity. When healthy, store one short checkpoint with what happened, what was learned, why it matters, and the canonical log citation. Add its diary entry using the supported checkpoint call or available write capabilities. Strip emoji/variation selectors from palace content for compatibility with the creator's tested setup. Save returned IDs.
4. Append one paragraph with the same stable identifier and log citation to `<vault>/_gds-sessions/<project-slug>.md`. Never overwrite curated notes. Reuse an existing paragraph with that identifier.
5. Read back both writes; only then add their exact IDs/paths and checkpoint identifier to this session's PROGRESS block. Include the diary agent identity if required for retrieval. Use a clickable file link for the vault and log, and the exact tool identifier for MemPalace; do not invent a URI scheme.
6. If either store fails, record the exact failure and a pending-memory citation in PROGRESS, then continue to the verified NEXT_ACTION save and lock release. NEXT_ACTION includes the pending receipt reference so the next session can attempt the missing write once, after checking the stable ID. A successful retry updates the receipt; do not duplicate the other destination.

Example citation format (values are placeholders, never evidence of a save):

```text
Memory: checkpoint <stable-id>; palace <returned-drawer-id>; diary <returned-id>, agent <configured-agent>; vault <exact-note-path>; source log/<session-page>.md; verification <readback result>.
```

## Branches and merges

A branch uses a separate room/topic and note: `_gds-sessions/<project-slug>/branches/<branch-id>.md`. Record citations only in branch PROGRESS. Branch-private is a scope rule, not access control; use separate stores/permissions where needed.

Only after a merge's parent and branch KISS writes have committed and passed validation may memory receive its promoted-only summary under the merge ID. Refused or rolled-back merges write no parent memory. If memory fails after a committed merge, the merge remains committed with a pending memory receipt. On retry, the watermark prevents re-promotion; separately reconcile only the missing memory receipt by stable ID. This avoids claiming a rollback can undo an external memory write.
