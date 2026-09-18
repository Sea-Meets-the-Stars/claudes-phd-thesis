"""Shared style for the qualifying-exam figures.

Every figure script under ``claudes_phd_thesis/scripts/figures/`` imports this
module: one palette, one set of spelled-out labels, one ``save`` that writes
PNG and PDF into ``reports/figures/``.  The conventions follow the data-viz
method (form first, colour by job, thin marks, direct labels, one axis):

* **Rungs of the RT ladder are ordered**, so they take an *ordinal* single-hue
  ramp (blue, light to dark: elastic to full inelastic), not five unrelated hues.
* **Algorithms are categorical** and take the validated categorical slots in
  fixed order: expb_pow blue, giop orange, gsm aqua.  The order is never cycled.
* **Truth is ink**: black or dark grey lines, never a series colour.
* Text is always in ink colours; a coloured mark beside it carries identity.

The palette validator (`scripts/validate_palette.js`) needs node, which this
workstation lacks; the values below are the reference palette's documented,
already-validated slots and ordinal steps (references/palette.md), used
unchanged, so no unvalidated colour is introduced.
"""

from __future__ import annotations

import os
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402

HERE = Path(__file__).resolve()
THESIS = HERE.parents[3]
OUT_DIR = THESIS / 'reports' / 'figures'
OS_COLOR = Path(os.environ.get('OS_COLOR', '/home/xavier/Oceanography/data/Color'))
RUNS = OS_COLOR / 'IOPtics' / 'runs'
PY = Path.home() / 'Oceanography' / 'python'

# ---- colour ---------------------------------------------------------------- #
INK = '#0b0b0b'
INK2 = '#52514e'
INK3 = '#8a8984'
GRID = '#e6e5e1'
SURFACE = '#fcfcfb'

#: Categorical slots (validated order): blue, orange, aqua, yellow, magenta.
CATEGORICAL = ['#2a78d6', '#eb6834', '#1baf7a', '#eda100', '#e87ba4']
ALGO_COLOR = {'expb_pow': CATEGORICAL[0], 'giop': CATEGORICAL[1], 'gsm': CATEGORICAL[2]}
ALGO_LABEL = {'expb_pow': 'BING (exp. CDOM + Bricaud + power-law bb)',
              'giop': 'GIOP', 'gsm': 'GSM'}

#: Ordinal blue ramp for the five RT rungs (steps 250, 350, 450, 550, 650).
RUNGS = ['expb_pow_ztt_el', 'expb_pow_hyb_el', 'expb_pow_hyb_ram',
         'expb_pow_hyb_ramfl', 'expb_pow_hyb_ramflcdom']
RUNG_COLOR = dict(zip(RUNGS, ['#86b6ef', '#5598e7', '#2a78d6', '#1c5cab', '#104281']))
RUNG_LABEL = {
    'expb_pow_ztt_el': 'elastic, analytic (ZTT)',
    'expb_pow_hyb_el': 'elastic, hybrid (ZTT + emulator)',
    'expb_pow_hyb_ram': '+ Raman scattering',
    'expb_pow_hyb_ramfl': '+ chlorophyll fluorescence',
    'expb_pow_hyb_ramflcdom': '+ CDOM fluorescence (full inelastic)',
}
RUNG_SHORT = {
    'expb_pow_ztt_el': 'elastic\n(analytic)', 'expb_pow_hyb_el': 'elastic\n(hybrid)',
    'expb_pow_hyb_ram': '+Raman', 'expb_pow_hyb_ramfl': '+Chl fluor.',
    'expb_pow_hyb_ramflcdom': '+CDOM fluor.\n(full)',
}
#: The two ends of the ladder the ΔBIC contest is read through.
ELASTIC, FULL = 'expb_pow_hyb_el', 'expb_pow_hyb_ramflcdom'

#: Diverging pair for signed bias (blue negative, red positive, grey midpoint).
DIVERGING = {'neg': '#2a78d6', 'pos': '#e34948', 'mid': '#c8c7c2'}

# ---- labels (spelled out for a reader who has never seen an ocean spectrum) - #
COMPONENT_NAME = {
    'a': 'total absorption a',
    'a_ph': 'phytoplankton absorption a_ph',
    'a_dg': 'CDOM + detrital absorption a_dg',
    'bb': 'total backscattering b_b',
    'bb_p': 'particulate backscattering b_bp',
}
COMPONENT_SHORT = {'a': 'total\nabsorption', 'a_ph': 'phytoplankton\nabsorption',
                   'a_dg': 'CDOM + detrital\nabsorption', 'bb': 'total\nbackscattering',
                   'bb_p': 'particulate\nbackscattering'}
UNIT = 'm$^{-1}$'


def component_label(comp, wave=None, unit=True):
    s = COMPONENT_NAME.get(comp, comp)
    if wave is not None:
        s += f' at {wave:g} nm'
    if unit:
        s += f' [{UNIT}]'
    return s


# ---- matplotlib defaults ---------------------------------------------------- #
def use_style():
    plt.rcParams.update({
        'figure.facecolor': SURFACE, 'axes.facecolor': SURFACE,
        'savefig.facecolor': SURFACE,
        'font.size': 9, 'axes.titlesize': 10, 'axes.labelsize': 9,
        'xtick.labelsize': 8, 'ytick.labelsize': 8, 'legend.fontsize': 8,
        'axes.edgecolor': INK3, 'axes.labelcolor': INK, 'xtick.color': INK2,
        'ytick.color': INK2, 'text.color': INK,
        'axes.spines.top': False, 'axes.spines.right': False,
        'axes.grid': True, 'grid.color': GRID, 'grid.linewidth': 0.6,
        'axes.axisbelow': True, 'lines.linewidth': 1.6, 'lines.markersize': 5,
        'legend.frameon': False, 'figure.dpi': 110, 'savefig.dpi': 200,
        'pdf.fonttype': 42,
    })


def save(fig, name, *, caption=None):
    """Write ``reports/figures/<name>.png`` and ``.pdf``; optionally a caption file."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for ext in ('png', 'pdf'):
        fig.savefig(OUT_DIR / f'{name}.{ext}', bbox_inches='tight')
    if caption:
        (OUT_DIR / f'{name}.caption.txt').write_text(caption.strip() + '\n')
    plt.close(fig)
    print(f'wrote {OUT_DIR / name}.png')
    return OUT_DIR / f'{name}.png'


def note(ax, text, loc='upper left'):
    """Small ink annotation in an axes corner."""
    x, ha = (0.02, 'left') if 'left' in loc else (0.98, 'right')
    y, va = (0.97, 'top') if 'upper' in loc else (0.03, 'bottom')
    ax.text(x, y, text, transform=ax.transAxes, ha=ha, va=va, fontsize=8, color=INK2)
