---
name: nejm-study-design
description: Use to confirm study-design rigor and the mandatory prospective trial registration, protocol, and statistical analysis plan before writing up a clinical study for NEJM. Surfaces registration problems early — they cannot be fixed retroactively.
---

# Study Design & Registration (nejm-study-design)

## When to trigger

- A trial is being written up and you must confirm it was registered **before enrollment**.
- There is no finalized protocol or statistical analysis plan to submit.
- The design (randomization, blinding, endpoints) needs to be stated rigorously for the Methods.
- An observational study needs its design (cohort / case-control / cross-sectional) named and justified.

## The non-negotiable: prospective trial registration

Per **ICMJE** policy (which NEJM enforces), a clinical trial must be **prospectively registered** in a public registry — **ClinicalTrials.gov** or a **WHO ICTRP** primary registry — **before the first patient is enrolled**. This is a deal-breaker, not a formatting detail.

- The **trial registration number** (e.g., an NCT number) is reported in the abstract and Methods.
- Registration must predate enrollment; retrospective registration is generally disqualifying for an Original Article.
- The registered **primary outcome** must match the reported primary outcome — discrepancies are a top reviewer flag.

> If a trial was never prospectively registered, raise it now. It changes venue and framing and cannot be repaired by writing.

## Protocol and statistical analysis plan (SAP)

For trials, NEJM expects the **full trial protocol** and the **statistical analysis plan** to be submitted (typically as a supplement) and made available to reviewers.

- The **SAP must be pre-specified** — finalized (and dated) before unblinding / database lock.
- Any **deviation** from the registered protocol or SAP must be disclosed and explained in the manuscript.
- A **CONSORT-aligned** trial write-up depends on these documents existing (see `nejm-reporting`).

## Design rigor checklist (trials)

- [ ] **Randomization** — method (e.g., permuted blocks, stratification factors) stated.
- [ ] **Allocation concealment** — mechanism described (central randomization, sealed envelopes).
- [ ] **Blinding** — who was blinded (participants, clinicians, outcome assessors, analysts); if open-label, justify and address bias.
- [ ] **Primary endpoint** — single, pre-specified, patient-important, with a clear definition and time point.
- [ ] **Secondary endpoints** — pre-specified and ordered; multiplicity handled (see `nejm-statistics`).
- [ ] **Sample size / power** — assumptions, effect size, alpha, power stated; not post hoc.
- [ ] **Analysis population** — **intention-to-treat** as primary; per-protocol as sensitivity.
- [ ] **Interim analyses / stopping rules** — DSMB, pre-specified boundaries (e.g., O'Brien-Fleming) if used.

## Observational studies

- Name the design: **cohort** (prospective/retrospective), **case-control**, **cross-sectional**, or nested designs.
- Pre-specify the primary exposure and outcome; define confounders and the adjustment strategy a priori.
- Address selection bias, information bias, and confounding explicitly; use cautious, non-causal language.
- Report per **STROBE** (see `nejm-reporting`); registration of observational protocols is encouraged though not mandated.


## Operating pass for New England Journal of Medicine

Use this as a second-pass capability check. First lock the clinical question, population, endpoint, effect size, safety signal, and practice implication; then test whether the manuscript addresses clinical-medicine reviewers who expect practice-changing evidence, patient relevance, safety, and exact reporting discipline.

- **Primary move:** Return a claim-evidence-risk ledger; every recommendation must point to a manuscript location or missing artifact.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against JAMA for broad clinical medicine, Lancet for global-health/public-health reach, specialty journals for narrower disease domains; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Study type】 RCT / other interventional / cohort / case-control / cross-sectional / SR-MA
【Registration】 registry + number + registered BEFORE enrollment? yes/no/UNREGISTERED-FLAG
【Registered vs reported primary outcome】 match? yes/no
【Protocol + SAP】 available, pre-specified, dated? yes/no
【Design rigor gaps】 randomization / concealment / blinding / endpoints / power / ITT
【Protocol/SAP deviations to disclose】 [...]
【Next】 nejm-reporting
```

## Anti-patterns

- **Do not** write up an unregistered trial as an Original Article without flagging it to the user.
- **Do not** present a post-hoc analysis plan as if it were pre-specified.
- **Do not** report a primary outcome that differs from the registered one without disclosing the change.
- **Do not** treat per-protocol as the primary analysis for a superiority trial — ITT is primary.
