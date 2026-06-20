---
name: ecj-referee-strategy
description: Use when running a pre-submission pre-mortem on a The Economic Journal (EJ) manuscript to anticipate the broad-interest, identification, and mechanism objections a demanding general-interest referee will raise. Builds the threat list and pre-empts it; it does not write the R&R response (see ecj-rebuttal).
---

# Referee Strategy & Pre-Mortem (ecj-referee-strategy)

## When to trigger

- Identification, model, and robustness are in place and you want to harden the paper before submitting
- You want to anticipate the report rather than react to it
- You sense a likely objection but have not addressed it in the text
- You are choosing how to frame the contribution to survive a demanding general-interest referee

## How EJ referees read

EJ referees read the paper as an **economic argument for a broad audience** and probe two things: is it credible, and is it of **broad interest** to economists at large? The prototypical EJ referee asks "so what — why should the wider profession care?" as hard as "is this identified?". They are unimpressed by a clean coefficient with no economic meaning or no general relevance, and they will name the alternative mechanism or the over-claimed generality. EJ review is **single-blind** (referees know who you are; you do not know them; verified 2026-06-20), so do not anonymize. Anticipating these objections is worth more than any extra robustness table, because a single unanswered first-order objection — especially "this is too narrow for EJ" — sinks the paper.

## The objection taxonomy (pre-empt each in the text)

1. **"Too narrow / not of broad interest."** — A result only one subfield would read. *Pre-empt:* `ecj-topic-selection` / `ecj-literature-positioning` — argue the general lesson and external relevance explicitly.
2. **"Where is the economics?"** — A reduced-form result with no model/mechanism. *Pre-empt:* `ecj-theory-model` — state the mechanism and the prediction it tests.
3. **"Your mechanism vs. the obvious alternative."** — A rival economic story produces the same sign. *Pre-empt:* `ecj-robustness` — a discriminating test.
4. **"Selection / endogeneity / weak design."** — Treatment or sample is endogenous; TWFE on staggered timing. *Pre-empt:* `ecj-identification` — defend the assumption, show falsification, use a modern estimator.
5. **"What identifies the parameter?"** (structural) — *Pre-empt:* explicit "what identifies what" + untargeted-moment validation.
6. **"Over-claimed generality."** — the headline asserts external validity the design cannot support. *Pre-empt:* bound the claim to what the evidence licenses (`ecj-robustness`).
7. **"Hard to read / exposition."** — a generalist gets lost. *Pre-empt:* `ecj-writing-style` — clear exposition is part of the EJ bar, not optional polish.

## Pre-mortem procedure

- Write the referee report you fear, in their voice, listing the three objections most likely to trigger a reject.
- For each, decide: fixable in text now (do it), needs new analysis (do it or scope it), or a genuine limitation (state it honestly and bound its damage).
- Identify the **one** first-order objection that would sink the paper — at EJ this is frequently "too narrow" or "no mechanism" — and make sure the manuscript answers it before a referee has to ask.
- Suggesting referees / handling COIs: name scholars who know the literature and would engage fairly; note conflicts honestly — the single-blind portal will flag obvious co-author/advisor ties.

## Checklist

- [ ] "Too narrow for EJ" pre-empted with an explicit broad-interest / general-lesson argument
- [ ] "Where is the economics?" answered by an explicit mechanism/model
- [ ] The leading rival mechanism named and tested against
- [ ] Selection/endogeneity threat defended with a falsification test; modern estimator where needed
- [ ] (Structural) parameter identification made transparent
- [ ] Generality claims bounded to what the evidence supports
- [ ] Exposition checked so a generalist can follow the argument
- [ ] The single most dangerous objection identified and pre-empted in the text

## Anti-patterns

- Submitting a narrow result and hoping the referee overlooks the broad-interest bar
- Anonymizing for a single-blind journal, or suggesting referees with a conflict the portal will catch
- A robustness section that never tests the *leading* rival mechanism
- Assuming broad importance instead of demonstrating it
- Hiding a known limitation rather than bounding it (referees find it anyway)
- Treating exposition as cosmetic when at EJ it is part of the decision

## Output format

```
【Feared report】the 3 objections most likely to trigger reject
【First-order threat】the single objection that would sink it (often "too narrow" / "no mechanism")
【Pre-empt plan】per objection: fix-in-text / new-analysis / state-as-limitation
【Broad-interest + rival-mechanism status】addressed? [y/n]
【Exposition pass】a generalist can follow it? [y/n]
【Next】ecj-submission
```
