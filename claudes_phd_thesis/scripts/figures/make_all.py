"""Regenerate every qualifying-exam figure into ``reports/figures/``.

Run with ``$OS_COLOR`` set, in ``ocean14``::

    conda run -n ocean14 python claudes_phd_thesis/scripts/figures/make_all.py

Each ``figNN_*.py`` is independent and can be run alone; this just runs them
in order and then copies the reused figures.
"""

from __future__ import annotations

import importlib
import sys
import traceback
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

SCRIPTS = ['fig01_inverse_problem', 'fig02_forward_model_ladder', 'fig03_inelastic_terms',
           'fig04_degeneracy_example', 'fig05_rt_ladder_l23', 'fig06_rt_ladder_vs_wavelength',
           'fig07_pace_fractional_change', 'fig08_dbic_three_arms',
           'fig09_benchmark_l23_pangaea', 'fig14_timeline', 'reuse_existing']


def main():
    failed = []
    for name in SCRIPTS:
        print(f'--- {name}')
        try:
            importlib.import_module(name).main()
        except Exception:
            traceback.print_exc()
            failed.append(name)
    if failed:
        print('FAILED:', ', '.join(failed))
        sys.exit(1)
    print('all figures written')


if __name__ == '__main__':
    main()
