---
name: psci-rebuttal
description: Use when writing the response to a Psychological Science revise-and-resubmit. Reviews here often demand added robustness, fuller disclosure, or stronger transparency, so the response must address every point and strengthen credibility without breaking the tight format. Structures the response letter; it does not fabricate new results.
---

# R&R Rebuttal (psci-rebuttal)

A Psychological Science **R&R** typically asks for **more robustness, fuller disclosure, or stronger
transparency** — and all of it has to fit back inside a **very tight word format**. The response
letter must convert every reviewer and reassure the editor on credibility, while keeping the paper
within budget.

## When to trigger

- An R&R arrived and you are planning the revision + response letter
- Reviewers requested added analyses, robustness, disclosure, or open-science changes
- A requested analysis would change the claim
- Writing the cover note to the editor

## Strategy

1. **Read the editor's letter as the rubric.** Solve the decisive points first; the editor adjudicates
   among reviewers.
2. **Point-by-point, every comment.** Quote each comment, then respond; never skip one.
3. **Strengthen credibility, don't just defend.** Many requests (more power, robustness checks, fuller
   disclosure, better data/materials sharing, clearer confirmatory/exploratory split) make the paper
   stronger — do them and say where. The Research Transparency Statement may need updating.
4. **Manage the word budget.** New robustness usually belongs in **supplemental online material** so the
   2,000-word core stays intact; summarize it briefly in the main text and point to the supplement.
5. **Concede or rebut with evidence.** Did what was asked (cite the location), or push back
   respectfully with a reason — don't add an analysis that quietly undercuts the claim without saying so.
6. **Keep anonymization** in the revised (masked) manuscript and repository links, and ensure new
   analyses are reflected in the shared scripts/data (see `psci-open-science-and-transparency`).

## Response-letter format

For each reviewer comment:

```
> [Quoted reviewer comment]

Response: [What we did / why we respectfully disagree].
Change: [Main text section, supplement section, or table/figure number].
```

Open with a short **summary of the main changes** to the editor; group by reviewer; end each entry
with the location (note when content went to the supplement to protect the word budget).

## Worked micro-example (illustrative response entries)

For the two-study attention package, an R&R asked for power, a replication, and tighter disclosure.

```
> R2: Study 1 (N = 240) feels underpowered for a d ≈ 0.3 effect.

Response: We agree precision matters here. Study 1 had ~80% power for
d = 0.36 (sensitivity analysis now in Methods). To address fragility we
added Study 2 (N = 300), which directly replicates the effect
(d = 0.29, 95% CI [0.06, 0.51]). Pooled estimate: d = 0.31, 95% CI [0.13, 0.49].
Change: Main text Methods (power), Results (Study 2); robustness grid → Supplement S3.

> R1: The trait-anxiety interaction looks post hoc.

Response: Correct — it was exploratory in Study 1 and we now say so
explicitly. We preregistered it for Study 2; it is labeled confirmatory
only there.
Change: Results (status labels); Research Transparency Statement updated.
```

## R&R triage — where each request lands

| Reviewer ask | Default home (protects the 2,000-word core) | Note |
|--------------|----------------------------------------------|------|
| Added robustness / specification grid | supplemental online material | summarize in one sentence in main text |
| New confirmatory study | Methods/Results (it is the contribution) | preregister it; update Transparency Statement |
| Fuller disclosure of exclusions/measures | Methods + Transparency Statement | a table, not prose, to save words |
| "Soften the claim" | Discussion | scale the wording to the CI, not the p-value |
| Effect-size/CI reporting | tables and inline | route exhibits to `psci-tables-figures` |

## Recurring R&R pushback and the venue fix

- "Single underpowered study" → add internal replication or move to a multi-study package; report the
  pooled estimate with its CI; never argue the p-value alone.
- "You added an analysis that quietly weakens the effect" → disclose it, interpret it, and adjust the
  claim; concealment is the cardinal sin at this venue.
- "Revision busts the format" → confirm the current word allowance against the journal's submission
  guidelines, then push new robustness to the supplement and cite it.

## Anti-patterns

- Ignoring or merging away a comment without a visible response
- Cramming new robustness into the 2,000-word core and busting the format
- Capitulating to a change that breaks the paper's logic
- Adding analyses that contradict the original claim without acknowledgment
- Letting shared data/scripts/Transparency Statement drift out of sync with the revision
- Reintroducing identifying information into the masked revision

## Output format

```
【Editor's decisive points】addressed first? [list]
【Coverage】every reviewer comment answered? [Y/N]
【Credibility strengthened】power/robustness/disclosure/transparency improved? [Y/N]
【Word budget】new material in supplement; core ≤ 2,000? [Y/N]
【Open-science updated】scripts/data/Transparency Statement in sync? [Y/N]
【Anonymization intact】[Y/N]
【Next】resubmit via Manuscript Central
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — review model, transparency weighting, format
