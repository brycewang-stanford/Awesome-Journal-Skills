---
name: lancet-study-design
description: Use to lock study design and mandatory prospective registration for a Lancet clinical manuscript — trial registration before enrollment, protocol + statistical analysis plan, and design rigor (randomization, allocation concealment, blinding, pre-specified endpoints, power, ITT). Covers observational design choices too.
---

# Study Design & Registration (lancet-study-design)

## When to trigger

- Planning or writing up a clinical trial or a major observational study.
- The trial registration number is missing, or registration timing is unclear.
- There is no protocol or no pre-specified statistical analysis plan (SAP).
- A reviewer is likely to ask "was the primary endpoint pre-specified?" and there is no clear answer.

## Mandatory: prospective trial registration

The Lancet follows ICMJE: **clinical trials must be registered prospectively — before the first participant is enrolled — in a WHO-ICTRP primary registry or ClinicalTrials.gov.**

- [ ] Registered **before** enrollment of the first participant (retrospective registration is a serious, often fatal, problem — flag it immediately and disclose honestly).
- [ ] Registration number reported **in the abstract** and Methods (e.g., ClinicalTrials.gov NCTxxxxxxxx; ISRCTN; or a WHO-ICTRP primary registry).
- [ ] Registered outcomes match the reported primary/secondary outcomes; explain and flag any change.

| Registry | Use / region |
|----------|--------------|
| [ClinicalTrials.gov](https://clinicaltrials.gov/) | US and international |
| [ISRCTN](https://www.isrctn.com/) | UK / international |
| [WHO ICTRP](https://trialsearch.who.int/) | global portal aggregating primary registries (e.g., EU-CTR, ANZCTR, CTRI, ChiCTR, PACTR) |

> The Lancet often handles large **international / multi-country** trials — confirm registration in each relevant jurisdiction and report the lead registry.

## Protocol + statistical analysis plan (SAP)

- [ ] A **protocol** exists and (typically) is submitted with the manuscript; published-protocol citation if available.
- [ ] A **pre-specified SAP** defines the primary analysis, populations (ITT / per-protocol), handling of missing data, and pre-specified subgroups **before unblinding**.
- [ ] Any deviation from protocol/SAP is reported transparently with dates and rationale.

## Trial design rigor (RCT)

- [ ] **Randomization** method (sequence generation) described.
- [ ] **Allocation concealment** mechanism described (separate from blinding).
- [ ] **Blinding** of participants, clinicians, outcome assessors, and analysts — or justification if open-label.
- [ ] **Pre-specified primary endpoint**, clinically meaningful, with a clear hierarchy of secondary endpoints.
- [ ] **Sample size / power** justified for the clinically meaningful effect, with assumptions stated.
- [ ] **Intention-to-treat (ITT)** as the primary analysis population.
- [ ] Trial design named (parallel, cluster, crossover, factorial, adaptive, non-inferiority/equivalence — state the margin).
- [ ] Independent **data and safety monitoring committee (DSMC)** and any interim/stopping rules described.

## Observational design choices

- [ ] Design named (cohort, case-control, cross-sectional) and justified.
- [ ] Exposure/outcome definitions, eligibility, and follow-up specified a priori.
- [ ] Confounding strategy (matching, adjustment, propensity methods) pre-specified; causal language calibrated to the design.
- [ ] Registration/protocol encouraged for major observational studies (e.g., a pre-registered analysis plan).

## What Lancet editors check on design and registration

Registration timing is the most consequential design fact The Lancet checks: following ICMJE, it will decline to consider a trial not registered prospectively, and an outcome switched from the registered one is an integrity concern. Desk-reject or major-revision triggers: retrospective registration left undisclosed; a switched primary outcome; no protocol or pre-specified SAP; concealment conflated with blinding; per-protocol presented as primary for a superiority trial. Confirm any current protocol-submission requirement against the journal's author guidelines.

## Worked micro-example (illustrative numbers — not real data)

A hypothetical double-blind, multi-country superiority RCT.

```
Design lock (illustrative):
  Registry ISRCTN registered 2021-03 BEFORE first enrolment 2021-06 -> prospective, PASS
  Registered primary outcome = reported primary outcome -> no switch, PASS
  Randomisation 1:1 stratified by country; central web concealment; double-blind
  Power: ARR 6 pp, alpha 0.05, power 90% -> n=2 040 (1 020/arm), +8% attrition
  Primary population ITT; per-protocol pre-specified sensitivity; independent DSMC
```

The design passes: registration is prospective and dated, outcomes agree, concealment and blinding are separate, and the sample size is justified.

## Reviewer-pushback patterns and the venue-specific fix

- *"The trial was not registered prospectively."* → Disclose exact registration and enrolment dates; if retrospective, flag it transparently — the editor may decline.
- *"The primary outcome was switched."* → Reconcile to the registered outcome or document the change with dates and rationale.
- *"The study is underpowered / concealment is unclear."* → Justify the sample size against the minimally important difference; describe sequence generation and concealment separately from blinding.

## Output format

```
【Study type】 RCT (parallel/cluster/crossover/factorial/adaptive/NI) / observational (cohort/case-control/cross-sectional)
【Registration】 registry + number + prospective? (before first enrollment: yes/no) + in abstract? yes/no
【Protocol + SAP】 present? primary analysis & populations pre-specified? yes/no
【RCT rigor】 randomization / allocation concealment / blinding / primary endpoint / power / ITT  → gaps
【Observational rigor】 design / confounding strategy / causal language calibrated  → gaps
【Deviations from protocol/SAP】 [...] reported transparently? yes/no
【Next】 lancet-reporting
```

## Anti-patterns

- **Do not** submit a trial that was registered **after** enrollment without flagging it — The Lancet/ICMJE may decline to consider it.
- **Do not** report a primary outcome that differs from the registered one without an explicit, dated explanation.
- **Do not** present a post-hoc analysis as if it were pre-specified.
- **Do not** rely on per-protocol as the primary analysis for a superiority trial — ITT leads.
