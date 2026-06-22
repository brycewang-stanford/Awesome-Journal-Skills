---
name: expecon-submission
description: Use when running the final pre-submission preflight for an Experimental Economics (ExpEcon) manuscript via the Editorial Manager portal — the no-deception/incentive gates, instructions-at-submission rule, anonymous review, and ESA data-deposit prep. Final checks; it does not draft content.
---

# Submission Preflight (expecon-submission)

## When to trigger

- "Submitting tomorrow" — the last check before uploading to Editorial Manager
- Unsure which files the ExpEcon submission expects (manuscript, instructions, package)
- Confirming the manuscript is anonymized for double-blind review
- Verifying the no-deception and incentive statements are in the paper before it goes out

## Process facts (检索于 2026-06；以官网为准)

- Experimental Economics is the **official journal of the Economic Science Association (ESA)**; as of **January 2025 (Vol. 28)** it is published by **Cambridge University Press** and is **fully open access (CC BY)** — it moved from Springer (verified 2026-06-22). Re-confirm the current platform and any APC/waiver before submitting.
- **Editors (verified 2026-06-22):** David Huffman (Cornell), Friederike Mengel (Essex), Andreas Ortmann (UNSW), Arno Riedl (Maastricht), and Marta Serra-Garcia (UC San Diego) — co-editors rather than a single EiC. Re-verify on the Cambridge editorial-board page before naming one.
- **Submission portal:** **Editorial Manager** (editorialmanager.com/eec). Review is **anonymous (double-blind)**; accepted papers require the approval of **two editors**.
- **Hard gates:** the journal only considers studies that **do not deceive participants** and in which **participants are incentivized**. These are entry conditions, not preferences.
- **Instructions at submission:** the **instructions participants received must be supplied at the time of submission** (reviewers check them for deception and comprehension). Methodology and replication papers are explicitly in scope.
- **Data appendices:** authors submit separate **data appendices** attached to the article page on publication, consistent with the **ESA Data and Replication Policy** (trusted-repository deposit). Exact length/abstract limits and APC/waiver terms are **待核实** — confirm on the current Cambridge journal page.

## Preflight checklist

### The two gates (verify first)
- [ ] **No deception** anywhere in the design; the paper states this explicitly
- [ ] **Salient real incentives** for every elicited object; ECU→money conversion and realized average payment reported

### Manuscript & anonymization
- [ ] Manuscript anonymized for **double-blind** review (no author names, no identifying repository/IRB links in the blind copy; self-cites neutralized)
- [ ] Abstract states the treatment contrast and the numeric headline effect
- [ ] Design/Procedures section is reproducible from the text; names z-Tree/oTree
- [ ] Predictions are signed and treatment-indexed; primary vs. exploratory results labeled
- [ ] Effect sizes reported with CIs at the session/matching-group level (not stars only)

### Files for Editorial Manager
- [ ] Main manuscript (anonymized)
- [ ] **Participant instructions** for every treatment (required at submission)
- [ ] Data appendix / replication materials per ESA policy; experiment software (z-Tree `.ztt` / oTree app) ready
- [ ] Pre-registration / PAP link (or Stage-1 Registered Report protocol) and timestamp
- [ ] Cover letter framing the **methods contribution** and (if relevant) replication/RR status

### Declarations
- [ ] IRB/ethics approval and consent procedure stated; explicit no-deception statement
- [ ] Funding and competing-interest disclosures; confirmation paper is not under review elsewhere
- [ ] Open-access/CC-BY and any APC/waiver terms checked on the current Cambridge page (待核实)

## Right journal, right ESA outlet

Before you submit, confirm the paper is a **full design paper**, not a short-format piece. The ESA runs **two** journals: *Experimental Economics* (the method flagship, full papers) and the **Journal of the Economic Science Association (JESA)** — its shorter-format outlet for replications, null results, software notes, comments, and minor extensions. A brief replication or a z-Tree/oTree tool note is usually a JESA submission, not an Experimental Economics one. Submitting a short note to the flagship invites a transfer suggestion and lost time.

## Cover letter essentials

- One paragraph framing the **methods contribution** (the design/elicitation advance), not the topic.
- Explicit statement that the study used **no deception** and **real salient incentives**.
- Pre-registration / Registered Report status with the registry link and timestamp.
- If a replication: what is replicated, the added power, and why it belongs in the flagship rather than JESA.
- Suggested non-conflicted referees (optional but useful given double-blind review).

## Anti-patterns

- Uploading without the **participant instructions** — a structural incompleteness here
- Any deceptive procedure, or hypothetical/token "incentives" — a desk reject
- A non-anonymized manuscript breaking double-blind review
- Stars-only significance with no effect sizes/CIs at the group unit
- Treating the new CC-BY open-access model as a submission-time fee without checking current terms
- Sending a short replication/software note to the flagship instead of JESA

## The anonymization pass (double-blind, done last)

Because review is anonymous, the blind manuscript needs a dedicated scrub that authors routinely botch:

- Remove author names, affiliations, and acknowledgments from the blind copy.
- Neutralize self-citations ("Smith (2022) showed" → "prior work showed [ref]") so they do not reveal authorship.
- Strip identifying links — your lab's repository, an OSF page tied to your name, a university IRB number — from the blind copy; provide them separately for the editor.
- Scrub document metadata (PDF author field, file properties) and any "Track Changes" author tags.
- Keep the instructions and data-appendix references in a way that lets referees read them without de-anonymizing you.

A manuscript that names its authors through a repository link defeats the blind review the journal runs; do this pass last, after all content is final.

## Output format

```text
【Journal】Experimental Economics (ESA flagship; Cambridge UP, OA, 检索于 2026-06)
【Skill】expecon-submission
【Gates】no deception? salient incentives? both stated in paper? [Y/N]
【Anonymized】double-blind copy clean? [Y/N]
【Instructions】all treatments attached at submission? [Y/N]
【Package】data appendix + z-Tree/oTree + PAP/RR link ready? [Y/N]
【Declarations】IRB / disclosures / OA terms checked (待核实 where unverified)
【Next step】submit via Editorial Manager (editorialmanager.com/eec) → expecon-rebuttal after decision
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
