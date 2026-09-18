"""Fig 9 — three parameterizations under one physics: totals agree, the split does not.

Left: fractional error (MAE) of three semi-analytical algorithms — BING's
ExpBricaud+power-law, GIOP, GSM — against L23 truth for total absorption,
its two constituents and particulate backscattering (χ² fits, 5 % noise,
``multi_L23_PANGAEA_v2``).  Right: the fraction of the 1,593 PANGAEA in-situ
spectra with spectral truth that each algorithm fits acceptably, under the
first scoring (flat 5 % error, out-of-scope declared after the fact) and under
the approved defaults (each record's own error with a 10 % floor, red-peaked
turbid spectra declined before fitting; ``pangaea_fits_v2``).

Data: ``metrics_scalar.parquet`` of the two sweeps.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import _style as st

CAPTION = ('Three different parameterizations retrieve total absorption to within about '
           '5–18 % but disagree by factors on the phytoplankton/CDOM split, and on real '
           'in-situ spectra half the apparent failures were an artefact of the error model, '
           'not of the algorithms.')

ALGOS = ['expb_pow', 'giop', 'gsm']
CELLS = [('a', 440.0), ('a_ph', 440.0), ('a_dg', 440.0), ('bb_p', 555.0)]


def main():
    st.use_style()
    multi = pd.read_parquet(st.RUNS / 'multi_L23_PANGAEA_v2' / 'metrics_scalar.parquet')
    pf2 = pd.read_parquet(st.RUNS / 'pangaea_fits_v2' / 'metrics_scalar.parquet')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4), gridspec_kw={'width_ratios': [1.6, 1]})

    m = multi[(multi.fit_method == 'chisq') & (multi.stratum == 'all') & (multi.dataset == 'L23')]
    x = np.arange(len(CELLS))
    w = 0.26
    for i, algo in enumerate(ALGOS):
        vals = []
        for comp, ref in CELLS:
            r = m[(m.algorithm == algo) & (m.component == comp) & (m.ref_wave == ref)]
            vals.append(float(r.mae.iloc[0]) * 100 if len(r) else np.nan)
        ax1.bar(x + (i - 1) * w, vals, width=w * 0.92, color=st.ALGO_COLOR[algo],
                edgecolor=st.SURFACE, lw=1.2, label=st.ALGO_LABEL[algo])
        for xi, v in zip(x + (i - 1) * w, vals):
            ax1.text(xi, v * 1.05, f'{v:.0f}', ha='center', va='bottom', fontsize=7, color=st.INK2)
    ax1.set_yscale('log')
    ax1.set_xticks(x)
    ax1.set_xticklabels([f'{st.COMPONENT_SHORT[c]}\n{r:g} nm' for c, r in CELLS], fontsize=8)
    ax1.set_ylabel('mean absolute fractional error vs L23 truth [%]')
    ax1.set_title('L23 synthetic, 3,300 water bodies, Gordon forward model', loc='left', fontsize=9)
    ax1.legend(loc='upper left', fontsize=7)

    def ok_rate(ms):
        q = ms[(ms.fit_method == 'chisq') & (ms.stratum == 'all') & (ms.component == 'Rrs')
               & (ms.dataset == 'PANGAEA')].set_index('algorithm')
        return [float(q.loc[a, 'frac_ok']) * 100 if a in q.index else np.nan for a in ALGOS]
    before, after = ok_rate(multi), ok_rate(pf2)
    xa = np.arange(len(ALGOS))
    ax2.bar(xa - 0.2, before, width=0.38, color=[st.ALGO_COLOR[a] for a in ALGOS], alpha=0.45,
            edgecolor=st.SURFACE, lw=1.2, label='first scoring (flat 5 % error)')
    ax2.bar(xa + 0.2, after, width=0.38, color=[st.ALGO_COLOR[a] for a in ALGOS],
            edgecolor=st.SURFACE, lw=1.2, label='approved defaults (native error, 10 % floor)')
    for xi, (b, a) in enumerate(zip(before, after)):
        ax2.text(xi - 0.2, b + 1, f'{b:.0f}', ha='center', fontsize=7.5, color=st.INK2)
        ax2.text(xi + 0.2, a + 1, f'{a:.0f}', ha='center', fontsize=7.5, color=st.INK2)
    ax2.set_xticks(xa)
    ax2.set_xticklabels(['BING', 'GIOP', 'GSM'])
    ax2.set_ylabel('in-situ spectra fitted acceptably [%]')
    ax2.set_ylim(0, 70)
    ax2.set_title('PANGAEA in-situ, 1,593 spectra: two error models', loc='left', fontsize=9)
    ax2.legend(loc='upper left', fontsize=7)
    fig.tight_layout()
    st.save(fig, 'fig09_benchmark_l23_pangaea', caption=CAPTION)


if __name__ == '__main__':
    main()
