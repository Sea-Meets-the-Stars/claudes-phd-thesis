"""The citation manifest: every sweep and report the thesis cites, and where it lives.

Prompt 8 of ``claude_prompts/qual_exam_prompts.md`` (A18: citations point at
``main`` and the advisor will make the links work).  For every artefact the
report and dissertation will cite, this records the ``main``-relative path in
its repository, whether it is on ``main`` today, and if not, the branch it
currently lives on with the short hash of the last commit that touched it there.
The rows that are not on ``main`` are the merge list.  Data products that live
outside git (``$OS_COLOR`` sweep outputs) are listed separately with the
``ioptics`` commit their provenance records.

Run on ``profx`` (canonical) with::

    conda run -n ocean14 python claudes_phd_thesis/scripts/citation_manifest.py

Writes ``reports/citation_manifest.md``.  Read-only git.
"""

from __future__ import annotations

import datetime as dt
import os
import subprocess
from pathlib import Path

import yaml

HERE = Path(__file__).resolve()
THESIS = HERE.parents[2]
OUT = THESIS / 'reports' / 'citation_manifest.md'
PY = Path.home() / 'Oceanography' / 'python'
OS_COLOR = Path(os.environ.get('OS_COLOR', '/home/xavier/Oceanography/data/Color'))

REPOS = {
    'IOPtics': PY / 'IOPtics', 'retrieve-or-bust': PY / 'retrieve-or-bust',
    'PAB': PY / 'PAB', 'bing': PY / 'bing', 'EPFT-UP': PY / 'EPFT-UP',
    'ocpy': PY / 'ocpy', 'claudes-phd-thesis': THESIS,
}

