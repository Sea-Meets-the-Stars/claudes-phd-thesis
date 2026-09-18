"""Copy the figures the report reuses from the source repositories into ``reports/figures/``.

Four figures already exist in a form the report can use, each produced by a
script in its own repository; rebuilding them here would only fork their
provenance.  This script copies them under stable report names and writes a
caption file beside each, recording the source path and the producing script.
Run it after the source repositories are current on this machine.
"""

from __future__ import annotations

import shutil

import _style as st

REUSE = [
    ('fig10_gloria_turbid_fits',
     st.PY / 'IOPtics' / 'reports' / 'figures' / 'talk_exemplar_fits.png',
     'IOPtics/reports/scripts/talk_exemplar_fits.py',
     'On turbid coastal water every backscatter parameterization returns the same '
     'failing fit (the four model curves lie on top of each other), so a richer '
     'parameterization cannot be the fix and the forward model is the remaining suspect.'),
    ('fig11_moana_heldout_skill',
     st.PY / 'EPFT-UP' / 'reports' / 'figures' / 'moana_heldout_skill.png',
     'EPFT-UP/reports/scripts/ (moana_report_figs.py)',
     'The published MOANA coefficients transfer to independent hyperspectral in-situ '
     'spectra for picoeukaryotes but not for Prochlorococcus or Synechococcus, a '
     'parameterization-transfer failure one level up from the IOPs.'),
    ('fig12_pab_chl_bias_vs_magnitude',
     st.PY / 'PAB' / 'pab' / 'matchup' / 'chl' / 'chl_reldiff_vs_magnitude.png',
     'PAB/pab/matchup/chl/ scripts (pab_chl_matchups_report.md §3)',
     'Against 9,814 BGC-Argo profiles the PACE chlorophyll retrieval is high in clear water '
     'and low in rich water, changing sign near 0.1–0.2 mg per cubic metre, so no single '
     'bias number describes the mission-scale error.'),
    ('fig13_pab_chl_raw_vs_adjusted',
     st.PY / 'PAB' / 'pab' / 'matchup' / 'chl' / 'chl_bias_raw_vs_adjusted.png',
     'PAB/pab/matchup/chl/ scripts (pab_chl_matchups_report.md §6)',
     'The in-situ reference itself is ambiguous: scoring PACE against delayed-mode-adjusted '
     'rather than raw Argo chlorophyll moves the median bias from +0.13 to +0.58, a larger '
     'effect than most of the retrieval physics.'),
]


def main():
    st.OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, src, producer, caption in REUSE:
        if not src.is_file():
            print(f'MISSING {src}')
            continue
        dst = st.OUT_DIR / f'{name}.png'
        shutil.copy2(src, dst)
        (st.OUT_DIR / f'{name}.caption.txt').write_text(
            caption + f'\n\n[reused from {src.relative_to(st.PY)}; produced by {producer}]\n')
        print(f'copied {src.name} -> {dst.name}')


if __name__ == '__main__':
    main()
