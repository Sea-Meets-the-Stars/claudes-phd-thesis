# Merge checklist for the thesis source repositories

Generated 2026-09-18 by `claudes_phd_thesis/scripts/merge_checklist.py` on `profx`.  Read-only.  **The advisor runs every git command below.**

Goal (round-1 Q6): before the written report is drafted, every result the thesis cites should resolve to `main` of a public repository.  Counts are for this clone only -- run this on `profx`, which is canonical, for the authoritative version.

## IOPtics

Checked out: `rt-tests`.  `main` at e66a942 2026-06-22.

| branch | ahead | behind | tip | carries |
|---|---|---|---|---|
| `rt-tests` | 101 | 0 | 5890c81 2026-09-18 | RT-A, the Q1 experiment |
| `improve-reporting` | 94 | 0 | 0207b8b 2026-08-20 |  |
| `oops` | 90 | 0 | 4e75326 2026-08-14 |  |
| `pangea` | 90 | 0 | 4e75326 2026-08-14 |  |
| `moana` | 74 | 0 | a80e3b1 2026-08-17 |  |
| `origin/develop` | 69 | 0 | 26a9801 2026-08-01 | benchmarking framework |
| `first-go` | 57 | 0 | 882b661 2026-07-21 |  |
| `origin/stage-3` | 27 | 2 | 62561b5 2026-06-30 |  |
| `origin/stage-2` | 16 | 2 | 0331b44 2026-06-29 |  |
| `stage-1` | 10 | 2 | 75cc36e 2026-06-27 |  |
| `origin/stage-0` | 3 | 2 | 7f29ccd 2026-06-23 |  |

Suggested order, shallowest first so each merge is small:

```bash
# origin/develop: 69 ahead -- benchmarking framework
git -C /home/xavier/Oceanography/python/IOPtics merge --no-ff origin/develop   # onto main
# rt-tests: 101 ahead -- RT-A, the Q1 experiment
git -C /home/xavier/Oceanography/python/IOPtics merge --no-ff rt-tests   # onto main
```

## PAB

Checked out: `full-inelastic`.  `main` at 7089074 2026-06-21.

| branch | ahead | behind | tip | carries |
|---|---|---|---|---|
| `full-inelastic` | 152 | 0 | e3d2a61 2026-09-17 | PAB 2.0 |
| `pace_giop_gsm` | 116 | 0 | 3fd2a8f 2026-09-11 | NASA GIOP retrofit |
| `origin/hyper_matchups` | 116 | 0 | 78446b9 2026-09-11 | hyperspectral inventory |
| `origin/cdom_chl` | 114 | 0 | 502d301 2026-09-11 | CDOM and Chl-a reports |
| `origin/database` | 106 | 0 | 1c36365 2026-09-16 |  |
| `first-full-run` | 79 | 0 | 0a3c577 2026-08-27 |  |
| `bbppaper` | 69 | 0 | 9972ad0 2026-09-13 |  |
| `stage-9` | 38 | 0 | a2b9378 2026-07-03 |  |
| `develop` | 27 | 0 | 6e08b9a 2026-06-28 |  |
| `stage-8` | 15 | 2 | 139de37 2026-06-26 |  |
| `origin/stage-7` | 10 | 2 | ccc7bb1 2026-06-24 |  |
| `origin/stage-6` | 9 | 2 | d49cd50 2026-06-24 |  |
| `origin/stage5` | 3 | 2 | 425e5f4 2026-06-22 |  |
| `origin/setup` *(merged -- safe to delete)* | 0 | 26 | a98ea86 2026-06-17 |  |

Suggested order, shallowest first so each merge is small:

```bash
# origin/cdom_chl: 114 ahead -- CDOM and Chl-a reports
git -C /home/xavier/Oceanography/python/PAB merge --no-ff origin/cdom_chl   # onto main
# pace_giop_gsm: 116 ahead -- NASA GIOP retrofit
git -C /home/xavier/Oceanography/python/PAB merge --no-ff pace_giop_gsm   # onto main
# origin/hyper_matchups: 116 ahead -- hyperspectral inventory
git -C /home/xavier/Oceanography/python/PAB merge --no-ff origin/hyper_matchups   # onto main
# full-inelastic: 152 ahead -- PAB 2.0
git -C /home/xavier/Oceanography/python/PAB merge --no-ff full-inelastic   # onto main
```

