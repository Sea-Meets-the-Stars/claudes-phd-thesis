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
- **MOANA** exists as IOPtics branch `moana` (report rev 4, 2026-08-17);
  GitHub holds newer commits than this clone.  No spin-off repository exists.
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

## Prompts

### Report

1. As noted in the `start_up.md` file, we need to scour my `profx` workstation to understand better all that has been accomplished by Claude.  As you are now on `profx`, please proceed to do so.  Then, update the Context section above.  Use Fable if you can.  Log your work.

2. Ok, let's now have a discussion on what you have learned from the inventory.  Focus on what you have created with me as regards our plans for your PhD.  Generate questions in the Q&A section below.  Use Fable if you can.  Log your work.

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
