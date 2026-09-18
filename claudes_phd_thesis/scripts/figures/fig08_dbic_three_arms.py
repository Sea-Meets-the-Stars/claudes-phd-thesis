"""Fig 8 — which physics the data prefer, on three kinds of spectra.

Per-spectrum ΔBIC = BIC(full inelastic) − BIC(elastic hybrid), MCMC, for the
three RT-A/RT-B arms: L23 synthetic (3,300), PANGAEA in-situ (72), PACE
satellite (99).  Both rungs have the same number of parameters, so this is a
pure likelihood contest; negative favours the inelastic physics, and |ΔBIC| > 10
is the conventional strong-evidence threshold (shaded band is weaker than that).

Data: ``results_scalar.parquet`` of the three sweeps.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import _style as st

CAPTION = ('The data prefer the fuller physics on synthetic spectra that contain it, are '
           'indifferent on sparse in-situ spectra, and split on real satellite pixels, so '
           'fit quality alone would never have found the forward-model error that the '
           'truth-referenced test shows.')

ARMS = [('rt_tests_A_l23_v1', 'L23 synthetic'), ('rt_tests_A_pangaea_v1', 'PANGAEA in-situ'),
        ('rt_tests_B_v1', 'PACE satellite')]
A, B = st.ELASTIC, st.FULL


def dbic(sweep):
    sc = pd.read_parquet(st.RUNS / sweep / 'results_scalar.parquet',
                         columns=['obs_id', 'algorithm', 'fit_method', 'BIC', 'status'])
    sc = sc[(sc.fit_method == 'mcmc') & (sc.status == 'ok') & sc.algorithm.isin([A, B])]
    p = sc.pivot_table(index='obs_id', columns='algorithm', values='BIC').dropna()
    return (p[B] - p[A]).to_numpy(float)


def main():
    st.use_style()
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.7))
    clip = 40
    edges = np.linspace(-clip, clip, 41)
    for ax, (sweep, title) in zip(axes, ARMS):
        d = dbic(sweep)
        ax.hist(np.clip(d, -clip, clip), bins=edges, color=st.CATEGORICAL[0], alpha=0.9,
                edgecolor=st.SURFACE, lw=0.6)
        ax.axvspan(-10, 10, color=st.INK, alpha=0.06, lw=0)
        ax.axvline(0, color=st.INK3, lw=0.9)
        fav = np.mean(d < 0)
        strong_a, strong_b = np.mean(d < -10), np.mean(d > 10)
        st.note(ax, f'n = {d.size}\nfavour inelastic: {fav:.0%}\nstrongly (< −10): {strong_a:.0%}\n'
                    f'strongly against (> +10): {strong_b:.0%}\nmedian ΔBIC {np.median(d):+.1f}', 'upper left')
        ax.set_ylim(top=ax.get_ylim()[1] * 1.35)
        ax.set_title(title, loc='left', fontsize=9)
        ax.set_xlabel('ΔBIC = BIC(full inelastic) − BIC(elastic)\n(negative favours the inelastic physics)')
    axes[0].set_ylabel('spectra')
    fig.suptitle('Does the fit itself prefer the fuller physics?  Same parameterization, equal parameter count',
                 fontsize=10, x=0.01, ha='left')
    fig.tight_layout()
    st.save(fig, 'fig08_dbic_three_arms', caption=CAPTION)


if __name__ == '__main__':
    main()
