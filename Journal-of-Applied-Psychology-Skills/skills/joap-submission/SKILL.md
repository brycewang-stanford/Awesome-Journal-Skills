---
name: joap-submission
description: Use when running the final pre-submission preflight for the Journal of Applied Psychology (JAP) via Editorial Manager — APA 7th-edition style, the APA submission/masking checklist, anonymization for masked review, the structured abstract, the data-availability/TOP statement, and persistent identifiers for data/materials/code. Final checks; it does not draft content.
---

# Submission Preflight (joap-submission)

The last check before submitting through **Editorial Manager** (`editorialmanager.com/apl`). Three
things sink JAP submissions most often: **a missing or weak theoretical contribution surfacing late**,
**broken masking**, and **incomplete open-science compliance**. Verify volatile specifics (length caps,
abstract limit, checklist contents, current editor) on the official APA page first.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure what the masking and open-science requirements demand
- Confirming the abstract, anonymization, data-availability statement, and deposits are in order

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** American Psychological Association (APA). ISSN 0021-9010 / e-ISSN 1939-1854.
- **Portal:** **Editorial Manager**, `editorialmanager.com/apl`.
- **Review:** **masked (anonymized)** — keep author identity out of the manuscript and repository links.
- **Submission checklist:** completing the **APA-published submission/masking checklist** is required at
  upload and signifies you have read and will follow the guidelines.
- **Style:** **APA 7th edition** throughout.
- **Article types:** Feature Article (length commensurate with contribution); Research Report (tighter;
  confirm current page cap, 待核实); theory-development / integrative review; qualitative; meta-analysis.
- **Abstract:** structured, content-bearing; confirm the **current word limit** (commonly ~250 words; 待核实).
- **Open science (TOP):** empirical work (including meta-analyses) held to the **TOP framework** —
  data/materials/code availability with DOIs, a **data-availability statement**, and preregistration
  weighed (effective for empirical submissions; confirm current TOP level, 待核实).
- **Current Editor:** Mo Wang (University of Florida), Editor-in-Chief from January 2026, succeeding Lillian T. Eby (web-verified 2026-06-22; re-verify the live masthead before submission).

## Preflight checklist

### Style & format
- [ ] APA 7th edition throughout (headings, statistics with ES + CI, references)
- [ ] Article type chosen; length appropriate (Feature Article vs Research Report cap, 待核实)
- [ ] Structured abstract within the current limit (待核实); states contribution, design, samples, result
- [ ] Tables/figures APA 7th; Table 1 has reliabilities; path tables/figures carry CIs and fit indices

### Masking (for anonymized review)
- [ ] No author names/affiliations anywhere in the manuscript
- [ ] Self-citations neutralized ("as we showed in…" removed)
- [ ] Repository / preregistration links **anonymized** (e.g., OSF anonymized view)
- [ ] Identifying file metadata stripped (document properties, tracked-change authors)
- [ ] Separate, non-anonymous title page prepared as a distinct file

### Open science (TOP)
- [ ] **Data** deposited + DOI + codebook (or justified exemption)
- [ ] **Materials** (scales, manipulations, instructions) deposited + DOI
- [ ] **Analysis code** deposited; reproduces results in a fresh session
- [ ] **Data-availability / transparency statement** drafted per current TOP wording
- [ ] **Prior-use disclosure** if the dataset overlaps another paper
- [ ] Preregistration linked (anonymized); confirmatory/exploratory split consistent

### Stats & rigor
- [ ] Measurement model reported (CFA fit + reliability) before structure
- [ ] Effect sizes + CIs for key paths; indirect effects with bootstrap/Monte Carlo CIs
- [ ] Nesting modeled (ICC/r_wg); CMV remedies stated
- [ ] Full disclosure of N-determination, exclusions, conditions, measures

## Worked micro-example — preflight verdict (illustrative)

Running the servant-leadership package through the gate the night before upload:

```
Style:      APA 7th throughout; structured abstract drafted (confirm limit) → PASS*
Contribution: cross-level mechanism + boundary stated by p.3 → PASS
Masking:    no names; self-cites neutralized; OSF anonymized-view links;
            PDF metadata stripped; separate title page → PASS
Open sci:   data + materials + code each have a DOI; data-availability
            statement + prior-use note; experiment preregistration linked → PASS
Stats:      CFA fit + reliabilities reported; indirect = .13, 95% CI [.05, .23];
            multilevel model + ICC/r_wg; CMV remedies declared → PASS
Verdict:    ready to upload to Editorial Manager.
*Re-confirm the current abstract limit and Research Report cap on the APA page.
```

## Last-mile failure modes that trigger a return

| Failure | Caught by | Quick fix |
|---------|-----------|-----------|
| Author name in self-citation or OSF link | masking check | neutralize self-cites; switch to anonymized view |
| Abstract over the current limit | abstract check | cut to the limit; keep contribution + design + result |
| "Data on request" instead of a DOI | open-science check | deposit and mint a persistent identifier |
| No data-availability statement | TOP check | draft it from the live DOIs |
| Table 1 missing reliabilities; paths lack CIs | exhibit check | add ω to the diagonal; add CIs + fit indices |

> Volatile specifics (length caps, abstract limit, TOP level, checklist contents, current editor) change.
> Re-confirm every item above against the journal's current submission guidelines before relying on it.
> See [`templates/checklist.md`](templates/checklist.md) for a copy-paste preflight list.

## Anti-patterns

- Submitting with the theoretical contribution buried or absent
- Broken masking (names, self-references, or identifying repository links)
- "Available on request" instead of persistent DOIs; missing data-availability statement
- Abstract over the current limit or missing the contribution/design/result
- Tables/figures without reliabilities, CIs, or fit indices

## Output format

```
【Style】APA 7th + article type + abstract within limit (待核实)? [Y/N]
【Contribution legible early?】[Y/N]
【Masking】manuscript + self-cites + repo links + metadata + title page? [Y/N]
【Open science】data + materials + code + DOIs + availability statement? [Y/N]
【Stats】measurement model + ES/CIs + indirect CIs + nesting + disclosure? [Y/N]
【Next】await decision → joap-rebuttal on R&R
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — copy-paste pre-submission preflight checklist
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — repositories, DOIs, `papaja`, SEM/HLM/meta tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official APA Journal of Applied Psychology URLs behind every fact in this pack