## bing

Checked out: `rob_cdom`.  `main` at f242b0e 2026-07-29.

| branch | ahead | behind | tip | carries |
|---|---|---|---|---|
| `rob_cdom` | 46 | 0 | bf56f6d 2026-09-10 | CDOM fluorescence |
| `develop` | 43 | 0 | 51a0fb9 2026-09-02 | Raman/fluorescence fixes, RoB RT backend |
| `origin/Kd` | 8 | 478 | ce8616f 2024-09-07 |  |
| `inelastic-fixes` | 2 | 1 | 850000b 2026-08-19 |  |
| `origin/prep_for_pip` | 2 | 19 | 859bc34 2026-06-27 |  |
| `PAB_edits` *(merged -- safe to delete)* | 0 | 18 | 8c2a8a7 2026-06-27 |  |
| `bing_2.0` *(merged -- safe to delete)* | 0 | 351 | e0106c0 2025-05-23 |  |
| `biomass` *(merged -- safe to delete)* | 0 | 19 | 4ab1306 2026-06-20 |  |
| `resub_bing_copernicus` *(merged -- safe to delete)* | 0 | 341 | c1d5fb3 2025-06-10 |  |
| `sbg_poster` *(merged -- safe to delete)* | 0 | 352 | c6789e0 2025-05-23 |  |
| `origin/Ed` *(merged -- safe to delete)* | 0 | 367 | 3d74330 2025-03-17 |  |
| `origin/Sexp_prior` *(merged -- safe to delete)* | 0 | 466 | 41eab5e 2024-08-26 |  |
| `origin/add_chl_fl` *(merged -- safe to delete)* | 0 | 154 | 3b9e68d 2026-05-24 |  |
| `origin/cdom_aph` *(merged -- safe to delete)* | 0 | 331 | 314135d 2025-07-28 |  |
| `origin/copilot/sub-pr-12` *(merged -- safe to delete)* | 0 | 325 | f268ead 2025-11-13 |  |
| `origin/copilot/sub-pr-12-again` *(merged -- safe to delete)* | 0 | 325 | 1eab588 2025-11-13 |  |
| `origin/ema` *(merged -- safe to delete)* | 0 | 368 | 6802364 2025-02-27 |  |
| `origin/implement_raman` *(merged -- safe to delete)* | 0 | 164 | 24d1f52 2026-02-25 |  |
| `origin/jxp_model` *(merged -- safe to delete)* | 0 | 458 | 6540b04 2024-09-18 |  |
| `origin/oo_poster` *(merged -- safe to delete)* | 0 | 473 | a8438ac 2024-10-02 |  |
| `origin/profxj-patch-1` *(merged -- safe to delete)* | 0 | 211 | b5098dc 2025-11-17 |  |
| `origin/save_fit` *(merged -- safe to delete)* | 0 | 140 | 2aa4b8f 2026-05-25 |  |
| `origin/turbid_bbp` *(merged -- safe to delete)* | 0 | 2 | 503c43e 2026-07-30 |  |

Suggested order, shallowest first so each merge is small:

```bash
# develop: 43 ahead -- Raman/fluorescence fixes, RoB RT backend
git -C /home/xavier/Oceanography/python/bing merge --no-ff develop   # onto main
# rob_cdom: 46 ahead -- CDOM fluorescence
git -C /home/xavier/Oceanography/python/bing merge --no-ff rob_cdom   # onto main
```

## retrieve-or-bust

Checked out: `inelastic-rt`.  `main` at a6acd35 2026-07-26.

