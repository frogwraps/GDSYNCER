---
type: workspace-entry
schema-version: v2.12
---

# Start your workspace

This folder contains independent projects. Read TOOLBOX.md for shared resources and PROTOCOL_VERSION.md for the public schema. The template folders are reference material; never run START/END inside them. This workspace root is an index/bootstrap, not a fifth project state store or a global session lock.

## Install a new project

1. Ask the operator for a project name and purpose if not supplied. Use a new child folder `GDS <name>`. Resolve the real destination; refuse traversal, an existing target, or a symlink/junction that escapes this workspace.
2. Copy only `_templates/project/` into that folder, including log/. Confirm the four KISS files and both routing wrappers exist. No Git is needed in this workspace.
3. Fill PROJECT_NAME, PROJECT_SLUG, PURPOSE, and SUCCESS only from confirmed facts; leave genuinely unknown facts explicitly pending. workspace-root is `..` because projects are direct children. Do not change rules or a schema stamp while personalizing.
4. Read the project START_HERE and initialize it through the START/END sequence. Preserve the template unchanged. Use unique owner and checkpoint identifiers; verify all writes.

## Adopt an existing project

Read its current instructions, locks and control files first. Inventory conflicts with the four KISS filenames and AGENTS/CLAUDE wrappers. Preserve all real work. Present an exact file migration/backup plan and use the operator's specific approval before replacing existing control files. No blind overwrite or inferred cleanup. A project actively owned elsewhere is unavailable for adoption.

## Enter a project

Open the selected project folder in your assistant and read its START_HERE.md. Discover the nearest START_BRANCH.md before selecting a project root when inside a branch. Only one project or branch is the active writing scope; inherit shared resources read-only. Commands at the workspace root without a selected project require one project choice, not guesses about all folders.

