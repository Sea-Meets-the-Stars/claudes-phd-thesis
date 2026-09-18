# Citation manifest

Generated 2026-09-18 03:12 by `claudes_phd_thesis/scripts/citation_manifest.py` on `profx`.  Read-only git.  Citations in the report point at `main` (A18); a row whose `on main` is **no** is on the merge list — the branch and hash say where it lives today.  `origin/main` is used where the remote exists, since that is what a reader will fetch.

**62 citations; 47 not yet on `main`.**

| # | repository | path (main-relative) | chapter | what | on main | lives on | hash | note |
|---|---|---|---|---|---|---|---|---|
| 1 | retrieve-or-bust | `reports/report_rt_elastic_model.md` | Ch 2 | elastic forward model report v1.0 (0.30 % rRMS) | **no** | `inelastic-rt` | 3e15778 |  |
| 2 | retrieve-or-bust | `reports/report_rt_inelastic_model.md` | Ch 2 | inelastic forward model report v1.0 (0.34 % rRMS) + M5 addendum | **no** | `inelastic-rt` | dfab27c |  |
| 3 | retrieve-or-bust | `design/rt_elastic_model.md` | Ch 2 | elastic design document | **no** | `inelastic-rt` | 4a7250d |  |
| 4 | retrieve-or-bust | `design/rt_inelastic_model.md` | Ch 2 | inelastic design document | **no** | `inelastic-rt` | f1bd765 |  |
| 5 | retrieve-or-bust | `design/rt_cdom_fluorescence_model.md` | Ch 2 | CDOM fluorescence design (M5) | **no** | `inelastic-rt` | 55bafe8 |  |
| 6 | retrieve-or-bust | `design/validation/metrics.md` | Ch 2 | elastic validation table | **no** | `inelastic-rt` | 1919f12 |  |
| 7 | retrieve-or-bust | `design/validation/metrics_inelastic.md` | Ch 2 | inelastic validation table | **no** | `inelastic-rt` | 1b36430 |  |
| 8 | retrieve-or-bust | `robust/rt/files/emulator_l23.npz` | Ch 2 | trained emulator weights (417 parameters) | **no** | `inelastic-rt` | 69e192a |  |
| 9 | retrieve-or-bust | `robust/rt/files/raman_corr_l23.npz` | Ch 2 | Raman correction head | **no** | `inelastic-rt` | 40becd8 |  |
| 10 | retrieve-or-bust | `robust/rt/files/fl_corr_l23.npz` | Ch 2 | fluorescence correction head | **no** | `inelastic-rt` | 40becd8 |  |
| 11 | retrieve-or-bust | `robust/rt/data/ed_l23.npz` | Ch 2 | packaged E_d table used by every RT sweep | **no** | `inelastic-rt` | 1cedae7 |  |
| 12 | retrieve-or-bust | `robust/rt/emulator.py` | Ch 2 | emulator incl. the 2026-09-15 off-nadir fix | **no** | `inelastic-rt` | e1f4289 |  |
| 13 | retrieve-or-bust | `robust/solar.py` | Ch 2 | NOAA solar zenith used for PANGAEA/PACE geometry | **no** | `inelastic-rt` | abf4360 |  |
| 14 | retrieve-or-bust | `docs/using/limitations.md` | Ch 2 | the forward/inversion boundary in RoB's words | **no** | `inelastic-rt` | 363951d |  |
| 15 | bing | `docs/radiative_transfer.rst` | Ch 2 | RT backends, inelastic terms, CDOM fluorescence | yes | `origin/main` | 2c82ab6 |  |
| 16 | bing | `bing/rt/defs.py` | Ch 2 | rt_dict incl. rt_backend / fit_Bp / include_CDOM_fl | yes | `origin/main` | 99a2a7b |  |
| 17 | bing | `bing/evaluate.py` | Ch 2 | robust-backend dispatch | yes | `origin/main` | b2c0367 |  |
| 18 | bing | `bing/tests/test_l23_inelastic.py` | Ch 2 | L23-anchored inelastic regression (1/pi fix) | **no** | `rob_cdom` | bd4180e |  |
| 19 | bing | `claude_prompts/inelastic_fixes.md` | Ch 2 | provenance of the fluorescence/Raman fixes | **no** | `rob_cdom` | a408b68 |  |
| 20 | bing | `bing/models/bbnw.py` | Ch 3 | turbid-water bb_p models Pow2 / Pow2Flat / PowFlex | yes | `origin/main` | 41a8c6a |  |
| 21 | bing | `claude_prompts/turbid_waters.md` | Ch 3 | provenance of the turbid-water models | **no** | `rob_cdom` | ae04cd6 |  |
| 22 | IOPtics | `docs/source/reports/rt_tests_A_l23_v1/rt_ladder.rst` | Ch 3 | RT ladder, L23 X=4 (3,320 spectra) | **no** | `rt-tests` | 5890c81 |  |
| 23 | IOPtics | `docs/source/reports/rt_tests_A_pangaea_v1/rt_ladder.rst` | Ch 3 | RT ladder, PANGAEA-97 | **no** | `rt-tests` | 5890c81 |  |
| 24 | IOPtics | `docs/source/reports/rt_tests_B_v1/rt_ladder.rst` | Ch 3 | RT ladder, PACE-100 (no truth) + PAB consistency | **no** | `rt-tests` | 5890c81 |  |
| 25 | IOPtics | `ioptics/report/rt_ladder.py` | Ch 3 | the RT-ladder page type | **no** | `rt-tests` | 5890c81 |  |
| 26 | IOPtics | `ioptics/runs/prototypes/rt_tests/run_rta_l23.yaml` | Ch 3 | RT-A L23 sweep config | **no** | `rt-tests` | 92eea90 |  |
| 27 | IOPtics | `ioptics/runs/prototypes/rt_tests/run_rta_pangaea.yaml` | Ch 3 | RT-A PANGAEA sweep config | **no** | `rt-tests` | 92eea90 |  |
| 28 | IOPtics | `ioptics/runs/prototypes/rt_tests/run_rtb.yaml` | Ch 3 | RT-B PACE sweep config | **no** | `rt-tests` | 509ec89 |  |
| 29 | IOPtics | `ioptics/runs/prototypes/rt_tests/pangaea97_ids.csv` | Ch 3 | frozen PANGAEA-97 population | **no** | `rt-tests` | 509ec89 |  |
| 30 | IOPtics | `ioptics/runs/prototypes/rt_tests/pace100_ids.csv` | Ch 3 | frozen PACE-100 population | **no** | `rt-tests` | 509ec89 |  |
| 31 | IOPtics | `ioptics/runs/prototypes/rt_tests/pab_consistency.py` | Ch 3 | RT-B vs PAB run1k consistency check | **no** | `rt-tests` |  | uncommitted (working tree only) |
| 32 | IOPtics | `ioptics/algorithms/registry.py` | Ch 3 | the five RT variants and RT_DBIC_PAIR | yes | `origin/main` | 17785f0 |  |
| 33 | IOPtics | `claude_prompts/rt_tests.md` | Ch 3 | design decisions Q1–Q55 and run logs | **no** | `rt-tests` | 5890c81 |  |
| 34 | IOPtics | `docs/source/reports/expb_giop_L23_mcmc_full/cross_algorithm.rst` | Ch 3 | full-L23 MCMC vs chi-squared, expb_pow vs giop | **no** | `rt-tests` | 0207b8b |  |
| 35 | IOPtics | `docs/source/reports/multi_L23_PANGAEA_v2/cross_algorithm.rst` | Ch 3 | three algorithms on L23 (+ superseded PANGAEA half) | **no** | `rt-tests` | 4ea86db |  |
| 36 | IOPtics | `docs/source/reports/pangaea_fits_v2/cross_algorithm.rst` | Ch 3 | PANGAEA under approved defaults (43/53/38 % ok) | **no** | `rt-tests` |  | uncommitted (working tree only) |
| 37 | IOPtics | `docs/source/reports/gloria_turbid_v3/cross_algorithm.rst` | Ch 3 | GLORIA turbid sweep: four bb_p models, one fit | **no** | `rt-tests` | 3ff2b7e |  |
| 38 | IOPtics | `docs/source/reports/gloria_investigation.rst` | Ch 3 | GLORIA investigation (converted report, with editorial warning) | **no** | `rt-tests` | 1093886 |  |
| 39 | IOPtics | `docs/source/reports/index.rst` | Ch 3 | cross-sweep leaderboard landing page | yes | `origin/main` | fb81818 |  |
| 40 | IOPtics | `reports/gloria_fits_report.md` | Ch 3 | GLORIA investigation report (markdown original) | **no** | `rt-tests` | eed3b32 |  |
| 41 | IOPtics | `reports/pangaea_fits_report.md` | Ch 3 | PANGAEA investigation report | **no** | `rt-tests` | f07cc6e |  |
| 42 | IOPtics | `docs/design/IOPtics_design.md` | Ch 3 | benchmarking framework design | yes | `origin/main` | ce413b9 |  |
| 43 | IOPtics | `docs/design/IOPtics_implementation.md` | Ch 3 | benchmarking framework implementation record | yes | `origin/main` | 15bbe89 |  |
| 44 | IOPtics | `claude_prompts/LS2/ls2_prompts.md` | Ch 3 | LS2 planning (future work) — written on the Mac 2026-09-17, untracked on its `ls2` branch; not on profx | **no** | `` |  | NOT FOUND on this machine |
| 45 | ocpy | `ocpy/ls2/ls2_main.py` | Ch 3 | the existing LS2 implementation (Loisel 2018 port) | yes | `origin/main` | a03ecab |  |
| 46 | EPFT-UP | `reports/MOANA_Claude_Report.md` | Ch 4 | MOANA reimplementation report (rev 4) | yes | `origin/main` | c2ac705 |  |
| 47 | EPFT-UP | `reports/moana_rederivation.md` | Ch 4 | re-derivation audit: 35 numbers, 6 figures reproduced | yes | `origin/main` | c2ac705 |  |
| 48 | EPFT-UP | `reports/moana_blocked.md` | Ch 4 | what blocks the retrain (PML data) | yes | `origin/main` | c2ac705 |  |
| 49 | EPFT-UP | `README.md` | Ch 4 | the EPFT-UP framework statement | yes | `origin/main` | 43080eb |  |
| 50 | PAB | `reports/PAB/pab_chl_matchups_report.md` | Ch 5 | PACE vs BGC-Argo Chl-a report (2026-09-07) | **no** | `full-inelastic` | b0be40c |  |
| 51 | PAB | `reports/PAB/pab_cdom_matchups_report.md` | Ch 5 | PACE vs BGC-Argo CDOM report v1.0 (qualitative) | **no** | `full-inelastic` | 778ed3e |  |
| 52 | PAB | `docs/design/PAB_full_run_report.md` | Ch 5 | production run close-out (pab_version 1.0) | **no** | `full-inelastic` | 4ef1d16 |  |
| 53 | PAB | `docs/design/PAB_design.md` | Ch 5 | PAB design document | yes | `origin/main` | c377f6e |  |
| 54 | PAB | `claude_prompts/pace_giop_gsm.md` | Ch 5 | NASA GIOP retrofit (BING vs GIOP) | **no** | `full-inelastic` | 3fd2a8f |  |
| 55 | PAB | `claude_prompts/hyper_matchups.md` | Ch 5 | hyperspectral floats + the match truncation finding | **no** | `origin/hyper_matchups` | f49bb83 |  |
| 56 | PAB | `claude_prompts/v2/run_full_inelastic.md` | Ch 5 | PAB 2.0 plan | **no** | `full-inelastic` | 6e6d050 |  |
| 57 | PAB | `claude_prompts/v2/build_v2_prompt_3.md` | Ch 5 | PAB 2.0 first real fits (2.0 vs 1.0 bb_p) | **no** | `full-inelastic` | 3efc987 |  |
| 58 | claudes-phd-thesis | `claude_prompts/start_up.md` | Ch 1/6 | scoping interview and Report | yes | `origin/main` | a14ee42 |  |
| 59 | claudes-phd-thesis | `claude_prompts/qual_exam_prompts.md` | Ch 1/6 | qualifying-exam Q&A rounds 1–4 and prompts | **no** | `qualifying-exam` | 751b8c4 |  |
| 60 | claudes-phd-thesis | `claude_prompts/profx_inventory.md` | Ch 1/6 | inventory of Claude's work on profx | **no** | `qualifying-exam` | df86e1b |  |
| 61 | claudes-phd-thesis | `reports/rta_reconcile.md` | Ch 3 | RT-A page vs provisional read reconciliation | **no** | `qualifying-exam` | 751b8c4 |  |
| 62 | claudes-phd-thesis | `reports/citation_manifest.md` | all | this manifest | **no** | `qualifying-exam` |  | uncommitted (working tree only) |

