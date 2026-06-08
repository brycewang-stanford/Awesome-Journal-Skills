> **Illustrative teaching example.** The paper, setting, farm, model run, and **every number below are
> fictional** and exist only to demonstrate *Agricultural Systems* (AgSy) house style. No real-paper facts
> and **no real policy** are stated. Corresponding skills (this pack):
> [`agsy-writing-style`](../../skills/agsy-writing-style/SKILL.md),
> [`agsy-systems-framing-and-modeling`](../../skills/agsy-systems-framing-and-modeling/SKILL.md),
> [`agsy-data-and-model-evaluation`](../../skills/agsy-data-and-model-evaluation/SKILL.md),
> [`agsy-topic-selection`](../../skills/agsy-topic-selection/SKILL.md), and
> [`agsy-impact-and-implications`](../../skills/agsy-impact-and-implications/SKILL.md).

# Worked Example: An Agricultural Systems Abstract + Introduction (before → after)

This demonstrates the AgSy arc drawn **only from this pack's own skill files**:
**systems question (interaction / trade-off) → system boundary, components & hierarchical level →
model described and *independently evaluated*, not a black box → trade-offs across the farming system on
multiple objectives → scoped, decision-relevant implication** — with the journal front matter
(`agsy-writing-style`): an **abstract ≤ 250 words**, **Highlights**, and a **graphical abstract**.

The two skill tests this example is built to pass:

- **The "interaction or it isn't AgSy" test** (`agsy-systems-framing-and-modeling`):
  *"The result arises because component A interacts with component B such that ___; absent that
  interaction the system would behave like ___."*
- **The decision-relevance test** (`agsy-impact-and-implications`):
  *"Because of this analysis, [actor] should weigh [option] differently because the system trades off
  ___ against ___, under conditions ___."*

**Illustrative paper (fictional):** *"Re-timing the herd to the crop: a whole-farm analysis of
crop–livestock integration trade-offs under rainfall variability."* Fictional setting: a mixed
crop–livestock farm type in a semi-arid region, studied with a coupled crop process model and a
whole-farm bio-economic model. All quantities are invented.

---

## Before (a single-factor field write-up wearing a "systems" label)

> **Abstract.** Crop–livestock farms are important in semi-arid regions. We ran a field experiment
> comparing two calving dates over three seasons and measured pasture biomass and liveweight gain.
> Calving date B produced more liveweight gain than calving date A in two of three years. We also
> simulated wheat yield. The results show calving date B is better. This has implications for farmers and
> for policy on sustainable agriculture.
>
> **1. Introduction.** Crop–livestock systems have been studied extensively. Many models exist, including
> APSIM, DSSAT, and various whole-farm models. In this paper we use a whole-farm model to simulate a farm
> and report the output. Calving date is an important management decision. Section 2 reviews the
> literature, Section 3 describes the model, Section 4 presents results, and Section 5 concludes.

**What's wrong (against this pack's skills):**

