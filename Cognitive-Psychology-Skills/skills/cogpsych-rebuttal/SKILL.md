---
name: cogpsych-rebuttal
description: Use when writing the response to a Cognitive Psychology (Elsevier) major/minor revision. Reviews here often demand added experiments, more model comparisons, recovery analyses, or fuller reproducibility, so the response must address every point and strengthen the model-driven inference. Structures the response letter; it does not fabricate new results or model fits.
---

# Revision Rebuttal (cogpsych-rebuttal)

A Cognitive Psychology **revision** typically asks for **more modeling rigor** — an additional
experiment, a further model comparison, parameter/model recovery, alternative priors, or reproducible
code — because the contribution is a model-driven theoretical claim. The response letter must convert
every reviewer and reassure the editor that the **model adjudication is now airtight**, while keeping
the integrative argument coherent.

## When to trigger

- A major/minor revision arrived and you are planning the revision + response letter
- Reviewers requested added experiments, model comparisons, recovery, or open-code changes
- A requested analysis or model would change the conclusion
- Writing the cover note to the handling editor

## Strategy

1. **Read the editor's letter as the rubric.** Solve the decisive points first; the editor adjudicates
   among reviewers and decides the next round.
2. **Point-by-point, every comment.** Quote each comment, then respond; never skip one.
3. **Strengthen the model inference, don't just defend.** Many requests (fit a further rival, add
   recovery, cross-validate, refit hierarchically, share code) make the adjudication stronger — do them
   and say where. A request that exposes overfitting must be addressed, not waved away.
4. **Keep the program coherent.** A new experiment or model should slot into the argument; update the
   General Discussion so the synthesis still holds (see `cogpsych-writing-style`).
5. **Concede or rebut with evidence.** Did what was asked (cite the location), or push back respectfully
   with a reason (e.g., why a requested model is not identifiable) — don't add an analysis that quietly
   undercuts the claim without saying so.
6. **Keep the modeling reproducible.** New analyses must be reflected in the deposited model/analysis
   code and regenerate in a fresh session (see `cogpsych-open-science-and-transparency`).

## Response-letter format

For each reviewer comment:

```
> [Quoted reviewer comment]

Response: [What we did / why we respectfully disagree].
Change: [Manuscript section, supplement/appendix section, table/figure, or
         deposited-code file].
```

Open with a short **summary of the main changes** to the editor; group by reviewer; end each entry with
the location (note when added analyses or experiments went to the supplement/appendix).

## Worked micro-example (illustrative response entries)

For the recognition-memory program, a major revision asked for a further model and recovery.

```
> R2: You compare UVSD and DPSD, but a mixture model might fit better -
> have you ruled it out?

Response: We agree this rival should be tested. We added a finite-mixture
SDT model, fit under matched flexibility; it does not improve penalized fit
(dBIC = 9 favoring UVSD) and model recovery confirms the comparison is
diagnostic at our design's N/trials.
Change: Results (model comparison, Table 1 expanded); recovery → Appendix B;
         fitting code updated (deposit, fit_mixture.R).

> R1: Can you recover the DPSD parameters at your trial counts?

Response: Yes - we now report parameter recovery for all three models
(recovered values within credible intervals). This is why the model
comparison is interpretable rather than an artifact of identifiability.
Change: Appendix B (recovery); deposited code recovery_sim.R; one sentence
         in Results pointing to it.
```

## Revision triage — where each request lands

| Reviewer ask | Default home | Note |
|--------------|--------------|------|
| Fit a further rival model | Results + model-comparison table | refit all models under matched flexibility |
| Parameter / model recovery | appendix/supplement | summarize the result in one main-text sentence |
| Refit hierarchically / alternative priors | Results + diagnostics | report convergence; sensitivity in supplement |
| New experiment | Methods/Results (it is contribution) | integrate into the General Discussion synthesis |
| "Soften the theoretical claim" | General Discussion | scale wording to what the comparison licenses |
| Reproducibility / code | deposit + Open Practices statement | ensure fits regenerate in a fresh session |

## Recurring revision pushback and the venue fix

- "You only ruled out one rival" → fit the additional model(s) under matched flexibility; report the
  penalized comparison and recovery; never argue from a single fit.
- "Your better fit might be overfitting" → add cross-validation/penalized criteria and model recovery;
  if the edge does not survive, adjust the claim.
- "I couldn't reproduce your fits" → ship seeded code + a pinned environment + a fresh-session run log;
  reference it in the response.
- "The new analysis weakens the effect" → disclose it, interpret it, and scale the theoretical claim;
  concealment is the cardinal sin.

## Anti-patterns

- Ignoring or merging away a comment without a visible response
- Defending a single fit instead of adding the requested comparison/recovery
- Adding an experiment or model that breaks the program's coherence without re-synthesizing
- Adding analyses that contradict the original claim without acknowledgment
- Letting deposited model code/data drift out of sync with the revision

## Output format

```
【Editor's decisive points】addressed first? [list]
【Coverage】every reviewer comment answered? [Y/N]
【Model inference strengthened】added comparison/recovery/hierarchy? [Y/N]
【Program coherent】new experiment/model integrated into the synthesis? [Y/N]
【Reproducible】deposited code updated + fits regenerate? [Y/N]
【Next】resubmit via Editorial Manager
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — review model, revision norms, reproducibility expectations
