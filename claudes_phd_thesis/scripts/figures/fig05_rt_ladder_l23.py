"""Fig 5 — the RT ladder on L23: what the physics fixes and what it does not.

For each of the five radiative-transfer rungs (same parameterization, more
physics down the ladder) the fractional error of the retrieved constituents
against HydroLight truth on 3,300 water bodies: mean absolute error (bars) and
signed bias (markers), MCMC medians.  Components: total absorption, the two
absorption constituents, and particulate backscattering, at the reference bands.

Data: ``$OS_COLOR/IOPtics/runs/rt_tests_A_l23_v1/metrics_scalar.parquet``
(fit_method mcmc, stratum all) — the same table the IOPtics ladder page shows.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import _style as st

CAPTION = ('Adding the missing physics removes the particulate-backscatter error almost '
           'entirely (+55 % to about 0) but leaves the phytoplankton and CDOM absorption '
           'errors where they were: the first is a physics failure, the second is not.')

CELLS = [('a', 440.0), ('a_ph', 440.0), ('a_dg', 440.0), ('bb_p', 555.0)]


def main():
    st.use_style()
    ms = pd.read_parquet(st.RUNS / 'rt_tests_A_l23_v1' / 'metrics_scalar.parquet')
    ms = ms[(ms.fit_method == 'mcmc') & (ms.stratum == 'all')]
    fig, axes = plt.subplots(1, len(CELLS), figsize=(11.5, 3.9), sharey=False)
    x = np.arange(len(st.RUNGS))
    for ax, (comp, ref) in zip(axes, CELLS):
        rows = ms[(ms.component == comp) & (ms.ref_wave == ref)].set_index('algorithm')
        mae = np.array([rows.loc[r, 'mae'] if r in rows.index else np.nan for r in st.RUNGS])
        bias = np.array([rows.loc[r, 'bias'] if r in rows.index else np.nan for r in st.RUNGS])
        n = int(rows['n'].max())
        ax.bar(x, mae * 100, width=0.62, color=[st.RUNG_COLOR[r] for r in st.RUNGS],
               edgecolor=st.SURFACE, linewidth=1.5, label='mean absolute error')
        ax.scatter(x, bias * 100, marker='D', s=34, color=st.INK, zorder=3, label='signed bias')
        ax.axhline(0, color=st.INK3, lw=0.8)
        for xi, (m, b) in enumerate(zip(mae, bias)):
            ax.text(xi, m * 100 + 3, f'{m * 100:.0f}', ha='center', va='bottom', fontsize=7.5, color=st.INK2)
        ax.set_xticks(x)
        ax.set_xticklabels(['elastic\nanalytic', 'elastic\nhybrid', '+Raman', '+Chl\nfluor.', '+CDOM\nfluor.'],
                           fontsize=7)
        ax.set_title(f'{st.COMPONENT_NAME[comp]} at {ref:g} nm', loc='left', fontsize=9)
        ax.set_ylabel('fractional error vs truth [%]')
        ymax = np.nanmax(mae) * 100
        ax.set_ylim(min(np.nanmin(bias) * 100, 0) - 8, ymax * 1.25 + 8)
        st.note(ax, f'n = {n:,} water bodies', 'upper right')
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center', ncol=2, bbox_to_anchor=(0.5, -0.02))
    fig.suptitle('Five forward models, one parameterization, L23 synthetic truth — '
                 'error moves down the ladder only where the physics was the problem',
                 fontsize=10, x=0.01, ha='left')
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    st.save(fig, 'fig05_rt_ladder_l23', caption=CAPTION)


if __name__ == '__main__':
    main()
