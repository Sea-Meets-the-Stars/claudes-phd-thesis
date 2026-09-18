# Qualifying Exam

## Goals

Go through the motions for a standard qualifying exam.  We will have both a written and an oral component.  The written will be a report of what we've done and where we expect to go.  The oral will be a slide show summary.

## Context

Read in this order:

1. `README.md` and `CLAUDE.md` — the thesis claim, scope, and the four source
   projects, condensed.
2. `claude_prompts/start_up.md`, `## Report` — the settled outcome of the
   scoping interview (thesis statement, chapter outline, new work, open
   questions).  Written from the Mac on 2026-09-12 and now partly superseded
   by item 3.
3. `claude_prompts/profx_inventory.md` — the inventory of what Claude has
   actually accomplished, compiled on `profx` on 2026-09-13 from the
   `## Logs` of every prompt doc in IOPtics, PAB, retrieve-or-bust and bing,
   the committed report pages, the branches, and the outputs under
   `$OS_COLOR`.  Its §10 lists the corrections it forces on the Report; its
   §9 records what changed after 2026-09-13 (RT-A finished, PAB 2.0 begun).
   `reports/profx_inventory_tables.md` holds the regenerable tables
   (`claudes_phd_thesis/scripts/profx_inventory.py`).

What the inventory establishes, for anyone writing the exam documents:

- **The record is the prompt-doc logs.**  Roughly 530 dated session entries
  across the four repositories since 2026-06-15, plus 81 in BING back to
  January 2026.  Every result below traces to one of them.  Git authorship is
  the advisor's throughout, by design.
