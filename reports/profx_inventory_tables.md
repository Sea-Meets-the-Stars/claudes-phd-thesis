# profx inventory tables

Generated 2026-09-13 21:40 by `claudes_phd_thesis/scripts/profx_inventory.py` on host `profx`.  Read-only; regenerate rather than edit.

## Source repositories

| repo | checked-out branch | commits | first commit | last commit | local branches | tracked files | uncommitted changes | prompt docs | log entries |
|---|---|---|---|---|---|---|---|---|---|
| IOPtics | rt-tests | 122 | 2026-06-15 | 2026-09-10 | 8 | 294 | 0 | 16 | 166 |
| PAB | bbppaper | 99 | 2026-06-17 | 2026-09-13 | 7 | 178 | 0 | 15 | 141 |
| retrieve-or-bust | cdom-rt | 131 | 2026-06-29 | 2026-09-07 | 10 | 180 | 0 | 19 | 141 |
| bing | rob_cdom | 690 | 2024-06-04 | 2026-09-10 | 9 | 373 | 0 | 17 | 81 |
| claudes-phd-thesis | qualifying-exam | 7 | 2025-11-24 | 2026-09-13 | 2 | 14 | 2 | 2 | 9 |

## Output directories in the data tree (`$OS_COLOR`)

| path under $OS_COLOR | what it is | GiB | files | newest file |
|---|---|---|---|---|
| IOPtics/runs/expb_giop_L23_mcmc_full | Full-L23 MCMC sweep (expb_pow + giop, 3,320 spectra) | 2.13 | 3364 | 2026-09-07 |
| IOPtics/runs/multi_L23_PANGAEA_v2 | Three-algorithm L23 + PANGAEA sweep | 0.19 | 6 | 2026-08-10 |
| IOPtics/runs/pangaea_fits_base | PANGAEA fit investigation, base | 0.01 | 3 | 2026-08-10 |
| IOPtics/runs/pangaea_fits_maxfev | PANGAEA fit investigation, maxfev variant | 0.01 | 3 | 2026-08-10 |
| IOPtics/runs/pangaea_fits_qwip | PANGAEA QWIP annotation | 0.00 | 2 | 2026-08-12 |
| IOPtics/runs/pangaea_fits_turbid | PANGAEA turbid-model variants | 0.00 | 1 | 2026-08-10 |
| IOPtics/runs/pangaea_fits_v2 | PANGAEA fit investigation, v2 | 0.01 | 3 | 2026-08-10 |
| IOPtics/runs/rt_tests_smoke | RT-tests smoke run | 0.05 | 76 | 2026-09-09 |
| IOPtics/runs/rt_tests_A_pangaea_v1 | RT-A sweep, PANGAEA-97 (five RT variants) | 0.28 | 478 | 2026-09-10 |
| IOPtics/runs/rt_tests_A_l23_v1 | RT-A sweep, L23 X=4 (five RT variants; running) | 7.95 | 10710 | 2026-09-13 |
| IOPtics/pace_pab_100 | PACE-100 spectra extracted from PAB run1k | 0.00 | 1 | 2026-09-07 |
| PAB/full | PAB production database (pab_version 1.0) | 0.48 | 5 | 2026-09-11 |
| PAB/run1k | PAB run1k (273-matchup development run) | 0.83 | 3857 | 2026-07-31 |
| PAB/run10 | PAB run10 (pilot) | 14.91 | 156 | 2026-07-30 |
| PAB/bias_analysis | bbp700 bias follow-up (whybbp.md; Allie James's topic) | 0.00 | 27 | 2026-09-13 |
| Biomass/L23_Fits_Inelastic | BING biomass-paper L23 inelastic fits | 41.60 | 9960 | 2026-06-16 |

## RT-A sweep progress (IOPtics `rt_tests`, launched 2026-09-10)

| variant | PANGAEA chains | L23 chains |
|---|---|---|
| expb_pow_ztt_el | 95/97 | 3309/3320 |
| expb_pow_hyb_el | 95/97 | 3309/3320 |
| expb_pow_hyb_ram | 95/97 | 3309/3320 |
| expb_pow_hyb_ramfl | 95/97 | 781/3320 |
| expb_pow_hyb_ramflcdom | 95/97 | 0/3320 |

Launched 2026-09-10 05:34; 11183 MCMC fits persisted in 88.1 h (127 fits/h); 5902 remaining in stage 1; stage-1 ETA at that rate 2026-09-15 (metrics + report stages follow).
