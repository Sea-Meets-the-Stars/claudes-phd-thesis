"""Headline numbers from the finished RT-A sweep (IOPtics ``rt_tests``).

Reads the stage-2 metrics tables that IOPtics wrote under ``$OS_COLOR`` for
the two RT-A arms (L23 X=4 and PANGAEA-97) and prints, per RT variant, the
fit-quality and accuracy columns the qualifying-exam discussion needs, plus
the configured delta-BIC contest.  It is a *peek* for the Q&A of
``claude_prompts/qual_exam_prompts.md``; the numbers of record will be the
ones IOPtics' own report stage (``rt_tests/build_v1.py`` stage 5) publishes.

Run with::

    conda run -n ocean14 python claudes_phd_thesis/scripts/rta_headline.py

Writes ``reports/rta_headline.md``.  Read-only with respect to the sweep.
"""

from __future__ import annotations

import datetime as dt
import os
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve()
OUT = HERE.parents[2] / "reports" / "rta_headline.md"
RUNS = Path(os.environ.get("OS_COLOR", "/home/xavier/Oceanography/data/Color")) / "IOPtics" / "runs"
ARMS = {"L23 (X=4, PACE noise, 3,320 spectra)": "rt_tests_A_l23_v1",
        "PANGAEA-97 (in-situ noise)": "rt_tests_A_pangaea_v1"}
VARIANTS = ["expb_pow_ztt_el", "expb_pow_hyb_el", "expb_pow_hyb_ram",
            "expb_pow_hyb_ramfl", "expb_pow_hyb_ramflcdom"]
ACC = [("a", 440.0), ("a_ph", 440.0), ("a_dg", 440.0), ("bb_p", 555.0), ("bb_p", 670.0)]


def fmt(v, nd=3):
    return "" if pd.isna(v) else f"{v:.{nd}f}"


def qc_table(ms: pd.DataFrame, method: str) -> str:
    rows = ["| variant | n_attempted | frac_ok | frac_poor_fit | frac_out_of_scope | chi2_nu median | rel_misfit median |",
            "|---|---|---|---|---|---|---|"]
    q = ms[(ms.fit_method == method) & (ms.stratum == "all") & (ms.component == "Rrs")]
    for v in VARIANTS:
        r = q[q.algorithm == v]
        if r.empty:
            rows.append(f"| {v} | (no row) |||||| ")
            continue
        r = r.iloc[0]
        rows.append(f"| {v} | {int(r.n_attempted) if pd.notna(r.n_attempted) else ''} | {fmt(r.frac_ok)} | "
                    f"{fmt(r.frac_poor_fit)} | {fmt(r.frac_out_of_scope)} | {fmt(r.chi2_nu_median, 2)} | "
                    f"{fmt(r.rel_misfit_median)} |")
    return "\n".join(rows)


def acc_table(ms: pd.DataFrame, method: str) -> str:
    head = "| variant | " + " | ".join(f"{c}({int(w)}) MAE / bias / cov68" for c, w in ACC) + " |"
    rows = [head, "|" + "---|" * (len(ACC) + 1)]
    q = ms[(ms.fit_method == method) & (ms.stratum == "all")]
    for v in VARIANTS:
        cells = []
        for c, w in ACC:
            r = q[(q.algorithm == v) & (q.component == c) & (q.ref_wave == w)]
            if r.empty:
                cells.append("")
            else:
                r = r.iloc[0]
                cells.append(f"{fmt(r.mae)} / {fmt(r.bias, 3)} / {fmt(r.coverage68, 2)} (n={int(r.n)})")
        rows.append(f"| {v} | " + " | ".join(cells) + " |")
    return "\n".join(rows)


def dbic_table(mp: pd.DataFrame) -> str:
    q = mp[mp.median_dbic.notna() & (mp.stratum == "all")]
    if q.empty:
        return "(no delta-BIC rows)"
    rows = ["| fit | model_a (more complex) | model_b | n | frac favour a | frac favour b | median dBIC |",
            "|---|---|---|---|---|---|---|"]
    for _, r in q.drop_duplicates(["fit_method", "model_a", "model_b"]).iterrows():
        rows.append(f"| {r.fit_method} | {r.model_a} | {r.model_b} | {int(r.n)} | {fmt(r.frac_favor_a)} | "
                    f"{fmt(r.frac_favor_b)} | {fmt(r.median_dbic, 1)} |")
    return "\n".join(rows)


def h2h_table(mp: pd.DataFrame, method: str) -> str:
    q = mp[(mp.fit_method == method) & (mp.stratum == "all") & mp.model_a.notna() & mp.verdict.notna()]
    if q.empty:
        return "(no head-to-head rows)"
    rows = ["| component | ref_wave | model_a | model_b | delta MAE (a - b) | 95% CI | verdict |",
            "|---|---|---|---|---|---|---|"]
    keep = q[q.component.isin(["a", "a_ph", "a_dg", "bb_p"])]
    for _, r in keep.iterrows():
        rows.append(f"| {r.component} | {fmt(r.ref_wave, 0)} | {r.model_a} | {r.model_b} | {fmt(r.delta_mae, 4)} | "
                    f"[{fmt(r.d_lo, 4)}, {fmt(r.d_hi, 4)}] | {r.verdict} |")
    return "\n".join(rows)


def main() -> None:
    out = [f"# RT-A headline numbers (peek)", "",
           f"Generated {dt.datetime.now():%Y-%m-%d %H:%M} by `claudes_phd_thesis/scripts/rta_headline.py` "
           f"from the IOPtics stage-2 metrics under `$OS_COLOR/IOPtics/runs/`.  The IOPtics report stage has "
           f"not run; treat these as provisional.", ""]
    for label, sweep in ARMS.items():
        d = RUNS / sweep
        if not (d / "metrics_scalar.parquet").exists():
            out += [f"## {label}", "", f"(no metrics in {d})", ""]
            continue
        ms = pd.read_parquet(d / "metrics_scalar.parquet")
        mp = pd.read_parquet(d / "metrics_pairwise.parquet")
        out += [f"## {label} — `{sweep}`", ""]
        for method in ("mcmc", "chisq"):
            out += [f"### Fit quality, {method}", "", qc_table(ms, method), "",
                    f"### Accuracy vs truth, {method} (MAE and bias are fractional, log-space; cov68 nominal 0.68)", "",
                    acc_table(ms, method), ""]
        out += ["### Model selection (delta-BIC), configured contest", "", dbic_table(mp), "",
                "### Head-to-head, mcmc (paired bootstrap, 10% equivalence floor)", "", h2h_table(mp, "mcmc"), ""]
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(out))
    print("\n".join(out))
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
