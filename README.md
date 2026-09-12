# claudes-phd-thesis

Code, analyses, and figures behind a PhD thesis written by Claude.

The thesis write-up itself lives in a separate repository —
`~/Projects/Overleaf/Claude-PhD-Thesis`, a LaTeX project on the UCSC
`ucthesis` document class, synced with Overleaf. This repository is where the
science gets done.

The topic is not settled yet; see the "Thesis topic" prompt in
[`claude_prompts/start_up.md`](claude_prompts/start_up.md).

## Installation

```bash
pip install -r requirements.txt
pip install -e .
```

Python runs in the `ocean14` conda environment:

```bash
conda run -n ocean14 python script.py
```

## Layout

- `claudes_phd_thesis/` — the Python package source.
- `claudes_phd_thesis/tests/` — tests (`pytest`).
- `claude_prompts/` — the prompt docs that drive this work, and their logs.

## Tests

```bash
conda run -n ocean14 pytest
```
