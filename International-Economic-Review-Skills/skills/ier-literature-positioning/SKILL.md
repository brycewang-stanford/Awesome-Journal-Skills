---
name: ier-literature-positioning
description: Use when staking an International Economic Review (IER) manuscript's contribution against the frontier and against sibling journals (Econometrica/QE, the top-5, field journals). Sharpens the gap and the delta; it does not invent citations.
---

# Literature Positioning (ier-literature-positioning)

## When to trigger

- The intro lists prior work but never says what *this* paper adds that none of them did
- A coauthor cannot state, in one sentence, the delta over the single closest paper
- The draft reads like a strong field-journal paper and you need the general-interest claim to be legible
- You are unsure how to position against the obvious sibling (Econometrica/QE) so the desk editor sees why it is here, not there

## The IER positioning logic

At IER the contribution is almost always **methodological or model-level generality**, so positioning is not "we study X in a new setting" — it is "the existing tool/result fails or is silent *here*, and ours is the first that is both correct and general." Build the position in three layers, from frontier down to the load-bearing delta:

1. **Frontier statement.** Name the 3–6 papers that define the current best answer. For a structural paper, name the canonical model you generalize or discipline; for a method paper, name the incumbent estimator; for theory, name the result you sharpen or overturn.
2. **The gap that matters.** State precisely what the frontier cannot do — a knife-edge assumption, an estimator that breaks under realistic conditions, a mechanism left unmodeled. The gap must be *consequential*, not cosmetic.
3. **Your delta, made falsifiable.** One sentence: "We are the first to [result] under [weaker/realistic condition], which [the frontier] could not." A referee should be able to check the claim.

### Drawing the sibling boundaries (this is where IER papers get mis-filed)

| Confused with | How IER differs | The positioning move |
|---------------|-----------------|----------------------|
| **Econometrica / QE** (Econometric Society) | IER is Penn–Osaka-owned, broad/theory-leaning, with a flat fee and Editorial Express portal; ES journals are method-first and membership-gated | If the paper's whole value is the theorem/estimator with no broad application, it may belong at ES — make the general-interest payoff explicit to justify IER |
| **Top-5 (AER/QJE/JPE/REStud/Eca)** | IER prizes rigor + generality but does not require the broad "importance"/splash a top-5 desk demands | Position on *depth and correctness*, not on topical importance or policy timeliness |
| **Field journals** (JIE, J. Econometrics, etc.) | IER wants the result to travel beyond one field/application | Show the second reader segment; convert a field finding into a general mechanism |
| **The Economic Journal / EER** | IER is more theory/structural and more rigor-gated | Emphasize the formal contribution, not breadth of coverage |

### Worked example (illustrative)

A structural labor paper positions itself as "the first dynamic model of occupational choice with X." A referee replies that two recent papers already model X. The weak fix adds more citations. The IER fix re-states the delta at the *capability* level: "prior dynamic models impose stationarity of the choice set; we are the first to allow the choice set to evolve, which is what generates the non-monotone life-cycle pattern in the data." Now the gap is consequential (stationarity was the knife-edge) and the delta is falsifiable (a referee can check whether prior models allowed an evolving choice set). The literature is no longer a list; it is the backdrop against which one capability is shown to be new.

### Common positioning failure and its fix

The most frequent IER positioning failure is a "first to study X in setting Y" claim, where Y is just a new dataset or country. That is a field-journal frame. The fix is always the same: convert the *setting* novelty into a *mechanism* or *method* novelty, then name the second reader segment for whom the mechanism (not the setting) is the news. If you cannot make that conversion, the paper is correctly positioned at a field journal, and `ier-topic-selection` should have caught it.

### Positioning by branch (the gap looks different in each)

- **Theory:** the gap is a result the frontier proves only under a restrictive assumption, or fails to prove at all. Your delta is "we prove it under weaker conditions" or "we show their result reverses when assumption A is relaxed."
- **Structural / quantitative:** the gap is a mechanism the canonical model omits, or a discipline (untargeted moments, external validity) the frontier never imposed. Your delta is "our model matches moments theirs cannot" — and you show which.
- **Econometric method:** the gap is a setting where the incumbent estimator is inconsistent, inefficient, or infeasible. Your delta is a head-to-head where yours wins, with finite-sample evidence.
- **Applied micro:** the gap is a credibility or generality limit in prior designs. Your delta is a cleaner design or a mechanism that travels — not just a new sample.

In every branch the discipline is the same: the gap must be something the frontier *could not do*, stated so a referee can verify it, and the delta must be the *general* lesson, not the local finding.

## Checklist

- [ ] The 3–6 frontier papers are named and the closest single paper is identified
- [ ] The gap is consequential and stated in terms of an assumption, condition, or capability the frontier lacks
- [ ] The delta is one falsifiable sentence a referee can check ("first to X under weaker Y")
- [ ] The general-interest payoff is explicit, so the Econometrica/QE boundary is justified
- [ ] Positioning rests on rigor + generality, not on topical importance (that's a top-5 frame)
- [ ] Every cited paper is real and correctly attributed (no invented prior work)
- [ ] Process/scope claims trace to `resources/official-source-map.md` or are marked 待核实

### Positioning a theory result that "feels" already known

A frequent trap for theory papers: the result feels intuitive, so a referee suspects it is folklore. Positioning rescues it by locating the *exact* prior statement closest to yours and showing what it lacked — a proof, a general class, a stated condition, or a regime. "The intuition appears in [X], but it was never proved; [Y] proved a special case under log utility; we establish it for the full class P and identify the regime where it reverses." This converts "isn't this obvious?" into "this was believed but never established," which is a genuine IER contribution.

## Anti-patterns

- A "literature review" that summarizes papers without ever stating the delta over the closest one
- Claiming a gap that is really a different question (moving the goalposts instead of clearing the bar)
- Positioning on policy relevance or topical importance — that is a top-5 desk pitch, not an IER one
- Inflating the delta past what the result supports; an IER referee will check the "first to" claim
- Citing a working paper or one's own prior work as if it settled the frontier

## Referee pushback mapped to the positioning fix

- *"This has been done before."* → Re-state the delta at the capability level ("first to do X under weaker Y"), not the topic level; show the cited prior work could not do it.
- *"Why is this in IER and not a field journal?"* → Name the second reader segment and the general mechanism; convert the setting-novelty into a method/mechanism-novelty.
- *"The contribution is incremental."* → Identify the consequential boundary your result moves (the knife-edge it removes), and state it as the headline.
- *"You ignore the closest paper."* → Cite it, state the precise delta over it, and never let a working paper or your own prior work stand in for the frontier.

## Output format

```text
【Journal】International Economic Review
【Skill】ier-literature-positioning
【Frontier】3–6 papers defining the current best answer
【Closest paper】the single nearest prior work
【Gap that matters】the consequential assumption/condition/capability the frontier lacks
【Delta (falsifiable)】"first to ___ under ___, which ___ could not"
【General-interest payoff】why this travels (justifies IER over ES/field)
【Sibling boundary】why not Econometrica/QE / top-5 / field journal
【Verdict】pass / revise / reroute
【Next skill】ier-theory-model (theory/structural) or ier-identification (applied)
```
