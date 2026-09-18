"""Inventory the Mac-only thesis evidence and emit the `rclone` commands to move it.

Context.  Round-1 A6 of the qualifying-exam Q&A made `profx` the canonical
machine for thesis evidence and authorised Mac-to-`profx` transfer via `rclone`
through the AIOcean Google Drive; round-2 A12 asked for this script.  The point
is that nothing gets cited from a machine that is not `profx`, so everything the
Mac holds and `profx` does not has to move before the 2026-09-19 evidence freeze.

Three classes of thing, handled differently:

- **Sweep outputs under `$OS_COLOR`** -- large, never committed by design, and
  the only class that actually needs Drive.  These get `rclone copy` commands.
- **Git history** (the IOPtics `moana` line, now in the `EPFT-UP` repository;
  the Overleaf thesis clone) -- moves by `git fetch`/`git clone`, not by Drive.
  Pushing git objects through a Drive folder would be slower and lossier.
- **Things already on `profx`** -- listed so the checklist is complete and so
  nobody re-copies 349 MB for nothing.

This script is read-only: it measures, and it *prints* the commands.  It never
runs `rclone` and never runs a git command that writes.  Run it on the Mac:

    conda run -n ocean14 python claudes_phd_thesis/scripts/mac_to_profx_manifest.py

Output: `reports/mac_to_profx_manifest.md`.
"""

from __future__ import annotations

import argparse
import datetime
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
REPORT = REPO / "reports" / "mac_to_profx_manifest.md"

DEFAULT_DEST = "AIOcean:Claude_PhD_transfer"

# Sweep-output trees under $OS_COLOR that the inventory records as Mac-only.
# (`claude_prompts/profx_inventory.md` section 9 and round-1 Q6.)
OS_COLOR_TREES = [
    ("IOPtics/runs/expb_giop_L23_test20", "test20 two-algorithm sweep, 2026-07-03"),
    ("IOPtics/runs/gloria_turbid_v3", "GLORIA turbid sweep (Ch 3 case study)"),
    ("IOPtics/runs/multi_L23_PANGAEA_v2", "three-algorithm L23 + PANGAEA sweep, 2026-08-08"),
    ("IOPtics/leaderboard.parquet", "cross-sweep leaderboard"),
    ("IOPtics/whn_explore", "WaterHypernet exploration"),
]

# Repositories whose history, not whose bytes, has to reach profx.
GIT_MOVES = [
    ("EPFT-UP", Path.home() / "Oceanography/python/EPFT-UP",
     "MOANA's spin-off home (A12).  Already installed on profx -- verify the tip matches."),
    ("Claude-PhD-Thesis", Path.home() / "Projects/Overleaf/Claude-PhD-Thesis",
     "Thesis LaTeX.  Clone on profx from Overleaf directly; do not send through Drive."),
]


def du_bytes(path: Path) -> int | None:
    """Apparent size of a file or tree, in bytes; None if it does not exist."""
    if not path.exists():
        return None
    if path.is_file():
        return path.stat().st_size
    total = 0
    for root, _dirs, files in os.walk(path):
        for f in files:
            fp = Path(root) / f
            try:
                total += fp.stat().st_size
            except OSError:
                pass
    return total


def human(n: int | None) -> str:
    if n is None:
        return "-"
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024.0
    return f"{n:.1f} GB"


def git(repo: Path, *args: str) -> str:
    """Read-only git.  Returns '' if the repo is missing or the command fails."""
    if not (repo / ".git").exists():
        return ""
    try:
        return subprocess.run(["git", "-C", str(repo), *args],
                              capture_output=True, text=True, timeout=30).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dest", default=DEFAULT_DEST,
                    help=f"rclone destination prefix (default {DEFAULT_DEST})")
    args = ap.parse_args()

    root = os.environ.get("OS_COLOR")
    if not root:
        sys.exit("OS_COLOR is not set; source the shell profile first.")
    os_color = Path(root)
    stamp = datetime.date.today().isoformat()
    dest = f"{args.dest}/{stamp}"

    lines = [
        "# Mac -> profx transfer manifest",
        "",
        f"Generated {stamp} by `claudes_phd_thesis/scripts/mac_to_profx_manifest.py` "
        f"on `{os.uname().nodename}`.  Read-only: this script measures and prints "
        "commands; it runs nothing.",
        "",
        "`profx` is canonical for thesis evidence (round-1 A6).  Everything below "
        "must be on `profx` before the 2026-09-19 18:00 exam evidence freeze.",
        "",
        "## 1. Sweep outputs (Drive)",
        "",
        "| tree under `$OS_COLOR` | size | what it is |",
        "|---|---|---|",
    ]

    total = 0
    present = []
    for rel, what in OS_COLOR_TREES:
        size = du_bytes(os_color / rel)
        if size is not None:
            total += size
            present.append(rel)
        lines.append(f"| `{rel}` | {human(size)} | {what}{'' if size is not None else ' **(absent)**'} |")
    lines += ["", f"**Total to move: {human(total)}.**", ""]

    lines += ["### Push, from this Mac", "", "```bash"]
    for rel in present:
        lines.append(f"rclone copy -P '{os_color / rel}' '{dest}/{rel}'")
    lines += ["```", "", "### Pull, on `profx`", "", "```bash"]
    for rel in present:
        lines.append(f"rclone copy -P '{dest}/{rel}' \"$OS_COLOR/{rel}\"")
    lines += ["```", "",
              "Then verify with `rclone check` on each pair, and delete the Drive "
              "copy once `profx` has it -- Drive is a transport here, not a backup.",
              ""]

    # --- git ------------------------------------------------------------------
    lines += ["## 2. Git history (not Drive)", "",
              "| repository | local tip | branch | note |", "|---|---|---|---|"]
    for name, path, note in GIT_MOVES:
        tip = git(path, "log", "-1", "--format=%h %ad", "--date=short") or "(not on this Mac)"
        branch = git(path, "rev-parse", "--abbrev-ref", "HEAD") or "-"
        lines.append(f"| `{name}` | {tip} | `{branch}` | {note} |")
    lines += ["",
              "`EPFT-UP` carries the MOANA work that left IOPtics on 2026-09-13 "
              "(A12).  On `profx`, `git fetch --all` in each of IOPtics, PAB, BING, "
              "retrieve-or-bust and EPFT-UP is enough; no branch in any of them "
              "needs to travel through Drive.",
              ""]

    # --- what is already there ------------------------------------------------
    lines += ["## 3. Already on `profx`, do not re-copy", "",
              "- The full-L23 MCMC sweep (2026-08-19) and the RT-A outputs -- "
              "`profx` produced them.",
              "- The PAB 1.0 production and 2.0 databases.",
              "- All four source repositories and their branches.",
              ""]

    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n")
    print(f"wrote {REPORT} ({human(total)} to move)")


if __name__ == "__main__":
    main()
