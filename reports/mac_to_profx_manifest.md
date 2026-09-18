# Mac -> profx transfer manifest

Generated 2026-09-17 by `claudes_phd_thesis/scripts/mac_to_profx_manifest.py` on `MacBook-Pro-4.local`.  Read-only: this script measures and prints commands; it runs nothing.

`profx` is canonical for thesis evidence (round-1 A6).  Everything below must be on `profx` before the 2026-09-19 18:00 exam evidence freeze.

## 1. Sweep outputs (Drive)

| tree under `$OS_COLOR` | size | what it is |
|---|---|---|
| `IOPtics/runs/expb_giop_L23_test20` | 107.7 MB | test20 two-algorithm sweep, 2026-07-03 |
| `IOPtics/runs/gloria_turbid_v3` | 30.6 MB | GLORIA turbid sweep (Ch 3 case study) |
| `IOPtics/runs/multi_L23_PANGAEA_v2` | 201.5 MB | three-algorithm L23 + PANGAEA sweep, 2026-08-08 |
| `IOPtics/leaderboard.parquet` | 38.8 KB | cross-sweep leaderboard |
| `IOPtics/whn_explore` | 8.5 MB | WaterHypernet exploration |

**Total to move: 348.3 MB.**

### Push, from this Mac

```bash
rclone copy -P '/Users/xavier/Projects/Oceanography/data/Color/IOPtics/runs/expb_giop_L23_test20' 'AIOcean:Claude_PhD_transfer/2026-09-17/IOPtics/runs/expb_giop_L23_test20'
rclone copy -P '/Users/xavier/Projects/Oceanography/data/Color/IOPtics/runs/gloria_turbid_v3' 'AIOcean:Claude_PhD_transfer/2026-09-17/IOPtics/runs/gloria_turbid_v3'
rclone copy -P '/Users/xavier/Projects/Oceanography/data/Color/IOPtics/runs/multi_L23_PANGAEA_v2' 'AIOcean:Claude_PhD_transfer/2026-09-17/IOPtics/runs/multi_L23_PANGAEA_v2'
rclone copy -P '/Users/xavier/Projects/Oceanography/data/Color/IOPtics/leaderboard.parquet' 'AIOcean:Claude_PhD_transfer/2026-09-17/IOPtics/leaderboard.parquet'
rclone copy -P '/Users/xavier/Projects/Oceanography/data/Color/IOPtics/whn_explore' 'AIOcean:Claude_PhD_transfer/2026-09-17/IOPtics/whn_explore'
```

### Pull, on `profx`

```bash
rclone copy -P 'AIOcean:Claude_PhD_transfer/2026-09-17/IOPtics/runs/expb_giop_L23_test20' "$OS_COLOR/IOPtics/runs/expb_giop_L23_test20"
rclone copy -P 'AIOcean:Claude_PhD_transfer/2026-09-17/IOPtics/runs/gloria_turbid_v3' "$OS_COLOR/IOPtics/runs/gloria_turbid_v3"
rclone copy -P 'AIOcean:Claude_PhD_transfer/2026-09-17/IOPtics/runs/multi_L23_PANGAEA_v2' "$OS_COLOR/IOPtics/runs/multi_L23_PANGAEA_v2"
rclone copy -P 'AIOcean:Claude_PhD_transfer/2026-09-17/IOPtics/leaderboard.parquet' "$OS_COLOR/IOPtics/leaderboard.parquet"
rclone copy -P 'AIOcean:Claude_PhD_transfer/2026-09-17/IOPtics/whn_explore' "$OS_COLOR/IOPtics/whn_explore"
```

Then verify with `rclone check` on each pair, and delete the Drive copy once `profx` has it -- Drive is a transport here, not a backup.

## 2. Git history (not Drive)

| repository | local tip | branch | note |
|---|---|---|---|
| `EPFT-UP` | 10b14ec 2026-09-15 | `diatom` | MOANA's spin-off home (A12).  Already installed on profx -- verify the tip matches. |
| `Claude-PhD-Thesis` | d611a28 2026-09-08 | `main` | Thesis LaTeX.  Clone on profx from Overleaf directly; do not send through Drive. |

`EPFT-UP` carries the MOANA work that left IOPtics on 2026-09-13 (A12).  On `profx`, `git fetch --all` in each of IOPtics, PAB, BING, retrieve-or-bust and EPFT-UP is enough; no branch in any of them needs to travel through Drive.

## 3. Already on `profx`, do not re-copy

- The full-L23 MCMC sweep (2026-08-19) and the RT-A outputs -- `profx` produced them.
- The PAB 1.0 production and 2.0 databases.
- All four source repositories and their branches.

