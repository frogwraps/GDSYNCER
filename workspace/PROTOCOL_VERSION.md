---
type: protocol-version
current-version: v2.12
distribution-version: v2.12.0-beta.3-unpublished
upstream-repository: frogwraps/GDSYNCER
update-policy: prompt
---

# Public protocol version

This is the complete initial public baseline: v2.12. Version manifests and templates belong to this workspace; they never point to the creator's private workspace.

## Updates

Compare a project's START_HERE schema-version with this current-version after reading the lock. No migration is needed when equal. For older or newer unknown schemas, preserve the files and request a reviewed migration; do not guess. Future releases must include explicit sequential migration blocks describing every affected protocol surface and required validation before raising current-version. Public ZIP updates do not overwrite a project automatically.

Apply only after honoring the project's update-policy: prompt asks the operator, auto permits documented migrations within existing authority, manual reports only. An active foreign writer always prevents mutation. Back up all affected files, preserve project identity and records, validate the full instruction surface and readback, then stamp last. Use reviewed public releases from https://github.com/frogwraps/GDSYNCER/releases; offline START can use this verified local manifest and record the unavailable upstream.
