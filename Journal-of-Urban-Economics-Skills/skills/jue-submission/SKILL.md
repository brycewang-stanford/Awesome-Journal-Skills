---
name: jue-submission
description: Use when running the final pre-submission preflight for a Journal of Urban Economics (JUE) manuscript via Elsevier Editorial Manager — submission fee, single-anonymized review, format, the JUE: Insights short-paper track, and the cover-letter confidential-data exemption. Final checks; it does not draft content.
---

# Submission Preflight (jue-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on Editorial Manager
- Unsure which files, fees, and declarations the Elsevier submission expects
- Confirming format and the cover letter are JUE-compliant
- Deciding between a full JUE article and the **JUE: Insights** short-paper track
- The data is confidential and the exemption must be requested at submission

## Process facts (检索于 2026-06；以官网为准)

- JUE is the **Elsevier** field flagship in urban economics (ISSN 0094-1190; bimonthly; founded 1974 by Edwin Mills). Submission is through **Elsevier Editorial Manager**.
- **Review model:** single-anonymized (single-blind) — reviewers are anonymous to authors; author identities are visible. Editors first assess suitability; suitable papers go to (typically ≥2) reviewers.
- **Submission fee:** a **nonrefundable US$100** fee is charged on new submissions, paid during submission; the paper is considered only after payment (待核实 exact amount and any waivers live).
- **Co-editors-in-chief:** Nathaniel Baum-Snow (Toronto) and Kristian Behrens (UQÀM) (检索于 2026-06；以官网为准).
- **Mandatory replication policy:** data + code deposited to a major repository at **acceptance, before publication**; proprietary/confidential data requires an **exemption requested in the submission cover letter** (see `jue-replication-package`).
- **JUE: Insights** short-paper track: ≤6,000 words and ≤5 exhibits; each exhibit below five buys +200 words (a zero-exhibit paper ≤7,000 words); manuscripts must carry the **"JUE: Insights"** title prefix; same peer-review process (检索于 2026-06；以官网为准).

## Preflight checklist

### Format & style
- [ ] Manuscript follows Elsevier/JUE format; exhibits and notes self-contained; references complete
- [ ] Abstract present (re-check exact word limit live; references in abstract given in full) (待核实)
- [ ] **Standard errors reported**; follow the journal's significance-reporting convention (待核实 exact style)
- [ ] Maps/figures legible in grayscale; spatial units, scale, and CRS clear in exhibits
- [ ] If JUE: Insights — title carries the "JUE: Insights" prefix; ≤6,000 words / ≤5 exhibits respected

### Files & fees on Editorial Manager
- [ ] Main manuscript uploaded; exhibits and any online appendix in the expected formats
- [ ] **US$100 submission fee** ready (nonrefundable; paper considered only after payment)
- [ ] Cover letter prepared: contribution, venue fit (why JUE not RSUE/JEG/JPubE), and any **confidential-data exemption** request
- [ ] Suggested/excluded reviewers per the form, if requested
- [ ] Replication folder prepared (deposit due at acceptance, but assembled now — see `jue-replication-package`)

### Declarations
- [ ] Competing-interests / funding declaration per Elsevier policy
- [ ] Confirmed not under review elsewhere; authorship and contributions accurate
- [ ] Data-availability statement consistent with the replication plan (or the exemption)
- [ ] Cover letter answers "is this JUE?" and "is the design credible?" up front
- [ ] A single best exhibit (map + design figure) makes the result legible at a glance

## Anti-patterns

- Submitting without the **US$100 fee** ready (the paper is not considered until it is paid)
- Treating the **APC** (open-access charge) as if it were the submission fee — they are different
- Forgetting the **"JUE: Insights" title prefix** on a short-paper submission, or exceeding its limits
- Confidential data with **no exemption request in the cover letter**
- Naive (non-spatial) standard errors left in the tables at submission
- A cover letter that does not pre-empt the "why not a sibling journal" question

## What to expect after submitting

- **Editor triage first.** The co-EiCs (or a handling editor) assess suitability before any referee sees the paper; a poorly-fit or weakly-identified spatial paper is desk-rejected here. This is why the cover letter must pre-empt the "why JUE" and the obvious sorting/SUTVA objections.
- **Then typically ≥2 referees** under single-anonymized review. Expect the design referee and the urban-economics referee personas (see `jue-referee-strategy`).
- **Outcomes** are the usual reject / major or minor revision / accept; a major revision at a field flagship is a real opportunity, not a soft reject — route the decision to `jue-rebuttal`.
- **Open-access option.** If accepted, an APC applies only if you choose open access; this is separate from the submission fee and is not a condition of acceptance (检索于 2026-06；以官网为准).

## Last-mile traps specific to JUE

- The **submission fee is nonrefundable even on desk-reject** — make sure the paper is genuinely JUE-fit before paying.
- Spatial standard errors and a map of the identifying variation are the two things a JUE editor scans first; do not submit without them.
- The replication folder need not be deposited at submission, but the data-availability statement and any **confidential-data exemption** must be in the cover letter *now*.

## Output format

```text
【Format】Elsevier/JUE format; SEs reported; grayscale-legible exhibits? [Y/N]
【Track】full article / JUE: Insights (prefix + ≤6,000w/≤5 exhibits)?
【Fee】US$100 nonrefundable ready? [Y/N]
【Cover letter】contribution + venue fit + confidential-data exemption (if any)? [Y/N]
【Replication】folder assembled (deposit at acceptance)? [Y/N]
【Declarations】competing interests / funding / data-availability? [Y/N]
【Next step】submit via Editorial Manager → jue-rebuttal when the decision arrives
```

## Cover letter: the one document that does framing work

For a JUE submission the cover letter is not a formality — it is where you do the framing the manuscript format cannot. In a few tight paragraphs: state the spatial question and the headline magnitude; name the strand and why this is a JUE contribution rather than an RSUE/JEG/JPubE one; flag the identifying variation and that the obvious spatial confounds (sorting, SUTVA, spatial SEs) are addressed; and, if the data is proprietary or confidential, make the **replication-policy exemption request here** with the access path. Suggested/excluded reviewers, if requested, go in the form. A cover letter that pre-empts the editor's first two questions — "is this JUE?" and "is the design credible?" — materially lowers desk-reject risk.

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
