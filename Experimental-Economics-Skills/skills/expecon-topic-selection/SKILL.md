---
name: expecon-topic-selection
description: Use when deciding whether a question is a method-defined fit for an Experimental Economics (ExpEcon) manuscript and which treatment contrast to build it around. Frames the fit decision; it does not invent results or citations.
---

# Topic Selection (expecon-topic-selection)

## When to trigger

- You have an interesting economic question but are unsure an experiment is the right tool — or whether *this* journal is the right home for it
- The draft reads topic-first ("a paper about charitable giving") rather than method-first ("a design that isolates warm-glow from social-image motives")
- You must decide *before* collecting data whether to pre-register, run a Registered Report, or pursue a replication
- The paper could plausibly land at JEBO, GEB, AEJ: Micro, or JESA and you need to pick deliberately

## The fit decision: method first, topic second

Experimental Economics is the **ESA method flagship**. The editors do not ask "is this topic important?" so much as "is this **the cleanest experiment** that could answer this question, and does the design *itself* teach the field something?" Three questions decide fit:

1. **Is the object causal and behavioral?** The unit of contribution is a **treatment effect produced by experimental control**, not an observed correlation or a calibrated structural object. If your answer lives in field-survey data, you are at an applied journal, not here.
2. **Is the design the contribution, or merely a delivery vehicle?** Papers that win at ExpEcon either (a) build a *novel, decisive treatment contrast* that prior work could not run, or (b) advance the **methodology of experimentation** (a better elicitation, a control that removes a confound, evidence on how a procedure biases results). A standard dictator game with a new label rarely clears the bar.
3. **Can it pass the two gates from day one?** Real **salient incentives** and the **no-deception** norm are not editorial preferences; they are entry conditions. If the question can only be answered by deceiving subjects or with hypothetical stakes, redesign or send it elsewhere.

## Choosing the treatment contrast (this is where the paper is won)

The center of an ExpEcon paper is the **minimal pair**: two conditions identical except for the one thing your hypothesis is about. Spend your design budget here.

- Strip the contrast to a *single* manipulated dimension; a treatment that changes payoffs *and* framing *and* matching identifies nothing.
- Pre-commit to the **primary outcome and primary comparison** in a pre-analysis plan (AEA RCT Registry / OSF / AsPredicted). For high-stakes or surprising claims, consider a **Registered Report**: in-principle acceptance before data collection insulates a clean null from publication bias and is increasingly welcomed in the ESA ecosystem (检索于 2026-06；以官网为准).
- Decide matching (partner vs. stranger), information, and one-shot vs. repeated *now* — these are identification choices, not implementation details.

## Sibling boundary — pick the right home deliberately

| Venue | What it rewards | Send there instead when… |
|-------|-----------------|--------------------------|
| **JEBO** | broad behavioral/organizational questions, method-agnostic | the topic, not the design, is the contribution; you need deception |
| **GEB** | game-theoretic *theory* | the experiment merely illustrates a theorem |
| **AEJ: Micro** | applied micro where an experiment supports a wider claim | the headline is an economic phenomenon, the experiment one leg |
| **JESA** | short-format ESA work: replications, null results, software, comments | the paper is a brief note, not a full design paper |

## Deciding the experiment *type* (it changes everything downstream)

The same question can be a lab, lab-in-the-field, or field experiment, and the choice fixes your later bottlenecks:

| Type | Buys you | Costs you | Choose when |
|------|----------|-----------|-------------|
| **Lab** | maximal control, clean minimal pairs, cheap iteration | external validity questions (often student pool) | the mechanism needs tight control to isolate |
| **Lab-in-the-field** | a relevant population with much control retained | recruitment/logistics, some control loss | the population is the point (farmers, traders, CEOs) |
| **Field** | behavior in situ, strong external validity | partial control, attrition, often costlier | the real-world stakes are the contribution |

Lab control is your comparative advantage at this journal; do not give it up unless the population or the in-situ behavior *is* the contribution.

## Checklist

- [ ] The contribution is stated as a **treatment effect / design advance**, not a topic
- [ ] The minimal-pair contrast manipulates exactly one dimension
- [ ] Both gates clear at the idea stage: salient incentives feasible; **no deception required**
- [ ] Pre-registration / Registered Report / replication status decided before data collection
- [ ] A one-line reason this belongs at ExpEcon and not JEBO/GEB/AEJ: Micro/JESA
- [ ] Primary outcome and primary comparison named before any results exist
- [ ] Experiment type (lab / lab-in-field / field) chosen for a stated reason

## The "could you publish a clean null?" test

A useful litmus for ExpEcon fit: imagine your treatment effect comes out **exactly zero**. Is the paper still publishable? If yes — because the design is decisive, the hypotheses were pre-registered, and a null adjudicates between behavioral models — you have a true method-defined contribution. If a null would be unpublishable because the paper rests entirely on getting a "surprising positive," you are leaning on the result, not the design, and you risk a publication-bias incentive to p-hack. The flagship (and especially the Registered Report track) values designs whose answer matters either way. Build the question so the null is informative.

## Anti-patterns

- A "topic paper" with an experiment bolted on, where the design teaches nothing new
- A treatment that varies several things at once, so no single effect is identified
- Discovering only after data collection that the design needed deception to work
- Choosing the journal by impact factor rather than by method fit
- Treating a brief replication or software note as a full ExpEcon design paper (that is JESA)

## Worked vignette (illustrative)

A team has "a paper on whether social media reduces cooperation." Topic-first, and unidentifiable as stated. Reframing method-first: design a repeated public-goods game where one treatment injects a between-round "feed" of (real, not fabricated — gate!) peer messages and the control does not. Now the contribution is a *treatment effect of peer messaging on contributions*, the minimal pair manipulates only the feed, incentives are real, no deception is needed (messages are genuine), and a pre-registered primary comparison (mean contribution, Feed vs. NoFeed, at the matching-group level) exists before any data. The vague topic became a clean ExpEcon design.

## Output format

```text
【Journal】Experimental Economics (ESA method flagship)
【Skill】expecon-topic-selection
【Verdict】fit / reframe / reroute
【The contribution】treatment effect or design/method advance (one sentence)
【Experiment type】lab / lab-in-field / field + reason
【Minimal-pair contrast】the single manipulated dimension
【Gate check】incentives salient? no deception? [Y/N]
【Pre-reg status】PAP / Registered Report / replication / none-yet
【Why here not sibling】JEBO/GEB/AEJ:Micro/JESA reason
【Next skill】expecon-literature-positioning
```
