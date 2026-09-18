"""Reconcile the committed RT-ladder pages against the provisional RT-A read.

``reports/rta_headline.md`` (2026-09-17) was a provisional read of the RT-A
stage-2 metrics, written before IOPtics had a report page for the ladder.  The
page now exists (``docs/source/reports/<sweep>/rt_ladder.rst`` and its
``rt_ladder_mcmc_all.csv``), and prompt 6 of ``qual_exam_prompts.md`` asks that
every number on the page be reconciled against that file and any discrepancy
reported loudly.  Both derive from the same ``metrics_scalar.parquet``, so the
expected outcome is agreement to the rounding of the CSV (4 decimals); anything
else means one of the two read the table wrongly.

Also checks the hand-typed Q1 table in ``qual_exam_prompts.md`` (L23, MCMC),
which was transcribed from the provisional read and rounded to 2-3 digits.

Run with::

    conda run -n ocean14 python claudes_phd_thesis/scripts/rta_reconcile.py

Writes ``reports/rta_reconcile.md`` and exits non-zero on any discrepancy
beyond rounding.
"""

from __future__ import annotations

import datetime as dt
import os
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve()
THESIS = HERE.parents[2]
OUT = THESIS / 'reports' / 'rta_reconcile.md'
IOPTICS = Path(os.environ.get('IOPTICS_ROOT', '/mnt/tank/Oceanography/python/IOPtics'))
RUNS = Path(os.environ.get('OS_COLOR', '/home/xavier/Oceanography/data/Color')) / 'IOPtics' / 'runs'

SWEEPS = {'rt_tests_A_l23_v1': 'L23', 'rt_tests_A_pangaea_v1': 'PANGAEA',
          'rt_tests_B_v1': 'PACE'}
CELLS = (('a', 440.0), ('a_ph', 440.0), ('a_dg', 440.0), ('bb_p', 555.0), ('bb_p', 670.0))
RUNGS = ['expb_pow_ztt_el', 'expb_pow_hyb_el', 'expb_pow_hyb_ram',
         'expb_pow_hyb_ramfl', 'expb_pow_hyb_ramflcdom']

#: The Q1 table in qual_exam_prompts.md (L23, MCMC): rung -> {cell: (mae, bias)}.
#: Transcribed by hand on 2026-09-17; checked here at its own precision.
Q1_TABLE = {
    'expb_pow_ztt_el': {'a_440': (0.053, None), 'a_ph_440': (0.91, -0.33),
                        'a_dg_440': (0.26, 0.06), 'bb_p_555': (0.55, 0.55),
                        'bb_p_670': (0.68, 0.68)},
    'expb_pow_hyb_el': {'a_440': (0.052, None), 'a_ph_440': (1.35, -0.48),
                        'a_dg_440': (0.29, 0.14), 'bb_p_555': (0.41, 0.41),
                        'bb_p_670': (0.60, 0.60)},
    'expb_pow_hyb_ram': {'a_440': (0.051, None), 'a_ph_440': (2.52, -0.69),
                         'a_dg_440': (0.38, 0.31), 'bb_p_555': (0.12, 0.10),
                         'bb_p_670': (0.26, 0.26)},
    'expb_pow_hyb_ramfl': {'a_440': (0.059, None), 'a_ph_440': (0.85, -0.38),
                           'a_dg_440': (0.26, 0.20), 'bb_p_555': (0.10, 0.06),
                           'bb_p_670': (0.18, 0.16)},
    'expb_pow_hyb_ramflcdom': {'a_440': (0.050, None), 'a_ph_440': (0.93, -0.40),
                               'a_dg_440': (0.25, 0.17), 'bb_p_555': (0.12, -0.05),
                               'bb_p_670': (0.13, 0.06)},
}


def page_csv(sweep):
    p = IOPTICS / 'docs' / 'source' / 'reports' / sweep / 'rt_ladder_mcmc_all.csv'
    return pd.read_csv(p) if p.is_file() else None


