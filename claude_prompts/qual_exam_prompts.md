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
   `$OS_COLOR`.  Its §9 lists the corrections it forces on the Report.
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
- **The RT tests are running now.**  Five RoB-based radiative-transfer
  variants of one BING parameterization over all of L23 X=4 and 97 PANGAEA
  spectra, launched 2026-09-10, stage 1 due about 2026-09-15.  Same
  parameterization, different physics: this is the direct test of the thesis
  statement and it is not in the Report.
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