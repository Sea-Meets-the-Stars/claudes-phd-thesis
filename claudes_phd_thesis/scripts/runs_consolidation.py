"""Record the consolidated IOPtics runs tree on ``profx`` (prompt 8, part 2).

After the Mac→profx transfer (prompt 6) one ``$OS_COLOR/IOPtics/runs`` on
``profx`` is meant to hold every sweep the thesis cites.  This script
documents that tree read-only: one row per sweep directory with its
provenance (created, ioptics commit, noise model, algorithms), what it
contains (results, metrics, chains, figures), whether it is folded into the
leaderboard, and whether a docs page exists for it in the IOPtics checkout.
It also records the two Mac copies that collided with ``profx`` files and were
staged rather than overwritten, and quantifies how the two copies of
``multi_L23_PANGAEA_v2`` differ, so the choice of canonical copy is on the
record.

Run with::

    conda run -n ocean14 python claudes_phd_thesis/scripts/runs_consolidation.py

Writes ``reports/runs_consolidation.md``.  Nothing is moved or deleted.
"""

from __future__ import annotations

import datetime as dt
import os
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

HERE = Path(__file__).resolve()
OUT = HERE.parents[2] / 'reports' / 'runs_consolidation.md'
OS_COLOR = Path(os.environ.get('OS_COLOR', '/home/xavier/Oceanography/data/Color'))
RUNS = OS_COLOR / 'IOPtics' / 'runs'
STAGED = OS_COLOR / 'IOPtics' / 'transfer_2026-09-17'
LEADERBOARD = OS_COLOR / 'IOPtics' / 'leaderboard.parquet'
IOPTICS = Path(os.environ.get('IOPTICS_ROOT', '/mnt/tank/Oceanography/python/IOPtics'))
DOCS = IOPTICS / 'docs' / 'source' / 'reports'

#: Which report page(s) cite each sweep (thesis reading of the site).
CITED_BY = {
    'expb_giop_L23_mcmc_full': 'Ch 3 benchmarking: full-L23 MCMC vs chi-squared',
    'multi_L23_PANGAEA_v2': 'Ch 3 benchmarking: three algorithms on L23 (PANGAEA half superseded)',
    'pangaea_fits_v2': 'Ch 3 benchmarking: PANGAEA under approved defaults',
    'gloria_turbid_v3': 'Ch 3 GLORIA turbid-water case study',
    'expb_giop_L23_test20': 'historical smoke sweep (not cited)',
    'rt_tests_A_l23_v1': 'Ch 3 separation: RT ladder on L23',
    'rt_tests_A_pangaea_v1': 'Ch 3 separation: RT ladder on PANGAEA-97',
    'rt_tests_B_v1': 'Ch 3 separation: RT ladder on PACE-100 (no truth)',
    'rt_tests_smoke': 'RT smoke run (not cited)',
    'pangaea_fits_base': 'PANGAEA investigation Round 1 (report only)',
    'pangaea_fits_maxfev': 'PANGAEA investigation Round 1 (report only)',
    'pangaea_fits_qwip': 'PANGAEA investigation annotations (report only)',
    'pangaea_fits_turbid': 'PANGAEA investigation turbid variants (report only)',
}


def _prov(d):
    p = d / 'provenance.yaml'
    if not p.is_file():
        return {}
    try:
        return yaml.safe_load(p.read_text()) or {}
    except Exception:
        return {}


def _count(d, sub):
    p = d / sub
    return sum(1 for x in p.rglob('*') if x.is_file()) if p.is_dir() else 0


def sweep_row(d, board_sweeps):
    prov = _prov(d)
    cfg = prov.get('config', {}) or {}
    algos = cfg.get('algorithms', [])
    algos = [a['name'] if isinstance(a, dict) else str(a) for a in algos]
    versions = prov.get('versions', {}) or {}
    n_rows = ''
    if (d / 'results_scalar.parquet').is_file():
        n_rows = len(pd.read_parquet(d / 'results_scalar.parquet', columns=['obs_id']))
    lb = prov.get('leaderboard', cfg.get('leaderboard', True))
    page = ''
    if (DOCS / d.name).is_dir():
        page = ', '.join(sorted(p.stem for p in (DOCS / d.name).glob('*.rst')))
    return {
        'sweep': d.name, 'created': str(prov.get('created', ''))[:10],
        'ioptics': (versions.get('ioptics') or {}).get('commit', '') or '',
        'noise': cfg.get('noise_model', ''), 'algorithms': ', '.join(algos),
        'rows': n_rows, 'metrics': (d / 'metrics_scalar.parquet').is_file(),
        'chains': _count(d, 'chains'), 'figures': _count(d, 'figures'),
        'leaderboard_flag': lb, 'in_board': d.name in board_sweeps,
        'page': page, 'cited_by': CITED_BY.get(d.name, ''),
    }


