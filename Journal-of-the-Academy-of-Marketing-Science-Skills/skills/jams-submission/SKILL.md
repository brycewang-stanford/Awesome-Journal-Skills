---
name: jams-submission
description: Use when running the final pre-submission preflight for a Journal of the Academy of Marketing Science (JAMS) manuscript — Springer Editorial Manager portal, double-anonymized blinding, APA style, the blinded title page, data/code availability, and declarations. Checks readiness to submit; it does not handle the post-decision response (jams-rebuttal).
---

# Pre-Submission Preflight (jams-submission)

## When to trigger

- "We're submitting this week" — the last check before pressing submit on Editorial Manager
- Unsure what the Springer portal requires (anonymized file, title page, statements)
- Verifying blinding, APA style, and required declarations are in place
- Confirming the data/code availability statement is prepared

> Always re-verify current limits and required files on the official JAMS submission guidelines (link.springer.com/journal/11747) before submitting — specifics change. Facts below were checked 2026-06; volatile items are marked 检索于 2026-06；以官网为准 or 待核实.

## Verified JAMS / Springer specs (confirm current values)

- **Publisher / owner:** Springer, for the **Academy of Marketing Science (AMS)**. ISSN **0092-0703** (print) / **1552-7824** (online); bimonthly.
- **Submission portal:** Springer **Editorial Manager** for JAMS (reached via the journal's "Submit manuscript" link). Online submission only.
- **Review model:** **double-anonymized** (double-blind) — the manuscript file must be fully anonymized; author identities and reviewer identities are mutually concealed.
- **Citation style:** **APA** author–date is JAMS house style (检索于 2026-06；以官网为准).
- **Co-Editors-in-Chief:** Stephanie M. Noble and Charles H. Noble (University of Tennessee), since June 2024 (verified 2026-06-22 via Springer JAMS home + AMS; re-verify the masthead before submission).
- **Abstract:** structured/concise abstract, typically **~200–250 words** (待核实 — confirm exact limit and whether structured on the official guidelines).
- **Length / page limit:** JAMS does not publish a single hard page count the way some AMA journals do; follow the article-type guidance on the official page (待核实 — confirm current limit).
- **Data & code:** Springer **research-data policy** applies; prepare a **data (and code) availability statement** and deposit references (e.g., OSF / Mendeley Data) where applicable (检索于 2026-06；以官网为准).
- **Fees:** subscription publication has **no submission fee / no APC**; **Open Access (Hybrid OA)** is optional and carries an article-processing charge for accepted articles only — the Springer hybrid OA APC is **£3,090 GBP / $4,990 USD / €3,990 EUR** (plus applicable VAT/local tax) as of 2026-06-23 (often covered by Springer transformative agreements). Re-verify the current APC before submission.

## Pre-submission checklist

### Anonymization (double-anonymized)
- [ ] Manuscript file has **no** author names, affiliations, acknowledgments, or funding
- [ ] Self-citations worded neutrally ("prior research (Author, 2020)"), not "our earlier work"
- [ ] File properties/metadata and file names scrubbed of identity
- [ ] Any preregistration or data-repository links anonymized (no identity leakage)

### Format & style
- [ ] **APA** author–date citations; reference list complete and reconciled with in-text cites
- [ ] Abstract within the journal's limit; keywords supplied
- [ ] Tables/figures self-contained, with effect sizes and uncertainty (not stars only)
- [ ] Conceptual model figure matches the hypothesis list
- [ ] Article type follows the official guidelines (length, structure)

### Files for Editorial Manager
- [ ] Anonymized main manuscript (text + exhibits, or as the portal specifies)
- [ ] **Separate title page** with all authors, affiliations, ORCID iDs, acknowledgments, funding
- [ ] Cover letter (fit to JAMS; theoretical **and** managerial contribution; not under review elsewhere)
- [ ] Supplementary/online appendix file(s) for material kept out of the main text

### Declarations & transparency
- [ ] **Data (and code) availability statement** prepared per Springer policy
- [ ] Human-subjects/IRB / ethics approval stated where applicable (on the title page)
- [ ] Conflicts of interest and funding disclosed (title page)
- [ ] No concurrent submission; conference/working-paper versions disclosed in the cover letter
- [ ] AI not listed as an author; any AI-assistance disclosed per policy

## Editorial Manager operation notes

- Reach the portal from the journal's "Submit manuscript" link (link.springer.com/journal/11747); keep your account and **ORCID** current.
- Choose **article type, keywords, and area/classifications** carefully — they route the manuscript to the area editor whose domain matches the paper. A mismatch slows review and risks an unsympathetic read.
- Upload the **anonymized manuscript** and the **separate title page** into the slots the system designates; the title page (not the blinded file) carries authors, affiliations, ORCID, funding, and acknowledgments.
- **Preview the system-built PDF** before final submission to confirm exhibits render and no identity leaked into headers, properties, or file names.
- Have the **cover letter** ready in the portal: state fit to JAMS, the theoretical *and* managerial contribution, and that the paper is not under review elsewhere.

## Anti-patterns

- Self-identifying language ("in our 2019 study") or a link that reveals identity in the blinded file
- Wrong (non-APA) citation style straight from a reference manager
- A missing or generic cover letter that omits the managerial contribution JAMS expects
- No data/code availability statement, or no plan for a repository deposit
- Treating the optional OA APC as a mandatory submission fee
- Quoting a page/abstract limit as fixed without checking the current guidelines
- Generic keyword/area choices that misroute the manuscript to the wrong editor

## Output format

```text
【Anonymization】no identity in file/metadata/links: pass/fix
【Style】APA citations; abstract within limit; keywords: pass/fix
【Files】anon manuscript / separate title page (ORCID) / cover letter / appendix: ready?
【Cover letter】states fit + theory + managerial contribution? yes/fix
【Transparency】data/code availability statement + repo plan: ready?
【Declarations】IRB / COI / funding / no concurrent submission: complete?
【Source check】volatile items (limit, APC, editors) re-verified or marked 检索于 2026-06
【Next step】submit via Editorial Manager → jams-review-process
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Springer/JAMS URLs and volatile facts
