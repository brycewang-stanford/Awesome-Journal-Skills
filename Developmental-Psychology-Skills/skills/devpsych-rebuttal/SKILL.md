---
name: devpsych-rebuttal
description: Use when writing the response to a Developmental Psychology (APA) revise-and-resubmit. Reviews here often demand measurement-invariance tests, attrition analyses, added robustness, fuller JARS disclosure, or stronger transparency. The response must address every point and strengthen the developmental claim while staying in the length tier and masked. Structures the response letter; it does not fabricate new results.
---

# R&R Rebuttal (devpsych-rebuttal)

A Developmental Psychology **R&R** typically asks for **a measurement-invariance test, an attrition
analysis, added robustness, fuller JARS disclosure, or stronger transparency** — and all of it must fit
back inside the **length tier**, with masking intact if review is masked. The response letter must convert
every reviewer and reassure the handling editor that the **developmental claim is credible**.

## When to trigger

- An R&R arrived and you are planning the revision + response letter
- Reviewers requested invariance, attrition, added analyses, or open-science changes
- A requested analysis would change the trajectory or the claim
- Writing the cover note to the editor

## Strategy

1. **Read the editor's letter as the rubric.** Solve the decisive developmental-credibility points first
   (often: invariance, age-vs-cohort, attrition); the editor adjudicates among reviewers.
2. **Point-by-point, every comment.** Quote each comment, then respond; never skip one.
3. **Strengthen the developmental claim, don't just defend.** Most requests — report invariance, model
   attrition with FIML/MI, add a robustness model, justify N, share data — make the paper stronger. Do
   them and say where; update the data-availability statement if sharing changed.
4. **Manage the length tier.** New robustness usually belongs in **online supplemental material** so the
   main text stays within budget; summarize briefly in the main text and point to the supplement.
5. **Concede or rebut with evidence.** Did what was asked (cite the location), or push back respectfully
   with a reason — and never add an analysis that quietly undercuts the change claim without disclosing it.
6. **Keep masking and sync deposits.** Keep the revised manuscript and links anonymized if review is
   masked, and ensure new analyses are reflected in the shared scripts/data
   (see `devpsych-open-science-and-transparency`).

## Response-letter format

For each reviewer comment:

```
> [Quoted reviewer comment]

Response: [What we did / why we respectfully disagree].
Change: [Main text section, supplement section, or table/figure number].
```

Open with a short **summary of the main changes** to the editor; group by reviewer; end each entry with
the location (note when content went to the supplement to protect the length tier).

## Worked micro-example (illustrative response entries)

For the three-wave effortful-control package, an R&R asked for invariance, attrition handling, and N.

```
> R2: You interpret growth, but is the measure invariant across ages 4-8?

Response: A fair and important point. We now test measurement invariance
before interpreting change: configural, metric, and scalar invariance hold
across waves (ΔCFI < .01; table now in Results). Mean change is therefore
interpretable on a common metric.
Change: Results (new invariance subsection + Table 2); Method (test plan).

> R1: Attrition (18%) could bias the trajectory.

Response: We refit all models with FIML under MAR and compared completers
and dropouts on baseline covariates (no differences). A pattern-mixture
sensitivity analysis leaves the slope and interaction unchanged.
Change: Results (FIML); attrition + sensitivity analysis → Supplement S2.
```

## R&R triage — where each request lands

| Reviewer ask | Default home (protects the length tier) | Note |
|--------------|------------------------------------------|------|
| Measurement-invariance test | Method + Results (it underwrites the claim) | compact table; full fit indices to supplement |
| Attrition / missing-data analysis | Results + supplement | FIML/MI in text; full table in supplement |
| Added robustness / alternative model | online supplemental material | one summarizing sentence in main text |
| "Address age vs. cohort" | Discussion (+ design note) | reframe or add covariate/sequential argument |
| Fuller JARS disclosure | Method + data-availability statement | a table, not prose, to save words |
| Effect-size/CI reporting | tables and inline | route exhibits to `devpsych-tables-figures` |

## Recurring R&R pushback and the venue fix

- "Trajectory without invariance" → add the configural→metric→scalar test and interpret change only at
  the level achieved; this is the single most common developmental R&R request.
- "You deleted dropouts" → refit with FIML/MI and add the attrition analysis; never argue from completers
  alone.
- "Added analysis quietly weakens the effect" → disclose it, interpret it, and scale the claim; concealment
  is the cardinal sin.
- "Revision busts the tier" → push new robustness to online supplemental material and cite it.

## Anti-patterns

- Ignoring or merging away a comment without a visible response
- Cramming new robustness into the main text and busting the length tier
- Capitulating to a change that breaks the developmental logic
- Adding analyses that contradict the change claim without acknowledgment
- Letting shared data/scripts/data-availability statement drift out of sync with the revision
- Reintroducing identifying information into the masked revision

## Output format

```
【Editor's decisive points】addressed first? [list]
【Coverage】every reviewer comment answered? [Y/N]
【Claim strengthened】invariance/attrition/power/disclosure improved? [Y/N]
【Length tier】new material in supplement; main text within limit? [Y/N]
【Transparency updated】scripts/data/data-availability statement in sync? [Y/N]
【Masking intact】[Y/N/NA]
【Next】resubmit via Editorial Manager
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — review model, JARS, TOP, and length tiers
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — invariance/SEM, missing-data, and power tooling
