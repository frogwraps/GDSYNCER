---
type: toolbox
scope: workspace
---

# AAA global project toolbox

This is the AAA workspace's single source of truth for shared project setup, templates and resource locations. Project TOOLBOX files point here. An entry is desired configuration, not proof of current connectivity.

| Resource | Scope | Location / access | Verify before use |
|---|---|---|---|
| AAA workspace root | global | this folder | Contains START_HERE.md, TOOLBOX.md, PROTOCOL_VERSION.md and _templates/ |
| Project template | global | _templates/project/ | Four KISS files + two entry wrappers + log/ |
| Branch template | global | _templates/branch/ | Four branch files + two entry wrappers + log/ |
| Version manifest | global | PROTOCOL_VERSION.md | v2.12 and public distribution |

## Optional memory

Enabled: false
Vault paths by surface: none configured
MemPalace connection: none configured
Project wing/room map: none configured
Checkpoint/readback capabilities: none verified

See the release's docs/OPTIONAL-MEMORY.md before enabling. Copy the configured memory contract into this section when enabling so installed sessions can read it without needing the download directory. Keep memory disabled until a fictional checkpoint and readback pass. No credentials belong here.

## Add your tools

Use scope global for shared tools or surface:<your-device-name> for a device-specific one. Record purpose, access method, credential variable NAME if needed, and a harmless verification step. Never assume that copying this file installs or authenticates a service. Project-specific resources belong in that project's TOOLBOX. The AAA toolbox helps create and organize projects; it is not proof that any external service is connected.
