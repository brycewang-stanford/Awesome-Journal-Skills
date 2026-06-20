---
name: jle-writing-style
description: Use when revising the prose, abstract, and introduction of a The Journal of Law and Economics (JLE) manuscript so the legal institution and the design land early, in University of Chicago Press house style with Chicago author-date citations. Polishes exposition; it does not change the result (jle-identification / jle-robustness) or the exhibits.
---

# Writing Style (jle-writing-style)

## When to trigger

- Identification and robustness are settled and the paper needs its final exposition pass
- The introduction buries the legal question and the effect under institutional or doctrinal setup
- The abstract does not state the headline effect of the rule with its uncertainty
- The prose reads either like a generic economics paper that forgot the law, or like a law-review article that forgot the economics

## The JLE introduction arc

JLE prose is **plain, direct, and institution-aware**. The introduction should follow the law-and-economics arc: **the legal/regulatory question → why the institution makes the answer matter → why naive estimates fail → the legal source of variation that solves it → the headline effect of the rule with a standard error → the mechanism (deterrence/price/quality) → the legal or policy lesson → brief roadmap.** A reader who is an economist but not a lawyer should grasp the rule and the answer in the first paragraph; the identification should be legible by the end of the second. Get the law right without writing like a law review: explain the rule's mechanics in economists' terms.

| Section | What it must do at JLE |
|---------|------------------------|
| Abstract | the legal question + the design + the headline effect (units & SE) + the lesson |
| Intro ¶1 | the legal/regulatory question and the headline number, with uncertainty, no throat-clearing |
| Intro ¶2–3 | why the institution matters + why naive estimates fail + the legal variation that fixes it |
| Intro mid | the effect, the mechanism, and the magnitude's economic meaning |
| Intro end | contribution (honest delta vs. the law-and-econ canon), scope of the claim, brief roadmap |

## Writing craft

1. **Lead with the answer about the rule, not the institutional history.** The first paragraph states what the legal rule does and roughly how big; the doctrinal background comes later.
2. **Numbers with units and SEs in sentences.** "The damages cap cut malpractice claims by 8% (s.e. 3)" — the magnitude lives in the prose, not only the table.
3. **Name the legal variation plainly.** "We use the staggered adoption of state damages caps" beats euphemism; JLE readers want the identification stated.
4. **Explain the institution in economists' terms.** State who is bound, when the rule binds, and the counterfactual rule — but in one efficient paragraph, not a treatise.
5. **Calibrate the claim.** State the estimand (ATT / LATE / local-at-threshold) and what it does *not* establish; over-claiming a local legal effect as universal is a frequent referee complaint.
6. **Chicago author-date citations**, plain English, active voice; write the abstract and intro last.

## Checklist

- [ ] Abstract states the legal question + design + headline effect (units & SE) + lesson
- [ ] Intro ¶1 gives the legal/regulatory question and the headline number with uncertainty — no throat-clearing
- [ ] The institution and the identifying legal variation appear by ¶2–3, in economists' terms
- [ ] Magnitudes written into sentences with units and standard errors
- [ ] Estimand and scope stated; external-validity / cross-jurisdiction claim calibrated, not inflated
- [ ] Chicago author-date style; plain English, active voice; abstract/intro written last

## Anti-patterns

- An introduction that spends a page on legal/doctrinal history before stating the economic question
- Writing like a law-review article (string citations, doctrinal exegesis) instead of economic analysis
- Writing like a generic economics paper that never explains how the rule actually works
- Reporting "statistically significant" without the magnitude, units, or SE in the prose
- Over-claiming a local/LATE legal effect as a general population effect across all jurisdictions
- Polishing the intro before identification and robustness are settled

## Worked vignette (illustrative)

A first-draft intro opens with two pages on the history of medical-malpractice doctrine, then a TWFE specification, then "the effect is statistically significant." The JLE rewrite leads with the answer: "Do caps on malpractice damages reduce litigation? Exploiting the staggered adoption of state damages caps, we find caps cut malpractice claims by 8% (s.e. 3), driven by the marginal low-value suit rather than catastrophic-injury cases." The legal variation is named in the next sentence, the deterrence-of-marginal-suits mechanism and the calibrated scope follow, and the doctrinal history moves to Section 2. An economist who is not a lawyer now grasps the rule and the result in the first paragraph.

## Writing for JLE's dual audience

JLE is read by economists and by economically literate legal scholars. Two habits keep both on board:

1. **Define the legal term once, in economists' language.** "A damages cap (a statutory ceiling on the jury award a plaintiff can recover) lowers the expected payoff to filing." One clause does the work; do not assume the reader knows the doctrine, and do not lecture.
2. **Keep the law in service of the economics.** Cite statutes and cases where they pin down the institution (the effective date, who is bound), not to display doctrinal command. The legal apparatus appears because the identification needs it.

Because review is **single-blind**, your name is on the paper — so the prose can use "we show / we exploit" naturally, and your prior work can be cited honestly without anonymization contortions. This is a small but real difference from blinded econ journals where self-reference must be masked.

## Referee pushback mapped to the writing fix

- *"I read three pages of legal history before learning what you find."* → Move the headline effect and the legal variation to ¶1; demote doctrinal background to the institutions section.
- *"This reads like a law-review article."* → Replace doctrinal exegesis with economic mechanism; keep the institution to what the identification needs.
- *"You overclaim the effect across all jurisdictions."* → State the estimand (ATT / local effect) and what it does not establish.
- *"A non-lawyer can't follow your legal terms."* → Define each legal term once, in economists' language, at first use.

## The institutions section: where the law lives

In a JLE empirical paper the introduction states the answer, but a dedicated **institutions section** (usually Section 2) carries the legal detail. Write it as the bridge between law and identification, not as background:

- State the rule's mechanics economically — the constraint it imposes, the agents it binds, the effective date, the exemptions — because every one of these is an identification assumption in disguise.
- Make the **counterfactual legal regime** explicit: what would have happened under the prior rule, since that is what the design compares against.
- End the section by handing the reader the **source of variation** the empirics will exploit, so the move into the design feels inevitable.

A crisp institutions section pre-empts the law-and-economics referee's first reflex — "do they actually understand this rule?"

## Output format

```
【Abstract】legal question + design + effect(units,SE) + lesson? [Y/N]
【Intro ¶1】headline number + uncertainty up front? [Y/N]
【Institution + identification legible by ¶3】[Y/N]
【Magnitudes in prose】units + SEs in sentences? [Y/N]
【Claim calibrated】estimand + scope stated, no overclaim? [Y/N]
【Style】Chicago author-date, plain English, active voice? [Y/N]
【Next step】jle-replication-package
```
