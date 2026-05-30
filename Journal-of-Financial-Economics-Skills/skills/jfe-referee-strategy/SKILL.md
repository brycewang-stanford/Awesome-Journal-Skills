---
name: jfe-referee-strategy
description: Use when anticipating and pre-empting the objections a Journal of Financial Economics (JFE) referee will raise — endogeneity, fragility, multiple testing, alternative explanations. Builds a defense plan before or during review; it does not draft the post-R&R response letter (jfe-rebuttal).
---

# Referee Strategy (jfe-referee-strategy)

## When to trigger

- Before submission, to find the objections a referee will raise first
- After a first round, to plan which battles to fight and which to concede
- When you suspect a specific weakness (a contested instrument, a thin subsample)
- When the paper is strong but you have not "refereed it yourself"

## How JFE referees behave

JFE referees are methodologically demanding experts who expect every plausible alternative explanation to be ruled out and every result to survive thorough robustness. They read the Internet Appendix. They are quicker to reject for an undefended identification or a fragile result than for a modest contribution. The winning strategy is to referee your own paper first and answer the hard questions in the text. Verify current editorial structure on the official page.

## Pre-empt the predictable objections

### Identification objections
- "X is endogenous to Y." -> Have the shock/IV/RDD defense and a placebo in the text.
- "Staggered DID is biased." -> Show a heterogeneity-robust estimator and Bacon decomposition.
- "Your instrument violates exclusion." -> Theory + institutional + falsification defense.

### Inference objections
- "Standard errors are understated." -> Cluster correctly; show two-way / wild bootstrap.
- "This is a multiple-testing artifact." -> Adjust and report; show out-of-sample.

### Robustness objections
- "Does it survive an alternative measure / sample / specification?" -> It is already in the body or IA.
- "An alternative story explains this." -> A distinguishing test exists for each rival story.

### Contribution objections
- "Isn't this already known?" -> The positioning text answers it directly.

## Plan the campaign (after reports arrive)

- Sort each comment into: (a) substantive, must address with new analysis; (b) clarification, address in text; (c) genuine disagreement, push back respectfully with evidence.
- Identify the editor's emphasis — the comments the editor flags are the ones that decide the paper.
- Decide where new tests go (main text vs. Internet Appendix) before writing the response.
- Never pick a fight you cannot win with evidence; concede gracefully where the referee is right.

## Checklist

- [ ] You have written, in advance, the three hardest referee questions
- [ ] Each has an answer in the manuscript or Internet Appendix
- [ ] Identification, inference, robustness, and contribution objections each pre-empted
- [ ] Suggested/opposed referees considered within system rules
- [ ] After reports: each comment triaged (substantive / clarification / disagreement)
- [ ] Editor's emphasis identified and prioritized

## Anti-patterns

- Submitting without having refereed your own paper
- Ignoring the obvious endogeneity question and hoping it slips through
- Treating every referee comment as equally important and missing the editor's signal
- Arguing with a referee without new evidence
- Conceding a point that guts the contribution when a defense exists

## Output format

```
【Top-3 anticipated objections】[...]
【Pre-empted in text/IA】[...] | 【Still exposed】[...]
【Editor's emphasis】(if reports received)
【Comment triage】substantive[...] clarify[...] disagree[...]
【New tests location】main / IA
【Next】jfe-rebuttal (to draft the response)
```
