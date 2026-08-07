---
name: rt-journal-match
description: Use when an author asks "which journal should I send this to?" or needs the best resubmission target after a reject. Profiles the paper, shortlists candidates from an index of 743 venues with tools/match_venues.py, and ranks them into reach / match / safe with a resubmission ladder. Reads live venue facts from each pack's source-map; defers fit judgment to the venue's own topic-selection skill.
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
   setting/data/region, ambition (be honest). Write it down once, in the shape of
   [`paper-profile.yml`](../../../shared-resources/journal-selection/paper-profile.md);
   every later skill reads the same file instead of re-deriving it.

2. **Shortlist** — run the matcher rather than reading the index by eye:

   ```bash
   python3 tools/match_venues.py \
       --title "..." --abstract "..." \
       --discipline economics/labor --lane empirical --top 15
   ```

   `--discipline` is a **prior, not a filter**: the discipline and its adjacents
   ([`discipline-adjacency.tsv`](../../../shared-resources/journal-selection/discipline-adjacency.tsv))
   are boosted, but a strong match elsewhere still surfaces, because Step 1 is a
   judgement that is sometimes wrong. Add `--only-discipline` when you are certain,
   `--exclude <venue_id>` for venues that have already rejected the paper,
   `--json` to pipe it. `--list-disciplines` prints the vocabulary.

   Every row names where to read more — `source_map` for a depth pack,
   `profile_path` for a breadth profile — and the terms it matched on, so a
   nonsense hit is visible as a nonsense hit.

   **Read the warnings.** The matcher flags *weak evidence* when its leading
   candidates each rest on one or two shared words — a ranking built on that is
   close to noise, because words the language reuses ("sensor", "generation",
   "network") will out-score a genuine subject match. It flags a *coverage gap*
   when nothing in the discipline you named scored at all: the prior can only
   re-rank venues that matched, never conjure one. Either warning means **do not
   pass the list on as a shortlist** — add the abstract, re-check the discipline
   label, or report that the subject area is thin in the index and route to
   [`rt-venue-integrity`](../rt-venue-integrity/SKILL.md).

   The matcher is measured: **R@10 = 41.5%** from a bare title, on a held-out half of a
   1,738-paper gold set ([`eval/RESULTS.md`](../../../shared-resources/journal-selection/eval/RESULTS.md)).
   That is a floor for one thin query, not the capability — it is why step 3 exists.
   The per-discipline table there is worth reading before trusting a result: coverage is
   uneven, and life sciences and natural science are visibly the thinnest.

3. **Score** each candidate on **Fit × acceptance-odds × turnaround × cost/policy ×
   audience**, reading the live facts from each candidate's `resources/official-source-map.md`.
   Never quote a fee, acceptance rate, turnaround or page limit from memory.

4. **Return reach / match / safe** (≈2–3 each) with one-line rationales + the live facts,
   then a **submit order and resubmission ladder** — seed the ladder from
   [`ladder.tsv`](../../../shared-resources/journal-selection/ladder.tsv) (candidate
   adjacency, not a ranking) and apply your own fit/odds judgement to it.

5. **Cost the ladder** with [`rt-ladder-ev`](../rt-ladder-ev/SKILL.md) whenever the
   author is under a clock or is choosing between two orders. The sequence, not the
   venue, is what costs a year.

## Hard rules

- **Live facts from the source-map, never from memory** (fees, acceptance, turnaround, page
  limits, data policy).
- **Fit judgment defers** to the venue's `*-topic-selection` / `*-contribution-framing`.
- **Be honest about odds**; don't inflate a paper into a reach it can't clear.
- **Coverage honesty**: if a plausible venue is outside the index and its bundle, say so —
  and hand to [`rt-venue-integrity`](../rt-venue-integrity/SKILL.md) before the author
  submits somewhere unverified.
- **The matcher retrieves; you recommend.** Never pass its ranking through as a
  shortlist: open the packs first.

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
- Reporting the matcher's top-10 as the answer. It is a reading list.
