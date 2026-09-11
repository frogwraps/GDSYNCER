# How it works

A project has four working files. Think of them as a bookmark and a table of contents for your AI-assisted work.

| File | Question it answers |
|---|---|
| START_HERE.md | What is this project and what are its rules? |
| NEXT_ACTION.md | Where are we now, and what comes next? |
| TOOLBOX.md | Where are the resources and which tools can we use? |
| PROGRESS.md | What did we decide, and where can we find the details? |

Detailed session records live in `log/`. PROGRESS holds a useful summary paragraph and citations, so an assistant can follow the relevant link instead of rereading every conversation. NEXT_ACTION wins when older notes disagree about current state. Confirm factual conflicts against the source before changing it.

At START, the assistant checks the project version and writer, then reads current state, resources, and relevant history. At END, it saves the log, index and changed resources, tries configured memory saves, then safely writes and reads back NEXT_ACTION before closing its session.

A branch is a subfolder with its own versions of these files. It can hold customer work or an experiment while reading the parent's context. END BRANCH saves just that branch. MERGE BRANCH brings back only selected reusable learning with citations. It refuses a busy or changed parent until the relevant difference is reconciled. Repeating an already completed merge should change nothing.

This can help keep projects separate, but the assistant must follow the instructions. There is no background agent, file-sync engine, database service, or security sandbox supplied by GD SYNCER. Your chosen AI tool needs actual access to the folder. A phone or browser chat without file access cannot execute a save simply because you type a command.

Google Drive carries project files between devices. Optional Obsidian provides browsable notes, MemPalace provides semantic recall, and TOOLBOX points to whatever tools you actually have. References connect these layers; the protocol does not install or authenticate them.