## Merge list (what must reach `main` for the citations to resolve)

- **retrieve-or-bust**: `inelastic-rt` (14 path(s))
- **bing**: `rob_cdom` (3 path(s))
- **IOPtics**: `rt-tests` (18 path(s)); `(uncommitted)` (1 path(s))
- **PAB**: `full-inelastic` (6 path(s)); `origin/hyper_matchups` (1 path(s))
- **claudes-phd-thesis**: `qualifying-exam` (4 path(s))

## Sweep outputs outside git (`$OS_COLOR/IOPtics/runs/`)

| sweep | created | ioptics commit | bing commit | rows | page |
|---|---|---|---|---|---|
| `expb_giop_L23_mcmc_full` | 2026-08-20 | dd4e162 | 850000b | 9960 | cross_algorithm, exemplar_fits |
| `multi_L23_PANGAEA_v2` | 2026-08-10 | 4ea86db | None | 14739 | cross_algorithm, exemplar_fits |
| `pangaea_fits_v2` | 2026-08-10 | 039c2b2 | f242b0e | 4779 | cross_algorithm, exemplar_fits |
| `gloria_turbid_v3` | 2026-07-31 | c70040c | f242b0e | 400 | cross_algorithm, exemplar_fits |
| `rt_tests_A_l23_v1` | 2026-09-17 | 92eea90 | bf56f6d | 33200 | rt_ladder |
| `rt_tests_A_pangaea_v1` | 2026-09-10 | 92eea90 | bf56f6d | 970 | rt_ladder |
| `rt_tests_B_v1` | 2026-09-17 | 92eea90 | bf56f6d | 1000 | rt_ladder |

These are not in any repository by design (parquet + chains); the page carries their provenance stamp, and `reports/runs_consolidation.md` records the tree they sit in.
