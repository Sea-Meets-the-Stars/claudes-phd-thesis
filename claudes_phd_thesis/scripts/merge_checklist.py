"""Generate the pre-write-up merge checklist for the thesis source repositories.

Context.  Round-1 Q6/A6 and round-2 A12 of the qualifying-exam Q&A: every
thesis-grade result currently sits on a branch that is not `main`, and a
dissertation should cite `main` of a public repository.  This script measures the
divergence read-only and writes the checklist; the advisor runs every git command
that changes state.

It reports, per repository: the checked-out branch, the tip of `main`, and for
each local and remote branch how far ahead of and behind `main` it is, with the
date of its tip.  Branches that are fully merged are called out as safe to
delete; branches ahead of `main` get a suggested merge order.

Run it wherever the repositories live -- the numbers are per clone, so run it on
`profx` (canonical, round-1 A6) for the authoritative answer:

    conda run -n ocean14 python claudes_phd_thesis/scripts/merge_checklist.py

Output: `reports/merge_checklist.md`.
"""

from __future__ import annotations

import argparse
import datetime
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
REPORT = REPO / "reports" / "merge_checklist.md"
PYROOT = Path.home() / "Oceanography/python"

# repo -> (path, the branch that thesis citations should resolve to)
REPOS = [
    ("IOPtics", PYROOT / "IOPtics", "main"),
    ("PAB", PYROOT / "PAB", "main"),
    ("bing", PYROOT / "bing", "main"),
    ("retrieve-or-bust", PYROOT / "retrieve-or-bust", "main"),
    ("EPFT-UP", PYROOT / "EPFT-UP", "main"),
    ("ocpy", PYROOT / "ocpy", "main"),
]

# Branches that carry evidence the thesis cites, from the inventory and the Q&A.
CARRIES_EVIDENCE = {
    "IOPtics": {"rt-tests": "RT-A, the Q1 experiment", "ls2": "LS2 (round-2 A8)",
                "develop": "benchmarking framework"},
    "PAB": {"full-inelastic": "PAB 2.0", "cdom_chl": "CDOM and Chl-a reports",
            "pace_giop_gsm": "NASA GIOP retrofit", "hyper_matchups": "hyperspectral inventory"},
    "bing": {"develop": "Raman/fluorescence fixes, RoB RT backend",
             "rob_cdom": "CDOM fluorescence"},
    "retrieve-or-bust": {"cdom-rt": "CDOM RT (merged 2026-09-11, PR #21)"},
}


def git(repo: Path, *args: str) -> str:
    if not (repo / ".git").exists():
        return ""
    try:
        r = subprocess.run(["git", "-C", str(repo), *args],
                           capture_output=True, text=True, timeout=60)
        return r.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def branches(repo: Path) -> list[str]:
    """Local branches plus remote branches that have no local counterpart."""
    local = [b for b in git(repo, "for-each-ref", "--format=%(refname:short)",
                            "refs/heads").splitlines() if b]
    remote = [b for b in git(repo, "for-each-ref", "--format=%(refname:short)",
                             "refs/remotes/origin").splitlines()
              if b and not b.endswith("/HEAD")]
    seen = set(local)
    out = list(local)
    for r in remote:
        if "/" not in r:          # `origin` itself, not a branch
            continue
        short = r.split("/", 1)[1]
        if short not in seen:
            out.append(r)
            seen.add(short)
    return out


def ahead_behind(repo: Path, ref: str, base: str) -> tuple[int, int] | None:
    out = git(repo, "rev-list", "--left-right", "--count", f"{base}...{ref}")
    if not out:
        return None
    try:
        behind, ahead = (int(x) for x in out.split())
    except ValueError:
        return None
    return ahead, behind


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fetch", action="store_true",
                    help="run `git fetch --all` first (writes to .git; off by default)")
    args = ap.parse_args()

    import os
    stamp = datetime.date.today().isoformat()
    lines = [
        "# Merge checklist for the thesis source repositories",
        "",
        f"Generated {stamp} by `claudes_phd_thesis/scripts/merge_checklist.py` on "
        f"`{os.uname().nodename}`.  Read-only"
        f"{'' if not args.fetch else ' apart from the `--fetch`'}.  "
        "**The advisor runs every git command below.**",
        "",
        "Goal (round-1 Q6): before the written report is drafted, every result the "
        "thesis cites should resolve to `main` of a public repository.  Counts are "
        "for this clone only -- run this on `profx`, which is canonical, for the "
        "authoritative version.",
        "",
    ]

    for name, path, base in REPOS:
        lines.append(f"## {name}")
        lines.append("")
        if not (path / ".git").exists():
            lines += [f"Not present at `{path}`.", ""]
            continue
        if args.fetch:
            git(path, "fetch", "--all", "--quiet")
        head = git(path, "rev-parse", "--abbrev-ref", "HEAD")
        base_tip = git(path, "log", "-1", "--format=%h %ad", "--date=short", base)
        if not base_tip:
            lines += [f"No `{base}` branch in this clone.", ""]
            continue
        lines += [f"Checked out: `{head}`.  `{base}` at {base_tip}.", "",
                  "| branch | ahead | behind | tip | carries |", "|---|---|---|---|---|"]
        rows = []
        for b in branches(path):
            if b == base:
                continue
            ab = ahead_behind(path, b, base)
            if ab is None:
                continue
            ahead, behind = ab
            tip = git(path, "log", "-1", "--format=%h %ad", "--date=short", b)
            carries = CARRIES_EVIDENCE.get(name, {}).get(b.split("/")[-1], "")
            rows.append((ahead, behind, b, tip, carries))
        for ahead, behind, b, tip, carries in sorted(rows, key=lambda r: -r[0]):
            flag = "" if ahead else " *(merged -- safe to delete)*"
            lines.append(f"| `{b}`{flag} | {ahead} | {behind} | {tip} | {carries} |")
        lines.append("")
        todo = [r for r in rows if r[0] > 0 and r[4]]
        if todo:
            lines.append("Suggested order, shallowest first so each merge is small:")
            lines.append("")
            lines.append("```bash")
            for ahead, behind, b, _tip, carries in sorted(todo, key=lambda r: r[0]):
                lines.append(f"# {b}: {ahead} ahead -- {carries}")
                lines.append(f"git -C {path} merge --no-ff {b}   # onto {base}")
            lines.append("```")
            lines.append("")

    lines += [
        "## Known blockers",
        "",
        "- **`bing/setup.py` pins RoB's deleted `cdom-rt` branch** (merged and "
        "deleted 2026-09-11, PR #21), so `pip install ./bing` fails and the PAB "
        "2.0 image build had to patch its staged copy.  Move the pin to a tag or "
        "to `main` *before* merging BING `develop`, or the merge ships a broken "
        "install.",
        "- **Run outputs are never committed**, by design.  Merging a branch does "
        "not bring its evidence; the evidence travels by the transfer manifest "
        "(`reports/mac_to_profx_manifest.md`).",
        "- **MOANA left IOPtics** for `EPFT-UP` on 2026-09-13; IOPtics' `moana` "
        "branch is now history, not a merge target.",
        "",
    ]

    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n")
    print(f"wrote {REPORT}")


if __name__ == "__main__":
    main()
