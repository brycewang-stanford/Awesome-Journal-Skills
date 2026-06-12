---
name: fcr-revision-and-rebuttal
description: Use when writing the response to a Field Crops Research (FCR) revision decision (major or minor) and revising the manuscript. FCR reviewers commonly press on scope/generality, statistics and G×E, reproducibility detail, and a discussion that interprets rather than repeats. The response must address every point while protecting the contribution. Structures the response letter; it does not fabricate new results.
---

# Revision & Rebuttal (fcr-revision-and-rebuttal)

An FCR **revise** decision is an opportunity, not a formality. The response letter must move **every
reviewer** toward acceptance while keeping the editor confident the revision converges. FCR reviewers
tend to focus on a recurring set of agronomy concerns — answer them with **data and detail**, not
assertion.

## When to trigger

- A major- or minor-revision decision arrived and you are planning the response
- Reviewers disagree and you must reconcile their requests
- A reviewer wants additional environments, statistics, or reproducibility detail
- Writing the cover note to the editor summarising the revision

## Strategy

1. **Read the editor's letter as the rubric.** The editor signals the decisive points; solve those
   first. The editor adjudicates disagreements among reviewers.
2. **Point-by-point, every comment addressed.** Quote each comment, then respond. Never skip one —
   silence reads as non-compliance.
3. **Concede or rebut explicitly, with evidence.** For each: did what was asked (say where, with the
   new text/table/figure number), or push back **respectfully with a reason** (design, agronomy, or
   data). A well-argued disagreement beats a capitulation that weakens the paper.
4. **Reconcile conflicting reviewers openly.** When two reviewers want opposite things, say so, choose
   a principled path, and explain the trade-off to the editor.
5. **Protect the contribution and scope.** Add analyses/robustness; resist changes that dilute the
   general-relevance claim or over-fit to one environment.

## Common FCR reviewer asks (anticipate them)

| Reviewer concern | How to respond |
|------------------|----------------|
| "Generality / scope unclear" | restate multi-environment evidence; scope the claim explicitly |
| "Wrong/incomplete statistics" | refit with the correct mixed model / error structure; report SED/LSD, G×E |
| "Methods not reproducible" | add cultivar, soil, weather-vs-phenology, management, design detail |
| "Discussion repeats results" | rewrite to interpret and place in agronomic context |
| "Conclusions overreach" | add scope conditions; align conclusions to the data |
| "More seasons/sites needed" | add available environments or justify and bound the claim |

## Response-letter format

For each reviewer comment:

```
> [Quoted reviewer comment]

Response: [What we did / why we respectfully disagree].
Change: [Section/page/table-figure number where the revision appears].
```

Open with a short **summary of the main changes** to the editor; group by reviewer; end each entry
with the location of every change so the editor can verify quickly. Keep the data-availability
materials and exhibits in sync with any new analyses.

## Referee-pushback playbook (FCR-specific fixes)

These are the objections FCR reviewers raise most, paired with the response that moves the needle.
Match the fix to the objection.

| Reviewer pushback | The venue-specific fix |
|-------------------|------------------------|
| "A single site-season cannot support a yield claim" | report the across-environment mean **and** the environment×treatment term; scope the claim |
| "The agronomic mechanism is not established" | link the yield effect to a measured process (N uptake, RUE, WUE); add the path, not just correlation |
| "Statistics ignore the trial's blocking structure" | refit with the correct whole-plot/sub-plot error; re-report adjusted means + SED |
| "Result may be confounded with environment" | show the interaction (AMMI/GGE or its variance) rather than averaging it away |
| "Discussion restates results" | rewrite to interpret: why this environment, what process, where it travels |

## Worked rebuttal vignette (illustrative)

*Illustrative exchange; wording is a template.* Reviewer 2 writes: *"The cultivar advantage is
significant, but the one-way ANOVA ignores the split-plot structure, and 'improves yield' is too
broad."* A strong response concedes the statistics and protects the contribution at once: refit the
mixed model (cultivar as sub-plot, environment×cultivar random); report the advantage as **~0.9 t ha⁻¹
in 3 high-N environments, non-significant in 2 dry ones**; revise the conclusion to "raises yield in
high-yielding environments, no penalty elsewhere"; cite the new Table 3 and SED column. The **same
re-analysis** answers both the methods and over-reach objections, keeping dataset and biplot in sync.

## Anti-patterns

- Ignoring or quietly merging away a comment without a visible response
- Capitulating to a request that breaks the agronomic logic just to please a reviewer
- Defensive or dismissive tone toward reviewers
- "We thank the reviewer" with no actual change or argued reason
- New analyses that drift out of sync with the deposited data or the exhibits

## Output format

```
【Editor's decisive points】addressed first? [list]
【Coverage】every reviewer comment answered? [Y/N]
【Concede vs rebut】each tagged with evidence + change location
【Reviewer conflicts】reconciled and explained to editor? [Y/N]
【Contribution/scope protected】no dilution of general relevance? [Y/N]
【Data/exhibits in sync】updated with new analyses? [Y/N]
【Next】resubmit via Editorial Manager
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — statistics packages for requested re-analyses
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — review model and decision categories
