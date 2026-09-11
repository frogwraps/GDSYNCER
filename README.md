# GD SYNCER

### Different AI. Different computer. Same project, same place.

I built GD SYNCER because I have ADD, 50 tabs open at once, and more than one project pulling at my attention. I'd step away from a project for a couple of days—or a couple of weeks—and come back lost, not quite remembering where I'd left off. This protocol gave me a way to keep working on projects over longer periods without having to reconstruct everything each time. I could return to the decisions, progress, and next step, while keeping the project in front of me separate from all the others.

GD SYNCER is designed to let you change AI assistants, conversations, and computers without starting your project over. Start with Claude, continue in Codex, or return through an agent environment such as Hermes: your saved instructions, decisions, and next step live in project files, not just inside one chat. Google Drive is the working home for those files, keeping them accessible across your connected devices without a Git commit-and-push routine for everyday work. Tell your assistant `:start` to pick up the project and `:end` to save your place; each assistant needs file access and must follow the protocol. The recommended stack is mounted Google Drive for live project files, Karpathy-style Obsidian notes for human-readable context, and optional MemPalace recall for semantic memory. Project and branch folders keep unrelated work separate while still letting your storage, notes, memory, and tools point at the same project. GitHub is where the free, open-source protocol is shared, not where you have to put your private projects.

— Ben, creator of GD SYNCER

**Public beta package · protocol v2.12 · MIT licensed.** The protocol is free; your AI assistant, storage, or optional services may have their own costs.

## Try it

1. Download the ZIP from [Releases](https://github.com/frogwraps/GDSYNCER/releases) when available, or use GitHub's **Code → Download ZIP**.
2. Set up Google Drive for desktop on Windows or macOS and confirm your Drive folder is accessible through your computer's file system. Extract the release outside your work folders, then copy the **contents** of `workspace/` into a new, empty `My Projects` folder on that Drive. See the setup guide below for sync checks and other environments.
3. Open that folder in an AI assistant that can read and write its files. Ask it to read `START_HERE.md` and install a project called `My First Project`. The protocol creates the folder as `GDS My First Project`.
4. Open the new project in your assistant and say `:start`. Do a small task, then say `:end`.

[Step-by-step setup](docs/QUICKSTART.md) · [How it works](docs/HOW-IT-WORKS.md) · [Add Obsidian and MemPalace](docs/OPTIONAL-MEMORY.md) · [Worked example](docs/WALKTHROUGH.md)

## What you get

- Continuity across AI assistants and computers through shared, readable project files—not a dependency on one chat's memory.
- A separate home for each project, with a written next step you can find again.
- Plain-text files you can read and keep without a special app.
- Customer, marketing, and research branches with their own working context.
- Citation links from short summaries to detailed session records.
- Optional memory connections using your own tools and accounts.

## Why download from GitHub but work in Google Drive?

GD SYNCER was built for work that gets interrupted. With Google Drive for desktop set up, your assistant can work through a folder on your computer. Drive automatically synchronizes files as they are saved, when connected and healthy; it does not wait for you to finish the session. Saved drafts and project updates can reach your other devices even before you say `:end`. That ongoing synchronization, without a separate publishing step, is why Google Drive is the working home. See [Google's desktop setup and sync guide](https://support.google.com/drive/answer/10838124?hl=en).

The same applies to the protocol's session-status file. At `:start`, the assistant records which surface has the project open. Once that file has synchronized, another assistant following the protocol can read it and warn: "This project is already open in Codex—do not proceed." This is an advisory flag, not an instant or unbreakable lock. Wait for sync before changing surfaces. `:end` still matters: it organizes the session's decisions, citations, and next action into a proper handoff and closes the session.

GitHub distributes the protocol and provides version history, contribution review, and releases. GitHub projects can also be worked on locally; they are not cloud-only. The difference is that an ordinary local save does not update GitHub: changes must be pushed or written through its API. That can happen at START, during work, or at END, but it is a separate operation, not automatic file synchronization supplied by this protocol. GitHub could support an OPEN flag too with explicit publication and verification. We chose Drive so sharing already-saved work does not depend on that extra operation. See [GitHub's explanation of Git](https://docs.github.com/en/get-started/using-git/about-git). Keep Git checkouts outside Drive-synced folders. Downloading this protocol does not publish your own projects.

Drive synchronizes **saved files**, not unwritten chat or an assistant's thoughts, and synchronization is not an independent backup: mistakes and deletions can propagate too. A mounted folder alone does not prove cloud sync has completed. Mirrored files are stored locally; streamed files may be fetched from the cloud and need offline availability configured when required. See [streaming versus mirroring](https://support.google.com/drive/answer/13401938?hl=en). Maintain separate backups and use the session checks rather than treating a visible folder as proof that it is safe to resume.

Cross-platform continuity means sharing saved project context, not automatically transferring an assistant's hidden reasoning, credentials, installed skills, or tool connections. Configure access separately in each environment. Obsidian uses its chosen vault sync method, and a live MemPalace database stays outside Drive; these are optional connections, not databases that Drive silently synchronizes for you.

GD SYNCER supplies instructions and templates. Your assistant performs the saves; Google Drive performs file synchronization. It cannot enforce an assistant's behavior, stop another computer from writing, or grant an assistant access to files or tools. Use one writer per project or branch and wait for synchronization before switching devices. Branch folders organize context; they are not access-control boundaries.

This beta grows out of the creator's daily multi-project use. The release tests and limits are described in [BETA.md](BETA.md). Other assistants and operating systems need their own verification. GD SYNCER is separate from the Get Shit Done (GSD) framework.

[License](LICENSE) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md)
