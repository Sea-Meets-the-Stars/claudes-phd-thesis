# Figure inventory for the qualifying-exam report and oral

Prompt 9 of `claude_prompts/qual_exam_prompts.md`, 2026-09-18, on `profx`.
One figure set serves both documents: the report shows each figure once, the
oral shows the same figures again at slide size.  Fourteen figures: ten built
here from data on disk, four reused from the source repositories.  Every file
is in `reports/figures/` as `figNN_<name>.png` (plus `.pdf` for the ten built
here) with a one-sentence caption beside it in `figNN_<name>.caption.txt`
stating what the reader should conclude.

Regenerate everything with

```bash
OS_COLOR=/home/xavier/Oceanography/data/Color \
  conda run -n ocean14 python claudes_phd_thesis/scripts/figures/make_all.py
```

Each `figNN_*.py` under `claudes_phd_thesis/scripts/figures/` is one figure and
runs alone; `_style.py` holds the shared palette and labels; `reuse_existing.py`
copies the four reused figures and records their source and producing script.

## What already existed (inventoried 2026-09-18)

| source | count | what | used |
|---|---|---|---|
| IOPtics `reports/figures/` | 22 | GLORIA and PANGAEA investigation figures (`reports/scripts/*.py`) | `talk_exemplar_fits.png` → fig 10 |
| IOPtics `docs/source/_static/` | 3 | site graphic, L23 overview, model components | none (fig 1 rebuilt cleaner from data) |
| IOPtics RT-ladder pages (prompt 6) | 13 kinds × 3 arms | fractional change, ΔBIC CDF/hist, scatters, accuracy vs wavelength | none directly; figs 5–8 rebuilt from the same tables with spelled-out labels |
| retrieve-or-bust `reports/` + `design/validation/` + `context/RT/` | 7 + 4 + 7 | forward-model ladder, unseen zenith, inelastic deltas, architecture | none directly; figs 2–3 rebuilt from the validation CSVs |
| retrieve-or-bust `reports/figs/` | 4 | biomass-summary figures (Schmidt EOI) | none (out of scope) |
| EPFT-UP `reports/figures/` | 6 | MOANA loadings, mapping verdict, masks, clipping, held-out skill | `moana_heldout_skill.png` → fig 11 |
| PAB `pab/matchup/chl/` + `cdom/` | 18 + 4 | Chl-a and CDOM report figures | `chl_reldiff_vs_magnitude.png` → fig 12, `chl_bias_raw_vs_adjusted.png` → fig 13 |
| PAB `docs/figures/` | 4 | architecture, example fit, hero graphic | none |
| BING | 0 | (figures cited in its logs are Mac-only) | — |

## The set

Sections follow the six chapters (Q20); the oral slot column is the proportion
prompt 11 gives (6 setup, 5 methods, 10 RT-A, 6 benchmarking, 4 EPFT-UP, 6 PAB,
3 future).  "exists" means the file is in `reports/figures/` now.

| # | file | report section / oral slot | built by | data | exists |
|---|---|---|---|---|---|
| 1 | `fig01_inverse_problem` | 1 Introduction / setup | `fig01_inverse_problem.py` | L23 X=4 bodies 0 and 2949 via the IOPtics L23 adapter | yes |
| 2 | `fig02_forward_model_ladder` | 2 Methods / methods | `fig02_forward_model_ladder.py` | RoB `design/validation/rrms_per_wavelength.csv`, `metrics.csv` | yes |
| 3 | `fig03_inelastic_terms` | 2 Methods / methods | `fig03_inelastic_terms.py` | RoB `design/validation/rrms_per_wavelength_inelastic.csv`, `metrics_inelastic.csv` | yes |
| 4 | `fig04_degeneracy_example` | 3 Separation / RT-A | `fig04_degeneracy_example.py` | `rt_tests_A_l23_v1/results_{scalar,spectral}.parquet` (body 1132, auto-picked) | yes |
| 5 | `fig05_rt_ladder_l23` | 3 Separation / RT-A (the headline) | `fig05_rt_ladder_l23.py` | `rt_tests_A_l23_v1/metrics_scalar.parquet` | yes |
| 6 | `fig06_rt_ladder_vs_wavelength` | 3 Separation / RT-A | `fig06_rt_ladder_vs_wavelength.py` | `metrics_spectral.parquet` of the L23 and PANGAEA arms | yes |
| 7 | `fig07_pace_fractional_change` | 3 Separation / RT-A (PACE) | `fig07_pace_fractional_change.py` | `rt_tests_B_v1/results_spectral.parquet` | yes |
| 8 | `fig08_dbic_three_arms` | 3 Separation / RT-A | `fig08_dbic_three_arms.py` | `results_scalar.parquet` of all three arms | yes |
| 9 | `fig09_benchmark_l23_pangaea` | 3 Separation / benchmarking | `fig09_benchmark_l23_pangaea.py` | `multi_L23_PANGAEA_v2` and `pangaea_fits_v2` `metrics_scalar.parquet` | yes |
| 10 | `fig10_gloria_turbid_fits` | 3 Separation / benchmarking | reused: IOPtics `reports/scripts/talk_exemplar_fits.py` | GLORIA turbid fits, four bb_p models | yes (PNG only) |
| 11 | `fig11_moana_heldout_skill` | 4 EPFT-UP / EPFT-UP | reused: EPFT-UP `reports/scripts/` | AMT23/25/28 held-out skill | yes (PNG only) |
| 12 | `fig12_pab_chl_bias_vs_magnitude` | 5 PAB / PAB | reused: PAB `pab/matchup/chl/` scripts | 9,814 Chl-a matchups, octile medians | yes (PNG only) |
| 13 | `fig13_pab_chl_raw_vs_adjusted` | 5 PAB / PAB | reused: PAB `pab/matchup/chl/` scripts | raw vs delayed-mode-adjusted Argo reference | yes (PNG only) |
| 14 | `fig14_timeline` | Timeline to completion / future work | `fig14_timeline.py` | dates from Q&A rounds 1–4 and prompts 6–15 (typed, sourced in comments) | yes |

