# Journal-Selection — cross-journal matching capability

A venue-neutral capability layer that turns *"where should I send this paper?"* into a
ranked, reasoned shortlist across the whole repository. Complements the per-journal packs
(which answer *"how do I clear this venue's bar?"*) with the missing front-door question
*"which venue?"*.

## Contents

| File | What it gives an agent |
|---|---|
| [`journal-match.md`](journal-match.md) | The matching methodology: profile the paper (discipline / method / contribution / setting / ambition) → shortlist candidates from the index → score on Fit × acceptance-odds × turnaround × cost/policy × audience → return a reach/match/safe shortlist + a resubmission ladder. Reads volatile facts live from each pack's source-map. |
| [`venue-index.tsv`](venue-index.tsv) | **Stable** index of the 185 first-party depth packs: `pack_dir`, `display_name`, `discipline`, `tier` (indicative), `lane` (empirical / theory / qualitative / review), `region` (international / china), and the `source_map` path where the live facts live. No volatile fees/acceptance here by design. |

## Design principle (no fact duplication / no drift)

The index holds only **stable** attributes (discipline, lane, region, tier bucket, and a
pointer). Everything volatile — APC/fees, acceptance and desk-reject rates, turnaround,
page limits, data-and-code policy — stays in each pack's
`resources/official-source-map.md`, which the live-check campaign keeps current. The
matcher reads those at match time. This keeps a single source of truth and avoids the
journal-match layer drifting out of date.

## How to use

1. An agent (or a pack's `*-workflow` router) facing a "which journal?" question loads
   [`journal-match.md`](journal-match.md) and follows the six steps.
2. It filters [`venue-index.tsv`](venue-index.tsv) to candidate packs by discipline /
   lane / region, then opens each candidate's `source_map` for the live facts.
3. For venues outside the depth index, it consults the relevant discipline **breadth
   bundle** (listed in `journal-match.md` Step 5).

## Regenerating the index

`venue-index.tsv` is generated from the repository structure (first-party depth packs +
a curated discipline/tier/lane map). Regenerate when packs are added or reclassified:

```bash
python3 tools/gen_venue_index.py
```

Tier is an *indicative bucket* (`top-5 econ`, `top-3 finance`, `FT50/UTD24`, `field`),
not a ranking; refine the discipline/tier/lane maps in the generator as packs evolve.

---
*Part of the cross-journal capability layer alongside
[`../empirical-methods/`](../empirical-methods/). Discipline/tier are curated annotations;
fit and all volatile facts defer to each pack's own skills and source-map.*
