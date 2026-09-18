"""Fig 3 — how much of the red-end signal an elastic-only model cannot produce.

Relative RMS error of modelled R_rs against the L23 X=4 truth (HydroLight run
*with* Raman scattering and chlorophyll fluorescence), for an elastic-only
forward model, the analytic Raman + fluorescence terms, and those terms with
the trained correction heads.  Data:
``retrieve-or-bust/design/validation/rrms_per_wavelength_inelastic.csv`` and
``metrics_inelastic.csv`` (report v1.0, 2026-08-27).
"""

from __future__ import annotations

import pandas as pd
import matplotlib.pyplot as plt

import _style as st

CAPTION = ('Light that water itself re-emits (Raman scattering, chlorophyll fluorescence) '
           'is 15–20 % of the red-end signal; an elastic-only forward model cannot fit it, '
           'and a retrieval run on one will put that light somewhere in the constituents.')

SERIES = [('elastic-only', 'elastic-only forward model', st.INK3),
          ('analytic inelastic', '+ analytic Raman and fluorescence', st.CATEGORICAL[1]),
          ('corrected inelastic', '+ trained correction heads (this work)', st.CATEGORICAL[0])]


def main():
    st.use_style()
    d = st.PY / 'retrieve-or-bust' / 'design' / 'validation'
    per = pd.read_csv(d / 'rrms_per_wavelength_inelastic.csv')
    met = pd.read_csv(d / 'metrics_inelastic.csv')
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    for col, label, color in SERIES:
        ax.plot(per['wavelength_nm'], per[col], color=color, label=label,
                lw=2.2 if 'corrected' in col else 1.6)
    ax.axvspan(400, 700, color=st.GRID, alpha=0.5, lw=0, zorder=0)
    ax.text(0.45, 0.60, 'validated window 400–700 nm', transform=ax.transAxes, ha='center',
            fontsize=7.5, color=st.INK2)
    ax.set_yscale('log')
    ax.set_xlabel('wavelength [nm]')
    ax.set_ylabel('relative RMS error of modelled $R_{rs}$\nvs HydroLight with inelastic light [%]')
    ax.set_title('What an elastic-only model misses, and what the inelastic terms recover',
                 loc='left', fontsize=9.5)
    ax.legend(loc='upper right')
    # summary numbers, held-out, 400–700 nm, per solar zenith
    tot = met[(met['section'] == 'total_rrms') & met['metric'].str.contains('400-700')]
    lines = ['held-out rRMS, 400–700 nm, sun at 0° / 30° / 60°:']
    for key, label in (('elastic-only', 'elastic-only'), ('analytic inelastic', 'analytic terms'),
                       ('corrected inelastic', 'with correction heads')):
        rows = tot[tot['metric'].str.startswith(key)].sort_values('zenith')
        if len(rows):
            lines.append(f'{label:<22s} ' + ' / '.join(f'{v:.2f} %' for v in rows['value'].astype(float)))
    ax.text(0.02, 0.04, '\n'.join(lines), transform=ax.transAxes, fontsize=7,
            family='monospace', color=st.INK2, va='bottom')
    fig.tight_layout()
    st.save(fig, 'fig03_inelastic_terms', caption=CAPTION)


if __name__ == '__main__':
    main()
