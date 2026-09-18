"""Fig 6 — the same ladder across the spectrum, on synthetic and on in-situ data.

Mean absolute fractional error of the retrieved constituents versus wavelength
for the five rungs: top row L23 (3,300 synthetic bodies, PACE-like noise),
bottom row PANGAEA-97 (real in-situ spectra, flat 10 % error model).  Columns:
phytoplankton absorption, CDOM + detrital absorption, particulate backscattering.

Data: ``metrics_spectral.parquet`` of ``rt_tests_A_l23_v1`` and
``rt_tests_A_pangaea_v1`` (fit_method mcmc, stratum all).
"""

from __future__ import annotations

import pandas as pd
import matplotlib.pyplot as plt

import _style as st

CAPTION = ('On synthetic data the physics fixes particulate backscattering at every '
           'wavelength while the absorption split stays wrong everywhere; on real in-situ '
           'spectra the fluorescence terms move error from CDOM into phytoplankton rather '
           'than removing it.')

ARMS = [('rt_tests_A_l23_v1', 'L23 synthetic (n up to 3,300)'),
        ('rt_tests_A_pangaea_v1', 'PANGAEA in-situ (n up to 83)')]
COMPS = ['a_ph', 'a_dg', 'bb_p']


def main():
    st.use_style()
    fig, axes = plt.subplots(2, 3, figsize=(11, 6.2), sharex='col')
    for row, (sweep, title) in enumerate(ARMS):
        ms = pd.read_parquet(st.RUNS / sweep / 'metrics_spectral.parquet')
        ms = ms[(ms.fit_method == 'mcmc') & (ms.stratum == 'all')]
        for col, comp in enumerate(COMPS):
            ax = axes[row, col]
            for rung in st.RUNGS:
                r = ms[(ms.algorithm == rung) & (ms.component == comp)].sort_values('wavelength')
                r = r[r['n'] > 0]
                if r.empty:
                    continue
                ax.plot(r.wavelength, r.mae * 100, color=st.RUNG_COLOR[rung], lw=1.6,
                        marker='o' if row == 1 else None, ms=3, label=st.RUNG_LABEL[rung])
            ax.set_yscale('log')
            if row == 0:
                ax.set_title(st.COMPONENT_NAME[comp], loc='left', fontsize=9)
            if col == 0:
                ax.set_ylabel(f'{title}\nmean absolute fractional error [%]')
            if row == 1:
                ax.set_xlabel('wavelength [nm]')
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center', ncol=5, fontsize=7.5,
               title='forward model, down the ladder', title_fontsize=7.5, bbox_to_anchor=(0.5, -0.01))
    fig.suptitle('Error across the spectrum for the five forward models', fontsize=10, x=0.01, ha='left')
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    st.save(fig, 'fig06_rt_ladder_vs_wavelength', caption=CAPTION)


if __name__ == '__main__':
    main()
