# Getting started

## Goals

This repository will hold the code, analyses, and figures behind a PhD thesis
written by Claude.  The write-up itself lives in the LaTeX project at
`~/Projects/Overleaf/Claude-PhD-Thesis` (UCSC `ucthesis` class); this repository
is where the science gets done.

## Prompts

1. Read this file.  Execute the 1st task under "Claude/CLAUDE.md file"
2. Read this file.  Execute the 1st task under "Claude/Skills"
3. Read this file.  Execute the 1st task under "Claude/Settings"
4. Read this file.  Execute the 1st task under "Basic start up"

5. Read this file.  Execute the 1st task under "Thesis topic"
6. Read this file.  Execute the 2nd task under "Thesis topic"

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

## Report

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
