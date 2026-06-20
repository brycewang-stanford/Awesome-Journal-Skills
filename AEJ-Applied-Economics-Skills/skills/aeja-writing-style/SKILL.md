---
name: aeja-writing-style
description: Use when revising the prose, abstract, and introduction of an American Economic Journal: Applied Economics (AEJ: Applied) manuscript so the design and headline estimate land in the first paragraph in AEA house style. Polishes exposition; it does not change the result (aeja-identification / aeja-robustness) or the exhibits.
---

# Writing Style (aeja-writing-style)

## When to trigger

- Identification and robustness are settled and the paper needs its final exposition pass
- The introduction buries the question and the estimate under setup or literature
- The abstract does not state the headline number with its uncertainty
- The prose reads like a field-internal note rather than broad applied micro

## The AEJ: Applied introduction arc

AEJ: Applied prose is **plain, direct, and design-forward**. The introduction should follow the applied-micro arc: **question → why credible identification is hard → the design that solves it → headline causal estimate with a standard error → mechanism → policy/economic lesson → brief roadmap.** A non-specialist applied economist should grasp the question and the answer in the first paragraph; the design should be legible by the end of the second.

| Section | What it must do at AEJ: Applied |
|---------|--------------------------------|
| Abstract | question + design + headline estimate (with units & SE) + lesson, in ≤ the AEA word norm |
| Intro ¶1 | the economic question and the headline number, with uncertainty, no throat-clearing |
| Intro ¶2–3 | why naive estimates fail + the source of variation that fixes it |
| Intro mid | the estimate, the mechanism, and the magnitude's economic meaning |
| Intro end | contribution (honest delta), scope of the claim, brief roadmap |

## Writing craft

1. **Lead with the answer, not the setup.** The first paragraph states what you find and roughly how big; the apparatus comes after.
2. **Numbers with units and SEs in sentences.** "We find X raises Y by 6.2% (s.e. 0.7)" — the magnitude lives in the prose, not only the table.
3. **Name the design plainly.** "We use a regression discontinuity at the eligibility cutoff" beats euphemism; AEJ: Applied readers want the identification stated.
4. **Calibrate the claim.** State what the estimand is (local / ITT) and what it does *not* establish — over-claiming external validity is a frequent referee complaint.
5. **Plain English over jargon.** Short sentences; active voice; define field-specific terms once. Broad applied-micro readership is the audience.
6. **Write the abstract and intro last**, after the result is final.

## Checklist

- [ ] Abstract states question + design + headline estimate (units & SE) + lesson, within the AEA word norm
- [ ] Intro ¶1 gives the economic question and the headline number with uncertainty — no throat-clearing
- [ ] The naive-estimate problem and the identifying variation appear by ¶2–3
- [ ] Magnitudes written into sentences with units and standard errors
- [ ] Estimand and scope stated; external-validity claim calibrated, not inflated
- [ ] Plain English, active voice, jargon defined once; abstract/intro written last

## Anti-patterns

- An introduction that spends a page on institutional background before stating the question
- A "literature tour" intro with no contribution sentence up front (see `aeja-literature-positioning`)
- Reporting "statistically significant" without the magnitude, units, or SE in the prose
- Over-claiming the local/ITT estimate as a general population effect
- Jargon-dense, passive-voice writing aimed only at sub-field specialists
- Polishing the intro before identification and robustness are settled

## Worked vignette (illustrative)

A first-draft intro opens with a page of institutional background on a transit program, then a TWFE
specification, then "the effect is statistically significant." The AEJ: Applied rewrite leads with the
answer: "Does cheap transportation help teenagers find work? Using a staggered municipal rollout of free
bus passes, we find the program raised teen employment by 3.1 percentage points (s.e. 0.9)." The design is
named in the next sentence, the mechanism and the calibrated scope follow, and the institutional detail
moves to Section 2. The full before→after is in
[`../../resources/worked-examples/01-introduction.md`](../../resources/worked-examples/01-introduction.md).

## Referee pushback mapped to the writing fix

- *"I read three pages before learning what you find."* → Move the headline number and design to ¶1; demote
  background to the data section.
- *"You report significance but not the magnitude."* → Put the point estimate, its units, and its SE in the
  sentence, not only the table.
- *"You overclaim external validity."* → State the estimand (local/ITT) and what it does not establish.

## Output format

```
【Abstract】question + design + estimate(units,SE) + lesson within word norm? [Y/N]
【Intro ¶1】headline number + uncertainty up front? [Y/N]
【Identification legible by ¶3】[Y/N]
【Magnitudes in prose】units + SEs in sentences? [Y/N]
【Claim calibrated】estimand + scope stated, no overclaim? [Y/N]
【Next step】aeja-replication-package
```
