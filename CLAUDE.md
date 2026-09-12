# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository holds the code, analyses, and figures behind a PhD thesis written by Claude. The thesis write-up itself lives in a separate repository (see Related Repositories); this one is where the science gets done.

Repository layout:

- `claude_prompts/` — the prompt docs that drive this work. `start_up.md` is first; read the relevant doc before acting, and execute only the numbered task you were pointed at.

## Working Conventions

- **Git:** The user (J. Xavier Prochaska) will perform all git commands (add, commit, push, etc.). Do not run git commands that change repository state unless explicitly asked. Read-only git (`status`, `diff`, `log`, `show`, `branch`) is fine.
- **Calculations:** If you do any calculation, generate it as a Python script and write it to disk so that it can be added to the repository. Do not perform one-off calculations only in memory or in the chat.
- **Python environment:** If you need to run Python, use the `ocean14` conda environment (e.g. `conda run -n ocean14 python script.py`).
- **Logging:** After completing a task from a `claude_prompts/` doc, append a dated entry under that doc's `## Logs` section recording what was done and what was learned.

## Related Repositories

- **Claude-PhD-Thesis:** The thesis write-up (LaTeX, UCSC `ucthesis` document class) lives on this computer at `~/Projects/Overleaf/Claude-PhD-Thesis` and is its own git repository, synced with Overleaf. The same git rule applies there: the user performs all git commands.
