# Getting started

## Goals

This repository holds the code, analyses, and figures behind a PhD thesis for
which **Claude is the candidate** and J. Xavier Prochaska is advisor and
committee chair.  The write-up itself lives in the LaTeX project at
`~/Projects/Overleaf/Claude-PhD-Thesis` (UCSC `ucthesis` class); this repository
is where the science gets done.

**The thesis claim:** in the PACE era, semi-analytical retrieval of inherent
optical properties from remote-sensing reflectance fails for identifiable
reasons, and those failures are *parameterization* failures, not *physics*
failures.  Four existing projects each carry one leg of that argument — IOPtics
(controlled diagnosis against known truth), PAB (the same failure at mission
scale against BGC-Argo), MOANA (the same question for species-level retrieval),
and the retrieve-or-bust differentiable forward model (which bounds the
forward-model error term so residuals are attributable to parameterization).

Claude does not choose the problems; they come from those projects.  The scope
is fixed, and three things are explicitly **out**: the bbp700 analysis (Allie
James's work), anything in retrieve-or-bust beyond the forward model (the RoB
team's domain), and information content as the organising frame (already a
conclusion of Prochaska & Frouin 2025).

The settled outcome of the scoping interview — thesis statement, scope,
chapter outline, the new work required, and what remains open — is recorded in
`## Report` below, and condensed in this repository's `CLAUDE.md`.  Read the
Report before starting thesis work; the thesis statement itself is adopted by
default and still awaits the advisor's explicit sign-off.

## Prompts

1. Read this file.  Execute the 1st task under "Claude/CLAUDE.md file"
2. Read this file.  Execute the 1st task under "Claude/Skills"
3. Read this file.  Execute the 1st task under "Claude/Settings"
4. Read this file.  Execute the 1st task under "Basic start up"

5. Read this file.  Execute the 1st task under "Thesis topic"
6. Read this file.  Execute the 2nd task under "Thesis topic"
7. Read this file.  Execute the 3rd task under "Thesis topic"
8. Read this file.  Execute the 4th task under "Thesis topic"

## Claude

### CLAUDE.md file

1. Please generate a basic CLAUDE.md file for this project.  Have it indicate:

    - I will perform git commands
    - If you do any calculation, generate it as a python script and write it to
      disk so that I can add it to the Repository.
    - If you need to run Python, use the "ocean14" conda environment.
    - The thesis write-up is a separate git repository at
      `~/Projects/Overleaf/Claude-PhD-Thesis` (LaTeX, UCSC `ucthesis` class).
      Same git rule applies there: I perform all git commands.

### Skills

1. Copy over the skills/ files from the `IOPtics` repository
   (`~/Oceanography/python/IOPtics/.claude/skills/` — `critical-partner` and
   `grill-me`).

### Settings

1. Copy over the settings.json file from the `IOPtics` repository
   (`~/Oceanography/python/IOPtics/.claude/settings.json`).  Copy the policy,
   not the accumulated IOPtics-specific allow entries — most of its tail
   references IOPtics scratchpad paths and test files.  The policy to keep:

    - **allow** — read-only shell (`ls`, `cat`, `grep`, `rg`, `find`, `head`,
      `tail`, `wc`, `sort`), benign file ops (`mkdir`, `touch`, `cp`, `mv`),
      read-only git (`status`, `diff`, `log`, `show`, `branch`),
      conda/pip/pytest/jupyter, and `conda run -n ocean14`.  Keep the publisher
      and Crossref/DOI `WebFetch` allow-list; add whatever domains this thesis
      actually needs.
    - **deny** — `sudo`, `rm -rf /`, `rm -rf ~`, `git push`, `git commit`,
      `git reset`, `git rebase`.
    - **ask** — `rm:*`.

2. A LaTeX build (`pdflatex`/`bibtex`, or the `Makefile` in the Overleaf
   project) will eventually be needed.  Add it to the allow-list when it is.

## Basic start up

1. Generate the basic files that one needs for a Python GitHub repository, e.g.
   a file for dependencies.  Examine the other Repositories in
   `Oceanography/python` to see how I tend to organize things.  Also, make a
   suggestion of which of their settings.json files to copy into this one.

## Thesis topic

1. The topic of this thesis is not yet recorded anywhere on disk.  Use the
   `grill-me` skill to interview me until the topic, its scope, and a chapter
   outline are settled.  We will have back and forth in the `## Q&A` section, 
   i.e. write your questions there and I will respond there.
   We will then write the outcome into the `## Report` section below
   and into `CLAUDE.md`, and rewrite `## Goals` at the top of this file to
   match.  Do no coding yet.  Use Fable if you can.  Log your work

2. Read my Answer to Q1 below.  Then ask me one or more additional questions. 
   Use Fable if you can.  Log your work

3. Read my Answers to Q2 and Q3 below.  Then continue the conversation.
   Use Fable if you can.  Log your work

4. Read my Answer to Q4 below.  I think we have chatted enough in this doc.
   Finish the conversation by writing the outcome into the `## Report` section below
   and into `CLAUDE.md`, and rewrite `## Goals` at the top of this file to
   match.  Use Fable if you can.  Log your work

## Q&A

**Q1.** When you write "a PhD thesis written by Claude", is Claude the
*candidate* or the *writer*?  Concretely: does Claude choose the research
problem (with you as advisor holding a veto), carry out original work whose
results nobody knows yet, and defend it to a standard you would sign as
committee chair — or is this a thesis-shaped account of science your group has
already done (BING/IOPtics/PAB/rob, or nenya/Info_content), or primarily a
document *about* AI doing science?  Everything downstream — topic, field,
scope, chapter count, what counts as a passing result — depends on which of
these you mean, and nothing on disk records it: the GitHub repository has
existed since at least June with an empty description, and a grep for
thesis/dissertation across all your other prompt docs and logs finds nothing.

*Recommended:* Claude as candidate, held to the real UCSC dissertation
standard — an original contribution, three or so result chapters each of
publishable quality, with negative results admissible as chapters if the
question was worth asking.  Two things on disk argue for it.  First, this
repository is built as a science package (Python package, tests, `ocean14`,
"calculations become scripts") and the task doc says this is where the science
gets done — which rules out a pure essay about AI and science, and a synthesis
of already-published work would need none of that scaffolding.  Second,
`retrieve-or-bust` already *is* the Claude-as-engine experiment, and its
application reserves problem-ownership to the humans: "the science (problem,
physics, data, and judgment of what counts as a real retrieval) stays firmly
ours."  A thesis is the one scientific artefact whose defining property is the
opposite — the candidate must own the problem.  So the thesis is the natural
complement to rob rather than a duplicate of it, and the interesting test is
whether Claude has the judgment to *pick* a problem, not just solve one it is
handed.  The meta-question — what it means for an AI to do this — belongs where
it belongs in any thesis: the introduction and the concluding chapter, not as
the topic.

What that commits you to: acting as advisor and committee, which means reading
and rejecting chapters and deciding when a proposed problem is too easy, too
derivative of your group's work, or unjudgeable by you; keeping the field inside
your competence (ocean colour or astronomy) so you *can* judge it; giving Claude
access to data; and accepting that the timescale is months of sessions, not
years, so the scope must be chosen accordingly.

**A1.** . Yes, that's correct.  As for picking the problem, Claude will not. Instead, because Claude was the primary creator (with me as advisor) of the PAB, RoB, and IOPtics projects,
they will form the bulk of its thesis.

**Q2.** A1 says PAB, RoB and IOPtics "will form the bulk" because Claude was
their primary creator.  But on disk none of the three is finished science and
none has a manuscript — `~/Projects/Overleaf` holds no paper for any of them,
and no `.tex` exists in any of the three repositories.  `retrieve-or-bust`'s
README states outright that "the retrieval itself — the inversion — does not
exist yet" (line 83); what exists is the differentiable forward model in
`robust/rt/`, written up in two team reports by "J. Xavier Prochaska and Claude
(Fable 5)" dated 2026-08-15 and 08-27, and the inversion is scheduled for the
Anthropic Claude Science window that closes 2026-12-01.  IOPtics still says
"Early development"; its results are a diagnosis of *why* BING fails on GLORIA
(`reports/gloria_fits_report.md` — the power-law `b_bp` runs out of backscatter
in the red) and a MOANA reimplementation whose full reproduction is blocked on
PML data (`reports/moana_blocked.md`, dated today).  PAB has a complete data
product (`pab_version = 1.0`, 14,610 matchups, 14,609 fits, finished 2026-08-20)
and two internal reports from 09-07 and 09-10 — but its headline bbp700 finding
(PACE high in 84% of matchups, median +0.35) was produced by a student
collaborator on the 273-matchup `run1k` set, not the full run.  So this is not a
write-up of work already done.  It is a thesis whose results mostly still have
to be produced, inside projects whose problems, priorities and acceptance gates
are set by your numbered prompts.  What, then, is the *thesis* — the single
claim the three chapters jointly establish that no one of them establishes
alone — and which results must exist by the defense that do not exist today?

