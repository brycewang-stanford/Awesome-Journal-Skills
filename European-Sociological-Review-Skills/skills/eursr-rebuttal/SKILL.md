---
name: eursr-rebuttal
description: Use when writing the response to a European Sociological Review (ESR) revise-and-resubmit. ESR R&Rs typically demand substantial revision and reviewers focus on comparative design, measurement equivalence, and modeling, so the response must convert each reviewer while keeping the editor confident. Structures the response letter; it does not fabricate new results.
---

# R&R Rebuttal (eursr-rebuttal)

An ESR **R&R** is the normal road to publication for a promising paper — and it usually asks for
**substantial** revision. Reviewers focus on the **comparative design, measurement equivalence, and the
modeling** (level, clustering, few-cluster inference), so the response letter must satisfy a quantitative
skeptic without breaking the paper, while the editor adjudicates.

## When to trigger

- An R&R decision arrived and you are planning the revision + response letter
- Reviewers disagree (e.g., one wants more countries, another a different estimator)
- A reviewer requests analyses or measurement changes that would change the claims
- Writing the cover note to the editor summarizing the revision

## Strategy

1. **Read the editor's letter as the rubric.** The editor flags which points are decisive — solve those
   first; the editor adjudicates conflicts among reviewers.
2. **One point-by-point response, every comment addressed.** Quote each comment, then respond. Never
   skip one — silence reads as non-compliance.
3. **Concede or rebut explicitly, with evidence.** For each: did what was asked (say where, with the new
   text/table number), or push back **respectfully with a reason** (theory, design, or measurement). A
   well-argued disagreement beats a capitulation that weakens the paper.
4. **Answer modeling and measurement demands on their own terms.** A request for invariance tests,
   df-aware SEs, a leave-one-country-out check, or an alternative harmonization should be *run and
   reported honestly* — these are ESR's core review currency.
5. **Protect the contribution.** Add robustness, invariance, and clarifications; resist changes that
   dilute the portable mechanism or the comparative leverage that earned the R&R.
6. **Keep anonymity intact** in the revised manuscript, and update the **Data Availability Statement and
   replication package** so any new tables/figures stay reproducible (see `eursr-transparency-and-data`).

## Response-letter format

For each reviewer comment:

```
> [Quoted reviewer comment]

Response: [What we did / why we respectfully disagree].
Change: [Section/page/table-figure number where the revision appears].
```

Open with a short **summary of the main changes** to the editor; group by reviewer; end each entry with
the location of the change so the editor can verify quickly.

## Triage grid for an ESR R&R

| Comment type | Default response |
|--------------|------------------|
| Editor's decisive point | do it; never argue these away |
| Modeling/measurement check you can run (invariance, df SEs, LOO) | run it; report honestly even if mixed |
| "Add more countries / waves" | add if feasible; if not, justify the set and bound the claim |
| Request that dilutes the mechanism or comparative leverage | rebut respectfully with a reason |

## Worked micro-example (illustrative)

A comparative attitudes paper gets an R&R where R1 doubts measurement equivalence and R2 thinks the
macro effect rests on too few clusters.

```
R1: "Are the attitude scales comparable across countries?"
  Response: Added configural/metric/scalar invariance tests (Appendix Table A3); scalar fails for 3
  countries → re-estimated with partial scalar invariance; substantive conclusion unchanged. Change: §4.2.
R2: "24 countries can't support that macro claim."
  Response: Re-ran macro inference with a wild cluster bootstrap and a Bayesian two-level model
  (Table 5); interaction CI widens but excludes zero; macro claim tempered. Change: §5.1, Appendix B.
```

The letter concedes where evidence warrants, runs the modeling checks on their own terms, and protects
the contribution by showing the cross-level result survives the stricter inference.

## Referee pushback → ESR-specific fix

- *"The revision didn't change anything."* → End each entry with an exact location; visible change beats
  a thank-you.
- *"You ignored the invariance issue."* → Run the invariance tests, report the level reached, and state
  what partial invariance licenses.
- *"You over-claim from few clusters."* → Re-estimate with df-aware or Bayesian methods and temper the
  macro claim rather than defending the original SEs.

## Calibration anchors

- **The editor's letter is the rubric.** At ESR the editor weights reviewers; solving the decisive points
  first converts an R&R.
- **Run the modeling checks.** Invariance, few-cluster inference, and leave-one-country-out are ESR's
  review currency — running them honestly is more persuasive than arguing them away.
- **Substantial means substantial.** Plan for a heavy revision; a light pass reads as non-engagement.

## Anti-patterns

- Ignoring or merging away a comment without a visible response
- Capitulating to a request that breaks the paper's logic just to please a reviewer
- Dismissing a measurement-equivalence or few-cluster objection instead of addressing it
- "We thank the reviewer" with no actual change or argued reason
- New analyses that quietly contradict the original claim without acknowledgment
- Reintroducing identifying information into the revised (still anonymous) manuscript

## Output format

```
【Editor's decisive points】addressed first? [list]
【Coverage】every reviewer comment answered? [Y/N]
【Concede vs rebut】each tagged with evidence + change location
【Modeling/measurement checks】invariance / few-cluster / LOO run and reported? [Y/N]
【Contribution protected】no dilution of mechanism / comparative leverage? [Y/N]
【Anonymity + DAS/package updated】[Y/N]
【Next】resubmit via ScholarOne
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — invariance, few-cluster, and Bayesian multilevel tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — ESR review model and ethics