#: (repo, path, chapter, what it is).  Paths are repository-relative.
CITATIONS = [
    # ---- Ch 2: the differentiable RT forward model (retrieve-or-bust) --------
    ('retrieve-or-bust', 'reports/report_rt_elastic_model.md', 'Ch 2', 'elastic forward model report v1.0 (0.30 % rRMS)'),
    ('retrieve-or-bust', 'reports/report_rt_inelastic_model.md', 'Ch 2', 'inelastic forward model report v1.0 (0.34 % rRMS) + M5 addendum'),
    ('retrieve-or-bust', 'design/rt_elastic_model.md', 'Ch 2', 'elastic design document'),
    ('retrieve-or-bust', 'design/rt_inelastic_model.md', 'Ch 2', 'inelastic design document'),
    ('retrieve-or-bust', 'design/rt_cdom_fluorescence_model.md', 'Ch 2', 'CDOM fluorescence design (M5)'),
    ('retrieve-or-bust', 'design/validation/metrics.md', 'Ch 2', 'elastic validation table'),
    ('retrieve-or-bust', 'design/validation/metrics_inelastic.md', 'Ch 2', 'inelastic validation table'),
    ('retrieve-or-bust', 'robust/rt/files/emulator_l23.npz', 'Ch 2', 'trained emulator weights (417 parameters)'),
    ('retrieve-or-bust', 'robust/rt/files/raman_corr_l23.npz', 'Ch 2', 'Raman correction head'),
    ('retrieve-or-bust', 'robust/rt/files/fl_corr_l23.npz', 'Ch 2', 'fluorescence correction head'),
    ('retrieve-or-bust', 'robust/rt/data/ed_l23.npz', 'Ch 2', 'packaged E_d table used by every RT sweep'),
    ('retrieve-or-bust', 'robust/rt/emulator.py', 'Ch 2', 'emulator incl. the 2026-09-15 off-nadir fix'),
    ('retrieve-or-bust', 'robust/solar.py', 'Ch 2', 'NOAA solar zenith used for PANGAEA/PACE geometry'),
    ('retrieve-or-bust', 'docs/using/limitations.md', 'Ch 2', 'the forward/inversion boundary in RoB\'s words'),
    # ---- Ch 2 extensions to BING ---------------------------------------------
    ('bing', 'docs/radiative_transfer.rst', 'Ch 2', 'RT backends, inelastic terms, CDOM fluorescence'),
    ('bing', 'bing/rt/defs.py', 'Ch 2', 'rt_dict incl. rt_backend / fit_Bp / include_CDOM_fl'),
    ('bing', 'bing/evaluate.py', 'Ch 2', 'robust-backend dispatch'),
    ('bing', 'bing/tests/test_l23_inelastic.py', 'Ch 2', 'L23-anchored inelastic regression (1/pi fix)'),
    ('bing', 'claude_prompts/inelastic_fixes.md', 'Ch 2', 'provenance of the fluorescence/Raman fixes'),
    ('bing', 'bing/models/bbnw.py', 'Ch 3', 'turbid-water bb_p models Pow2 / Pow2Flat / PowFlex'),
    ('bing', 'claude_prompts/turbid_waters.md', 'Ch 3', 'provenance of the turbid-water models'),
    # ---- Ch 3: the separation (RT ladder) -------------------------------------
    ('IOPtics', 'docs/source/reports/rt_tests_A_l23_v1/rt_ladder.rst', 'Ch 3', 'RT ladder, L23 X=4 (3,320 spectra)'),
    ('IOPtics', 'docs/source/reports/rt_tests_A_pangaea_v1/rt_ladder.rst', 'Ch 3', 'RT ladder, PANGAEA-97'),
    ('IOPtics', 'docs/source/reports/rt_tests_B_v1/rt_ladder.rst', 'Ch 3', 'RT ladder, PACE-100 (no truth) + PAB consistency'),
    ('IOPtics', 'ioptics/report/rt_ladder.py', 'Ch 3', 'the RT-ladder page type'),
    ('IOPtics', 'ioptics/runs/prototypes/rt_tests/run_rta_l23.yaml', 'Ch 3', 'RT-A L23 sweep config'),
    ('IOPtics', 'ioptics/runs/prototypes/rt_tests/run_rta_pangaea.yaml', 'Ch 3', 'RT-A PANGAEA sweep config'),
    ('IOPtics', 'ioptics/runs/prototypes/rt_tests/run_rtb.yaml', 'Ch 3', 'RT-B PACE sweep config'),
    ('IOPtics', 'ioptics/runs/prototypes/rt_tests/pangaea97_ids.csv', 'Ch 3', 'frozen PANGAEA-97 population'),
    ('IOPtics', 'ioptics/runs/prototypes/rt_tests/pace100_ids.csv', 'Ch 3', 'frozen PACE-100 population'),
    ('IOPtics', 'ioptics/runs/prototypes/rt_tests/pab_consistency.py', 'Ch 3', 'RT-B vs PAB run1k consistency check'),
    ('IOPtics', 'ioptics/algorithms/registry.py', 'Ch 3', 'the five RT variants and RT_DBIC_PAIR'),
    ('IOPtics', 'claude_prompts/rt_tests.md', 'Ch 3', 'design decisions Q1–Q55 and run logs'),
    # ---- Ch 3: benchmarking (L23 / PANGAEA / GLORIA) --------------------------
    ('IOPtics', 'docs/source/reports/expb_giop_L23_mcmc_full/cross_algorithm.rst', 'Ch 3', 'full-L23 MCMC vs chi-squared, expb_pow vs giop'),
    ('IOPtics', 'docs/source/reports/multi_L23_PANGAEA_v2/cross_algorithm.rst', 'Ch 3', 'three algorithms on L23 (+ superseded PANGAEA half)'),
    ('IOPtics', 'docs/source/reports/pangaea_fits_v2/cross_algorithm.rst', 'Ch 3', 'PANGAEA under approved defaults (43/53/38 % ok)'),
    ('IOPtics', 'docs/source/reports/gloria_turbid_v3/cross_algorithm.rst', 'Ch 3', 'GLORIA turbid sweep: four bb_p models, one fit'),
    ('IOPtics', 'docs/source/reports/gloria_investigation.rst', 'Ch 3', 'GLORIA investigation (converted report, with editorial warning)'),
    ('IOPtics', 'docs/source/reports/index.rst', 'Ch 3', 'cross-sweep leaderboard landing page'),
    ('IOPtics', 'reports/gloria_fits_report.md', 'Ch 3', 'GLORIA investigation report (markdown original)'),
    ('IOPtics', 'reports/pangaea_fits_report.md', 'Ch 3', 'PANGAEA investigation report'),
    ('IOPtics', 'docs/design/IOPtics_design.md', 'Ch 3', 'benchmarking framework design'),
    ('IOPtics', 'docs/design/IOPtics_implementation.md', 'Ch 3', 'benchmarking framework implementation record'),
    ('IOPtics', 'claude_prompts/LS2/ls2_prompts.md', 'Ch 3', 'LS2 planning (future work) — written on the Mac 2026-09-17, untracked on its `ls2` branch; not on profx'),
    ('ocpy', 'ocpy/ls2/ls2_main.py', 'Ch 3', 'the existing LS2 implementation (Loisel 2018 port)'),
    # ---- Ch 4: EPFT-UP / MOANA ------------------------------------------------
    ('EPFT-UP', 'reports/MOANA_Claude_Report.md', 'Ch 4', 'MOANA reimplementation report (rev 4)'),
    ('EPFT-UP', 'reports/moana_rederivation.md', 'Ch 4', 're-derivation audit: 35 numbers, 6 figures reproduced'),
    ('EPFT-UP', 'reports/moana_blocked.md', 'Ch 4', 'what blocks the retrain (PML data)'),
    ('EPFT-UP', 'README.md', 'Ch 4', 'the EPFT-UP framework statement'),
    # ---- Ch 5: PAB ------------------------------------------------------------
    ('PAB', 'reports/PAB/pab_chl_matchups_report.md', 'Ch 5', 'PACE vs BGC-Argo Chl-a report (2026-09-07)'),
    ('PAB', 'reports/PAB/pab_cdom_matchups_report.md', 'Ch 5', 'PACE vs BGC-Argo CDOM report v1.0 (qualitative)'),
    ('PAB', 'docs/design/PAB_full_run_report.md', 'Ch 5', 'production run close-out (pab_version 1.0)'),
    ('PAB', 'docs/design/PAB_design.md', 'Ch 5', 'PAB design document'),
    ('PAB', 'claude_prompts/pace_giop_gsm.md', 'Ch 5', 'NASA GIOP retrofit (BING vs GIOP)'),
    ('PAB', 'claude_prompts/hyper_matchups.md', 'Ch 5', 'hyperspectral floats + the match truncation finding'),
    ('PAB', 'claude_prompts/v2/run_full_inelastic.md', 'Ch 5', 'PAB 2.0 plan'),
    ('PAB', 'claude_prompts/v2/build_v2_prompt_3.md', 'Ch 5', 'PAB 2.0 first real fits (2.0 vs 1.0 bb_p)'),
    # ---- Provenance of the thesis itself --------------------------------------
    ('claudes-phd-thesis', 'claude_prompts/start_up.md', 'Ch 1/6', 'scoping interview and Report'),
    ('claudes-phd-thesis', 'claude_prompts/qual_exam_prompts.md', 'Ch 1/6', 'qualifying-exam Q&A rounds 1–4 and prompts'),
    ('claudes-phd-thesis', 'claude_prompts/profx_inventory.md', 'Ch 1/6', 'inventory of Claude\'s work on profx'),
    ('claudes-phd-thesis', 'reports/rta_reconcile.md', 'Ch 3', 'RT-A page vs provisional read reconciliation'),
    ('claudes-phd-thesis', 'reports/citation_manifest.md', 'all', 'this manifest'),
]

