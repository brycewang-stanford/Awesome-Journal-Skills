---
name: wber-writing-style
description: Use when the prose for a The World Bank Economic Review (WBER) manuscript buries the development-policy contribution — abstract, introduction, and the bridge from estimate to policy lesson. Sharpens the writing for a mixed economist + policymaker audience; it does not run analysis or build exhibits.
---

# Writing Style (wber-writing-style)

## When to trigger

- The abstract states a topic, not a result, and never names the policy stake
- The introduction takes three pages to reach the question
- The paper reads either as a dry econometrics exercise or as an advocacy brief — not the WBER middle
- The bridge from "we estimate X" to "so development policy should consider Y" is missing
- A coauthor says the writing does not sound like a WBER paper

## The WBER voice

WBER writing serves a **dual audience**: economists who demand precision and policymakers/practitioners who demand relevance. The house voice is **rigorous but legible** — technically exact, jargon-controlled, and always closing the loop to a development-policy implication. Two failure modes bracket it: prose so technical that a finance-ministry reader gives up, and prose so policy-breathless that an economist distrusts it. Aim for the middle: state the credible result plainly, then say what it means for a development decision *without* overclaiming and *without* implying alignment with any World Bank position (editorial independence is explicit). Write the body first; write the abstract and introduction last, once the result is final.

## The introduction recipe (WBER variant)

A WBER introduction should, in order:

1. **The development problem and its policy stakes** — one paragraph: why this matters for poverty/growth/welfare in developing countries.
2. **The question, sharply** — the specific causal or measurement question.
3. **The setting and data** — country/region, the data spine (LSMS/DHS/admin/survey), the source of variation.
4. **The headline result in policy units** — the magnitude a practitioner would quote (a pp change, a dollar figure, a cost-effectiveness number), with its precision.
5. **Identification in one paragraph** — the design and the one assumption it rests on, stated honestly.
6. **The contribution and the boundary** — what is new vs. the frontier, and why this is a WBER (not JDE/World Development/Research Observer) paper.
7. **The policy takeaway** — what a development decision-maker should do differently, scoped to what the evidence supports.

## The abstract

- ~100–150 words (confirm the current limit on the OUP page; 待核实).
- Sentence 1: the development question and why it matters.
- Sentence 2–3: the setting, data, and identification in plain terms.
- Sentence 4: the headline result in policy units, with magnitude.
- Sentence 5: the policy implication, scoped honestly.
- No undefined acronyms; no "we study"; lead with what you find.

## Prose discipline

- **Magnitudes over significance.** "Enrollment rose 4 percentage points" beats "the effect is significant at 1%."
- **Define development jargon once.** Spell out program names, local institutions, and acronyms (PMT, CCT, LSMS) on first use — practitioners and economists from other fields read WBER.
- **Active, claim-first sentences.** Topic-sentence each paragraph with its point.
- **Reference style** is Chicago-style author-date as applied by OUP (verify current style on the author guidelines; 待核实). Keep citations engaging the best version of prior work, not a strawman.
- **Honest hedging.** Scope every policy claim to the estimand and external-validity argument; do not let the conclusion outrun the design.

## Checklist

- [ ] Abstract states a *result in policy units*, not a topic, and names the policy stake
- [ ] Introduction reaches the question within the first page and the headline result soon after
- [ ] Identification stated honestly in one paragraph in the intro
- [ ] The "why WBER, not a sibling" boundary is visible
- [ ] Effects reported as magnitudes (with precision), not asterisk significance
- [ ] Development jargon/acronyms defined on first use
- [ ] Policy takeaway scoped to what the design supports; no implied Bank-policy alignment
- [ ] Abstract and intro written last, after results are final

## Anti-patterns

- An abstract that describes the topic and method but never states the finding or its magnitude
- A meandering introduction that reaches the question on page three
- Pure-econometrics prose with no policy bridge (reads like the wrong journal)
- Advocacy prose that overclaims beyond the estimand
- Implying the paper endorses or follows a World Bank policy position
- Unexplained local acronyms and program names

## Worked vignette (illustrative)

An abstract opens: "This paper studies the effects of a conditional cash transfer using a regression discontinuity design in [country]." It states method, not result. The WBER rewrite: "Means-tested cash transfers are a central anti-poverty tool, but it is unclear whether eligibility cutoffs improve schooling at the margin. Using a sharp eligibility threshold in [country]'s national program and administrative enrollment records, we find the transfer raises secondary enrollment by 5 percentage points (s.e. 1.4) at a cost of about $90 per additional enrollee. The effect concentrates among girls, suggesting that relaxing the cutoff modestly would be a cost-effective way to close the gender gap." It now leads with stakes, gives a magnitude in policy units, and scopes the implication.

## Calibrating the technical register

The hardest WBER writing skill is pitching the technical level for a dual audience without dumbing down or losing rigor:

- **Method in the body, intuition in the intro.** State the estimator precisely where it is used; in the introduction, give the one-sentence intuition ("we compare eligible and just-ineligible households at the cutoff") a non-specialist can follow.
- **Carry the magnitude through.** Whatever the technical detail, the reader should never lose the policy number — repeat it (with its precision) in the abstract, intro, results, and conclusion.
- **Quarantine the jargon.** Push estimator derivations, identification proofs, and notation to a methods subsection or appendix; keep the narrative spine readable.
- **Conclude with the decision, not a recap.** End on what a development decision-maker should weigh, scoped to the evidence — not a paragraph that merely restates the findings.

## Output format

```text
【Abstract】states result in policy units + policy stake? [Y/N]
【Intro】question by page 1; headline result + honest identification soon after? [Y/N]
【Audience bridge】estimate → development-policy lesson present? [Y/N]
【Magnitudes】effects in policy units, not asterisks? [Y/N]
【Boundary】"why WBER not sibling" visible? [Y/N]
【Scope】policy claim within the estimand; no Bank-alignment implication? [Y/N]
【Next step】wber-replication-package
```
