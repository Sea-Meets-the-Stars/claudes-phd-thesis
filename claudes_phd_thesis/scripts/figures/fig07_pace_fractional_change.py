"""Fig 7 — how far the physics moves a real PACE retrieval (no truth needed).

For 99 real PACE OCI pixels (PAB run1k matchups), the ratio of each retrieved
constituent under the full inelastic forward model to that under the elastic
hybrid, at the band nearest 443 nm, MCMC medians.  Log-ratio axis with the
end bins folded; the dashed line is the median, the shaded band the 16–84 %
span.  Data: ``$OS_COLOR/IOPtics/runs/rt_tests_B_v1/results_spectral.parquet``.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import _style as st

CAPTION = ('On real satellite spectra the choice of forward model moves the retrieved '
           'particulate backscatter down by about a fifth and leaves the absorption '
           'constituents nearly unchanged on average but with a wide spread, so the '
           'physics matters for what is claimed pixel by pixel.')

COMPS = ['a_ph', 'a_dg', 'bb_p']
A, B = st.ELASTIC, st.FULL


def main():
    st.use_style()
    sp = pd.read_parquet(st.RUNS / 'rt_tests_B_v1' / 'results_spectral.parquet',
                         filters=[('fit_method', '==', 'mcmc'), ('algorithm', 'in', [A, B]),
                                  ('component', 'in', COMPS)])
    waves = np.sort(sp.wavelength.unique())
    band = float(waves[np.argmin(np.abs(waves - 443.0))])
    at = sp[np.isclose(sp.wavelength, band)]
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.7))
    edges = np.linspace(-1.0, 1.0, 33)
    ticks = [-1, -0.5, 0, 0.5, 1]
    for ax, comp in zip(axes, COMPS):
        c = at[at.component == comp]
        a = c[c.algorithm == A][['obs_id', 'value']]
        b = c[c.algorithm == B][['obs_id', 'value']]
        m = a.merge(b, on='obs_id', suffixes=('_a', '_b'))
        ratio = (m.value_b / m.value_a).to_numpy(float)
        ratio = ratio[np.isfinite(ratio) & (ratio > 0)]
        dex = np.log10(ratio)
        folded = np.clip(dex, -1, 1)
        ax.hist(folded, bins=edges, color=st.RUNG_COLOR[B], alpha=0.9, edgecolor=st.SURFACE, lw=0.6)
        med, p16, p84 = np.percentile(dex, [50, 16, 84])
        ax.axvspan(p16, p84, color=st.INK, alpha=0.07, lw=0)
        ax.axvline(0, color=st.INK3, lw=0.9)
        ax.axvline(med, color=st.INK, lw=1.2, ls='--')
        ax.set_xticks(ticks)
        ax.set_xticklabels([f'{10 ** t:.2g}×' for t in ticks])
        ax.set_xlabel('retrieved with full inelastic physics ÷ retrieved elastic')
        ax.set_title(f'{st.COMPONENT_NAME[comp]} at {band:g} nm', loc='left', fontsize=9)
        n_fold = int((np.abs(dex) > 1).sum())
        st.note(ax, f'n = {ratio.size} pixels\nmedian {10 ** med - 1:+.0%}\n'
                    f'16–84 %: {10 ** p16 - 1:+.0%} … {10 ** p84 - 1:+.0%}'
                    + (f'\n{n_fold} beyond axis' if n_fold else ''), 'upper left')
    axes[0].set_ylabel('PACE pixels')
    fig.suptitle('Same parameterization, two forward models, 99 real PACE pixels: how much the physics moves the answer',
                 fontsize=10, x=0.01, ha='left')
    fig.tight_layout()
    st.save(fig, 'fig07_pace_fractional_change', caption=CAPTION)


if __name__ == '__main__':
    main()