Captions (one sentence each, the conclusion the reader should draw):

1. Ocean colour is an inverse problem: the one measurable spectrum must be decomposed into absorbing and scattering constituents, and in turbid water the water itself no longer dominates.
2. The forward-model error term can be driven from 7 % (Gordon) to 0.3 % (differentiable hybrid), so whatever retrieval error remains is not the physics.
3. Re-emitted light (Raman, chlorophyll fluorescence) is 15–20 % of the red-end signal; an elastic-only model cannot fit it and a retrieval will put that light somewhere in the constituents.
4. Two forward models fit the same reflectance equally well and return different phytoplankton and CDOM absorption: the fit cannot tell them apart.
5. Adding the missing physics removes the particulate-backscatter error almost entirely but leaves the phytoplankton and CDOM absorption errors where they were.
6. On synthetic data the physics fixes backscattering at every wavelength while the absorption split stays wrong; on in-situ spectra the fluorescence terms move error from CDOM into phytoplankton.
7. On real satellite spectra the physics moves retrieved backscatter down by about a fifth and leaves the absorption constituents nearly unchanged on average, with a wide spread.
8. The data prefer the fuller physics on synthetic spectra that contain it, are indifferent on sparse in-situ spectra, and split on satellite pixels; fit quality alone would not have found the physics error.
9. Three parameterizations agree on total absorption to 5–18 % and disagree by factors on the phytoplankton/CDOM split; on in-situ spectra half the apparent failures were an error-model artefact.
10. On turbid coastal water every backscatter parameterization returns the same failing fit, so a richer parameterization cannot be the fix.
11. The published MOANA coefficients transfer to independent hyperspectral spectra for picoeukaryotes but not for Prochlorococcus or Synechococcus.
12. Against BGC-Argo the PACE chlorophyll retrieval is high in clear water and low in rich water, changing sign near 0.1–0.2 mg m⁻³.
13. Scoring against adjusted rather than raw Argo chlorophyll moves the median bias from +0.13 to +0.58, larger than most of the retrieval physics.
14. Everything the exam report cites exists by the 19 September freeze; PAB 2.0, LS2 and the synthetic-Adg test follow, and the last is cut first.

## Conventions (so the set reads as one system)

- **Rungs are ordered**, so the five forward models take a single-hue ordinal
  ramp (light to dark blue, elastic to full inelastic), never five hues.
  Algorithms are categorical and take the reference palette's first three
  slots in fixed order (BING blue, GIOP orange, GSM aqua).  Truth is black ink.
- **Labels are spelled out** ("phytoplankton absorption a_ph at 440 nm [m⁻¹]",
  "remote-sensing reflectance"), no unexplained acronyms on an axis; where a
  symbol appears it sits beside its name.  Titles state the population and n.
- **One axis per panel**; bias and error share a percent axis; ratios are drawn
  on a log axis labelled as factors (0.1×, 1×, 10×) with folded end bins and
  their count stated.
- **Direct labels** on bars (values) and a legend for every multi-series panel;
  text is always ink, never a series colour.
- The palette validator in the data-viz skill needs `node`, which `profx`
  lacks; the colours are the reference palette's documented, already-validated
  categorical order and ordinal ramp, used unchanged.
- Figures 10–13 are reused as published in their repositories.  Their axis
  labels use the source conventions (`Chl^PACE`, `R_rs`); the captions above
  carry the plain-language reading, and the report text introduces each symbol
  before the figure appears.

## Decisions worth knowing

- Figure 4's example body is picked by rule (both rungs at χ²ν within 15 % of
  1, chlorophyll between 0.1 and 1 mg m⁻³, largest disagreement in a_ph at
  445 nm), not by hand; re-running picks the same body (1132) from the same data.
- Figure 5 is the centrepiece and is deliberately the same table as the
  IOPtics ladder page, drawn.  Its numbers reconcile to `reports/rta_reconcile.md`.
- Figure 9's right panel is the honest version of the PANGAEA story: the two
  bars per algorithm are two error models on the same spectra, not two runs of
  the algorithms.
- No figure is drawn from bbp700 validation, the RoB inversion, or an
  information-content quantity (A2 exclusions).
