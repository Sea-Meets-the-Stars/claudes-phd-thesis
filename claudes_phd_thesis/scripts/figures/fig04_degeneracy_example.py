"""Fig 4 — two physics, one spectrum, two decompositions.

One L23 water body from the RT-A sweep, fitted with the same parameterization
under the elastic hybrid forward model and under the full inelastic one.  Top:
the observed reflectance with both model spectra laid over it — both fit to
reduced chi-squared near 1.  Bottom: the retrieved phytoplankton and CDOM +
detrital absorption under each, with the HydroLight truth.  The spectrum is
chosen automatically: among bodies both rungs fit to χ²ν within 15 % of 1, the
one where the two retrievals of a_ph(445) disagree most.

Data: ``$OS_COLOR/IOPtics/runs/rt_tests_A_l23_v1/results_{scalar,spectral}.parquet``.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import _style as st

CAPTION = ('Two forward models fit the same reflectance equally well and return different '
           'phytoplankton and CDOM absorption: the fit quality cannot tell them apart, '
           'which is what makes the decomposition a parameterization problem rather than '
           'a physics one.')

A, B = st.ELASTIC, st.FULL


def pick_obs(sc):
    m = sc[(sc.fit_method == 'mcmc') & (sc.status == 'ok') & sc.algorithm.isin([A, B])]
    piv = m.pivot_table(index='obs_id', columns='algorithm', values='chi2_nu')
    good = piv[(piv.sub(1.0).abs() < 0.15).all(axis=1)].index
    return sorted(int(i) for i in good)


def main():
    st.use_style()
    d = st.RUNS / 'rt_tests_A_l23_v1'
    sc = pd.read_parquet(d / 'results_scalar.parquet',
                         columns=['obs_id', 'algorithm', 'fit_method', 'chi2_nu', 'status', 'Chl_truth'])
    cands = pick_obs(sc)
    # a_ph at the band nearest 445 nm for both rungs, MCMC, over the candidates
    sp = pd.read_parquet(d / 'results_spectral.parquet',
                         filters=[('fit_method', '==', 'mcmc'), ('algorithm', 'in', [A, B]),
                                  ('component', '==', 'a_ph'), ('wavelength', '==', 445.0)])
    sp = sp[sp.obs_id.astype(int).isin(cands)]
    piv = sp.pivot_table(index='obs_id', columns='algorithm', values='value')
    piv = piv[(piv > 0).all(axis=1)]
    # prefer a mid-chlorophyll body so the example is typical, then the largest disagreement
    chl = sc.drop_duplicates('obs_id').set_index('obs_id')['Chl_truth']
    piv['ratio'] = np.abs(np.log10(piv[B] / piv[A]))
    piv['chl'] = chl.reindex(piv.index.astype(int)).to_numpy()
    mid = piv[(piv.chl > 0.1) & (piv.chl < 1.0)]
    obs = int((mid if len(mid) else piv)['ratio'].idxmax())

    full = pd.read_parquet(d / 'results_spectral.parquet',
                           filters=[('obs_id', '==', obs), ('fit_method', '==', 'mcmc'),
                                    ('algorithm', 'in', [A, B])])
    chi = sc[(sc.obs_id == obs) & (sc.fit_method == 'mcmc')].set_index('algorithm')['chi2_nu']

    fig, axes = plt.subplots(1, 3, figsize=(11, 3.9))
    ax = axes[0]
    obs_rrs = full[(full.algorithm == A) & (full.component == 'Rrs_obs')].sort_values('wavelength')
    ax.plot(obs_rrs.wavelength, obs_rrs.value, 'o', ms=3, color=st.INK, label='observed (L23 X=4)')
    for rung, ls in ((A, '-'), (B, '--')):
        mod = full[(full.algorithm == rung) & (full.component == 'Rrs_model')].sort_values('wavelength')
        ax.plot(mod.wavelength, mod.value, ls, color=st.RUNG_COLOR[rung], lw=1.8,
                label=f'{st.RUNG_LABEL[rung]}  (χ²ν = {chi.get(rung, np.nan):.2f})')
    ax.set_ylabel('remote-sensing reflectance $R_{rs}$ [sr$^{-1}$]')
    ax.set_xlabel('wavelength [nm]')
    ax.set_title(f'the same fit quality (L23 body {obs})', loc='left', fontsize=9)
    st.note(ax, f'chlorophyll {chl.get(obs, np.nan):.2f} mg m$^{{-3}}$', 'lower left')
    ax.legend(loc='upper right', fontsize=7)

    for ax, comp in zip(axes[1:], ('a_ph', 'a_dg')):
        tr = full[(full.algorithm == A) & (full.component == comp)].sort_values('wavelength')
        ax.plot(tr.wavelength, tr.truth, color=st.INK, lw=1.4, ls=':', label='HydroLight truth')
        for rung, ls in ((A, '-'), (B, '--')):
            r = full[(full.algorithm == rung) & (full.component == comp)].sort_values('wavelength')
            ax.plot(r.wavelength, r.value, ls, color=st.RUNG_COLOR[rung], lw=1.8,
                    label=st.RUNG_LABEL[rung])
            ax.fill_between(r.wavelength, r.lo68, r.hi68, color=st.RUNG_COLOR[rung], alpha=0.15, lw=0)
        ax.set_yscale('log')
        ax.set_xlabel('wavelength [nm]')
        ax.set_ylabel(st.component_label(comp))
        ax.set_title('a different decomposition' + (' (i)' if comp == 'a_ph' else ' (ii)'),
                     loc='left', fontsize=9)
    axes[1].legend(loc='lower left', fontsize=7)
    fig.tight_layout()
    st.save(fig, 'fig04_degeneracy_example', caption=CAPTION)
    print('chosen obs', obs)


if __name__ == '__main__':
    main()
