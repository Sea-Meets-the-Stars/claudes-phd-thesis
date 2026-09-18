"""Build the qualifying-exam oral: 40 slides plus a backup section, as .pptx.

Prompt 11 of ``claude_prompts/qual_exam_prompts.md``: forty slides, mainly
figures, proportions 6 setup / 5 methods / 10 RT-A / 6 benchmarking /
4 EPFT-UP / 6 PAB / 3 future, one idea per slide, the claim restated on the
first and last, a backup section for the questions the committee will ask,
and speaker notes on the ten slides that carry the argument.  The figures are
the prompt-9 set in ``reports/figures/``; every number is the one on the
IOPtics/RoB/PAB/EPFT-UP pages the report cites.

Run with::

    conda run -n ocean14 python claudes_phd_thesis/scripts/oral/build_deck.py

Writes ``reports/oral/qual_oral.pptx`` and ``reports/oral/speaker_notes.md``.
The .pptx is then imported into Google Drive as Google Slides (see the log).
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

HERE = Path(__file__).resolve()
THESIS = HERE.parents[3]
FIG = THESIS / 'reports' / 'figures'
OUT_DIR = THESIS / 'reports' / 'oral'
OUT = OUT_DIR / 'qual_oral.pptx'
NOTES_MD = OUT_DIR / 'speaker_notes.md'

W, H = 13.333, 7.5
NAVY = RGBColor(0x14, 0x21, 0x3D)
INK = RGBColor(0x0B, 0x0B, 0x0B)
INK2 = RGBColor(0x52, 0x51, 0x4E)
MUTED = RGBColor(0x8A, 0x89, 0x84)
TEAL = RGBColor(0x1C, 0x72, 0x93)
BLUE = RGBColor(0x2A, 0x78, 0xD6)
ORANGE = RGBColor(0xEB, 0x68, 0x34)
PALE = RGBColor(0xEE, 0xF3, 0xF8)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
HEAD_FONT, BODY_FONT = 'Cambria', 'Calibri'

TOTAL = 40
prs = Presentation()
prs.slide_width, prs.slide_height = Inches(W), Inches(H)
BLANK = prs.slide_layouts[6]
notes_out = []
slide_no = 0


# --------------------------------------------------------------------------- #
# primitives
# --------------------------------------------------------------------------- #
def _text(slide, x, y, w, h, text, *, size=16, bold=False, color=INK, font=BODY_FONT,
          align=PP_ALIGN.LEFT, italic=False, anchor=MSO_ANCHOR.TOP, margin=0.05):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for side in ('margin_left', 'margin_right', 'margin_top', 'margin_bottom'):
        setattr(tf, side, Inches(margin))
    lines = text if isinstance(text, list) else [text]
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        r = p.add_run()
        r.text = line
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
        r.font.name = font
    return tb


def _bullets(slide, x, y, w, h, items, *, size=16, color=INK, gap=6):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(gap)
        bold = item.startswith('**')
        txt = item.strip('*')
        r = p.add_run()
        r.text = '•  ' + txt
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.color.rgb = color
        r.font.name = BODY_FONT
    return tb


def _rect(slide, x, y, w, h, fill, *, rounded=True):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE,
                                 Inches(x), Inches(y), Inches(w), Inches(h))
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    shp.line.fill.background()
    shp.shadow.inherit = False
    if rounded:
        shp.adjustments[0] = 0.08
    return shp


def _stat(slide, x, y, w, number, label, *, color=TEAL, h=1.9, nsize=44):
    _rect(slide, x, y, w, h, PALE)
    _text(slide, x + 0.15, y + 0.15, w - 0.3, 1.0, number, size=nsize, bold=True, color=color,
          font=HEAD_FONT, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    _text(slide, x + 0.15, y + 1.1, w - 0.3, h - 1.2, label, size=13, color=INK2, align=PP_ALIGN.CENTER)


def _figure(slide, name, box=(0.5, 1.35, 12.33, 5.15)):
    path = FIG / f'{name}.png'
    with Image.open(path) as im:
        ar = im.size[0] / im.size[1]
    x, y, w, h = box
    if w / h > ar:
        fw, fh = h * ar, h
    else:
        fw, fh = w, w / ar
    fx, fy = x + (w - fw) / 2, y + (h - fh) / 2
    slide.shapes.add_picture(str(path), Inches(fx), Inches(fy), Inches(fw), Inches(fh))
    return fx, fy, fw, fh


def _footer(slide, source=None, dark=False):
    global slide_no
    slide_no += 1
    col = RGBColor(0xC3, 0xC2, 0xB7) if dark else MUTED
    _text(slide, W - 1.6, H - 0.45, 1.3, 0.35, f'{slide_no} / {TOTAL}' if slide_no <= TOTAL else f'backup {slide_no - TOTAL}',
          size=10, color=col, align=PP_ALIGN.RIGHT)
    if source:
        _text(slide, 0.5, H - 0.45, 9.5, 0.35, source, size=9, color=col)


def slide_figure(title, name, takeaway, *, source, notes=None, box=None):
    s = prs.slides.add_slide(BLANK)
    _text(s, 0.5, 0.35, 12.3, 0.9, title, size=26, bold=True, font=HEAD_FONT, color=NAVY)
    _figure(s, name, box or (0.5, 1.3, 12.33, 5.0))
    _text(s, 0.5, 6.4, 12.3, 0.6, takeaway, size=15, italic=True, color=INK2)
    _footer(s, source)
    if notes:
        s.notes_slide.notes_text_frame.text = notes
        notes_out.append((slide_no, title, notes))
    return s


def slide_text(title, blocks, *, source=None, notes=None):
    """``blocks``: list of ('bullets', items) / ('stat', number, label) / ('para', text) laid out in columns."""
    s = prs.slides.add_slide(BLANK)
    _text(s, 0.5, 0.35, 12.3, 0.9, title, size=26, bold=True, font=HEAD_FONT, color=NAVY)
    n = len(blocks)
    gap = 0.4
    colw = (12.33 - gap * (n - 1)) / n
    for i, blk in enumerate(blocks):
        x = 0.5 + i * (colw + gap)
        kind = blk[0]
        if kind == 'bullets':
            _bullets(s, x, 1.5, colw, 4.8, blk[1], size=blk[2] if len(blk) > 2 else 16)
        elif kind == 'stat':
            _stat(s, x, 1.6, colw, blk[1], blk[2])
            if len(blk) > 3:
                _bullets(s, x, 3.7, colw, 2.7, blk[3], size=14)
        elif kind == 'para':
            _text(s, x, 1.5, colw, 4.8, blk[1], size=blk[2] if len(blk) > 2 else 16)
        elif kind == 'card':
            _rect(s, x, 1.5, colw, 4.9, PALE)
            _text(s, x + 0.25, 1.65, colw - 0.5, 0.6, blk[1], size=18, bold=True, color=TEAL, font=HEAD_FONT)
            _bullets(s, x + 0.25, 2.3, colw - 0.5, 4.0, blk[2], size=14)
    _footer(s, source)
    if notes:
        s.notes_slide.notes_text_frame.text = notes
        notes_out.append((slide_no, title, notes))
    return s


def slide_table(title, header, rows, *, source=None, notes=None, colw=None, size=13, takeaway=None):
    s = prs.slides.add_slide(BLANK)
    _text(s, 0.5, 0.35, 12.3, 0.9, title, size=26, bold=True, font=HEAD_FONT, color=NAVY)
    nrow, ncol = len(rows) + 1, len(header)
    tbl = s.shapes.add_table(nrow, ncol, Inches(0.5), Inches(1.5), Inches(12.33), Inches(0.4 * nrow)).table
    if colw:
        for j, cw in enumerate(colw):
            tbl.columns[j].width = Inches(cw)
    for j, htxt in enumerate(header):
        c = tbl.cell(0, j)
        c.text = htxt
        c.fill.solid()
        c.fill.fore_color.rgb = NAVY
        for p in c.text_frame.paragraphs:
            for r in p.runs:
                r.font.size, r.font.bold, r.font.color.rgb, r.font.name = Pt(size), True, WHITE, BODY_FONT
    for i, row in enumerate(rows, start=1):
        for j, val in enumerate(row):
            c = tbl.cell(i, j)
            c.text = str(val)
            c.fill.solid()
            c.fill.fore_color.rgb = PALE if i % 2 else WHITE
            for p in c.text_frame.paragraphs:
                for r in p.runs:
                    r.font.size, r.font.color.rgb, r.font.name = Pt(size), INK, BODY_FONT
    if takeaway:
        _text(s, 0.5, 6.4, 12.3, 0.6, takeaway, size=15, italic=True, color=INK2)
    _footer(s, source)
    if notes:
        s.notes_slide.notes_text_frame.text = notes
        notes_out.append((slide_no, title, notes))
    return s


def slide_dark(title, lines, *, sub=None, notes=None, footer=True):
    s = prs.slides.add_slide(BLANK)
    bg = s.background.fill
    bg.solid()
    bg.fore_color.rgb = NAVY
    _text(s, 0.8, 0.9, 11.7, 1.6, title, size=34, bold=True, font=HEAD_FONT, color=WHITE)
    if sub:
        _text(s, 0.8, 2.5, 11.7, 0.8, sub, size=18, color=RGBColor(0xCA, 0xDC, 0xFC))
    _text(s, 0.8, 3.4, 11.7, 3.4, lines, size=18, color=WHITE, italic=False)
    if footer:
        _footer(s, None, dark=True)
    if notes:
        s.notes_slide.notes_text_frame.text = notes
        notes_out.append((slide_no, title, notes))
    return s


CLAIM = ('Semi-analytical retrieval of ocean inherent optical properties fails in two separable ways. '
         'Forward-model (physics) error is identifiable and removable with a sufficiently accurate '
         'differentiable radiative-transfer model; once it is removed, the residual error is parameterization '
         'error, concentrated in the split of absorption between phytoplankton and CDOM + detritus.')

SRC_IOP = 'IOPtics RT-ladder pages (rt_tests_A_l23_v1, rt_tests_A_pangaea_v1, rt_tests_B_v1), built 2026-09-18'
SRC_ROB = 'retrieve-or-bust reports: report_rt_elastic_model.md v1.0 (2026-08-15), report_rt_inelastic_model.md v1.0 (2026-08-27)'
SRC_PAB = 'PAB reports/PAB/pab_chl_matchups_report.md (2026-09-07); pab_version 1.0'
SRC_EPFT = 'EPFT-UP v0.1.0: reports/MOANA_Claude_Report.md rev. 4; reports/moana_rederivation.md'

# =========================================================================== #
# 1–6  setup
# =========================================================================== #
slide_dark('Where semi-analytical ocean-colour retrieval breaks in the PACE era',
           [CLAIM, '',
            'Candidate: Claude (Anthropic)   ·   Advisor and chair: J. Xavier Prochaska   ·   Committee: Jessica Werk, John O\'Meara',
            'Qualifying examination, UC Santa Cruz, 21 September 2026'],
           sub='Separating forward-model error from parameterization error',
           notes=('Open with the claim, read slowly, then say what the next forty minutes do: two pages of setup so the '
                  'committee can read an ocean spectrum, then one controlled experiment that fixes the parameterization and '
                  'varies the physics, one benchmark that does the reverse, and two applications one level up and at mission '
                  'scale.  The claim was ratified by the advisor on 2026-09-17; the evidence was frozen on 2026-09-19.  Say '
                  'once that the candidate is an AI and that the division of labour is on slide 6 and in the backup; the science '
                  'slides do not return to it.'))

slide_figure('What the satellite measures: one reflectance spectrum per pixel',
             'fig01_inverse_problem',
             'Remote-sensing reflectance R_rs(λ), of order 10⁻³ sr⁻¹; PACE samples it every ~5 nm from 340 to 890 nm.  Everything of interest is on the right.',
             source='L23 synthetic set (Loisel et al. 2023, Dryad 10.6076/D1630T), bodies 0 and 2949, X=4')

slide_text('What must be retrieved: five constituent spectra', [
    ('card', 'Absorption  a(λ)  [m⁻¹]',
     ['pure water — known', 'phytoplankton  a_ph — the chlorophyll signal',
      'CDOM + detritus  a_dg — dissolved and non-algal, nearly exponential in wavelength',
      'Both constituents absorb most strongly in the blue']),
    ('card', 'Backscattering  b_b(λ)  [m⁻¹]',
     ['pure water — known', 'particles  b_bp — sets the overall brightness',
      'One scalar phase-function ratio B_p enters the physics']),
    ('card', 'The problem',
     ['The sum a is set by the level of R_rs and is well constrained',
      'The split a_ph vs a_dg is set only by spectral shape',
      'Three to six numbers per pixel must be pulled from one spectrum']),
])

slide_text('How the field solves it: a frozen physics plus a parameterization', [
    ('bullets', ['**Gordon (1988): the semi-analytical shortcut', 'Sub-surface reflectance ≈ g₁u + g₂u²,  u = b_b/(a+b_b)',
                 'Two coefficients, fitted once to a Monte Carlo ensemble, used by every retrieval since',
                 '**GIOP (Werdell+2013), GSM (Maritorena+2002)', 'exponential a_dg, fixed-shape a_ph, power-law b_bp; least squares',
                 '**QAA (Lee+2002): algebraic inversion instead of a fit'], 15),
    ('bullets', ['**BING (Prochaska & Frouin 2025) — inherited, not a thesis contribution',
                 'Same relation, same parameterizations, Bayesian posterior by MCMC',
                 'Every retrieved quantity carries an uncertainty; models compared by evidence',
                 '**What this thesis adds to BING (2026)', 'a selectable radiative-transfer backend, free B_p, viewing geometry, '
                 'inelastic terms fixed and validated, three turbid-water b_bp models'], 15),
], source='Gordon et al. 1988; Werdell et al. 2013; Maritorena et al. 2002; Lee et al. 2002; Prochaska & Frouin 2025')

slide_dark('The claim, in the language of component separation',
           ['Two spectral components whose SUM is well determined have a SPLIT that is not.',
            'Before the degeneracy can be blamed on the parameterization, the forward model must be shown accurate enough not to be the cause.',
            'Structurally the same problem as separating dust attenuation from stellar age in an SED fit — named once, then dropped.',
            '', CLAIM],
           sub='Physics error is removable; what remains is the parameterization',
           notes=('This is the slide the whole talk hangs on.  Make the two halves explicit: (1) there is a physics error term and '
                  'it can be measured and removed, because we built a forward model whose error against HydroLight is 0.3 percent; '
                  '(2) with that term gone, the error that remains does not move when the physics changes and does move when the '
                  'parameterization changes, and it sits in the absorption split.  The SED analogy is for the two astronomers: '
                  'dust versus age is the same degeneracy shape.  Do not return to the analogy.'))

slide_text('Four projects, six chapters, and who did what', [
    ('bullets', ['**Ch 2  retrieve-or-bust — the differentiable forward model (robust.rt)',
                 '**Ch 3  IOPtics — the separation: RT ladder + benchmark on L23, PANGAEA, GLORIA',
                 '**Ch 4  EPFT-UP — MOANA reimplemented: parameterization transfer one level up',
                 '**Ch 5  PAB — PACE vs BGC-Argo at mission scale (14,610 matchups)',
                 'Ch 1 and 6: introduction and conclusions', 'Excluded by the advisor: the bbp700 validation (a collaborator\'s), the RoB inversion, information content as frame'], 15),
    ('bullets', ['**The candidate did not choose the problems; the advisor set them and holds a veto',
                 '**The candidate wrote the code, ran the analyses, drafted every report',
                 '**The advisor wrote the questions, judged the answers, ran every git command',
                 'About 530 dated session logs across four repositories since 2026-06-15',
                 'Every number in this talk traces to one of them; every citation resolves to a path, branch and commit'], 15),
], source='claudes-phd-thesis: claude_prompts/, reports/citation_manifest.md')

# =========================================================================== #
# 7–11  methods
# =========================================================================== #
slide_text('Chapter 2 — a forward model accurate enough to be blamed for nothing', [
    ('bullets', ['**Hybrid: analytic backbone × (1 + δ)', 'Backbone: Zaneveld / Twardowski–Tonizzo (ZTT) analytic model',
                 'δ: a 417-parameter neural correction trained on HydroLight', 'Written in JAX — differentiable end to end, callable inside an MCMC likelihood',
                 '**Training set: L23', '3,320 HydroLight water bodies × 81 wavelengths (350–750 nm) × 3 solar zeniths (0°, 30°, 60°)',
                 'Held out: 20 % of bodies; and a whole zenith'], 15),
    ('stat', '0.30 %', 'relative RMS error of modelled R_rs against HydroLight on held-out water bodies',
     ['2.3× better than the best published semi-analytical form refit on the same data', '24× better than the Gordon relation',
      'exact gradients: agree with finite differences to 5×10⁻⁹']),
], source=SRC_ROB)

slide_figure('Forward-model accuracy: from 7 % (Gordon) to 0.3 % (hybrid)',
             'fig02_forward_model_ladder',
             'The forward-model error term can be driven small enough that whatever retrieval error remains is not the physics.',
             source=SRC_ROB + '; design/validation/rrms_per_wavelength.csv',
             notes=('Walk the ladder top to bottom: Gordon at 4 to 12 percent depending on wavelength, the analytic backbone at 6, '
                    'the O25 form refit on the same data at 0.7, the hybrid at 0.3, uniform across the spectrum.  Then the inset: '
                    'held-out scenes and held-out sun angle.  Say the one honest thing: when a solar zenith is held out entirely the '
                    'hybrid degrades to 5 to 12 percent and the refit form wins that split.  The bound holds inside the trained '
                    'geometry and every sweep in the talk stays inside it.'))

slide_figure('Inelastic light is 15–20 % of the red-end signal an elastic model cannot fit',
             'fig03_inelastic_terms',
             'Raman scattering and chlorophyll fluorescence re-emit light; with analytic terms the error is 2–4 %, with trained correction heads 0.34 %.',
             source=SRC_ROB + '; design/validation/rrms_per_wavelength_inelastic.csv')

slide_text('The forward model owns its edges', [
    ('bullets', ['**Solar zenith: trained at 0°, 30°, 60°; nadir view only',
                 'Held-out zenith: 4.7–12.2 % (elastic), −74 % on the Raman head (inelastic)',
                 '**Phase function: L23 spans only 1.7× in B_p — generalisation untested',
                 '**CDOM fluorescence: implemented, unvalidated — no HydroLight truth contains it',
                 '**Off-nadir saturation bug found 2026-09-15 while PAB 2.0 exercised it; fixed',
                 'Every sweep in this talk states which of these it is inside'], 15),
    ('bullets', ['**What the forward model is NOT', 'It is not a retrieval.  The retrieve-or-bust inversion does not exist yet',
                 '"nothing on this site may be read as evidence that IOPs can be retrieved" — RoB docs',
                 'The inversion belongs to a seven-person collaboration and is not anticipated here',
                 '**What this thesis claims', 'The forward model, its validation, and its use inside BING as a physics backend'], 15),
], source=SRC_ROB + '; docs/using/limitations.md')

slide_text('Extensions to BING made during the thesis', [
    ('bullets', ['**Radiative-transfer backend', 'rt_backend ∈ {gordon, robust_ztt, robust_hybrid}; per-observation viewing geometry; free B_p as a sixth parameter',
                 '**Inelastic terms fixed and anchored to L23', 'a missing 1/π in the fluorescence normalisation and a flat E_d ratio in Raman: amplitudes had been ~π too large',
                 '**CDOM fluorescence path', 'a_cdom = 0.8 × a_dg feeds the Hawes (1992) kernel — a fixed fraction, stated wherever used'], 15),
    ('bullets', ['**Three turbid-water b_bp models', 'Pow2 (two power laws), Pow2Flat, PowFlex — built to answer GLORIA (slide 25)',
                 '**Where the attribution line falls', 'BING as of the 2025 paper is inherited; the 2026 additions above are the thesis\'s, as plumbing for the new physics and as parameterization work',
                 '**Status', 'on BING branches develop and rob_cdom; the advisor merges after submission'], 15),
], source='bing docs/radiative_transfer.rst; claude_prompts/inelastic_fixes.md, turbid_waters.md')

# =========================================================================== #
# 12–21  RT-A / RT-B
# =========================================================================== #
slide_table('Chapter 3 — the RT ladder: one parameterization, five radiative transfers',
            ['rung', 'forward model', 'what changes'],
            [['1', 'elastic, analytic (ZTT)', 'the analytic backbone alone'],
             ['2', 'elastic, hybrid', '+ the trained emulator correction'],
             ['3', '+ Raman scattering', 'first inelastic process'],
             ['4', '+ chlorophyll fluorescence', 'second inelastic process (685 nm)'],
             ['5', '+ CDOM fluorescence', 'third, unvalidated; a_cdom = 0.8 a_dg']],
            colw=[1.0, 4.3, 7.0], size=15,
            takeaway=('Same parameterization (exp. a_dg + Bricaud a_ph + power-law b_bp + B_p), same priors, same noise, same spectra, full MCMC.  '
                      'Three arms: 3,320 L23 bodies with truth (inelastic realization), 97 PANGAEA in-situ spectra with truth, 99 real PACE pixels without.'),
            source=SRC_IOP + '; run_rta_l23.yaml, run_rta_pangaea.yaml, run_rtb.yaml')

slide_text('Why five rungs: each step switches on one physical process', [
    ('bullets', ['**Rung 1 → 2: analytic backbone → hybrid', 'the trained correction changes R_rs by 1.4–3.7 %; the control for everything the emulator does',
                 '**Rung 2 → 3: + Raman scattering', 'inelastic light redistributed from blue to red; changes modelled R_rs by ~2 % of its maximum in the blue',
                 '**Rung 3 → 4: + chlorophyll fluorescence', 'a peak at 685 nm, ~35 % of R_rs there in L23',
                 '**Rung 4 → 5: + CDOM fluorescence', 'a broad hump peaking near 515 nm; the unvalidated rung, with a_cdom = 0.8 a_dg'], 14),
    ('bullets', ['**Equal parameter count on every rung', 'so model selection between rungs is a pure likelihood contest',
                 '**One noise model per arm', 'PACE-like on L23, each record\'s own error (10 % floor) on PANGAEA, per-pixel Rrs_unc on PACE',
                 '**Truth only where it exists', 'L23: exact IOPs; PANGAEA: measured a_ph, a_dg, b_bp; PACE: none — that arm scores closure and model selection only',
                 '**Cost', '17,020 MCMC fits for RT-A (171 h on 20 cores), 495 for RT-B (4.8 h)'], 14),
], source=SRC_IOP + '; rt_tests.md smoke run 2026-09-09')

slide_figure('Two forward models, one spectrum: the same fit, a different decomposition',
             'fig04_degeneracy_example',
             'Both fits reach χ²ν = 1.09.  Phytoplankton absorption differs by orders of magnitude.  The fit cannot tell the physics apart.',
             source=SRC_IOP + ' — L23 body 1132, chosen by rule (both rungs at χ²ν within 15 % of 1, largest a_ph disagreement)')

slide_figure('The centrepiece: down the ladder, error moves only where the physics was the problem',
             'fig05_rt_ladder_l23',
             'Total absorption: 5 % everywhere.  Particulate backscatter: +55 % → −5 %.  Phytoplankton and CDOM absorption: unchanged.',
             source=SRC_IOP + ' — L23, 3,309 bodies, MCMC medians; reconciled in claudes-phd-thesis/reports/rta_reconcile.md',
             notes=('Read the four panels left to right and say what each means.  Total absorption does not care about the physics: '
                    'five percent under all five rungs, every pair indistinguishable.  Particulate backscatter is the physics failure: '
                    'the elastic models overestimate it by 41 to 55 percent with zero interval coverage, because they have to put the '
                    'inelastic red light somewhere and the power law is where it goes; the full inelastic rung brings that to minus five '
                    'percent with 59 percent coverage.  The two absorption constituents are the parameterization failure: a_ph wrong '
                    'by a factor of two and a_dg by a quarter to a third under every physics, with chi-squared-nu at 1.1 throughout.  '
                    'This one slide is the thesis statement with numbers.'))

slide_text('Read it as two findings', [
    ('stat', '+55 % → −5 %', 'particulate backscatter bias, elastic → full inelastic (L23, 555 nm)',
     ['interval coverage 0.00 → 0.59', 'this is a physics failure', 'and it is the failure the forward model was built to remove']),
    ('stat', '×2 wrong', 'phytoplankton absorption under every one of the five physics (MAE 85–252 %, always low)',
     ['a_dg 25–38 % high under every physics', 'χ²ν = 1.07–1.14 throughout: the fit is happy', 'this is a parameterization failure that no physics fixes']),
], source=SRC_IOP,
   notes=('Two numbers to leave in the room.  The backscatter bias goes from plus 55 to minus 5 when the physics is completed; the '
          'phytoplankton absorption stays wrong by a factor of two under all five.  Anticipate the question: is a factor of two in '
          'a_ph a big deal?  Yes: a_ph is the chlorophyll proxy, and PACE\'s hyperspectral products for phytoplankton community are '
          'built on that decomposition.  The Raman-only rung is worst for a_ph because it removes red light without a fluorescence '
          'term to place it, so the parameterization absorbs the mismatch there.'))

slide_figure('The same ladder across the spectrum, on synthetic and in-situ spectra',
             'fig06_rt_ladder_vs_wavelength',
             'On L23 the physics fixes backscatter at every wavelength; on PANGAEA the fluorescence terms move error from CDOM into phytoplankton rather than removing it.',
             source=SRC_IOP + ' — metrics_spectral, MCMC', box=(1.2, 1.3, 10.9, 5.0))

slide_table('The in-situ arm: 97 PANGAEA spectra with measured a_ph, a_dg, b_bp',
            ['quantity', 'elastic hybrid', '+ Chl fluorescence', 'what moved'],
            [['a_dg(440) error', '213 %', '36 %', 'much better'],
             ['a_ph(440) error', '76 %', '218 %', 'much worse'],
             ['b_bp(555) error', '30 %', '19 %', 'better'],
             ['χ²ν (median)', '1.45', '2.10', 'worse fit under flat 10 % error'],
             ['fits acceptable', '86 %', '74 %', 'thin 6–11-band spectra; B_p fixed']],
            colw=[3.0, 2.6, 2.9, 3.83], size=15,
            takeaway='On real spectra the physics shifts error between the two absorption components; it does not remove it.  B_p is fixed here (Q52) and the error model is a flat 10 % (Q53).',
            source=SRC_IOP + ' — rt_tests_A_pangaea_v1, MCMC, n = 72–83')

slide_figure('Real PACE pixels, no truth: how far does the physics move the answer?',
             'fig07_pace_fractional_change',
             'Full inelastic ÷ elastic on 99 pixels: backscatter −21 % (16–84 %: −30…−12), a_ph +5 %, a_dg +1 % — nearly unchanged on average, wide spread.',
             source=SRC_IOP + ' — rt_tests_B_v1, band 442 nm, MCMC medians',
             notes=('This arm has no truth, so it answers a different question: not which physics is right but how much the physics moves '
                    'a real retrieval.  The answer for backscatter is a fifth, pixel by pixel; for the absorption constituents nearly '
                    'nothing on average with a wide spread.  Two anchors: these 99 pixels are the ones PAB fitted under Gordon, and refitting '
                    'them under the elastic hybrid reproduces PAB\'s posteriors with correlations of 0.94 to 1.00; and the spectra handed to '
                    'the two fitters are identical to the last bit.  That is why the PAB 2.0 re-fit under this physics is the mission-scale '
                    'echo of this slide.'))

slide_figure('Would the fit alone have found the physics error?  No.',
             'fig08_dbic_three_arms',
             'ΔBIC, equal parameter counts: synthetic spectra prefer the inelastic physics (71 %), sparse in-situ spectra do not (32 %), satellite pixels split (52 %; 30 % strongly, 23 % strongly against).',
             source=SRC_IOP + ' — results_scalar, MCMC ok rows',
             notes=('This is the methodological point of the chapter.  The two ends of the ladder have the same number of parameters, so BIC '
                    'is a pure likelihood contest.  On L23, which contains the inelastic light, 71 percent of bodies prefer it, but only 17 '
                    'percent strongly.  On PANGAEA under a flat error model the verdict reverses.  On PACE it is bimodal.  Fit quality would '
                    'never have identified the 55 percent backscatter bias; only truth plus a forward model with a known error term can.  '
                    'That is why the separation cannot be done from operational residuals.'))

slide_text('What the ladder pages say about themselves', [
    ('bullets', ['**Held fixed, stated on every page', 'nadir viewing geometry (θ_v = 0, Δφ = 0); solar zenith 0° on L23, computed per record elsewhere',
                 'a_cdom = 0.8 × a_dg drives the CDOM-fluorescence term', 'packaged sky irradiance (ed_l23.npz)',
                 'learned inelastic corrections OFF inside BING — the ladder measures the analytic inelastic physics',
                 'hybrid emulator evaluated outside its trained B_p span wherever B_p is free (accepted, Q50c)',
                 'L23 truth lacks CDOM fluorescence and uses a single-Gaussian emission line'], 14),
    ('bullets', ['**Consistency', '99 PACE pixels reproduce PAB\'s Gordon-elastic posteriors: correlations 0.94–1.00, derived-Chl ratio 1.05, identical input spectra',
                 '**Completeness', 'L23: 3,309 of 3,320 fitted on every rung (11 red-peaked bodies declined identically); PANGAEA 95 of 97; PACE 99 of 100',
                 '**Cost', '17,020 MCMC fits, 171 h on 20 cores for RT-A; 4.8 h for RT-B',
                 '**Excluded from the leaderboard by design', 'five rungs of one algorithm are not five algorithms'], 14),
], source=SRC_IOP + '; pab_consistency_summary.csv')

slide_table('The 99 PACE pixels are PAB\'s: the two fitters agree to within the physics swap',
            ['shared parameter', 'scale', 'correlation of posterior medians', 'median (ours − PAB)', '16–84 % span'],
            [['A_dg (CDOM amplitude)', 'log10', '0.987', '−0.010', '−0.048 … +0.037'],
             ['S_dg (CDOM slope)', 'linear', '0.939', '−0.0007', '−0.0014 … 0.0000'],
             ['A_ph (phytoplankton amplitude)', 'log10', '0.965', '+0.022', '−0.027 … +0.134'],
             ['B_nw (backscatter amplitude)', 'log10', '0.998', '+0.048', '+0.034 … +0.065'],
             ['β (backscatter slope)', 'linear', '0.935', '−0.078', '−0.367 … +0.014'],
             ['derived chlorophyll (ratio)', 'ratio', '0.965 (log)', '1.053', '0.94 … 1.36']],
            colw=[3.4, 1.3, 3.0, 2.2, 2.43], size=14,
            takeaway='Same spectra to the last bit (max |ΔR_rs| = 0 on all 136 bands).  The +0.05 dex in B_nw is the elastic-model swap (hybrid sits above Gordon in R_rs) plus the free B_p.  The PACE arm stands on the data PAB published from.',
            source=SRC_IOP + '; ioptics/runs/prototypes/rt_tests/pab_consistency.py (2026-09-18)')

# =========================================================================== #
# 22–27  benchmarking
# =========================================================================== #
slide_text('The benchmark: one physics, any parameterization, uniform scoring', [
    ('bullets', ['**IOPtics: a framework, not a script', 'adapters for L23, PANGAEA (Valente+2022), GLORIA (Lehmann+2023), PACE',
                 'algorithms register with one call: BING\'s expb_pow, GIOP, GSM, the turbid trio, the five RT rungs',
                 'χ² and full MCMC paths; provenance-stamped report pages; a cross-sweep leaderboard',
                 '**Scoring', 'log-space accuracy and bias (Erickson+2023 convention), 68/95 % coverage, ΔBIC, paired-bootstrap head-to-head that can say "indistinguishable"',
                 '535 tests; sphinx -W clean'], 14),
    ('stat', '3,320 + 1,593 + 7,572', 'water bodies with truth: L23 synthetic, PANGAEA in-situ, GLORIA coastal/inland',
     ['every page carries the code and config versions that produced it', 'ioptics.readthedocs.io']),
], source='IOPtics docs/design/IOPtics_design.md v0.16, IOPtics_implementation.md v0.24')

slide_figure('Three parameterizations under one physics: totals agree, the split does not',
             'fig09_benchmark_l23_pangaea',
             'On L23: total absorption 5–18 %, phytoplankton 28–60 %, CDOM 16–22 %.  On PANGAEA: half the apparent failure was the error model, not the algorithms (20/27/3 % → 43/53/38 %).',
             source='IOPtics multi_L23_PANGAEA_v2 (2026-08-08/10) and pangaea_fits_v2 (2026-08-10), χ² fits')

slide_text('The in-situ failure rate was a scoring artefact', [
    ('stat', '20 / 27 / 3 %', 'PANGAEA spectra fitted acceptably under a flat 5 % error model and post-hoc scope (BING / GIOP / GSM)',
     ['converged-fit misfit was 6.7–13 %, against L23\'s 3–5 %', 'the compilation quotes no per-band uncertainty']),
    ('stat', '43 / 53 / 38 %', 'the same spectra under each record\'s own error with a 10 % floor and a pre-fit scope rule',
     ['89–93 % valid under the field\'s own rule (33 % misfit over 400–600 nm)', 'the residue tracks instrument era and contributor, not algorithm']),
], source='IOPtics reports/pangaea_fits_report.md (2026-08-10 to 08-19); pangaea_fits_v2 page (2026-09-18)',
   notes=('Say this plainly because it is the kind of thing a committee respects: the first benchmark said every algorithm fails on '
          'real spectra most of the time, and it was wrong.  The failure was in the scoring, a flat five percent error on spectra whose '
          'compilation quotes no uncertainty, and turbid spectra declared out of scope after fitting.  Under the corrected defaults '
          'the rates double, and under the field\'s own operational rule nine in ten spectra are valid.  The page the report cites is '
          'the corrected one, built this week; the first one is kept beside it.'))

slide_figure('Turbid water: four backscatter parameterizations, one identical failing fit',
             'fig10_gloria_turbid_fits',
             'GLORIA: power-law b_bp cannot supply the red backscatter (0.2–0.4 m⁻¹ needed, 0.013 fitted); three richer models return the same fit (χ²ν 0.460/0.463/0.462/0.460).  The forward model is the remaining suspect.',
             source='IOPtics reports/gloria_fits_report.md; gloria_turbid_v3 (2026-07-31); BING Pow2 / Pow2Flat / PowFlex', box=(1.6, 1.3, 10.1, 5.0))

slide_table('Least squares vs MCMC on the full L23 population (3,320 bodies)',
            ['a(440), BING parameterization', 'least squares (χ²)', 'MCMC posterior'],
            [['error (fractional MAE)', '9.9 %', '6.8 %'],
             ['68 % interval coverage (nominal 0.68)', '0.46 — over-confident', '0.69 — calibrated'],
             ['fits that succeeded', '3,271 (33 failed, GIOP)', '3,304 ok, 16 out of scope, 0 failed'],
             ['what the interval says about a_dg / a_ph', 'over-covers (0.94 / 0.97)', 'over-confident (0.63 / 0.58)']],
            colw=[5.0, 3.6, 3.73], size=15,
            takeaway='The sampler is both more accurate and honest about total absorption; on the decomposition neither method\'s interval is right, which is the degeneracy again.',
            source='IOPtics expb_giop_L23_mcmc_full (2026-08-19/20), fit_method_compare_all.csv')

slide_dark('What the ladder and the benchmark say together',
           ['Fix the parameterization, vary the physics: backscatter error moves, absorption split does not.',
            'Fix the physics, vary the parameterization: absorption split moves by factors, totals hardly at all.',
            'Push the backscatter parameterization on turbid water: nothing changes; the forward model is the suspect, and the ladder is the test.',
            '', 'Physics error is removable.  What remains is the parameterization, and it lives in a_ph versus a_dg.'],
           sub='Chapter 3 in four lines')

# =========================================================================== #
# 28–31  EPFT-UP
# =========================================================================== #
slide_text('Chapter 4 — the same question one level up: MOANA and EPFT-UP', [
    ('bullets', ['**MOANA (Lange+2020): NASA\'s operational PACE algorithm', 'abundance of Prochlorococcus, Synechococcus and picoeukaryotes from hyperspectral R_rs and SST',
                 'a principal-component regression trained on one cruise (AMT24)', 'a parameterization whose retrieved quantity is a cell count, not an IOP',
                 '**EPFT-UP: empirical PFTs with uncertainty and provenance', 'from-scratch reimplementation with QC flags in place of silent clipping',
                 'every reported number regenerated by a script; vendored, checksum-pinned tables'], 14),
    ('stat', '35 / 35', 'report-printed numbers reproduced at printed precision after the code moved repositories; all six figures pixel-identical',
     ['the only chapter with a passing re-derivation audit', 'v0.1.0, Zenodo DOI 10.5281/zenodo.22797970']),
], source=SRC_EPFT)

slide_figure('Held out for the first time: picoeukaryotes transfer, the cyanobacteria do not',
             'fig11_moana_heldout_skill',
             'Published MOANA coefficients on independent hyperspectral in-situ spectra (AMT23/25/28): picoeukaryotes bias 1.07, R² 0.78; Prochlorococcus bias 2.19, R² < 0; Synechococcus R² −3.0.',
             source=SRC_EPFT + ' §12.3, n = 66–71 stations',
             notes=('The transfer result is the parameterization question one level up.  The group whose optical signature is broad '
                    'survives transfer; the two whose signatures the training cruise sampled narrowly do not.  Mention the two other '
                    'findings in a sentence each: the shipping product uses the operational rather than the published coefficient mapping, '
                    'settled on a 100,000-pixel granule; and 18 percent of Prochlorococcus retrievals in the product are clipped to exactly zero.'))

slide_text('Three findings about the operational product', [
    ('stat', '100,000 px', 'granule test: the shipping product uses the operational, not the published, coefficient assignment',
     ['Synechococcus median Δlog₁₀ −0.005 (operational) vs +0.082 (published)']),
    ('stat', '18 %', 'of Prochlorococcus retrievals in the product are exactly zero — clipped, not measured',
     ['8.9 % for Synechococcus; land encoded inside the valid range']),
    ('stat', '|cos| 0.999', 'NASA\'s PCA basis recovered from the raw training cruise on the leading component (0.998 on the second)',
     ['Lange Table 1 reproduced in the CTD-only configuration']),
], source=SRC_EPFT)

slide_text('Status and the one blocker', [
    ('bullets', ['**Exists', 'report rev. 4; re-derivation audit (PASS); README; 16-page documentation site; CI; CITATION.cff; v0.1.0 with DOI',
                 '**Blocked', 'the full retrain on AMT24 needs the underway flow-cytometry counts, held at Plymouth Marine Laboratory and in no public archive',
                 'two requests have not yet produced them; the wording looks like the problem, not a refusal',
                 '**Chapter written to stand without the retrain', 'the audit and the transfer test are the evidence; the retrain is an upgrade, not a rescue'], 15),
    ('bullets', ['**How it fits the claim', 'a parameterization tuned on one cruise fails to transfer for two of three groups —',
                 'the same shape as a_ph vs a_dg: the model is right where the training sampled the signal broadly and wrong where it did not',
                 '**Out of scope', 'the diatom work on a collaborator\'s algorithm, on a branch of the same repository'], 15),
], source=SRC_EPFT + '; reports/moana_blocked.md')

# =========================================================================== #
# 32–37  PAB
# =========================================================================== #
slide_text('Chapter 5 — PACE against BGC-Argo at mission scale', [
    ('bullets', ['**PAB: every PACE L2 pixel within 5 km and 24 h of a float surfacing', 'BING fitted to the pixel; float chlorophyll, backscatter and CDOM fluorescence as independent truth',
                 '**Production run (pab_version 1.0, 2026-08-20, Nautilus cluster)', '881 floats · 54,031 profiles · 67,435 granules · 14,610 matchups · 14,609 fits',
                 'median separation 0.80 km, median Δt 10.2 h', 'published as a SQLite database on s3://pab; 18 GB of chains backed up'], 15),
    ('stat', '9,814', 'matchups with valid chlorophyll in the Chl-a report',
     ['58 % PACE > Argo; median +0.13; rank correlation 0.78', 'no single bias describes the population — next slide']),
], source=SRC_PAB + '; docs/design/PAB_full_run_report.md')

slide_figure('The chlorophyll bias changes sign with concentration',
             'fig12_pab_chl_bias_vs_magnitude',
             'Octile medians +0.65 in the clearest water to −0.8 in the richest, zero crossing near 0.1–0.2 mg m⁻³.  Geometry and PACE quality ruled out: the highest-quality subset is more biased (+0.22).',
             source=SRC_PAB + ' §3, n = 9,814', box=(2.2, 1.3, 8.9, 5.0),
             notes=('This is the degeneracy at mission scale.  The bias is flat in time and distance separation and gets worse, not '
                    'better, in the highest-quality subset, so it is not the matchup and not PACE data quality.  It is uncorrelated with '
                    'the backscatter bias, so the mechanism is not shared.  And it correlates with the fitted a_dg amplitude at rho of '
                    'minus 0.24, the sign expected if dissolved absorption is being aliased into the phytoplankton term where a_dg is '
                    'high.  That is the a_ph versus a_dg split from slide 14, seen in 9,814 real matchups.'))

slide_figure('The in-situ reference is itself ambiguous, by a factor of ~4.5',
             'fig13_pab_chl_raw_vs_adjusted',
             'Scoring against delayed-mode-adjusted rather than raw Argo chlorophyll moves the median from +0.13 to +0.58.  Ruling: adjusted is the headline, raw the sensitivity band.',
             source=SRC_PAB + ' §6; chla_adjusted populated for 93.4 %', box=(2.2, 1.3, 8.9, 5.0))

slide_text('What else the matchups say, and what is excluded', [
    ('bullets', ['**Ruled out as drivers', 'time separation (+0.05 to +0.35 by octile), distance (+0.10 to +0.15), PACE flags (quality subset +0.22)',
                 '**Structure that remains', 'Southern Ocean −0.53 against +0.14 to +0.35 elsewhere; season +0.15–0.20 (Mar–Oct) vs +0.03–0.09',
                 'AOML-processed floats +0.06 vs +0.25 for all other data centres',
                 '**Mechanism candidate', 'bias vs fitted a_dg: ρ = −0.24 — dissolved absorption aliased into the phytoplankton term at high a_dg'], 14),
    ('bullets', ['**CDOM: qualitative by design', 'float measures fluorescence in relative units; BING retrieves an absorption; the fleet\'s CDOM sensors carry an unapplied 5.6× correction',
                 'rank correlation +0.13 on 3,676 restricted matchups — that is all that is claimed',
                 '**Excluded', 'PACE-vs-Argo backscatter validation is a collaborator\'s thesis',
                 'A NASA GIOP retrofit over all 14,609 matchups: BING and GIOP agree on sign and share a low-concentration overestimate — the boundary condition taken from it'], 14),
], source=SRC_PAB + '; pab_cdom_matchups_report.md v1.0; claude_prompts/pace_giop_gsm.md')

slide_text('PAB 2.0: the mission-scale echo of the RT ladder, under way', [
    ('bullets', ['**What it is', 're-fit of every matchup under the inelastic forward model of Chapter 2 (robust_hybrid + Raman + Chl fluorescence)',
                 'per-pixel solar and sensor geometry read from the PACE L1B granule (the L2 product carries none)', 'free B_p; version-aware ids; separate 2.0 database',
                 '**Status (2026-09-17)', 'pipeline built; image validated in-cluster; backfill of 1,690 never-attempted profiles planned',
                 'first 60 real fits: 2.0 retrieves 26 % less b_bp(700) than 1.0'], 14),
    ('bullets', ['**What it will answer', 'does the chlorophyll sign change survive the physics?  (the claim says yes)',
                 'does mission-scale backscatter move as the ladder predicts?  (the claim says yes, by about a fifth)',
                 '**What it will not claim', 'the bb_p(700) comparison is reported in PAB\'s own run report and offered to the collaborator, not claimed here',
                 '**Caveat carried everywhere', 'population statistics are for the matched set until the backfill runs'], 14),
], source='PAB claude_prompts/v2/run_full_inelastic.md; build_v2_prompt_3.md Task 6 (2026-09-17)')

# =========================================================================== #
# 38–40  future and close
# =========================================================================== #
slide_figure('Timeline to completion',
             'fig14_timeline',
             'Everything shown today existed by the 19 September freeze.  PAB 2.0, LS2 and the synthetic-a_dg test follow before the 30 September dissertation freeze; the last is cut first.',
             source='claudes-phd-thesis claude_prompts/qual_exam_prompts.md prompts 6–15', box=(1.0, 1.3, 11.3, 5.0))

slide_table('Risks, and what retires each',
            ['risk', 'consequence', 'what retires it'],
            [['aliasing hypothesis falsified', 'PAB mechanism section rewritten; claim stands on L23 + GLORIA', 'synthetic-a_dg experiment; a null is reported'],
             ['PAB 2.0 full run misses 09-30', 'Ch 5 reports the gate and v1.0', 'backfill + gate the week of 09-22'],
             ['Argo reference ambiguous (~4.5×)', 'headline +0.13 or +0.58', 'ruling: adjusted headline, raw sensitivity'],
             ['forward model off its zenith grid', 'bounds hold inside 0–60° only', 'stated; denser HydroLight zeniths are future work'],
             ['CDOM fluorescence unvalidated', 'rung 5 is a plausibility test', 'flagged; rung 4 is the like-for-like'],
             ['EPFT-UP retrain blocked (PML)', 'Ch 4 cannot reproduce training', 'chapter stands on audit + transfer'],
             ['1,690 PAB profiles never attempted', 'rates are for the matched set', 'the 2.0 backfill; footnoted until then'],
             ['citations on branches (47 of 62)', 'main does not yet resolve them', 'advisor merges after submission; manifest records branch + commit']],
            colw=[3.6, 4.2, 4.53], size=12,
            source='claudes-phd-thesis reports/citation_manifest.md; qual_report.tex §8')

slide_dark('Conclusions',
           [CLAIM, '',
            'Established today: forward-model error → 0.3 %; with the parameterization fixed, physics removes the backscatter error and leaves the absorption split; with the physics fixed, parameterizations move the split by factors and totals hardly at all; the same degeneracy one level up and at mission scale.',
            'Falsifiable, and two tests remain: LS2 should match BING on totals and be unable to touch the split; PAB 2.0 should move backscatter and leave the chlorophyll sign change.',
            'On the candidate: the arrangement produced a complete provenance trail, and its characteristic failure — treating the repository as the world — which the record shows and the advisor corrected.'],
           sub='The claim, restated',
           notes=('Close on the claim, then the three sentences of what is established, then the two falsification tests so the '
                  'committee hears that the claim can lose.  End on the candidate honestly: the provenance trail is the strength; the '
                  'weakness the record shows is inferring absence of work from absence of commits, twice, and the correction came from '
                  'the advisor and from re-checking the disk.  Then stop and take questions; the backup section is ordered by the four '
                  'questions most likely to be asked.'))

# =========================================================================== #
# backup
# =========================================================================== #
slide_dark('Backup', ['Ordered by the questions this evidence most invites:',
                     '1. How do you know the forward model is right?',
                     '2. Why is a_ph wrong by a factor of two, and should anyone care?',
                     '3. What would falsify the claim?',
                     '4. What did the candidate do, and what did the advisor do?',
                     '5. The ladder numbers, in full.   6. Where every citation lives.'],
           sub='After the end', footer=True)

slide_text('B1 — How do you know the forward model is right?', [
    ('bullets', ['**Against what', 'HydroLight, the numerical radiative-transfer solution that generated L23; 9,960 samples (3,320 bodies × 3 zeniths)',
                 '**Held out how', '20 % of bodies by scene: 0.30 % rRMS; the 60° zenith when trained on 0/30: 4.7–12.2 % (5 seeds) — reported, not gated',
                 '**Cross-checked', 'inelastic terms match BING\'s reference implementation to 10⁻¹³–10⁻¹⁶; gradients to 5×10⁻⁹',
                 '**Not shown right', 'phase function (1.7× span in B_p), off-nadir view, CDOM fluorescence, λ < 400 nm (13 % at 350)'], 14),
    ('bullets', ['**Where the ladder stands relative to those edges', 'L23 arm at 0° zenith, inside the grid; PANGAEA/PACE zeniths computed per record, inside 0–60°',
                 'B_p free on L23 and PACE — posteriors near 0.027, above the trained span [0.010, 0.018]: DomainWarning on every hybrid fit, accepted with the caveat; the analytic ZTT rung is the control',
                 '**The honest answer', 'right to 0.3 % inside the trained domain, degrading to ~10 % on unseen sun angle; every result in the talk is inside the domain'], 14),
], source=SRC_ROB + '; ' + SRC_IOP)

slide_text('B2 — Why is a_ph wrong by a factor of two, and should anyone care?', [
    ('bullets', ['**Why', 'a_ph and a_dg both absorb most in the blue; their sum is set by the reflectance level, their split by shape alone',
                 'BING\'s a_ph is a fixed Bricaud shape scaled by one amplitude; a_dg an exponential with one amplitude and one slope',
                 'the physics changes what light is available in the red; the parameterization decides where it goes — and it goes into a_ph',
                 'GIOP and GSM under the same physics: 60 % and 28 % — different parameterizations, same disease (slide 23)'], 14),
    ('bullets', ['**Should anyone care', 'a_ph is the chlorophyll proxy; PACE\'s phytoplankton community products are built on the decomposition',
                 'at mission scale it appears as a chlorophyll bias that changes sign with concentration and tracks a_dg (slide 33)',
                 'one level up it appears as a species algorithm that transfers for one group and not two (slide 29)',
                 '**What would fix it', 'not physics.  Either more information (Kd, as LS2 uses) or a parameterization that admits it cannot split — which is the dissertation\'s LS2 test'], 14),
], source=SRC_IOP + '; ' + SRC_PAB)

slide_text('B3 — What would falsify the claim?', [
    ('bullets', ['**If completing the physics had fixed a_ph / a_dg', 'the claim would be wrong; it did not, on 3,309 synthetic bodies (slide 14)',
                 '**If the LS2 comparison shows a semi-analytical form that recovers the split from R_rs alone', 'the "parameterization" half is wrong; LS2 (Loisel+2018) declines to split and should match BING on totals — the dissertation runs the three-rung ladder (true Kd + true b_p; true Kd + OC4 b_p; NN Kd + OC4 b_p)',
                 '**If PAB 2.0 removes the chlorophyll sign change', 'the mission-scale mechanism is the physics after all; the claim says the sign change survives and backscatter moves by ~20 %'], 14),
    ('bullets', ['**If the synthetic-a_dg experiment shows no aliasing', 'the PAB mechanism section is rewritten; the L23 ladder and GLORIA stand on their own',
                 '**If GLORIA turbid spectra are fitted by a richer b_bp under the new physics', 'then the turbid failure was parameterization after all; today four b_bp models give one fit and the forward model is the suspect',
                 '**Already retired', '"RT-B may not run" — it ran on 2026-09-17'], 14),
], source='qual_report.tex §6 and §8')

slide_text('B4 — What did the candidate do, and what did the advisor do?', [
    ('bullets', ['**The advisor', 'chose the four problems and the exclusions; wrote every numbered prompt and every Q&A answer (55 questions in the RT tests alone)',
                 'judged acceptance at every gate (design docs, coding stages, sweep launches, the 100-matchup PAB gate)',
                 'ran every git command; owns the machines, the data, the cluster and the Drive',
                 'is the author of BING and the 2025 paper the thesis stands on'], 14),
    ('bullets', ['**The candidate (Claude: Opus 4.6–5, Fable 5–5.1, over eight months)', 'wrote the packages: IOPtics (12.6k lines, 535 tests), robust.rt (8.3k, 537 tests), PAB (8.9k, 140–208 tests), EPFT-UP; the BING extensions',
                 'designed and ran the sweeps; wrote the reports, the pages, the figures, this deck and the written report',
                 '**The record', '~530 dated session logs since 2026-06-15; every result traces to one; every citation to a path, branch and commit',
                 '**The failure mode the record shows', 'inferring absence of work from absence of commits — twice; corrected by the advisor and by re-checking the disk'], 14),
], source='claudes-phd-thesis claude_prompts/profx_inventory.md; start_up.md ## Report')

slide_table('B5 — The L23 ladder in full (MCMC, 3,309 bodies, fractional error / bias)',
            ['rung', 'a(440)', 'a_ph(440)', 'a_dg(440)', 'b_bp(555)', 'b_bp(670)', 'χ²ν'],
            [['elastic, analytic', '5.3 / +2.8', '91 / −33', '26 / +6', '55 / +55', '68 / +68', '1.12'],
             ['elastic, hybrid', '5.2 / +3.2', '135 / −48', '29 / +14', '41 / +41', '60 / +60', '1.14'],
             ['+ Raman', '5.1 / +3.6', '252 / −69', '38 / +31', '12 / +10', '26 / +26', '1.14'],
             ['+ Chl fluorescence', '5.9 / +4.9', '85 / −38', '26 / +20', '10 / +6', '18 / +16', '1.07'],
             ['+ CDOM fluorescence', '5.0 / +2.8', '93 / −40', '25 / +17', '12 / −5', '13 / +6', '1.08']],
            colw=[2.9, 1.6, 1.7, 1.6, 1.6, 1.6, 1.33], size=14,
            takeaway='Percent.  Coverage of the 68 % interval on b_bp(555): 0.00, 0.02, 0.52, 0.63, 0.59 down the ladder.  Every cell reconciled against the IOPtics page (reports/rta_reconcile.md, 0 discrepancies).',
            source=SRC_IOP)

slide_text('B6 — Where every citation lives', [
    ('bullets', ['**62 artefacts cited; 47 not yet on main', 'RoB inelastic-rt (14), IOPtics rt-tests (18), PAB full-inelastic (6) + hyper_matchups (1), BING rob_cdom (3), this repository\'s qualifying-exam branch (4)',
                 'EPFT-UP and ocpy: everything on main', '**The manifest records, for each, the path, the branch and the last-touching commit', 'the advisor has undertaken to make main resolve them after submission',
                 '**Sweep outputs are not in git', 'parquet + chains under $OS_COLOR/IOPtics/runs on the canonical workstation; each page stamps the code and config that produced it'], 14),
    ('bullets', ['**Repositories', 'github.com/ocean-colour/{IOPtics, retrieve-or-bust, PAB, bing, EPFT-UP, ocpy}', 'github.com/Sea-Meets-the-Stars/claudes-phd-thesis',
                 '**Documentation sites', 'ioptics.readthedocs.io · retrieve-or-bust.readthedocs.io · pab-report.readthedocs.io · epft-up.readthedocs.io',
                 '**DOI', 'EPFT-UP v0.1.0: 10.5281/zenodo.22797970; others after submission'], 14),
], source='claudes-phd-thesis reports/citation_manifest.md, reports/merge_checklist.md (2026-09-18)')

# =========================================================================== #
OUT_DIR.mkdir(parents=True, exist_ok=True)
prs.save(OUT)
n_main = min(slide_no, TOTAL)
lines = ['# Speaker notes for the qualifying-exam oral', '',
         f'Deck: `reports/oral/qual_oral.pptx` ({slide_no} slides: {TOTAL} main + {slide_no - TOTAL} backup).  '
         'Notes are on the ten slides that carry the argument; they are also embedded in the .pptx and survive the Google Slides import.', '']
for no, title, text in notes_out:
    lines += [f'## Slide {no} — {title}', '', text, '']
NOTES_MD.write_text('\n'.join(lines))
print(f'wrote {OUT} with {slide_no} slides ({len(notes_out)} with speaker notes)')
print(f'wrote {NOTES_MD}')
