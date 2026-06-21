---
name: jedpsych-rebuttal
description: Use when writing the response to a Journal of Educational Psychology revise-and-resubmit. JEP R&Rs often demand added methodological rigor (multilevel modeling, cluster-level power, mechanism tests), fuller JARS disclosure, or stronger transparency, and the response must address every point while keeping the paper within format and masked. Structures the response letter; it does not fabricate new results.
---

# R&R Rebuttal (jedpsych-rebuttal)

A Journal of Educational Psychology **R&R** (usually a major revision) typically asks for **more
methodological rigor** (model the nesting, power at the cluster level, test the mechanism), **fuller JARS
disclosure**, or **stronger transparency** — and all of it must fit back inside the format and stay
**masked**. The response letter must convert every reviewer and reassure the handling editor on rigor and
educational relevance, while keeping the manuscript within the word budget.

## When to trigger

- An R&R arrived and you are planning the revision + response letter
- Reviewers requested multilevel reanalysis, added power, mechanism tests, disclosure, or open-science
  changes
- A requested analysis would change the claim
- Writing the cover note to the editor

## Strategy

1. **Read the editor's letter as the rubric.** Solve the decisive points first; the handling editor
   adjudicates among reviewers and synthesizes the required changes.
2. **Point-by-point, every comment.** Quote each comment, then respond; never skip one.
3. **Strengthen rigor, don't just defend.** Many requests (refit a multilevel model, re-power at the
   cluster level, add the mediation test, report effect sizes with CIs, fuller JARS disclosure, better
   data/code sharing) genuinely strengthen the paper — do them and say where. Update the Transparency and
   Openness subsection if deposits or preregistration status changed.
4. **Manage the word budget.** New robustness, full measurement models, and extra specifications usually
   belong in **online supplemental material**; summarize briefly and point to the supplement so the body
   stays under the limit.
5. **Concede or rebut with evidence.** Did what was asked (cite the location), or push back respectfully
   with a reason — don't add an analysis that quietly undercuts the claim without saying so.
6. **Keep the revision masked.** No author names, grant numbers, site/IRB names, or first-person self-
   citations in the revised manuscript or links; keep shared scripts/data in sync (see
   `jedpsych-open-science-and-transparency`).

## Response-letter format

For each reviewer comment:

```
> [Quoted reviewer comment]

Response: [What we did / why we respectfully disagree].
Change: [Main text section, supplement section, or table/figure number].
```

Open with a short **summary of the main changes** to the editor; group by reviewer; end each entry with
the location (note when content went to the supplement to protect the word budget).

## Worked micro-example (illustrative response entries)

For the cluster-randomized reading trial, an R&R asked for multilevel reanalysis, the mechanism, and
fuller disclosure.

```
> R2: The analysis treats students as independent; with classroom
> randomization, the SEs are too small.

Response: Agreed. We refit the primary analysis as a two-level model
(students within classrooms) with random classroom intercepts and a pretest
covariate. The effect remains educationally meaningful (g = 0.23, 95% CI
[0.06, 0.40]; ICC = 0.14). Cluster-level power is now justified in Method.
Change: Method (power), Results (two-level model, Table 1); robustness → Supplement S2.

> R1: You claim a strategy-instruction mechanism but never test it.

Response: We added the preregistered multilevel mediation: gains in
metacognitive monitoring mediate ~40% of the effect (indirect 95% CI
[0.02, 0.13]).
Change: Results (mediation, Figure 1); analysis code updated in the deposit.

> R3: Attrition handling is unclear.

Response: We now report attrition by arm and re-estimate under FIML; the
effect is unchanged (g = 0.21).
Change: Method (attrition), Results (robustness); JARS flow reported.
```

## R&R triage — where each request lands

| Reviewer ask | Default home (protects the word budget) | Note |
|--------------|------------------------------------------|------|
| Refit multilevel / re-power at cluster level | Method + Results (it is the contribution) | report ICC; update power justification |
| Mechanism (mediation/moderation) test | Results | preregistered if possible; update deposit |
| Added robustness / specification grid | online supplemental material | summarize in one main-text sentence |
| Fuller disclosure (exclusions/attrition/measures) | Method + Transparency subsection | a table, not prose, to save words |
| "Soften the claim" | Discussion | scale wording to the CI and the setting studied |
| Effect-size/CI + educational interpretation | tables and inline | route exhibits to `jedpsych-tables-figures` |

## Recurring R&R pushback and the venue fix

- "Clustering ignored" → refit a multilevel/random-effects model, report the ICC, re-justify cluster-level
  power; never argue the single-level p-value. "Mechanism asserted, not tested" → add the preregistered
  mediation/moderation and interpret it.
- "You added an analysis that weakens the effect" → disclose it, interpret it, adjust the claim;
  concealment is fatal here. "Revision busts the format" → push new robustness to the supplement, cite it.

## Anti-patterns

- Ignoring or merging away a comment without a visible response
- Cramming new robustness into the body and busting the word limit
- Capitulating to a change that breaks the paper's logic
- Adding analyses that contradict the original claim without acknowledgment
- Letting shared data/scripts/Transparency subsection drift out of sync, or reintroducing identifying
  information into the masked revision

## Output format

```
【Editor's decisive points】addressed first? [list]
【Coverage】every reviewer comment answered? [Y/N]
【Rigor strengthened】nesting/power/mechanism/disclosure improved? [Y/N]
【Word budget】new material in supplement; body ≤ 12,000? [Y/N]
【Open-science updated】scripts/data/Transparency subsection in sync? [Y/N]
【Masked】no identity reintroduced? [Y/N]
【Next】resubmit via Editorial Manager
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — masked review, JARS, transparency, and format policy
