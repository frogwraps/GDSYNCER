# Your first AAA workspace and project: Shorts

You do not need to know Git, write code, or buy a template. Allow one short practice session. **Shorts is a fictional example here—we are testing project memory, not creating a YouTube channel.**

## 1. Download GDSYNCER

From the GDSYNCER repository, choose the green **Code** button, then **Download ZIP**. While this beta is unpublished, you need repository access. Extract the ZIP into Downloads or another temporary location outside your live workspace.

Prefer a versioned copy? Publication is paused while the AAA workspace-manager flow is tightened, so use only the current staging package you were given access to. Do not use older beta ZIPs for a first impression.

The downloaded README is the introduction; workspace/ contains what you install. Keep docs/ available for reference.

## 2. Set up the working home

Install [Google Drive for desktop](https://support.google.com/drive/answer/10838124?hl=en) on Windows or macOS, sign in and enable starting it when you sign in to the computer. Open its folder through File Explorer or Finder—not just the Drive website.

Create a NEW empty folder there called **AAA**. Copy the CONTENTS of the download's workspace/ folder into AAA, including _templates/. Do not copy over an existing project or create separate disconnected copies on different computers.

Choose [streaming or mirroring](https://support.google.com/drive/answer/13401938?hl=en); make the active workspace available offline if needed and leave sufficient local disk space. Seeing a folder is not proof sync finished. Have your assistant create a harmless test file, wait for Drive, and confirm the same content appears on the Drive website or another device before trusting cross-device handoff. Keep separate backups.

Linux/server environments, including a remote Hermes agent, need their own configured Drive access route; Google's native desktop client is for Windows/macOS. Do not assume a remote agent can see a local drive letter. See [supported systems](https://support.google.com/drive/answer/2375082?hl=en).

## 3. Open AAA in your assistant and start the workspace

Use an assistant environment that can read AND write local Markdown files, such as a configured local Codex or Claude environment. Give it access to AAA. A normal browser chat without connected file access cannot execute this protocol.

Paste:

> Read START_HERE.md and execute :start.

Expected: the assistant identifies this as the `AAA` workspace manager, reads the shared TOOLBOX and version manifest, and offers to start or enter a project. It should not create a project until you ask.

Now say:

> start a project named Shorts. Its purpose is ONLY a fictional GDSYNCER setup/save/resume test. Success means a fresh conversation recovers the exact saved next action and its source citation. Do not create a channel, publish anything, connect paid services or invent business details. Include the optional sample content folders described in the downloaded docs/TEMPLATES.md if that file is available. Initialize and close the setup session, then show the project path.

Expected: a new **GDS Shorts** folder containing four KISS files, AGENTS/CLAUDE entry wrappers and log/. New project roots use the `GDS <name>` pattern; give the assistant the plain name, such as `Shorts`, and let the protocol add `GDS`. The workspace template must remain unchanged. If files already exist, the assistant must stop rather than overwrite them.

## 4. Open GDS Shorts and start

Open the NEW project folder, preferably in a fresh assistant conversation. Paste:

> Read START_HERE.md and execute :start. This remains a fictional protocol test.

Expected: the assistant reads current state, checks the session owner, records its unique session and tells you where the project stands. It should not start producing videos.

## 5. Make one small, unmistakable decision

Paste:

> Record this test decision: each sample video keeps its sources with its script. Create 03_Videos/sample-001/README.md containing that decision, clearly marked fictional. The next action must be: Review the sample-001 source checklist. Do not perform that next action yet.

This creates something concrete to find later. It does not require a YouTube account, Obsidian, MemPalace, Python or a paid tool.

## 6. Save and close

Type:

> :end

Expected: a detailed session log, a PROGRESS summary with a working citation, and NEXT_ACTION written last with the exact next action and a closed session. The assistant says **FINISHED** after verified local save. Optional-memory failure must be marked pending, not falsely successful.

Drive synchronizes saved files while healthy. FINISHED means the protocol saved locally; wait for Drive to catch up before switching computers.

## 7. Prove you can return

Open GDS Shorts in a NEW conversation (or another configured assistant) and type:

> Read START_HERE.md and execute :start. Tell me the saved next action and follow its source citation. Do not execute the next action yet.

It should recover **Review the sample-001 source checklist**, the decision about sources, and the saved file/log. You should not have to paste the old conversation.

While this session is OPEN, a second fresh conversation attempting :start must identify the existing writer and stop without changing project files. Return to the owning session and :end when the test is complete. This is an advisory warning; sync delays mean it is not a guarantee against simultaneous starts.

## Once the test works

Create your own separately named project by opening `AAA`, running `:start`, then saying `start a project`. Use [project templates](TEMPLATES.md) for organization and [the full walkthrough](WALKTHROUGH.md) to test branches. Add [optional memory](OPTIONAL-MEMORY.md) only after the basic handoff works. Do not mix private project data into the protocol repository.

## If you already have a project

Do not paste a starter over existing files. Ask the assistant to read the workspace's **Adopt an existing project** procedure, inventory conflicts, make a recoverable backup and request exact approval before replacing any control file.

## Programmer path and updates

You may clone https://github.com/frogwraps/GDSYNCER outside Google Drive, inspect the Markdown, and copy workspace/ into a fresh synced working home. Normal protocol use needs neither a Git checkout nor a command-line runtime.

For an update, download a reviewed release outside the workspace and ask your assistant to compare its version manifest. Follow documented migrations with backups and readback. Never replace your project with a new blank template. This first public baseline cannot automatically migrate an arbitrary older private installation.
