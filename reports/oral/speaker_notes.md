# Speaker notes for the qualifying-exam oral

Deck: `reports/oral/qual_oral.pptx` (47 slides: 40 main + 7 backup).  Notes are on the ten slides that carry the argument; they are also embedded in the .pptx and survive the Google Slides import.

## Slide 1 — Where semi-analytical ocean-colour retrieval breaks in the PACE era

Open with the claim, read slowly, then say what the next forty minutes do: two pages of setup so the committee can read an ocean spectrum, then one controlled experiment that fixes the parameterization and varies the physics, one benchmark that does the reverse, and two applications one level up and at mission scale.  The claim was ratified by the advisor on 2026-09-17; the evidence was frozen on 2026-09-19.  Say once that the candidate is an AI and that the division of labour is on slide 6 and in the backup; the science slides do not return to it.

## Slide 5 — The claim, in the language of component separation

This is the slide the whole talk hangs on.  Make the two halves explicit: (1) there is a physics error term and it can be measured and removed, because we built a forward model whose error against HydroLight is 0.3 percent; (2) with that term gone, the error that remains does not move when the physics changes and does move when the parameterization changes, and it sits in the absorption split.  The SED analogy is for the two astronomers: dust versus age is the same degeneracy shape.  Do not return to the analogy.

## Slide 8 — Forward-model accuracy: from 7 % (Gordon) to 0.3 % (hybrid)

Walk the ladder top to bottom: Gordon at 4 to 12 percent depending on wavelength, the analytic backbone at 6, the O25 form refit on the same data at 0.7, the hybrid at 0.3, uniform across the spectrum.  Then the inset: held-out scenes and held-out sun angle.  Say the one honest thing: when a solar zenith is held out entirely the hybrid degrades to 5 to 12 percent and the refit form wins that split.  The bound holds inside the trained geometry and every sweep in the talk stays inside it.

## Slide 15 — The centrepiece: down the ladder, error moves only where the physics was the problem

Read the four panels left to right and say what each means.  Total absorption does not care about the physics: five percent under all five rungs, every pair indistinguishable.  Particulate backscatter is the physics failure: the elastic models overestimate it by 41 to 55 percent with zero interval coverage, because they have to put the inelastic red light somewhere and the power law is where it goes; the full inelastic rung brings that to minus five percent with 59 percent coverage.  The two absorption constituents are the parameterization failure: a_ph wrong by a factor of two and a_dg by a quarter to a third under every physics, with chi-squared-nu at 1.1 throughout.  This one slide is the thesis statement with numbers.

## Slide 16 — Read it as two findings

Two numbers to leave in the room.  The backscatter bias goes from plus 55 to minus 5 when the physics is completed; the phytoplankton absorption stays wrong by a factor of two under all five.  Anticipate the question: is a factor of two in a_ph a big deal?  Yes: a_ph is the chlorophyll proxy, and PACE's hyperspectral products for phytoplankton community are built on that decomposition.  The Raman-only rung is worst for a_ph because it removes red light without a fluorescence term to place it, so the parameterization absorbs the mismatch there.

## Slide 19 — Real PACE pixels, no truth: how far does the physics move the answer?

This arm has no truth, so it answers a different question: not which physics is right but how much the physics moves a real retrieval.  The answer for backscatter is a fifth, pixel by pixel; for the absorption constituents nearly nothing on average with a wide spread.  Two anchors: these 99 pixels are the ones PAB fitted under Gordon, and refitting them under the elastic hybrid reproduces PAB's posteriors with correlations of 0.94 to 1.00; and the spectra handed to the two fitters are identical to the last bit.  That is why the PAB 2.0 re-fit under this physics is the mission-scale echo of this slide.

## Slide 20 — Would the fit alone have found the physics error?  No.

This is the methodological point of the chapter.  The two ends of the ladder have the same number of parameters, so BIC is a pure likelihood contest.  On L23, which contains the inelastic light, 71 percent of bodies prefer it, but only 17 percent strongly.  On PANGAEA under a flat error model the verdict reverses.  On PACE it is bimodal.  Fit quality would never have identified the 55 percent backscatter bias; only truth plus a forward model with a known error term can.  That is why the separation cannot be done from operational residuals.

## Slide 25 — The in-situ failure rate was a scoring artefact

Say this plainly because it is the kind of thing a committee respects: the first benchmark said every algorithm fails on real spectra most of the time, and it was wrong.  The failure was in the scoring, a flat five percent error on spectra whose compilation quotes no uncertainty, and turbid spectra declared out of scope after fitting.  Under the corrected defaults the rates double, and under the field's own operational rule nine in ten spectra are valid.  The page the report cites is the corrected one, built this week; the first one is kept beside it.

## Slide 30 — Held out for the first time: picoeukaryotes transfer, the cyanobacteria do not

The transfer result is the parameterization question one level up.  The group whose optical signature is broad survives transfer; the two whose signatures the training cruise sampled narrowly do not.  Mention the two other findings in a sentence each: the shipping product uses the operational rather than the published coefficient mapping, settled on a 100,000-pixel granule; and 18 percent of Prochlorococcus retrievals in the product are clipped to exactly zero.

## Slide 34 — The chlorophyll bias changes sign with concentration

This is the degeneracy at mission scale.  The bias is flat in time and distance separation and gets worse, not better, in the highest-quality subset, so it is not the matchup and not PACE data quality.  It is uncorrelated with the backscatter bias, so the mechanism is not shared.  And it correlates with the fitted a_dg amplitude at rho of minus 0.24, the sign expected if dissolved absorption is being aliased into the phytoplankton term where a_dg is high.  That is the a_ph versus a_dg split from slide 14, seen in 9,814 real matchups.

## Slide 40 — Conclusions

Close on the claim, then the three sentences of what is established, then the two falsification tests so the committee hears that the claim can lose.  End on the candidate honestly: the provenance trail is the strength; the weakness the record shows is inferring absence of work from absence of commits, twice, and the correction came from the advisor and from re-checking the disk.  Then stop and take questions; the backup section is ordered by the four questions most likely to be asked.
