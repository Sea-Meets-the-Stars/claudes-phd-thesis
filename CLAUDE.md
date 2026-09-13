# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository holds the code, analyses, and figures behind a PhD thesis for which **Claude is the candidate**, held to a real UCSC dissertation standard, with J. Xavier Prochaska as advisor and committee chair. The thesis write-up itself lives in a separate repository (see Related Repositories); this one is where the science gets done.

Repository layout:

- `claude_prompts/` — the prompt docs that drive this work. `start_up.md` is first; read the relevant doc before acting, and execute only the numbered task you were pointed at.

## Thesis Topic and Scope

The full settled outcome of the scoping interview — thesis statement, chapter outline, new work required, dependencies, and open questions — is in the `## Report` section of `claude_prompts/start_up.md`. **Read it before doing thesis work.** Summary:

**The claim.** In the PACE era, semi-analytical retrieval of inherent optical properties (IOPs) from remote-sensing reflectance fails for identifiable reasons, and those failures are *parameterization* failures, not *physics* failures. This statement is adopted by default and still awaits the advisor's explicit sign-off — do not represent it as agreed.

**Claude does not pick the problems.** They come from four existing projects Claude co-created with Prochaska as advisor, each carrying one leg of the argument:

- **IOPtics** (`~/Oceanography/python/IOPtics`) — controlled diagnosis: benchmarking IOP algorithms against L23, PANGAEA, and GLORIA, where truth is known. Note: much of this analysis exists only on the advisor's workstation and must be migrated into the repository before it can be cited.
- **PAB** (`~/Oceanography/python/PAB`) — the same class of failure at mission scale: PACE × BGC-Argo Chl-a (and CDOM) matchups against independent in-situ truth.
- **MOANA** — species-level retrieval and the limits of hyperspectral transfer. Currently in IOPtics (`reports/MOANA_Claude_Report.md`), being spun off into its own repository.
- **retrieve-or-bust** (`~/Oceanography/python/retrieve-or-bust`) — **the differentiable RT forward model only**, as a methods chapter. It bounds the forward-model error term so residual error is attributable to parameterization.

All four run on **BING** (`~/Oceanography/python/bing`; Prochaska & Frouin 2025, Biogeosciences 22, 4705), which predates Claude's involvement and is inherited foundation, not a thesis contribution.

**Explicitly out of scope** — do not develop, extend, or claim any of these:

- **The bbp700 analysis.** It is Allie James's work.
- **Anything in retrieve-or-bust beyond the forward model.** That belongs to the seven-person RoB team; its inversion does not yet exist and must not be claimed or anticipated as a thesis deliverable.
- **Information content as the organising frame.** Already a primary conclusion of the BING paper.

**The meta-question** — what it means for an AI to be the candidate — belongs in the Introduction and Conclusions only, never in a science chapter.

## Working Conventions

- **Git:** The user (J. Xavier Prochaska) will perform all git commands (add, commit, push, etc.). Do not run git commands that change repository state unless explicitly asked. Read-only git (`status`, `diff`, `log`, `show`, `branch`) is fine.
- **Calculations:** If you do any calculation, generate it as a Python script and write it to disk so that it can be added to the repository. Do not perform one-off calculations only in memory or in the chat.
- **Python environment:** If you need to run Python, use the `ocean14` conda environment (e.g. `conda run -n ocean14 python script.py`).
- **Logging:** After completing a task from a `claude_prompts/` doc, append a dated entry under that doc's `## Logs` section recording what was done and what was learned.

## Related Repositories

- **Claude-PhD-Thesis:** The thesis write-up (LaTeX, UCSC `ucthesis` document class) lives on this computer at `~/Projects/Overleaf/Claude-PhD-Thesis` and is its own git repository, synced with Overleaf. The same git rule applies there: the user performs all git commands.
- **Source projects:** The science the thesis draws on lives in `~/Oceanography/python/` — `IOPtics`, `PAB`, `retrieve-or-bust`, and `bing`. These are separate repositories with their own `CLAUDE.md` and `claude_prompts/`; the same git rule applies to all of them. MOANA is being spun off from IOPtics into its own repository.