def metrics_cells(sweep):
    """The provisional read's source: metrics_scalar, MCMC, stratum all."""
    ms = pd.read_parquet(RUNS / sweep / 'metrics_scalar.parquet')
    ms = ms[(ms.fit_method == 'mcmc') & (ms.stratum == 'all')]
    out = {}
    for rung in RUNGS:
        g = ms[ms.algorithm == rung]
        row = {}
        q = g[g.component == 'Rrs']
        if not q.empty:
            row['frac_ok'] = float(q.iloc[0].frac_ok)
            row['chi2_nu_median'] = float(q.iloc[0].chi2_nu_median)
        for comp, ref in CELLS:
            c = g[(g.component == comp) & (g.ref_wave == ref) & g.n.fillna(0).gt(0)]
            if not c.empty:
                c = c.iloc[0]
                row[f'{comp}_{int(ref)}'] = (float(c.mae), float(c.bias), float(c.coverage68))
        out[rung] = row
    return out


def main() -> int:
    lines = [f'# RT-A reconciliation', '',
             f'Generated {dt.datetime.now():%Y-%m-%d %H:%M} by '
             f'`claudes_phd_thesis/scripts/rta_reconcile.py`. Compares the committed '
             f'RT-ladder page CSVs (IOPtics) against the stage-2 metrics tables the '
             f'provisional `reports/rta_headline.md` was read from, and against the '
             f'hand-typed Q1 table in `claude_prompts/qual_exam_prompts.md`.', '']
    bad = 0
    for sweep, arm in SWEEPS.items():
        lines += [f'## {arm} — `{sweep}`', '']
        page = page_csv(sweep)
        if page is None:
            lines += ['**No page CSV found.**', '']
            bad += 1
            continue
        src = metrics_cells(sweep)
        n_checked = 0
        for _, r in page.iterrows():
            rung = r['rung']
            s = src.get(rung, {})
            for key in ('frac_ok', 'chi2_nu_median'):
                if key in s and key in r and pd.notna(r[key]):
                    n_checked += 1
                    if abs(float(r[key]) - s[key]) > 5e-4:
                        bad += 1
                        lines.append(f'- **MISMATCH** {rung} {key}: page {r[key]} vs metrics {s[key]:.4f}')
            for comp, ref in CELLS:
                tag = f'{comp}_{int(ref)}'
                if tag not in s:
                    continue
                for suffix, idx in (('mae', 0), ('bias', 1), ('cov68', 2)):
                    col = f'{tag}_{suffix}'
                    if col in r and pd.notna(r[col]):
                        n_checked += 1
                        if abs(float(r[col]) - s[tag][idx]) > 5e-4:
                            bad += 1
                            lines.append(f'- **MISMATCH** {rung} {col}: page {r[col]} vs metrics {s[tag][idx]:.4f}')
        lines += [f'Page-versus-metrics cells checked: {n_checked}; mismatches so far: {bad}.', '']
        if arm == 'L23':
            q1_bad = 0
            for rung, cells in Q1_TABLE.items():
                s = src[rung]
                for tag, (mae, bias) in cells.items():
                    got_mae, got_bias = s[tag][0], s[tag][1]
                    tol_m = 0.5 * 10 ** -(len(str(mae).split('.')[1]))
                    if abs(got_mae - mae) > tol_m + 1e-9:
                        q1_bad += 1
                        lines.append(f'- **Q1 TABLE** {rung} {tag} MAE typed {mae} vs metrics {got_mae:.4f}')
                    if bias is not None:
                        tol_b = 0.5 * 10 ** -(len(str(bias).split('.')[1]))
                        if abs(got_bias - bias) > tol_b + 1e-9:
                            q1_bad += 1
                            lines.append(f'- **Q1 TABLE** {rung} {tag} bias typed {bias:+} vs metrics {got_bias:+.4f}')
            lines += [f'Q1 table (qual_exam_prompts.md) cells checked at their typed precision: '
                      f'{sum(2 if b is not None else 1 for c in Q1_TABLE.values() for _, b in c.values())}; '
                      f'discrepancies: {q1_bad}.', '']
            bad += q1_bad
    verdict = ('**All numbers agree.** The page supersedes `rta_headline.md`, which now '
               'has nothing the page lacks.' if bad == 0 else
               f'**{bad} discrepancies found — see above.**')
    lines += ['## Verdict', '', verdict, '']
    OUT.write_text('\n'.join(lines))
    print('\n'.join(lines))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
