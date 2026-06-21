---
name: joap-rebuttal
description: Use when writing the response to a Journal of Applied Psychology (JAP) revise-and-resubmit. JAP R&Rs typically demand stronger theory, added rigor (alternative models, CMV checks, robustness), and fuller transparency across multiple reviewers and an action editor. The response must address every point, strengthen the contribution, and keep masking intact. Structures the response letter; it does not fabricate results.
---

# R&R Rebuttal (joap-rebuttal)

A JAP **R&R** is demanding and usually multi-round. Reviewers and the **action editor** typically ask
for a **sharper theoretical contribution**, **added methodological rigor** (alternative models, CMV
diagnostics, robustness, measurement evidence), and **fuller transparency**. The response letter must
**convert every reviewer**, **reassure the editor on the dual gate** (theory + rigor), and keep the
masked manuscript anonymized.

## When to trigger

- An R&R arrived and you are planning the revision + response letter
- Reviewers requested added analyses, alternative models, robustness, or open-science changes
- A requested analysis would change the claim or the contribution
- Writing the cover note to the action editor

## Strategy

1. **Read the editor's letter as the rubric.** The action editor adjudicates among reviewers and tells
   you which points are decisive — solve those first and visibly.
2. **Point-by-point, every comment.** Quote each comment, then respond; never skip or silently merge one.
3. **Strengthen the contribution, don't just defend.** Many requests (sharper mechanism, alternative
   models tested, CMV diagnostics, measurement invariance, robustness) make the paper stronger — do them
   and say where. If the theory advance is the weak point, rebuild it (route to
   `joap-theory-and-hypotheses`).
4. **Test rival explanations head-on.** JAP reviewers raise alternative models and method artifacts;
   run and report them rather than hand-waving — concede where a rival fits better, defend with evidence
   where it does not.
5. **Place new material wisely.** Core new evidence belongs in the manuscript; extended robustness,
   invariance, and alternative-model tables usually go to **online supplemental materials**, summarized
   in one sentence in the main text.
6. **Keep masking and transparency in sync.** Maintain anonymization in the revised manuscript and
   repository links, and reflect new analyses in the shared data/code and the data-availability
   statement (see `joap-open-science-and-transparency`).

## Response-letter format

For each reviewer comment:

```
> [Quoted reviewer comment]

Response: [What we did / why we respectfully disagree, with evidence].
Change: [Main text section, supplement section, or table/figure number].
```

Open with a short **summary of the main changes** to the action editor; group by reviewer; end each
entry with the location.

## Worked micro-example (illustrative response entries)

For the servant-leadership package, an R&R asked for an alternative model, a CMV check, and a sharper boundary.

```
> R2: Could reverse causality or a third variable explain the safety→
> performance path? An alternative model should be tested.

Response: We agree. We now test (a) the reversed mediation and (b) a model with
prior team performance (Wave 0) as a control; the hypothesized 2-2-2 model fits
better (ΔCFI > .01) and the indirect effect remains (.11, 95% CI [.04, .20]).
The lab experiment provides the causal warrant for the safety path.
Change: Results (alternative models); robustness grid → Supplement S4.

> R1: Same-source bias may inflate the field correlations.

Response: Predictor and outcome were separated by wave and source (member-rated
leadership/safety; supervisor-rated performance). We add a CFA marker-variable
test; estimates are essentially unchanged.
Change: Method (design separation), Results (marker test), Transparency statement.
```

## R&R triage — where each request lands

| Reviewer ask | Default home | Note |
|--------------|--------------|------|
| Alternative / reverse-causal model | Results (core) + supplement detail | this often decides the paper |
| CMV diagnostic (marker, ULMC) | Method + Results | pair with the procedural remedies already used |
| Measurement invariance / extra validity | supplement | summarize one sentence in main text |
| Robustness / sensitivity grid | supplement | cite from one main-text sentence |
| "Sharpen the contribution" | Introduction + Theory | rebuild the mechanism/boundary, don't just reword |
| "Soften causal language" | throughout | scale verbs to the design; reserve causation for the experiment |

## Recurring R&R pushback and the venue fix

- "Theory is still thin" → do not just expand the literature; articulate the new mechanism/boundary and
  rederive the hypotheses (route to `joap-theory-and-hypotheses`).
- "You didn't rule out the alternative" → run the rival model and report the comparison; this is the
  most common reason a JAP R&R fails.
- "Added analysis quietly weakens the effect" → disclose it, interpret it, adjust the claim;
  concealment is the cardinal sin.
- "Data/code don't reflect the revision" → update the deposit and the data-availability statement.

## Anti-patterns

- Ignoring or merging away a comment without a visible response
- Defending against an alternative model instead of testing it
- Adding analyses that contradict the original claim without acknowledgment
- Rewording the introduction and calling it a strengthened contribution
- Letting shared data/code/transparency statement drift out of sync with the revision
- Reintroducing identifying information into the masked revision

## Output format

```
【Editor's decisive points】addressed first? [list]
【Coverage】every reviewer comment answered? [Y/N]
【Contribution strengthened】mechanism/boundary sharpened? [Y/N]
【Rigor strengthened】alternative models + CMV + robustness added? [Y/N]
【Placement】core in main text, extended in supplement? [Y/N]
【Open-science + masking】data/code/statement updated; anonymization intact? [Y/N]
【Next】resubmit via Editorial Manager
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — masked review model, action-editor process, TOP weighting
