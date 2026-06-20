---
name: ier-topic-selection
description: Use when deciding whether a question is broad and rigorous enough for an International Economic Review (IER) manuscript, and which branch (theory / structural-macro / econometric method / applied micro) frames it. Tests fit and scope; it does not invent evidence or citations.
---

# Topic Selection (ier-topic-selection)

## When to trigger

- You have a result but are unsure it is *general-interest* — would a macro theorist and an applied micro reader both see why it matters?
- The question feels like a field-journal question (a single applied estimate, a narrow extension) and you want to know if it clears IER's broad-rigor bar
- The contribution is a model with a clean result, and you want to confirm theory is welcome here (it is — IER tilts theory/structural)
- The team is choosing between IER, Econometrica/QE, a top-5, and a field journal and needs the boundary drawn

## What IER actually rewards

IER was founded in 1960 to be a **forum for modern quantitative economics**, and its center of gravity is *rigor and generality* over topical novelty. The papers that fit are the ones where the contribution is a **method, a model, or a tight model-to-evidence link** that travels beyond the immediate application. Sort your question against these archetypes before going further:

| Archetype | What makes it an IER paper | What gets it desk-rejected here |
|-----------|----------------------------|---------------------------------|
| Pure / applied theory | A new result with a clean proof and load-bearing assumptions made explicit; comparative statics that teach something general | A model that only re-derives a known result, or a toy with no general lesson |
| Structural / quantitative macro | A model disciplined by data whose mechanism and counterfactual are the point | A calibration with an undefended elasticity driving the headline number |
| Econometric theory / method | A new estimator/test with asymptotics AND finite-sample evidence, beating a clear incumbent | A method searching for a problem, or a marginal tweak with no practical gain |
| Applied micro (causal) | A credible design whose answer speaks to a general mechanism, not one institution | A clean DID whose interest is purely local/policy and not generalizable |

The decisive question is not "is this correct?" but "**does the rigor buy generality?**" An IER referee forgives a narrow empirical setting if the mechanism generalizes, and forgives an abstract model if the result is genuinely new. They do not forgive a paper that is merely competent and local.

### Where IER sits among the siblings (so you don't mis-target)

- **vs. Econometrica / Quantitative Economics** (Econometric Society): those are method-first and membership-gated; IER is Penn–Osaka-owned, broad/theory-leaning, with a flat US$150 fee and an Editorial Express portal. If your paper's entire value is the theorem or estimator with no broad payoff, it may be an ES paper — at IER the general-interest case must be visible.
- **vs. the top-5** (AER/QJE/JPE/REStud/Eca): IER rewards rigor and generality but does not require the topical "importance" a top-5 desk demands. A deep, correct, general result that a top-5 would call "not splashy enough" is squarely an IER paper.
- **vs. field journals** (JIE, J. of Econometrics, etc.): IER wants the result to travel beyond one field. If you can name only one narrow audience, it is a field paper.

### Worked example (illustrative)

A draft estimates the pass-through of a specific country's import tariff to local prices — a clean, well-identified applied result. As stated it is a field-journal (trade/IO) paper: the interest is local. The IER version reframes the contribution as a *general mechanism* — "how incomplete pass-through depends on market structure, identified by tariff variation" — and shows a second reader segment (IO theorists) would care because the mechanism is portable. Same data, different contribution: the rigor now buys generality, which is what moves it from a field outlet to IER.

## How to sharpen the question

1. State the contribution in one sentence that names the *general* object (a parameter, a theorem, an estimator, a mechanism) — not the dataset or the country.
2. Name the two reader segments who must both care (e.g., trade theorists + IO empiricists). If you can only name one narrow segment, it is a field-journal paper.
3. Identify the single load-bearing assumption or identifying source the whole result rests on, and ask whether you can defend it to a skeptic.
4. Decide the branch (theory / structural / method / applied) — this fixes which skill is your real first bottleneck via `ier-workflow`.
5. Hand off to `ier-literature-positioning` if it passes, or back to `ier-workflow` if the branch is still unclear.

### Three questions that decide fit before you write

Run these before committing the topic; if any answer is "no," reroute via `ier-workflow` rather than polishing a misfit.

1. **Generality test.** If I strip the specific dataset/country/institution, does a result remain that another economist could use? If nothing survives the stripping, the contribution was the setting, and the setting is not enough for IER.
2. **Two-referee test.** Can I name a plausible referee from a *different* subfield who would find the paper interesting on its own terms? IER's broad readership means a paper that only one narrow community can referee is a poor fit.
3. **Sibling test.** Is there a journal where this paper would be a *more* natural fit — Econometrica/QE if it is pure method, a field journal if it is field-local? If yes and the IER-specific edge is thin, name the edge explicitly or retarget.

These are not box-ticking; each maps to a real desk-rejection reason. The generality test catches field-local papers; the two-referee test catches papers too specialized for a general-interest board; the sibling test catches papers that would be stronger submissions elsewhere.

## Checklist

- [ ] The contribution is stated as a general object (theorem / parameter / estimator / mechanism), not as a dataset or setting
- [ ] At least two distinct IER reader segments would care; the paper is not single-field-local
- [ ] The rigor visibly buys generality — the lesson survives outside the immediate application
- [ ] The branch is named, so the real first bottleneck is identified
- [ ] If empirical, the mechanism is generalizable, not just the policy estimate
- [ ] Sibling boundary is drawn: this is not better placed at Econometrica/QE or a field journal
- [ ] Process facts cited (fee, length, portal) are from `resources/official-source-map.md` or marked 待核实

### What "International" does and does not mean

A recurring misreading: authors assume IER wants cross-country or trade topics because of the name. It does not. "International" denotes the **Penn–Osaka ownership** (the partnership behind the Klein Lectures), not a field scope. A purely domestic macro-theory or applied-micro paper is exactly as welcome as a trade paper, provided the rigor buys generality. Do not bend a topic toward an international angle to "fit the name" — fit the *standard* (rigor + generality), which is what the editorial board actually applies.

## Anti-patterns

- Pitching a clean-but-local applied result as if novelty of setting were the contribution — IER prizes generality, not a fresh dataset
- Sending a method-first econometrics paper to IER when it is really an Econometric Society (Econometrica/QE) paper — IER takes method, but the broad-interest case must be visible
- Assuming "International" means the topic must be cross-country — it names the Penn–Osaka ownership, not the field
- Treating a marginal model extension as general-interest because it is formally correct

## Output format

```text
【Journal】International Economic Review
【Skill】ier-topic-selection
【Branch】theory / structural-macro / econometric-method / applied-micro
【Contribution (general object)】one sentence naming the theorem/parameter/estimator/mechanism
【Two reader segments】who must both care
【Load-bearing assumption / identifying source】the thing the result rests on
【Sibling boundary】why IER and not Econometrica/QE / top-5 / field journal
【Verdict】pass / revise / reroute
【Source status】verified / 待核实
【Next skill】ier-literature-positioning
```