#: Sweep outputs the pages were built from (outside git).
DATA = ['expb_giop_L23_mcmc_full', 'multi_L23_PANGAEA_v2', 'pangaea_fits_v2',
        'gloria_turbid_v3', 'rt_tests_A_l23_v1', 'rt_tests_A_pangaea_v1', 'rt_tests_B_v1']


def git(repo, *args):
    try:
        return subprocess.run(['git', '-C', str(repo), *args], capture_output=True,
                              text=True, timeout=60).stdout.strip()
    except Exception:
        return ''


def branches(repo):
    """Checked-out branch first, then local branches, then remote ones."""
    cur = git(repo, 'branch', '--show-current')
    local = [b.strip('* ').strip() for b in git(repo, 'branch').splitlines() if b.strip()]
    remote = [b.strip() for b in git(repo, 'branch', '-r').splitlines()
              if b.strip() and '->' not in b]
    seen, out = set(), []
    for b in [cur] + local + remote:
        if b and b not in seen:
            seen.add(b)
            out.append(b)
    return out


def on_ref(repo, ref, path):
    return subprocess.run(['git', '-C', str(repo), 'cat-file', '-e', f'{ref}:{path}'],
                          capture_output=True).returncode == 0


def locate(repo, path):
    """(on_main, branch, short_hash, note) for one path."""
    main_ref = 'origin/main' if git(repo, 'rev-parse', '--verify', '-q', 'origin/main') else 'main'
    if on_ref(repo, main_ref, path):
        h = git(repo, 'log', '-1', '--format=%h', main_ref, '--', path)
        return True, main_ref, h, ''
    for b in branches(repo):
        if b in ('main', 'origin/main'):
            continue
        if on_ref(repo, b, path):
            h = git(repo, 'log', '-1', '--format=%h', b, '--', path)
            return False, b, h, ''
    if (Path(repo) / path).exists() or path == str(OUT.relative_to(THESIS)):
        return False, git(repo, 'branch', '--show-current'), '', 'uncommitted (working tree only)'
    return False, '', '', 'NOT FOUND on this machine'


