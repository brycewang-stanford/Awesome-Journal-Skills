---
name: gcb-submission
description: Use when running the final pre-submission preflight for Global Change Biology (GCB) via ScholarOne / Manuscript Central — article-type selection, word/abstract caps, graphical abstract, data availability statement, and required files. Final checks; it does not draft content.
---

# Submission Preflight (gcb-submission)

The last check before pressing submit on **ScholarOne / Manuscript Central** (`mc.manuscriptcentral.com/gcb`).
GCB desk-rejects heavily, so the preflight is about removing avoidable reasons to bounce: wrong scope
framing, missing graphical abstract, over-length text, or a non-compliant data statement. Verify
volatile specifics on the official page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata ScholarOne expects
- Confirming the chosen article type's caps and required elements are met

## Process facts (verify volatile items on the official page)

- **Publisher:** Wiley.
- **Portal:** **ScholarOne / Manuscript Central** (`mc.manuscriptcentral.com/gcb`).
- **Article types:** Research Articles, Technical Advances, Reviews, GCB Reviews, Mini Reviews,
  Opinions, and Perspectives; GCB Reviews should be treated as commissioned unless the live guidance
  states otherwise.
- **Length:** Research Articles currently route to an **up to 8,000-word** cap; confirm what the cap
  includes on the live page.
- **Abstract:** **300-word limit**; **6–10 keywords or phrases**.
- **Graphical abstract:** **required** — depicts the driver-to-response mechanism.
- **Data/code:** **data availability statement** required; data and code archived with a **DOI** as a
  condition of publication ("available on request" not accepted).
- **Review model:** editor-mediated expert review; live-check current anonymity / transparent-review
  options.

## Preflight checklist

### Article type & length
- [ ] Article type chosen and its word cap met (confirm current cap)
- [ ] Abstract within 300-word limit, states aim + approach + quantified result + conclusion
- [ ] 6–10 keywords

### Required elements
- [ ] **Graphical abstract** showing driver → response mechanism
- [ ] **Data availability statement** naming repository + access (not "on request")
- [ ] Data and code archived (or staged) with a DOI per policy (see `gcb-reporting-and-data-policy`)
- [ ] Figures/tables self-contained and accessible (see `gcb-figures-and-tables`)

### Format & metadata
- [ ] Manuscript formatted per current GCB/Wiley template; author-date citations consistent
- [ ] Cover letter establishes scope fit + advance (see `gcb-cover-letter`)
- [ ] Author list, ORCID, affiliations, conflicts, and funding complete
- [ ] Ethics / permits / sampling compliance stated where applicable

## Last-mile failure modes at upload

These are the avoidable bounces that surface in the final hour. Catch each one here rather than in a
desk-reject letter.

| Failure mode | Where it bites | Pre-upload fix |
|--------------|----------------|----------------|
| Graphical abstract missing/non-mechanistic | Required element check | Supply a driver → response figure |
| Abstract over cap | Metadata field | Trim to the current limit |
| Data statement says "on request" | Compliance screen | Name repository + DOI + access route |
| Wrong article type for the content | Editorial triage | Match type to contribution and its caps |
| Missing ORCID / conflicts / funding | ScholarOne fields | Complete all author metadata |

## Worked micro-example (illustrative)

A meta-analysis is queued for upload. The preflight catches three things: the graphical abstract was a
forest plot (a result, not the mechanism) — replaced with a warming → biomass-response arrow; the
abstract ran an illustrative 340 words against an assumed ~300 cap — trimmed; and the data statement read
"on request" — rewritten to name the Dryad and Zenodo DOIs with the access route. Article type is
confirmed as a Research Review (open section), not an unsolicited GCB Review. With those fixed, the
remaining metadata fields pass. Word counts and the cap are illustrative; verify the current caps before
submitting.

## Referee/editor pushback this preflight pre-empts

- "Scope reads as regional" → confirm the cover letter and abstract lead with the global-change
  mechanism.
- "Non-compliant data statement" → verify a DOI deposit is named, not request-only access.
- "Over-length" → confirm the manuscript and abstract meet the current article-type caps.

## Anti-patterns

- Missing or non-mechanistic graphical abstract (site map / phylogeny)
- "Data available on request" instead of a DOI deposit (rejected)
- Over-length manuscript or an abstract over the cap
- Wrong scope framing (local/conservation) that invites a desk reject
- Submitting an unsolicited "GCB Review" (use Research Reviews)

## Output format

```
【Article type】... (cap met? confirm current cap) [Y/N]
【Abstract】word count (300-word limit) + 6–10 keywords
【Graphical abstract】driver → response present? [Y/N]
【Data statement + DOI deposit】names repo, not "on request"? [Y/N]
【Cover letter + metadata】scope fit, ORCID, conflicts complete? [Y/N]
【Next】await decision → gcb-revision-and-rebuttal on revision
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — submission portal, repositories, reference/template tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official GCB URLs behind every fact in this pack
