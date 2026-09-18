"""Fig 2 — how accurately each forward model reproduces HydroLight reflectance.

Relative RMS error of R_rs against the L23 HydroLight truth as a function of
wavelength, for the models in the retrieve-or-bust elastic report: the fixed
Gordon (1988) relation every semi-analytical retrieval has used, the analytic
Zaneveld/Twardowski-Tonizzo backbone, the O25 form refit on L23, and the hybrid
(backbone + 417-parameter emulator).  Inset text: the held-out summary numbers.

Data: ``retrieve-or-bust/design/validation/rrms_per_wavelength.csv`` and
``metrics.csv`` (report v1.0, 2026-08-15).
"""

from __future__ import annotations

import pandas as pd
import matplotlib.pyplot as plt

import _style as st

CAPTION = ('The forward-model error term can be driven from 7 % (the Gordon relation '
           'every retrieval has used) to 0.3 % with a differentiable hybrid model, so '
           'whatever retrieval error remains after that is not the physics.')

SERIES = [('standard Gordon', 'Gordon (1988), fixed coefficients', st.INK3, '-'),
          ('ZTT backbone', 'analytic backbone (ZTT)', st.CATEGORICAL[1], '-'),
          ('O25 form, refit on L23', 'O25 form, refit on L23', st.CATEGORICAL[2], '--'),
          ('hybrid, MLP', 'hybrid: backbone + emulator (this work)', st.CATEGORICAL[0], '-')]


def main():
    st.use_style()
    d = st.PY / 'retrieve-or-bust' / 'design' / 'validation'
    per = pd.read_csv(d / 'rrms_per_wavelength.csv')
    met = pd.read_csv(d / 'metrics.csv')
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    for col, label, color, ls in SERIES:
        ax.plot(per['wavelength_nm'], per[col], color=color, ls=ls, label=label,
                lw=2.2 if 'hybrid' in col else 1.6)
    ax.set_yscale('log')
    ax.set_xlabel('wavelength [nm]')
    ax.set_ylabel('relative RMS error of modelled $R_{rs}$ vs HydroLight [%]')
    ax.set_xlim(350, 760)
    ax.set_title('Forward model accuracy on 9,960 synthetic water bodies (train + held-out)',
                 loc='left', fontsize=9.5)
    held = met[met['split'] == 'held-out scenes'].set_index('model')['rrms_percent']
    z60 = met[met['split'] == 'held-out @60'].set_index('model')['rrms_percent']
    txt = 'held-out scenes / held-out at 60° sun:\n' + '\n'.join(
        f"{lab.split(' (')[0].split(':')[0]}: {held[col]:.2f} % / {z60[col]:.2f} %"
        for col, lab, _, _ in SERIES if col in held.index)
    ax.text(0.02, 0.04, txt, transform=ax.transAxes, fontsize=7.5, color=st.INK2, va='bottom',
            family='monospace')
    ax.legend(loc='upper right', ncol=1)
    fig.tight_layout()
    st.save(fig, 'fig02_forward_model_ladder', caption=CAPTION)


if __name__ == '__main__':
    main()