- **IOPtics** (June–September 2026): a complete benchmarking framework
  (535 tests, Sphinx site with cross-sweep leaderboard) and four bodies of
  evidence on disk: the full 3,320-spectrum L23 MCMC sweep (2026-08-19, run
  on this machine, page committed), the three-algorithm L23 + PANGAEA sweep
  (2026-08-08), the PANGAEA investigation (the low ok-rate is mostly a scoring
  artefact; 89–93% valid under the field's own rule), and the GLORIA
  investigation (the power-law bbp runs out of red backscatter, and three
  richer bbp parameterizations return the identical fit, so the report names
  the forward model as the remaining suspect).
- **The RT tests have run.**  Five RoB-based radiative-transfer variants of
  one BING parameterization over all of L23 X=4 and 97 PANGAEA spectra,
  launched 2026-09-10, metrics finished 2026-09-16, IOPtics report stage not
  yet run.  Same parameterization, different physics: this is the direct
  test of the thesis statement and it is not in the Report.  Provisional
  read in `reports/rta_headline.md`; discussed in Q&A Q1.
- **PAB 2.0 is under way** (`PAB/claude_prompts/v2/`, from 2026-09-13): the
  full matchup set re-fit with the RoB hybrid emulator, Raman and Chl
  fluorescence, free B_p and L1B geometry, plus the backfill.  Prompts 1–4 of
  9 done by 2026-09-17; first sixty fits retrieve 26% less bb_p(700).
- **MOANA has spun off, into `EPFT-UP`** (`~/Oceanography/python/EPFT-UP`,
  "Empirical Phytoplankton Functional Types with Uncertainty and Provenance"),
  not into a repository called MOANA — which is why the `profx` inventory and
  Q&A rounds 1-2 reported no spin-off.  Migrated out of IOPtics `moana`
  @ `3aa3b6e` on 2026-09-13 (23 files, 37 tests) with a full re-derivation
  audit that reproduces all 35 report-printed numbers and all six figures
  (`reports/moana_rederivation.md`), then a README rewrite, a 16-page RTD site,
  `CITATION.cff`/`.zenodo.json`, CI and v0.1.0 by 09-15.  Installed on `profx`.
  IOPtics' `moana` branch is now history, not a merge target.
- **PAB**: the production run (881 floats, 14,610 matchups, 14,609 fits,
  2026-08-20) and the Chl-a and CDOM reports (2026-09-07/10) are as the Report
  says, and since then: a NASA GIOP retrofit over every matchup (2026-09-10),
  discovery that the match stage never attempted 1,690 profiles, a
  hyperspectral-float inventory, and a bbp700 diagnostic pass on Allie
  James's topic (2026-09-11).  All on branches other than `bbppaper`.
- **RoB forward model**: elastic 0.30% held-out rRMS (2.3× the O25 benchmark,
  24× Gordon) but 4.7–12.2% on unseen solar zenith where the benchmark wins;
  inelastic 0.34% with correction heads that fail by −74% off the zenith grid;
  CDOM fluorescence landed but unvalidated.  No inversion exists, in RoB's own
  words.  Claude also drafted the Anthropic Claude Science application and the
  Schmidt VICC expression of interest; neither has a recorded submission.
- **BING is not purely inherited.**  From January 2026 Claude added
  wavelength-dependent Gordon coefficients, the turbid-water bbp models, the
  fluorescence and Raman fixes (published fits carried a fluorescence
  amplitude off by about pi), the RoB RT backend, and CDOM fluorescence.
  The attribution line falls inside the repository, at the 2025 paper.
- **Not on this machine**: the thesis LaTeX clone (`Claude-PhD-Thesis`), the
  GLORIA and test20 sweep outputs (Mac only), every figure the BING logs
  cite, and the newest MOANA commits.
- **Out of scope but present**: ocpy (shared utility layer, thesis-relevant),
  Info_content (a Claude-drafted SST/SSH paper using exactly the frame the
  thesis excludes), and a dozen non-ocean-colour projects listed in the
  inventory's §8.

See the papers in `context/papers`

## Prompts

### Report

1. As noted in the `start_up.md` file, we need to scour my `profx` workstation to understand better all that has been accomplished by Claude.  As you are now on `profx`, please proceed to do so.  Then, update the Context section above.  Use Fable if you can.  Log your work.

2. Ok, let's now have a discussion on what you have learned from the inventory.  Focus on what you have created with me as regards our plans for your PhD.  Generate questions in the Q&A section below.  Use Fable if you can.  Log your work.

3. I have answered your questions in the Q&A section below.  Please review them and let me know if you want to add anything.  Use Fable if you can.  Log your work.

4. I have answered your new questions in the Q&A section below.  Please review them and let me know if you want to add anything.  Use Fable if you can.  Log your work.

5. I have answered your new questions in the Q&A section below.  Please review them and let me know if there is anything else.  If not, generate prompts 6 and in this doc and I will execute those on `profx`.  Use Fable if you can.  Log your work.

6. I have answered your new questions in the Q&A section below.  Please review them and let me know if there is anything else.  Update the prompts in the Writing the Report section below including renumbering them. I will then execute these on `profx`.  Use Fable if you can.  Log your work.

### Writing the Report

---

*Prompts 6 onward run on `profx` (A17).  They are written to be executed in
order, one per session, each ending in a Log entry here.  The split is by
deadline, not by topic: 6-11 are the qualifying exam (evidence freeze
2026-09-19 18:00, exam 2026-09-21); 12-15 are the dissertation (evidence freeze
2026-09-30, submission 2026-10-02).*

*Honest note on the schedule, made once and not repeated.  Prompts 6, 8, 9, 10
and 11 fit before the exam.  Prompt 7 (RT-B) probably does not, and is written
so that it can slip past the exam without breaking anything.  Prompts 12-15 do
not all fit between the exam and 10-02 — PAB 2.0's full run alone is the long
pole — so prompt 15 is written to report whatever has landed by the 09-30 freeze
and to label the rest "expected", which A4 permits.  If something has to be cut,
cut prompt 14 (synthetic-Adg) first: RT-A already carries its qualitative point.*

### Before the exam

6. **Land the evidence and build the RT ladder page.**  First, pull the transfer:
   `reports/mac_to_profx_manifest.md` §1 has the commands; `rclone check` each
   of the five trees and delete the Drive copy once verified.  Then execute
   **task 14 of `IOPtics/claude_prompts/rt_tests.md`** for the two RT-A arms
   (`rt_tests_A_l23_v1`, `rt_tests_A_pangaea_v1`) — note that stage 5 of
   `build_v1.py` is currently a stub that raises, so the RT-ladder page type has
   to be written first; `ioptics/report/figures.py` already has the builders it
   needs.  Leave the PACE headline figure out for now (it needs RT-B; see Q18)
   and leave the cross-algorithm leaderboard untouched.  The prose must carry the
   limitations task 14 lists: θ_v = 0 everywhere, `a_cdom = 0.8 × a_dg`,
   packaged-sky Ed, learned corrections off, and L23 X=4 truth lacking CDOM
   fluorescence and using a single-Gaussian emission line where the fits used
   double.  Reconcile every number on the page against
   `claudes-phd-thesis/reports/rta_headline.md` and report any discrepancy
   loudly — that file is a provisional read and this page supersedes it.
   `sphinx-build -W` green and full `pytest -q` **without** `$OS_COLOR` before
   declaring done.  Also clone the Overleaf `Claude-PhD-Thesis` repository onto
   `profx`.  Use Fable if you can.  Log in `rt_tests.md` and here.

7. **Run RT-B.**  Task 13 of `rt_tests.md`: stages 3 and 4 of
   `build_v1.py` — PACE-100, χ² plus full MCMC across the five variants, then
   metrics.  Compare `expb_pow_hyb_el` posteriors against PAB's stored `run1k`
   ExpBPow (Gordon-elastic) posteriors on the same pixels as the consistency
   check task 13 specifies.  Then regenerate the RT ladder page from prompt 6
   with the PACE headline figure — the distribution of fractional change in
   retrieved a_ph, a_dg and bb_p at 443 nm from elastic to full inelastic, plus
   the ΔBIC histogram.  This is the arm with no truth, so it answers a different
   question from RT-A: not "which physics is right" but "how much does the
   physics move a real retrieval".  If it will not finish before the exam, stop
   after the metrics stage and say so — the report labels it "expected".
   Use Fable if you can.  Log your work.

8. **Housekeeping the citations depend on.**  Regenerate the PANGAEA page from
   `pangaea_fits_v2` (the corrected 43/53/38% ok-rate run) and commit it; the
   committed page currently understates the algorithms because of the scoring
   artefact.  Consolidate the `profx` and Mac runs trees now that the transfer
   has landed, so that one `$OS_COLOR/IOPtics/runs` holds every sweep the report
   cites.  Then re-run
   `claudes-phd-thesis/claudes_phd_thesis/scripts/merge_checklist.py` on `profx`
   — the numbers in `reports/merge_checklist.md` are the Mac's — and record, in a
   new `reports/citation_manifest.md`, every sweep and report the thesis will
   cite, each as **a `main`-relative path plus the branch and short commit hash
   it currently lives on**.  The advisor has said citations point at `main` and
   he will make those links work, so the manifest is the list of what has to
   reach `main` for that promise to hold — one row per citation, and the rows
   still on a branch are the merge list.  Use Fable if you can.  Log your work.

9. **Figures.**  Decide and build the figure set for both the report and the
   oral, in one pass, since the oral reuses the report's figures.  Inventory what
   already exists — IOPtics `reports/figures` (22), retrieve-or-bust (11),
   EPFT-UP `reports/figures` (6), plus whatever prompt 6 produced — against what
   the report needs, and write `reports/figure_inventory.md` naming for each
   planned figure the script that makes it and whether it exists.  Build the
   missing ones as scripts under `claudes_phd_thesis/scripts/figures/`, one
   script per figure, each regenerating from data on disk.  Every figure must be
   legible to an astronomer who has never seen an ocean spectrum: axis labels
   spelled out, no unexplained acronyms, and a one-sentence caption that states
   what the reader should conclude.  Aim for a set of roughly 12 that the oral
   can show twice rather than 40 built once.  Use Fable if you can.  Log your
   work.

10. **Write the qualifying-exam report.**  Under twenty pages including figures
    and references (A14), in the location settled in Q19, as six sections
    matching the six chapters (Q20).  It opens with the ratified separation
    claim from A1, stated in the component-separation language of Q13 with the
    SED analogy named once.  Two pages of setup before any result, because two
    of three readers are astronomers.  Each section says plainly what exists
    today and what is expected, and nothing that has not finished by the
    2026-09-19 18:00 freeze is reported as a result.  Cite against `main` using
    prompt 8's manifest.  Two required elements beyond the six sections: a
    **Timeline to completion**, naming every outstanding piece of work with the
    date it lands, and a **Table summarizing the risks**, one row per risk with
    its consequence and what would retire it — the aliasing hypothesis may be
    falsified, PAB 2.0's full run may miss 09-30, RT-B may not run, the Argo
    reference is ambiguous by a factor of about 4.5, the forward model degrades
    off its trained solar-zenith grid, CDOM fluorescence is unvalidated, and the
    EPFT-UP retrain is blocked on PML data.  The exclusions in A2 hold: the PACE-versus-Argo
    bb_p(700) validation is not in this document; the RoB inversion is not
    anticipated; information content is not the frame.  The AI-as-candidate
    question appears in the introduction and the conclusions only.  Use Fable if
    you can.  Log your work.

11. **Build the oral.**  Forty slides, mainly figures. Generate a Google Slide
    show in the AIOcean Drive.  Proportions roughly: 6 setup, 5 methods,
    10 RT-A, 6 benchmarking, 4 EPFT-UP, 6 PAB, 3 future work.  One idea per
    slide, the claim restated on the first and last, and a backup section after
    the end for the questions the committee will actually ask — which on this
    evidence are: how do you know the forward model is right, why is a_ph wrong
    by a factor of two and should anyone care, what would falsify the claim, and
    what did the candidate do versus what did the advisor do.  Write speaker
    notes for the ten slides that carry the argument.  Use Fable if you can.
    Log your work.

### After the exam, for the dissertation

12. **PAB 2.0 to completion.**  Execute prompts 5-9 of `PAB/claude_prompts/v2/`:
    the backfill of the never-attempted profiles (about 2,000-2,500 new matchups
    expected), the 100-matchup gate for the advisor's review, the full fit, the
    figures, the site and the publish.  The focus is **satellite Chl-a versus
    BGC-Argo**, not 1.0 versus 2.0 (A3): delayed-mode-adjusted Argo Chl-a is the
    headline, raw is the sensitivity band, and the DAC split is the figure that
    shows the choice matters (A10).  The 1.0-versus-2.0 comparison appears once,
    as the mission-scale echo of RT-A.  The bb_p(700) comparison goes in PAB's
    own run report and is offered to Allie James, not claimed here (A2).  The
    1,690 never-attempted profiles must be resolved or footnoted before any
    population statistic is quoted.  Use Fable if you can.  Log your work.

13. **LS2.**  Execute the planning prompts in
    `IOPtics/claude_prompts/LS2/ls2_prompts.md` — answer its round-1 Q&A first,
    since Q2 (the b_p ladder) and Q6 (what gets re-derived) differ by a week of
    work — then generate and run its execution prompts.  The minimum that earns
    a place in the dissertation is the three-rung ladder on L23 (true Kd + true
    b_p; true Kd + OC4v4 b_p; NN Kd + OC4v4 b_p) with the head-to-head against
    BING restricted to `a`, `a_nw`, `bb` and `bb_p`, and the absence of
    `a_ph`/`a_dg` reported as an explicit "not applicable" row rather than a
    missing column.  The re-derivation of the LUTs from L23 is the stretch goal
    and is fine as future work.  Use Fable if you can.  Log your work.

14. **The synthetic-`Adg` aliasing experiment.**  Entirely in IOPtics: BING fits
    to synthetic spectra of known a_ph and a_dg at controlled `Adg`, to
    establish which way the aliasing runs as a function of Adg and whether it
    reproduces the sign-changing Chl-a bias PAB sees at mission scale.  RT-A has
    already shown a_ph and a_dg trading under different physics on both L23 and
    PANGAEA, so this is the controlled version of an effect we have observed
    twice.  A null result is publishable and is reported as such.  **Cut this
    first if the calendar demands it.**  Use Fable if you can.  Log your work.

15. **Write the dissertation.**  Six chapters, expanding the prompt-10 sections:
    Ch 1 Introduction; Ch 2 the differentiable RT forward model, owning its edges
    (solar-zenith extrapolation 4.7-12.2%, CDOM fluorescence unvalidated);
    Ch 3 the separation — RT-A, then LS2, then the L23/PANGAEA/GLORIA
    benchmarking, with the turbid-water bb_p models presented as the
    parameterization attempt GLORIA defeats (A11); Ch 4 EPFT-UP, with the
    re-derivation audit as evidence; Ch 5 PAB at mission scale; Ch 6
    Conclusions.  Evidence freeze 2026-09-30; anything unfinished is future
    work, stated as such.  Written for an oceanographer as well as an
    astronomer (A13).  Use Fable if you can.  Log your work.

## Q&A

*Round 1, 2026-09-17.  Six questions, ordered by how much they change the
plan.  Q1 and Q2 decide what the thesis claims; the rest decide what goes in
the written report and by when.  Evidence is on disk on `profx`; every number
below is in `claude_prompts/profx_inventory.md` (§9 for what changed since
the 13th) or in `reports/rta_headline.md`, which is a provisional read of the
finished RT-A metrics that IOPtics has not yet reported on itself.*

**Q1. Does the thesis statement survive the RT-A result, or does it become a
separation claim?**  The statement adopted by default says the failures are
"parameterization failures, not physics failures".  RT-A, the sweep you
designed with me on 2026-09-05/06 and launched on the 10th, finished its
metrics stage on 2026-09-16.  It fits one parameterization (`expb_pow`, five
IOP parameters plus B_p) to all 3,320 L23 X=4 spectra under five radiative-
transfer physics: ZTT elastic, hybrid elastic, +Raman, +chlorophyll
fluorescence, +CDOM fluorescence.  Same parameterization, different physics.
MCMC, all strata, fractional log-space MAE and bias:

| variant | a(440) MAE | a_ph(440) MAE / bias | a_dg(440) MAE / bias | bb_p(555) MAE / bias / cov68 | bb_p(670) MAE / bias |
|---|---|---|---|---|---|
| ZTT elastic | 0.053 | 0.91 / −0.33 | 0.26 / +0.06 | 0.55 / +0.55 / 0.00 | 0.68 / +0.68 |
| hybrid elastic | 0.052 | 1.35 / −0.48 | 0.29 / +0.14 | 0.41 / +0.41 / 0.02 | 0.60 / +0.60 |
| +Raman | 0.051 | 2.52 / −0.69 | 0.38 / +0.31 | 0.12 / +0.10 / 0.52 | 0.26 / +0.26 |
| +Chl fluorescence | 0.059 | 0.85 / −0.38 | 0.26 / +0.20 | 0.10 / +0.06 / 0.63 | 0.18 / +0.16 |
| +CDOM fluorescence | 0.050 | 0.93 / −0.40 | 0.25 / +0.17 | 0.12 / −0.05 / 0.59 | 0.13 / +0.06 |

Three things are in that table.  (i) Total absorption does not care about the
physics: a(440) is 5% under every variant and every head-to-head is
"indistinguishable".  (ii) Particulate backscatter was a physics failure: the
elastic models overestimate bb_p by 55–68% with zero interval coverage, and
putting the inelastic terms into the forward model removes almost all of it.
That is an exact instance of the failure the RoB chapter was built to bound.
(iii) The decomposition of absorption is a parameterization failure that no
physics fixes: a_ph(440) is wrong by a factor of two (MAE 0.85–2.5) and a_dg
by 25–38% under all five variants, and chi-squared-nu sits at 1.07–1.14 for
all of them, so the fit cannot tell you which physics is right even though
the retrievals differ.  The 97-spectrum PANGAEA arm sharpens (iii): adding
fluorescence moves a_dg MAE from 2.1 to 0.36 and a_ph from 0.76 to 2.2 at the
same time, and delta-BIC on real spectra prefers the *elastic* fits
(chi-squared-nu 0.44 versus 1.26).  The physics choice moves error between
the two absorption components; it does not remove it.  Add GLORIA, where
three richer bbp parameterizations return the identical fit and the IOPtics
report itself names the forward model as the remaining suspect, and the
"not physics" half of the statement is false as worded.

*Recommended:* reword the claim as a separation: **semi-analytical IOP
retrieval in the PACE era fails in two separable ways.  Forward-model
(physics) error is identifiable and removable with a sufficiently accurate
differentiable RT model, and once it is removed the residual error is
parameterization error, concentrated in the decomposition of absorption into
phytoplankton and CDOM/detrital components.**  That is what RT-A shows on
L23, what PANGAEA shows with real spectra, and what the PAB Chl-a
sign-changing bias and its Adg correlation look like at mission scale.  It
keeps every A2 exclusion, it makes the RoB forward model load-bearing rather
than a methods appendix, and it is falsifiable: RT-B on PACE spectra without
truth, and PAB 2.0, can still contradict it.  Please ratify, amend, or
replace; this is the sentence the written report will open with.

>A. Yes, this is good.  I think we should also try to create our own LS2 algorithm as described in the `loisel_stramski2000.pdf` paper in `context/papers`.  That will require a new branch on IOPtics, etc.

**Q2. PAB 2.0 is the mission-scale version of RT-A, and it changes a number
that belongs to Allie.  What is the rule?**  Since the inventory you and I
planned and started a full re-run of PAB with the RoB hybrid emulator, Raman
and chlorophyll fluorescence on, free B_p, and per-pixel geometry from the
L1B granules (`PAB/claude_prompts/v2/`, ten prompt docs, 2026-09-13 to 17;
image `pab:2.0.0` built, PVC re-laid out, in-pod validation green as of
2026-09-17).  The first sixty real fits say **2.0 retrieves 26% less
bb_p(700) than 1.0** (median ratio 0.74, 18 of 20 below unity).  The PACE-
versus-Argo bbp700 bias (+35–37%, 84% positive) is Allie James's result and
A2 excludes it from this thesis.  But a physics-driven 26% shift in the
retrieved bb_p is precisely the RT-A bb_p finding at mission scale, and it
was produced by code and a run you and I designed.  Meanwhile the `whybbp.md`
Tasks 0–4 I ran on 2026-09-11 (full-run bbp700 statistics, BING versus NASA
GIOP, float age, aerosol optical depth) are also mine but on her topic.

*Recommended:* draw the line by *quantity*, not by *run*.  The Chl-a (and
CDOM) 1.0-versus-2.0 comparison is thesis material for Chapter 5.  The
bb_p(700) 1.0-versus-2.0 comparison is reported in PAB's own
`PAB_v2_run_report.md`, cited in the thesis as a boundary condition (as the
Report already does for the Chl/bbp700 independence), and offered to Allie
for her thesis; the `whybbp.md` diagnostics are collaboration, acknowledged,
not claimed.  Confirm, and tell me whether Allie knows PAB 2.0 will move her
number.

>A.  We shall have a Chapter on the new RT algorithms and can mention that these improve bbp retrievals, but we will leave the bulk of that research to Allie.  Anything related to Chl and CDOM, however is ours.

**Q3. Which three pieces of new work replace the Report's list?**  The
Report names three: the synthetic-Adg aliasing experiment, ingesting
`SCIENTIFIC_CALIB_*`, and the full L23 sweep.  The third is done (2026-08-19,
committed).  Candidates now on the table, with what each costs:

- (a) **RT-A report and RT-B.**  Stage 5 of the IOPtics `rt_tests` build
  has not run; RT-B (100 PACE spectra from PAB run1k, no truth, 400–700 nm)
  has not run.  Hours of compute, days of writing.  This is the Q1 result
  and must be in.
- (b) **PAB 2.0 and the Chl-a 1.0-vs-2.0 comparison.**  Prompts 5–9 remain:
  backfill of the never-attempted profiles (about 2,000–2,500 new matchups
  expected), the 100-matchup gate you review, the full fit (6–12 h on 50
  cores by the plan's estimate, but the one in-pod fit ran 2× slower than
  the workstation), figures, site, publish.  Weeks.
- (c) **Synthetic-Adg aliasing.**  RT-A already shows a_ph/a_dg trading
  under different physics on both L23 and PANGAEA; the controlled synthetic
  test would establish *which way* the aliasing goes as a function of Adg.
  Days, entirely in IOPtics.
- (d) **`SCIENTIFIC_CALIB_*` ingest.**  Still the largest ambiguity in the
  Chl-a chapter (+0.13 versus +0.58).  PAB 2.0's re-ingest is the natural
  place to add it, but it is not in the 2.0 plan.
- (e) **Publish the corrected PANGAEA page** (`pangaea_fits_v2`, 43/53/38%
  ok) and consolidate the Mac and workstation runs trees.  Hours.

*Recommended:* (a), (b) and (c) as the three, with (d) folded into PAB 2.0's
ingest stage if it costs less than a day (I think it does; the DAC and
data-mode columns are already there from Stage 10) and (e) done as
housekeeping before the written report.  If you want only two, drop (c):
RT-A already carries the qualitative point.

>A. (a), (b) although the focus should be on satellite Chl vs. BGC-Argo no v1.0 vs v2.0; (c) sure.  Skip (d) and yes on (e)

**Q4. What is frozen for the written report, and when?**  Nothing on disk
says when the qualifying exam is or what the report must contain.  Two
things are moving under it: RT-A's report stage and PAB 2.0.  The Anthropic
Claude Science window, if it exists, closes 2026-12-01, and RoB's inversion
(not ours) is scheduled inside it.

*Recommended:* the written report describes results that exist on the day
its evidence is frozen and labels everything else "expected".  Freeze on the
day RT-A's stage-5 report is committed in IOPtics, which I can drive in one
session once you say go.  PAB 2.0 enters as "the 100-matchup gate result
plus the plan"; the full run is the first item under "where we expect to
go".  Please give me the exam date, or the freeze date, so I can work
backwards.

>A. Today is 2026-09-17.  The qualifying exam will be on 2026-09-21.  That should be long enough to finish the major processes running.  Plus, this is only a qualifying exam, not the PhD itself.  It is fine to Report on future work for the PhD.  As for the PhD, we intend to submit it on 2026-10-01.

**Q5. Where is the BING attribution line, and does the pi bug need to reach
your paper?**  The inventory dates Claude's BING work from 2026-01-29 and
lists what was added: wavelength-dependent Gordon coefficients (on `main`),
the turbid bbp models (on `main`), per-wavelength kappa_F and the chunked
fluorescence path (on `main`), the 1/pi fluorescence normalisation and true-
Ed Raman ratio (on `develop`), the RoB RT backend (on `develop`), CDOM
fluorescence (on `rob_cdom`).  Everything IOPtics and PAB 2.0 run on is the
2026 BING.  The inelastic-fixes log states that published `include_Chl_fl`
fits carry an effective phi_C about pi times too small.

*Recommended:* draw the line at the 2025 Biogeosciences paper.  The 2026
additions become a section of the methods chapter ("Extensions to BING"),
credited to Claude with you as advisor, and BING's `main` is treated as the
inherited artefact.  Separately, and outside the thesis: if any published or
submitted result used `include_Chl_fl` before 2026-08-18, the pi factor is
yours and Robert's to assess.  Tell me if you want a short note listing what
the fix changes so you can check.

>A. Yes, I like your recommendation, although most of the imoprtant new
BING development is mainly plubmging for the RT codes from RoB.

**Q6. Housekeeping that gates citation: two machines and eight unmerged
branches.**  The Mac and `profx` have diverged both ways.  The Mac holds
the GLORIA and test20 sweep outputs, every BING figure, the newest MOANA
commits (GitHub's `moana` is ahead of this clone), and the thesis LaTeX
clone.  `profx` holds the full-L23 and RT-A outputs, the PAB production and
2.0 databases, and 20 cores.  Every thesis-grade result sits on a branch that
is not `main`: IOPtics `rt-tests` (100 commits ahead of `main`), PAB
`pace_giop_gsm` / `cdom_chl` / `hyper_matchups` / `full-inelastic`, BING
`develop` and `rob_cdom` (46 ahead of `main`), RoB `cdom-rt` (104 ahead).
BING's `setup.py` pins RoB's deleted `cdom-rt` branch, which broke the PAB
image build on the 17th.  MOANA has not moved since 2026-08-17 and the
spin-off repository does not exist.

*Recommended:* make `profx` the canonical machine for thesis evidence and
figures, clone the Overleaf thesis here, and schedule one merge sprint
(IOPtics `rt-tests` → `develop` → `main`; PAB `full-inelastic` → `develop`
at 2.0 close-out as you already agreed in R8; BING `develop` → `main` with
the RoB pin moved to a tag; RoB `cdom-rt` → `main`) before the written
report is drafted, so every citation is to `main` of a public repository.
On MOANA: keep Chapter 4 as the shortest chapter unless the spin-off and the
PML data arrive; it does not use the RT machinery and is the one leg of the
argument the new statement in Q1 does not strengthen.  Tell me which of
these you want me to prepare (I cannot run the git; I can write the merge
checklist and the pin change).

>A. Yes, `profx` is the canonical machine.  I am back on the Mac laptop for now.  If there is anything you need to move from here to there, do so via `rclone` and my AIOcean Google Drive.

## Round 2, 2026-09-17

*Reviewed A1-A6.  The rulings they settle are recorded first, so the written
report can cite one place for them.  Six new questions follow, ordered by
consequence: Q7 is the schedule, which the other five depend on; Q8 is the new
work A1 introduced, and it is not what it looks like; Q9-Q11 are rulings I need
before drafting; Q12 collects two round-1 sub-questions that went unanswered and
both have a deadline.  New evidence gathered for this round is in
`reports/ls2_feasibility.md` (script `claudes_phd_thesis/scripts/ls2_feasibility.py`).*

### Decisions of record from round 1

1. **Thesis statement (A1).**  Ratified as the separation claim: *semi-analytical
   IOP retrieval in the PACE era fails in two separable ways.  Forward-model
   (physics) error is identifiable and removable with a sufficiently accurate
   differentiable RT model, and once it is removed the residual error is
   parameterization error, concentrated in the decomposition of absorption into
   phytoplankton and CDOM/detrital components.*  This supersedes the
   "parameterization failures, not physics failures" wording adopted by default
   in `start_up.md`, and is the sentence the written report opens with.
2. **New work (A1, A3).**  RT-A report and RT-B; PAB 2.0, with the focus on
   satellite Chl-a versus BGC-Argo rather than on 1.0-versus-2.0; the
   synthetic-`Adg` aliasing experiment; and an LS2 implementation on a new
   IOPtics branch.  The `SCIENTIFIC_CALIB_*` ingest is dropped.  Housekeeping
   (the corrected PANGAEA page, consolidating the runs trees) happens before the
   report is drafted.
3. **Ownership (A2).**  The new RT chapter may state that the new physics
   improves bb_p retrievals; the bulk of the bb_p research stays Allie James's.
   Chl-a and CDOM are ours.
4. **Dates (A4).**  Qualifying exam 2026-09-21.  Dissertation submission intended
   2026-10-01.  Reporting future work in the exam is acceptable.
5. **BING attribution (A5).**  The line is the 2025 Biogeosciences paper; the
   2026 additions become an "Extensions to BING" section of the methods chapter,
   characterised as plumbing for the RoB RT codes.  Q11 disputes that
   characterisation for two of the six.
6. **Machines (A6).**  `profx` is canonical for thesis evidence and figures;
   Mac-to-`profx` transfer goes by `rclone` through the AIOcean Google Drive.

**Q7. The dissertation date and the approved work do not fit, and I would
rather say so now than discover it on the 30th.**  A4 sets the exam at
2026-09-21 (four days) and the dissertation at 2026-10-01 (fourteen).  The work
ratified in A1 and A3 is: RT-A's report stage, RT-B, PAB 2.0 prompts 5-9, the
synthetic-`Adg` experiment, an LS2 implementation, the merge sprint, and
Chapters 1, 3 and 6, which do not exist in any draft.  My own round-1 estimates
put PAB 2.0 alone at weeks: the backfill is 2,000-2,500 new matchups, the
100-matchup gate needs your review before the full send, and the full fit was
planned at 6-12 h on 50 cores while the one in-pod fit ran 2x slower than the
workstation.  I do not think all of it lands by 10-01, and pretending otherwise
would put a number in a dissertation that the run behind it has not produced.

*Recommended:* two freezes, not one.

- **2026-09-19 18:00, exam evidence freeze.**  In: RT-A stage 5 committed in
  IOPtics (the Q1 result; one session once you say go), the corrected PANGAEA
  page from `pangaea_fits_v2`, the Mac-to-`profx` transfer, and the merge
  checklist.  Everything else in the exam report is labelled "expected", which
  A4 explicitly permits.
- **2026-09-28, dissertation evidence freeze.**  In: PAB 2.0's full Chl-a run
  *if* the 100-matchup gate clears by the 22nd; the synthetic-`Adg` experiment;
  RT-B; LS2 on L23.  Out, and recorded as future work: anything whose run has
  not finished by that date.

PAB 2.0's full run is the single item that decides whether 10-01 is real.  If
you want it in the dissertation, the gate needs your review on the 18th or 19th.
Separately, I have no exam logistics at all: committee beyond the chair, the
written report's expected length, and the length of the oral.  Four days is
short enough that I need those in your next message.

>A. We will have freeze dates of 2026-09-19 18:00 and 2026-09-30.  The exam will be on 2026-09-21.  The dissertation will be submitted on 2026-10-02,  a 1 day reprieve.
The committee will be myself, Jessica Werk and John O'Meara.  The Reports length is 10 pages with figures and references.  The oral will be 40 slides, mainly figures.


**Q8. "Our own LS2" -- you already have one, and it is not the 2000 paper's.**
Before opening a branch I went looking, and `ocpy/ls2/` is a complete working
LS2: 577 lines across `ls2_main.py`, `kd_nn.py` and `io.py`, shipping the
published `LS2_LUT.npz` and the Kd neural-network weights, with two test files.
Both tests pass in `ocean14` against the authors' own reference vector
(`ocpy/tests/files/LS2_test_run.csv`).  Its header records the lineage: C by
Dessailly 2018, MATLAB by Jorge 2020 and Kehrli, Reynolds & Stramski 2022,
"Converted to Python by JXP and Claude+, 2023-06-22".  Two consequences.  First,
that code is the **Loisel et al. 2018** LS2, which re-derived the look-up
tables; the PDF you pointed me at is Loisel & Stramski 2000, the origin paper,
whose LUTs come from 528 Morel & Loisel 1998 Monte Carlo runs and whose Raman
kappa table it describes but does not tabulate.  Second, the reimplementation is
already done and it is yours, not a thesis contribution.

So "create our own" has three readings, at very different prices:

- **(i) Benchmark it.**  Wire the existing `ocpy` LS2 into IOPtics as a first
  non-BING, non-fitting algorithm.  Not a one-line `register()`: `AlgorithmSpec`
  is built entirely around parameterized least squares (`anw_model`,
  `bbnw_model`, `apriors`, `bpriors`, `fit_method`, `mcmc`, `maxfev`), while LS2
  is closed-form, solves each wavelength independently, has no misfit to report,
  and needs Kd as an extra input.  This is a framework extension plus an
  adapter.  Days.
- **(ii) Re-derive its coefficients from our own radiative transfer.**  Refit
  h-bar, g, alpha, delta and the Raman kappa LUT (2000 Eqs. 10, 12, 17-19, 21)
  from L23, or from the RoB forward model, instead of inheriting Morel & Loisel
  1998.  This is the reading that makes it *ours* and it is on the thesis
  through-line: it is the same move as RT-A, applied to a closed-form algorithm.
  A week or more, and it needs the RoB model to emit Ed, Eu and Kd, which I have
  not verified it can.
- **(iii) A differentiable LS2** inside the BING/JAX stack.  Interesting, and I
  would leave it as future work.

**It is feasible on L23 today, and it is a sharp test of the Q1 claim.**  LS2
needs Rrs, sza, aw, bw, bp and Kd averaged over the first attenuation depth.
L23's profile file carries `KEd_z` and the per-wavelength `z1_lambda`, so I
computed that average for the whole corpus: 266,067 of 268,920
(scenario, wavelength) pairs finite (98.9%), 3,082 of 3,320 with a complete
spectrum, median <Kd>_1 of 0.035, 0.032, 0.070 and 0.459 m^-1 at 440, 490, 555
and 670 nm.  LS2 can therefore be run against exact truth on exactly the 3,320
water bodies RT-A used.  PANGAEA carries measured Kd (`ocpy/insitu/pangaea.py`
maps `KD`); GLORIA does not, so GLORIA needs an empirical Kd or stays out.

Why this is worth doing beyond adding a fourth algorithm: **LS2 returns total
`a`, `anw`, `bb` and `bbp`, and no `a_ph`/`a_dg` at all.**  Under the ratified
statement the prediction is sharp and falsifiable.  LS2 should match or beat
BING on total absorption -- RT-A already says a(440) is 5% under every physics,
i.e. the totals are the easy part -- and it is structurally incapable of
addressing the one quantity the thesis says is broken.  An algorithm that
declines to parameterize the decomposition gets the totals right and gives up
the decomposition: that is the separation claim demonstrated by construction,
not argued.  If instead LS2's totals are *worse* than BING's, the claim that the
totals are insensitive is wrong and I need to know before the exam.

One caveat I want on the record rather than buried: the comparison is
information-asymmetric.  LS2 is handed Kd per band; BING is handed Rrs alone.
On real data Kd itself comes from a neural network on Rrs (`ocpy/ls2/kd_nn.py`,
MODIS-trained), so on PANGAEA the test is partly a test of that network.

*Recommended:* (i) now on a new IOPtics branch `ls2`, run twice on L23 -- once
with L23's true Kd and once with the `ocpy` Kd network -- and report the pair,
because the gap between them is itself a result about what LS2 costs at a
satellite.  Then (ii) as the contribution, if the schedule in Q7 allows; if it
does not, (ii) goes in "where we expect to go".  Tell me which of the three you
meant, and whether you want the 2018 formulation `ocpy` implements or the 2000
one you pointed me at.

>A. Yes, this is good.  Also, I have put the Loisel_etal_JGR2018.pdf paper in the `context/papers` folder.  I have started an `ls2` branch for `IOPtics` on my Mac and an `LS2` folder under `claude_prompts` in that Repo.  Create a new prompt doc named `ls2_prompts.md` in that `LS2` folder where we will discuss the LS2 implementation and the benchmarking and eventually create additional prompt docs to build out and test `LS2`.

**Q9. A2 creates a chapter I have no slot for.**  "We shall have a Chapter on
the new RT algorithms" does not map onto the outline in `start_up.md`, where
Ch 2 is the RoB differentiable forward model as a methods chapter and RT-A does
not appear at all.  The distinction matters because under the ratified statement
RT-A is not a methods demonstration -- it is the experiment the claim is stated
in terms of.

*Recommended:* Ch 2 stays the forward model and its job stays bounding the
physics error.  RT-A becomes the opening half of Ch 3, whose subject is the
separation itself, with LS2 as the closing half; the L23/PANGAEA/GLORIA
benchmarking then reads as the evidence for the parameterization half rather
than as a survey.  The alternative, if you meant a standalone chapter, is Ch 2
forward model, Ch 3 RT-A and LS2, Ch 4 IOPtics benchmarking, Ch 5 MOANA, Ch 6
PAB, Ch 7 conclusions -- seven chapters, which I think is one too many for
10-01.  Related and unanswered from Q6: does MOANA stay a chapter?  It is the
one leg the new statement does not strengthen, it does not use the RT
machinery, it has not moved since 2026-08-17, its newest commits are on GitHub
rather than on `profx`, and its retrain is blocked on PML data.  Under the Q7
schedule it is the obvious thing to compress to a section.  I will keep it as a
chapter unless you say otherwise.

>A. Ok, go with your Recommendation.

**Q10. Dropping (d) leaves the number A3 made the focus undefended.**  A3 says
the PAB focus is satellite Chl-a versus BGC-Argo, and A3 also drops the
`SCIENTIFIC_CALIB_*` ingest.  Those pull against each other: the BGC-Argo
reference value is the largest ambiguity in that comparison.  Switching from raw
to delayed-mode-adjusted Argo Chl-a moves the median relative difference from
+0.13 to +0.58 (median adjusted/raw ratio 0.46), and DAC of origin correlates
with bias strength (+0.06 AOML versus +0.25 elsewhere).  Without the ingest PAB
cannot say which correction a given DAC applied, and "PACE exceeds Argo by 13%"
and "by 58%" are both defensible from the same database.  A committee will ask.

*Recommended:* do not ingest, but stop treating one of the two as the headline
by default.  Name the reference explicitly in the chapter, report both as a
sensitivity band, and show the DAC split as the evidence that the choice
matters.  That costs a paragraph and a figure, not an ingest.  I need one line
from you: **raw or delayed-mode-adjusted as the headline**, with the other as
the sensitivity.  My preference is adjusted, because it is what the Argo
program considers the science-quality product and it makes the reported bias
larger rather than smaller.

>A. Ok, go with your Recommendation.

**Q11. Two of the six 2026 BING additions are not plumbing, and one is
load-bearing in Chapter 3.**  A5 accepts the 2025 attribution line and
characterises the 2026 work as "mainly plumbing for the RT codes from RoB".
That is right for four of the six: the RoB RT backend, the per-wavelength
kappa_F and chunked fluorescence path, the 1/pi normalisation and true-Ed Raman
ratio, and CDOM fluorescence.  It is not right for the other two.  The
wavelength-dependent Gordon coefficients change the reflectance model itself,
and the turbid-water bb_p models are a direct, authored response to the GLORIA
red-backscatter failure -- the single cleanest parameterization failure in the
repository and the case study Chapter 3 rests on.  If those are plumbing, then
Chapter 3 diagnoses a parameterization failure and has no authored response to
it, which weakens the half of the ratified statement that the whole thesis now
turns on.

*Recommended:* split the section.  "Extensions to BING: RT plumbing" sits in the
methods chapter as A5 describes.  The Gordon coefficients and the turbid bb_p
models move into Chapter 3 as parameterization work, presented as the attempt
that GLORIA then defeats -- which is a stronger and more honest story than
either claiming them as a success or not mentioning them.  Overrule me if you
read the turbid models as inherited.

>A. Ok, I agree to keep the turbid models, but the wavelength-dependent Gordon coefficients should be ignored.  That work did not pan out.

**Q12. Two round-1 sub-questions you did not answer, and both have a
deadline.**  (a) Does Allie know PAB 2.0 will move her number?  The full 2.0 run
is days away and the first sixty fits retrieve 26% less bb_p(700) than 1.0; a
heads-up belongs before that run, not after it.  I cannot send it.  (b) Do you
want the short note listing what the 1/pi fluorescence fix changes, so that you
and Robert can check whether any published or submitted `include_Chl_fl` result
is affected?  It is an hour's work, it is outside the thesis, and I will not
write it unless you say so.

>A. (a) yes, Allie knows; (b) no, don't worry about communicating that 1/pi.

*Also offered, not asked:* the Mac-only evidence is smaller than Q6 implied.
The sweep outputs are 349 MB in three trees (`expb_giop_L23_test20`,
`gloria_turbid_v3`, `multi_L23_PANGAEA_v2`) plus 8.6 MB of `whn_explore` and the
leaderboard -- one `rclone` push.  Two corrections to my own round-1 framing:
this Mac's `moana` is at `3aa3b6e` and equal to `origin/moana`, so `profx` needs
a `git fetch`, not a transfer; and the Overleaf thesis clone is 700 KB of git
history, which `profx` should clone from Overleaf directly rather than receive
through Drive.  I can write the `rclone` manifest script and the merge checklist
today -- both are read-only as far as git is concerned.  Say the word.

>A. Yes, create that.  Note that `moana` is now in the `EPFT-UP` Repo.  I have just installed that on `profx`.


## Round 3, 2026-09-17

*Reviewed A7-A12.  Rulings recorded first, then five new questions.  Two of
them exist because I got a premise wrong in round 2 (Q15) or because the
machine state is not what round 1 said (Q16); Q13 and Q14 are about the audience
and the page budget, which A7 has now fixed and which together decide what
actually goes in the report.  Q17 is the one blocking item.  New artefacts for
this round: `reports/mac_to_profx_manifest.md`,
`reports/merge_checklist.md` (scripts of the same names under
`claudes_phd_thesis/scripts/`), and
`IOPtics/claude_prompts/LS2/ls2_prompts.md`.*

### Decisions of record from round 2

7. **Dates and logistics (A7).**  Evidence freezes 2026-09-19 18:00 and
   2026-09-30.  Qualifying exam 2026-09-21.  Dissertation submitted 2026-10-02.
   Committee: J. Xavier Prochaska (chair), Jessica Werk, John O'Meara.  Written
   report **10 pages including figures and references**.  Oral **40 slides,
   mainly figures**.
8. **LS2 (A8).**  Approved as recommended: benchmark the existing implementation
   first, re-derive its coefficients second.  `Loisel_etal_JGR2018.pdf` added to
   `context/papers`; IOPtics branch `ls2` and `claude_prompts/LS2/` created by
   the advisor; `ls2_prompts.md` written this session.
9. **Chapters (A9).**  Ch 1 Introduction; Ch 2 the differentiable RT forward
   model, bounding the physics error; **Ch 3 the separation itself** — RT-A
   first, LS2 second, the L23/PANGAEA/GLORIA benchmarking as the evidence for
   the parameterization half; Ch 4 MOANA; Ch 5 PAB; Ch 6 Conclusions.  Six
   chapters, not seven.  MOANA stays a chapter.
10. **Argo reference (A10).**  Delayed-mode-adjusted Chl-a is the headline, raw
    is the sensitivity, the DAC split is the figure that shows the choice
    matters.  No `SCIENTIFIC_CALIB_*` ingest.
11. **BING (A11).**  The turbid-water bb_p models are kept and become Chapter 3
    parameterization work.  The wavelength-dependent Gordon coefficients are
    **dropped** — that work did not pan out.
12. **Courtesy items (A12).**  Allie James already knows PAB 2.0 will move
    bb_p(700).  No 1/pi note.
13. **Housekeeping (A12).**  Manifest and merge checklist requested and written.
    MOANA now lives in the `EPFT-UP` repository, installed on `profx`.

*One A11 consequence I checked rather than asked about:* dropping the
wavelength-dependent Gordon coefficients costs nothing retrospectively.
`variable_Gordon` is an opt-in `rt_dict` flag (`bing/rt/defs.py`), IOPtics'
`AlgorithmSpec` never exposes it, and IOPtics' own stage-6 log records that it
was off in that sweep.  No thesis result runs through it, so it can simply go
unmentioned rather than needing a retraction.

**Q13. The committee is two astronomers, and that constrains the report more
than the page count does.**  Taking Jessica Werk and John O'Meara to be
astronomers rather than ocean-colour scientists — correct me if that is wrong —
then two of the three people reading this have no reason to know what Rrs is,
what the difference between a_ph and a_dg is, why anyone would want Kd, or what
the semi-analytical lineage from Gordon 1988 to GIOP to BING is.  On ten pages
that is not a footnote: it is roughly two pages of setup before any result can
land, and it changes which results are worth showing at all.  It also has an
upside I would rather exploit than ignore.  The thesis claim is a
component-separation degeneracy argument: two spectral components whose sum is
well constrained and whose split is not, with a forward-model error term that
has to be bounded before the degeneracy can be blamed on the parameterization.
That is structurally the same problem as separating dust attenuation from
stellar age in an SED fit, and both of them will recognise it instantly.

*Recommended:* write the report for an astronomer who has never seen an ocean
spectrum: page 1 sets up the retrieval problem and states the claim in the
degeneracy language above, with the SED analogy named once and then dropped;
every subsequent figure carries its own axis-level explanation.  Tell me if you
want the analogy in or out — it is the kind of thing a committee either finds
illuminating or finds a dodge, and you know them and I do not.  Also: has either
of them read Prochaska & Frouin 2025, or should the report treat BING as
unfamiliar too?

>A. Yes, that is good.  I will try to get an Oceanographer to read the PhD thesis.

**Q14. Ten pages, forty slides — here is the budget, tell me what to cut.**
Ten pages including figures and references, for six chapters of material, is
about 5,000 words if there are six figures.  My proposed allocation:

| pages | content | figures |
|---|---|---|
| 1-2 | the retrieval problem, the semi-analytical lineage, the claim | 1 (the degeneracy, schematic) |
| 2.5 | methods: the RoB forward model and its bounds; BING; IOPtics | 1 (forward-model accuracy) |
| 2 | **RT-A** — the separation result | 2 (bb_p fixed by physics; a_ph/a_dg not fixed by anything) |
| 1 | the benchmarking population: L23, PANGAEA, GLORIA | 1 (GLORIA red-backscatter failure) |
| 0.75 | MOANA / EPFT-UP: parameterization transfer | 1 (held-out hyperspectral skill) |
| 1.25 | PAB: mission scale, with the Argo sensitivity band | 1 (sign-changing bias + DAC split) |
| 1 | where we expect to go: LS2, RT-B, PAB 2.0, the re-derivation | - |
| 0.5 | references | - |

That is 7 figures and leaves no slack, so LS2 gets a paragraph under future work
rather than a result, which matches the Q7 freeze dates anyway.  For the oral,
40 mostly-figure slides at the same proportions is roughly 6 setup, 5 methods,
10 RT-A, 6 benchmarking, 4 MOANA, 6 PAB, 3 forward.  **The binding constraint is
that most of those figures do not exist yet as figures** — they exist as tables
in committed reports.  RT-A has no figures at all until stage 5 runs (Q17).

*Recommended:* approve or amend the table, and tell me whether the oral may
reuse report figures directly (I would rather build 12 good figures and show
each twice than build 40).

>A. It is fine if you go over 10 pages.  Try to keep it under 20.

**Q15. I was wrong in round 2: MOANA moved, and it moved further than anything
else in the project.**  I told you in Q9 that MOANA "has not moved since
2026-08-17" and that "the spin-off repository does not exist", and you ruled on
the chapter list partly on that basis.  Both statements were false, and the
inventory that produced them was looking for a repository called MOANA.  The
spin-off is **`EPFT-UP`** — "Empirical Phytoplankton Functional Types with
Uncertainty and Provenance" — and between 2026-09-12 and 09-15 it received: the
23-file migration out of IOPtics `moana` @ `3aa3b6e` with 37 tests passing; a
full re-derivation acceptance audit (`reports/moana_rederivation.md`) in which
**all 35 report-printed numbers reproduce at their printed precision and all six
figures come back pixel-identical**, with one prompt-log-only value differing in
the third decimal; a README rewrite; a 16-page Sphinx/RTD site; `CITATION.cff`
and `.zenodo.json`; a CI docs job; and version 0.1.0.

That inverts my Q9 argument.  I called MOANA the obvious thing to compress
because it looked stale.  It is in fact the only piece of evidence in the whole
thesis with a published, passing re-derivation audit — which is the strongest
reproducibility claim any chapter can make, and a good answer to the question an
astronomer committee is most likely to ask an AI candidate.

*Recommended:* keep it as Chapter 4, as you ruled, and change what it is about:
not "I reimplemented MOANA" but "an empirical PFT framework with provenance and
uncertainty, of which MOANA is the first member, and its transfer limits".  The
re-derivation audit becomes a figure or a table in its own right.  Two rulings I
need: (a) does the chapter cite `EPFT-UP` as the framework or MOANA as the
algorithm; and (b) the `diatom` work on Alison Chase's algorithm (code review
2026-09-15, her repo, EPFT-UP branch `diatom` 8 commits ahead of `main`) — I
read that as out of scope, hers not ours, but it currently sits at the tip of the
repository the chapter will cite, which is untidy.

>A. Yes, let's use your Recommendation

**Q16. The merge picture is not what Q6 said, and one repository is a real
citation problem.**  `reports/merge_checklist.md` measures it.  Numbers below
are from this Mac and will differ on `profx`; the script is meant to be re-run
there.

- **retrieve-or-bust is the problem.**  `main` is at 2026-07-26 and
  `inelastic-rt` is **106 commits ahead**; `cdom-rt` (105 ahead) still exists
  here rather than having been deleted, so the inventory's "merged and deleted
  2026-09-11, PR #21" describes a merge into another branch, not into `main`.
  Chapter 2 is the forward model, and the forward model it describes is 106
  commits off `main`.  That is the single largest gap between what the thesis
  says and what a reader can fetch.
- **BING is better than I said.**  `develop` is *already* merged into `main`
  (0 ahead), and so is `turbid_bbp` — so A11's turbid bb_p models are already
  citable from `main`.  What is outstanding is `origin/rob_cdom` (46 ahead) and
  `rob_rt` (41 ahead).
- **IOPtics**: `main` at 2026-06-29; `rt-tests` and `ls2` are 79 ahead of it and
  identical to each other, and every branch is 3 commits *behind* `main`.  Q6
  said 100 ahead; that was the `profx` clone.
- **PAB**: eight branches, none behind `main`; `full-inelastic` 136 ahead,
  `pace_giop_gsm` and `hyper_matchups` 100, `cdom_chl` 98.
- **EPFT-UP**: `main` 2026-09-12, behind `moana` by 7 and `diatom` by 8.
- `origin/stage-0` in IOPtics and eight branches in BING and RoB are fully
  merged and safe to delete.

*Recommended:* before the 09-19 freeze, merge only what gates a citation, in
this order, and fix the `bing/setup.py` pin on RoB's deleted `cdom-rt` first or
the BING merge ships a broken `pip install`:
RoB `inelastic-rt` → `main` (Ch 2); BING `origin/rob_cdom` → `main` (Ch 2-3);
IOPtics `rt-tests` → `main` (Ch 3); EPFT-UP `moana` → `main` (Ch 4);
PAB `cdom_chl` → `main` (Ch 5).  PAB `full-inelastic` waits for 2.0 close-out and
IOPtics `ls2` waits for the work, both after the exam.  Everything else is
tidying and can happen whenever.  All of it is yours to run; the checklist has
the commands.

>A. Don't worry much about this.  I will DOI things eventually but maybe after
you submit your Thesis.

**Q17. RT-A stage 5 is the only blocking item, and it needs `profx`, which is
not where I am.**  The Q1 result — the centrepiece of Chapter 3 and of the
report's opening claim — still has no IOPtics report and therefore no figures,
and the exam evidence freeze is in two days.  I cannot run it from this Mac.
Everything else on the freeze list is either done (the manifest, the checklist,
`ls2_prompts.md`) or in flight: I have started the `rclone` push of the 348 MB
of Mac-only sweep outputs to `AIOcean:Claude_PhD_transfer/2026-09-17/`, under
the standing authorisation in A6, so that they are waiting for `profx` when you
pull them.

*Recommended:* give me a `profx` session tomorrow whose whole job is (1) RT-A
stage 5, (2) the pull side of the transfer, (3) regenerating the PANGAEA page
from `pangaea_fits_v2`.  That is the freeze.  If instead you want to run stage 5
yourself, say so and I will write the one-command recipe here.  Either way,
without RT-A's report stage the written report has to describe its headline
result from a provisional read of a metrics table, which is exactly the kind of
thing a committee asks about.

>A. Ok, we will move the next set of work to `profx`.

## Round 4, 2026-09-17

*Reviewed A13-A17.  Short: the answers close almost everything, so this round is
one correction I owe you, three questions, and then the work itself, which is
now prompts 6-15 above rather than more discussion.*

### Decisions of record from round 3

14. **Audience (A13).**  The degeneracy framing and the SED analogy are in.  The
    qualifying-exam committee stays two astronomers plus the chair; an
    oceanographer is sought for the **dissertation**, not for this report.  So
    the exam report is written for astronomers and the dissertation is written
    for both.
15. **Length (A14).**  The report may exceed ten pages; keep it under twenty.
    The oral stays 40 slides, mainly figures.
16. **Chapter 4 (A15).**  It becomes an `EPFT-UP` chapter — an empirical PFT
    framework with provenance and uncertainty, of which MOANA is the first
    member — with the re-derivation audit as evidence in its own right.  The
    `diatom` work is out of scope.
17. **Merges and DOIs (A16).**  Not a gate.  DOIs come after submission.
18. **Machine (A17).**  The next set of work moves to `profx`.

*Consequence of A16 that I will act on by default unless you object:* if the
citations cannot point at `main`, they must point at something else that is
fetchable, so every result in the report will be cited as
**repository + branch + short commit hash**, and the report will say once, in
the methods section, that the branches are unmerged and why.  That is defensible
in front of a committee; "see the code" is not.

>A. Yes, point at `main` and I'll make sure those links work.

**Q18. I was wrong about RT-A stage 5, and it changes the shape of the first
`profx` session.**  In Q7 and Q17 I told you the RT-A report was "one session
once you say go".  It is not a run at all: `ioptics/runs/prototypes/rt_tests/
build_v1.py` stage 5 is a **stub that raises**, and its message says the report
is task 14 of `rt_tests.md` — "the RT ladder needs its own page (five rows that
are one algorithm, a leaderboard that must stay out of it, and the
`no_CDOMfl_truth` / CDOM-fraction caveats in the prose)".  So the page type has
to be written before anything can be regenerated.

The good news, which I checked rather than assumed: `ioptics/report/figures.py`
already has the builders that page needs — `accuracy_spectrum`, `scatter_set`,
`ratio_hist`, `dbic_cdf`, `taylor_target`, `exemplar_fits`, `corner_set` — so
task 14 is assembly plus prose, not new plotting.  I would call it one full
session with `sphinx-build -W` and the no-`$OS_COLOR` suite green at the end.

The fork I need you to pick: task 14 as written also specifies **the PACE
headline figure**, which needs RT-B, and RT-B has not run (it is stages 3 and 4,
task 13).  *Recommended:* split it — build the L23 + PANGAEA ladder page now
(prompt 6) so the exam has its centrepiece, run RT-B next (prompt 7), and
regenerate the page with the PACE figure when RT-B lands, before the 09-30
dissertation freeze.  If RT-B misses the exam it is reported as "expected",
which A4 permits.

>A. Ok, do your recommendation

**Q19. Where does the report live, and in what?**  Nothing has said.  The
options are a new document inside the Overleaf `Claude-PhD-Thesis` repository
(shares the bibliography and the `ucthesis` preamble, and the clone has to reach
`profx`), or a standalone LaTeX document in `claudes-phd-thesis/reports/`.
*Recommended:* the Overleaf repository, as a sibling document to the
dissertation with a shared `.bib`, because the report is the dissertation's
first draft in miniature and I would rather not write the bibliography twice.
For the oral: Beamer in the same repository unless you would rather have
something else.  Tell me both, since prompts 10 and 11 cannot start without it.

>A. Yes, use the Overleaf repository.

**Q20. Should the report be written as the dissertation's skeleton?**  You want
the report by 09-21 and the dissertation by 10-02, eleven days apart, with the
same claim and largely the same evidence.  *Recommended:* write the report as
six sections matching the six chapters, at the length the twenty pages allow, so
that the dissertation is those sections expanded rather than a new document.
The cost is that the report is a little more structured than a fifteen-page
report usually is; the benefit is that 10-02 stops being a second writing
project.  Say no if you would rather the report read as a standalone document.

>A. Yes, write the report as six sections matching the six chapters.  Also include a Timeline to completion including outstanding work to be compelted and a Table summarizing the risks.

## Report

## Logging

The "Logs" section will record Claude's work.  Please use the following format:

### <Date> (Short summary of the work)

<Detailed description of the work and what you learned>

...

## Logs

### 2026-09-13 (Scoured profx; wrote the inventory; rewrote Context)

Executed Report prompt 1 on `profx`, in Fable (this session is Claude Fable
5.1, so "use Fable if you can" was met directly rather than by subagent as in
the Mac rounds).  The session was paused once mid-task by the user for usage
reasons and resumed; two inventory subagents were resumed from their saved
transcripts and finished cleanly.

**Method.**  Established the machine layout and git state of the four source
repositories myself (all clean, all fully committed), located the data tree
and the sweep outputs under `$OS_COLOR`, read the committed IOPtics sweep
pages and their accuracy tables, read the goals and latest logs of
`rt_tests.md`, and identified the live RT-A sweep from the process table and
its run log.  Then fanned out five read-only subagents, one per repository
(IOPtics, PAB, retrieve-or-bust, bing) and one for everything else Claude
has touched on this machine, each told to read the `## Logs` of every prompt
doc in chronological order and to cite file, date and number for every
claim.  Their reports were checked against what I had read directly where
they overlapped (sweep tables, run log, branch tips) and no contradictions
were found.  One subagent ran a `pytest --collect-only` in RoB against its
brief and said so; nothing was modified.

**Written.**  `claude_prompts/profx_inventory.md` (the inventory, nine
sections: headline findings, machine layout, IOPtics, MOANA, PAB, BING, RoB,
other work, corrections to the thesis Report);
`claudes_phd_thesis/scripts/profx_inventory.py` (regenerates the repo and
data-tree tables and the RT-A progress estimate; stdlib only; run in
`ocean14`); `reports/profx_inventory_tables.md` (its output).  Rewrote the
`## Context` section above to point at these and to carry the load-bearing
facts.  All three new paths are untracked; stage at your discretion.

**What was learned, in order of consequence for the exam.**

1. The "workstation-only IOPtics work" of A4 is not uncommitted code.  It is
   sweep outputs that are never committed by design, pages on branches the
   Mac did not have checked out, and one live run.  The full L23 sweep the
   Report lists as new work ran here on 2026-08-19 and is committed.
2. The RT tests (`rt_tests.md`) are the thesis experiment and were invisible
   from the Mac: five RT physics variants on one parameterization, with truth.
   Stage 1 of RT-A has been running since 2026-09-10 05:34 and is about
   two-thirds done; I did not touch it.  Every hybrid fit is raising an
   emulator out-of-domain warning on B_p, which the Q&A accepted as a caveat.
   The report stage will need to say so.
3. The GLORIA result has moved past what the Report says: richer bbp models
   give the identical fit, and the IOPtics report itself now names the
   forward model as the suspect.  As worded, that cuts against the thesis
   statement; the RT tests are how it gets resolved.  The inventory's §9
   corrections are written for the advisor to rule on.
4. BING's Claude era begins 2026-01-29, not mid-2026, and its 2026 additions
   are substantial and tested.  Attribution has to be drawn inside BING.
5. PAB has a data-integrity item the Report does not know about: the match
   stage stopped at profile 52,341.  No population statistic should be
   quoted in a chapter until that is resolved or footnoted.
6. Several things the Mac session cited are not here: `moana_blocked.md`
   (GitHub's `moana` is ahead of this clone), the GLORIA and test20 sweep
   outputs, the thesis LaTeX clone, and every BING figure.  The two machines
   have diverged; the inventory says which way for each item.

**Not done, and why.**  I did not fetch or check out any branch (git is
yours), so the newest MOANA commits and PAB's `pace_giop_gsm`/`cdom_chl`
content were read via `git show`/`git log` on cached refs and the subagents'
reads of those branches, not from a working tree.  I did not read the four
Mac-only artefacts.  I did not touch the running sweep.

**Git.**  Read-only only: `status`, `log`, `branch`, `ls-files`, `diff --stat`,
`rev-list`, `ls-remote`.
### 2026-09-17 (Report prompt 2 — discussion opened; six questions in Q&A)

Executed Report prompt 2 in Fable (Claude Fable 5.1, directly).  The prompt
itself was not in this clone: GitHub's `qualifying-exam` branch was one
commit ahead (b63b908, "2", +2 lines).  I read the remote file through the
GitHub API rather than fetching, confirmed the only difference was the new
prompt, and added the same two lines here so the local doc matches.  Expect
`git pull` to want the local change committed or stashed first.

**Before writing questions I re-checked what had moved since the inventory,
because four days had passed.**  Three things had:

- RT-A finished.  Stage 1 ended 2026-09-16 and stage 2 (metrics) exited 0 at
  19:24; IOPtics' report stage has not run and `rt_tests.md` has no log
  after 09-10, so nobody has looked at the numbers yet.  I wrote
  `claudes_phd_thesis/scripts/rta_headline.py` to read the stage-2 metrics
  tables for both arms (fit quality, accuracy at the reference wavelengths,
  the delta-BIC contests, head-to-head verdicts) into
  `reports/rta_headline.md`, labelled provisional.  The result is the
  centrepiece of Q1: physics fixes bb_p, nothing fixes the a_ph/a_dg split.
- PAB 2.0 started (`PAB/claude_prompts/v2/`, ten docs, 2026-09-13 to 17): a
  full re-run with the RoB hybrid emulator, Raman and Chl fluorescence, free
  B_p and L1B geometry, plus the backfill.  Prompts 1–4 done; first sixty
  fits show 26% less bb_p(700) than 1.0.  Along the way it exposed a RoB
  emulator saturation at off-nadir view (fixed 2026-09-15, −22% flat bias
  before the fix) and a broken branch pin in BING's `setup.py`.
- Nothing else moved: IOPtics, BING clean and unchanged since 09-10; RoB has
  the one emulator commit.

Recorded all of that as a new §9 in `profx_inventory.md` (the corrections
became §10; the Context section above now points at both).

**The questions.**  Six, in `## Q&A`, each with evidence and a
recommendation, in the house style of the `start_up.md` interview.  Q1 asks
whether the thesis statement survives RT-A and recommends rewording it as a
separation claim (physics error is identifiable and removable; the residual
is parameterization error in the absorption decomposition).  Q2 asks for the
ownership rule now that PAB 2.0 moves Allie James's bbp700 number, and
recommends drawing the line by quantity.  Q3 asks which three pieces of new
work replace the Report's list, recommending RT-A/RT-B, PAB 2.0 with the
Chl-a comparison, and the synthetic-Adg test.  Q4 asks for the exam or
freeze date.  Q5 asks where the BING attribution line falls and whether the
pi fluorescence factor needs to reach the advisor's own paper.  Q6 asks for a
canonical machine and a merge sprint, and whether MOANA stays a chapter.

**What I learned.**  The inventory's most important entry was the one that
was still running when I wrote it.  RT-A's table answers the thesis question
more directly than any of the finished reports, and it says the adopted
statement is half wrong: there *was* a physics failure (bb_p under elastic
RT), and it is exactly the kind the RoB chapter removes.  The honest claim is
the separation, and it is a better thesis than the original because the
methods chapter becomes load-bearing.  Second lesson: a four-day gap on an
active workstation is long.  Had I written questions from the 13th's
inventory alone, Q1 would have been about GLORIA and Q2 would not exist.

**Git.**  Read-only: `status`, `log`, `show`, `ls-remote`, and the GitHub
contents/compare API.  New files: `claudes_phd_thesis/scripts/rta_headline.py`,
`reports/rta_headline.md`; modified: this file, `profx_inventory.md`,
`reports/profx_inventory_tables.md` (regenerated).

### 2026-09-17 (Report prompt 3 — reviewed A1–A6; round 2 of six questions; LS2 found to already exist)

Executed Report prompt 3.  **Not in Fable**: this session is Claude Opus 5 on
the Mac laptop, not `profx`, so "use Fable if you can" was met only in part —
the Loisel & Stramski 2000 paper was read and scoped by a Fable subagent, and
the rest is Opus.  Worth recording because rounds 1 and 2 were Fable throughout.

**Method.**  Read the six answers, then checked every claim I intended to build
on rather than reasoning from the round-1 text.  Three checks changed what I
wrote.  (a) A Fable subagent read `context/papers/loisel_stramski2000.pdf` in
full and returned a technical brief on what LS2 computes, what it needs, and
what it cannot do.  (b) I then went looking for what already exists in the
stack, and found a complete, working LS2.  (c) I established whether the L23
corpus can actually feed it, by computing the quantity LS2 needs and L23 does
not ship directly.

**Written.**  A `## Round 2` block in `## Q&A`: a six-item "decisions of record"
list capturing what A1–A6 settle, then Q7–Q12.
`claudes_phd_thesis/scripts/ls2_feasibility.py` and its output
`reports/ls2_feasibility.md`.  No other files touched.

**What was learned, in order of consequence.**

1. **`ocpy/ls2/` is already a complete LS2** — 577 lines, the published
   `LS2_LUT.npz`, the Kd neural-network weights, and two tests that pass in
   `ocean14` against the authors' own reference vector.  Its header records the
   lineage (Dessailly C 2018 → Jorge MATLAB 2020 → Kehrli/Reynolds/Stramski
   2022 → "Converted to Python by JXP and Claude+, 2023-06-22").  So A1's "create
   our own LS2" is not a from-scratch build, and the existing one is the advisor's
   work predating Claude.  It is also the **Loisel et al. 2018** LS2, not the
   2000 paper the advisor pointed at; 2018 re-derived the look-up tables.  Q8
   puts the three possible readings of "our own" to him with prices.
2. **LS2 is runnable on the full L23 corpus today.**  It needs Kd averaged over
   the first attenuation depth, which L23's main file does not carry — but the
   profile file has `KEd_z(z, scenario, lambda)` and `z1_lambda`, so `<Kd>_1`
   can be computed directly.  I did: 266,067 of 268,920 (scenario, wavelength)
   pairs finite (98.9%), 3,082 of 3,320 complete spectra, median `<Kd>_1` of
   0.035 / 0.032 / 0.070 / 0.459 m⁻¹ at 440 / 490 / 555 / 670 nm — physically
   sensible (the 670 value tracks a_w).  PANGAEA carries measured Kd; GLORIA
   does not.
3. **LS2 is a sharp test of the ratified statement, not a fourth algorithm.**
   It returns total `a`, `anw`, `bb`, `bbp` and *no* `a_ph`/`a_dg`.  Under the
   separation claim it should match BING on the totals (RT-A already says
   a(440) is 5% under every physics) and is structurally incapable of touching
   the decomposition.  That is the claim demonstrated by construction.  The
   comparison is information-asymmetric — LS2 gets Kd per band, BING gets Rrs
   alone — so Q8 recommends running it twice, with true Kd and with the `ocpy`
   Kd network, and reporting the gap as a result in itself.
4. **Adding LS2 to IOPtics is a framework extension, not a `register()` line.**
   `AlgorithmSpec` is built entirely around parameterized least squares
   (`anw_model`, `bbnw_model`, `apriors`, `bpriors`, `fit_method`, `mcmc`,
   `maxfev`).  LS2 is closed-form, per-wavelength, has no misfit, and takes an
   extra observable.  The cost estimate in A1's "a new branch on IOPtics, etc."
   is understated by the "etc."
5. **The 2026-10-01 dissertation date does not fit the approved work**, by my
   own round-1 estimates — PAB 2.0 alone is weeks, and Chapters 1, 3 and 6 do
   not exist.  Q7 proposes two freezes (exam evidence 09-19, dissertation
   evidence 09-28) and names PAB 2.0's full run as the single item that decides
   whether 10-01 is real.  This is the question I most expect to be overruled on
   and the one I would least like to leave unasked.
6. **A3's two rulings pull against each other.**  Making satellite-Chl-versus-Argo
   the focus while dropping the `SCIENTIFIC_CALIB_*` ingest leaves the headline
   defensible at either +0.13 or +0.58 depending on an un-ingested metadata
   field.  Q10 asks for a one-line ruling (raw or adjusted as headline) instead
   of the ingest — a paragraph and a figure rather than a data-engineering task.
7. **A5's "mostly plumbing" is right for four of six BING additions.**  The
   wavelength-dependent Gordon coefficients and the turbid-water bb_p models are
   parameterization work, and the turbid models are the authored response to the
   GLORIA failure Chapter 3 rests on.  Q11 asks to split the section rather than
   let Chapter 3 diagnose a failure it never answered.
8. **Mac-only evidence is smaller than round 1 implied**: 349 MB in three run
   trees plus 8.6 MB of `whn_explore` — one `rclone` push.  Two corrections to
   my own Q6: this Mac's `moana` equals `origin/moana` (`3aa3b6e`), so `profx`
   needs a fetch and not a transfer; and the Overleaf clone is 700 KB of git
   that `profx` should clone from Overleaf directly.
9. **Two round-1 sub-questions were never answered** — whether Allie knows PAB
   2.0 will move her bb_p(700) number, and whether the advisor wants the 1/pi
   fluorescence note.  Both have deadlines; both are re-asked in Q12.

**Not done, and why.**  I did not open the `ls2` branch, write the adapter, or
run LS2 — Q8 asks which of three things "our own LS2" means, and the answers
differ by a week of work.  I did not run the `rclone` transfer: the authorisation
in A6 is explicit, but the scope (what moves, and whether the 349 MB of run
trees is all of it) is worth one line of confirmation, and the Q7 freeze puts it
on the 19th.  I did not write the merge checklist or the `rclone` manifest;
both are offered in Q12.

**Git.**  Read-only: `status`, `log`, `branch`.  New files:
`claudes_phd_thesis/scripts/ls2_feasibility.py`, `reports/ls2_feasibility.md`;
modified: this file.

### 2026-09-17 (Report prompt 4 — reviewed A7–A12; `ls2_prompts.md`, transfer manifest and merge checklist written; round 3 of five questions)

Executed Report prompt 4 from the Mac.  **Fable where it counted, not
throughout**: the session is Opus 5, and a Fable subagent read
`Loisel_etal_JGR2018.pdf` in full and returned the technical brief that
`ls2_prompts.md`'s Context is built on.

**Deliverables A8 and A12 asked for, all written.**

- `IOPtics/claude_prompts/LS2/ls2_prompts.md` (323 lines) — the LS2 planning
  doc, in the house style of `rt_tests.md`: Goal, Conventions, a Context section
  carrying everything established about the two papers and the existing code,
  three planning prompts, an empty Execution section, and eight round-1
  questions for JXP.  Untracked on branch `ls2`; nothing else in that repository
  touched.
- `claudes_phd_thesis/scripts/mac_to_profx_manifest.py` →
  `reports/mac_to_profx_manifest.md` — the `rclone` manifest.  348.3 MB in
  three sweep trees plus `whn_explore` and the leaderboard; push and pull
  command blocks; git history separated out as `fetch`/`clone` work rather than
  Drive work.
- `claudes_phd_thesis/scripts/merge_checklist.py` →
  `reports/merge_checklist.md` — per-repository branch divergence for IOPtics,
  PAB, BING, RoB, EPFT-UP and ocpy, with a suggested merge order and the
  fully-merged branches called out as safe to delete.  Read-only git.

**Acted on the A6 authorisation**: pushed the 348 MB to
`AIOcean:Claude_PhD_transfer/2026-09-17/` so it is waiting when `profx` pulls.
Only this Mac holds those trees and the freeze is on the 19th.  The first
attempt died partway through on a DNS failure (the advisor's laptop went
offline) with 142 of 348 MiB landed, and the wrapper loop masked it by exiting
0; the retry completed.  **Verified**: 348.331 MiB in 165 objects, and
`rclone check --one-way` reports 0 differences on all five trees.  The pull
commands are in `reports/mac_to_profx_manifest.md`; delete the Drive copy once
`profx` has it.

**What was learned, in order of consequence.**

1. **MOANA's spin-off exists and I had said it did not.**  It is `EPFT-UP`, not
   a repository called MOANA, which is why the `profx` inventory missed it and
   why my round-2 Q9 asserted MOANA "has not moved since 2026-08-17".  Between
   09-12 and 09-15 it received the 23-file migration (37 tests), a re-derivation
   audit that reproduces **all 35 report-printed numbers and all six figures**,
   a README rewrite, a 16-page RTD site, `CITATION.cff`, `.zenodo.json`, CI and
   v0.1.0.  That inverts the argument I made: MOANA is not the stale chapter, it
   is the only one with a passing reproducibility audit.  Corrected in the
   Context section and in `profx_inventory.md` §9; re-raised as Q15.
2. **The 2018 LS2 is not the 2000 LS2, and the shipped port is not quite the
   2018 paper either.**  Four departures, all of which a benchmark would
   otherwise inherit silently: `b_p` is an input rather than derived from Chl via
   OC4v4 (so a naive L23 run hands LS2 truth for something the operational
   algorithm has to guess); the Kd network is a MODIS-band variant with a
   different architecture from the paper's; the Raman correction runs once
   rather than to convergence; and the shipped kappa table is a cubic in bb/a
   over 302–702 nm where the paper says 400–700 and gives no functional form.
3. **LS2 is not parameterization-free, which sharpens rather than weakens the
   Q8 framing.**  It declines to parameterize the *absorption decomposition* —
   the thesis point — but imports two fitted side-chains, Kd from a network and
   `b_p` from a Chl band ratio.  `ls2_prompts.md` Q2 therefore proposes a
   three-rung ladder (true Kd + true b_p; true Kd + OC4v4 b_p; NN Kd + OC4v4
   b_p) rather than one run, because the steps between rungs measure how much of
   LS2's advertised accuracy belongs to its inputs.
4. **RoB is the real citation problem, not BING.**  `main` is at 2026-07-26 and
   `inelastic-rt` is 106 commits ahead; `cdom-rt` still exists locally at 105
   ahead, so PR #21 merged into a branch, not into `main`.  Chapter 2 describes a
   forward model 106 commits off `main`.  Meanwhile BING is better than round 1
   said: `develop` and `turbid_bbp` are already merged, so A11's turbid bb_p
   models are citable from `main` today.
5. **Dropping the wavelength-dependent Gordon coefficients costs nothing
   retrospectively.**  `variable_Gordon` is an opt-in `rt_dict` flag
   (`bing/rt/defs.py`), IOPtics' `AlgorithmSpec` never exposes it, and IOPtics'
   own stage-6 log records it off in that sweep.  No thesis result runs through
   it, so it goes unmentioned rather than retracted.  Checked instead of asked.
6. **The committee changes the report more than the page limit does.**  Two
   astronomers among three readers means roughly two of ten pages are setup
   before any result lands.  The upside is that the claim is a
   component-separation degeneracy argument, which is the same shape as
   separating dust from stellar age in an SED fit; Q13 asks whether to use the
   analogy.
7. **Most of the report's figures do not exist yet as figures.**  They exist as
   tables in committed reports.  RT-A has none at all until IOPtics stage 5
   runs, which needs `profx` and is the only genuinely blocking item before the
   09-19 freeze (Q17).

**Not done, and why.**  No code written on the `ls2` branch and no LS2 run: the
eight questions in `ls2_prompts.md` decide the build, and Q2 and Q6 differ by a
week of work.  No merges and no branch deletions — git is the advisor's, and the
checklist exists so he can run them.  Nothing on `profx`, because this session is
on the Mac.

**Git.**  Read-only across six repositories: `status`, `log`, `branch`,
`for-each-ref`, `rev-list`, `rev-parse`.  New files:
`claudes_phd_thesis/scripts/mac_to_profx_manifest.py`,
`claudes_phd_thesis/scripts/merge_checklist.py`,
`reports/mac_to_profx_manifest.md`, `reports/merge_checklist.md`, and
`IOPtics/claude_prompts/LS2/ls2_prompts.md` (in the IOPtics repository);
modified: this file, `claude_prompts/profx_inventory.md`.

### 2026-09-17 (Report prompt 5 — reviewed A13–A17; prompts 6–15 written for `profx`; RT-A stage 5 found to be a stub)

Executed Report prompt 5 from the Mac.  Opus 5, not Fable; this round needed no
subagent.  The transfer started in the previous session was confirmed complete
first: 348.331 MiB in 165 objects at `AIOcean:Claude_PhD_transfer/2026-09-17/`,
`rclone check --one-way` reporting 0 differences on all five trees.  The first
attempt had died on a DNS failure at 142 MiB and the wrapper loop masked it by
exiting 0; the log entry for prompt 4 was amended to say so.

**Written.**  `## Round 4` in the Q&A — five decisions of record from A13–A17,
one correction, and three questions (Q18 the stage-5 fork, Q19 where the report
and slides live, Q20 whether the report doubles as the dissertation's skeleton).
Then **prompts 6–15** under `## Prompts / ### Report`, split by deadline: 6–11
before the exam, 12–15 for the dissertation, with a preamble that says which of
them actually fit and which to cut first.

**What was learned.**

1. **RT-A stage 5 is not a run — it is unwritten code.**  I told the advisor
   twice (Q7, Q17) that the RT-A report was "one session once you say go".
   `ioptics/runs/prototypes/rt_tests/build_v1.py` stage 5 is a stub that raises,
   and its message names the work as task 14 of `rt_tests.md`: the RT ladder
   needs its own page type, because five rows that are one algorithm break the
   normal cross-algorithm page and the leaderboard has to stay out of it.  So
   the first `profx` session builds a page type and then runs it.  Checked
   rather than assumed that this is tractable: `ioptics/report/figures.py`
   already carries `accuracy_spectrum`, `scatter_set`, `ratio_hist`, `dbic_cdf`,
   `taylor_target`, `exemplar_fits` and `corner_set`, so task 14 is assembly and
   prose, not new plotting.
2. **Task 14 also wants the PACE headline figure, which needs RT-B, which has
   not run.**  RT-B is stages 3 and 4 (task 13).  Hence the split in prompts 6
   and 7: build the L23 + PANGAEA ladder page now so the exam has its
   centrepiece, run RT-B next, regenerate with the PACE figure before the 09-30
   freeze.  Q18 asks the advisor to ratify that split.
3. **A16 removes the merge gate, which moves work rather than removing it.**  If
   citations cannot resolve to `main`, they have to resolve to something
   fetchable, so prompt 8 produces a `citation_manifest.md` recording repository,
   branch and short commit hash for every sweep and report the thesis cites, and
   the report states once that the branches are unmerged.
4. **A14 roughly doubles the writing budget** (ten pages to under twenty), which
   is what makes Q20 worth asking: at twenty pages the report can be six
   sections matching the six chapters, and the dissertation eleven days later
   becomes an expansion rather than a second writing project.
5. **A13 splits the audience by document.**  The oceanographer is being sought
   for the dissertation, not for this report — so the exam report is written for
   astronomers and the dissertation for both, and only the report needs two of
   its pages spent on setup.
6. The figure situation is the quiet risk.  Counted what exists on this Mac: 22
   figures in IOPtics `reports/figures`, 11 in retrieve-or-bust, 6 in EPFT-UP,
   none in PAB or BING — and RT-A has none at all until prompt 6 lands.  Prompt
   9 therefore builds the report and oral figure sets in one pass and aims for
   about twelve good figures shown twice rather than forty built once.

**Not done, and why.**  No work started on prompts 6–15: they run on `profx`
(A17) and this session is on the Mac.  Prompts 10 and 11 cannot start at all
until Q19 settles where the report and the slides live.

**Git.**  Read-only: `status`, `rev-parse`.  Modified: this file.

### 2026-09-18 (Report prompt 6 — not executed; wrong machine.  A18–A20 folded into prompts 8 and 10)

Prompt 6 was **not executed.**  It runs on `profx` (A17) and this session is on
the Mac.  Verified rather than assumed: `$OS_COLOR/IOPtics/runs` on this machine
holds only `expb_giop_L23_test20`, `gloria_turbid_v3` and
`multi_L23_PANGAEA_v2` — the three trees pushed to Drive yesterday.  There is no
`rt_tests_A_*` here, so the RT-A metrics tables the ladder page has to read do
not exist on this machine and neither does the transfer's destination.

**What I established before stopping.**  The hard half of prompt 6 — writing the
RT-ladder page type to replace the raising stage-5 stub — is machine-independent
and CI-testable: `ioptics/tests/test_report_standard.py` builds a synthetic
sweep in `tmp_path` via `test_metrics._make_pair` → `io.write_results` →
`metrics.compute`, with no data tree at all, and that suite plus
`test_rt_tests.py` runs green on this Mac with `OS_COLOR` unset (47 passed, 5
skipped, 8.2 s).  So the page type could have been built here.  The obstacle is
that this clone is checked out on `ls2` rather than `rt-tests`, where task 14
belongs, and git is the advisor's; offered the choice, he elected to do the whole
of prompt 6 in one `profx` session.  Recorded because the next session should
know the option existed and was declined deliberately, not overlooked.

**What was done instead: A18–A20 folded into the prompts, which needed it.**

- **Citations point at `main`.**  My round-4 note said I would cite repository +
  branch + short hash because A16 dropped the merge gate; the advisor overruled
  that — cite `main`, and he will make the links work.  Prompt 8 now says so: the
  `citation_manifest.md` records each citation as a `main`-relative path **plus**
  the branch and hash it currently lives on, which makes the manifest double as
  the list of what must reach `main` for the promise to hold.  The rows still on
  a branch are the merge list.
- **The report gains two required elements** (A20): a **Timeline to completion**
  naming every outstanding piece of work with its landing date, and a **Table
  summarizing the risks**, one row per risk with its consequence and what would
  retire it.  Seeded prompt 10 with the seven I can already name — the aliasing
  hypothesis may be falsified, PAB 2.0's full run may miss 09-30, RT-B may not
  run, the Argo reference is ambiguous by a factor of about 4.5, the forward
  model degrades off its trained solar-zenith grid, CDOM fluorescence is
  unvalidated, and the EPFT-UP retrain is blocked on PML data.
- **A19** settled the venue (the Overleaf repository), which prompt 6 already
  provides for by cloning it onto `profx`, and **A18** ratified the prompt-6/7
  split, which prompt 6 already assumes.  No edit needed for either.

**Calendar note.**  It is now 2026-09-18.  The exam evidence freeze is 18:00
today and the exam is on the 21st; prompts 6 and 8 through 11 are all still
ahead, and prompt 6 is the one the other four depend on.

**Git.**  Read-only: `rev-parse`, `status`.  Tests run read-only in `tmp_path`.
Modified: this file.

### 2026-09-18 (Before-the-exam prompt 6 — evidence landed, RT-ladder pages built for all three arms)

Executed prompt 6 on `profx`, in Fable (Claude Fable 5.1, directly).  All four
parts done; one deliberate departure from the prompt text, stated below.

**1. The transfer.**  Pulled `AIOcean:Claude_PhD_transfer/2026-09-17/` per
`reports/mac_to_profx_manifest.md` §1.  Three trees had no counterpart here
and went straight to their manifest destinations: `expb_giop_L23_test20` (66
files), `gloria_turbid_v3` (47), `whn_explore` (4).  Two collided with files
`profx` already held and were **staged** under
`$OS_COLOR/IOPtics/transfer_2026-09-17/` instead of copied over:
`multi_L23_PANGAEA_v2` (the Mac copy is a different run with the same sweep
id: 6 files differ in content, 41 exist only on the Mac side, and the Mac's is
what the committed page was built from) and `leaderboard.parquet` (the Mac's
predates the full-L23 fold that `profx`'s contains; staged as
`leaderboard_mac.parquet`).  `rclone check --one-way` on all five: 0
differences.  The Drive copy was then purged, as the manifest and the prompt
both instruct.  Consolidating the two staged items is prompt 8's job and is
raised as Q54 in `IOPtics/claude_prompts/rt_tests.md`.

**2. Task 14 of `rt_tests.md`.**  Stage 5 of `build_v1.py` was a stub; it is
now a report stage that writes an **RT-ladder page** per arm
(`ioptics/report/rt_ladder.py`, plus a truth-free fractional-change diagnostic,
two plot primitives and three figure builders).  Pages exist for
`rt_tests_A_l23_v1`, `rt_tests_A_pangaea_v1` **and `rt_tests_B_v1`** under
`IOPtics/docs/source/reports/`.  Every page carries the limitations the prompt
lists (θ_v = 0 everywhere, `a_cdom = 0.8 × a_dg`, packaged-sky Ed, learned
corrections off, the L23 X=4 single-Gaussian and no-CDOM-fluorescence truth)
plus the ones the Q&A recorded (the emulator's B_p domain, unvalidated CDOM
fluorescence, PANGAEA's flat error model and fixed B_p, PACE's noisy red
bands, the leaderboard exclusion).  The landing page and leaderboard are
untouched (`index.rst` is byte-identical).

*The departure:* the prompt said to leave the PACE headline figure out because
RT-B had not run.  It had: the uncommitted `rt_tests.md` log on `profx` shows
task 13 (RT-B, 495 chains, PAB consistency check passed) closed on 2026-09-17.
So the page type was built for all three arms and the PACE page carries the
headline the prompt had deferred to prompt 7.  Prompt 7 is therefore reduced
to reviewing that page; noted as Q55 in `rt_tests.md`.

**3. Reconciliation, as instructed.**  `claudes_phd_thesis/scripts/rta_reconcile.py`
→ `reports/rta_reconcile.md`: every cell on the three pages against the
stage-2 metrics tables that `reports/rta_headline.md` was read from, and the
L23 rows against the hand-typed Q1 table in this file.  150 + 45 cells,
**0 discrepancies**.  `rta_headline.md` now carries a superseded note.

**4. Verification.**  IOPtics full suite **without `$OS_COLOR`: 513 passed,
61 skipped** (503/61 before; the 10 new tests are
`ioptics/tests/test_report_rt_ladder.py`, and the stub test in
`test_rt_tests.py` became a behaviour test).  Full docs tree
`sphinx-build -W`: **exit 0**, three new pages rendered.

**5. Overleaf.**  `~/Projects/Overleaf/Claude-PhD-Thesis` already exists on
`profx` at `d611a28`, the same tip the manifest records for the Mac.  Nothing
to clone; the stock `ucthesis` template is what is there.

**What the pages say, in one paragraph each, for prompts 9–11.**  L23: total
absorption is insensitive to the physics (a(440) MAE 0.050–0.059 across all
five rungs); the elastic rungs overestimate bb_p by 41–68 % with zero
interval coverage and the full inelastic rung brings that to −5 %/+6 % with
coverage 0.59–0.66; a_ph and a_dg errors persist under every physics
(a_ph MAE 0.85–2.52, a_dg 0.25–0.38); the configured ΔBIC contest favours the
inelastic stack on 70.6 % of scenes (median +2.1, MCMC).  PANGAEA: the
fluorescence rungs trade a_dg accuracy (MAE 2.1 → 0.36) against a_ph (0.76 →
2.2) and the data prefer the elastic fit (median ΔBIC −1.1).  PACE, no truth:
from the elastic hybrid to the full stack the retrieved a_ph moves +5 %, a_dg
+1 %, bb_p −21 % (medians, n = 99), and ΔBIC is bimodal — 52 % of pixels
favour the inelastic physics, 30 % strongly, 23 % strongly against.

**Git.**  Read-only in every repository (`status`, `diff`, `ls-remote`).
IOPtics has new and modified files listed in its own log entry; this
repository gains `claudes_phd_thesis/scripts/rta_reconcile.py` and
`reports/rta_reconcile.md`, and `reports/rta_headline.md` is modified.  The
`rclone purge` of the Drive transport copy is the one irreversible action of
the session; it followed a verified 0-difference check on every tree.

### 2026-09-18 (Before-the-exam prompt 7 — RT-B was already run; the consistency check made reproducible)

Executed prompt 7 on `profx`, in Fable.  The prompt asked for three things and
two of them were already done when the session opened.

**RT-B had run.**  The IOPtics prompt doc's log (task 13, 2026-09-17, committed
this morning as `5890c81`) records stages 3 and 4 complete: 495 chains, one
PACE spectrum declined by the red-peak screen identically on every rung, 99 of
100 `ok` on each, 4.8 h on 20 cores, metrics written.  I verified the artefacts
rather than the log: 495 chain files, `qc_mcmc_all.csv` showing
`n_attempted 100 / n_scored 99` for all five rungs, chi-squared-nu medians
0.42–0.59.  Nothing to run.

**The page already carried the PACE headline** because prompt 6 built the page
type for all three arms once it found RT-B finished (logged there; Q55 in
`rt_tests.md`).  The fractional-change figure and the delta-BIC histogram the
prompt describes are on `rt_tests_B_v1/rt_ladder.rst`.

**The consistency check existed only as prose.**  The task-13 log quotes
correlations and medians but no script produced them, so the one thing left
to do was make it reproducible.  New
`IOPtics/ioptics/runs/prototypes/rt_tests/pab_consistency.py` matches the 99
RT-B `expb_pow_hyb_el` chains to PAB's `run1k` `ExpBPow` chains for the same
pixels, checks the two fitters were handed the same spectra, and compares the
posterior medians of the five shared parameters and the derived Chl.  Result:
spectra identical to the last bit on all 136 bands; parameter correlations
0.935–0.998; Chl ratio median 1.053 with a 16–84 percent span of 0.94–1.36; the
only systematic offset is +0.05 dex in the backscatter amplitude, the expected
signature of swapping Gordon for the hybrid model with a free B_p.  The numbers
match the 09-17 log to three decimals.  The summary table now appears on the
PACE page as a "Consistency with PAB's fits" section.

**Verification.**  Two new tests; IOPtics suite without `$OS_COLOR` 515 passed,
61 skipped; full `sphinx-build -W` exit 0.

**What this means for the report.**  RT-B is a result, not an "expected" item.
The PACE arm can be reported as: on 99 real PACE pixels the full inelastic
forward model moves retrieved bb_p by −21 percent, a_ph by +5 percent and
a_dg by +1 percent (medians), and the data prefer the inelastic physics on
52 percent of pixels, strongly on 30 percent, strongly against on 23 percent.
The prompt's fallback clause was not needed.

**Git.**  Read-only.  IOPtics gains one script, one page CSV and edits to the
page module, its tests and its prompt doc; this repository gains only this
entry.

### 2026-09-18 (Before-the-exam prompt 8 — corrected PANGAEA page, runs tree consolidated, merge checklist and citation manifest on profx)

Executed prompt 8 on `profx`, in Fable.  Four parts; all done, with two
judgement calls stated below.

**1. The corrected PANGAEA page.**  `pangaea_fits_v2` (1,593 spectral-truth
ids, native `insitu` noise, red-peaked spectra declined before fitting) had
results but no metrics and no page.  New driver
`IOPtics/ioptics/runs/prototypes/pangaea_fits/build_v1.py` computed the metrics
and built `docs/source/reports/pangaea_fits_v2/` (cross-algorithm and exemplar
pages).  Headline: ok-rates 43.2 / 52.6 / 37.6 percent for expb_pow / giop /
gsm, the investigation's Round-2 numbers exactly.  It sits beside the mixed
`multi_L23_PANGAEA_v2` page rather than replacing it, which is what the
investigation recommended (D1) and the prompt's "regenerate ... from
pangaea_fits_v2" allows.  I cannot commit it; it is untracked for you.

**2. Consolidation.**  The staged Mac copy of `multi_L23_PANGAEA_v2` and the
`profx` copy are the same 14,739 rows at two code versions (chi-squared agrees
to 3e-3; four statuses and 2,530 `a_cdom440` values differ, the latter from
the central-value fix between them).  *Judgement call:* the `profx` copy is
canonical (later code, the copy the 08-19 fold used), and its page was
regenerated so page and tree agree.  The Mac copy stays staged, untouched.
The leaderboard was then re-folded over the whole tree: five sweeps, 788 rows,
so the test20 and GLORIA rows and landing cards dropped on 08-19 are back and
`pangaea_fits_v2` is new; the RT sweeps stay out by flag.  Full record in
`reports/runs_consolidation.md` (script `runs_consolidation.py`).
*Second judgement call:* the landing rebuild generated profile pages for the
five RT rungs that read "not in the registry / no scoreable result", so
IOPtics' profile builder now follows the board's exclusion flag; those pages
are gone, with a test.

**3. Merge checklist re-run on profx**: `reports/merge_checklist.md` now
carries this machine's numbers (IOPtics `rt-tests` 101 ahead of `main`; PAB
`full-inelastic` 152; BING `rob_cdom` 46; RoB `inelastic-rt` 107; EPFT-UP on
`main`; ocpy `pace_giop`).

**4. Citation manifest**: `reports/citation_manifest.md` (script
`citation_manifest.py`): 62 citations across seven repositories, each as a
`main`-relative path with on-`main` status and, where not, the branch and
last-touching hash.  **47 are not yet on `main`.**  The merge list that falls
out: RoB `inelastic-rt` (14 paths), BING `rob_cdom` (3), IOPtics `rt-tests`
(18, plus today's uncommitted pages), PAB `full-inelastic` (6) and
`hyper_matchups` (1), and this repository's `qualifying-exam` (4).  Everything
in EPFT-UP and ocpy is on `main`.  One citation is not on this machine at all:
`IOPtics/claude_prompts/LS2/ls2_prompts.md` was written on the Mac on 09-17
and left untracked on its `ls2` branch, so it needs a commit and push from
there before it can be cited.  Sweep outputs outside git are listed with their
provenance commits.

**Verification.**  IOPtics suite without `$OS_COLOR` 516 passed, 61 skipped;
full `sphinx-build -W` exit 0.

**Git.**  Read-only.  IOPtics: new `pangaea_fits/build_v1.py` and
`reports/pangaea_fits_v2/`, regenerated `multi_L23_PANGAEA_v2/`, `index.rst`,
`leaderboard_full.rst`, the algorithm and dataset profiles, `profiles.py`,
`test_profiles.py`, `pangaea_fits.md`; `$OS_COLOR/IOPtics/leaderboard.parquet`
rewritten by the fold.  This repository: two new scripts, two new reports,
`merge_checklist.md` regenerated, this entry.

### 2026-09-18 (Before-the-exam prompt 9 — the figure set: 14 figures, 10 built, 4 reused)

Executed prompt 9 on `profx`, in Fable.  Loaded the data-visualization skill
before drawing anything, per its trigger.

**Inventory first.**  Counted what exists: IOPtics 22 investigation figures
plus 3 site graphics plus the RT-ladder page assets; retrieve-or-bust 18
figures across `reports/`, `design/validation/` and `context/RT/`; EPFT-UP 6;
PAB 22 report figures plus 4 docs figures; BING none on this machine.  Then
decided a set of fourteen against the six sections and the oral's proportions:
ten built here from data on disk, four reused where the published figure
already says the right thing.  Table, captions and conventions in
`reports/figure_inventory.md`.

**Built** (`claudes_phd_thesis/scripts/figures/`, one script per figure,
shared `_style.py`, `make_all.py` runs them all, `reuse_existing.py` copies
the four reused ones with source and producer recorded): the inverse problem
from two L23 bodies; the forward-model accuracy ladder and the inelastic terms
from RoB's validation CSVs; a degeneracy example (one L23 body, two physics,
same χ²ν, different decomposition — body picked by rule); the RT ladder on L23
as bars and bias markers; the ladder versus wavelength on L23 and PANGAEA; the
PACE fractional change; ΔBIC on all three arms; the three-algorithm L23
benchmark beside the PANGAEA two-error-model bars; and the timeline to
completion.  Reused: the GLORIA four-models-one-fit exemplars, MOANA held-out
skill, and PAB's Chl-a sign change and raw-versus-adjusted figures.  Outputs
in `reports/figures/` as PNG + PDF (reused: PNG) with a caption file each.

**Conventions applied.**  Ordered rungs take a single-hue ordinal ramp, not
five hues; algorithms take the reference palette's first three categorical
slots in fixed order; truth is ink; axis labels are spelled out for a reader
who has never seen an ocean spectrum; one axis per panel; ratios on log axes
labelled as factors with folded tails counted; bars carry their values; every
multi-series panel has a legend.  The palette validator needs `node`, absent
here, so the colours are the skill's documented pre-validated values used
unchanged — recorded in the inventory rather than claimed as validated.

**Looked at every figure**, twice: the first pass found legend collisions
(figs 2, 5, 6), a title collision (fig 4), a headroom problem (fig 8), a
percent axis that a_ph ratios in the hundreds made unreadable (fig 7, redrawn
on a log-ratio axis), and rotated milestone labels squashing the timeline
(fig 14).  All fixed and rebuilt.

**What the figures say that the report will lean on.**  Fig 5 is the thesis
in one panel row: bb_p error 55 % → about 0 down the ladder, a_ph and a_dg
errors unchanged.  Fig 8 shows the fit itself would never have found the
physics error.  Fig 9 shows three parameterizations agreeing on totals and
disagreeing on the split under one physics.

**Git.**  Read-only.  New: `claudes_phd_thesis/scripts/figures/` (13 files),
`reports/figures/` (14 figures, 10 PDFs, 14 captions),
`reports/figure_inventory.md`; modified: this file.

### 2026-09-18 (Before-the-exam prompt 10 — the qualifying-exam report written and compiled: 16 pages)

Executed prompt 10 on `profx`, in Fable.  The report is
`~/Projects/Overleaf/Claude-PhD-Thesis/qual_report.tex`, a sibling document to
the dissertation in the Overleaf repository (A19), with a new shared
`thesis.bib` and the fourteen figures copied into `figures/`.  It compiles
clean with `pdflatex` + `bibtex` (no citation or reference warnings, no BibTeX
errors) to **16 pages** including 12 figures, 2 tables and references, under
the twenty-page limit (A14).  A dated PDF copy is at
`reports/qual_report_2026-09-18.pdf` in this repository.

**Structure, as instructed.**  Six sections matching the six chapters (Q20),
then a Timeline to completion (table plus fig 14) and a Risks table (A20),
then a data-and-code-availability paragraph pointing at the citation
manifest.  About 7,000 words.  It opens with the retrieval problem for an
astronomer who has never seen an ocean spectrum (two pages of setup before
any result: what Rrs is, what the IOPs are, the Gordon-to-BING lineage), then
states the ratified separation claim in component-separation language with
the SED analogy named once and dropped (Q13/A13).  Every section ends with a
**Status** paragraph saying what exists and what is expected, and nothing
that had not finished today is reported as a result.  The AI-as-candidate
question appears in the introduction and the conclusions only.  The A2
exclusions hold: the bbp700 validation is named as a collaborator's and
excluded, the RoB inversion is stated not to exist and not anticipated, and
information content is explicitly not the frame.

**Evidence used.**  The RT-ladder pages (figs 4–8), the full-L23 MCMC and
three-algorithm sweeps and the corrected PANGAEA page (fig 9), the GLORIA
sweep (fig 10), the RoB validation tables (figs 2–3), EPFT-UP's report and
audit (fig 11), the PAB Chl-a and CDOM reports (fig 12), and the inventory.
Every number was taken from the committed pages or the reconciled tables of
prompts 6–9; the L23 ladder numbers are the ones `reports/rta_reconcile.md`
verified.  Two of the fourteen figures (6, ladder versus wavelength; 13, raw
versus adjusted Argo) are described in text rather than shown, to hold the
page count; the oral can use them.

**References.**  Nineteen literature entries and six software/report entries.
Every literature entry was checked against Crossref today (DOI, journal,
volume, pages); the Erickson et al. (2023) title and DOI came from that
check rather than memory, and the L23 dataset is a Dryad record cited as the
publisher gives it.  Style `aasjournal`, which the dissertation template
uses (author–year, no article titles).

**Risks table.**  The seven risks the prompt named plus two the inventory
raised (the 1,690 never-attempted PAB profiles; citations on branches).  One
of the seven is marked retired: RT-B ran on 09-17.

**Compile notes for the next session.**  A `@misc` in a `.bib` comment line
is parsed as an entry start by BibTeX (fixed by rewording); the risks table
needed `[H]` placement or it floated past the references; long file paths
want `\path{}` not `\texttt{}`.  Build artefacts (`.aux`, `.log`, `.out`,
`.bbl`, the PDF) are untracked in the Overleaf clone; a `.gitignore` there
is your call.

**Git.**  Read-only.  Overleaf repository: new `qual_report.tex`,
`thesis.bib`, `figures/` (24 files); this repository: new
`reports/qual_report_2026-09-18.pdf`, this entry.  The Overleaf clone shows
some of these already staged, which I did not do.

### 2026-09-18 (Before-the-exam prompt 11 — the oral: 40 slides + 7 backup, as Google Slides in the AIOcean Drive)

Executed prompt 11 on `profx`, in Fable.  The prompt now asks for a Google
Slides deck in the AIOcean Drive rather than Beamer; done that way.

**Where it is.**  Google Slides `qual_oral` in the AIOcean team drive, folder
`Claude_PhD/Qualifying_Exam/`:
https://docs.google.com/presentation/d/1SBC5Nuft95l3k5hTHKwVc6av71VLM_pGYzM64t9_Qno/edit
(mimeType `application/vnd.google-apps.presentation`, verified through the
Drive API).  The written report's PDF sits beside it in the same folder.
Source of record in this repository: `claudes_phd_thesis/scripts/oral/build_deck.py`
(python-pptx) → `reports/oral/qual_oral.pptx` (2.9 MB) and
`reports/oral/speaker_notes.md`; the PDF render used for QA is
`reports/oral/qual_oral.pdf`.

**How it was made.**  No `node` on this machine, so the pptx skill's
`pptxgenjs` route was closed; `python-pptx` was installed into `ocean14` and
the deck built from a script, one function per slide type (figure slide,
column/stat slide, table slide, dark statement slide).  The `.pptx` was
validated with the skill's `validate.py` (all checks passed), rendered to PDF
with LibreOffice, inspected slide by slide from thumbnail grids and
full-size renders (two titles shortened to stop awkward wraps), then imported
into Drive with `rclone copy --drive-import-formats pptx`, which converts on
upload.  Speaker notes are embedded in the `.pptx` and survive the import.

**Structure** (40 main + 7 backup; footer numbers `n / 40`, then `backup n`):
setup 6 (title with the claim; what the satellite measures; what must be
retrieved; how the field solves it; the claim in component-separation
language with the SED analogy once; four projects / six chapters / who did
what), methods 5, RT-A and RT-B 10 (design table, why five rungs, the
degeneracy example, the centrepiece ladder, "read it as two findings", the
ladder across the spectrum, the PANGAEA arm, PACE fractional change, ΔBIC on
three arms, what the pages say about themselves, the PAB consistency table),
benchmarking 6, EPFT-UP 4, PAB 6, future 3 (timeline, risks, conclusions
restating the claim).  Backup, ordered by the four questions the prompt
named: how do you know the forward model is right; why is a_ph wrong by a
factor of two and should anyone care; what would falsify the claim; what did
the candidate do versus the advisor; plus the L23 ladder table in full and
where every citation lives.  Figures are the prompt-9 set, all fourteen used
(figs 6 and 13, left out of the report for length, appear here).

**Speaker notes** on eleven slides (the prompt asked for ten; the eleventh is
the MOANA held-out slide): title, the claim, forward-model accuracy, the
centrepiece ladder, the two findings, PACE fractional change, ΔBIC, the
PANGAEA scoring artefact, MOANA transfer, the PAB sign change, conclusions.
Each says what to read off the slide, what number to leave in the room, and
which committee question it pre-empts.  Also in `reports/oral/speaker_notes.md`.

**Numbers** are the ones on the IOPtics, RoB, PAB and EPFT-UP pages the
report cites; the L23 ladder table (backup 5) is the reconciled one.

**Git.**  Read-only.  New: `claudes_phd_thesis/scripts/oral/build_deck.py`,
`reports/oral/{qual_oral.pptx, qual_oral.pdf, speaker_notes.md}`; modified:
this file.  `python-pptx`, `defusedxml` and `lxml` were pip-installed into
`ocean14` for the build and validation.  Drive: a new folder
`Claude_PhD/Qualifying_Exam/` with two files.