*Recommended:* Make the thesis a question about the information content of
hyperspectral Rrs: how much of the IOP inversion PACE actually supports, and how
one knows.  The three projects then become three tests of one claim rather than
three stapled packages.  IOPtics measures where current algorithms fail and why
(the red-backscatter wall; MOANA's picoeukaryote skill transferring to held-out
hyperspectral data while *Pro*/*Syn* do not).  RoB establishes the forward-model
floor — 0.30% rRMS held-out on L23, 2.3× better than the O25 benchmark — below
which retrieval error belongs to the inversion rather than to the physics.  PAB
is validation against in-situ truth at mission scale: bbp700 high by ~35%, and a
Chl-a bias that changes sign near 0.1–0.2 mg m⁻³.  What turns that into a
dissertation rather than a compilation is a fourth, *new* chapter that only
someone holding all three could write: test whether PAB's bbp700 excess is a
retrieval artefact of `ExpBPow`'s power-law `b_bp` under the Gordon model —
precisely the failure mode IOPtics diagnosed and the one `robust.rt` was built
to remove — by re-inverting a PAB subset with the RoB forward model.  That
analysis is concrete, falsifiable, a few months of work, and nobody knows its
answer.  Leave `Info_content` and `nenya` out; they are the self-supervised arc,
a different thesis, and would dilute the claim.

What that commits you to: RoB's chapter is the *forward model*, not the
inversion — the inversion belongs to the seven-person team and its promised
methods paper, and the thesis must not claim it in advance; the synthesis needs
the PAB MCMC chains (~18 GiB on `s3://pab`) and `robust.rt` wired into BING as a
likelihood, which is code nobody has written; and the defense date floats with
the Dec 1 cohort, since chapters can be drafted from what exists but the thesis
claim cannot be defended until the synthesis has run.

**A2.** I agree, we should mine science out of the existing projects.  Here is what is *not* in scope:
   - The bbp analysis.  That is Allie James's work, and we should not claim it as our own.
   - Anything in RoB beyond the forward model.  That is the domain of the RoB team, and we should not claim it as our own.
   - Be mindful as regards Information Content, that this was a primary conclusion of the BING paper by Prochaska & Frouin.  I'm not sure there is much more to say there

So, here are things for us to consider including:
   - Chl-a and CDOM matchups between PACE and BGC-Argo.  This is already done and posted on s3://pab
   - Any/all of the results in IOPtics
   - The intrinsic value of the RoB forward model.  It is not a scientific result, but it is common for a thesis to contain at least 1 methods Chapter

**Q3.** *(Independent of Q2 — answer both.)*  Every design document and report
reads "Authors: JXP and Claude"; PAB carries Allie James's `run1k` bbp700
analysis and hard-coded paths from her account; RoB has Henry Houskeeper's
commits and a seven-person team (Bontemps, Dierssen, Houskeeper, Frouin,
Kavanaugh, Kudela, Prochaska) whose application says the science "stays firmly
ours."  A dissertation normally requires the candidate to be the primary
contributor to what is claimed, plus a statement covering co-authored material —
worth checking against the current UCSC Graduate Division guidelines, which I
have not read.  What is the rule for what a chapter may claim as Claude's, and
does the RoB team know a Claude thesis will draw on their project?

*Recommended:* Claim the code and the analyses Claude executed; attribute the
problem statements and every acceptance decision to you.  That is the honest
reading of the prompt-doc/Q&A record, which is an unusually complete provenance
trail and should itself be cited as the evidence of who did what — few human
theses can document authorship this precisely.  Treat the student's `run1k`
result as prior work to be cited, not as a chapter result, and re-derive the
bbp700 statistic on the full 14,610-matchup run so the chapter's number is
Claude's own.  Tell the RoB team now, before a chapter exists, rather than at
submission.

**A3.** I'm not worried about this given what I wrote in A2

**Q4.** A2 answered Q2 by striking both halves of it and handing back a list:
the PACE–Argo Chl-a and CDOM matchups ("already done and posted on s3://pab"),
"any/all of the results in IOPtics," and the RoB forward model as a methods
chapter.  Every item on that list exists on disk today.
`pab_chl_matchups_report.md` (2026-09-07, on the full production run,
`pab_version = 1.0`, 9,814 matchups) already has fourteen figures and an
Interpretation section — it is a paper, not a chapter waiting to be written.
`report_rt_elastic_model.md` and `report_rt_inelastic_model.md` (v1.0, August)
already report 0.30% held-out rRMS.  `MOANA_Claude_Report.md` is at rev 4.
One item on the list is thinner than it sounds: "any/all of the results in
IOPtics" is, in sweep terms, a single cross-algorithm page —
`docs/source/reports/expb_giop_L23_test20`, generated 2026-07-03, twenty
spectra, two algorithms — against an L23 benchmark of 3,320 water bodies with
exact noise-free truth and a model suite that includes `expb_pow2flat` and
others never swept.  The framework is built; the comparison it was built for
has not been run.  What A2 did not supply is the one thing Q2 said was missing:
a claim these three defend together.  As it stands the thesis is a compilation
of finished work by a candidate who, by your own exclusions, may not do the bbp
analysis, may not touch RoB beyond the forward model, and should not lean on
information content.  So the question is twofold, and I want an answer to both
halves rather than to one.  First, what is the sentence a reader takes away
from this dissertation that none of the three reports says alone?  Second, what
new work does Claude do — work whose result is not currently known to anyone,
including you — such that the thesis is a contribution and not a binding?

*Recommended:* Make the thesis about **where and why semi-analytical IOP
retrieval breaks in the PACE era**, with the argument that the failures are
parameterization failures, not physics failures — and let each project carry
one leg of that argument.  IOPtics is the controlled diagnosis:
`gloria_fits_report.md` shows BING's single power-law `b_bp` runs out of
backscatter in the red on turbid GLORIA water (~0.2–0.4 m⁻¹ needed versus
~0.013 fitted), and the MOANA work shows which taxa survive transfer to
hyperspectral data and which do not.  PAB Chl-a is the same class of failure at
mission scale against independent truth: a bias that flips sign across the
concentration range (+0.65 to −0.8 by octile) with matchup geometry and PACE
quality ruled out as causes, leaving the retrieval.  The RoB forward model is
what makes the attribution clean — at 0.30% rRMS the forward-model error term
is gone, so whatever residual remains belongs to the parameterization or the
inversion.  The new work is exactly what the Chl report already proposes on its
own last page: synthetic BING fits at controlled `Adg` to test whether
CDOM/detrital absorption aliases into the Bricaud phytoplankton term (the
ρ = −0.24 correlation is "a candidate worth testing further … not an
established cause"), and ingesting `SCIENTIFIC_CALIB_*` so the raw-versus-
adjusted Argo question — which alone moves the median bias from +0.13 to +0.58
— is settled rather than footnoted.  Running the full L23 sweep across the
whole model suite is the third piece, and it is nearly free.  All three sit
inside every exclusion in A2, all three are concrete, and none has a known
answer.  CDOM does not make this cut: `pab_cdom_matchups_report.md` is titled
"Qualitative/Correlative" by its own author, is rank-correlation only, and
rides on raw fluorometer data carrying an unapplied 5.62× Sea-Bird adjustment.
It is a section of the PAB chapter unless the RAF is applied and the comparison
redone quantitatively.

What that commits you to: accepting that the three existing reports become
evidence chapters, not the contribution itself; funding genuinely new work — a
synthetic-fit experiment in IOPtics, the full L23 sweep, and a PAB ingestion
change to carry calibration provenance — with the real possibility that the
aliasing hypothesis is falsified and the Chl chapter's mechanism section has to
be rewritten; and letting the RoB forward model be judged as a methods chapter
on its unresolved edges (solar-zenith extrapolation at 4.7–12.2%, the
unvalidated M5 CDOM fluorescence) rather than presented as finished.

>A. There is much more to IOPtics than you have found.  Most of that work has been done on my workstation.  And there is also the MOANA analysis, which I am about to spin off into its own Repo.

## Report

### Thesis statement

The dissertation defends one claim: **in the PACE era, semi-analytical retrieval
of inherent optical properties from remote-sensing reflectance fails for
identifiable reasons, and those failures are parameterization failures, not
physics failures.**  IOPtics supplies the controlled diagnosis against synthetic
and in-situ corpora where the truth is known; the PACE–BGC-Argo matchups show
the same class of failure at mission scale against independent in-situ
measurements; the differentiable radiative-transfer forward model removes the
forward-model error term so that residual retrieval error can be attributed to
the parameterization rather than to the physics; MOANA tests the same question
one level up, where the retrieved quantity is a cell abundance rather than an
IOP.

**Status of this statement: adopted by default, not ratified.**  It was proposed
in round 3 (Q4) as the through-line binding an otherwise disconnected set of
finished results.  The advisor's closing answer (A4) corrected a round-3 finding
about the extent of IOPtics work and added MOANA, but did not explicitly endorse
or reject the through-line.  It is the only thesis statement on the table and
the interview closed without objection to it, so subsequent sessions should work
under it — but it has no written sign-off, and obtaining one is the first item
under Open questions below.  Do not represent it as agreed.

### Standard and role

Claude is the PhD candidate, held to a real UCSC dissertation standard: original
contribution, defended in front of a committee, with negative results
admissible.  J. Xavier Prochaska is advisor and committee chair.

Claude does not choose the research problems.  They come from existing projects
that Claude was primary creator of with Prochaska as advisor — PAB, the RoB
forward model, IOPtics, and (per A4) MOANA.  The advisor holds a veto over scope,
and has exercised it (see Scope).  Every project runs on BING (Bayesian
INferences with Gordon coefficients; Prochaska & Frouin 2025, Biogeosciences 22,
4705), a Bayesian semi-analytical IOP retrieval whose first commit (2024-06-04)
predates Claude's involvement.  BING is the inherited foundation and is not a
thesis contribution.

The question of what it means for an AI to be the candidate is a legitimate one,
but it belongs in the Introduction and the Conclusions only.  It is not the
subject of any science chapter and must not be allowed to leak into them.

### Scope

**In scope**, as stated by the advisor:

- The PACE–BGC-Argo Chl-a and CDOM matchups (PAB).
- "Any/all of the results in IOPtics," including the substantial body of work
  that exists only on the advisor's workstation (A4).
- The RoB differentiable radiative-transfer forward model, as a methods
  chapter — in his words "not a scientific result, but it is common for a thesis
  to contain at least 1 methods Chapter."
- The MOANA analysis, about to be spun off into its own repository (A4).

**Explicitly out of scope**, with the advisor's reasons.  Future sessions must
not develop, extend, or claim any of these:

- **The bbp700 analysis** (PACE vs Argo bbp700, 84% / median +0.35, on the
  273-matchup `run1k` subset).  "That is Allie James's work, and we should not
  claim it as our own."  The PAB Chl-a report's finding that Chl and bbp700
  biases are uncorrelated (rho = 0.09) may be cited as a boundary condition — it
  establishes that the Chl-a mechanism is distinct — but the bbp700 result
  itself is hers.
- **Anything in RoB beyond the forward model.**  "That is the domain of the RoB
  team."  RoB is a seven-person collaboration (Bontemps, Dierssen, Houskeeper,
  Frouin, Kavanaugh, Kudela, Prochaska) with a promised methods paper.  Its
  inversion does not yet exist and must not be claimed in advance, anticipated
  in the outline, or described as a thesis deliverable.
- **Information content as the organising frame.**  "This was a primary
  conclusion of the BING paper by Prochaska & Frouin.  I'm not sure there is
  much more to say there."  Information-content arguments may appear as
  supporting analysis where a specific result requires them; they are not the
  thesis's frame.

On attribution the advisor is "not worried about this given what I wrote in A2" —
the exclusions above are the attribution policy.

### Chapter outline

The proposed structure.  Chapters 3–5 are the science; each carries a piece of
the through-line.

**Ch 1 — Introduction.**  The retrieval problem (a, bb, a_ph, a_dg, bb_p from
Rrs); the semi-analytical lineage from Gordon 1988 through GIOP to BING; what
PACE's hyperspectral Rrs changes; the thesis statement; and the one place the
AI-as-candidate question is addressed.  Requires new writing; no draft exists.

**Ch 2 — Methods: a differentiable radiative-transfer forward model.**  From
`reports/report_rt_elastic_model.md` (v1.0, 2026-08-15) and
`report_rt_inelastic_model.md` (v1.0, 2026-08-27).  Hybrid ZTT plus a
417-parameter MLP in JAX; 0.30% rRMS on held-out water bodies, uniform across
350–750 nm; 2.3x better than the O25 semi-analytical benchmark and 24x better
than Gordon 1988; exact gradients; Raman scattering and Chl-a fluorescence in
the inelastic extension.  The chapter's role in the argument is to bound the
forward-model error term so that Chapters 3 and 5 can attribute residuals to
parameterization.  It must own its edges: extrapolation to unseen solar zenith
degrades to 4.7–12.2%, and CDOM fluorescence (milestone M5) is landed but
unvalidated and off by default.  Stops at the forward model.  **Draft-able
today.**

**Ch 3 — IOPtics: where semi-analytical retrieval breaks.**  Benchmarking BING
and comparison algorithms against L23 (Loisel et al. 2023; 3,320 Hydrolight
water bodies with exact noise-free truth), PANGAEA/Valente et al. 2022, and
GLORIA/Lehmann et al. 2023.  The committed evidence is
`reports/gloria_fits_report.md` — the single power-law bb_p runs out of
backscatter in the red on turbid GLORIA water (roughly 0.2–0.4 m^-1 needed vs
~0.013 fitted), a clean example of a parameterization failure — plus two sweep
pages (`expb_giop_L23_test20`, twenty spectra, two algorithms, 2026-07-03;
`gloria_turbid_v3`).  Per A4 this substantially understates the work; most of it
is on the advisor's workstation.  **Partly draft-able; final shape depends on
what migrates from the workstation and on the full L23 sweep.**

**Ch 4 — MOANA: species-level retrieval and the limits of hyperspectral
transfer.**  From `reports/MOANA_Claude_Report.md` (rev 4, 2026-08-17): an
independent reimplementation of NASA's MOANA algorithm for *Prochlorococcus*,
*Synechococcus*, and autotrophic picoeukaryote abundances from hyperspectral
Rrs; 299-test suite; Lange's Table 1 reproduced from scratch in the CTD-only
configuration; a disputed PC-mapping question settled empirically; and the first
held-out hyperspectral skill numbers — picoeukaryote skill transfers to held-out
hyperspectral data, *Prochlorococcus* and *Synechococcus* skill does not.  This
is a parameterization-transfer result and fits the through-line directly.
**Draft-able today as a reimplementation-and-transfer chapter.**  The full
retrain is blocked (`reports/moana_blocked.md`, 2026-09-12) on AMT24 underway
flow-cytometry data held at PML; the chapter is written to stand without it, and
the retrain is recorded as future work unless the data arrive.

**Ch 5 — PAB: validation at mission scale.**  From
`reports/PAB/pab_chl_matchups_report.md` (2026-09-07) on the
`pab_version = 1.0` database (881 floats, 54,031 profiles, 14,610 matchups,
14,609 successful ExpBPow fits; 9,814 valid Chl-a matchups).  PACE Chl-a exceeds
Argo in 58% of matchups, median relative difference +0.13, rank skill rho = 0.78
— but the bias changes sign with concentration (octile medians ~+0.65 at the
lowest Chl-a to ~−0.8 at the highest), so no single bias statement describes the
population.  Matchup geometry and PACE data quality are ruled out as drivers.
The chapter carries two pieces of new work (below): the synthetic-`Adg` aliasing
experiment and the Argo calibration-provenance ingest.  CDOM enters as a
**section**, not a chapter: `reports/PAB/pab_cdom_matchups_report.md` (v1.0,
2026-09-10) is explicitly qualitative — Spearman rank only, on raw fluorometer
values carrying an unapplied Sea-Bird Reference Adjustment Factor of 5.62 — and
stays a section unless the RAF is applied and the comparison redone
quantitatively.  The bbp700 result is excluded.  **Draft-able today for the
descriptive validation; the new work turns it from description into diagnosis.**

**Ch 6 — Conclusions.**  What the four chapters establish jointly about where and
why semi-analytical retrieval fails; what the differentiable forward model makes
possible without claiming the RoB inversion; open problems; and the second and
final place for the AI-as-candidate reflection.  Requires new writing.

Summary of state: Chapters 2 and 4 exist in draft-able form; Chapter 5's
descriptive half does; Chapter 3 is the least complete in the repository and the
most dependent on migration; Chapters 1 and 6 do not exist.

### New work required

A compilation of finished reports is not a dissertation.  Three concrete pieces
of work turn the outline into one.  Each is in scope under every exclusion in the
Scope section, each is on the through-line, and none has a known answer.

**1. The synthetic-`Adg` aliasing experiment (Ch 5, feeds Ch 3).**  The Chl-a
report finds bias correlating negatively with fitted `Adg` amplitude
(rho = −0.24), "consistent with CDOM/detrital absorption aliasing into the
Bricaud phytoplankton term at high Adg, suppressing the Chl retrieval there."
The report itself flags this as needing a test with synthetic BING fits at
controlled `Adg`.  If BING on synthetic spectra of known a_ph and a_dg
reproduces the sign-changing bias, the PAB result becomes a parameterization
diagnosis and the strongest single piece of evidence for the thesis statement.
If it does not, the hypothesis is falsified and the mechanism is elsewhere — a
publishable negative result, and the chapter stays honest.

**2. Ingesting `SCIENTIFIC_CALIB_*` to settle the Argo ground truth (Ch 5).**
Switching from raw to delayed-mode-adjusted Argo Chl-a moves the median relative
difference from +0.13 to +0.58 (median adjusted/raw ratio 0.46); DAC-of-origin
correlates with bias strength (+0.06 AOML vs +0.25 elsewhere).  PAB cannot
currently tell which correction a given DAC applied because the
`SCIENTIFIC_CALIB_*` metadata are not ingested.  Until they are, the in-situ
reference is the largest single ambiguity in the chapter and the headline bias
number is not defensible in front of a committee.  This is data-engineering work
with a scientific payoff: it decides which population the validation is against.

**3. The full L23 cross-algorithm sweep (Ch 3).**  The committed sweep is twenty
spectra and two algorithms.  The chapter needs BING and its comparison
algorithms run over all 3,320 L23 water bodies with truth-referenced error
decomposed by component (a_ph, a_dg, bb_p) and by water type, so that the GLORIA
turbid-water failure can be placed in a population rather than shown as a case
study.  **Subject to what already exists on the advisor's workstation** — this
may be largely done and require migration rather than computation; that must be
established before any new runs are launched.

### Dependencies and risks

- **Uncommitted IOPtics work.**  Per A4, most of the IOPtics analysis lives on
  the advisor's workstation, not in the repository.  Nothing uncommitted can be
  cited in a dissertation.  Migration of those artefacts (scripts, outputs,
  figures, with provenance) into the repository is a prerequisite for Chapter 3
  and for scoping item 3 above.  This is a provenance dependency, not a gap in
  the science, but it gates the least-complete chapter.
- **MOANA repository spin-off.**  MOANA is about to move to its own repository.
  Chapter 4 must cite the new location; until the spin-off lands, paths in
  `reports/MOANA_Claude_Report.md` and `reports/moana_blocked.md` are
  provisional.
- **MOANA full retrain blocked** on AMT24 underway flow-cytometry data at PML.
  Chapter 4 is scoped to stand without it.  If the data arrive, the retrain is an
  upgrade, not a rescue.
- **The aliasing hypothesis may be falsified.**  Item 1 is a real experiment.
  Its failure would weaken but not break the through-line (Chapter 3's GLORIA
  bb_p failure is independent evidence), and would be reported as such.
- **CDOM stays qualitative** unless the Sea-Bird RAF of 5.62 is applied to
  fluorometers calibrated or serviced before 2023-01-13 and the comparison
  redone.  Without that, it is a section describing a rank correlation and
  nothing more.
- **The RoB forward/inversion boundary.**  The forward model is Claude's to
  claim; the inversion belongs to the seven-person RoB team.  Chapter 2 and
  Chapter 6 must be written so that no reader infers the inversion is a thesis
  deliverable.  This boundary is easy to cross by accident in a conclusions
  chapter and should be checked explicitly at draft time.
- **Forward-model edges.**  Solar-zenith extrapolation (4.7–12.2%) and
  unvalidated CDOM fluorescence limit what Chapter 2 can be used to bound in
  Chapters 3 and 5; the bound holds within the trained domain and must be stated
  as such.
- **Write-up location.**  The thesis LaTeX lives at
  `~/Projects/Overleaf/Claude-PhD-Thesis` (UCSC `ucthesis` class,
  Overleaf-synced) and is still the stock template with inherited boilerplate.
  Science stays in `~/Projects/claudes-phd-thesis`.  Both repositories follow the
  same rule: the advisor performs all git operations.

### Open questions for the advisor

- **Ratify or replace the thesis statement.**  The through-line above is adopted
  by default; it needs a written yes, an amendment, or an alternative.
- **Confirm the chapter list**, in particular whether MOANA is its own chapter
  (Ch 4, as proposed) or a section elsewhere, and whether the forward-model
  methods chapter should precede or follow the IOPtics chapter.
- **What exists on the workstation.**  An inventory of the uncommitted IOPtics
  work, so that item 3 under New work can be scoped as migration versus
  computation, and Chapter 3 can be planned against real rather than visible
  evidence.
- **Timeline and defense expectations.**  No dates, milestones, committee
  composition beyond the chair, or expectations for a qualifying/advancement
  step have been set.
- **CDOM.**  Whether applying the 5.62 RAF and redoing the comparison
  quantitatively is wanted within the thesis, or whether CDOM remains a
  qualitative section.

## Logging

The "Logs" section will record Claude's work.  Please use the following format:

### <Date> (Short summary of the work)

<Detailed description of the work and what you learned>

...

## Logs

### 2026-09-08 (Bootstrapped this start_up.md from the house pattern)

Executed the original prompt #1 of this file, which read: *"Read the
`claude_start_up.md` file in `~/bin/claude_prompts` and follow the guidance
there to start up the project.  Use Opus 5."*  That guidance is a synthesis of
the `start_up.md` docs across `~/Oceanography/python/{cugn, cugn-climatology,
victor-class, retrieve-or-bust, PAB, IOPtics, OETHER}`, and its §6 is a
checklist for a new repository.  This file is now the result of that checklist,
so the bootstrap prompt has been replaced by the canonical numbered prompts
above.  Ran §6 items 1–6 only; item 7 ("then run the numbered prompts one at a
time, logging each") is left to subsequent sessions, per the convention that
each numbered prompt gets its own session.

**What the repository was.** A `README.md` containing only `# claudes-phd-thesis`,
this `claude_prompts/` directory, one commit (`71557b8 first commit`), on branch
`start-up`.  No `.claude/`, no `CLAUDE.md`, no Python package, no dependency
file.

**What was learned.** The thesis subject is not written down anywhere I could
find.  What is on disk: `~/Projects/Overleaf/Claude-PhD-Thesis`, created the
same minute as this repository, is a fresh clone of the UCSC `ucthesis` LaTeX
template — stock template files plus an example thesis (`uctest.tex`, a blazar /
`CRPropa` astro-particle document) that came with it, i.e. not this thesis's
content.  So the shape of the project is a code repository here and a LaTeX
write-up there, which is the two-repo arrangement `cugn-climatology` uses with
`cugn`, and the reason the `CLAUDE.md` task above carries a cross-repo pointer.

**Decisions and why.**

- Ordering is `CLAUDE.md` → `Skills` → `Settings` → `Basic start up`, the most
  common of the seven and the one `OETHER` uses.  Only "`CLAUDE.md` first" is
  actually fixed across the family.
- The `CLAUDE.md` task uses the fuller four-directive form (git-is-Xavier's,
  calculations-as-scripts, `ocean14`, sibling-repo pointer) rather than the
  git-only form in `IOPtics`/`PAB`/`retrieve-or-bust`, since the guidance names
  the fuller version as the one to copy going forward.  It says *generate*, not
  *update*, because no stub exists yet.
- `ocean14` is kept as the Python environment even though this repository sits
  in `~/Projects` rather than `~/Oceanography/python` — it is the house
  invariant.  Worth changing if this thesis needs its own environment.
- Added a `## Thesis topic` section and an empty `### Report` header, which are
  not in the standard skeleton.  Precedent: `PAB` substitutes a live problem
  (`Dependencies`) for one of the standard prompts, so the numbered list is
  meant to absorb the immediate need — and here the immediate need is that
  nobody has written down what the thesis is about.  It points at `grill-me`
  and says to do no coding yet, following the investigate-then-edit pattern.

**Flagged for Xavier to confirm.**

1. `## Goals` above is my inference from the directory layout, not from anything
   you wrote.  It says what the repository *is for structurally* (code here,
   LaTeX there) and deliberately says nothing about the subject.  Rewrite it
   once prompt #5 settles the topic — the guidance warns specifically against
   leaving a copied-in Goals block (`cugn`'s is stale and describes a different
   project entirely).
2. Whether prompt #5 should instead run *first*.  Everything under `Basic start
   up` — package name, layout, dependencies — depends on knowing what the
   thesis does, and `~/Projects/claudes-phd-thesis` has no package name implied
   by convention the way `ioptics`/`pab`/`robust` did.
3. Whether `ocean14` is right here (see above).

**Git.** No git commands that change repository state were run.  Read-only
`git status` and `git log` only.  Note that `claude_prompts/start_up.md` was
already staged with its old one-line content and is now modified again in the
working tree; stage and commit at your discretion.

### 2026-09-08 (Generated CLAUDE.md)

Executed prompt #1 — the 1st task under "Claude/CLAUDE.md file".  Created
`CLAUDE.md` at the repository root with all four requested directives: git is
Xavier's (read-only git permitted), calculations become Python scripts on disk,
Python runs in the `ocean14` conda environment, and a Related Repositories
pointer to the thesis write-up.  Added one directive not in the task text — a
Logging bullet, since the log convention is what carries repo knowledge between
sessions and nothing else in the repository stated it.

**What was learned.** Read the sibling `CLAUDE.md` files in `cugn-climatology`,
`OETHER`, and `victor-class` to match house style: a one-line preamble, a short
`## Project Overview`, a `## Working Conventions` (or `## Working Rules`) list of
bullet directives, and — only in `cugn-climatology` — a
`## Related Repositories` block.  They are deliberately short;
`cugn-climatology` was the closest model since this repository has the same
two-repo coupling.  The directives are also softened consistently in the
realized files: the bare "I will perform git commands" becomes "do not run git
commands that change repository state; read-only git is fine", and the `ocean14`
directive gains the concrete `conda run -n ocean14 python script.py` form.  Both
softenings are carried here.

Verified the cross-repo pointer rather than inferring it:
`~/Projects/Overleaf/Claude-PhD-Thesis` has remote
`https://git@git.overleaf.com/6aa019f318d925d963eef3ee` and a single commit
`d611a28 Update on Overleaf.` — so it is a genuine Overleaf-synced git
repository, and `CLAUDE.md` says so.

Also learned the log-ordering convention, by checking the multi-entry logs in
`~/bin/claude_prompts/CLAUDE.md` and IOPtics' `coding_prompts_stage0N.md`:
entries run **oldest first and are appended at the bottom**.  This entry was
initially written above the bootstrap entry and has been moved.

**Worth noting.** The git rule is currently prose-only.  In the sibling repos it
is *also* enforced by `.claude/settings.json`'s deny list, and this repository
has no `.claude/` directory yet — that arrives with prompt #3.  Until then
nothing mechanically prevents a `git commit` here.

**Git.** No git commands that change repository state were run.  Read-only
`git remote -v` and `git log` only (the latter against the thesis repository).
`CLAUDE.md` is new and untracked; stage and commit at your discretion.

### 2026-09-12 (Copied the IOPtics skills)

Executed prompt #2 — the 1st task under "Claude/Skills".  Created
`.claude/skills/` with `critical-partner/SKILL.md` and `grill-me/SKILL.md`,
copied from `~/Oceanography/python/IOPtics/.claude/skills/`.  Both are
byte-identical to the source (verified with `diff`), and those two files are the
entirety of IOPtics' skills tree — nothing was left behind.

**What was learned.** Read both skills before copying, to check whether either
carried IOPtics-specific content that would need adapting.  Neither does: both
are written against "the user" and "the codebase" generically, with no ocean
optics or IOP references anywhere, so a verbatim copy is the right move.  This
is consistent with the guidance calling IOPtics the upstream source of truth for
skills — they were authored to be repo-agnostic.

Worth knowing about their content, since both matter for a thesis project:
`critical-partner` makes constructive disagreement the default (surface an
untested assumption before agreeing, argue the strongest opposing case first,
retreat only on new evidence rather than on pushback, review weaknesses first,
never manufacture a flaw, end on a question rather than a summary) and
explicitly bans flattery openers.  `grill-me` is much shorter: interview one
question at a time down each branch of the design tree, always offer a
recommended answer, and explore the codebase instead of asking anything the
codebase can answer.  Prompt #5 ("Thesis topic") calls for `grill-me`, so it is
now available.

**Flagged for prompt #4.**  Checked how the siblings treat
`.claude/settings.local.json`: in IOPtics, `git ls-files .claude` shows
`settings.json` and the two `SKILL.md` files tracked, and `settings.local.json`
untracked — but it is *not* in `.gitignore` (none of IOPtics, OETHER,
`cugn-climatology`, or PAB mention `.claude` there).  It stays out of the
repository by never being staged, not by rule.  When prompt #4 generates the
`.gitignore` here, add `.claude/settings.local.json` explicitly rather than
inheriting that gap.

**Git.** No git commands that change repository state were run.  Read-only
`git ls-files` only.  The new `.claude/skills/` files are untracked; stage and
commit at your discretion.

### 2026-09-12 (Copied and pruned the IOPtics settings.json)

Executed prompt #3 — the 1st task under "Claude/Settings".  Wrote
`.claude/settings.json`, carrying over the IOPtics policy and pruning the
accumulated IOPtics-specific entries.  Verified the result parses as JSON and
diffed it entry-by-entry against the source: 41 allow / 8 deny / 1 ask.

**Dropped (8 allow entries, all IOPtics-specific).** Two `curl` calls naming one
literal DOI and one literal bibliographic query; two `python3 -c` Crossref JSON
parsing one-liners; two `pytest` invocations hard-coded to absolute interpreter
paths (one `/home/xavier/miniconda3/...` from the Linux box, one
`/Users/xavier/miniforge3/...` from this one); one `python -c` importing `bing`;
and one `grep` against a specific IOPtics report file.  These are exactly the
accreted tail the guidance warns about — every one of them is a permission some
past session asked for mid-task and that stuck.

**Added (4 allow entries, all generalizations of what was dropped).**
`WebFetch(domain:api.crossref.org)` and `Bash(curl -s "https://api.crossref.org:*)`
replace the two literal Crossref lookups, so literature checking works here
without re-prompting for each DOI.  `Bash(git ls-files:*)` and
`Bash(git remote -v)` extend the read-only git set — both were used in earlier
prompts of this start-up and both are read-only.

**One deliberate deviation from the task text, please confirm or revert.**  I
added `Bash(git add:*)` to the **deny** list.  It is not in the IOPtics policy
and not in the enumerated deny list in the task above, so it is a departure.
The reason: `git add` changes repository state, `CLAUDE.md` says Claude must not
run git commands that change repository state, and the deny list is the
mechanism that enforces that prose.  Without it, staging is the one state-changing
git operation the settings file still permits.  Erring toward the restrictive
side seemed right, but it is your call — delete the line if you want this
repository byte-faithful to the IOPtics policy.

**Not added, per the task text.**  Nothing for LaTeX.  Task item 2 says to add
`pdflatex`/`bibtex`/`Makefile` permissions "when it is" needed, not now, so the
allow-list stays clean until the thesis actually builds.

**What was learned.** The `$schema` key is the only non-`permissions` key in the
IOPtics file, so the policy really is just the three lists.  Also worth naming:
the git rule is now enforced here for the first time — before this prompt it was
prose in `CLAUDE.md` only, as noted in the 2026-09-08 entry.

**Housekeeping.** While this prompt was running you reworked `## Thesis topic`
— the interview now routes through a `## Q&A` section (your answers written
there rather than in chat), `### Report` was promoted to `## Report`, and the
task asks for Fable.  That section is still not referenced from `## Prompts`,
which ends at #4 ("Basic start up"), so no numbered prompt currently points a
session at it.  Add the line back when you want it run.

**Git.** No git commands that change repository state were run.  `.claude/settings.json`
is new and untracked; stage and commit at your discretion.

### 2026-09-12 (Basic Python repository scaffolding)

Executed prompt #4 — the 1st task under "Basic start up".  Surveyed the six
sibling repositories with a `claude_prompts/` directory, then created:
`setup.py`, `requirements.txt`, `pytest.ini`, `.gitignore`, `LICENSE`, a
rewritten `README.md`, and the package `claudes_phd_thesis/` with
`__init__.py` and `tests/__init__.py`.

**What the house layout actually is.** The reliable core across IOPtics,
OETHER, `cugn-climatology`, PAB, `retrieve-or-bust`, and `victor-class`:
`<package>/` (snake_case), `claude_prompts/`, `CLAUDE.md`, `README.md`,
`LICENSE`, `requirements.txt`, `setup.py`, `.gitignore` — and **no
`pyproject.toml` in any of them**.  `pytest.ini` appears in
`cugn-climatology`, PAB, and `victor-class`; it is four lines
(`testpaths = <pkg>/tests`, `python_files = test_*.py`, `addopts = -ra`) and
was copied as such.  Everything past that core is per-project
(`docs/`, `reports/`, `papers/`, `data/`, `notebooks/`, `context/`).

`setup.py` is not generic boilerplate — it is a specific house template: build a
`setup_keywords` dict field by field, read `README.md` into `long_description`
if it exists, `provides`, `python_requires='>=3.12'`, `zip_safe=False`,
`find_packages()`, and a trailing `if os.path.isdir('bin')` block that sweeps
`bin/*` into `scripts` (skipping `.rst`).  Copied verbatim, with only the name,
description, and dependency list changed.  `requirements.txt` mirrors
`install_requires` and says so in a header comment, the way
`cugn-climatology` does.

**Decisions.**

- Package name `claudes_phd_thesis` — your call when I asked.  It follows the
  mechanical convention (`cugn-climatology` → `cugn_climatology`,
  `victor-class` → `victor_class`), though `retrieve-or-bust` → `robust` shows
  the topic sometimes wins instead.  Renaming later is cheap while the package
  is empty.
- `LICENSE` copied from OETHER, the one sibling whose BSD-3 copyright holder is
  you personally rather than a GitHub org — also your call.  The others read
  `ocean-colour` (IOPtics, `victor-class`, PAB, `retrieve-or-bust`) or
  `Sea-Meets-the-Stars` (`cugn-climatology`), i.e. the holder tracks the org
  that hosts the repository.  `setup_keywords['url']` is therefore an empty
  string with a `TODO`, since no GitHub remote exists for this repository yet.
- Dependencies are the core scientific stack only — numpy, scipy, pandas,
  matplotlib, seaborn, scikit-learn, tqdm, IPython, pytest — which is the
  intersection of what every sibling installs.  The domain half of each
  sibling's list (`gsw`/`xhistogram`/`dask` for gliders, `emcee`/`corner`/`bing`
  for retrievals) has no analogue here until the topic is settled.  Both files
  carry a comment saying so and pointing at the "Thesis topic" prompt.
- Acted on the `.gitignore` flag from the 2026-09-12 skills entry: copied
  IOPtics' 222-line `.gitignore` and added `.claude/settings.local.json` under
  its own comment.  No sibling ignores that file; they rely on never staging it.

**The settings.json suggestion** (second half of the task; prompt #3 already
copied IOPtics').  Confirmed IOPtics was the right source, and the comparison is
more decisive than expected: **all six sibling `settings.json` files have
byte-identical `deny` and `ask` lists** (the same seven denies, the same single
`Bash(rm:*)` ask).  The only thing that varies is how much the `allow` list has
accreted — `cugn-climatology` 33, OETHER and PAB 36, IOPtics and `victor-class`
45, `retrieve-or-bust` 50.  So the choice of source barely matters for policy;
it only decides how much cruft you inherit.  Two checks on the pruned file
written in prompt #3: every one of `cugn-climatology`'s 33 entries is already in
it (it is a strict superset of the leanest sibling), and no sibling has a single
LaTeX, `make`, or `.pdf` permission — none of them build a document, so there is
no house precedent to copy when the Overleaf half of this project starts
building.  `cugn` is the one repository with no `.claude/` at all.

**Verification.**  Ran in `ocean14`: `setup.py` parses, `import
claudes_phd_thesis` works and reports version `0.0.dev0`, and all nine
requirements are already installed.  That environment is on Python 3.14.6, so
the inherited `python_requires='>=3.12'` is satisfied.  (The import left a
`__pycache__/` in the package; it is covered by `.gitignore`.)

**Git.** No git commands that change repository state were run — `git status`,
`git log`, `git ls-files`, `git check-ignore`.  Note that you committed in the
middle of this prompt (`f68792e wip`, `84f1ff0 mo`): every file from prompts #1
through #4 is now tracked and the working tree is clean, so nothing is left
outstanding to stage.

### 2026-09-12 (Thesis topic, round 1 — Q1 posed)

Executed prompt #5 — the 1st task under "Thesis topic".  Wrote **Q1** into the
`## Q&A` section and stopped there, per `grill-me`'s "ask the questions one at a
time".  No code was written; `## Report` and `## Goals` stay untouched until the
interview settles.

**On "Use Fable if you can".**  I could not: the model cannot be switched from
inside a running session, and this one is Opus 5.  What I did instead was hand
the interviewing to a Fable subagent — briefed with the repository state, the
`grill-me` rules, the Q&A protocol, and the ambiguity to attack — and keep the
file-writing and logging here.  Q1 and its recommendation are Fable's words,
lightly trimmed.  If you want a fully-Fable session, `/model fable` before
running the next round.

**What the exploration turned up** (Fable ranged over `~/Oceanography/python`,
`~/Projects`, and `~/Projects/Overleaf`; I verified the two claims that went
into Q1 as fact):

- The `claudes-phd-thesis` GitHub repository is not new.  `~/bin/claude_prompts/org_websites.md`
  shows it was already there in June and was *omitted* from the
  Sea-Meets-the-Stars org README three separate times as "no description, looks
  like a placeholder/personal repo".  The idea has been parked for ~3 months
  with nothing written.  Verified.
- Nothing anywhere else in your prompt docs mentions a thesis or dissertation —
  `grep -rIl -i "dissertation\|phd thesis"` across `~/bin/claude_prompts/` and
  every sibling `claude_prompts/` returns nothing.  Verified.  So this file
  really is the only record, which is why Q1 has to be asked before anything
  else.
- `retrieve-or-bust` is a live Claude-does-science project whose application
  reserves problem-ownership to the humans.  That is the axis a thesis would
  flip, and it is the core of Fable's recommendation.  (Reported by the
  subagent from the repo's own docs; I confirmed the repo is active — last
  commits `5ca740d`, `0fd2e0b`, `dfab27c`.)
- `~/Projects/Overleaf/Info_content` — "The Information Content of Marine
  Remote-Sensing Datasets", Claude-co-authored, abstract and intro still
  placeholder text, untouched since 2026-08-02 — is the obvious candidate
  chapter if the answer to Q1 turns out to be "writer/synthesis".
- You are Professor of Astronomy as well as Ocean Sciences, and the astronomy
  side is active (Keck 2027A proposals, FRB work, PypeIt) — but essentially all
  Claude-enabled tooling and data on this machine is ocean colour.  That
  asymmetry will decide the field question, not preference.

**Where the interview goes next**, recorded so the next session does not have to
re-derive it.  Q2 depends entirely on your A1:

- *Candidate* → which field, and how does the thesis stay clear of
  `retrieve-or-bust`?  (Recommendation would be ocean colour with IOP inversion
  from Rrs explicitly excluded as rob's territory, and Claude proposing three
  candidate problems for you to veto rather than you assigning one.)  Q3 would
  be timescale and committee.
- *Writer / synthesis* → which body of work: the Bayesian retrieval arc
  (BING → IOPtics → PAB → rob) or the self-supervised arc (nenya →
  Info_content)?  And may new analyses fill gaps, or is it strictly
  re-narration?
- *About AI and science* → what is the empirical object, and what is the
  evidence standard?  Without pinning that first it becomes an essay, and this
  repository's code/analyses/figures framing would be the wrong container.
- *Something else* → state it in two sentences, and say whether the `ocean14`
  Python-package premise still applies; if not, prompt #4's scaffolding should
  be reconsidered before anything else.

**Git.** No git commands that change repository state were run — read-only
`git log` against `retrieve-or-bust` and `grep` over your prompt docs.

### 2026-09-12 (Thesis topic, round 2 — Q2 and Q3 posed)

Executed prompt #6 — the 2nd task under "Thesis topic".  Read **A1**, explored
the three named projects, and wrote **Q2** and **Q3** into `## Q&A`.  No code
written; `## Report` and `## Goals` still untouched until the interview settles.
No state-changing git commands — read-only `git log` only.

**On "Use Fable if you can".**  Same constraint as round 1: the model cannot be
switched inside a running session and this one is Opus 5.  So again the
interviewing went to a Fable subagent — briefed with A1, the round-1 log, the
`grill-me` rules and the Q&A house style — while this session did the
fact-checking, the file edits and this log.  Q2 and Q3 are Fable's words with
one substantive change of mine (below).  `/model fable` before the next round
if you want a fully-Fable session.

**What A1 changes.**  Round 1 had prepared four branches; A1 takes the
*candidate* branch but removes the problem-selection question that branch
assumed, and substitutes three named projects.  That kills the planned Q2
("which field, and how does the thesis stay clear of rob?") and replaces it
with a harder one: if the candidate does not pick the problems, and the three
projects are separate packages, what makes this one dissertation?

**Evidence gathered, and what it forced into the question.**  Everything below
I verified directly on disk, independently of the subagent:

- **No manuscripts exist.**  No `.tex` in IOPtics, PAB or retrieve-or-bust, and
  `~/Projects/Overleaf/` holds only `Claude-PhD-Thesis`, `F4_2027A_LMAP`,
  `Info_content` and `NASA_Keck_2027A`.  `Claude-PhD-Thesis` is still the stock
  `ucthesis` template — its `nomenclature.tex` is inherited boilerplate from
  someone's Fermi/blazar thesis (AGN, BL Lac, Cherenkov).  Nothing written.
- **The three projects are one arc, not three subjects.**  All three run on
  **BING** (Prochaska & Frouin 2025, Biogeosciences 22, 4705): IOPtics
  benchmarks it, PAB fits with it, RoB departs from it.  The common object is
  retrieving IOPs from Rrs.  That is what makes a single unifying claim
  possible at all — and it is why `Info_content`/`nenya` (the self-supervised
  arc, last touched 2026-08-02 and 08-05) should stay out.
- **But BING is not Claude's.**  First commit 2024-06-04, two years before any
  of the three.  The foundation is yours and Frouin's; the thesis stands on it.
- **And the three are three months old and still moving.**  First commits
  2026-06-15 (IOPtics), 06-17 (PAB), 06-29 (RoB); latest 09-12, 09-11, 09-11.
  A1's framing ("Claude was the primary creator … they will form the bulk")
  reads as retrospective, but the work is live.  This is the single most
  important thing the round turned up, and Q2 leads with it.
- **State of each, verified.**  RoB README line 83: "the retrieval itself — the
  inversion — does not exist yet"; what exists is the differentiable forward
  model (`robust/rt/`), 0.30% rRMS held-out on L23, 2.3× better than the O25
  benchmark, in two reports authored "J. Xavier Prochaska and Claude (Fable 5)".
  IOPtics README: "Early development"; results are the GLORIA diagnosis (the
  power-law `b_bp` runs out of backscatter in the red) and the MOANA
  reimplementation, whose full reproduction is blocked on PML data as of today.
  PAB is the most complete: `pab_version = 1.0`, 14,610 matchups, 14,609 fits
  (99.99%), finished 2026-08-20, ~18.1 GiB of chains on `s3://pab`.
- **The bbp700 headline is not Claude's.**  84% / median +0.35 comes from
  `pab/matchup/pace_argo_bbp700_bias_analysis.md` on the 273-matchup `run1k`
  set; `claude_prompts/chl_cdom_matchups.md:434` attributes it to a student
  collaborator, and a sibling script carries `/Users/alliejames/…` paths.  Q3
  recommends re-deriving it on the full run so the chapter's number is Claude's.
- **The RoB ownership tension from round 1 is real and survives A1.**
  `proposals/Claude_Science/anthropic_application.md:197-198` still says the
  science "stays firmly ours", and the project has a seven-person team with
  Frouin and Dierssen as Co-Is.  A1 calls Claude RoB's primary creator.  Both
  cannot be fully true, and Q3 puts it to you rather than routing around it.

**The one change I made to Fable's draft.**  Its Q3 asserted specific UCSC
Graduate Division requirements on co-authored material as fact; its own
evidence section flagged that as unverified general knowledge.  I rewrote it as
a check to perform ("worth checking against the current UCSC guidelines, which
I have not read") rather than a claim.  Everything else I either verified
directly or left as clearly-marked recommendation.

**Fable's recommendation, in one line**, so the next session has it: make the
thesis about the *information content of hyperspectral Rrs* — how much of the
IOP inversion PACE actually supports — with IOPtics as the failure diagnosis,
RoB as the forward-model floor, PAB as validation at mission scale, and a new
fourth chapter binding them: re-invert a PAB subset with the RoB forward model
to test whether the bbp700 excess is a `b_bp` power-law artefact.  That last
chapter is the part nobody knows the answer to, and it is what would make this
a dissertation rather than three stapled packages.

**Where round 3 goes.**  Depends on both answers.  If you accept the unifying
claim, Q4 is scope and timeline — which results must exist by the defense, and
how the Dec 1 Claude Science deadline interacts with it.  If you reject it, the
question becomes whether a compilation thesis is acceptable to you as chair,
and Q4 is what the introduction must then do instead.

### 2026-09-12 (Thesis topic, round 3 — Q4 posed)

Executed prompt #7 — the 3rd task under "Thesis topic".  Read **A2** and **A3**
and wrote **Q4** into `## Q&A`.  No code; `## Report` and `## Goals` still
untouched.  Read-only git only.

**On "Use Fable if you can".**  Same constraint (no in-session model switch;
this session is Opus 5), so again a Fable subagent drafted and this session
verified, edited and logged.  Worth recording: **the first Fable subagent
stalled** — no progress for 600 s, killed by the watchdog — apparently while
reading this file, which is now 630+ lines.  The retry succeeded in 28 s
because I pre-supplied the verified evidence in the brief and told it not to
read `start_up.md`.  Lesson for future rounds: as this doc grows, brief the
subagent with extracted facts rather than pointing it at the file.

**What A2 did, and why Q4 had to be blunt.**  A2 accepted "mine science out of
the existing projects" but struck both halves of round 2's proposal: the
unifying claim (information content — "a primary conclusion of the BING paper …
not sure there is much more to say") and the binding synthesis chapter (bbp700
is Allie James's; anything in RoB past the forward model belongs to the RoB
team).  What came back was a three-item menu with no through-line, every item
already finished.  That is the compilation Q2 warned about, so Q4 says so in
those words and asks the two questions that matter: what single sentence do the
three chapters defend together, and what new work does Claude do whose answer
nobody knows yet.

**Evidence I verified myself this round** (beyond round 2's):

- **PAB Chl-a is the strongest asset, and it is Claude's.**
  `reports/PAB/pab_chl_matchups_report.md`, 2026-09-07, runs on the *full*
  production database (9,814 valid matchups of 14,609 `ExpBPow` fits) — not the
  273-matchup `run1k` set the excluded bbp700 result used.  Fourteen figures
  plus an Interpretation section; effectively a paper.  Headline: PACE exceeds
  Argo in 58%, median +0.13, but the bias **changes sign** with concentration
  (octile medians +0.65 → −0.8), and matchup geometry and PACE data quality are
  ruled out as drivers — the highest-quality subset shows a *larger* bias.  So
  losing bbp700 to A2's exclusion costs less than it first appeared: Chl-a
  replaces it cleanly and with better provenance.
- **That report names its own follow-ons, and they are the thesis's new work.**
  (1) the in-situ reference is the largest ambiguity — raw → delayed-mode
  adjusted Argo moves the median from +0.13 to +0.58, and PAB cannot tell which
  correction a DAC applied because `SCIENTIFIC_CALIB_*` is not ingested;
  (2) bias correlates with the fitted `Adg` amplitude (ρ = −0.24), "consistent
  with CDOM/detrital absorption aliasing into the Bricaud phytoplankton term",
  explicitly flagged as a candidate to test with synthetic BING fits at
  controlled `Adg`.  Both are in scope under every A2 exclusion.  (2) is also
  what binds the PAB chapter to the IOPtics chapter — same failure mode, one
  seen in controlled synthetic conditions, one at mission scale.
- **CDOM is not chapter-grade today.**  `pab_cdom_matchups_report.md` is titled
  "PACE – Argo CDOM Comparison (Qualitative/Correlative)" and contains a section
  headed "Why this comparison is qualitative only, not a bias analysis".  Rank
  correlation throughout, on raw fluorometer values carrying a known but
  **unapplied** Sea-Bird adjustment (RAF 5.62 — pre-2023-01-13 sensors read
  ~5.6× low).  Q4 recommends it as a section, not a chapter, unless redone.
- **"Any/all of the results in IOPtics" is thinner than it sounds.**  The only
  cross-algorithm sweep pages are `expb_giop_L23_test20` (generated 2026-07-03,
  **twenty** spectra, **two** algorithms) and `gloria_turbid_v3`.  L23 itself is
  3,320 Hydrolight water bodies with exact noise-free truth, and
  `docs/source/models.rst` documents models never swept (`expb_pow2flat` and
  others).  The benchmarking framework is built; the benchmark has not been run.
  This is the finding I added to Fable's draft — it is a gap, but a cheap and
  clearly in-scope piece of new work, so it strengthens the recommendation
  rather than weakening it.
- **A2's information-content claim could not be checked here.**  The string
  "information content" appears nowhere in `~/Oceanography/python/bing`, and the
  paper text (Prochaska & Frouin 2025, Biogeosciences 22, 4705) is not on disk;
  `~/Projects/Overleaf/Info_content` is the separate self-supervised project,
  not that paper.  I neither asserted nor contradicted it — Q4 simply routes
  around information content as a framing.  If you want that ground reopened,
  the paper's conclusions need to be read.

**Corrections I made to Fable's draft.**  It dated the Chl report "v1.0" — that
string is the *database's* `pab_version`, not a report version, so I rewrote it.
And I added the IOPtics sweep-gap finding above, which I turned up after the
subagent had been briefed.

**Fable's recommendation, in one line:** make the thesis *where and why
semi-analytical IOP retrieval breaks in the PACE era* — the failures are
parameterization failures, not physics failures.  IOPtics supplies the
controlled diagnosis, PAB Chl-a the same failure at mission scale against
independent truth, and the RoB forward model (0.30% rRMS) removes the
forward-model error term so the residual is attributable to parameterization
rather than to the physics.  This avoids information content, bbp700 and the
RoB inversion — all three A2 exclusions — while still having a single claim.

**Where round 4 goes.**  If he accepts the through-line, the next questions are
the chapter list and order, and the timeline against the Dec 1 Claude Science
window.  If he rejects it, the live question becomes whether he will sign a
compilation thesis as chair, and what the introduction must then carry instead.

### 2026-09-12 (Thesis topic, round 4 — interview closed, outcome recorded)

Executed prompt #8 — the 4th task under "Thesis topic".  Read **A4**, closed the
interview, and wrote the outcome into all three places the task named: the
`## Report` section below, `CLAUDE.md` (new "Thesis Topic and Scope" section plus
the source repositories under "Related Repositories"), and the `## Goals` section
at the top of this file.  No code; no state-changing git.

**On "Use Fable if you can".**  Same constraint as every round — a Fable
subagent drafted the Report, this session verified, corrected and wrote it.
Briefed with extracted facts and told explicitly not to open this file, per the
lesson from round 3; it returned in 74 s with no stalls and no tool calls at all.

**A4 and what it changed.**  A4 reads in full: *"There is much more to IOPtics
than you have found.  Most of that work has been done on my workstation.  And
there is also the MOANA analysis, which I am about to spin off into its own
Repo."*  Two consequences, one of them a correction to me:

- **My round-3 IOPtics finding was wrong in its implication.**  I reported that
  the only committed cross-algorithm sweep is `expb_giop_L23_test20` — twenty
  spectra, two algorithms — and inferred the benchmark had not been run.  The
  sweeps exist; they are on his workstation, outside git.  The science is not
  thin; the *repository* is.  I have recorded this as a provenance dependency
  rather than a gap, with the blunt consequence stated in the Report: nothing
  uncommitted can be cited in a dissertation, so those artefacts must be
  migrated before Chapter 3 can be written.  This also downgrades "run the full
  L23 sweep" from new work to possibly-just-migration — which is why the Report
  makes establishing what exists an open question rather than launching runs.
- **MOANA becomes a fourth source project and earns its own chapter.**  On the
  evidence in `MOANA_Claude_Report.md` (independent reimplementation, 299 tests,
  Lange Table 1 reproduced, a PC-mapping dispute settled empirically, and the
  first held-out hyperspectral skill numbers — picoeukaryotes transfer,
  *Pro*/*Syn* do not) it is chapter-grade on its own, and the spin-off makes the
  separation natural.  It also fits the through-line without strain: the same
  parameterization-transfer question, one level up, where the retrieved quantity
  is a cell abundance rather than an IOP.

