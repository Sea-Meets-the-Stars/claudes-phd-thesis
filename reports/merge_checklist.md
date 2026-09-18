# Merge checklist for the thesis source repositories

Generated 2026-09-17 by `claudes_phd_thesis/scripts/merge_checklist.py` on `MacBook-Pro-4.local`.  Read-only.  **The advisor runs every git command below.**

Goal (round-1 Q6): before the written report is drafted, every result the thesis cites should resolve to `main` of a public repository.  Counts are for this clone only -- run this on `profx`, which is canonical, for the authoritative version.

## IOPtics

Checked out: `ls2`.  `main` at 482427d 2026-06-29.

| branch | ahead | behind | tip | carries |
|---|---|---|---|---|
| `ls2` | 79 | 3 | 92eea90 2026-09-10 | LS2 (round-2 A8) |
| `rt-tests` | 79 | 3 | 92eea90 2026-09-10 | RT-A, the Q1 experiment |
| `origin/oops` | 69 | 3 | 4e75326 2026-08-14 |  |
| `origin/pangea` | 64 | 3 | 039c2b2 2026-08-10 |  |
| `improve-reporting` | 63 | 3 | 4ea86db 2026-08-08 |  |
| `moana` | 57 | 3 | 3aa3b6e 2026-09-12 |  |
| `waterhypernet` | 50 | 3 | c1e1cd5 2026-09-15 |  |
| `develop` | 48 | 3 | 26a9801 2026-08-01 | benchmarking framework |
| `first-go` | 46 | 3 | c20b06c 2026-08-02 |  |
| `origin/stage-3` | 6 | 5 | 62561b5 2026-06-30 |  |
| `origin/stage-0` *(merged -- safe to delete)* | 0 | 23 | 7f29ccd 2026-06-23 |  |

Suggested order, shallowest first so each merge is small:

```bash
# develop: 48 ahead -- benchmarking framework
git -C /Users/xavier/Oceanography/python/IOPtics merge --no-ff develop   # onto main
# ls2: 79 ahead -- LS2 (round-2 A8)
git -C /Users/xavier/Oceanography/python/IOPtics merge --no-ff ls2   # onto main
# rt-tests: 79 ahead -- RT-A, the Q1 experiment
git -C /Users/xavier/Oceanography/python/IOPtics merge --no-ff rt-tests   # onto main
```

## PAB

Checked out: `full-inelastic`.  `main` at 636ffd2 2026-06-26.

| branch | ahead | behind | tip | carries |
|---|---|---|---|---|
| `full-inelastic` | 136 | 0 | e3d2a61 2026-09-17 | PAB 2.0 |
| `hyper_matchups` | 100 | 0 | 78446b9 2026-09-11 | hyperspectral inventory |
| `pace_giop_gsm` | 100 | 0 | 3fd2a8f 2026-09-11 | NASA GIOP retrofit |
| `cdom_chl` | 98 | 0 | 502d301 2026-09-11 | CDOM and Chl-a reports |
| `database` | 83 | 0 | 9e6058a 2026-09-08 |  |
| `origin/develop` | 68 | 0 | 7e4bec2 2026-09-01 |  |
| `first-full-run` | 65 | 0 | 917a51b 2026-09-01 |  |
| `bbppaper` | 55 | 0 | 01fc0b4 2026-09-13 |  |

Suggested order, shallowest first so each merge is small:

```bash
# cdom_chl: 98 ahead -- CDOM and Chl-a reports
git -C /Users/xavier/Oceanography/python/PAB merge --no-ff cdom_chl   # onto main
# hyper_matchups: 100 ahead -- hyperspectral inventory
git -C /Users/xavier/Oceanography/python/PAB merge --no-ff hyper_matchups   # onto main
# pace_giop_gsm: 100 ahead -- NASA GIOP retrofit
git -C /Users/xavier/Oceanography/python/PAB merge --no-ff pace_giop_gsm   # onto main
# full-inelastic: 136 ahead -- PAB 2.0
git -C /Users/xavier/Oceanography/python/PAB merge --no-ff full-inelastic   # onto main
```

## bing

Checked out: `rob_rt`.  `main` at f242b0e 2026-07-29.

| branch | ahead | behind | tip | carries |
|---|---|---|---|---|
| `origin/rob_cdom` | 46 | 0 | bf56f6d 2026-09-10 | CDOM fluorescence |
| `rob_rt` | 41 | 0 | e849855 2026-09-02 |  |
| `origin/Kd` | 8 | 478 | ce8616f 2024-09-07 |  |
| `inelastic-fixes` | 3 | 1 | 763ac1c 2026-09-01 |  |
| `origin/prep_for_pip` | 2 | 19 | 859bc34 2026-06-27 |  |
| `develop` *(merged -- safe to delete)* | 0 | 1 | 7c91e6d 2026-07-29 | Raman/fluorescence fixes, RoB RT backend |
| `turbid_bbp` *(merged -- safe to delete)* | 0 | 2 | 503c43e 2026-07-30 |  |
| `origin/add_chl_fl` *(merged -- safe to delete)* | 0 | 154 | 3b9e68d 2026-05-24 |  |
| `origin/copilot/sub-pr-12` *(merged -- safe to delete)* | 0 | 325 | f268ead 2025-11-13 |  |
| `origin/copilot/sub-pr-12-again` *(merged -- safe to delete)* | 0 | 325 | 1eab588 2025-11-13 |  |
| `origin/implement_raman` *(merged -- safe to delete)* | 0 | 164 | 24d1f52 2026-02-25 |  |
| `origin/save_fit` *(merged -- safe to delete)* | 0 | 140 | 2aa4b8f 2026-05-25 |  |