def main():
    rows = []
    for repo_name, path, chapter, what in CITATIONS:
        repo = REPOS[repo_name]
        on_main, branch, h, note = locate(repo, path)
        rows.append((repo_name, path, chapter, what, on_main, branch, h, note))
    lines = ['# Citation manifest', '',
             f'Generated {dt.datetime.now():%Y-%m-%d %H:%M} by '
             f'`claudes_phd_thesis/scripts/citation_manifest.py` on `{os.uname().nodename}`.  '
             f'Read-only git.  Citations in the report point at `main` (A18); a row whose '
             f'`on main` is **no** is on the merge list — the branch and hash say where it '
             f'lives today.  `origin/main` is used where the remote exists, since that is what a '
             f'reader will fetch.', '']
    n_off = sum(1 for r in rows if not r[4])
    lines += [f'**{len(rows)} citations; {n_off} not yet on `main`.**', '',
              '| # | repository | path (main-relative) | chapter | what | on main | lives on | hash | note |',
              '|---|---|---|---|---|---|---|---|---|']
    for i, (repo_name, path, chapter, what, on_main, branch, h, note) in enumerate(rows, 1):
        lines.append(f'| {i} | {repo_name} | `{path}` | {chapter} | {what} | '
                     f'{"yes" if on_main else "**no**"} | `{branch}` | {h} | {note} |')
    # merge list
    lines += ['', '## Merge list (what must reach `main` for the citations to resolve)', '']
    by_repo = {}
    for repo_name, path, chapter, what, on_main, branch, h, note in rows:
        if not on_main:
            by_repo.setdefault(repo_name, {}).setdefault(branch or '(uncommitted)', []).append(path)
    for repo_name, br in by_repo.items():
        lines.append(f'- **{repo_name}**: ' + '; '.join(f'`{b}` ({len(ps)} path(s))' for b, ps in br.items()))
    if not by_repo:
        lines.append('(everything is on main)')
    # data
    lines += ['', '## Sweep outputs outside git (`$OS_COLOR/IOPtics/runs/`)', '',
              '| sweep | created | ioptics commit | bing commit | rows | page |', '|---|---|---|---|---|---|']
    for sid in DATA:
        d = OS_COLOR / 'IOPtics' / 'runs' / sid
        prov = {}
        if (d / 'provenance.yaml').is_file():
            try:
                prov = yaml.safe_load((d / 'provenance.yaml').read_text()) or {}
            except Exception:
                prov = {}
        v = prov.get('versions', {}) or {}
        page = REPOS['IOPtics'] / 'docs' / 'source' / 'reports' / sid
        pages = ', '.join(sorted(p.stem for p in page.glob('*.rst'))) if page.is_dir() else '(none)'
        import pandas as pd
        n = len(pd.read_parquet(d / 'results_scalar.parquet', columns=['obs_id'])) if (d / 'results_scalar.parquet').is_file() else ''
        lines.append(f'| `{sid}` | {str(prov.get("created", ""))[:10]} | {(v.get("ioptics") or {}).get("commit", "")} | '
                     f'{(v.get("bing") or {}).get("commit", "")} | {n} | {pages} |')
    lines += ['', 'These are not in any repository by design (parquet + chains); the page carries their '
              'provenance stamp, and `reports/runs_consolidation.md` records the tree they sit in.', '']
    OUT.write_text('\n'.join(lines))
    print('\n'.join(lines[:8]))
    for r in rows:
        if not r[4]:
            print(f'  off main: {r[0]}:{r[1]} -> {r[5]} {r[6]} {r[7]}')
    print(f'\nwrote {OUT}')


if __name__ == '__main__':
    main()