| branch | ahead | behind | tip | carries |
|---|---|---|---|---|
| `inelastic-rt` | 107 | 5 | e1f4289 2026-09-15 |  |
| `cdom-rt` | 104 | 5 | dfab27c 2026-09-07 | CDOM RT (merged 2026-09-11, PR #21) |
| `nasa_a15` | 69 | 0 | d623dba 2026-09-02 |  |
| `vicc-proposal` | 68 | 5 | 02468c6 2026-08-25 |  |
| `RT` | 64 | 5 | a95aedd 2026-08-23 |  |
| `inelastic-rt-staging` | 64 | 5 | a95aedd 2026-08-23 |  |
| `origin/rt-elastic-prototype` | 52 | 5 | 69d577f 2026-08-13 |  |
| `origin/graphic` | 5 | 5 | d90461f 2026-07-19 |  |
| `model-priors` | 3 | 5 | be6c655 2026-08-15 |  |
| `claude-science` *(merged -- safe to delete)* | 0 | 9 | a99578f 2026-07-15 |  |
| `develop` *(merged -- safe to delete)* | 0 | 5 | ddadc0d 2026-07-15 |  |
| `origin/start_up` *(merged -- safe to delete)* | 0 | 29 | 88f79b3 2026-06-29 |  |
| `origin/websites` *(merged -- safe to delete)* | 0 | 1 | 223d562 2026-07-22 |  |

Suggested order, shallowest first so each merge is small:

```bash
# cdom-rt: 104 ahead -- CDOM RT (merged 2026-09-11, PR #21)
git -C /home/xavier/Oceanography/python/retrieve-or-bust merge --no-ff cdom-rt   # onto main
```

## EPFT-UP

Checked out: `main`.  `main` at 43080eb 2026-09-17.

| branch | ahead | behind | tip | carries |
|---|---|---|---|---|
| `origin/diatom` | 1 | 3 | 10b14ec 2026-09-15 |  |
| `origin/moana` *(merged -- safe to delete)* | 0 | 3 | ac9f640 2026-09-14 |  |

## ocpy

Checked out: `pace_giop`.  `main` at da55e1a 2026-06-27.

| branch | ahead | behind | tip | carries |
|---|---|---|---|---|
| `origin/dev` | 31 | 187 | b5d9e26 2023-11-18 |  |
| `origin/ihop` | 26 | 187 | fd2092a 2023-11-03 |  |
| `pace_giop` | 9 | 0 | c3132a6 2026-09-09 |  |
| `develop` | 8 | 0 | 3aed28a 2026-07-30 |  |
| `origin/xiop` | 8 | 76 | 73b453b 2025-01-01 |  |
| `origin/dye` | 6 | 187 | 560b137 2023-10-30 |  |
| `origin/prep_for_pip` | 4 | 0 | 24a207a 2026-06-29 |  |
| `origin/Ed` | 3 | 20 | 5702286 2026-04-13 |  |
| `gloria` | 2 | 3 | da6dff9 2026-07-26 |  |
| `origin/correlated_error` | 2 | 47 | a084056 2025-11-24 |  |
| `figures` *(merged -- safe to delete)* | 0 | 60 |  |  |
| `plot_pace` *(merged -- safe to delete)* | 0 | 33 | 3e17792 2026-02-01 |  |
| `water_world` *(merged -- safe to delete)* | 0 | 53 | b1d6a10 2025-06-11 |  |
| `origin/Kdpar` *(merged -- safe to delete)* | 0 | 49 | 62b7ca7 2025-09-07 |  |
| `origin/hyper-a` *(merged -- safe to delete)* | 0 | 43 | 800a703 2025-12-11 |  |
| `origin/kd_NN` *(merged -- safe to delete)* | 0 | 183 | 139ca9e 2024-05-09 |  |
| `origin/nmf_paper_support` *(merged -- safe to delete)* | 0 | 134 | bb54c1f 2024-05-21 |  |
| `origin/package_data` *(merged -- safe to delete)* | 0 | 1 | ab92bfb 2026-06-27 |  |
| `origin/panagea` *(merged -- safe to delete)* | 0 | 4 | e913f4b 2026-06-26 |  |
| `origin/raman` *(merged -- safe to delete)* | 0 | 47 | 116a237 2025-11-15 |  |
| `origin/rrs_ood` *(merged -- safe to delete)* | 0 | 125 | 788a6e4 2024-05-17 |  |
| `origin/support_ihop` *(merged -- safe to delete)* | 0 | 69 | bd1068a 2025-01-11 |  |

## Known blockers

- **`bing/setup.py` pins RoB's deleted `cdom-rt` branch** (merged and deleted 2026-09-11, PR #21), so `pip install ./bing` fails and the PAB 2.0 image build had to patch its staged copy.  Move the pin to a tag or to `main` *before* merging BING `develop`, or the merge ships a broken install.
- **Run outputs are never committed**, by design.  Merging a branch does not bring its evidence; the evidence travels by the transfer manifest (`reports/mac_to_profx_manifest.md`).
- **MOANA left IOPtics** for `EPFT-UP` on 2026-09-13; IOPtics' `moana` branch is now history, not a merge target.