Suggested order, shallowest first so each merge is small:

```bash
# origin/rob_cdom: 46 ahead -- CDOM fluorescence
git -C /Users/xavier/Oceanography/python/bing merge --no-ff origin/rob_cdom   # onto main
```

## retrieve-or-bust

Checked out: `inelastic-rt`.  `main` at a6acd35 2026-07-26.

| branch | ahead | behind | tip | carries |
|---|---|---|---|---|
| `inelastic-rt` | 106 | 5 | 5ca740d 2026-09-11 |  |
| `cdom-rt` | 105 | 5 | 0fd2e0b 2026-09-11 | CDOM RT (merged 2026-09-11, PR #21) |
| `origin/inelastic-rt-staging` | 85 | 5 | d67f1ec 2026-08-27 |  |
| `origin/nasa_a15` | 69 | 0 | d623dba 2026-09-02 |  |
| `RT` | 66 | 0 | c42ef25 2026-08-29 |  |
| `rt-elastic-prototype` | 52 | 5 | 69d577f 2026-08-13 |  |
| `vicc-proposal` | 17 | 5 | 52097d2 2026-08-15 |  |
| `graphic` | 5 | 5 | d90461f 2026-07-19 |  |
| `model-priors` | 5 | 5 | eb409d9 2026-08-28 |  |
| `claude-science` *(merged -- safe to delete)* | 0 | 8 | ab623e1 2026-07-15 |  |
| `develop` *(merged -- safe to delete)* | 0 | 5 | ddadc0d 2026-07-15 |  |
| `websites` *(merged -- safe to delete)* | 0 | 1 | 223d562 2026-07-22 |  |
| `origin/start_up` *(merged -- safe to delete)* | 0 | 29 | 88f79b3 2026-06-29 |  |

Suggested order, shallowest first so each merge is small:

```bash
# cdom-rt: 105 ahead -- CDOM RT (merged 2026-09-11, PR #21)
git -C /Users/xavier/Oceanography/python/retrieve-or-bust merge --no-ff cdom-rt   # onto main
```

## EPFT-UP

Checked out: `diatom`.  `main` at cd07fd1 2026-09-12.

| branch | ahead | behind | tip | carries |
|---|---|---|---|---|
| `diatom` | 8 | 0 | 10b14ec 2026-09-15 |  |
| `moana` | 7 | 0 | ac9f640 2026-09-14 |  |
| `start-up` | 3 | 0 | 836adb2 2026-09-12 |  |

## ocpy

Checked out: `whn`.  `main` at 3aed28a 2026-07-30.

| branch | ahead | behind | tip | carries |
|---|---|---|---|---|
| `origin/dev` | 31 | 195 | b5d9e26 2023-11-18 |  |
| `origin/xiop` | 8 | 84 | 73b453b 2025-01-01 |  |
| `origin/dye` | 6 | 195 | 560b137 2023-10-30 |  |
| `origin/Ed` | 3 | 28 | 5702286 2026-04-13 |  |
| `origin/correlated_error` | 2 | 55 | a084056 2025-11-24 |  |
| `origin/pace_giop` | 1 | 0 | c3132a6 2026-09-09 |  |
| `gloria` *(merged -- safe to delete)* | 0 | 9 | da6dff9 2026-07-26 |  |
| `whn` *(merged -- safe to delete)* | 0 | 0 | 3aed28a 2026-07-30 |  |
| `origin/develop` *(merged -- safe to delete)* | 0 | 11 | ec021ad 2026-06-26 |  |
| `origin/hyper-a` *(merged -- safe to delete)* | 0 | 51 | 800a703 2025-12-11 |  |
| `origin/package_data` *(merged -- safe to delete)* | 0 | 9 | ab92bfb 2026-06-27 |  |
| `origin/panagea` *(merged -- safe to delete)* | 0 | 12 | e913f4b 2026-06-26 |  |
| `origin/prep_for_pip` *(merged -- safe to delete)* | 0 | 4 | 24a207a 2026-06-29 |  |

## Known blockers

- **`bing/setup.py` pins RoB's deleted `cdom-rt` branch** (merged and deleted 2026-09-11, PR #21), so `pip install ./bing` fails and the PAB 2.0 image build had to patch its staged copy.  Move the pin to a tag or to `main` *before* merging BING `develop`, or the merge ships a broken install.
- **Run outputs are never committed**, by design.  Merging a branch does not bring its evidence; the evidence travels by the transfer manifest (`reports/mac_to_profx_manifest.md`).
- **MOANA left IOPtics** for `EPFT-UP` on 2026-09-13; IOPtics' `moana` branch is now history, not a merge target.

