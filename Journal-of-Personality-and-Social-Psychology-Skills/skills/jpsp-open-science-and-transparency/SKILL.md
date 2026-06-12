---
name: jpsp-open-science-and-transparency
description: Use when meeting the Journal of Personality and Social Psychology (JPSP) transparency requirements — TOP Guidelines at Level 2, JARS reporting, data/code/materials disclosure to a trusted repository, preregistration status, and Registered Reports. Guides compliance; it does not create data or post your files for you.
---

# Open Science & Transparency (jpsp-open-science-and-transparency)

JPSP implements APA's **Transparency and Openness Promotion (TOP) Guidelines at Level 2 (Requirement)**
(effective July 1, 2021) and requires **JARS** reporting. Transparency is not optional polish: you
must **state** the availability of data, code, and materials and whether the work was preregistered.
Note JPSP **does not offer open-science badges** — the requirement is the disclosure itself, not a
badge.

## When to trigger

- Preparing the transparency disclosures before submission
- Posting data/code/materials to a trusted repository
- Deciding what to preregister or whether to pursue a Registered Report
- Writing the data-availability / preregistration statements

## What JPSP requires (verify on the live page — 待核实 on exact wording)

1. **TOP Level 2 (Requirement).** For data, code, and materials: **state whether** they are posted to
   a **trusted repository**, and post them (with a persistent identifier) unless a justified exemption
   applies (e.g., ethical, legal, privacy constraints — then explain why and how to obtain the data).
2. **JARS reporting.** Follow the matching APA Journal Article Reporting Standards table (JARS-Quant,
   JARS-Qual, or JARS-Mixed) for your design; report participant flow, exclusions, all manipulations
   and measures, and effect sizes with intervals.
3. **Preregistration disclosure.** **State whether or not** any analyses were preregistered; mark
   registered vs. exploratory analyses; share the (masked) preregistration link.
4. **Registered Reports.** JPSP publishes Registered Reports — if your design is prospective, consider
   the Stage-1 protocol route (reviewed before data collection); see `jpsp-review-process`.
5. **Data availability.** APA expects data to remain available **throughout review** and for **at
   least 5 years after publication**.
6. **Badges: not offered.** Do not claim or design for open-science badges at JPSP.

## Transparency checklist

- [ ] Data, code, and materials in a trusted repository (OSF/ResearchBox/Dataverse/ICPSR) with a DOI
- [ ] Data/code/materials availability **stated** in the manuscript (TOP Level 2)
- [ ] Preregistration status stated; registered vs. exploratory clearly marked
- [ ] JARS table for the design completed; reporting matches it
- [ ] Any non-sharing justified, with README on how to obtain restricted data
- [ ] Repository links **masked** for review (no author-identifying URLs)
- [ ] Plan to keep data available ≥ 5 years post-publication

## Anti-patterns

- Saying "data available on request" instead of posting to a trusted repository at Level 2
- Designing for a badge JPSP does not offer
- Vague preregistration claims with no link or no registered/exploratory split
- Disclosing materials but not the analysis code
- A repository link that de-anonymizes the masked submission

## Desk-screen triggers a section editor flags first

Post-credibility-revolution, an APA section editor can screen a JPSP manuscript before review on transparency grounds alone. These are the avoidable triggers — confirm exact requirements against the journal's submission guidelines (待核实).

| Trigger | Why it stalls at the editor's desk | The fix before submission |
|---------|------------------------------------|---------------------------|
| "Data available on request" | Falls short of TOP **Level 2** posting | Deposit in a trusted repository with a persistent DOI, and state it |
| Materials posted, code missing | Reviewers cannot reproduce the analysis | Post the analysis code, not just stimuli/measures |
| Vague "we preregistered" | No registered-vs-exploratory split, no link | Give the (masked) prereg link and label every confirmatory test |
| OSF link shows author names | Breaks **masked review** | Use an anonymized view-only OSF link |
| Claiming a badge | JPSP **does not offer** open-science badges | Drop badge language; the disclosure is the requirement |
| No JARS table | Missing standardized reporting | Complete JARS for the design |

## Worked example: a transparency block for a three-study package

*Illustrative — wording to adapt, not a quotation of any real manuscript.*

A preregistered three-study PPID package would carry a disclosure paragraph like: *"Data, analysis code, and materials for all three studies are available at [anonymized OSF DOI]. Studies 1 and 2 were preregistered (links in the repository); Study 3 was exploratory and labeled as such. Reporting follows JARS-Quant. We will maintain availability for at least five years after publication."* Note the four parts a reviewer checks: repository + DOI, the confirmatory/exploratory split, the JARS commitment, and the masking-safe link. A missing part is the most common avoidable transparency flag at JPSP. The five-year availability figure is an APA-wide norm — confirm the precise duration against the journal's current submission guidelines.

## Output format

```
【Repository】where data/code/materials are posted + DOI
【TOP Level 2 disclosure】availability stated in manuscript? [Y/N]
【Preregistration】status stated + registered vs exploratory marked? [Y/N]
【JARS】correct table completed? [Y/N]
【Registered Report?】considered if prospective? [Y/N]
【Masked】repository links de-identified for review? [Y/N]
【Next】jpsp-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — OSF/ResearchBox/Dataverse, JARS, preregistration tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — TOP Level 2, JARS, data-availability and badges policy
