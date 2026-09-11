# Changelog

## v2.12.0-beta.3 — unpublished

Workspace-manager correction.

- Makes `AAA` the root workspace manager for all projects.
- Defines the expected flow: open `AAA`, run `:start`, then say `start a project`.
- Clarifies that `AAA` owns the global toolbox, version manifest, project templates and project organization.
- Keeps project folders as `GDS <Project Name>` inside `AAA`.
- Pauses public publication while this user experience is sorted out.

## v2.12.0-beta.2 — 2026-09-11

Small public setup-doc patch.

- Sets the recommended Google Drive workspace folder name to `AAA`.
- Keeps the project-folder rule unchanged: a project named `Shorts` becomes `GDS Shorts` inside `AAA`.
- Does not change the v2.12 protocol schema.

## v2.12.0-beta.1 — 2026-09-10

First separate public-distribution candidate, based on GD SYNCER protocol v2.12.

- Adds an accessible introduction, complete workspace starter, project and branch templates, optional memory guide, and fictional walkthrough.
- Preserves current-first startup, current-last closeout, cited history, snapshot/readback saves, advisory locks, and selective repeat-safe branch merges.
- Generalizes tool/account configuration for each user and gives the public package its own update source.
- Starts new repository history; no private workspace history is included.

This distribution revision does not migrate or replace the creator's live projects. Only v2.12 is supported as the initial public schema; older installations require a reviewed migration rather than a blind overwrite.
