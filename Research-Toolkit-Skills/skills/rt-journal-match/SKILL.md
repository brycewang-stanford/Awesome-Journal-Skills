---
name: rt-journal-match
description: Use when an author asks "which journal should I send this to?" or needs the best resubmission target after a reject. Profiles the paper, shortlists candidate venues across 185+ packs, and ranks them into reach / match / safe with a resubmission ladder. Reads live venue facts from each pack's source-map; defers fit judgment to the venue's own topic-selection skill.
---

# Journal-Match (rt-journal-match)

The missing front-door question — *which venue?* — across the whole repository. Full
methodology + the stable venue index live in
[`shared-resources/journal-selection/journal-match.md`](../../../shared-resources/journal-selection/journal-match.md)
and [`venue-index.tsv`](../../../shared-resources/journal-selection/venue-index.tsv).

## When to trigger

- The author has a result/draft and no settled target.
- A paper was rejected and needs the best next venue.
- A "not a fit" signal means the scope/venue needs rethinking.

## What it does

1. **Profile the paper** — discipline + subfield, method/design, contribution type,
   setting/data/region, ambition (be honest).
2. **Shortlist** from `venue-index.tsv` by discipline / lane / region (long-tail venues →
   the discipline breadth bundle).
3. **Score** each candidate on **Fit × acceptance-odds × turnaround × cost/policy ×
   audience**, reading the live facts from each candidate's `resources/official-source-map.md`.
4. **Return reach / match / safe** (≈2–3 each) with one-line rationales + the live facts,
   then a **submit order and resubmission ladder**.

## Hard rules

- **Live facts from the source-map, never from memory** (fees, acceptance, turnaround, page
  limits, data policy).
- **Fit judgment defers** to the venue's `*-topic-selection` / `*-contribution-framing`.
- **Be honest about odds**; don't inflate a paper into a reach it can't clear.
- **Coverage honesty**: if a plausible venue is outside the index and its bundle, say so.

## Output format

```
【Paper profile】discipline / method / contribution / setting / ambition
【Reach】V — why; key live facts (desk-reject, turnaround, fee)
【Match】V — …
【Safe】V — …
【Submit order & ladder】V_top → if reject → V_next (what to change) → …
【Open questions】facts to re-verify in the source-map before submitting
```

## Anti-patterns

- Recommending only reaches (wastes the timeline) or only safes (undersells the paper).
- Ignoring `lane` — sending a qualitative/theory paper to an empirical-only venue.
- Treating the `tier` column as a precise ranking (it is an indicative bucket).

Next: once a target is chosen, `rt-execution-bridge` to run the analysis and
`rt-submission-readiness` to check the bar.
