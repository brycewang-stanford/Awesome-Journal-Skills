---
name: jama-ethics-registration
description: Use when verifying trial registration, IRB/ethics approval, informed consent, ICMJE authorship and conflict-of-interest disclosures, and the data-sharing statement for a JAMA manuscript. Confirms compliance; it does NOT design the study or write the abstract.
---

# Ethics, Registration & Disclosures (jama-ethics-registration)

## When to trigger

- A clinical trial's registration status or timing is uncertain
- IRB/ethics approval or informed-consent statements are missing from Methods
- Author roles, contributorship, or COI disclosures are incomplete
- A data-sharing statement is required and not yet drafted

## Prospective trial registration (ICMJE policy)

- Clinical trials must be **prospectively registered — before the first participant is enrolled** — in ClinicalTrials.gov or another ICMJE-accepted registry (e.g., a WHO ICTRP primary registry).
- A trial registered **after enrollment began** is retrospectively registered; ICMJE journals including JAMA treat this as non-compliant, and it generally cannot be remedied at submission. Disclose it transparently if it happened — do not hide it.
- Report the registry name and trial identifier in the abstract (Trial Registration line), the Methods, and any required submission field.
- Systematic reviews/meta-analyses should register the protocol (e.g., PROSPERO) and cite it.

## Ethics and consent statements (in Methods)

- Name the **IRB / research ethics committee** that approved the study (or state the basis for exemption).
- State that the study followed the **Declaration of Helsinki** (and Good Clinical Practice for trials, as applicable).
- State how **informed consent** was obtained, or justify any waiver.
- For studies with identifiable individuals (including images/case details), obtain and state **consent for publication**.

## ICMJE authorship, contributorship, and disclosures

- Each author should meet the **ICMJE four authorship criteria**; non-qualifying helpers go in Acknowledgments.
- Provide a **contributorship** statement (who did what).
- Every author files an **ICMJE Disclosure of Potential Conflicts of Interest** form; summarize relevant financial and non-financial conflicts in the manuscript.
- Disclose **funding sources** and the **role of the funder/sponsor** (design, conduct, analysis, decision to publish).
- For trials, address **access to data / statistical responsibility** (which authors had full data access and vouch for the analysis).

## Data sharing

- Provide a **data-sharing statement** (per ICMJE) for clinical trials and, increasingly, other study types: whether de-identified individual-participant data will be shared, what documents (protocol, statistical analysis plan), when, with whom, and by what mechanism.

## Compliance gates JAMA enforces before review

At the Journal of the American Medical Association, an ICMJE member journal, several integrity items are hard gates: a manuscript that fails them is stopped regardless of merit. Treat each as pass/fail — registration before first enrollment (ID in abstract and Methods); a named IRB / ethics committee and the Declaration of Helsinki; consent described or its waiver IRB-justified; the four ICMJE authorship criteria with per-author COI disclosure; and the funder's role plus a concrete ICMJE-style data-sharing plan.

## Worked example: registration timing (illustrative)

Vignette (illustrative): a multicenter randomized clinical trial, N = 2,600 adults with resistant hypertension, primary outcome 24-week change in ambulatory systolic blood pressure, mean difference -6.4 mm Hg (95% CI, -8.9 to -3.9). First participant enrolled March 3; registered April 18 — retrospective by ICMJE definition, ~6 weeks late.

Consequence and fix: generally not remediable; disclose the timing transparently, do not backdate. The effect estimate does not cure a registration-timing defect.

## Reviewer pushback and the JAMA fix

- "Trial not registered before enrollment." Fix: state the dates plainly; if retrospective, disclose and accept the venue may decline — never hide it.
- "IRB approval obtained" with no committee named. Fix: name the specific IRB and the Helsinki / GCP basis.
- "Data available upon request." Fix: replace with a concrete plan — what data, which documents, when, by what mechanism.

Calibration anchors (hedge where uncertain): prospective-before-enrollment registration, the four ICMJE authorship criteria, the Declaration of Helsinki, and per-author COI forms are durable; the accepted-registry list and data-sharing wording evolve — confirm against current author guidelines.

## Checklist

- [ ] Trial prospectively registered before enrollment; registry + ID reported
- [ ] Systematic-review protocol registered (e.g., PROSPERO) and cited
- [ ] IRB/ethics approval (or exemption) named in Methods
- [ ] Declaration of Helsinki (and GCP for trials) stated
- [ ] Informed-consent process described or waiver justified
- [ ] Consent for publication for identifiable individuals
- [ ] All authors meet ICMJE criteria; contributorship statement present
- [ ] COI disclosure forms collected; conflicts summarized
- [ ] Funding source and funder role stated
- [ ] Data-sharing statement drafted

## Anti-patterns

- Unregistered trial, or registration after enrollment began
- "IRB approval obtained" with no committee named
- Honorary/guest authorship; ghostwriting
- Undisclosed industry funding or author conflicts
- Funder controlled analysis or publication decision, undisclosed
- "Data available upon request" used as a non-committal placeholder

## Output format

```
【Trial registration】prospective + ID: ... / retrospective (disclose) / n.a.
【Protocol registration (review)】PROSPERO ID / n.a.
【IRB + Helsinki + consent stated】yes / fixes: ...
【ICMJE authorship + contributorship】complete / issues: ...
【COI + funding + funder role disclosed】yes / gaps: ...
【Data-sharing statement】drafted / missing
【Next skill】jama-writing-style
```
