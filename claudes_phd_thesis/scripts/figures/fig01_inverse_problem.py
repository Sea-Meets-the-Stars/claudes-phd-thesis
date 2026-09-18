"""Fig 1 — what an ocean-colour spectrum is, and what has to be pulled out of it.

Two HydroLight water bodies from the Loisel et al. (2023) synthetic set (L23,
inelastic realization X=4): a clear one and a turbid one.  Left: the observable,
remote-sensing reflectance R_rs(λ).  Middle and right: the inherent optical
properties that produced it — absorption split into water, phytoplankton and
CDOM + detritus, and backscattering split into water and particles.  The
retrieval problem is the arrow from the left panel to the other two.

Data: ``$OS_COLOR/Loisel2023`` through the IOPtics L23 adapter (truth included).
The clear body is L23 index 0; the turbid one is the L23 body with the largest
chlorophyll among those RT-A fitted.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import _style as st

CAPTION = ('Ocean colour is an inverse problem: the one measurable spectrum on the left '
           'must be decomposed into the absorbing and scattering constituents on the '
           'right, and in the turbid case the water itself no longer dominates.')


def main():
    st.use_style()
    from ioptics import datasets
    ad = datasets.get_adapter('L23')
    sc = pd.read_parquet(st.RUNS / 'rt_tests_A_l23_v1' / 'results_scalar.parquet',
                         columns=['obs_id', 'Chl_truth', 'status'])
    ok = sc[sc.status == 'ok']
    turbid = int(ok.loc[ok.Chl_truth.idxmax(), 'obs_id'])
    bodies = [(0, 'clear water'), (turbid, 'turbid water')]

    fig, axes = plt.subplots(2, 3, figsize=(10.5, 5.6), sharex=True)
    for row, (idx, name) in enumerate(bodies):
        obs = ad.load_obs(idx, X=4)
        w = obs.wave
        t = {k: np.asarray(getattr(v, 'values', v), float) for k, v in obs.truth.items()
             if hasattr(getattr(v, 'values', v), '__len__')}
        chl = obs.truth['Chl']
        ax = axes[row, 0]
        ax.plot(w, obs.Rrs, color=st.INK, lw=1.8)
        ax.set_ylabel('remote-sensing reflectance\n$R_{rs}(\\lambda)$ [sr$^{-1}$]')
        ax.set_title(f'{name} — L23 body {idx}, chlorophyll {chl:.2f} mg m$^{{-3}}$',
                     loc='left', fontsize=9)
        st.note(ax, 'what the satellite measures', 'upper right')

        ax = axes[row, 1]
        ax.plot(w, t['a_w'], color=st.INK3, lw=1.4, label='pure water')
        ax.plot(w, t['a_ph'], color=st.CATEGORICAL[2], label='phytoplankton')
        ax.plot(w, t['a_dg'], color=st.CATEGORICAL[1], label='CDOM + detritus')
        ax.plot(w, t['a'], color=st.INK, lw=1.0, ls='--', label='total')
        ax.set_yscale('log')
        ax.set_ylabel(f'absorption coefficient [{st.UNIT}]')
        if row == 0:
            ax.legend(loc='lower right', ncol=2)
            st.note(ax, 'what must be retrieved (i)', 'upper left')

        ax = axes[row, 2]
        ax.plot(w, t['bb_w'], color=st.INK3, lw=1.4, label='pure water')
        ax.plot(w, t['bb_p'], color=st.CATEGORICAL[0], label='particles')
        ax.plot(w, t['bb'], color=st.INK, lw=1.0, ls='--', label='total')
        ax.set_yscale('log')
        ax.set_ylabel(f'backscattering coefficient [{st.UNIT}]')
        if row == 0:
            ax.legend(loc='lower right')
            st.note(ax, 'what must be retrieved (ii)', 'upper left')
    for ax in axes[1]:
        ax.set_xlabel('wavelength [nm]')
    fig.suptitle('One spectrum in, five constituent spectra out', fontsize=11, x=0.02, ha='left')
    fig.tight_layout()
    st.save(fig, 'fig01_inverse_problem', caption=CAPTION)


if __name__ == '__main__':
    main()
