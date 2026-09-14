"""Inventory of Claude's work on the ``profx`` workstation.

Written for the qualifying-exam report (``claude_prompts/qual_exam_prompts.md``,
Report prompt 1).  Everything here is read-only: it walks the four source
repositories and the ocean-colour data tree, and writes Markdown tables to
``reports/profx_inventory_tables.md`` so the numbers quoted in the prompt doc
can be regenerated.

Run with::

    conda run -n ocean14 python claudes_phd_thesis/scripts/profx_inventory.py

Only the standard library is used.  Git is invoked read-only (``log``,
``branch``, ``ls-files``, ``status``).
"""

from __future__ import annotations

import datetime as dt
import os
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve()
THESIS_REPO = HERE.parents[2]
OUT = THESIS_REPO / "reports" / "profx_inventory_tables.md"

PY_ROOT = Path(os.environ.get("OCEAN_PY", "/mnt/tank/Oceanography/python"))
OS_COLOR = Path(os.environ.get("OS_COLOR", "/home/xavier/Oceanography/data/Color"))

REPOS = {
    "IOPtics": PY_ROOT / "IOPtics",
    "PAB": PY_ROOT / "PAB",
    "retrieve-or-bust": PY_ROOT / "retrieve-or-bust",
    "bing": PY_ROOT / "bing",
    "claudes-phd-thesis": THESIS_REPO,
}

# Sweep / run output directories in the data tree, with the sweep they belong to.
RUN_DIRS = {
    "IOPtics/runs/expb_giop_L23_mcmc_full": "Full-L23 MCMC sweep (expb_pow + giop, 3,320 spectra)",
    "IOPtics/runs/multi_L23_PANGAEA_v2": "Three-algorithm L23 + PANGAEA sweep",
    "IOPtics/runs/pangaea_fits_base": "PANGAEA fit investigation, base",
    "IOPtics/runs/pangaea_fits_maxfev": "PANGAEA fit investigation, maxfev variant",
    "IOPtics/runs/pangaea_fits_qwip": "PANGAEA QWIP annotation",
    "IOPtics/runs/pangaea_fits_turbid": "PANGAEA turbid-model variants",
    "IOPtics/runs/pangaea_fits_v2": "PANGAEA fit investigation, v2",
    "IOPtics/runs/rt_tests_smoke": "RT-tests smoke run",
    "IOPtics/runs/rt_tests_A_pangaea_v1": "RT-A sweep, PANGAEA-97 (five RT variants)",
    "IOPtics/runs/rt_tests_A_l23_v1": "RT-A sweep, L23 X=4 (five RT variants; running)",
    "IOPtics/pace_pab_100": "PACE-100 spectra extracted from PAB run1k",
    "PAB/full": "PAB production database (pab_version 1.0)",
    "PAB/run1k": "PAB run1k (273-matchup development run)",
    "PAB/run10": "PAB run10 (pilot)",
    "PAB/bias_analysis": "bbp700 bias follow-up (whybbp.md; Allie James's topic)",
    "Biomass/L23_Fits_Inelastic": "BING biomass-paper L23 inelastic fits",
}

RTA_LOG = OS_COLOR / "IOPtics" / "runs" / "rt_tests_A_run.log"
RTA_CHAINS = OS_COLOR / "IOPtics" / "runs" / "rt_tests_A_l23_v1" / "chains"
RTA_PANGAEA_CHAINS = OS_COLOR / "IOPtics" / "runs" / "rt_tests_A_pangaea_v1" / "chains"
RTA_VARIANTS = [
    "expb_pow_ztt_el",
    "expb_pow_hyb_el",
    "expb_pow_hyb_ram",
    "expb_pow_hyb_ramfl",
    "expb_pow_hyb_ramflcdom",
]
N_L23 = 3320
N_PANGAEA = 97


