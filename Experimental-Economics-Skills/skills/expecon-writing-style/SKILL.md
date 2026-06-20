---
name: expecon-writing-style
description: Use when the prose of an Experimental Economics (ExpEcon) manuscript buries the design or the result, or when the intro/abstract do not land for an experimentalist reader. Polishes structure and voice; it does not change the analysis.
---

# Writing Style (expecon-writing-style)

## When to trigger

- The abstract names a topic but never states the treatment contrast or the headline effect
- A reader reaches the results before understanding *what subjects actually did*
- The design is described as scattered implementation notes instead of a clean procedure section
- The intro reads like a JEBO behavioral essay or a GEB theory paper rather than an experimental-methods paper

## Structure: the design is the narrative

ExpEcon papers have a near-canonical, **design-forward** shape. Honor it; referees read for it.

1. **Abstract (the contract).** Within a few sentences: the question, the **treatment contrast**, the **incentivized design** in one clause, the **headline effect with a number and direction**, and the takeaway. "We run a lab experiment in which [contrast]; [outcome] is X% higher under [T] (p=…); this adjudicates between [model A] and [model B]."
2. **Introduction.** Motivate, state the precise hypothesis, then say *how the design isolates it* and what is new about that design. The reader should know your treatments before the literature review ends.
3. **Design / Procedures (the load-bearing section).** This is what an experimentalist reads most carefully. Write it so the study is **reproducible from the text alone**: game and payoffs (ECU + conversion), treatments and what each manipulates, matching, information, rounds, incentive mechanism, subject pool and recruitment, software (z-Tree/oTree), sessions and n, comprehension checks. State explicitly that **no deception was used**.
4. **Predictions.** The signed, treatment-indexed hypotheses from `expecon-theory-model`.
5. **Results.** Raw behavior → primary test (correct unit) → secondary/exploratory (labeled) → robustness.
6. **Discussion.** Mechanism, external validity, boundary conditions, and what the design cannot speak to.

## Voice an ExpEcon referee trusts

- **Procedural transparency over rhetoric.** The register is sober and precise. Claims are pinned to the design ("because matching was anonymous and one-shot, reputation cannot drive this"), not to adjectives.
- **Subjects' perspective.** Describe what participants saw and decided, in their units; do not narrate only the analyst's regression.
- **Say "no deception" out loud.** Experimentalist readers look for the explicit statement that participants were not deceived and were paid real, salient incentives. Make it unmissable.
- **Calibrate the claim to control.** Internal validity is your strength; do not overclaim external validity. A line acknowledging the population (often a student pool) and what generalization is and is not warranted reads as competence, not weakness.
- **Hedge honestly on nulls.** If the result is a precise null, frame it with the power to detect a meaningful effect; that is a strength here, not an apology.

## Sentence-level habits

- **Name treatments, do not number them only.** "the Punishment treatment" reads far better than "T3"; if you must abbreviate, define mnemonic labels (NoPun / Pun) and use them consistently.
- **Quantify in the subjects' units.** "contributions rose by 3.2 tokens (16% of the 20-token endowment)" beats "contributions rose significantly."
- **Attribute causality to the design, not the data.** "Because matching was anonymous and one-shot, reputation cannot explain X" is the ExpEcon move; "X is correlated with Y" is not.
- **Front-load the procedure of each elicitation** before its result, so the reader knows what was incentivized.
- **Use the past tense for what subjects did and the present for what the data show** — a small convention experimentalist readers expect.

## Checklist

- [ ] Abstract states contrast + incentivized design + numeric headline effect + takeaway
- [ ] Treatments are introduced before the literature review closes
- [ ] Design/Procedures section is reproducible from the text alone and names z-Tree/oTree
- [ ] "No deception" and "salient real incentives" stated explicitly
- [ ] Predictions are signed and treatment-indexed; results lead with raw behavior
- [ ] Primary (pre-registered) vs. exploratory results are verbally distinguished
- [ ] External-validity claims are calibrated to the subject pool and control
- [ ] Treatments have mnemonic names; effects quantified in subjects' units

## The Procedures section, line by line

Because this is the section referees scrutinize, give it a fixed internal order so nothing is missing:

1. **Subjects** — pool, recruitment system (ORSEE/hroot), n, sessions, dates if relevant.
2. **The game** — actions, information, ECU payoffs and the money conversion, matching, horizon.
3. **Treatments** — each condition and the *single* dimension it manipulates, with mnemonic names.
4. **Incentives** — the payment mechanism per elicited object and the realized average payment.
5. **Procedure flow** — instructions, comprehension quiz, practice rounds, paid rounds, debrief.
6. **Software & environment** — z-Tree/oTree, lab vs. online, any device constraints.
7. **Ethics** — IRB reference, consent, and the explicit **no-deception** statement.

A reader who finishes this section should be able to reconstruct a session without emailing you. If they cannot, the paper is not yet submittable to this journal.

## Anti-patterns

- An abstract with a topic and a vibe but no contrast and no number
- Procedures so thin the experiment cannot be reproduced — fatal at this journal
- Burying the treatment manipulation in a footnote or appendix
- Overclaiming real-world generality from a student-lab sample
- Prose that reads as a behavioral essay (JEBO) or a theory paper with a demo (GEB)
- Never stating, in the body, that no deception was used

## Writing the abstract as a contract

The abstract is read by editors deciding whether to desk-screen and by referees deciding their prior. Treat it as a four-clause contract: (1) the question and why it matters; (2) the **incentivized experimental design** and the treatment contrast in one clause; (3) the **headline effect with a number, direction, and the comparison it comes from**; (4) the interpretation — which behavioral account it supports and the scope. Avoid abstracts that spend three sentences motivating and one vague sentence on "we find evidence that…". An experimentalist editor wants to know, by sentence two, *what you manipulated and what moved* — give it to them.

## Output format

```text
【Journal】Experimental Economics (ESA method flagship)
【Skill】expecon-writing-style
【Verdict】lands / restructure
【Abstract】contrast + design + numeric effect + takeaway present? [Y/N]
【Design section】reproducible from text? names software? no-deception stated? [Y/N]
【Results order】raw behavior → primary → exploratory(labeled) → robustness
【Claim calibration】external-validity scoped to pool/control
【Next skill】expecon-replication-package
```