- **No systems question.** It reports a single factor (calving date) measured one outcome at a time — the
  named off-fit anti-pattern in `agsy-topic-selection` ("a single-factor field trial with no
  interactions, model, or trade-off"). Nothing in the farm is shown to *interact*.
- **System never defined.** No boundary, components, or hierarchical level —
  `agsy-systems-framing-and-modeling` requires inside-vs-external-driver and field→farm→… stated early.
- **Model is a black box.** "We use a whole-farm model" with no version, calibration, or evaluation —
  `agsy-data-and-model-evaluation`'s first anti-pattern.
- **No trade-off.** It declares one option "better" on one objective; AgSy wants multiple objectives and
  the trade-off surfaced (`agsy-data-and-model-evaluation`: "scenario tables with no trade-offs").
- **Over-claims and invents policy.** "Implications for policy on sustainable agriculture" generalizes
  beyond the modelled system — `agsy-impact-and-implications` anti-pattern.
- **Front matter missing / abstract hides the result** — `agsy-writing-style` (no Highlights, no
  graphical abstract; abstract states no magnitudes, no trade-off).
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (AgSy arc — system, evaluated model, trade-offs, scoped decision)

> **Abstract.** *(fictional; ~210 words, ≤ 250)* Mixed crop–livestock farms in semi-arid regions are
> managed as **one system**, yet calving date, crop rotation, and feed reserves are usually optimised
> separately. **We ask how re-timing calving interacts with the cropping program to shift whole-farm
> trade-offs between profit, downside risk, and soil cover under rainfall variability** — an interaction a
> field trial on calving date alone cannot reveal. We couple a calibrated crop process model (driving
> grain yield and stubble) to a whole-farm bio-economic model spanning the field-to-farm levels, and
> evaluate the crop component against independent multi-season observations (1:1 fit reported: RMSE and
> modelling efficiency). Across 100 stochastic weather years we compare four management configurations on
> four objectives. Re-timing calving to follow stubble availability raises mean whole-farm gross margin by
> a modelled **9%** and cuts the worst-decile income shortfall by **18%**, but **lowers minimum ground
> cover by 6 percentage points** in dry years — a profit-versus-erosion-risk trade-off that is invisible
> when calving and cropping are tuned in isolation. The benefit arises because the regime synchronises
> animal feed demand with crop residue supply; absent that crop–livestock coupling the farm behaves like
> two independent enterprises and the gain disappears. We map the trade-off and identify the rainfall
> conditions under which a farm manager should, or should not, adopt the re-timed regime.

> **Highlights** *(fictional)*
> - Calving date and cropping are analysed as **one interacting whole-farm system**, not separately.
> - A **calibrated, independently evaluated** crop–livestock model (1:1 fit, sensitivity, 100 stochastic
>   years) drives the analysis.
> - Re-timing calving raises modelled gross margin **9%** and cuts worst-decile shortfall **18%**…
> - …but **reduces dry-year ground cover 6 pp** — an explicit **profit vs. erosion-risk trade-off**.
> - The gain exists **only** through crop-residue–feed-demand coupling; it vanishes if the enterprises
>   are decoupled.

> **Graphical abstract** *(fictional, described):* a conceptual system diagram (crop ↔ residue ↔ feed ↔
> herd, with rainfall as an external driver) beside a **trade-off plot** of whole-farm gross margin
> against minimum ground cover, the four configurations marked on the frontier.

> **1. Introduction.** *(fictional)* On a mixed crop–livestock farm, the herd and the cropping program
> are not separate businesses: crop residues feed animals, animals return nutrients and affect ground
> cover, and both compete for the same land, labour, and a single rainfall signal. **We ask how the
> timing of calving interacts with the cropping program to move the whole farm's trade-offs between
> profit, downside risk, and soil protection — and under which rainfall conditions a manager should
> re-time the herd.** *(systems question stated first, as an interaction and a trade-off.)*
>
> A field trial that varies calving date alone cannot answer this, because the payoff to any calving date
> depends on what the crop is doing — how much stubble is on the ground and when. We therefore treat the
> **farm** as the system: components are crop, soil cover, residues, the herd, and farm finances;
> rainfall and prices are external drivers; we model the **field and farm** levels and let field-scale
> residue production constrain farm-scale feed. *(system boundary, components, hierarchical levels —
> `agsy-systems-framing-and-modeling`.)*
>
> We couple a crop process model to a whole-farm bio-economic model. We do not treat the model as a black
> box: we report its version, what was calibrated against which seasons, and we **evaluate the crop
> component on independent data** (observed-vs-simulated, RMSE and modelling efficiency), then run a
> sensitivity analysis and propagate weather uncertainty through 100 stochastic years. *(model described
> and independently evaluated — `agsy-data-and-model-evaluation`.)*
>
> The central finding is a **trade-off, not a winner**: re-timing calving to follow stubble availability
> raises modelled whole-farm gross margin and cuts downside income risk, but lowers dry-year ground cover.
> The benefit **arises because** synchronising feed demand with crop-residue supply links the two
> enterprises; **absent that interaction** the farm behaves like two independent enterprises and the gain
> disappears. *(interaction test satisfied explicitly.)*
>
> The result is decision-relevant and **scoped**: a manager of this farm type should weigh the re-timed
> regime differently because the system **trades profit and risk-reduction against erosion risk**, and
> only **in the wetter part of the rainfall range** does the trade-off favour adoption — outside that
> range, and beyond this farm type and these soils, we do not extend the claim. *(decision-relevance test;
> no invented policy — `agsy-impact-and-implications`.)*
>
> Section 2 describes the system and the coupled model; Section 3 reports the evaluation and the
> trade-off analysis; Section 4 discusses the management decision and its scope. *(brief roadmap.)*

---

## Why the "after" meets the AgSy bar

Mapped to this pack's skill checklists:

- **A genuine systems question, stated first** — an *interaction* (calving × cropping) and a *trade-off*
  (profit / risk / ground cover), clearing the `agsy-topic-selection` fit test rather than reporting a
  single factor.
- **System defined early** — boundary (farm), components, external drivers, and hierarchical levels
  (field → farm) appear in the introduction (`agsy-systems-framing-and-modeling`).
- **Model evaluated, not asserted** — version, calibration-vs-evaluation split, **independent**
  observed-vs-simulated fit (RMSE, modelling efficiency), sensitivity, and propagated uncertainty over
  100 stochastic years (`agsy-data-and-model-evaluation`; no "single tuned run").
- **Trade-offs across the farming system** — four configurations on four objectives, the profit-vs-cover
  tension made explicit on a frontier, not collapsed to "B is best."
- **The interaction test is passed in one sentence** — the gain exists *only* through residue–feed
  coupling and vanishes if the enterprises are decoupled.
- **Scoped, honest implication; no invented policy** — the recommendation is tied to rainfall conditions
  and the farm type, and explicitly does not transfer (`agsy-impact-and-implications`).
- **Front matter present** — abstract ≤ 250 words that *states* the result and the trade-off, Highlights,
  and a graphical abstract pairing a system diagram with a trade-off plot (`agsy-writing-style`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified** *Agricultural
> Systems* papers whose framing executes this arc, and [`../external_tools.md`](../external_tools.md) for
> the process, whole-farm, bio-economic, and evaluation tooling referenced above. (No econometrics code
> kit is vendored in this pack — see [`../README.md`](../README.md).)