def git(repo: Path, *args: str) -> str:
    """Run a read-only git command and return stdout (empty string on failure)."""
    try:
        return subprocess.run(
            ["git", "-C", str(repo), *args],
            check=True, capture_output=True, text=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def count_log_entries(md: Path) -> int:
    """Number of ``### `` headings after the ``## Logs`` heading of a prompt doc."""
    n, in_logs = 0, False
    for line in md.read_text(errors="replace").splitlines():
        if line.startswith("## Logs"):
            in_logs = True
        elif in_logs and line.startswith("### "):
            n += 1
    return n


def repo_row(name: str, repo: Path) -> dict:
    dates = git(repo, "log", "--format=%ad", "--date=short").splitlines()
    prompts = sorted((repo / "claude_prompts").rglob("*.md")) if (repo / "claude_prompts").is_dir() else []
    return {
        "repo": name,
        "branch": git(repo, "branch", "--show-current"),
        "commits": len(dates),
        "first": dates[-1] if dates else "",
        "last": dates[0] if dates else "",
        "local_branches": len([b for b in git(repo, "branch").splitlines() if b.strip()]),
        "tracked": len(git(repo, "ls-files").splitlines()),
        "dirty": len(git(repo, "status", "--porcelain").splitlines()),
        "prompt_docs": len(prompts),
        "log_entries": sum(count_log_entries(p) for p in prompts),
    }


def dir_row(rel: str, desc: str) -> dict:
    path = OS_COLOR / rel
    if not path.exists():
        return {"path": rel, "desc": desc, "gib": 0.0, "files": 0, "newest": "missing"}
    size, n, newest = 0, 0, 0.0
    for p in path.rglob("*"):
        if p.is_file():
            st = p.stat()
            size += st.st_size
            n += 1
            newest = max(newest, st.st_mtime)
    return {
        "path": rel, "desc": desc, "gib": size / 2**30, "files": n,
        "newest": dt.datetime.fromtimestamp(newest).strftime("%Y-%m-%d") if n else "",
    }


def rta_progress() -> tuple[list[dict], str]:
    """Per-variant chain counts for the RT-A sweep, plus a rate/ETA note."""
    rows = []
    for var in RTA_VARIANTS:
        n_l23 = len(list(RTA_CHAINS.glob(f"{var}_L23_*.npz"))) if RTA_CHAINS.is_dir() else 0
        n_pan = len(list(RTA_PANGAEA_CHAINS.glob(f"{var}_PANGAEA_*.npz"))) if RTA_PANGAEA_CHAINS.is_dir() else 0
        rows.append({"variant": var, "pangaea": f"{n_pan}/{N_PANGAEA}", "l23": f"{n_l23}/{N_L23}"})

    note = "RT-A log not found."
    if RTA_LOG.is_file():
        first = RTA_LOG.read_text(errors="replace").splitlines()[0]
        m = re.search(r"launch (\S+) host", first)
        done_l23 = sum(len(list(RTA_CHAINS.glob(f"{v}_L23_*.npz"))) for v in RTA_VARIANTS)
        done_pan = sum(len(list(RTA_PANGAEA_CHAINS.glob(f"{v}_PANGAEA_*.npz"))) for v in RTA_VARIANTS)
        if m:
            t0 = dt.datetime.fromisoformat(m.group(1))
            now = dt.datetime.now(t0.tzinfo)
            hours = (now - t0).total_seconds() / 3600
            done = done_l23 + done_pan
            rate = done / hours if hours > 0 else float("nan")
            remaining = len(RTA_VARIANTS) * (N_L23 + N_PANGAEA) - done
            eta = now + dt.timedelta(hours=remaining / rate) if rate > 0 else None
            note = (
                f"Launched {t0:%Y-%m-%d %H:%M}; {done} MCMC fits persisted in {hours:.1f} h "
                f"({rate:.0f} fits/h); {remaining} remaining in stage 1; "
                f"stage-1 ETA at that rate {eta:%Y-%m-%d} (metrics + report stages follow)."
            )
    return rows, note


def md_table(rows: list[dict], cols: list[tuple[str, str]], fmt: dict | None = None) -> str:
    fmt = fmt or {}
    head = "| " + " | ".join(h for _, h in cols) + " |"
    sep = "|" + "|".join("---" for _ in cols) + "|"
    body = []
    for r in rows:
        cells = []
        for key, _ in cols:
            v = r.get(key, "")
            cells.append(fmt[key](v) if key in fmt else str(v))
        body.append("| " + " | ".join(cells) + " |")
    return "\n".join([head, sep, *body])


def main() -> None:
    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    repo_rows = [repo_row(n, p) for n, p in REPOS.items() if p.is_dir()]
    dir_rows = [dir_row(rel, desc) for rel, desc in RUN_DIRS.items()]
    rta_rows, rta_note = rta_progress()

    out = [
        f"# profx inventory tables",
        "",
        f"Generated {stamp} by `claudes_phd_thesis/scripts/profx_inventory.py` on "
        f"host `{os.uname().nodename}`.  Read-only; regenerate rather than edit.",
        "",
        "## Source repositories",
        "",
        md_table(repo_rows, [
            ("repo", "repo"), ("branch", "checked-out branch"), ("commits", "commits"),
            ("first", "first commit"), ("last", "last commit"), ("local_branches", "local branches"),
            ("tracked", "tracked files"), ("dirty", "uncommitted changes"),
            ("prompt_docs", "prompt docs"), ("log_entries", "log entries"),
        ]),
        "",
        "## Output directories in the data tree (`$OS_COLOR`)",
        "",
        md_table(dir_rows, [
            ("path", "path under $OS_COLOR"), ("desc", "what it is"), ("gib", "GiB"),
            ("files", "files"), ("newest", "newest file"),
        ], fmt={"gib": lambda v: f"{v:.2f}"}),
        "",
        "## RT-A sweep progress (IOPtics `rt_tests`, launched 2026-09-10)",
        "",
        md_table(rta_rows, [("variant", "variant"), ("pangaea", "PANGAEA chains"), ("l23", "L23 chains")]),
        "",
        rta_note,
        "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(out))
    print("\n".join(out))
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
