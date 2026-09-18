# IOPtics runs tree on profx, consolidated

Generated 2026-09-18 03:11 by `claudes_phd_thesis/scripts/runs_consolidation.py` on `profx`. Read-only. Canonical tree: `/home/xavier/Oceanography/data/Color/IOPtics/runs`.

## Every sweep directory

| sweep | created | ioptics | noise | algorithms | rows | metrics | chains | figures | lb flag | in board | docs page(s) | cited by |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `expb_giop_L23_mcmc_full` | 2026-08-20 | dd4e162 | pace | expb_pow, giop | 9960 | yes | 3304 | 44 | True | yes | cross_algorithm, exemplar_fits | Ch 3 benchmarking: full-L23 MCMC vs chi-squared |
| `expb_giop_L23_test20` | 2026-08-07 | 61c83e0 | pace | expb_pow, giop | 48 | yes | 8 | 44 | True | yes | cross_algorithm, exemplar_fits | historical smoke sweep (not cited) |
| `gloria_turbid_v3` | 2026-07-31 | c70040c | insitu | expb_pow, expb_powflex, expb_pow2flat, expb_pow2 | 400 | yes | 0 | 32 | True | yes | cross_algorithm, exemplar_fits | Ch 3 GLORIA turbid-water case study |
| `multi_L23_PANGAEA_v2` | 2026-08-10 | 4ea86db | pct:0.05 | expb_pow, giop, gsm | 14739 | yes | 0 | 30 | True | yes | cross_algorithm, exemplar_fits | Ch 3 benchmarking: three algorithms on L23 (PANGAEA half superseded) |
| `pangaea_fits_base` | 2026-08-10 | 4ea86db | pct:0.05 | expb_pow, giop, gsm | 4779 | no | 0 | 0 | True | no |  | PANGAEA investigation Round 1 (report only) |
| `pangaea_fits_maxfev` | 2026-08-10 | 4ea86db | pct:0.05 | expb_pow, giop, gsm | 4779 | no | 0 | 0 | True | no |  | PANGAEA investigation Round 1 (report only) |
| `pangaea_fits_qwip` |  |  |  |  |  | no | 0 | 0 | True | no |  | PANGAEA investigation annotations (report only) |
| `pangaea_fits_turbid` |  |  |  |  |  | no | 0 | 0 | True | no |  | PANGAEA investigation turbid variants (report only) |
| `pangaea_fits_v2` | 2026-08-10 | 039c2b2 | insitu | expb_pow, giop, gsm | 4779 | yes | 0 | 20 | True | yes | cross_algorithm, exemplar_fits | Ch 3 benchmarking: PANGAEA under approved defaults |
| `rt_tests_A_l23_v1` | 2026-09-17 | 92eea90 | pace | expb_pow_ztt_el, expb_pow_hyb_el, expb_pow_hyb_ram, expb_pow_hyb_ramfl, expb_pow_hyb_ramflcdom | 33200 | yes | 16545 | 24 | False | no | rt_ladder | Ch 3 separation: RT ladder on L23 |
| `rt_tests_A_pangaea_v1` | 2026-09-10 | 92eea90 | insitu | expb_pow_ztt_el, expb_pow_hyb_el, expb_pow_hyb_ram, expb_pow_hyb_ramfl, expb_pow_hyb_ramflcdom | 970 | yes | 475 | 16 | False | no | rt_ladder | Ch 3 separation: RT ladder on PANGAEA-97 |
| `rt_tests_B_v1` | 2026-09-17 | 92eea90 | insitu | expb_pow_ztt_el, expb_pow_hyb_el, expb_pow_hyb_ram, expb_pow_hyb_ramfl, expb_pow_hyb_ramflcdom | 1000 | yes | 495 | 10 | False | no | rt_ladder | Ch 3 separation: RT ladder on PACE-100 (no truth) |
| `rt_tests_smoke` | 2026-09-09 | 3bdc719 | pace | expb_pow_ztt_el, expb_pow_hyb_el, expb_pow_hyb_ram, expb_pow_hyb_ramfl, expb_pow_hyb_ramflcdom | 160 | yes | 70 | 0 | False | no |  | RT smoke run (not cited) |

Leaderboard `leaderboard.parquet`: 788 rows folded from 5 sweep(s): expb_giop_L23_mcmc_full, expb_giop_L23_test20, gloria_turbid_v3, multi_L23_PANGAEA_v2, pangaea_fits_v2.

## Mac copies that collided, staged not merged

- `IOPtics/transfer_2026-09-17/leaderboard_mac.parquet` (39,777 B)
- `IOPtics/transfer_2026-09-17/runs/multi_L23_PANGAEA_v2/metrics_pairwise.parquet` (36,214 B)
- `IOPtics/transfer_2026-09-17/runs/multi_L23_PANGAEA_v2/metrics_scalar.parquet` (33,992 B)
- `IOPtics/transfer_2026-09-17/runs/multi_L23_PANGAEA_v2/metrics_spectral.parquet` (294,426 B)
- `IOPtics/transfer_2026-09-17/runs/multi_L23_PANGAEA_v2/provenance.yaml` (2,459 B)
- `IOPtics/transfer_2026-09-17/runs/multi_L23_PANGAEA_v2/results_scalar.parquet` (1,187,505 B)
- `IOPtics/transfer_2026-09-17/runs/multi_L23_PANGAEA_v2/results_spectral.parquet` (206,965,393 B)
- plus 32 figure files and 9 table files under the staged sweep

## The two `multi_L23_PANGAEA_v2` copies

Same sweep id, same 14,739 result rows, two code versions: `profx` created 2026-08-10T15:02:31Z at ioptics `4ea86db`; Mac created 2026-08-08T10:18:43Z at ioptics `e0e6729` (the committed page of 2026-08-08 was built from the Mac copy).

| quantity | max abs difference | rows differing |
|---|---|---|
| chi2 | 0.002739 | 540 of 14739 |
| BIC | 0.002739 | 540 of 14739 |
| a_cdom440 | 135.6 | 2530 of 14739 |
| beta | 0.001552 | 3455 of 14739 |
| Sdg | 0.0005512 | 1155 of 14739 |
| status | — | 4 of 14739 |

**Decision (prompt 8, Q54 unanswered, recommendation applied):** the `profx` copy is canonical — it ran on the later code, it is the copy the 2026-08-19 leaderboard fold used, and the page was regenerated from it on 2026-09-18 so page and tree agree. The Mac copy stays staged, untouched, until the advisor rules otherwise. `a_cdom440` differences are the point-estimate central-value fix that landed between the two runs, not a change in the fits (chi-squared agrees to 3e-3 or better).
