---
type: workspace-entry
schema-version: v2.12
---

# Start your AAA workspace

This folder is `AAA`, the workspace manager for GD SYNCER. All projects live inside this folder as direct child folders named `GDS <Project Name>`. Read TOOLBOX.md for shared/global resources, PROTOCOL_VERSION.md for the schema and `_templates/` for project/branch starters. The template folders are reference material; never run START/END inside them.

AAA manages project setup and organization. It is not a normal project and does not replace a project's own four KISS files. It should guide creation/adoption/entry, then hand the operator into one selected project.

## When the operator says `:start` in AAA

1. Confirm the current folder is the AAA workspace root by checking this START_HERE.md, TOOLBOX.md, PROTOCOL_VERSION.md and `_templates/`.
2. Read TOOLBOX.md as the shared/global project toolbox and resource map.
3. Report the workspace briefly: where AAA is, whether project and branch templates exist, current protocol schema/distribution version and that projects belong directly under AAA as `GDS <name>`.
4. Ask for one next action only. Suggested prompt: `Say "start a project" to create a new project, or tell me which existing GDS project to open.`
5. Do not create, overwrite, migrate, publish, authenticate, spend or install anything during AAA `:start` alone.

## Command: `start a project`

When the operator says `start a project`, run the new-project flow below. If the name or purpose is missing, ask one question at a time. Do not guess.

## Install a new project

1. Ask the operator for project name, purpose and success criteria if not supplied. One question at a time is preferred.
2. Use a new child folder `GDS <name>` inside AAA. Resolve the real destination; refuse traversal, an existing target, or a symlink/junction that escapes this workspace.
3. Copy only `_templates/project/` into that folder, including log/. Confirm the four KISS files and both routing wrappers exist. No Git is needed in this workspace.
4. Fill PROJECT_NAME, PROJECT_SLUG, PURPOSE, and SUCCESS only from confirmed facts; leave genuinely unknown facts explicitly pending. workspace-root is `..` because projects are direct children. Do not change rules or a schema stamp while personalizing.
5. Read the project START_HERE and initialize it through the START/END sequence. Preserve the template unchanged. Use unique owner and checkpoint identifiers; verify all writes.
6. Show the final project path and the exact next command: open `GDS <name>` and say `:start`.

## Adopt an existing project

Read its current instructions, locks and control files first. Inventory conflicts with the four KISS filenames and AGENTS/CLAUDE wrappers. Preserve all real work. Present an exact file migration/backup plan and use the operator's specific approval before replacing existing control files. No blind overwrite or inferred cleanup. A project actively owned elsewhere is unavailable for adoption.

## Enter a project

Open the selected project folder in your assistant and read its START_HERE.md. Discover the nearest START_BRANCH.md before selecting a project root when inside a branch. Only one project or branch is the active writing scope; inherit shared resources read-only from AAA. Commands at the workspace root without a selected project require one project choice, not guesses about all folders.