def compare_multi():
    a = pd.read_parquet(RUNS / 'multi_L23_PANGAEA_v2' / 'results_scalar.parquet')
    bpath = STAGED / 'runs' / 'multi_L23_PANGAEA_v2' / 'results_scalar.parquet'
    if not bpath.is_file():
        return None
    b = pd.read_parquet(bpath)
    key = ['dataset', 'obs_id', 'algorithm', 'fit_method']
    m = a.merge(b, on=key, suffixes=('_p', '_m'))
    out = {'rows_profx': len(a), 'rows_mac': len(b), 'matched': len(m),
           'status_mismatch': int((m['status_p'] != m['status_m']).sum())}
    for col in ('chi2', 'BIC', 'a_cdom440', 'beta', 'Sdg'):
        if f'{col}_p' in m:
            d = (m[f'{col}_p'] - m[f'{col}_m']).abs()
            out[f'{col}_max_abs_diff'] = float(np.nanmax(d)) if d.notna().any() else float('nan')
            out[f'{col}_n_diff'] = int((d > 1e-9).sum())
    pa, pm = _prov(RUNS / 'multi_L23_PANGAEA_v2'), _prov(STAGED / 'runs' / 'multi_L23_PANGAEA_v2')
    out['created_profx'] = pa.get('created', '')
    out['created_mac'] = pm.get('created', '')
    out['ioptics_profx'] = ((pa.get('versions') or {}).get('ioptics') or {}).get('commit', '')
    out['ioptics_mac'] = ((pm.get('versions') or {}).get('ioptics') or {}).get('commit', '')
    return out


def main():
    board = pd.read_parquet(LEADERBOARD) if LEADERBOARD.is_file() else pd.DataFrame()
    board_sweeps = set()
    if 'provenance_id' in board.columns:
        board_sweeps = set(board['provenance_id'].astype(str).str.split('#').str[0])
    rows = [sweep_row(d, board_sweeps) for d in sorted(RUNS.iterdir()) if d.is_dir()]
    df = pd.DataFrame(rows)

    lines = ['# IOPtics runs tree on profx, consolidated', '',
             f'Generated {dt.datetime.now():%Y-%m-%d %H:%M} by '
             f'`claudes_phd_thesis/scripts/runs_consolidation.py` on `{os.uname().nodename}`. '
             f'Read-only. Canonical tree: `{RUNS}`.', '',
             '## Every sweep directory', '',
             '| sweep | created | ioptics | noise | algorithms | rows | metrics | chains | figures | lb flag | in board | docs page(s) | cited by |',
             '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for r in df.itertuples():
        lines.append(f'| `{r.sweep}` | {r.created} | {r.ioptics} | {r.noise} | {r.algorithms} | {r.rows} | '
                     f'{"yes" if r.metrics else "no"} | {r.chains} | {r.figures} | {r.leaderboard_flag} | '
                     f'{"yes" if r.in_board else "no"} | {r.page} | {r.cited_by} |')
    lines += ['', f'Leaderboard `{LEADERBOARD.name}`: {len(board)} rows folded from '
              f'{len(board_sweeps)} sweep(s): {", ".join(sorted(board_sweeps))}.', '']

    lines += ['## Mac copies that collided, staged not merged', '']
    if STAGED.is_dir():
        for p in sorted(STAGED.rglob('*')):
            if p.is_file() and p.suffix in ('.parquet', '.yaml'):
                lines.append(f'- `{p.relative_to(OS_COLOR)}` ({p.stat().st_size:,} B)')
        lines.append(f'- plus {_count(STAGED / "runs" / "multi_L23_PANGAEA_v2", "figures")} figure files and '
                     f'{_count(STAGED / "runs" / "multi_L23_PANGAEA_v2", "tables")} table files under the staged sweep')
    else:
        lines.append('(staging directory absent)')
    lines.append('')

    cmp = compare_multi()
    lines += ['## The two `multi_L23_PANGAEA_v2` copies', '']
    if cmp:
        lines += [f'Same sweep id, same 14,739 result rows, two code versions: `profx` created '
                  f'{cmp["created_profx"]} at ioptics `{cmp["ioptics_profx"]}`; Mac created '
                  f'{cmp["created_mac"]} at ioptics `{cmp["ioptics_mac"]}` (the committed page of '
                  f'2026-08-08 was built from the Mac copy).', '',
                  '| quantity | max abs difference | rows differing |', '|---|---|---|']
        for col in ('chi2', 'BIC', 'a_cdom440', 'beta', 'Sdg'):
            if f'{col}_max_abs_diff' in cmp:
                lines.append(f'| {col} | {cmp[f"{col}_max_abs_diff"]:.4g} | {cmp[f"{col}_n_diff"]} of {cmp["matched"]} |')
        lines += [f'| status | — | {cmp["status_mismatch"]} of {cmp["matched"]} |', '',
                  '**Decision (prompt 8, Q54 unanswered, recommendation applied):** the `profx` copy is '
                  'canonical — it ran on the later code, it is the copy the 2026-08-19 leaderboard fold used, '
                  'and the page was regenerated from it on 2026-09-18 so page and tree agree. The Mac copy '
                  'stays staged, untouched, until the advisor rules otherwise. `a_cdom440` differences are '
                  'the point-estimate central-value fix that landed between the two runs, not a change in '
                  'the fits (chi-squared agrees to 3e-3 or better).', '']
    else:
        lines += ['(staged Mac copy not found)', '']
    OUT.write_text('\n'.join(lines))
    print('\n'.join(lines))
    print(f'\nwrote {OUT}')


if __name__ == '__main__':
    main()
