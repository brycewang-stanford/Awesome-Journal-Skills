---
name: wp-transparency-and-data-policy
description: Use when preparing replication / transparency materials for a World Politics manuscript. World Politics requires authors who rely on quantitative data to deposit replication materials in the World Politics Dataverse after acceptance and before publication, with an explanatory file that lets others replicate the exact numerical results; embargoes up to two years may be approved by the editorial committee. Prepares the package; it does not waive requirements.
---

# Transparency & Data Policy (wp-transparency-and-data-policy)

World Politics has a **Dataverse archive**, and **authors who rely on quantitative data must deposit**
their materials there **after a piece is accepted but prior to publication**. The deposited file must
let others **replicate the exact numerical results**. Build the package as you go so acceptance does
not stall.

## When to trigger

- Building the replication package for a quantitative or mixed-method paper
- A manuscript has been **accepted** and you must deposit before publication
- Original/proprietary data require an **embargo** and you need the approval path
- Documenting qualitative/comparative-historical sources for transparency

## What World Politics requires (verify current wording on the policy page)

1. **Deposit to the World Politics Dataverse.** After acceptance and **before publication**, authors
   relying on quantitative data place materials in this trusted digital repository — not a personal
   site or generic cloud link.
2. **What to include.** The original data; specialized computer programs; lists of program recodes;
   extracts of existing data files; and — most importantly — an **explanatory file (README)** that
   describes what is in the data, how it was created, the sources it was drawn from, and **how to
   replicate the exact numerical results**.
3. **State availability in the article.** The published piece must indicate where/how the data are
   available.
4. **Embargoes.** Embargoes on original, proprietary data for **up to two years** beyond publication
   (or other special circumstances) may be granted, but require **editorial-committee approval before
   publication**. Junior scholars collecting original data for other projects may request longer.

## Qualitative & comparative-historical transparency
- Document the **evidentiary basis**: which archival documents, interviews, or fieldnotes support which
  inferential step. Evidence tables and active citation (ATI) make process-tracing claims auditable.
- Use access-controlled repositories (e.g., QDR) where sensitivity or human-subjects concerns require
  it; reconcile with the **APSA Principles and Guidance for Human Subjects Research** (see
  `wp-review-process`).

## Build-as-you-go checklist

- [ ] One **master script** regenerates **every** table and figure from raw/constructed data
- [ ] **README** documents contents, construction, sources, and how to replicate exact results
- [ ] **Seeds** set and reported for every stochastic step
- [ ] Software/package **versions pinned** (`renv.lock` / `requirements.txt` / recorded installs)
- [ ] Exhibit numbers in the manuscript **match** the package output exactly
- [ ] Data-availability statement drafted for the article
- [ ] Embargo (if any) justified and slated for **editorial-committee approval** before publication
- [ ] Qualitative sources documented (evidence tables / access-controlled repository where needed)

## Anti-patterns

- Treating the deposit as optional when the paper relies on quantitative data (it is required)
- Depositing code that does not reproduce the published numbers
- A personal URL instead of the World Politics Dataverse
- Assuming an embargo without editorial-committee approval
- Undocumented, un-seeded, unpinned code that "works on my machine"

## Replication-objection patterns and the venue-specific fix

The deposit is checked against the published numbers, so the failures here are about reproducibility
and provenance rather than design.

| Objection at deposit/replication | The fix this skill drives |
|----------------------------------|----------------------------|
| "Code doesn't reproduce the published table" | One master script that regenerates every exhibit; match numbers exactly |
| "Stochastic step won't replicate" | Set and report seeds for bootstrap, randomization, sampling |
| "Provenance unclear" | README documenting sources, construction, recodes, and replication steps |
| "Proprietary data can't be shared" | Request an editorial-committee-approved embargo (up to two years) before publication |
| "Qualitative claims unauditable" | Evidence tables / active citation; access-controlled repository where sensitivity requires |

## Worked micro-example (illustrative)

A hypothetical accepted paper on **trade agreements and democratic backsliding** stages its package:

```text
Master script: make.R → regenerates Tables 1–4 + Figures 1–3 from /raw and /derived
Seeds:         set.seed(20260601) before the bootstrap in model 3
Versions:      renv.lock pins R 4.x + 18 packages
Provenance:    README maps V-Dem v14 + DESTA to each constructed variable
Embargo:       one proprietary firm-survey extract → 2-year embargo, committee approval requested
Check:         a clean-machine run reproduces every published number before deposit
```

The clean-machine run is the gate; "works on my machine" is not deposit-ready. (The Dataverse,
embargo, and timing rules are policy that can change — confirm against the current data-policy page.)

## Output format

```
【Repository】World Politics Dataverse — package staged? [Y/N]
【Reproduces exact results?】master script verified locally? [Y/N]
【Documentation】README + provenance + seeds + pinned versions? [Y/N]
【Data-availability statement】drafted for the article? [Y/N]
【Embargo?】needed? justified for editorial-committee approval?
【Qualitative transparency】evidence/sources documented? [Y/N/NA]
【Next】wp-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling and qualitative-transparency options (QDR, ATI)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — World Politics Dataverse policy and embargo terms
