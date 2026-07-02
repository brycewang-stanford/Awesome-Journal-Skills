---
name: nejm-ethics
description: Use to confirm clinical ethics and research-integrity requirements for an NEJM submission — IRB/ethics-committee approval and informed consent per the Declaration of Helsinki, ICMJE conflict-of-interest disclosures and authorship criteria, the role-of-the-funding-source statement, and the ICMJE data-sharing statement.
---

# Clinical Ethics & Integrity (nejm-ethics)

## When to trigger

- The Methods do not state IRB/ethics approval or how informed consent was obtained.
- ICMJE disclosure forms are not collected for every author.
- There is no data-sharing statement (required by ICMJE for clinical trials).
- Authorship, contributions, or the role of the funder are unstated or unclear.

## Human-subjects ethics

- [ ] **IRB / ethics committee approval** — named committee(s) and that approval was obtained before enrollment.
- [ ] **Informed consent** — obtained from participants (or legal surrogates); describe any waiver and its basis.
- [ ] **Declaration of Helsinki** — state the trial was conducted in accordance with it (and GCP for trials).
- [ ] **Special populations** — additional protections for children, incapacitated adults, emergency-consent settings.

## ICMJE conflict-of-interest disclosures

- Every author completes the **ICMJE disclosure form**; financial and non-financial conflicts are reported.
- The manuscript carries a **disclosure / competing-interests statement**; "ICMJE disclosure forms are available with the full text" is the typical NEJM phrasing.
- Disclose relationships even if the author judges them irrelevant — the editor decides relevance.

## Authorship and contributions (ICMJE criteria)

ICMJE authorship requires **all four**: (1) substantial contribution to design or data; (2) drafting or critical revision; (3) final approval; (4) **accountability** for the work. Everyone meeting them is listed; everyone listed meets them.

- Contributors who do not meet all four go in **Acknowledgments** (with permission).
- Disclose **medical writers** and their funding source.
- State the **corresponding author's** attestation of data integrity and analysis.

## Role of the funding source

- A **role-of-the-funding-source statement** is required: did the funder design the study, collect/analyze/interpret data, write the manuscript, or decide to submit?
- For industry-sponsored trials, state who had access to the data and who vouches for completeness and fidelity to the protocol.

## Data-sharing statement (ICMJE)

ICMJE requires a **data-sharing statement for clinical trials**. Specify:

- **What** individual-participant data (and supporting documents: protocol, SAP, analytic code) will be shared.
- **When** (e.g., after publication, with an end date or "indefinitely").
- **To whom and for what** (e.g., researchers with a methodologically sound proposal).
- **By what mechanism** (repository, request to a committee) and under what conditions (data-use agreement).
- "No data will be shared" is a permissible statement but must be explicit and justified.

## Patient privacy and other integrity items

- **De-identify** all data and images; remove PHI; obtain consent for any potentially identifying material (e.g., clinical photographs).
- **Trial protocol publication** — NEJM publishes the protocol and SAP with trials; ensure they are submission-ready (see `nejm-study-design`).
- Report **plagiarism/originality** status: the work is original and not under consideration elsewhere.
- Note any **preprint** posting and prior presentation.

## Statement placement map (draft each as a named block)

Draft each statement as a block with a fixed home, then verify all blocks survived formatting:

- **Methods — study conduct:** named IRB/ethics committee(s), consent method (or waiver basis), Helsinki + GCP conformance.
- **Methods — oversight (trials):** who designed the trial, analyzed the data, wrote the first draft, and who **vouches for data completeness and fidelity to the protocol**; the protocol and SAP accompany the article.
- **End matter:** disclosure statement ("ICMJE disclosure forms are available with the full text"), funding acknowledgment, data-sharing statement.

## Worked micro-example — data-sharing statement (before → after)

- Before (fails ICMJE): "Data are available from the corresponding author on reasonable request."
- After: "De-identified individual-participant data, with the protocol and statistical analysis plan, will be shared beginning 12 months after publication with researchers whose methodologically sound proposal is approved by the trial's data-access committee, under a signed data-use agreement."

The before answers none of the four ICMJE questions — what, when, to whom, by what mechanism.

## Output format

```
【IRB/ethics approval + consent】 stated? Helsinki/GCP cited? yes/no
【Placement】 conduct/oversight/end-matter blocks all present after formatting? yes/no
【ICMJE disclosures】 all authors' forms collected + statement drafted? yes/no
【Authorship】 all 4 ICMJE criteria met by each author? contributors acknowledged? yes/no
【Role of funding source】 statement present + data-access/vouching for trials? yes/no
【Data-sharing statement】 what/when/to-whom/how specified (ICMJE)? yes/no
【Privacy】 de-identified, PHI removed, consent for identifying material? yes/no
【Next】 nejm-abstract
```

## Anti-patterns

- **Do not** submit a trial without IRB approval and a consent description in the Methods.
- **Do not** omit the data-sharing statement — ICMJE requires it for clinical trials.
- **Do not** list honorary authors or omit qualifying contributors.
- **Do not** hide the funder's role, or who had full data access in a sponsored trial.
- **Do not** include identifiable patient information without explicit consent.
