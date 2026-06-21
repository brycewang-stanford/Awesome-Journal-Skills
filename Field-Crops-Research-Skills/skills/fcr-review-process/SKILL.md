---
name: fcr-review-process
description: Use to understand how Field Crops Research (FCR) evaluates a manuscript — initial editor screening against the journal's scope boundary, the single-anonymized review model with typically two or more reviewers, and the common reasons for desk rejection (controlled-environment-only, single-site single-season, descriptive/local, out-of-scope species). Sets expectations and shapes the paper to survive review; it does not contact editors.
---

# Review Process (fcr-review-process)

Knowing how FCR screens and decides lets you pre-empt the failure modes before submitting. FCR screens
**hard against scope** at the editor stage, then uses a **single-anonymized** review with **typically
at least two reviewers**.

## When to trigger

- Before submitting, to stress-test against desk-rejection grounds
- Interpreting a decision letter and setting expectations
- Understanding what reviewers and editors weigh in field-crop science

## How FCR review works

1. **Editor scope screening first.** Editors assess suitability before review. The most common
   **desk-rejection** grounds are scope failures:
   - **Controlled-environment only** — greenhouse, pots, or any root-restricting system as the main evidence.
   - **Single site, single season** — not the expected ≥ 2 seasons and/or multiple environments.
   - **Descriptive / corroborative / local** — no new scientific insight of general relevance.
   - **Out-of-scope species** — horticultural, woody-perennial, medicinal, or non-cultivated species.
   - **Inadequate English** or methods too incomplete to evaluate.
2. **Single-anonymized review.** Reviewers know the authors; authors do not know the reviewers.
   Suitable papers are sent to **typically two or more** expert reviewers.
3. **Decision categories.** Reject / major revision / minor revision / accept (exact labels per
   Editorial Manager). Revisions are common; address every point.
4. **Co-submission.** Related data/methods may be routed to **Data in Brief** / **MethodsX**.

## Shape the paper to pass

- Make **scope fit obvious** in the cover letter, abstract, and introduction (field-based,
  multi-environment, field crop, general relevance).
- State the **novel contribution** and link results to **yield / biophysical process**.
- Use **statistics that match the design** (mixed models, G×E) so a methods reviewer is satisfied.
- Report enough agronomic detail (soil, weather-vs-phenology, management) to be reproducible.
- Make the **discussion interpret**, not repeat — a frequent reviewer complaint.

## What each gatekeeper weighs

A submission passes three readers, each with a distinct veto. Anticipating who blocks on what lets you
pre-empt the objection in the right section.

| Gatekeeper | Weighs most | Blocks when |
|------------|-------------|-------------|
| Editor (scope) | field-based, multi-environment, field crop, general | controlled-environment-only, single site-season, descriptive/local, out-of-scope species |
| Methods reviewer | design–analysis match, error structure, G×E | pseudoreplication, wrong error term, pooled environments hiding G×E |
| Agronomy reviewer | yield/process link, mechanism, generality | yield with no biophysical explanation, discussion that repeats results |

## Worked screening vignette (illustrative)

*Illustrative walk-through.* A paper reports a **0.7 t ha⁻¹** sorghum yield gain from a sowing-date
shift over **2 seasons at 3 sites**. The editor's scope screen passes: field-based, 6 site-years, a
field crop, plausibly general. The methods reviewer flags that sowing date was applied to whole strips
with cultivar nested inside, so the **strip-plot error** must be used — the original ANOVA over-stated
significance. The agronomy reviewer wants the effect tied to **escaping terminal heat at anthesis**, a
phenology mechanism, not just a number. Realistic outcome: **major revision** — refit with the correct
error term, add phenology-vs-temperature evidence, and scope the recommendation to terminal-heat
environments.

## Anti-patterns

- Submitting controlled-environment-only or single-site/single-season work to a multi-environment journal
- A descriptive "we measured X here" paper with no general insight
- Wrong error structure or pseudoreplication that a methods reviewer will catch
- A discussion that restates results without agronomic interpretation
- Conclusions not justified by the data


## Review-risk pass for Field Crops Research

Treat this skill as an executable review pass, not a prose hint. First lock the crop system, environment structure, GxE logic, and yield or physiology endpoint; then judge whether the current manuscript answers the venue's real reader: agronomy reviewers who expect field-based, multi-environment evidence and crop-level general significance.

- **Do the pass:** Turn probable reviewer objections into a ledger with response evidence, manuscript location, and the decision-maker who must be convinced first.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Agricultural Systems for whole-system modeling, European Journal of Agronomy for agronomic breadth, Crop Science for cultivar or breeding emphasis; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Submission-ready gate:** do not give final advice until the pack's `resources/official-source-map.md` has been checked for upload-week rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Scope screen】field-based? ≥2 seasons/envs? field crop? general? — any red flags?
【Novelty】new insight of general relevance stated? [Y/N]
【Statistics】design-appropriate (mixed model / G×E)? [Y/N]
【Reproducibility】agronomic detail + data availability ready? [Y/N]
【Realistic outcome】reject / major / minor revision / accept
【Next】fcr-submission (or fcr-revision-and-rebuttal once decided)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — review model, reviewer count, scope-based desk-rejection grounds