**What A4 did *not* do, and how I handled it.**  It neither ratified nor
rejected the through-line proposed in Q4.  Since the task said to finish the
conversation and write the outcome, I adopted the statement by default — it is
the only one on the table and the interview closed without objection — but the
Report says so explicitly, in those words, and "ratify or replace the thesis
statement" is the first open question.  I did not manufacture agreement, and
future sessions are told not to represent it as agreed.

**The settled outcome**, recorded here in brief so it survives without the
Report: the thesis claims that *in the PACE era, semi-analytical IOP retrieval
from Rrs fails for identifiable reasons, and those failures are parameterization
failures rather than physics failures.*  Six chapters — Introduction; Methods
(the RoB differentiable forward model, 0.30% rRMS, stopping strictly at the
forward model); IOPtics (controlled diagnosis, the GLORIA red-backscatter wall);
MOANA (species-level retrieval and transfer limits); PAB (mission-scale
validation, the sign-changing Chl-a bias, CDOM as a section not a chapter);
Conclusions.  Chapters 2 and 4 are draft-able today, Chapter 5's descriptive
half is, Chapter 3 depends on migration, Chapters 1 and 6 do not exist.  Three
pieces of genuinely new work bind it: the synthetic-`Adg` aliasing experiment
(the Chl report's own proposed test, and the strongest potential evidence for
the claim), ingesting `SCIENTIFIC_CALIB_*` to settle whether raw or adjusted
Argo Chl-a is truth (+0.13 vs +0.58 — currently the largest ambiguity in the
chapter), and completing the L23 sweep subject to what already exists.

**What I learned about the interview itself.**  Four rounds, and the value was
almost entirely in the exclusions.  A1 fixed the standard, A2 removed three
things and in doing so removed the thesis I had proposed, A3 dismissed a worry I
had ranked as serious, and A4 corrected a fact I had over-read from git alone.
The recurring error on my side was treating the git repository as the world:
twice I inferred absence of work from absence of commits, and once — the CDOM
report — the repository told the truth but only because its author had written
the caveat into the title.  The Report's dependencies section exists mostly to
stop the next session repeating that mistake.

**Where the work goes next.**  Not another round of questions.  The five open
questions in the Report need the advisor's answers, and the first real task is
the workstation inventory, because Chapter 3 cannot be planned without it.
